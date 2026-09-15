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
