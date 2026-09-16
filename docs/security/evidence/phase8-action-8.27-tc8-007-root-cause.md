# Phase 8 Action 8.27 — TC8-007 Root-Cause Analysis

## Classification

**CONFIRMED_SECURITY_RELEVANT_DEFECT**

## Metadata

- UTC: 2026-09-16T21:45:11Z
- Project HEAD before this record: `ac808b62147f9aca0c3ca464fb174aa3d8ae7d74`
- Onyx pin under assessment: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Reproduction commit: `ac808b62147f9aca0c3ca464fb174aa3d8ae7d74`
- Target: authorized synthetic local lab

## Demonstrated runtime behavior

| Request variant | Result |
|---|---:|
| Foreign read without added parameters | 403 |
| Unknown parameter | 403 |
| `user_id=<Alice>` | 403 |
| `tenant_id=public` | 403 |
| `tenant_id=default` | 500 |
| `user_id=<Alice>&tenant_id=default` | 500 |
| Final foreign-object integrity control | 403 |

The HTTP 500 response identified an attempted query against
`default.user` and returned internal SQL/database details.

## Root-cause chain

1. The chat-session endpoint uses
   `require_permission(..., allow_anonymous=True)`.
2. That dependency reaches `current_chat_accessible_user`.
3. `current_chat_accessible_user` depends on `optional_user`.
4. `optional_user` depends on `get_async_session`.
5. `get_async_session` declares
   `tenant_id: str | None = None`.
6. The supplied tenant identifier reaches
   `schema_translate_map = {None: tenant_id}`.
7. Consequently, `tenant_id=default` causes ORM queries to target the
   nonexistent `default` PostgreSQL schema instead of `public`.

## Confirmed impact

- Caller-controlled tenant/schema selection reaches the asynchronous
  database-session dependency.
- A valid but nonexistent schema name causes an internal server error.
- The API response discloses internal SQL, ORM, table and schema details.
- Normal foreign-resource authorization remained denied.

## Not demonstrated

- No unauthorized read of Alice's data.
- No unauthorized write or deletion.
- No successful tenant-boundary crossing.
- No production or third-party impact.
- No claim of an authorization bypass.

## Security interpretation

This is no longer classified only as an unexplained robustness anomaly.

It is a confirmed trust-boundary and dependency-design defect because a
request parameter can influence database schema selection. The observed
impact is denial of the affected request and verbose internal-error
disclosure. Broader cross-tenant impact remains unconfirmed.

Potential CWE mappings remain provisional until remediation review:

- CWE-20 — Improper Input Validation
- CWE-209 — Generation of Error Message Containing Sensitive Information

## Required remediation direction

1. Remove request-bindable `tenant_id` from the FastAPI database dependency.
2. Obtain the request tenant only from trusted authenticated server context.
3. Preserve a separate explicit internal API for background jobs and controlled
   tenant-specific operations.
4. Return a generic external error response while retaining diagnostic details
   only in protected server logs.
5. Add regression tests proving query parameters cannot select database schemas.

## Evidence integrity

Source excerpts and SHA-256 digests were captured in:

- `/tmp/phase8-action-8.27/source-trace.txt`
- `/tmp/phase8-action-8.27/source-digests.sha256`

## Safety

- Authorized repository and local runtime only
- Static source inspection
- No additional authorization-manipulation traffic
- No production data or credentials
- No external services
