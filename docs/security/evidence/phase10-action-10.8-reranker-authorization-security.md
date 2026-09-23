# Phase 10 — Action 10.8 Reranker Authorization / Security

## Objective

Determine whether reranking can alter or bypass authorization boundaries in the
current Onyx retrieval architecture.

## Current architecture

The active retrieval path does not invoke the retained RerankingModel helper.

Current search behavior instead includes:

1. authorization and tenant filters;
2. retrieval;
3. post-query permission censoring where applicable;
4. weighted reciprocal-rank fusion for multi-query results;
5. later LLM-based section selection/expansion.

**ACTIVE_RERANKER_REACHABILITY: NO**

## Authorization property

A direct synthetic pipeline test supplied both:

- an authorized candidate;
- an unauthorized candidate.

The post-query censoring boundary returned only the authorized candidate.

**PASS**

## Historical reranking configuration

The database migration:

`78ebc66946a0_remove_reranking_from_search_settings.py`

removed the historical reranking configuration fields, including:

- rerank model;
- rerank provider;
- rerank API key;
- rerank API URL;
- rerank count.

**PASS**

## Legacy local reranker

The old model-server reranker module is retained only as commented legacy
source.

Its Python AST contains no executable statements.

**PASS**

## Dormant RerankingModel helper

A RerankingModel implementation remains in:

`onyx/natural_language_processing/search_nlp_models.py`

A fully mocked direct-provider test confirmed that, if deliberately called,
query and document text would be supplied to the configured cloud reranking
provider.

No provider was contacted.

This is therefore recorded as a dormant/configuration data-egress trust
boundary rather than an active retrieval vulnerability.

## Security conclusion

**NO PUBLIC RERANK AUTHORIZATION BYPASS CONFIRMED.**

Because the retained reranking helper is not reachable from the tested active
search pipeline, there is currently no active reranking stage capable of
reordering unauthorized candidates into the response.

## Future guardrail

**R10-RERANK-01**

If reranking is reintroduced, it must:

- consume only already-authorized candidates;
- preserve tenant restrictions;
- run after mandatory retrieval authorization;
- respect post-query field/object censoring where applicable;
- use only approved external providers;
- avoid logging raw query/document content;
- receive regression tests proving unauthorized candidates cannot enter or
  re-enter the final result set.

## Evidence

Results:

`docs/security/evidence/phase10-action-10.8-reranker-security-results.txt`

SHA-256:

`86971cb5a4ec8a2f44ca010350f1da2a7fbcf50cc13583082b7d1b53cf8975f2`

Source trace:

`docs/security/evidence/phase10-action-10.8-reranker-source-trace.txt`

SHA-256:

`d4e6338b8f69d67574d07a14d7f78386081e10c1c1def6c554c6478cb3b356ff`

Regression:

`backend/tests/unit/onyx/context/search/test_reranker_security_boundary.py`

## Safety

- synthetic candidates/content only: **YES**
- database mutations: **0**
- HTTP requests: **0**
- external network requests: **0**
- external reranker calls: **0**
- real credentials/data: **0**

## Completion

**ACTION 10.8: COMPLETE**

Next:

**Action 10.9 — context assembly and citation authorization**
