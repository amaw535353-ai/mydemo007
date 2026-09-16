# Phase 8 - Onyx Web, API and Business-Logic Security

Phase 8 status: **COMPLETE**

## Objective

Convert the Phase 7 web/API/business-logic threat hypotheses and security
requirements into reproducible security verification against the authorized
Onyx laboratory.

## Baseline

Pinned Onyx revision:

`160f9b143605ca45a85bd387b5bd173840bab15d`

Phase 7 handoff:

`fe5f15730086b3408dff8248e0f8770e9a5fddf8`

## Rules

- synthetic data only;
- local authorized lab only;
- no unsupported vulnerability claims;
- distinguish static observations from runtime results;
- preserve request/response evidence;
- use explicit expected ALLOW/DENY outcomes.

## Action 8.1 - Test charter

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase8-engagement-test-charter.md`


## Action 8.2 - Static API route reconnaissance

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase8-api-route-reconnaissance.md`

Important:

Detected route declarations and nearby security-related keywords are
reconnaissance evidence only.

They do not prove runtime exposure or enforcement.

## Action 8.3 - Authentication/authorization/business-logic test matrix

Status: **COMPLETE**

Defined tests:

**16**

Evidence:

`docs/security/evidence/phase8-authz-business-logic-test-matrix.md`

## Action 8.4 - Executable runtime readiness gate

Status: **COMPLETE**

Decision:

**LIVE ONYX TESTING CURRENTLY BLOCKED ON THIS HOST**

Reasons include the currently unavailable Docker/Compose runtime and incomplete
local application toolchain.

Evidence:

`docs/security/evidence/phase8-runtime-readiness-gate.md`

No active Onyx security request was performed during Actions 8.1 through 8.4.

## Next

Because a positively identified live Onyx target is not yet available, Phase 8
continues with evidence-driven static security work:

- select concrete high-value API endpoints;
- trace authentication dependencies;
- trace object-level authorization;
- trace ownership checks;
- identify client-controllable object identifiers;
- map expected ALLOW/DENY outcomes;
- prepare reproducible HTTP fixtures for later runtime execution.

Static control presence must not be represented as proof that the control works
at runtime.

---

## Action 8.5 - High-value endpoint shortlist

Status: **COMPLETE**

The pinned Onyx API inventory was prioritized for security-relevant web/API
testing.

Evidence:

`docs/security/evidence/phase8-high-value-endpoint-shortlist.md`

Runtime exposure remains unverified.

## Action 8.6 - Authentication and authorization control trace

Status: **COMPLETE**

Directly visible route dependencies and security-related calls were extracted
from the pinned source.

Evidence:

`docs/security/evidence/phase8-authentication-authorization-control-trace.md`

Presence of a control-looking function does not prove enforcement.

Absence of a visible route-local control does not prove a vulnerability.

## Action 8.7 - Object-authorization test surface

Status: **COMPLETE**

Object-reference route candidates suitable for later BOLA/IDOR and ownership
verification were identified.

Evidence:

`docs/security/evidence/phase8-object-authorization-surface.md`

## Action 8.8 - Privileged-operation test surface

Status: **COMPLETE**

Administrative and privilege-sensitive route candidates were identified for
later vertical-authorization verification.

Evidence:

`docs/security/evidence/phase8-privileged-operation-surface.md`

## Action 8.9 - HTTP security test fixtures

Status: **COMPLETE**

Concrete source-backed request templates were prepared for later execution
against an approved local runtime.

Evidence:

`docs/security/fixtures/phase8-http-test-fixture-manifest.md`

No Phase 8 HTTP security fixture has yet been executed against Onyx.

## Current status

Actions completed:

**8.1 through 8.9**

Static evidence is sufficient to continue endpoint/control tracing while the
live runtime limitation remains documented.

## Next

Resolve route composition and control chains more deeply:

- router/include-router prefix composition;
- concrete full-path candidates;
- authentication dependency definitions;
- ownership-check implementation paths;
- tenant-context propagation;
- negative authorization expectations.

Then prepare the smallest executable test pack for the first approved local
runtime.

---

## Action 8.10 - Router composition trace

Status: **COMPLETE**

