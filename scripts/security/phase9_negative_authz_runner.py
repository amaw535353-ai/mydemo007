#!/usr/bin/env python3
"""Bounded Phase 9 authorization negative-test runner.

Safety properties:
- loopback HTTP(S) targets only;
- dry-run unless PHASE9_RUN=1;
- sequential requests only;
- <= 50 cases;
- timeout capped at 5 seconds;
- response body capped at 1 MiB;
- redirects are not followed;
- credentials and raw response bodies are never written to results.

All fixtures must be synthetic and belong to the authorized local Onyx lab.
"""

from __future__ import annotations

import hashlib
import ipaddress
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MAX_CASES = 50
MAX_RESPONSE_BYTES = 1024 * 1024
ALLOWED_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE"}
TEMPLATE_RE = re.compile(r"\{([A-Z0-9_]+)\}")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        return None


@dataclass(frozen=True)
class Case:
    case_id: str
    source: str
    description: str
    mode: str  # deny | allow | scoped_marker | review
    credential_prefix: str | None = None
    method: str = "GET"
    method_env: str | None = None
    path: str | None = None
    path_env: str | None = None
    body_env: str | None = None
    extra_headers_json_env: str | None = None
    required_envs: tuple[str, ...] = ()
    success_statuses: tuple[int, ...] = (200,)
    in_scope_marker_env: str | None = None
    out_scope_marker_env: str | None = None
    review_reason: str | None = None


@dataclass
class Result:
    case_id: str
    source: str
    disposition: str
    description: str
    method: str | None = None
    path: str | None = None
    http_status: int | None = None
    response_bytes: int | None = None
    response_sha256: str | None = None
    assertions: dict[str, Any] = field(default_factory=dict)
    note: str | None = None
    timestamp_utc: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


def _truthy(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes"}


def _timeout() -> float:
    raw = os.environ.get("PHASE9_TIMEOUT_SECONDS", "5")
    try:
        value = float(raw)
    except ValueError:
        value = 5.0
    return max(0.5, min(value, 5.0))


def _base_url() -> str:
    return os.environ.get("PHASE9_BASE_URL", "http://127.0.0.1:8080").rstrip("/")


def _assert_loopback_base(url: str) -> None:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise SystemExit("REFUSED: PHASE9_BASE_URL must use http or https")
    if not parsed.hostname:
        raise SystemExit("REFUSED: PHASE9_BASE_URL has no hostname")

    host = parsed.hostname
    if host == "localhost":
        return
    try:
        ip = ipaddress.ip_address(host)
    except ValueError as exc:
        raise SystemExit(
            "REFUSED: PHASE9_BASE_URL must resolve syntactically to localhost/loopback; "
            "DNS hostnames other than exact 'localhost' are not allowed"
        ) from exc
    if not ip.is_loopback:
        raise SystemExit("REFUSED: PHASE9_BASE_URL is not loopback")


def _expand(value: str) -> tuple[str | None, list[str]]:
    missing: list[str] = []

    def repl(match: re.Match[str]) -> str:
        name = match.group(1)
        env_value = os.environ.get(name)
        if env_value is None or env_value == "":
            missing.append(name)
            return match.group(0)
        return env_value

    expanded = TEMPLATE_RE.sub(repl, value)
    return (None if missing else expanded), missing


def _case_method(case: Case) -> tuple[str | None, list[str]]:
    method = case.method
    missing: list[str] = []
    if case.method_env:
        method = os.environ.get(case.method_env, "").strip().upper()
        if not method:
            missing.append(case.method_env)
    method = method.upper()
    if missing:
        return None, missing
    if method not in ALLOWED_METHODS:
        raise ValueError(f"unsupported HTTP method {method!r} for {case.case_id}")
    return method, []


def _case_path(case: Case) -> tuple[str | None, list[str]]:
    if case.path_env:
        raw = os.environ.get(case.path_env, "")
        if not raw:
            return None, [case.path_env]
    elif case.path is not None:
        raw = case.path
    else:
        return None, ["<path>"]

    expanded, missing = _expand(raw)
    if missing or expanded is None:
        return None, missing
    parsed = urllib.parse.urlparse(expanded)
    if parsed.scheme or parsed.netloc or not expanded.startswith("/"):
        raise ValueError(
            f"unsafe path for {case.case_id}: case paths must be relative and start with '/'"
        )
    return expanded, []


def _credentials(case: Case) -> tuple[dict[str, str], list[str]]:
    if not case.credential_prefix:
        return {}, []

    auth = os.environ.get(f"{case.credential_prefix}_AUTH", "")
    cookie = os.environ.get(f"{case.credential_prefix}_COOKIE", "")
    if not auth and not cookie:
        return {}, [
            f"{case.credential_prefix}_AUTH or {case.credential_prefix}_COOKIE"
        ]

    headers: dict[str, str] = {}
    if auth:
        headers["Authorization"] = auth
    if cookie:
        headers["Cookie"] = cookie
    return headers, []


def _extra_headers(case: Case) -> tuple[dict[str, str], list[str]]:
    if not case.extra_headers_json_env:
        return {}, []
    raw = os.environ.get(case.extra_headers_json_env, "")
    if not raw:
        return {}, [case.extra_headers_json_env]
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"{case.extra_headers_json_env} must be a JSON object"
        ) from exc
    if not isinstance(parsed, dict) or not all(
        isinstance(k, str) and isinstance(v, str) for k, v in parsed.items()
    ):
        raise ValueError(f"{case.extra_headers_json_env} must map strings to strings")
    return parsed, []


