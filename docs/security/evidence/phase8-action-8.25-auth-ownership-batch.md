# Phase 8 Action 8.25 - Authentication and Object Ownership Batch

## Result

**PASS**

## Runtime

- UTC: 2026-09-16T20:02:45Z
- Onyx SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Runtime: Onyx Standard API core
- API health: HTTP 200
- Model server disabled
- Hugging Face offline mode enabled
- Onyx telemetry disabled
- Remote disposable-domain refresh disabled
- Synthetic-only test data

## Actors

- Alice: `phase8-alice-20260916200242-24324@example.com`
- Bob: `phase8-bob-20260916200242-24324@example.com`

Passwords and cookie values are excluded from repository evidence.

## Objects

- Alice chat: `246f45b4-e0a3-4f88-a045-6b5737800620`
- Bob chat: `0d4a53c5-450e-40f6-8180-31894bdc4384`

## Results

| Test | Observation | Result |
|---|---|---|
| TC8-002 | Alice own read HTTP 200 | **PASS** |
| TC8-003 | Alice -> Bob read HTTP 403 | **PASS** |
| TC8-004 | Alice -> Bob PATCH HTTP 400; PRIVATE_UNCHANGED | **PASS** |
| TC8-005 | Alice -> Bob DELETE HTTP 400; Bob post-read HTTP 200 | **PASS** |
| TC8-008 | Alice/Bob admin endpoint HTTP 403 / 403 | **PASS** |

## Safety

- Authorized Codespace only
- Synthetic users/resources only
- No production credentials
- No customer data
- Concurrency 1
- Bounded request count
- Hugging Face Hub forced offline
- Onyx telemetry disabled
- Disposable-domain remote refresh disabled
