# Phase 11 — Action 11.5 Action Approval and Confused-Deputy Boundaries

## Verified controls

- the strictest policy governs multi-action requests;
- ASK actions define approval scope;
- MCP tools default to ASK unless an administrator overrides policy;
- unclassifiable MCP calls are DENY;
- proxy/session authorization headers are removed before origin forwarding;
- denial and internal approval failures have explicit block paths.

## Finding classification

**NO CONFUSED-DEPUTY OR APPROVAL BYPASS CONFIRMED**

## Evidence

Results:

`docs/security/evidence/phase11-action-11.5-action-approval-results.txt`

SHA-256:

`2a8c974b5c6042fada07e9cdc8036bfd17d293b8f2301cb53240512bef27dc95`

Source trace:

`docs/security/evidence/phase11-action-11.5-action-approval-source-trace.txt`

SHA-256:

`83f5e66b55d1684cc6b9c4f3737e17f35560210d221809c1357a5d469bc0cc5f`

Regression:

`backend/tests/unit/onyx/external_apps/test_phase11_action_approval_boundaries.py`

## Completion

**ACTION 11.5: COMPLETE**

**RESULT=PHASE_11_ACTION_11_5_PASS**