def _body(case: Case) -> tuple[bytes | None, list[str]]:
    if not case.body_env:
        return None, []
    raw = os.environ.get(case.body_env, "")
    if not raw:
        return None, [case.body_env]
    try:
        json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{case.body_env} must contain valid JSON") from exc
    return raw.encode("utf-8"), []


def _missing_required(case: Case) -> list[str]:
    return [name for name in case.required_envs if not os.environ.get(name)]


def _request(
    base_url: str,
    method: str,
    path: str,
    headers: dict[str, str],
    body: bytes | None,
) -> tuple[int, bytes]:
    url = base_url + path
    req_headers = {
        "Accept": "application/json",
        "User-Agent": "phase9-negative-authz-runner/1.0",
        **headers,
    }
    if body is not None:
        req_headers.setdefault("Content-Type", "application/json")

    request = urllib.request.Request(
        url=url,
        data=body,
        headers=req_headers,
        method=method,
    )
    opener = urllib.request.build_opener(NoRedirect())

    try:
        with opener.open(request, timeout=_timeout()) as response:
            status = int(response.status)
            data = response.read(MAX_RESPONSE_BYTES + 1)
    except urllib.error.HTTPError as exc:
        status = int(exc.code)
        data = exc.read(MAX_RESPONSE_BYTES + 1)
    except urllib.error.URLError as exc:
        raise RuntimeError(f"request failed: {exc.reason}") from exc

    if len(data) > MAX_RESPONSE_BYTES:
        raise RuntimeError("response exceeded 1 MiB safety ceiling")
    return status, data


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _evaluate(case: Case, status: int, data: bytes) -> tuple[str, dict[str, Any], str | None]:
    assertions: dict[str, Any] = {}

    if status >= 500:
        return "FAIL", {"server_error": True}, "unexpected 5xx response"

    if case.mode == "deny":
        if status in {401, 403}:
            return "PASS", {"deny_status": True}, None
        if status == 404:
            return (
                "REVIEW",
                {"deny_status": "concealed-or-not-found"},
                "404 requires a paired positive control to prove route/resource validity",
            )
        if 200 <= status < 300:
            return "FAIL", {"unexpected_success": True}, "request succeeded but DENY was required"
        return "REVIEW", {"unexpected_status": status}, "non-standard denial requires review"

    if case.mode == "allow":
        if status in case.success_statuses:
            return "PASS", {"success_status": True}, None
        return "FAIL", {"success_status": False}, "authorized control did not reach expected status"

    if case.mode == "scoped_marker":
        if status != 200:
            return "REVIEW", {"status_200": False}, "scoped-read fixture did not produce a 200 response"
        text = data.decode("utf-8", errors="replace")
        in_name = case.in_scope_marker_env
        out_name = case.out_scope_marker_env
        if not in_name or not out_name:
            return "REVIEW", {}, "marker configuration missing"
        in_marker = os.environ[in_name]
        out_marker = os.environ[out_name]
        in_present = in_marker in text
        out_present = out_marker in text
        assertions["in_scope_marker_present"] = in_present
        assertions["out_of_scope_marker_absent"] = not out_present
        if out_present:
            return "FAIL", assertions, "out-of-scope synthetic marker was disclosed"
        if not in_present:
            return "REVIEW", assertions, "in-scope marker absent; fixture/policy requires review"
        return "PASS", assertions, None

    if case.mode == "review":
        return (
            "REVIEW",
            {"request_completed": True},
            case.review_reason or "manual evidence/policy review required",
        )

    raise ValueError(f"unknown case mode {case.mode!r}")


