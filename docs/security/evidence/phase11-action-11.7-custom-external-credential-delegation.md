# Phase 11 — Action 11.7 Custom / External Credential Delegation

## Objective

Verify that action execution receives credentials from trusted application or
sandbox identity rather than model-selected owner identity.

## Verified properties

- passthrough authentication cannot be combined with a static Authorization
  header;
- linking a different OAuth configuration crosses an explicit authorization
  gate;
- per-tool OAuth resolution is keyed by the authenticated user ID;
- dynamic custom-tool identity fields come from trusted application context;
- external-app credential resolution uses the sandbox tenant and user identity;
- an unfillable credential template omits its authentication header;
- substituted credential values are not recursively interpreted as templates.

## Finding classification

**NO CREDENTIAL-DELEGATION BYPASS CONFIRMED**

## Evidence

Results:

`docs/security/evidence/phase11-action-11.7-credential-delegation-results.txt`

SHA-256:

`d3a694c86182abf117711b91ba111fa1a423b7901056e48a148c1a120eba6926`

Source trace:

`docs/security/evidence/phase11-action-11.7-credential-delegation-source-trace.txt`

SHA-256:

`8904fca5e4fb030ab7caf8a902cfb16226fb59a0f5539514851971cd3e2dd166`

Regression:

`backend/tests/unit/onyx/server/features/tool/test_phase11_credential_delegation.py`

## Completion

**ACTION 11.7: COMPLETE**

**RESULT=PHASE_11_ACTION_11_7_PASS**
