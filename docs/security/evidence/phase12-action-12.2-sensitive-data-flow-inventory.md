# Phase 12 — Action 12.2 Sensitive-Data Architecture and Data-Flow Inventory

## Objective

Map privacy-relevant data from collection through persistence, processing,
egress and deletion.

## Primary data flows

### Identity

Sources include authenticated user records, email addresses, personal names,
roles and IdP-derived organization profile fields.

Primary destinations include:

- user/account tables;
- memory/personalization context;
- authorization decisions;
- telemetry/audit surfaces;
- downstream prompts when personalization is enabled.

### Conversations

Chat sessions and messages may contain arbitrary user content.

Ordinary and content-persisting sessions use persistent chat/session storage.

Incognito content-free operation uses a separate ephemeral context path.

### Retrieval / RAG

Search results and document content may enter:

- retrieval structures;
- chat context;
- citations;
- saved search-document relationships;
- LLM prompts.

Their privacy boundary inherits source authorization.

### Memory and personalization

Persistent memory includes user-scoped memory text plus identity and
organization-profile information used for personalization.

### Files

Uploaded/generated files span:

- UserFile ownership metadata;
- FileRecord metadata;
- file-store objects;
- optional database FileContent;
- indexing/chunk representations;
- chat/project relationships.

### Credentials and OAuth

Credential JSON, client secrets and user OAuth tokens are high-sensitivity
authentication data with separate ownership and lifecycle paths.

### LLM/provider boundary

Prompts, retrieved context, personalization, tool information and model output
may cross the configured model/provider boundary.

### Telemetry / tracing

Telemetry and tracing form independent data sinks and therefore must be treated
as privacy boundaries rather than debugging-only implementation details.

### Usage metadata

Token/cost/usage records may persist independently from content.

## Data lifecycle model

The Phase-12 data-flow model is:

collection
→ authorization/ownership
→ persistence
→ transformation/retrieval
→ LLM/tool/provider processing
→ telemetry/audit
→ export/sharing
→ retention/deletion

Each transition is independently security-relevant.

## Evidence classification

**STATIC / SOURCE INVENTORY VERIFIED**

This action establishes architecture and does not claim every listed data sink
is unsafe.

Source trace:

`docs/security/evidence/phase12-action-12.2-sensitive-data-flow-source-trace.txt`

SHA-256:

`00bf4bf69e0eac07c2f9cc933966b1435da9297cf6022e3f00c16fa25e373a24`

## Completion

**ACTION 12.2: COMPLETE**

**RESULT=PHASE_12_ACTION_12_2_PASS**
