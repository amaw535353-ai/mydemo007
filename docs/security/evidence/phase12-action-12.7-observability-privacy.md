# Phase 12 — Action 12.7 Logs, Traces, Telemetry and Error Disclosure

## Verified controls

- incognito policy can suppress complete external traces;
- trace masking recognizes authorization/private-key material;
- Langfuse processing applies the shared masking helper;
- telemetry can be deployment-disabled.

## Privacy-sensitive boundaries

Normal external traces may contain model inputs and outputs.

Telemetry accepts caller-supplied event data and may attach user/customer
identifiers.

Background-error persistence can include an original error message after an
integrity failure.

These are privacy-sensitive observability surfaces.

## Finding classification

No evidence in this static action proves that sensitive synthetic content
reaches those surfaces without authorization or policy.

Therefore:

**NO UNAUTHORIZED OBSERVABILITY DISCLOSURE CONFIRMED**

The background-error original-message path remains a runtime review candidate.

## Evidence

Results:

`docs/security/evidence/phase12-action-12.7-results.txt`

SHA-256:

`ce50867fce267609abcd1f3e9253eb0e5e893756f38a3a36d33ff0e3f55173ee`

Source trace:

`docs/security/evidence/phase12-action-12.7-source-trace.txt`

SHA-256:

`9dba81322613d8d0f75f998c90c56b14b7652080d2c3de619ecb765fbcea08b2`

Test:

`backend/tests/unit/onyx/privacy/test_phase12_observability_privacy.py`

## Completion

**ACTION 12.7: COMPLETE**

**RESULT=PHASE_12_ACTION_12_7_PASS**
