# Phase 12 — Action 12.4 Collection, Minimization and Purpose Boundaries

## Objective

Identify implementation controls that reduce collection or persistence when the
product is operating in a content-minimized mode.

## Verified controls

The incognito/content-free design includes:

- metadata-only session policy;
- Redis-backed ephemeral conversation context;
- one-hour sliding idle TTL;
- message-count bound;
- byte-size bound;
- image removal from persisted ephemeral context;
- content-free chat-title suppression;
- content-free file-descriptor minimization.

## Provider-side minimization

For content-free operation, the source includes provider-specific attempts to
reduce provider retention/logging, including:

- OpenAI/Azure `store=False`;
- OpenRouter data-collection deny routing;
- Bifrost content-logging suppression;
- LiteLLM proxy message redaction;
- Portkey logging/tracking suppression behavior.

## Evidence limitation

Provider-side controls are configuration/API requests made by Onyx.

This action does not claim independent proof that every external provider
honors those settings in production.

## Finding classification

**NO COLLECTION-OVERREACH FINDING CONFIRMED BY THIS ACTION**

Provider egress is tested separately in Action 12.8.

## Evidence

Results:

`docs/security/evidence/phase12-action-12.4-minimization-results.txt`

SHA-256:

`a6e1f06da12433cd9ea544b6d9c7604fe1e7ae700ec9ecaeab27bb7a2d8656d8`

Source trace:

`docs/security/evidence/phase12-action-12.4-minimization-source-trace.txt`

SHA-256:

`f9785e039b2eeb98053c58c4b2464ede3b4587c70256e1a0af47d23bb994edbe`

Test:

`backend/tests/unit/onyx/chat/test_phase12_data_minimization_controls.py`

## Completion

**ACTION 12.4: COMPLETE**

**RESULT=PHASE_12_ACTION_12_4_PASS**