def _cases() -> list[Case]:
    return [
        Case(
            "P9-ANON-01",
            "baseline",
            "Anonymous access to protected /manage/users",
            "deny",
            path="/manage/users",
        ),
        Case(
            "P9-CTRL-01",
            "baseline-control",
            "Global admin access to /manage/users",
            "allow",
            credential_prefix="PHASE9_ADMIN",
            path="/manage/users",
            success_statuses=(200,),
        ),
        Case(
            "P9-H11-01",
            "H9-11",
            "Scoped manager must not receive unmanaged-group user marker",
            "scoped_marker",
            credential_prefix="PHASE9_SCOPED_MANAGER",
            path="/manage/users",
            required_envs=("PHASE9_H11_IN_SCOPE_MARKER", "PHASE9_H11_OUT_OF_SCOPE_MARKER"),
            in_scope_marker_env="PHASE9_H11_IN_SCOPE_MARKER",
            out_scope_marker_env="PHASE9_H11_OUT_OF_SCOPE_MARKER",
        ),
        Case(
            "P9-CHAT-01",
            "ownership-control",
            "Alice reads her own known chat resource",
            "allow",
            credential_prefix="PHASE9_ALICE",
            path_env="PHASE9_ALICE_CHAT_PATH",
            success_statuses=(200,),
        ),
        Case(
            "P9-CHAT-02",
            "horizontal-authz",
            "Bob attempts to read Alice's known chat resource",
            "deny",
            credential_prefix="PHASE9_BOB",
            path_env="PHASE9_ALICE_CHAT_PATH",
        ),
        Case(
            "P9-ADMIN-01",
            "vertical-authz",
            "Ordinary user attempts a full-admin mutation",
            "deny",
            credential_prefix="PHASE9_BOB",
            method="PATCH",
            method_env="PHASE9_ADMIN_MUTATION_METHOD",
            path_env="PHASE9_ADMIN_MUTATION_PATH",
            body_env="PHASE9_ADMIN_MUTATION_BODY_JSON",
        ),
        Case(
            "P9-PAT-01",
            "token-scope",
            "Under-scoped PAT attempts an operation outside token scope",
            "deny",
            credential_prefix="PHASE9_UNDERSCOPED_PAT",
            path_env="PHASE9_PAT_PROTECTED_PATH",
        ),
        Case(
            "P9-H12-01",
            "H9-12",
            "Bob attempts to retrieve Alice's CHAT_IMAGE_GEN file",
            "deny",
            credential_prefix="PHASE9_BOB",
            path="/chat/file/{PHASE9_H12_FOREIGN_FILE_ID}",
            required_envs=("PHASE9_H12_FOREIGN_FILE_ID",),
        ),
        Case(
            "P9-H14-01",
            "H9-14",
            "Bob attempts to attach Alice's non-shared custom action",
            "deny",
            credential_prefix="PHASE9_BOB",
            method="PATCH",
            path_env="PHASE9_H14_ATTACH_PATH",
            body_env="PHASE9_H14_ATTACH_BODY_JSON",
        ),
        Case(
            "P9-H14-02",
            "H9-14",
            "Invoke foreign static-header custom action; receiver evidence decides credential delegation",
            "review",
            credential_prefix="PHASE9_BOB",
            method="POST",
            path_env="PHASE9_H14_INVOKE_PATH",
            body_env="PHASE9_H14_INVOKE_BODY_JSON",
            review_reason="inspect approved loopback mock-receiver evidence; HTTP success/failure alone is insufficient",
        ),
        Case(
            "P9-H15-01",
            "H9-15",
            "After agent-share revocation, Bob attempts to create a new session",
            "deny",
            credential_prefix="PHASE9_BOB",
            method="POST",
            path_env="PHASE9_H15_NEW_SESSION_PATH",
            body_env="PHASE9_H15_NEW_SESSION_BODY_JSON",
        ),
        Case(
            "P9-H15-02",
            "H9-15",
            "After revocation, Bob continues the pre-existing chat session",
            "review",
            credential_prefix="PHASE9_BOB",
            method="POST",
            path_env="PHASE9_H15_EXISTING_SESSION_PATH",
            body_env="PHASE9_H15_EXISTING_SESSION_BODY_JSON",
            review_reason="compare with documented revocation policy and inspect post-revocation tool/receiver evidence",
        ),
        Case(
            "P9-H16-01",
            "H9-16",
            "Caller-supplied MCP headers must not exceed configured server auth policy",
            "review",
            credential_prefix="PHASE9_BOB",
            method="POST",
            path_env="PHASE9_H16_MESSAGE_PATH",
            body_env="PHASE9_H16_MESSAGE_BODY_JSON",
            review_reason="inspect local MCP receiver and effective-header evidence; do not infer from HTTP status alone",
        ),
        Case(
            "P9-SA-01",
            "workload-authz",
            "Ordinary user attempts service-account API-key administration",
            "deny",
            credential_prefix="PHASE9_BOB",
            method="POST",
            path_env="PHASE9_SERVICE_ADMIN_PATH",
            body_env="PHASE9_SERVICE_ADMIN_BODY_JSON",
        ),
        Case(
            "P9-SA-02",
            "workload-control",
            "Low-privilege service account reaches its explicitly permitted endpoint",
            "allow",
            credential_prefix="PHASE9_SERVICE_LOW",
            path_env="PHASE9_SERVICE_ALLOWED_PATH",
            success_statuses=(200, 201, 204),
        ),
        Case(
            "P9-SA-03",
            "workload-revocation",
            "Same service credential after privilege removal must lose formerly allowed capability",
            "deny",
            credential_prefix="PHASE9_SERVICE_REVOKED",
            path_env="PHASE9_SERVICE_REVOKED_PATH",
        ),
        Case(
            "P9-SA-04",
            "workload-rotation",
            "Old API key must fail after regeneration",
            "deny",
            credential_prefix="PHASE9_SERVICE_OLD",
            path_env="PHASE9_SERVICE_ROTATION_PATH",
        ),
        Case(
            "P9-SA-05",
            "workload-deletion",
            "Deleted API key must fail",
            "deny",
            credential_prefix="PHASE9_SERVICE_DELETED",
            path_env="PHASE9_SERVICE_DELETED_PATH",
        ),
        Case(
            "P9-SA-06",
            "workload-disable",
            "API key for inactive synthetic service-account user must fail",
            "deny",
            credential_prefix="PHASE9_SERVICE_INACTIVE",
            path_env="PHASE9_SERVICE_INACTIVE_PATH",
        ),
        Case(
            "P9-SA-07",
            "workload-tenant",
            "Tenant-A service credential replayed in Tenant-B context must fail",
            "deny",
            credential_prefix="PHASE9_SERVICE_TENANT_A",
            path_env="PHASE9_SERVICE_CROSS_TENANT_PATH",
            extra_headers_json_env="PHASE9_SERVICE_CROSS_TENANT_HEADERS_JSON",
        ),
    ]


