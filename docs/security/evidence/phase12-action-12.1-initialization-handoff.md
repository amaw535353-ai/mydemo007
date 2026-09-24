# Phase 12 — Action 12.1 Initialization and Privacy Charter

## Parent

Phase 11 final SHA:

`7dc4350614b432edfc0d871e202704b3cf2d4c70`

Phase 11 status:

**COMPLETE — 15/15 ACTIONS**

## Phase 12

Branch:

`security/phase-12-privacy-data-protection-dlp`

Objective:

Assess privacy, sensitive-data handling, retention, deletion, data egress,
redaction and DLP boundaries across the Onyx AI application.

## Authorized laboratory boundary

Allowed:

- owned repository;
- local/Codespaces execution;
- pinned local Docker images;
- synthetic identities;
- synthetic PII;
- synthetic credentials;
- synthetic documents;
- local mock services;
- deterministic unit/property tests;
- bounded integration tests.

Not authorized:

- real customer data;
- real personal data;
- production accounts;
- real credentials;
- public Onyx deployments;
- uncontrolled external systems;
- paid API use;
- public data-exfiltration testing.

## Synthetic privacy fixtures

Examples may include:

- alice@tenant-alpha.test
- bob@tenant-beta.test
- synthetic phone numbers;
- synthetic addresses;
- synthetic employee records;
- synthetic financial-like identifiers;
- fake API tokens;
- synthetic confidential documents.

No fixture may intentionally contain real private data.

## Data classes

Phase 12 distinguishes:

1. public/non-sensitive application data;
2. user identity and account metadata;
3. conversation content;
4. uploaded/generated file content;
5. indexed/retrieved document content;
6. persistent personalization/memory;
7. connector/provider content;
8. credentials, OAuth tokens and secrets;
9. telemetry/log/trace data;
10. usage/billing metadata;
11. security/audit metadata.

## Privacy invariants

1. Data access must remain scoped to the authorized user/tenant.
2. Sensitive values must not be logged merely for observability.
3. Collection should be bounded to application purpose.
4. Incognito/content-free modes must not silently persist conversation content.
5. Provider egress must be explicit and documented.
6. Secrets and credentials require stronger handling than ordinary content.
7. Deletion must identify every persistent copy that is expected to disappear.
8. Intentional retention exceptions must be explicit rather than hidden.
9. Redaction/DLP must operate before an unsafe boundary, not after disclosure.
10. Export/download paths must preserve authorization.
11. Data derived by AI systems remains subject to its source privacy boundary.
12. Cross-user and cross-tenant privacy tests must fail closed.
13. Telemetry must not silently become an uncontrolled secondary data store.
14. Residual privacy risk must remain explicit.
15. Compliance language must not exceed the evidence actually produced.

## Evidence levels

Phase 12 distinguishes:

- STATIC/SOURCE VERIFIED
- PROPERTY VERIFIED
- UNIT VERIFIED
- MOCK INTEGRATION VERIFIED
- BOUNDED LOCAL RUNTIME VERIFIED
- PRODUCTION RUNTIME NOT CLAIMED

## Finding rule

A privacy/security finding requires a concrete adverse property such as:

- unauthorized disclosure;
- unnecessary sensitive-data persistence;
- deletion failure;
- unbounded provider/telemetry egress;
- secret exposure;
- cross-user/cross-tenant leakage;
- missing required redaction;
- DLP/export bypass.

The mere existence of stored data is not itself classified as a vulnerability.

## Fixed Phase 12 plan

1. 12.1 — immutable handoff / privacy charter
2. 12.2 — sensitive-data architecture and data-flow inventory
3. 12.3 — classification / ownership / tenant boundaries
4. 12.4 — collection / minimization / purpose boundaries
5. 12.5 — sensitive-storage / secrets / PII inventory
6. 12.6 — prompt / context / RAG privacy leakage
7. 12.7 — logs / traces / telemetry / error disclosure
8. 12.8 — connector / tool / MCP / provider egress
9. 12.9 — conversation / file / memory retention and deletion
10. 12.10 — DLP / redaction / export / download controls
11. 12.11 — cross-user / cross-tenant privacy negative tests
12. 12.12 — consolidated privacy/DLP attack matrix
13. 12.13 — bounded synthetic privacy runtime
14. 12.14 — findings / regression / framework mapping
15. 12.15 — independent residual-risk final gate

## Completion

**ACTION 12.1: COMPLETE**

**RESULT=PHASE_12_ACTION_12_1_PASS**
