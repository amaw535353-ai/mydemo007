# Phase 8 TC8-001 - Anonymous Request to Protected Route

## Result

**PASS**

## Objective

Verify that an unauthenticated client cannot access protected
administrative API routes.

## Runtime

- UTC: 2026-09-16T19:19:40Z
- Health endpoint: HTTP 200
- Runtime: pinned Onyx Standard API core
- Authentication mode: basic
- Actor: unauthenticated client

## Expected secure behavior

**DENY**

## Safety boundary

- Authorized Codespace runtime only
- Read-only GET requests only
- Maximum requests: 3
- Actual requests: 3
- Concurrency: 1
- Per-request timeout: 5 seconds
- No production credentials
- No real user/customer data
- No external services targeted

## Harness history

Attempt 1 produced a partial result because the dynamic target-selection
helper selected two paths whose GET method returned HTTP 405.

That was classified as a test-harness defect rather than an application
security result.

The original attempt evidence was preserved at:

`docs/security/evidence/phase8-tc8-001-attempt1-harness-partial.md`

Attempt 2 used three exact GET endpoints verified against the live pinned
FastAPI route inventory.

## Results

| Route | Path | HTTP | Interpretation | Bytes | SHA-256 |
|---|---|---:|---|---:|---|
| `get_valid_domains` | `/manage/admin/valid-domains` | 403 | PASS_DENY | 82 | `d82fa6aeca8944ed71d2ba5a18fcbad5777e3590867c0628e4d66ccd3eaf0c4c` |
| `list_credentials_admin` | `/manage/admin/credential` | 403 | PASS_DENY | 82 | `d82fa6aeca8944ed71d2ba5a18fcbad5777e3590867c0628e4d66ccd3eaf0c4c` |
| `get_connector_status` | `/manage/admin/connector/status` | 403 | PASS_DENY | 82 | `d82fa6aeca8944ed71d2ba5a18fcbad5777e3590867c0628e4d66ccd3eaf0c4c` |

## Summary

- Requests executed: 3
- Explicit DENY responses (401/403): 3
- Ambiguous responses: 0
- Unexpected HTTP 200 responses: 0

**TC8-001 result: PASS**

A response is not treated as a vulnerability merely because it is unexpected.
Any candidate finding requires reproduction and exclusion of fixture,
identity, route and runtime-configuration errors.
