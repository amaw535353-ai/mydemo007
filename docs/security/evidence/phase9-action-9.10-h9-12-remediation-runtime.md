# Phase 9 — Action 9.10 — H9-12 Remediation Runtime Verification

## Finding

Generated `CHAT_IMAGE_GEN` resources previously allowed an authenticated non-owner read path.

## Remediation

Generated images now carry owner/session authorization metadata. `user_can_access_chat_file()` uses owner/session-aware generated-image authorization instead of the previous unconditional generated-image allow path.

## Focused regression verification

- Focused H9-12 regression suite previously passed: **51/51**.
- Owner access, authenticated non-owner denial, anonymous denial, public/shared behavior, malformed metadata and non-`CHAT_IMAGE_GEN` behavior were covered.

## Final patched-runtime verification — 2026-09-22

- Anonymous HTTP: **403**
- Alice owner HTTP: **200**
- Bob authenticated non-owner HTTP: **404**
- Alice response bytes: **38**
- Alice response SHA-256: `abfdb8d4b8f5247a86f4de23cf39858d3f78c21b323a742dda665309edf8686b`
- `LINKED_TO_ALICE=TRUE`
- `ALICE_CAN_ACCESS=TRUE`
- `BOB_CAN_ACCESS=FALSE`
- `RESULT=PASS`
- `H9-12=SECURITY_PROPERTY_ENFORCED`
- Runbook return code: **0**
- Requests before cleanup: **5**
- Total requests including logout cleanup: **7**

The API remained running and healthy with patched `access.py` SHA-256:

`150317a698c4c84357bf90ed8804a3b239a1d09f628b4d39d9d5d8449561d80c`

Verification used synthetic identities/data, sequential bounded requests, loopback-only routing, automatic cleanup and no Docker image pulls.

The transient `/tmp` runtime transcript was not retained through the later closeout step. The successful result above was observed in the completed operator terminal execution before closeout.

Temporary harness adaptations addressed only stale mechanics: the obsolete vulnerable-source-shape assertion, psql variable transport and enum-display case. They did not alter the Alice/Bob/anonymous authorization assertions.

## Classification

**H9-12 — PASS / REMEDIATED**

Owner access is preserved while anonymous and authenticated non-owner access are denied.
