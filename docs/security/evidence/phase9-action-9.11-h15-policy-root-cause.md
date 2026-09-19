# Phase 9 Action 9.11 — H9-15 Policy and Root-Cause Analysis

## Status

**ROOT CAUSE ESTABLISHED — SECURITY REQUIREMENT DEFINED — REMEDIATION REQUIRED**

Runtime evidence:
`docs/security/evidence/phase9-action-9.10-runtime-slice7-h15.md`

Tracking: GitHub Issue #4.

## SR-H9-15

Revoking access to a non-default persona must prevent future execution using that persona or its derived capabilities, including future turns in an already-created session.

Historical chat read access is a separate authorization decision and must not itself authorize future persona execution.

## Runtime result

- persona access existed before revocation;
- existing session was created successfully;
- persona access was then revoked;
- new-session creation was denied with HTTP 403;
- the old session remained usable;
- core message execution continued after revocation;
- the reproduction used no persona tools, so post-revocation tool execution is not claimed.

## Source-backed asymmetry

New-session path:
`backend/onyx/chat/chat_utils.py:160-197`

`create_chat_session_from_request()` checks current access with `user_can_access_persona(...)`.

Existing-session path:
`backend/onyx/chat/process_message.py:634-661`

`build_chat_turn()` loads the owned session with `get_chat_session_by_id(...)`, eagerly loads its persona, and continues with `persona = chat_session.persona`.

The existing-session branch does not perform an equivalent fresh `user_can_access_persona(...)` decision before execution.

Session ownership primitive:
`backend/onyx/db/chat.py:41-70`

Chat-session ownership and current persona-share authorization are distinct security properties.

Persona-derived capability construction later reaches:
`backend/onyx/chat/process_message.py:1337-1365`

## RC-H9-15

**Persona authorization is checked when the session is created but is not equivalently revalidated before a future turn in an already-owned session.**

This creates stale authorization after persona-share revocation.

## Required invariant

Before a future turn executes with a non-default persona, current server-side `user_can_access_persona(...)` authorization must still succeed.

Session ownership alone must not act as continuing persona authorization.

## Remediation direction

Add current persona-access validation to the existing-session branch of `build_chat_turn()` before LLM execution, tool construction, knowledge access, delegated credentials, custom actions, MCP execution, or other persona-derived effects.

Historical chat read/delete behavior remains a separate policy decision.

## Regression requirements

- H9-15-R1: authorized existing persona session — ALLOW.
- H9-15-R2: revoked persona new session — DENY.
- H9-15-R3: revoked persona existing session future turn — DENY.
- H9-15-R4: historical session read follows separate policy.
- H9-15-R5: default persona remains functional.
- H9-15-R6: currently authorized principals remain functional.
- H9-15-R7: revoked persona tool construction is not reached.

## Classification

**CONFIRMED AUTHORIZATION REVOCATION GAP UNDER SR-H9-15**

This classification is based on the assessment security requirement and does not claim that upstream Onyx previously documented a conflicting revocation contract.

## Result

**H9-15_ROOT_CAUSE_CONFIRMED_AND_READY_FOR_REMEDIATION**
