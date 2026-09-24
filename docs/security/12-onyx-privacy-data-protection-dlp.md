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

## Action 12.3 — Data classification, ownership and tenant boundaries

Action 12.3 classified identity, content, source, credential and operational
data and traced the primary ownership boundaries.

Chat, memory and credential paths contain explicit user-scoping controls.

Low-level user-file ID helpers are not treated as authorization APIs; their
externally reachable consumers remain candidates for direct negative testing.

No cross-user privacy bypass was confirmed by this action.

**Action 12.3 status: COMPLETE.**

## Action 12.4 — Collection, minimization and purpose boundaries

Action 12.4 verified multiple content-minimization properties in incognito
operation, including bounded ephemeral context, provider retention-suppression
requests, filename/title minimization and image removal.

Provider compliance with requested retention settings is not independently
claimed.

No collection-overreach finding was confirmed by this action.

**Action 12.4 status: COMPLETE.**

## Action 12.5 — Sensitive storage, secrets and PII inventory

Action 12.5 inventoried user/account data, chat content, persistent memory,
file/blob representations, connector credentials, OAuth data and telemetry
identifiers.

A deliberate retention exception was recorded for later testing: historical
user-usage rows survive user deletion with their user foreign key nulled.

This is not yet classified as a privacy defect; Action 12.9 will verify the
actual retained fields and deletion semantics.

**Action 12.5 status: COMPLETE.**
