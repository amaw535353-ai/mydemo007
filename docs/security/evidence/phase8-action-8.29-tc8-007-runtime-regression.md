# Phase 8 Action 8.29 — TC8-007 Runtime Regression

## Classification

**TC8_007_RUNTIME_FIX_VERIFIED**

## Remediation

Commit under verification:

`4ebd7a06be5fe0238f264d298ad19b342116d357`

Patched source SHA-256:

`2323f63a524f2da64108f2024097cbb4bafbe2d6c9ae0466ef8017c42599bcc9`

Runtime:

`onyx-api_server-1`

## Synthetic test identities

Fresh low-privilege synthetic Alice and Bob accounts were created for this
regression execution.

No production identities or data were used.

## Positive controls

| Test | HTTP |
|---|---:|
| Bob users/me | 200 |
| Bob own chat | 200 |
| Bob own chat + tenant_id=default | 200 |

## TC8-007 regression

| Request | HTTP |
|---|---:|
| Bob → Alice, no added parameters | 403 |
| unknown parameter | 403 |
| user_id=Alice | 403 |
| tenant_id=public | 403 |
| tenant_id=default | 403 |
| user_id=Alice + tenant_id=default | 403 |

## Final controls

- Foreign read: HTTP 403
- Owner read: HTTP 200
- API health: HTTP 200

## Disclosure

- Client SQL/schema disclosure: **ABSENT**
- Server default-schema error: **ABSENT**

## Runtime verification

- Running source SHA-256: `2323f63a524f2da64108f2024097cbb4bafbe2d6c9ae0466ef8017c42599bcc9`
- FastAPI get_async_session parameters:
  `<none>`

## Interpretation

A successful result demonstrates that request-supplied tenant parameters no
longer influence the asynchronous database dependency while foreign-object
authorization remains enforced and legitimate owner behavior remains intact.

## Environment limitation

The committed patch was overlaid into the authorized lab API container and the
container was restarted.

This verifies runtime behavior in the controlled Phase 8 lab. It does not yet
represent verification of a separately rebuilt production image.

## Safety

- Authorized Codespace only
- Synthetic users and objects
- Sequential bounded requests
- No production data
- No real credentials
- External model/network activity disabled
