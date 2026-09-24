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

## Action 12.6 — Prompt, context and RAG privacy leakage

Action 12.6 verified user ACL, document-set authorization, tenant filtering and
post-query censoring boundaries before retrieved content reaches model context.

Prompt construction intentionally exposes personalization data such as identity,
preferences and memories to the model context when configured.

That is recorded as a privacy-sensitive provider-egress surface rather than an
unauthorized disclosure finding.

**Action 12.6 status: COMPLETE.**

## Action 12.7 — Logs, traces, telemetry and error disclosure

Action 12.7 verified incognito external-trace suppression, sensitive trace
masking and the telemetry disable gate.

External tracing, telemetry event payloads and persisted background error
messages remain explicit privacy-sensitive secondary-data boundaries.

No unauthorized observability disclosure was confirmed by this static action.

**Action 12.7 status: COMPLETE.**

## Action 12.8 — Connector, tool, MCP and provider egress

Action 12.8 mapped external model, custom-tool and MCP boundaries and verified
outbound URL validation, redirect suppression, MCP header filtering, SSRF-aware
transport construction and bounded MCP call timing.

All verification was offline; no real external provider or tool endpoint was
contacted.

**Action 12.8 status: COMPLETE.**

## Action 12.9 — Conversation, file and memory retention / deletion

Action 12.9 verified chat hard-delete paths, file-store deletion primitives and
user-cascade behavior for memory and chat sessions.

The Action 12.5 retention exception was narrowed: UserUsage intentionally
survives user deletion with its direct user foreign key nulled, while the
reviewed schema contains usage/accounting fields rather than prompt, message,
memory or file content.

This evidence does not claim deletion from production backups, external
provider stores or every derived representation.

**Action 12.9 status: COMPLETE.**
