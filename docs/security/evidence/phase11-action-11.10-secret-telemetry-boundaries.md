# Phase 11 — Action 11.10 Secret and Telemetry Boundaries

## H11-03 — Raw tool content in generic tracing

### Baseline

The generic tool runner recorded raw tool argument values, complete tool
response content and raw arguments in generic error tracing.

### Remediation

Generic tracing now records only:

- argument count;
- top-level argument names;
- tool-output character count.

Raw argument values, nested values and arbitrary tool-response content are no
longer recorded by these generic trace fields.

The three generic error-span paths also use the structural argument summary.

## Residual scope

This action does not claim every application exception string or stack trace is
secret-free.

Residual review remains for:

- tool-specific exception strings;
- LLM-facing error text;
- stack traces;
- third-party library errors.

## Evidence strength

**DIRECT UNIT / SOURCE REGRESSION VERIFIED**

## Evidence

Results:

`docs/security/evidence/phase11-action-11.10-secret-telemetry-results.txt`

SHA-256:

`30ef4767076d4992257c36de312e64225f76afa23f1e90f36d1fe3e0a619c234`

Source trace:

`docs/security/evidence/phase11-action-11.10-secret-telemetry-source-trace.txt`

SHA-256:

`a9b313461831b81197917c457e5ad583d549069986fae0ab41fd12795701ff2f`

Regression:

`backend/tests/unit/onyx/tools/test_phase11_tool_trace_redaction.py`

## Completion

**ACTION 11.10: COMPLETE**

**H11-03: REMEDIATED**

**RESULT=PHASE_11_ACTION_11_10_PASS**
