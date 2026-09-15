# Phase 6 - Onyx Baseline and System Reverse Engineering
Phase 6 status: **IN PROGRESS**.
## Objective
Establish a reproducible Onyx source and runtime baseline, reverse engineer
the system architecture and security-relevant flows, identify trust and
privilege boundaries, and preserve evidence before later threat modeling
and security testing.
## Safety boundary
- Authorized local learning environment only.
- Synthetic data only.
- No production/customer data.
- No production credentials.
- No paid APIs or billable services.
- No external AI provider invocation.
- No active vulnerability testing during baseline reverse engineering.
- Active testing must remain bounded and separately authorized.
## Phase 5 parent
- Branch: `security/phase-5-ai-foundations`
- Closure SHA: `c1725814f8825681c9d3f739d62ba55300489d85`
## Action 6.1 - Establish and Pin Onyx Target Baseline
Status: **COMPLETE**.
### Target provenance
- Repository: `https://github.com/onyx-dot-app/onyx.git`
- Target branch: `main`
- Pinned commit: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Commit date: `2026-09-15T02:03:45Z`
- Commit subject: `chore(dev): upgrade onyx-devtools to 0.13.7 (#14725)`
- Local target path: `/home/ahmed/projects/onyx-phase6`
- Acquisition mode: shallow clone, depth 1
### License boundary
- Source under `ee` directories: Onyx Enterprise License.
- Source outside documented enterprise/restricted directories: MIT Expat.
- LICENSE SHA256: `d4847240794058c7ac3cfdf8e5d528fe8b0edf15b32a96612ecb9b3e182092b7`
### Current limitations
- Deployment edition/mode has not yet been established.
- Onyx has not been built or started.
- Runtime architecture has not yet been verified.
- Authentication and authorization flows have not yet been traced.
- RAG, agent, tool, MCP, queue, cache, logging and deletion flows remain unverified.
- Git history outside the pinned shallow revision was not acquired.
### Evidence
`docs/security/evidence/phase6-target-provenance-evidence.md`
## Action 6.2 - Documentation and Repository Topology Reconnaissance
Status: **COMPLETE**.
The exact pinned Onyx working tree was inspected without executing the
application.
Observed inventory:
- root objects: 44
- root directories: 20
- tracked files: 7751
- documentation/governance candidates captured: 200
- build/package candidates captured: 25
- deployment/infrastructure candidates captured: 250
- security-relevant path candidates captured: 300
- AI/RAG/agent path candidates captured: 400
- data/queue/storage path candidates captured: 300
Path-name searches were treated only as reconnaissance heuristics. They do
not yet establish component purpose, trust boundaries, security guarantees,
or vulnerabilities.
### Evidence
`docs/security/evidence/phase6-repository-topology-evidence.md`
### Next reverse-engineering question
Determine the actual major application components, their responsibilities,
their startup/deployment relationships, and the first candidate trust
boundaries using source and configuration evidence.
## Action 6.3 - Major Component and Responsibility Mapping
Status: **COMPLETE**.
Source code, deployment configuration, build metadata and documentation from
the exact pinned Onyx revision were analyzed to establish the first
component-responsibility model.
Observed architectural categories include:
- web/client application;
- backend API surface;
- authentication/authorization code;
- persistence infrastructure;
- cache/queue infrastructure;
- background workers;
- connectors and document ingestion;
- search/index infrastructure;
- model-serving infrastructure;
- MCP functionality;
- sandbox/execution functionality;
- deployment/configuration infrastructure.
These categories are evidence-backed repository/deployment observations.
Runtime communication and security properties remain unverified.
### Evidence
`docs/security/evidence/phase6-component-responsibility-map.md`
### Next reverse-engineering question
Trace the actual startup paths and service-to-service relationships so that
the provisional component inventory can be converted into an evidence-backed
architecture and data-flow graph.
## Action 6.4 - Startup and Service Relationship Trace
Status: **COMPLETE**.
Static source and deployment analysis traced startup configuration and major
service relationships without executing Onyx.
Startup dependency, candidate application data flow, and candidate trust
boundaries were kept as separate concepts.
### Evidence
`docs/security/evidence/phase6-startup-service-relationship-trace.md`
### Next
Trace the security-critical request path:
external request -> ingress/web -> API -> authentication -> tenant context ->
authorization decision -> protected resource.
## Action 6.5 - Identity and Request-Context Flow Trace
Status: **COMPLETE**.
Static source analysis traced the major security layers between request entry
and protected-resource access:
- application/router entry;
- authentication backend;
- user identity;
- tenant context;
- route/feature permissions;
- tenant-aware data access;
- object/document access control.
The analysis explicitly separates authentication, tenant resolution,
feature-level authorization and object-level authorization.
No runtime authorization claim or vulnerability claim was made.
### Evidence
`docs/security/evidence/phase6-identity-request-context-flow.md`
### Next reverse-engineering question
Trace the complete document lifecycle:
connector or upload -> fetch -> processing -> embedding/indexing -> search ->
retrieval -> user access filtering -> context supplied to AI.
This will establish the core RAG data-flow model.
## Action 6.6 - Document and RAG Data-Flow Trace
Status: **COMPLETE**.
Static source analysis traced the provisional document/RAG lifecycle:
connector or upload -> acquisition -> processing -> chunking -> embedding ->
indexing -> tenant/access metadata -> retrieval -> access filtering ->
reranking -> AI context.
The analysis identified two especially important security properties for
later runtime verification:
1. tenant identity must remain attached to content throughout indexing and
   retrieval;
