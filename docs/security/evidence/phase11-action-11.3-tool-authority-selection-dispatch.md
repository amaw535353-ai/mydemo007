# Phase 11 — Action 11.3 Tool Authority, Selection and Dispatch

## Objective

Determine whether model output can create tool authority that was not supplied
by trusted application state.

## Verified controls

The application constructs the executable tool set before model-requested calls
are dispatched.

Verified properties:

- disabled tools are skipped;
- optional allowed-tool filtering is applied;
- authenticated user identity is propagated from application context;
- unknown model-requested tool names are dropped;
- zero execution capacity prevents execution;
- the batch execution cap limits dispatched tools.

## Harness note

The initial synthetic test harness omitted the required tool emitter.

The real runner correctly requires the emitter because it emits a SectionEnd
packet after execution.

The harness was repaired with a synthetic mocked emitter.

This was not an Onyx security defect.

## Finding classification

**NO TOOL AUTHORITY BYPASS CONFIRMED**

## Evidence

Results:

`docs/security/evidence/phase11-action-11.3-tool-authority-results.txt`

SHA-256:

`04bb6f3f9b8ad4281645a2043fa6a72ed10b515ffeb444f7b5ea1ef36a3231a0`

Source trace:

`docs/security/evidence/phase11-action-11.3-tool-authority-source-trace.txt`

SHA-256:

`c41cd8f62f59c78ba927ebfc6f2f252b76cd0445b0b0638187a0eee2de00b95a`

Regression:

`backend/tests/unit/onyx/tools/test_phase11_tool_authority_boundaries.py`

## Completion

**ACTION 11.3: COMPLETE**

**RESULT=PHASE_11_ACTION_11_3_PASS**
