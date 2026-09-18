#!/usr/bin/env bash
set -euo pipefail

# Phase 9 Action 9.10 — bounded local runtime verification wrapper.
# This script never prints credential environment variables or raw HTTP bodies.

EXPECTED_BRANCH="security/phase-9-identity-authorization-tenant-isolation"
MINIMUM_ANCESTOR="5d7a602680200e50134b5048fc79f27c8f32e41b"

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "ERROR: not inside a git repository" >&2
  exit 2
}
cd "$ROOT"

BRANCH="$(git branch --show-current)"
HEAD="$(git rev-parse HEAD)"

if [[ "$BRANCH" != "$EXPECTED_BRANCH" ]]; then
  echo "ERROR: wrong branch: $BRANCH" >&2
  echo "Expected: $EXPECTED_BRANCH" >&2
  exit 2
fi

if ! git merge-base --is-ancestor "$MINIMUM_ANCESTOR" HEAD; then
  echo "ERROR: current HEAD does not contain the completed Action 9.9 baseline" >&2
  exit 2
fi

if [[ -n "$(git status --porcelain)" ]]; then
  echo "ERROR: working tree must be clean before runtime evidence collection" >&2
  exit 2
fi

RUNNER="$ROOT/scripts/security/phase9_negative_authz_runner.py"
SUMMARIZER="$ROOT/scripts/security/phase9_results_to_markdown.py"

[[ -f "$RUNNER" ]] || { echo "ERROR: missing $RUNNER" >&2; exit 2; }
[[ -f "$SUMMARIZER" ]] || { echo "ERROR: missing $SUMMARIZER" >&2; exit 2; }

python3 -m py_compile "$RUNNER" "$SUMMARIZER"

export PHASE9_BASE_URL="${PHASE9_BASE_URL:-http://127.0.0.1:8080}"
export PHASE9_TIMEOUT_SECONDS="${PHASE9_TIMEOUT_SECONDS:-5}"
export PHASE9_RESULT_PATH="${PHASE9_RESULT_PATH:-/tmp/phase9-action-9.10-results.json}"
PHASE9_SUMMARY_PATH="${PHASE9_SUMMARY_PATH:-/tmp/phase9-action-9.10-summary.md}"
PHASE9_METADATA_PATH="${PHASE9_METADATA_PATH:-/tmp/phase9-action-9.10-metadata.txt}"

# Fail closed unless the configured URL is syntactically loopback.
python3 - <<'PY'
import ipaddress
import os
import sys
import urllib.parse

url = os.environ["PHASE9_BASE_URL"]
p = urllib.parse.urlparse(url)
if p.scheme not in {"http", "https"} or not p.hostname:
    raise SystemExit("REFUSED: PHASE9_BASE_URL must be loopback HTTP(S)")
host = p.hostname
if host == "localhost":
    sys.exit(0)
try:
    ip = ipaddress.ip_address(host)
except ValueError:
    raise SystemExit("REFUSED: only exact localhost or literal loopback IPs are allowed")
if not ip.is_loopback:
    raise SystemExit("REFUSED: PHASE9_BASE_URL is not loopback")
PY

# Reachability check. Any HTTP response proves the local service answered;
# the status itself is not treated as an authorization result.
HTTP_CODE="$(
  curl --silent --show-error --output /dev/null        --max-time 5 --connect-timeout 3        --write-out '%{http_code}'        "$PHASE9_BASE_URL/" || true
)"
if [[ -z "$HTTP_CODE" || "$HTTP_CODE" == "000" ]]; then
  echo "ERROR: local Onyx API is not reachable at $PHASE9_BASE_URL" >&2
  exit 3
fi

{
  printf 'phase9_action=9.10\n'
  printf 'timestamp_utc=%s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  printf 'branch=%s\n' "$BRANCH"
  printf 'head=%s\n' "$HEAD"
  printf 'base_url=%s\n' "$PHASE9_BASE_URL"
  printf 'http_reachability_status=%s\n' "$HTTP_CODE"
  printf 'runner_sha256=%s\n' "$(sha256sum "$RUNNER" | awk '{print $1}')"
} > "$PHASE9_METADATA_PATH"

if [[ "${PHASE9_RUN:-0}" != "1" ]]; then
  echo "DRY RUN ONLY: PHASE9_RUN is not 1."
  echo "The runner will validate fixture availability but send no requests."
fi

set +e
python3 "$RUNNER"
RUN_RC=$?
set -e

if [[ ! -s "$PHASE9_RESULT_PATH" ]]; then
  echo "ERROR: runner did not produce $PHASE9_RESULT_PATH" >&2
  exit 4
fi

python3 "$SUMMARIZER"   "$PHASE9_RESULT_PATH"   "$PHASE9_SUMMARY_PATH"   "$PHASE9_METADATA_PATH"

echo
echo "============================================================"
echo "PHASE 9 ACTION 9.10 RUNTIME VERIFICATION WRAPPER"
echo "============================================================"
echo "Branch:      $BRANCH"
echo "HEAD:        $HEAD"
echo "Base URL:    $PHASE9_BASE_URL"
echo "Result JSON: $PHASE9_RESULT_PATH"
echo "Summary:     $PHASE9_SUMMARY_PATH"
echo "Metadata:    $PHASE9_METADATA_PATH"
echo
echo "No credential values or raw response bodies were written by this wrapper."
echo "Review the sanitized summary before committing any evidence."
echo "============================================================"

exit "$RUN_RC"
