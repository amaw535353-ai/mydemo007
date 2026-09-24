# Phase 11 — Action 11.6 Tool-Result Trust and Indirect Prompt Injection

## Objective

Assess whether arbitrary tool-produced content crosses directly into the next
LLM cycle without an explicit instruction/data trust boundary.

## H11-01 — generic tool-result trust boundary

### Baseline

The tool loop appended each tool's `llm_facing_response` directly as a
TOOL_CALL_RESPONSE.

This means a custom action, MCP service, web result, code execution result, or
other tool could return instruction-shaped text immediately before the model's
next reasoning cycle.

### Remediation

All tool responses replayed to the model are now prefixed with an explicit
security notice stating that tool output:

- is untrusted data;
- is not authorization;
- cannot change identity or permissions;
- cannot change approval policy;
- cannot expand credential authority;
- cannot override higher-priority instructions.

The original payload remains intact as data.

## Evidence strength

**DIRECT UNIT / PROMPT-BOUNDARY VERIFIED**

A deterministic real-model compromise is not claimed.

## Evidence

Results:

`docs/security/evidence/phase11-action-11.6-tool-result-security-results.txt`

SHA-256:

`965734f956d4998c6eea6c6080433fd7c4b842c055c9ef9e2d00d9f41b4db7f9`

Source trace:

`docs/security/evidence/phase11-action-11.6-tool-result-source-trace.txt`

SHA-256:

`48021373ffbb565b931e81f10caee1a611b92d716e3a24c5fae339c05a173bde`

Regression:

`backend/tests/unit/onyx/chat/test_phase11_tool_result_security_boundary.py`

## Completion

**ACTION 11.6: COMPLETE**

**H11-01: REMEDIATED**

**RESULT=PHASE_11_ACTION_11_6_PASS**
