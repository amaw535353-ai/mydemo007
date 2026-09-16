# Phase 8 Action 8.14 - Maximum-Evidence and Runtime-Gap Gate

## Baseline

Pinned Onyx revision:

`160f9b143605ca45a85bd387b5bd173840bab15d`

## Static security evidence completed

Phase 8 has produced:

- 718 composed/static route candidates;
- 591 security-relevant dependency usages;
- 604 ownership/tenant control-path candidates;
- 150 high-value endpoint candidates;
- 200 object-reference/BOLA candidates;
- 200 privileged-operation candidates;
- 80 broad HTTP authorization fixtures;
- 24 prioritized P1 executable authorization fixtures;
- 16 explicit authentication/authorization/business-logic test cases.

## Corrected verification note

The previous Batch 3 terminal verification displayed:

`P1 executable fixtures: 1`

That value was caused by the verification command extracting the digit
`1` from the label `P1`.

The actual generated artifact records:

**24 P1 fixtures**

This Action 8.14 gate uses capture-group parsing and verifies the value as 24.

## Proven observations

Phase 8 can currently claim:

- the pinned Onyx source was preserved unchanged;
- web/API route declarations were statically inventoried;
- high-value security surfaces were prioritized;
- object-reference surfaces were identified;
- privileged-operation surfaces were identified;
- visible authentication/authorization dependencies were traced;
- ownership and tenant-related control paths were mapped;
- router composition was analyzed statically;
- executable authorization-test fixtures were prepared.

## Not proven

Phase 8 has not yet proven runtime behavior for:

- authentication enforcement;
- BOLA/IDOR resistance;
- conversation ownership;
- document ownership;
- cross-tenant isolation;
- vertical privilege enforcement;
- workflow sequencing;
- request/state manipulation resistance;
- authorization revocation;
- request/resource limits.

## Live execution count

Actual live Onyx security tests executed:

**0**

## Blocking environment evidence

The approved Debian host currently lacks a usable local Onyx runtime path.

Observed constraints include:

- Docker unavailable;
- Docker Compose unavailable;
- Node unavailable;
- Windows npm PATH entry unusable without Node;
- pnpm unavailable;
- uv unavailable;
- poetry unavailable;
- full Onyx runtime not positively identified.

Therefore HTTP authorization testing cannot honestly be represented as
executed.

## Current Phase 8 assurance status

Static reconnaissance:

**COMPLETE**

Static authorization/control analysis:

**COMPLETE**

Executable test design:

**COMPLETE**

Live authentication/authorization verification:

**BLOCKED / NOT EXECUTED**

Runtime vulnerability findings:

**0 CONFIRMED**

## Engineering decision

Phase 8 has reached the maximum defensible evidence available on the current
host without installing or establishing a suitable approved runtime.

The next engineering requirement is not additional speculative static
analysis.

The next requirement is:

**ESTABLISH AN APPROVED EXECUTABLE ONYX LAB AND RUN THE P1 TEST PACK**

## Result

**MAXIMUM CURRENT-HOST PHASE 8 EVIDENCE COMPLETE**

**LIVE SECURITY VERIFICATION REMAINS REQUIRED**
