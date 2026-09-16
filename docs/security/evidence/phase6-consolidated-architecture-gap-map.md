# Phase 6 Action 6.19 - Consolidated Architecture and Gap Map

## Baseline

- Evidence parent: `35b8db9f200f41f4b5e802b64d00da764385d4cc`
- Pinned Onyx SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx source modified: NO
- Phase 6 evidence files verified through Action 6.18: 18
- Phase 6 related artifacts currently inventoried: 21

## Purpose

Consolidate the architecture knowledge produced during Phase 6 and explicitly
separate:

1. static/source evidence;
2. bounded executable evidence;
3. live runtime evidence;
4. remaining deferred evidence.

This prevents static architecture understanding from being mistaken for
runtime security verification.

---

# 1. Consolidated Logical Architecture

```text
                           USER / BROWSER
                                 |
                                 v
                       +-------------------+
                       |      Web / UI     |
                       +-------------------+
                                 |
                          HTTP / API path
                                 |
                                 v
                    +------------------------+
                    |    Application API     |
                    |       / Backend        |
                    +------------------------+
                       |          |        |
                       |          |        |
                       v          v        v
                Identity /    Document /  Conversation /
                Request       Ingestion    Generation
                Context          |            |
                    |            v            v
                    |       Retrieval /    LLM / Model
                    |        RAG path       Provider path
                    |            |
                    |            v
                    |       Indexed /
                    |       Retrieved Data
                    |
                    +-----------------------------+
                                                  |
                                                  v
                                    Agent / Action / Tool
                                                  |
                                      +-----------+-----------+
                                      |                       |
                                      v                       v
                                     MCP                Code / Execution
                                      |                       |
                                      +-----------+-----------+
                                                  |
                                                  v
                                          External-effect
                                          trust boundary

Supporting logical roles observed in deployment/source evidence:

- relational persistence;
- cache / queue roles;
- search / vector roles;
- background processing;
- model-serving roles;
- object/file-storage roles;
- logging / audit / lifecycle paths.
```

This is a logical security architecture map.

It is not evidence that every listed component was running simultaneously on
the current workstation.

---

# 2. Primary Trust Boundaries

## Boundary A - User / Browser to Application

Security questions include:

- authentication state;
- request ownership;
- session/token handling;
- route authorization;
- object authorization.

Static architecture evidence exists.

Live browser/API enforcement is not yet proven.

## Boundary B - Identity Context to Tenant Data

Security questions include:

- tenant resolution;
- object ownership;
- cross-tenant access;
- authorization propagation;
- revocation.

Static identity/request-context evidence exists.

Runtime tenant-isolation correctness is deferred to later security phases.

## Boundary C - Documents to Retrieval / RAG

Security questions include:

- ingestion authorization;
- document ownership;
- retrieval filtering;
- malicious retrieved instructions;
- vector/index isolation.

Static RAG/data-flow evidence exists.

Live retrieval behavior has not been observed.

## Boundary D - Application to LLM / Model Provider

Security questions include:

- prompt/data disclosure;
- provider configuration;
- model trust;
- response handling;
- cost/resource control.

Static generation/model-provider paths are mapped.

No real external LLM call was performed.

## Boundary E - Model Output to Tools / MCP / Actions

Security questions include:

- tool authorization;
- argument validation;
- privilege boundaries;
- dangerous side effects;
- code execution;
- sandboxing.

Static tool/MCP/code-execution paths are mapped.

Runtime enforcement effectiveness is not yet proven.

## Boundary F - Application to Persistence / Queue / Cache

Security questions include:

- state propagation;
- lifecycle consistency;
- deletion;
- stale authorization state;
- logging/audit behavior.

Static lifecycle evidence exists.

Live state propagation has not been exercised.

---

# 3. Evidence Classification

```
PROVEN_STATIC:
- pinned repository provenance
- repository topology
- component responsibilities
- static startup/service relationships
- identity/request-context code paths
- document/RAG code paths
- LLM/chat-generation code paths
- agent/tool/MCP/code-execution code paths
- lifecycle-state code paths
- security asset/data/secret/dependency inventory
- synthetic fixture design
- local mock-service contract design
- edition/deployment-mode selection
- build/install procedure
- startup/readiness contract
- test architecture inventory

PROVEN_BOUNDED_EXECUTION:
- Python 3.13 compatibility check
- bounded Python source parsing
- structured JSON/TOML parsing
- shell-script syntax validation
- reproducibility-input hashing
- bounded Python test-file syntax validation

NOT_PROVEN_LIVE:
- complete dependency synchronization
- complete frontend build
- Docker image/container build
- live Onyx startup
- live health/readiness success
- browser-to-API request execution
- runtime authentication enforcement
- runtime authorization enforcement
- runtime tenant-isolation behavior
- live document ingestion
- live retrieval/vector behavior
- live LLM/model-provider interaction
- live mock LLM interaction
- live MCP/tool/action execution
- runtime sandbox effectiveness
- live queue/cache behavior
- live audit/log propagation
- full pytest suite
- full Jest/Playwright/frontend suite
- full integration/container suite
```

---

# 4. Phase 6 Requirement Status

## R6.1 - Target provenance

**COMPLETE**

Pinned source and repository provenance recorded.

## R6.2 - Documentation / repository topology

**COMPLETE**

Repository structure inventoried.

## R6.3 - Component / responsibility map

**COMPLETE**

Static component responsibilities mapped.

## R6.4 - Startup / service relationships

**COMPLETE STATICALLY**

