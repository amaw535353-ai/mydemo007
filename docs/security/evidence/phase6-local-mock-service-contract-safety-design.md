# Phase 6 Action 6.12 - Local Mock-Service Contract and Safety Design
## Purpose
Define deterministic local substitutes for external AI and application
dependencies for later controlled Onyx runtime verification.
Action 6.12 is design-only.
No mock service was started.
## Verified Baseline
- Evidence branch: `security/phase-6-onyx-baseline`
- Parent commit: `3f15c71866e6495f16e8eda23d52272dd4ddb45e`
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx source clean: PASS
## Contract Artifact
`docs/security/fixtures/phase6-local-mock-service-contract.md`
## Source Mapping
Bounded static source signals:
- LLM/provider: 300
- embedding/model server: 300
- reranker: 122
- MCP: 295
- webhook/network side effect: 143
- email: 250
- file store: 245
These counts establish architectural relevance only.
They do not prove runtime protocol compatibility.
## Reserved Local Services
- MOCK-LLM: 127.0.0.1:18080
- MOCK-EMBEDDING: 127.0.0.1:18081
- MOCK-RERANKER: 127.0.0.1:18082
- MOCK-MCP: 127.0.0.1:18083
- MOCK-WEBHOOK: 127.0.0.1:18084
- MOCK-EMAIL: 127.0.0.1:18085
- MOCK-FILE: 127.0.0.1:18086
## Bounded Safety Policy
Maximum limits:
- concurrent requests: 10;
- requests per test: 100;
- request body: 1 MB;
- generated response: 1 MB;
- test duration: 60 seconds;
- network binding: loopback only;
- outbound internet: prohibited;
- production credentials: prohibited;
- production/customer data: prohibited.
## Security Principle
Dependency behavior is not authorization.
A mock LLM, reranker or MCP server may deliberately produce adversarial
content.
Application controls must independently enforce:
- authenticated identity;
- tenant identity;
- object authorization;
- capability authorization;
- credential scope;
- network policy;
- execution policy.
## Adversarial Dependency Scenarios
The contract includes deterministic support for:
- unauthorized tool requests;
- prompt-injection-following model behavior;
- adversarial reranking;
- malicious MCP tool descriptions;
- malicious MCP results;
- cross-tenant capability advertisement;
- bounded errors and timeouts;
- malformed or stale synthetic results.
## Side-Effect Evidence
Local webhook and email boundaries may later act as tripwires for unauthorized
state-changing behavior without causing external real-world side effects.
## Interpretation Boundary
Action 6.12 does not prove:
- runtime mock compatibility;
- LLM integration;
- embedding integration;
- reranking integration;
- MCP integration;
- network isolation;
- authorization correctness;
- sandbox isolation.
Those remain later runtime verification targets.
## Safety Record
- Onyx started: NO
- Docker started: NO
- mock service started: NO
- network listener created: NO
- external API contacted: NO
- model invoked: NO
- MCP server contacted: NO
- webhook sent: NO
- email sent: NO
- real credential used: NO
- production/customer data used: NO
- Onyx source modified: NO
## Result
Action 6.12 local mock-service contract and safety design: **PASS**.
