# Phase 8 TC8-001 - Anonymous Request to Protected Route

## Runtime

- UTC: 2026-09-16T19:17:20Z
- Health endpoint: HTTP 200
- Live FastAPI routes internally enumerated: 646
- Public OpenAPI exposure: disabled
- Test actor: unauthenticated client

## Expected secure behavior

**DENY**

## Safety boundary

- Authorized Codespace runtime only
- Read-only GET requests only
- Maximum requests: 3
- Actual requests: 3
- Concurrency: 1
- Per-request timeout: 5 seconds
- No real credentials
- No real user data

## Results

| Route | Path | HTTP | Interpretation | Bytes | SHA-256 |
|---|---|---:|---|---:|---|
| `change_my_password` | `/password/change-password` | 405 | AMBIGUOUS_REVIEW | 31 | `83c09ba9a8daedb136f90b17a294caa90ad471a016e430df6e229acb5a81e100` |
| `admin_reset_user_password` | `/password/reset_password` | 405 | AMBIGUOUS_REVIEW | 31 | `83c09ba9a8daedb136f90b17a294caa90ad471a016e430df6e229acb5a81e100` |
| `get_user_chat_sessions` | `/chat/get-user-chat-sessions` | 403 | PASS_DENY | 82 | `d82fa6aeca8944ed71d2ba5a18fcbad5777e3590867c0628e4d66ccd3eaf0c4c` |

## Summary

- Requests: 3
- Explicit DENY responses (401/403): 1
- Ambiguous responses: 2
- Unexpected HTTP 200 responses: 0

**TC8-001 result: PARTIAL_REVIEW_REQUIRED**

Any unexpected HTTP 200 is only a candidate finding until independently
reproduced and route/authentication assumptions are verified.
