# Finding — Foreign Custom Action Attachment

## Finding ID

P9-H14-01

## Status

**CONFIRMED AT BUSINESS-LOGIC LAYER — REMEDIATION RETEST PENDING**

## Component

`backend/onyx/db/persona.py::upsert_persona`

## Security boundary

Custom-action attachment and delegated capability authorization.

## Expected behavior

Only the action creator or an actions administrator can add a custom action to an agent.

An existing attachment can survive an ordinary update. A removed foreign attachment cannot be added again.

## Observed behavior

Bob attached Alice's custom action to Bob's synthetic persona.

The test made no HTTP request. It rolled back every synthetic object and verified cleanup.

## Root cause

`upsert_persona` loads every requested tool identifier before it updates the persona.

The function checks access for newly attached MCP tools. A non-MCP custom action has no MCP server identifier.

The old flow skipped the MCP check and applied no equivalent custom-action owner check.

## Remediation

The patched flow separates three tool classes:

1. Existing attachments pass without a new access decision.
2. New custom actions require `can_manage_own_tool`.
3. New MCP tools retain the existing MCP-server access check.

Built-in tools retain their existing attachment behavior.

An unauthorized custom-action attachment raises `OnyxErrorCode.INSUFFICIENT_PERMISSIONS`. The API maps this error to HTTP 403.

## Regression coverage

`backend/tests/external_dependency_unit/db/test_custom_action_persona_guard.py` covers:

- foreign non-owner denial;
- creator attachment;
- actions-administrator attachment;
- preservation of an existing foreign attachment;
- denial after removal and attempted reattachment.

## Compatibility and residual risk

The new policy intentionally restricts Onyx's current tenant-wide custom-action catalog behavior.

The catalog can still display an action that the server will reject during attachment. This is a usability gap.

Existing foreign attachments remain usable until removal. This prevents unexpected breakage but leaves temporary delegated capability.

Credential transmission was not executed. Its runtime impact remains unconfirmed.

A future explicit action-sharing model can replace the owner-or-admin policy if the product requires delegated reuse.

## Verification status

Passed:

- Ruff formatting;
- Ruff linting;
- Python syntax compilation;
- Git whitespace validation.

Pending:

- database-backed external-dependency regression suite;
- rebuilt local-container negative retest;
- API-level HTTP 403 verification.

## Evidence

`docs/security/evidence/phase9-action-9.10-runtime-slice6-h14.md`
