# Phase 8 Action 8.1 - Web/API/Business-Logic Security Test Charter

## Objective

Perform evidence-driven security verification of the Onyx web, API and
business-logic surfaces identified during Phases 6 and 7.

Primary areas:

- authentication enforcement;
- object-level authorization;
- ownership;
- tenant-context handling;
- request/state manipulation;
- privilege enforcement;
- workflow sequencing;
- business-logic abuse;
- bounded API resource use.

## Baseline

Pinned Onyx revision:

`160f9b143605ca45a85bd387b5bd173840bab15d`

Phase 7 completion:

`fe5f15730086b3408dff8248e0f8770e9a5fddf8`

## Phase 7 requirements entering Phase 8

Highest-relevance requirements include:

- SR-001 - protected-route authentication;
- SR-002 - server-side object authorization;
- SR-003 - tenant-context binding;
- SR-004 - privilege enforcement;
- SR-005 - authorization revocation convergence;
- SR-022 - bounded request/resource consumption.

## Safety boundary

Testing is authorized only against the approved local laboratory.

Required:

- synthetic identities;
- synthetic documents;
- synthetic credentials;
- loopback/local targets only;
- no production/customer systems;
- no real credentials;
- no paid APIs;
- no uncontrolled external connections.

Bounded active-test limits:

- maximum 100 requests per test;
- maximum 10 concurrent requests;
- maximum 60 seconds;
- maximum 1 MB test file.

## Stop conditions

Stop immediately if:

- a request would leave the approved local lab;
- a real credential is observed;
- real customer/production data appears;
- scope becomes uncertain;
- resource bounds cannot be guaranteed;
- a test requires an unapproved paid/external service.

## Evidence states

Every test must be classified as:

- PLANNED;
- BLOCKED;
- EXECUTED;
- PASS;
- FAIL;
- INCONCLUSIVE.

A threat hypothesis becomes a security finding only after reproducible
authorized evidence exists.

## Evidence requirements

For executable tests record:

- timestamp;
- target;
- synthetic identity;
- request;
- expected result;
- actual result;
- response status;
- relevant response evidence;
- interpretation;
- reproducibility;
- cleanup state.

## Source integrity

The pinned Onyx source is read-only for reconnaissance.

No Phase 8 reconnaissance step may modify the pinned source tree.

# Result

Action 8.1 charter:

**ESTABLISHED**
