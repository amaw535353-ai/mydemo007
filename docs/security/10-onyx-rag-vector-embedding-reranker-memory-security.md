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

## Action 10.3 — Retrieval authorization / ACL propagation trace

Action 10.3 produced a symbol-level retrieval authorization trace.

Primary enforcement boundaries include:

- `SearchTool.run`;
- `DocumentQuery._get_search_filters`;
- `search_pipeline`;
- the search API entry point.

The trace shows explicit ACL/filter-building behavior but does not by itself
prove all retrieval paths fail closed.

Action 10.4 therefore moves from static analysis to bounded authorization
negative tests.

**Action 10.3 status: COMPLETE.**

## Action 10.4 — Retrieval authorization negative tests

Action 10.4 directly tested the authorization/filter contracts identified by
the Action 10.3 trace.

Verified properties include:

- missing normal-user ACL derivation state fails closed;
- empty ACL state becomes public-only retrieval rather than unrestricted
  retrieval;
- non-empty user ACLs produce public-or-authorized visibility;
- unauthorized document-set selection is rejected;
- tenant identity propagates into backend filtering in multi-tenant mode;
- normal search-pipeline execution forwards ACL filters into backend queries;
- the public search API does not expose `bypass_acl` and explicitly constructs
  search with `bypass_acl=False`.

The privileged `ACL=None` / `bypass_acl=True` behavior remains an intentional
security-sensitive internal contract for continued call-site review.

No retrieval authorization bypass was confirmed by these direct tests.

**Action 10.4 status: COMPLETE.**

## Action 10.5 — Chunk/index ACL persistence and propagation

Action 10.5 verified authorization metadata through document access,
index-aware chunks, OpenSearch storage models/schema and the
Vespa-to-OpenSearch migration path.

Private/public state and ACL principals remained distinct throughout the tested
transformations.

No ACL persistence or propagation bypass was confirmed.

Runtime cross-tenant and revocation behavior remain separate Phase 10 tests.

**Action 10.5 status: COMPLETE.**

## Action 10.6 — Vector/index tenant isolation

Action 10.6 verified tenant isolation across the application, OpenSearch and
Vespa retrieval boundaries.

OpenSearch maintains tenant-specific chunk identity and tenant-specific search
constraints.

The normal search path propagates current tenant identity.

A lower-level Vespa defense-in-depth weakness was reproduced: multi-tenant
filter construction tolerated missing tenant identity and omitted the tenant
constraint.

No public cross-tenant retrieval bypass was demonstrated.

The lower-level contract was changed to fail closed and protected with a
regression test.

**H10-01: REMEDIATED.**

**Action 10.6 status: COMPLETE.**

## Action 10.7 — Embedding security boundaries

Action 10.7 assessed the content-to-embedding trust boundary.

Tenant and request identity propagate into local model-server embedding
requests.

A failure-path information-exposure issue was reproduced: raw embedding input
could be emitted in debug logs or exception messages.

The failure paths were changed to retain operational metadata while avoiding
intentional raw embedding-content disclosure.

**H10-02: REMEDIATED.**

Configured cloud embedding providers remain an explicit data-egress trust
boundary. ACL enrichment occurs after embedding, so retrieval authorization
does not itself prevent content from reaching the configured embedding
provider.

**Action 10.7 status: COMPLETE.**

## Action 10.8 — Reranker authorization/security

Action 10.8 established that the retained reranking implementation is not
reachable from the tested active Onyx search path.

Current search applies authorization-aware retrieval and post-query censoring,
then uses reciprocal-rank fusion and later section selection rather than the
historical reranker.

Historical reranking settings have been removed, and the legacy local
cross-encoder endpoint is non-executable commented source.

The retained cloud-capable RerankingModel remains a dormant/configuration
data-egress trust boundary if future code calls it.

No public reranking authorization bypass was confirmed.

**R10-RERANK-01:** any future reranker reintroduction must consume only
authorized/tenant-scoped candidates and retain regression coverage.

**Action 10.8 status: COMPLETE.**

## Action 10.9 — Context assembly and citation authorization

Action 10.9 reviewed the authorization boundary after retrieval and before
retrieved content becomes LLM context and citations.

A post-expansion authorization gap was reproduced. Initial search results were
permission-censored, but additional adjacent chunks fetched during context
expansion did not cross that censoring boundary again.

A synthetic property test demonstrated that such adjacent content could enter
the expanded context.

The search tool now re-applies post-query permission censoring to expanded
chunks before merging, LLM context generation or citation construction.

Sections whose center chunk no longer survives the permission check are dropped
fail-closed.

**H10-03: REMEDIATED.**

No public end-to-end exploit is claimed by this action.

**Action 10.9 status: COMPLETE.**
