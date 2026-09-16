# Phase 8 Action 8.26 - Business Logic and Resilience Batch

## Result

**REVIEW_OR_DOCUMENTED_LIMITATION**

## Runtime

- UTC: 2026-09-16T20:06:28Z
- Onyx SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Runtime: Onyx Standard API core
- Synthetic-only lab
- API health before tests: HTTP 200
- Concurrency ceiling used: 4
- Repetition requests: 20
- Large request bytes: 524288

## Results

| Test | Observation | Result |
|---|---|---|
| TC8-007 | Alice cookie + Bob user/object parameters: HTTP 500 | **REVIEW** |
| TC8-009 | Direct foreign PATCH/DELETE from Action 8.25 | **PASS_EVIDENCE_REUSE** |
| TC8-010 | Chat-session owner/foreign isolation from Action 8.25 | **PASS_EVIDENCE_REUSE** |
| TC8-013 | Alice session + conflicting Bob identity headers: HTTP 403 | **PASS** |
| TC8-014 | Logout 204; normal jar 401; stale pre-logout jar 401 | **PASS_STRONG_REVOCATION** |
| TC8-015 | 524288-byte registration request HTTP 400; health 200 | **PASS** |
| TC8-016 | 20 requests / concurrency 4; denied 20; allowed 0; other 0; health 200 | **PASS** |

## Runtime-limited cases

- TC8-006: **DEFER_PHASE9_MULTI_TENANT**
  - Current Phase 8 runtime is single-tenant.
  - No fabricated cross-tenant claim is made.

- TC8-011: **DEFER_PHASE10_RAG_DOCUMENT_RUNTIME**
  - Dedicated RAG/document authorization runtime is deferred to Phase 10.

- TC8-012: **PARTIAL_ADMIN_CONTROL_ONLY**
  - Administrative connector routes have authentication/privilege evidence,
    but dedicated per-owner connector fixtures were not created.

## Interpretation

Evidence reuse is explicitly marked and is not counted as an independent
additional request set.

TC8-014 distinguishes normal browser logout behavior from reuse of the
pre-logout cookie. A stale cookie that remains valid is not automatically
classified as a vulnerability; it requires review against the intended
server-side session-revocation design.

## Safety

- Authorized Codespace only
- Synthetic users/resources only
- No production credentials
- No customer data
- Maximum concurrent requests used: 4
- Maximum repetition requests used: 20
- Large-request fixture remained below 1 MB
- External telemetry/Hugging Face/disposable-domain fetches disabled
