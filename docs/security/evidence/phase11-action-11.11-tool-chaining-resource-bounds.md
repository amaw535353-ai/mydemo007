# Phase 11 — Action 11.11 Tool Chaining and Resource Exhaustion

## Objective

Determine whether model-driven tool chaining can create an unbounded execution
path.

## Existing controls

The agent loop already uses:

`MAX_LLM_CYCLES`

with a default of six cycles.

When the final cycle is reached, tools are disabled and the model is forced
toward a final answer.

Individual tool execution is also bounded by the tool-runner timeout.

Craft agent turns additionally have soft and hard wall-clock budgets.

## H11-04 — unbounded per-cycle tool fan-out

### Baseline

Although `run_tool_calls()` already supported an execution cap, the production
LLM loop explicitly invoked it with:

`max_concurrent_tools=None`

Therefore a model-generated cycle containing many otherwise valid tool calls
had no application-level fan-out ceiling at that call site.

No external overload was attempted.

### Remediation

A new application limit:

`MAX_TOOL_CALLS_PER_CYCLE`

defaults to 10 and is clamped to the authorized maximum of 10.

The production LLM loop now passes this limit directly to the existing runner
cap.

## Resulting bound

Under default configuration, one chat turn now has a finite application-level
tool-call envelope:

- finite LLM cycles;
- at most 10 dispatched tool calls per cycle;
- bounded individual tool execution time.

This does not claim every downstream provider has identical latency or cost.

## Evidence

Results:

`docs/security/evidence/phase11-action-11.11-resource-bound-results.txt`

SHA-256:

`4f3836b8252d60039160b883767866d2456c6c54a92b371932ad8c944ebf21ca`

Source trace:

`docs/security/evidence/phase11-action-11.11-resource-bound-source-trace.txt`

SHA-256:

`086f7e1bf3a35ae6f7f0d9fc1d01e29bcb43e1d48eb6b3c2ebbac790558162e3`

Regression:

`backend/tests/unit/onyx/chat/test_phase11_agent_resource_bounds.py`

## Completion

**ACTION 11.11: COMPLETE**

**H11-04: REMEDIATED**

**RESULT=PHASE_11_ACTION_11_11_PASS**