2. authorization metadata must remain synchronized and must be enforced before
   retrieved content reaches AI-visible context.
No connector, model, index backend or LLM was executed.
### Evidence
`docs/security/evidence/phase6-document-rag-data-flow-trace.md`
### Next reverse-engineering question
Trace the LLM/chat-generation path in detail:
user message -> conversation/session ownership -> prompt construction ->
retrieved context -> model configuration/provider -> generation/streaming ->
citations/output persistence.
This will establish the model-interaction trust boundaries.
## Action 6.7 - LLM and Chat Generation Flow Trace
Status: **COMPLETE**.
Static source analysis traced the provisional chat-generation lifecycle:
request -> conversation/session -> user message -> prompt construction ->
retrieved context -> model/provider selection -> model invocation ->
streaming/citations/output -> persistence.
The action identified conversation ownership, prompt assembly, RAG-to-model
context transfer, provider boundaries, streaming, citations and persistent
chat state as security-critical surfaces.
No model or external provider was invoked.
### Evidence
`docs/security/evidence/phase6-llm-chat-generation-flow-trace.md`
### Next reverse-engineering question
Trace agents, actions, tools, MCP and code-execution boundaries:
model decision -> tool selection -> authorization -> arguments -> execution ->
result -> model context.
This will establish the highest-risk capability boundary in the application.
## Action 6.8 - Agent, Tool, MCP and Code-Execution Flow Trace
Status: **COMPLETE**.
Static source analysis traced the provisional capability-execution lifecycle:
model decision -> tool availability -> structured tool call -> argument
processing -> authorization/credential boundary -> execution -> result ->
subsequent model context.
MCP discovery/invocation and code-interpreter execution surfaces were traced
as separate high-risk capability boundaries.
No tool, MCP server or executable sandbox was invoked.
### Evidence
`docs/security/evidence/phase6-agent-tool-mcp-code-execution-flow-trace.md`
### Next reverse-engineering question
Trace long-lived state transitions and asynchronous propagation:
delete/revoke/change -> database -> queue/worker -> index/cache/object storage ->
logs/audit -> observable final state.
This will establish deletion, reindexing, revocation, cache, queue and audit
behavior for later consistency and security testing.
## Action 6.9 - Lifecycle State Propagation Trace
Status: **COMPLETE**.
Static analysis traced deletion, permission revocation, MCP/tool revocation,
chat/session retention, file/object deletion, credential lifecycle, asynchronous
queues, index updates, cache invalidation, retries, concurrency controls and
security-relevant logging.
The central security conclusion is that deletion or revocation is not a single
database event. Security depends on downstream representations converging on the
new authoritative state.
### Evidence
`docs/security/evidence/phase6-lifecycle-state-propagation-trace.md`
### Next reverse-engineering question
Create a consolidated security asset inventory covering data stores, model
providers, credentials/secrets, queues, caches, files, external services and
trust dependencies.
This will prepare Phase 6 for synthetic runtime fixtures and controlled
verification.
## Action 6.10 - Security Asset, Data, Secret and Dependency Inventory
Status: **COMPLETE**.
Static analysis produced a consolidated inventory of data stores, identity
state, AI/model assets, RAG-derived data, tools/MCP capabilities, credential
mechanisms, external connectors, queues/caches, file/blob storage,
observability data, dependency manifests and deployment/container inputs.
Secret-related configuration was recorded by identifier only; secret values
were not collected.
### Evidence
`docs/security/evidence/phase6-security-asset-data-secret-dependency-inventory.md`
### Next reverse-engineering question
Create controlled synthetic tenant, user, group, document, credential and
capability fixtures that map directly onto the architecture discovered in
Actions 6.1 through 6.10.
Those fixtures will become the reusable test identities and data for later
authorization, RAG, agent, MCP, deletion and isolation verification.
## Action 6.11 - Synthetic Tenant, Identity and Data Fixture Design
Status: **COMPLETE**.
A deterministic synthetic security fixture universe was defined for later
authorization, tenant-isolation, RAG, prompt-injection, tool, MCP, revocation
and deletion tests.
The design includes Tenant Alpha and Tenant Beta, users, groups, synthetic
credentials, documents with different intended access scopes, adversarial
retrieval content, capability fixtures and explicit expected ALLOW/DENY
outcomes.
No Onyx runtime state was created.
### Fixture manifest
`docs/security/fixtures/phase6-synthetic-security-fixture-manifest.md`
### Evidence
`docs/security/evidence/phase6-synthetic-tenant-identity-data-fixture-design.md`
### Next reverse-engineering question
Design the local mock-service contract for LLM, embedding, reranking, MCP,
webhook, email and file boundaries so later runtime verification can exercise
Onyx without paid APIs or uncontrolled external calls.
## Action 6.12 - Local Mock-Service Contract and Safety Design
Status: **COMPLETE**.
A deterministic loopback-only safety contract was defined for local LLM,
embedding, reranking, MCP, webhook, email and file/object mocks.
The contract establishes synthetic-only inputs, bounded resources,
deterministic adversarial and failure scenarios, loopback-only endpoints,
evidence requirements, stop conditions and prohibition of intentional
external forwarding.
No mock service was implemented or started.
### Contract
`docs/security/fixtures/phase6-local-mock-service-contract.md`
### Evidence
`docs/security/evidence/phase6-local-mock-service-contract-safety-design.md`
### Next reverse-engineering question
Determine the exact Onyx edition/deployment mode and whether this local host
can safely support the selected baseline before any application startup.
## Action 6.13 - Edition, Deployment Mode and Host Suitability
Status: **COMPLETE**.
The pinned Onyx deployment definitions and current local host resources were
evaluated before runtime startup.
Decision:
- Full Standard local runtime: **DEFERRED**
- Selective local baseline: **APPROVED**
- Mock-assisted local baseline: **APPROVED**
- Application startup: **NOT YET AUTHORIZED**
This closes original Phase 6 requirement R6.5.
### Evidence
`docs/security/evidence/phase6-edition-deployment-host-suitability-decision.md`
### Next requirement
Original R6.6: establish a reproducible installation/build procedure before
starting Onyx.
## Action 6.14 - Reproducible Installation and Build Plan
Status: **COMPLETE**.
Pinned-source manifests, lockfiles, container inputs, version signals and
installation/build command references were inventoried.
A reproducible Lite/selective, mock-assisted installation/build procedure was
defined.
No dependency installation, image download, build or application startup was
performed.
Original R6.6 status:
**PROCEDURE COMPLETE - EXECUTION VALIDATION PENDING**
### Evidence
`docs/security/evidence/phase6-reproducible-install-build-plan.md`
### Next runtime question
Can the smallest approved prerequisite/build validation be executed on this
host without exceeding resource, network or cost boundaries?
## Action 6.15 - Bounded Build Prerequisite Validation
Status: **COMPLETE**.
A bounded executable validation was performed without dependency installation
or application startup.
The local Python interpreter satisfies the pinned repository minimum and
successfully parsed 100 pinned Onyx Python files.
The local host remains unsuitable for the first Compose build because required
Docker/Compose and other pinned build tools are unavailable.
A repository devcontainer path was observed, so a bounded Codespace build
validation is conditionally approved subject to the zero-cost safety boundary.
Original R6.6 remains:
**PROCEDURE COMPLETE - PARTIAL EXECUTION PROOF - FULL BUILD PENDING**
### Evidence
`docs/security/evidence/phase6-bounded-build-prerequisite-validation.md`
### Next step
Perform the smallest reproducible dependency/build validation in an approved
environment while preserving the pinned SHA and zero-cost/external-service
boundaries.
