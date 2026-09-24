# Phase 12 — Onyx Privacy / Data Protection / DLP

## Status

**Phase 12: IN PROGRESS**

## Parent

Phase 11 final SHA:

`7dc4350614b432edfc0d871e202704b3cf2d4c70`

## Objective

Assess privacy and sensitive-data handling across identity, chat, files,
retrieval, memory, connectors, tools, providers, telemetry, retention,
deletion, export and DLP boundaries.

## Core principles

- synthetic data only;
- least necessary collection;
- explicit ownership;
- explicit egress;
- sensitive-data minimization;
- bounded retention;
- reliable deletion;
- redaction before unsafe boundaries;
- tenant/user isolation;
- evidence-based privacy claims.

## Action 12.1 — Initialization and privacy charter

Phase 12 was created directly from the completed Phase 11 SHA.

The privacy scope, synthetic-data rules, evidence model, data classes, stop
conditions and completion criteria were fixed before technical privacy testing.

**Action 12.1 status: COMPLETE.**

## Action 12.2 — Sensitive-data architecture and data-flow inventory

Action 12.2 mapped identity, conversation, retrieval, memory, files,
credentials, OAuth, provider, telemetry and usage-data flows.

Privacy review will treat telemetry, model providers and derived/indexed copies
as independent data boundaries rather than assuming the primary database is
the only privacy-relevant store.

**Action 12.2 status: COMPLETE.**