def _manual_results() -> list[Result]:
    manual = [
        ("P9-H13-01", "H9-13", "Prove no untrusted path can set search bypass_acl=True", "instrumented integration/source-provenance evidence required"),
        ("P9-H17-01", "H9-17", "Verify service-account interactive-session reachability", "product policy plus synthetic login/runtime evidence required"),
        ("P9-H18-01", "H9-18", "Verify actual credential-at-rest encryption state", "isolated local DB byte inspection required"),
        ("P9-H18-02", "H9-18", "Verify synthetic ciphertext tamper/integrity behavior", "isolated local DB mutation test required"),
        ("P9-H19-01", "H9-19", "Verify login OAuth access/refresh token storage", "local/mock OAuth and DB inspection required"),
        ("P9-H19-02", "H9-19", "Verify logout/unlink/revocation cleanup for login OAuth tokens", "lifecycle and DB evidence required"),
    ]
    return [
        Result(
            case_id=case_id,
            source=source,
            disposition="REVIEW",
            description=description,
            note=note,
        )
        for case_id, source, description, note in manual
    ]


def _run_case(case: Case, base_url: str, execute: bool) -> Result:
    missing = _missing_required(case)

    try:
        method, method_missing = _case_method(case)
        path, path_missing = _case_path(case)
        credential_headers, credential_missing = _credentials(case)
        extra_headers, extra_missing = _extra_headers(case)
        body, body_missing = _body(case)
    except ValueError as exc:
        return Result(
            case_id=case.case_id,
            source=case.source,
            disposition="FAIL",
            description=case.description,
            note=f"fixture validation failed: {exc}",
        )

    missing.extend(method_missing)
    missing.extend(path_missing)
    missing.extend(credential_missing)
    missing.extend(extra_missing)
    missing.extend(body_missing)

    if missing:
        return Result(
            case_id=case.case_id,
            source=case.source,
            disposition="SKIP",
            description=case.description,
            method=method,
            path=path,
            note="missing synthetic fixture(s): " + ", ".join(sorted(set(missing))),
        )

    assert method is not None
    assert path is not None

    if not execute:
        return Result(
            case_id=case.case_id,
            source=case.source,
            disposition="SKIP",
            description=case.description,
            method=method,
            path=path,
            note="dry-run: set PHASE9_RUN=1 after authorized synthetic fixtures are ready",
        )

    try:
        status, data = _request(
            base_url,
            method,
            path,
            {**credential_headers, **extra_headers},
            body,
        )
        disposition, assertions, note = _evaluate(case, status, data)
        return Result(
            case_id=case.case_id,
            source=case.source,
            disposition=disposition,
            description=case.description,
            method=method,
            path=path,
            http_status=status,
            response_bytes=len(data),
            response_sha256=_digest(data),
            assertions=assertions,
            note=note,
        )
    except Exception as exc:  # bounded harness: preserve error, continue other cases
        return Result(
            case_id=case.case_id,
            source=case.source,
            disposition="FAIL",
            description=case.description,
            method=method,
            path=path,
            note=f"execution error: {type(exc).__name__}: {exc}",
        )


