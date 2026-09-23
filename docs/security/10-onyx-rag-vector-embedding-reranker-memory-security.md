# Phase 10 — Onyx RAG / Vector / Embedding / Reranker / Memory Security

## Status

**Phase 10: IN PROGRESS**

## Objective

Assess authorization and security boundaries across document ingestion,
chunking, embedding, indexing, retrieval, reranking, context construction,
citations and application/conversation memory.

Phase 10 inherits the completed Phase 9 identity, authorization and tenant
isolation controls, but independently verifies whether those controls survive
the RAG and memory data paths.

## Core security invariants

- unauthorized documents must not enter a user's retrieval context;
- document authorization must survive chunking and indexing;
- cross-user and cross-tenant vector retrieval must fail closed;
- revocation/deletion must propagate to retrievable representations;
- reranking must never reintroduce unauthorized candidates;
- citations must not disclose unauthorized source information;
- retrieval caches must not bypass current authorization state;
- memory must not cross user/session/tenant boundaries;
- retrieved untrusted content must remain data rather than authority.

## Safety boundary

Testing remains restricted to the authorized local laboratory, synthetic
identities/data, bounded execution and approved local services.

No public Onyx target, real credential, real customer data or unapproved
external API is in scope.

## Action 10.2 — RAG data-flow and authorization inventory

Action 10.2 completed the initial bounded static inventory of ingestion,
chunking, embeddings, vector/index storage, retrieval, reranking, prompt
context, citations, memory and authorization-related source surfaces.

The inventory is a discovery map and does not classify keyword presence or
absence as a security vulnerability.

The next step traces concrete retrieval authorization and ACL propagation from
authenticated identity through filtering, candidate retrieval, reranking and
prompt-context construction.

**Action 10.2 status: COMPLETE.**
