# Phase 6 Action 6.11 - Synthetic Tenant, Identity and Data Fixture Design
## Purpose
Create a deterministic synthetic security test universe mapped to the
architecture discovered during Phase 6.
No Onyx runtime state was created.
The fixture design establishes expected security outcomes before later active
testing.
## Verified Baseline
- Evidence branch: `security/phase-6-onyx-baseline`
- Action 6.10 parent: `6f141b0aa0c2caf96b84bb4cd08baa6ab4457bfd`
- Onyx repository: `https://github.com/onyx-dot-app/onyx.git`
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx source clean: PASS
## Source Mapping
Static Onyx support signals captured:
- tenant/context evidence lines: 200
- identity/group/permission evidence lines: 250
- document/access evidence lines: 250
- tool/MCP evidence lines: 250
- credential evidence lines: 250
These counts establish architectural relevance only.
They do not prove that every synthetic fixture can be instantiated exactly as
written without deployment-specific adaptation.
## Fixture Manifest
`docs/security/fixtures/phase6-synthetic-security-fixture-manifest.md`
The fixture universe contains:
Tenant Alpha and Tenant Beta;
tenant administrators;
normal users;
group memberships;
service-identity concepts;
public, tenant, group and private documents;
prompt-injection and conflicting-instruction documents;
revocation and deletion lifecycle documents;
synthetic credential placeholders;
local mock service endpoints;
MCP servers;
read-oriented and state-changing tool concepts;
authorization oracles;
revocation and deletion oracles.
## Primary Isolation Invariant
A principal belonging only to Tenant Alpha must not obtain Tenant Beta
protected data, capabilities or credentials.
The inverse also applies.
## Primary Authorization Invariant
Security decisions are made by application control mechanisms.
The following are not authorization authorities:
- user prompt text;
- retrieved document content;
- model output;
- tool description text;
- MCP server output.
## Pre-Test Oracle Discipline
Expected ALLOW/DENY outcomes are recorded before execution.
Later observations therefore compare:
expected policy
against
actual behavior.
This reduces hindsight bias and prevents unexpected access from being
reclassified as intended behavior after the fact.
## Synthetic Prompt-Injection Fixture
`DOC-ALPHA-POISON-001` deliberately contains hostile-looking instructions.
Its presence is authorized because:
- the content is synthetic;
- no real external system is targeted;
- no real credential is present;
- execution is not performed in Action 6.11.
Later testing must verify that retrieval of this document cannot create
authorization or capability permission.
## Revocation Fixture
`DOC-ALPHA-REVOKE-001` establishes a known precondition:
Alice initially receives access through Alpha Engineering membership.
Later removal of that membership will permit measurement of the stale-access
window described in Action 6.9.
## Deletion Fixture
`DOC-ALPHA-DELETE-001` establishes content that may later be inserted and
deleted in a bounded local environment.
Later tests will check whether all derived representations converge on the
deleted state.
## Credential Safety
Credential placeholders use the form:
`SYNTHETIC_NOT_SECRET_...`
No valid provider-format credential was intentionally stored.
Common real-provider secret patterns were checked: PASS.
## Network Safety
All explicit mock endpoints are loopback addresses.
External provider endpoints in the fixture manifest: NONE.
## Interpretation Boundary
Action 6.11 designs fixtures only.
It does not prove:
- successful tenant creation;
- successful user creation;
- actual Onyx role mapping;
- actual group behavior;
- runtime document visibility;
- runtime MCP sharing;
- runtime tool authorization;
- tenant isolation;
- revocation correctness;
- deletion correctness;
- prompt-injection resistance.
Those require controlled later runtime tests.
## Safety Record
- Onyx started: NO
- Docker started: NO
- users created in Onyx: NO
- tenants created in Onyx: NO
- documents ingested: NO
- credentials used: NO
- MCP server contacted: NO
- tool invoked: NO
- model invoked: NO
- external API contacted: NO
- production/customer data used: NO
- Onyx source modified: NO
## Result
Action 6.11 synthetic tenant, identity and data fixture design: **PASS**.