Runtime execution remains deferred.

## R6.5 - Edition / deployment mode and host suitability

**COMPLETE**

Selective local baseline and mock-assisted strategy approved.

## R6.6 - Reproducible installation / build

**PARTIAL EXECUTION / DOCUMENTED DEFERRED PORTION**

Completed:

- procedure;
- version pins;
- configuration parsing;
- bounded Python validation;
- lock/reproducibility evidence.

Deferred:

- dependency synchronization;
- full application/container/frontend build.

## R6.7 - Startup / service baseline

**STATIC BASELINE COMPLETE**

Deferred:

- live startup;
- live readiness;
- live health observation.

## R6.8 - Test inventory / execution

**INVENTORY + BOUNDED VALIDATION COMPLETE**

Repository inventory observed:

- Python tests: 1207
- Python unit paths: 717
- Python integration paths: 178
- JS/TS tests/specs: 323

300 Python test files passed syntax parsing.

No dependency-free repository unittest candidate satisfied the conservative
execution filter.

Therefore:

- actual selected repository tests executed: 0;
- full test suites: deferred.

This must not be interpreted as test-suite success.

## R6.9 - Component / service inventory refinement

**STATICALLY SUBSTANTIAL**

Runtime service-state refinement remains unavailable without a running stack.

## R6.10 - Identity / secrets / configuration

**STATIC BASELINE COMPLETE**

Runtime security correctness is deferred to later testing phases.

## R6.11 - Browser to API

**STATIC PATH MAPPED**

Live browser/API request evidence is deferred.

## R6.12 - Authentication / authorization

**STATIC PATH MAPPED**

Runtime enforcement testing belongs to later security phases.

## R6.13 - Ingestion / RAG

**STATIC PATH MAPPED**

Live ingestion/retrieval behavior remains deferred.

## R6.14 - Generation / model provider

**STATIC PATH MAPPED**

No real provider traffic was authorized.

## R6.15 - Agent / action / MCP / tool / code execution

**STATIC PATH MAPPED**

Runtime control effectiveness remains deferred.

## R6.16 - Queue / cache / log / audit / deletion

**STATIC LIFECYCLE PATHS MAPPED**

Runtime consistency remains unobserved.

## R6.17 - Asset / data / model / trust / dependency inventory

**COMPLETE STATIC BASELINE**

## R6.18 - Synthetic tenants / users / documents

**COMPLETE DESIGN BASELINE**

Synthetic fixture artifacts exist.

## R6.19 - Local mocks / normal behavior

**CONTRACT COMPLETE - EXECUTION DEFERRED**

Mock endpoints, safety limits and deterministic behavior are defined.

Mock runtime behavior has not been executed.

## R6.20 - Maps / limitations / completion gate

Architecture and limitations are now consolidated by Action 6.19.

Final completion gate remains Action 6.20.

---

# 5. Explicit Remaining Runtime Gap Register

| Gap | Current status | Phase 6 treatment |
|---|---|---|
| Full dependency installation | Not observed | Deferred |
| Full backend build | Not observed | Deferred |
| Full frontend build | Not observed | Deferred |
| Docker/Compose runtime | Unavailable | Deferred |
| Live Onyx startup | Not observed | Deferred |
| Live health checks | Not observed | Deferred |
| Browser-to-API requests | Not executed | Deferred |
| Runtime authentication | Not tested | Later phase |
| Runtime authorization | Not tested | Later phase |
| Runtime tenant isolation | Not tested | Later phase |
| Live document ingestion | Not executed | Later phase |
| Live RAG retrieval | Not executed | Later phase |
| Live model interaction | Not executed | Mock/later phase |
| Mock service runtime | Contract only | Deferred |
| MCP/tool execution | Not executed | Later phase |
| Code-execution controls | Not executed | Later phase |
| Runtime lifecycle propagation | Not executed | Later phase |
| Full Python tests | Not executed | Deferred |
| Frontend/Jest tests | Not executed | Deferred |
| Playwright tests | Not executed | Deferred |
| Integration/container tests | Not executed | Deferred |

---

# 6. What Phase 6 Can Legitimately Claim

Phase 6 has established a reproducible, source-pinned, evidence-backed
understanding of the Onyx architecture sufficient to begin formal threat
modeling and targeted security-testing phases.

Phase 6 can claim:

- source provenance;
- architectural understanding;
- primary data-flow understanding;
- major trust-boundary identification;
- identity/RAG/model/tool path identification;
- security asset inventory;
- synthetic test-fixture design;
- mock-service safety contract;
- bounded source/configuration validation;
- host/build/runtime limitation documentation.

Phase 6 cannot claim:

- a successful full Onyx build;
- a successful live Onyx deployment;
- successful full test suites;
- runtime tenant isolation;
- runtime authorization correctness;
- successful RAG isolation;
- successful prompt-injection resistance;
- safe tool/MCP enforcement;
- effective code sandboxing;
- production readiness.

Those require later runtime security work.

---

# 7. Architecture Principle Carried Forward

The following distinction remains mandatory:

**Repository component != active runtime**

**Configuration declaration != runtime exposure**

**Security-control code != runtime enforcement**

**Static path mapping != successful security behavior**

**Test inventory != passing tests**

**Mock contract != executed mock behavior**

These boundaries will be preserved in Phase 7 and later phases.

---

# Result

Action 6.19 architecture and evidence-gap consolidation:

**PASS**

The Phase 6 evidence set is ready for the final completion-gate audit.