Best-effort static route composition was performed across visible
`include_router` and `APIRouter` relationships.

Evidence:

`docs/security/evidence/phase8-router-composition-trace.md`

Unresolved route prefixes remain explicitly marked rather than guessed.

## Action 8.11 - Authentication/authorization dependency definitions

Status: **COMPLETE**

Security-relevant route dependencies were traced toward candidate source
definitions.

Evidence:

`docs/security/evidence/phase8-auth-dependency-definition-trace.md`

Static same-name resolution does not prove runtime Python binding.

## Action 8.12 - Ownership and tenant-control paths

Status: **COMPLETE**

Route-local ownership/access/tenant calls and candidate helper definitions were
mapped for later authorization verification.

Evidence:

`docs/security/evidence/phase8-ownership-tenant-control-trace.md`

No control is represented as effective until runtime evidence exists.

## Action 8.13 - P1 executable authorization test pack

Status: **COMPLETE**

A reduced high-priority authorization test set was prepared.

Evidence:

`docs/security/fixtures/phase8-p1-executable-test-pack.md`

Status:

**PREPARED - NOT EXECUTED**

Live execution remains blocked until an approved local Onyx runtime is
positively identified.

## Current Phase 8 state

Actions complete:

**8.1 through 8.13**

Live Onyx security tests executed:

**0**

The project now contains:

- broad API reconnaissance;
- high-value endpoint selection;
- object-reference surfaces;
- privileged-operation surfaces;
- router composition evidence;
- authentication dependency traces;
- ownership/tenant-control traces;
- broad HTTP fixtures;
- reduced P1 executable test fixtures.

## Next

Action 8.14 should determine the maximum remaining evidence that can be
established without a live runtime and define the formal Phase 8 runtime-gap
handoff.

Runtime testing must not be simulated or represented as completed.

---

## Action 8.14 - Maximum-evidence / runtime-gap gate

Status: **COMPLETE**

The maximum defensible web/API/business-logic security evidence available on
the current host has been established.

Important corrected count:

- P1 executable fixtures: **24**

The previous terminal display of `1` was a verification-parser error caused by
matching the digit in the label `P1`; it was not the artifact's real count.

### Current evidence state

Static reconnaissance:

**COMPLETE**

Static control-path analysis:

**COMPLETE**

Executable test preparation:

**COMPLETE**

Live Onyx web/API security verification:

**BLOCKED / NOT EXECUTED**

Confirmed runtime vulnerabilities:

**0**

Evidence:

`docs/security/evidence/phase8-maximum-evidence-runtime-gap.md`

## Required next step

Establish an approved runnable Onyx laboratory and execute the prepared P1
authorization pack.

Phase 8 must not be represented as having verified runtime authentication,
authorization, tenant isolation or business-logic controls until those tests
are actually executed.

---

## Action 8.30 - Formal Phase 8 closure

Status: **COMPLETE**

The earlier runtime-blocked state documented in Actions 8.4 and 8.14 remains
preserved as historical evidence. A controlled authorized Onyx runtime was
subsequently established and runtime security verification was completed.

### Confirmed security finding

TC8-007 identified request-controlled tenant/schema selection through the
asynchronous database-session dependency.

Confirmed effects before remediation:

- caller influence over schema selection;
- HTTP 500 for a valid but nonexistent schema;
- internal SQL/database-detail disclosure.

Not demonstrated:

- unauthorized cross-user data access;
- authorization bypass;
- unauthorized state change.

### Remediation outcome

The request-facing asynchronous database dependency now exposes no
request-bindable tenant identifier.

The explicit tenant-aware interface is isolated for trusted internal use.

### Runtime regression outcome

**TC8-007 FIX VERIFIED**

Post-remediation verification demonstrated:

- owner access remains functional;
- foreign-object access remains denied;
- tenant query manipulation no longer changes database schema selection;
- the former HTTP 500 is not reproduced;
- SQL/schema disclosure is absent;
- API health remains functional.

Closure evidence:

`docs/security/evidence/phase8-final-closure.md`

### Final Phase 8 decision

**COMPLETE**

Next:

**Phase 9 — Onyx Identity, Authorization and Tenant Isolation**
