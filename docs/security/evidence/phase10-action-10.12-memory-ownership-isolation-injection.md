# Phase 10 — Action 10.12 Memory Ownership, Isolation and Injection

## Objective

Assess memory ownership, mutation boundaries, and memory-content instruction
integrity.

## Ownership chain

authenticated user
→ get_memories(user)
→ UserMemoryContext.user_id
→ MemoryTool
→ MemoryToolResponse
→ llm_loop persistence
→ add_memory / update_memory_at_index
→ Memory.user_id-scoped database operation

## Ownership properties

Memory reads are scoped by:

`Memory.user_id == user.id`

Memory updates are scoped by:

`Memory.user_id == user_id`

Persistence receives the owner from:

`user_memory_context.user_id`

The model-facing MemoryTool exposes memory text but no user_id, tenant_id, or
owner_id selector.

**MEMORY OWNERSHIP PROPERTY: PASS**

## Memory-disabled behavior

`without_memories()` removes stored memory text while preserving current user
identity and user information.

**PASS**

## H10-05 — memory instruction/data boundary

The baseline memory-update prompt embedded chat history, existing memories, and
new memory content without explicitly classifying those values as untrusted
data.

The prompt was hardened so those fields cannot legitimately:

- override the memory-update task;
- change ownership or identity;
- authorize tools;
- request secrets;
- change the required JSON output schema.

The regression verifies the security notice occurs before synthetic hostile
memory content.

**H10-05: REMEDIATED**

## Regression

Five deterministic tests passed.

An earlier test run failed only because its assertion expected a security phrase
to occupy one physical line while the prompt wrapped the phrase across a
newline.

The test now normalizes whitespace before comparison.

That was a test-harness defect, not a product security finding.

## Limitations

Verified:

- source ownership flow;
- direct deterministic unit/property behavior;
- instruction/data prompt boundary.

Not claimed:

- live tenant-alpha versus tenant-beta DB isolation;
- real LLM resistance to every memory injection;
- production deployment behavior.

Live runtime isolation remains for Action 10.15.

## Findings

**CROSS-USER MEMORY OWNERSHIP BYPASS CONFIRMED: NO**

**H10-05 MEMORY PROMPT BOUNDARY: REMEDIATED**

**MODEL MEMORY-INJECTION COMPROMISE: NOT CLAIMED**

## Evidence

Results:

`docs/security/evidence/phase10-action-10.12-memory-security-results.txt`

SHA-256:

`ebeeb3b76ac5e8377d8d673ead6b763893f994e4ab0e208701fd1d9c49303742`

Source trace:

`docs/security/evidence/phase10-action-10.12-memory-security-source-trace.txt`

SHA-256:

`5ad671ed21a5fca209eebeb70ea55d0625766de8a8fb8740f2a4abbb58a27f4c`

Regression:

`backend/tests/unit/onyx/tools/tool_implementations/memory/test_memory_security_boundaries.py`

## Safety

- synthetic data: **YES**
- DB mutations: **0**
- LLM calls: **0**
- HTTP requests: **0**
- external application network requests: **0**
- real credentials/data: **0**

## Completion

**ACTION 10.12: COMPLETE**

**RESULT=PHASE_10_ACTION_10_12_PASS**
