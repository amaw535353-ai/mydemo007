#!/usr/bin/env python3
"""Convert Phase 9 runtime JSON into a sanitized Markdown decision record.

The input is produced by phase9_negative_authz_runner.py. This script never
requires or emits credentials or raw HTTP response bodies.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

EXPECTED_SCHEMA = "phase9-negative-authz-results/v1"
VALID_DISPOSITIONS = {"PASS", "FAIL", "REVIEW", "SKIP"}


def _load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"ERROR: results file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit("ERROR: result document must be a JSON object")
    return data


def _load_metadata(path: Path | None) -> dict[str, str]:
    if path is None or not path.exists():
        return {}
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        out[key.strip()] = value.strip()
    return out


def _escape(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\n", " ").replace("\r", " ")
    return text.replace("|", "\\|")


def _compact_assertions(value: Any) -> str:
    if not isinstance(value, dict) or not value:
        return ""
    return ", ".join(f"{k}={v}" for k, v in sorted(value.items()))


def main() -> int:
    if len(sys.argv) not in {3, 4}:
        raise SystemExit(
            "usage: phase9_results_to_markdown.py RESULTS.json SUMMARY.md [METADATA.txt]"
        )

    result_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    metadata_path = Path(sys.argv[3]) if len(sys.argv) == 4 else None

    payload = _load_json(result_path)
    metadata = _load_metadata(metadata_path)

    if payload.get("schema") != EXPECTED_SCHEMA:
        raise SystemExit(
            f"ERROR: unexpected schema {payload.get('schema')!r}; expected {EXPECTED_SCHEMA!r}"
        )

    results = payload.get("results")
    if not isinstance(results, list):
        raise SystemExit("ERROR: results must be a list")

    normalized: list[dict[str, Any]] = []
    for item in results:
        if not isinstance(item, dict):
            raise SystemExit("ERROR: every result item must be an object")
        disposition = item.get("disposition")
        if disposition not in VALID_DISPOSITIONS:
            raise SystemExit(f"ERROR: invalid disposition {disposition!r}")
        normalized.append(item)

    counts = {
        name: sum(item.get("disposition") == name for item in normalized)
        for name in ("PASS", "FAIL", "REVIEW", "SKIP")
    }

    executed = bool(payload.get("execute"))
    fails = [x for x in normalized if x.get("disposition") == "FAIL"]
    reviews = [x for x in normalized if x.get("disposition") == "REVIEW"]
    skips = [x for x in normalized if x.get("disposition") == "SKIP"]

    if not executed:
        gate = "NOT EXECUTED — DRY RUN ONLY"
    elif fails:
        gate = "RUNTIME FAILURES PRESENT — PROMOTE TO ACTION 9.11 VALIDATION"
    elif skips:
        gate = "INCOMPLETE — REQUIRED SYNTHETIC FIXTURES WERE SKIPPED"
    elif reviews:
        gate = "INCOMPLETE — MANUAL/RECEIVER/DB REVIEW ITEMS REMAIN"
    else:
        gate = "HTTP AUTOMATED GATE PASSED — VERIFY MANUAL EVIDENCE BEFORE CLOSURE"

    lines: list[str] = []
    lines.append("# Phase 9 Action 9.10 — Runtime Verification Result")
    lines.append("")
    lines.append(f"Status: **{gate}**")
    lines.append("")
    lines.append("## Immutable execution context")
    lines.append("")
    lines.append(f"- Branch: `{_escape(metadata.get('branch', 'unknown'))}`")
    lines.append(f"- HEAD: `{_escape(metadata.get('head', 'unknown'))}`")
    lines.append(f"- UTC timestamp: `{_escape(metadata.get('timestamp_utc', 'unknown'))}`")
    lines.append(f"- Base URL: `{_escape(payload.get('base_url', metadata.get('base_url', 'unknown')))}`")
    lines.append(f"- Runner SHA-256: `{_escape(metadata.get('runner_sha256', 'unknown'))}`")
    lines.append(f"- Execute flag: `{executed}`")
    lines.append(f"- Timeout: `{_escape(payload.get('timeout_seconds'))}` seconds")
    lines.append("")
    lines.append("## Disposition counts")
    lines.append("")
    lines.append(f"- PASS: **{counts['PASS']}**")
    lines.append(f"- FAIL: **{counts['FAIL']}**")
    lines.append(f"- REVIEW: **{counts['REVIEW']}**")
    lines.append(f"- SKIP: **{counts['SKIP']}**")
    lines.append("")
    lines.append("## Case results")
    lines.append("")
    lines.append("| Case | Source | Disposition | Method | Path | HTTP | Assertions | Note |")
    lines.append("|---|---|---|---|---|---:|---|---|")
    for item in normalized:
        lines.append(
            "| "
            + " | ".join(
                [
                    _escape(item.get("case_id")),
                    _escape(item.get("source")),
                    _escape(item.get("disposition")),
                    _escape(item.get("method")),
                    _escape(item.get("path")),
                    _escape(item.get("http_status")),
                    _escape(_compact_assertions(item.get("assertions"))),
                    _escape(item.get("note")),
                ]
            )
            + " |"
        )

    lines.append("")
    lines.append("## Evidence-integrity properties")
    lines.append("")
    lines.append("- Raw HTTP bodies are not included; the runner records response length and SHA-256 only.")
    lines.append("- Credential environment values are not included in this summary.")
    lines.append("- A 404 denial is not automatically treated as proof of authorization enforcement.")
    lines.append("- REVIEW cases remain unresolved until required policy, mock-receiver, DB, audit, or lifecycle evidence is attached.")
    lines.append("")
    lines.append("## Action 9.11 promotion queue")
    lines.append("")

    promotion = fails + reviews
    if not promotion:
        lines.append("No FAIL/REVIEW cases were present in this result set.")
    else:
        for item in promotion:
            lines.append(
                f"- `{_escape(item.get('case_id'))}` / `{_escape(item.get('source'))}` — "
                f"{_escape(item.get('disposition'))}: {_escape(item.get('note'))}"
            )

    lines.append("")
    lines.append("## Completion decision")
    lines.append("")
    lines.append("Action 9.10 must not be marked COMPLETE from this artifact unless the run used the authorized synthetic lab, required fixtures were executed, and every REVIEW item has supporting evidence or an explicit documented non-applicability disposition.")
    lines.append("")
    lines.append("A FAIL is a reproducible candidate security failure, not automatically a final vulnerability. Action 9.11 must validate product intent, impact, root cause, remediation, and retest.")
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"sanitized summary written to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
