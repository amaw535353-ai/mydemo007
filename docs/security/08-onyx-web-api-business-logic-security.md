# Phase 8 - Onyx Web, API and Business-Logic Security

Phase 8 status: **IN PROGRESS**

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