def main() -> int:
    base_url = _base_url()
    _assert_loopback_base(base_url)
    execute = _truthy("PHASE9_RUN")

    cases = _cases()
    if len(cases) > MAX_CASES:
        raise SystemExit(f"REFUSED: case count {len(cases)} exceeds {MAX_CASES}")

    results = [_run_case(case, base_url, execute) for case in cases]
    results.extend(_manual_results())

    payload = {
        "schema": "phase9-negative-authz-results/v1",
        "base_url": base_url,
        "execute": execute,
        "timeout_seconds": _timeout(),
        "case_count": len(results),
        "counts": {
            disposition: sum(r.disposition == disposition for r in results)
            for disposition in ("PASS", "FAIL", "REVIEW", "SKIP")
        },
        "results": [asdict(result) for result in results],
    }

    rendered = json.dumps(payload, indent=2, sort_keys=True)
    result_path = os.environ.get("PHASE9_RESULT_PATH", "").strip()
    if result_path:
        path = Path(result_path)
        path.write_text(rendered + "\n", encoding="utf-8")
        print(f"results written to {path}")
    else:
        print(rendered)

    # FAIL means an assertion contradicted the expected property or the harness
    # encountered an execution/fixture-validation error. REVIEW/SKIP do not make
    # the process non-zero because they intentionally require later evidence.
    return 1 if any(r.disposition == "FAIL" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
