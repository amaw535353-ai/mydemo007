# Phase 9 Action 9.11 — H9-14 Remediation Record

## Status

**IMPLEMENTED — DATABASE AND RUNTIME RETEST PENDING**

## Decision

The fork uses an owner-or-actions-administrator policy for new custom-action attachments.

The decision is stricter than the assessed Onyx tenant-wide catalog behavior.

## Code change

`upsert_persona` now checks each new non-MCP custom action with `can_manage_own_tool`.

The function raises a standard insufficient-permissions error when the check fails.

The existing MCP authorization check remains unchanged.

The function preserves existing attachments before it evaluates new attachment access.

## Security effectiveness

Expected post-fix outcomes:

| Case | Expected result |
| --- | --- |
| Bob attaches Alice's custom action | DENY with HTTP 403 |
| Alice attaches Alice's custom action | ALLOW |
| Actions administrator attaches Alice's custom action | ALLOW |
| Bob saves an agent with an existing Alice action | ALLOW and preserve |
| Bob removes and re-adds Alice's action | DENY with HTTP 403 |

## Tradeoffs

- Security: blocks new cross-owner delegated action capabilities.
- Compatibility: preserves existing attachments.
- Usability: the catalog can show an action that attachment later rejects.
- Performance: one in-memory permission decision per new custom action.
- Cost: no paid service or external provider is required.

## Verification

Static verification passed on the changed files.

The current work environment has no Docker or PostgreSQL service. The database-backed test remains pending.

The authorized local Onyx laboratory must run the focused test after it receives the patch.
