# Phase 2 - Complete System, Asset, and Supply-Chain Inventory

## Evidence Metadata

Captured: 2026-09-14T19:25:44+01:00

Repository:
https://github.com/amaw535353-ai/mydemo007.git

Phase 1 closure commit:
74ac6b78a51567ca31d1302c1941aec172963848

Phase 2 branch:
security/phase-2-inventory

Phase 2 starting commit:
74ac6b78a51567ca31d1302c1941aec172963848

Tracked files:
7658

Dependency/build manifests discovered:
122

Deployment/container/CI/IaC candidates displayed:
250

## Inventory Discipline

Discovery is not confirmation.

A filename, directory, manifest, class, module, or configuration candidate
does not by itself prove that the item is an active runtime asset.

Runtime inventories will require later verification against the approved
local deployment.

Candidate secret, credential, token, key, and certificate filenames are
recorded without displaying their contents.

## Inventory Status

| Domain | Status |
| --- | --- |
| Source-code inventory | DISCOVERY BASELINE ESTABLISHED |
| Repository inventory | DISCOVERY BASELINE ESTABLISHED |
| Service inventory | STATIC DEFINITIONS ENUMERATED; RUNTIME UNVERIFIED |
| Client inventory | STATIC SOURCE SURFACES ENUMERATED; RUNTIME UNVERIFIED |
| API inventory | STATIC ROUTE SURFACES ENUMERATED; RUNTIME UNVERIFIED |
| Endpoint inventory | STATIC ROUTE DEFINITIONS ENUMERATED; RUNTIME UNVERIFIED |
| Identity inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Role inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Permission inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Tenant inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Data inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Dataset inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Document inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Index inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Embedding inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Vector-store inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Memory inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Cache inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Prompt inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Template inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Model inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Provider inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Model-weight inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Adapter inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Agent inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Tool inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Action inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| MCP client inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| MCP server inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| A2A component inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Connector inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Secret inventory | FILENAME DISCOVERY ONLY |
| Token inventory | FILENAME DISCOVERY ONLY |
| Key inventory | FILENAME DISCOVERY ONLY |
| Certificate inventory | FILENAME DISCOVERY ONLY |
| Dependency inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Container inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Image inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Infrastructure inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Cloud-resource inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Vendor inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Supplier inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| License inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| Ownership inventory | PARTIAL FROM PHASE 1 |
| Data-lineage inventory | STATIC SOURCE CANDIDATES ENUMERATED; RUNTIME UNVERIFIED |
| AI-BOM planning | NOT YET COMPLETED |
| SBOM planning | NOT YET COMPLETED |
| CBOM planning | NOT YET COMPLETED |

## Application Source Surfaces

backend: 3741 tracked files
web: 2445 tracked files
desktop: 65 tracked files
cli: 171 tracked files
mobile: 451 tracked files
widget: 20 tracked files
extensions: 27 tracked files
deployment: 228 tracked files
examples: 13 tracked files
tools: 212 tracked files

These are repository source surfaces, not yet verified runtime services.

## Supply-Chain Baseline

Manifest and definition discovery has begun for:

- Python;
- JavaScript/Bun;
- containers;
- Docker Compose;
- Helm;
- Terraform/IaC;
- build configuration;
- version declarations;
- MCP configuration;
- licensing and governance artifacts.

Exact direct and transitive dependencies, package sources, image digests,
signatures, provenance, attestations, runtime versions, and deployed
configuration remain to be inventoried.

## Sensitive Material Rule

Possible sensitive filenames were inventoried by name only.

Their contents were not collected.

## Evidence

docs/security/evidence/phase2-repository-manifest-evidence.md

## Service, Client, API and Endpoint Static Inventory

Static enumeration results:

- Compose service definitions: 144
- Helm/Kubernetes resource-kind definitions: 123
- Client source surfaces: 6
- Client API/transport filename candidates: 136
- Backend static route definitions: 716
- Next.js static route handlers: 22

Interpretation:

These values represent source/configuration definitions at the current
repository commit.

They do not prove that a service is deployed, an endpoint is reachable,
a route has no additional parent prefix, or a client is enabled in the
eventual local deployment.

Runtime reconciliation remains required.

Evidence:

docs/security/evidence/phase2-service-client-api-endpoint-evidence.md


## Action 2.3 - Identity, Role, Permission, and Tenant Static Inventory

Observation class: **SOURCE-OBSERVED; RUNTIME UNVERIFIED**

Static candidate-file counts:

- Identity candidate files: 1136
- Role candidate files: 403
- Permission/authorization candidate files: 956
- Tenant-boundary candidate files: 844

Evidence:

`docs/security/evidence/phase2-identity-role-permission-tenant-evidence.md`

These counts identify source locations for deeper security analysis. They do not prove runtime authentication, authorization, RBAC, permission enforcement, or tenant isolation.


## Action 2.4 - Data, Retrieval, Memory, and Prompt Static Inventory
Observation class: **SOURCE-OBSERVED; RUNTIME UNVERIFIED**
Static candidate-file counts:
- Data: 1931
- Dataset: 37
- Document: 1211
- Index: 824
- Embedding: 198
- Vector store: 5
- Memory: 299
- Cache: 816
- Prompt: 463
- Template: 292
Evidence:
`docs/security/evidence/phase2-data-retrieval-memory-prompt-evidence.md`
These counts identify static source candidates only. They do not
prove runtime data flow, access control, retrieval authorization,
tenant isolation, memory isolation, cache isolation, prompt
provenance, or template safety.

## Action 2.5 - Model, Provider, Model-Weight, and Adapter Static Inventory
Observation class: **SOURCE-OBSERVED; RUNTIME UNVERIFIED**
Static candidate-file counts:
- Model: 2196
- Provider: 1204
- Model weight/checkpoint: 122
- Adapter: 46
Evidence:
`docs/security/evidence/phase2-model-provider-weight-adapter-evidence.md`
These counts are static discovery candidates only. They do not prove
that a model, provider, checkpoint, weight file, or adapter is active
or trusted at runtime.

## Action 2.6 - Agent, Tool, Action, MCP, A2A, and Connector Static Inventory
Observation class: **SOURCE-OBSERVED; RUNTIME UNVERIFIED**
Static candidate-file counts:
- Agent: 695
- Tool: 913
- Action: 807
- MCP client: 14
- MCP server: 191
- A2A component: 0
- Connector: 1399
Evidence:
`docs/security/evidence/phase2-agent-tool-action-mcp-a2a-connector-evidence.md`
These counts identify static source candidates only. They do not prove
that any agent, tool, action, MCP component, A2A component, or connector
is enabled, authorized, reachable, or isolated correctly at runtime.

## Action 2.7 - Supply Chain and Infrastructure Static Inventory
Observation class: **SOURCE-OBSERVED; RUNTIME UNVERIFIED**
Static candidate-file counts:
- Dependency: 834
- Container: 883
- Image: 257
- Infrastructure: 677
- Cloud resource: 694
- Vendor: 67
- Supplier: 2
- License: 200
- Data lineage: 8
Evidence:
`docs/security/evidence/phase2-supply-chain-infrastructure-evidence.md`
These are static discovery candidates only. Runtime deployment,
ownership, provenance, supplier trust, patch status, license
compliance, and lineage integrity remain unverified.
## Phase 2 Completion Gate

Phase 2 remains IN PROGRESS.

Every applicable inventory domain must eventually be:

- evidence-backed and enumerated;
- explicitly marked not applicable with rationale; or
- explicitly recorded as unresolved with a reason.

Phase 2 is not closed by filename discovery alone.
