# Phase 10 — Action 10.3 Retrieval Authorization and ACL Propagation Trace

## Objective

Trace concrete source-code boundaries where authenticated identity,
authorization state, retrieval filters, search/index execution, reranking and
prompt-context construction intersect.

This action converts the broad Action 10.2 inventory into a bounded
negative-test design.

## Trace results

Retrieval/security-relevant symbols:

**962**

Identity + retrieval:

**542**

ACL/permission + retrieval:

**396**

Filter + retrieval:

**343**

Backend-search + retrieval:

**158**

Reranking + retrieval:

**9**

Context/citation + retrieval:

**233**

ACL + filter + retrieval:

**111**

## High-value enforcement boundaries

The trace identified several concrete Phase 10 review anchors.

### SearchTool.run

`backend/onyx/tools/tool_implementations/search/search_tool.py`

Observed call signals include:

- `build_access_filters_for_user`
- `filter_document_set_names_by_user_access`
- search/retrieval operations
- context/document conversion

This is a primary application-level authorization boundary for Action 10.4.

### DocumentQuery._get_search_filters

`backend/onyx/document_index/opensearch/search.py`

Observed filter construction includes:

- `_get_acl_visibility_filter`
- document-set filters
- attached-document filters
- user-project filters
- other search constraints

This is a primary backend-query authorization boundary.

### search_pipeline

`backend/onyx/context/search/pipeline.py`

Observed calls include:

- `_build_index_filters`
- `search_chunks`

Action 10.4 must determine whether unsafe or incomplete filter state can reach
`search_chunks`.

### Search API

`backend/onyx/server/features/search/api.py`

Observed signals include:

- `require_permission`
- user-group retrieval
- search-tool construction and execution

This provides an externally reachable application entry-point boundary for
bounded authorization tests.

## Interpretation

The trace demonstrates that authorization-related logic exists in the
retrieval path.

It does **not** yet establish that every path is safe.

Action 10.4 must verify:

1. unauthorized document/chunk retrieval is denied;
2. cross-user retrieval fails closed;
3. tenant boundaries remain enforced where applicable;
4. missing/empty ACL state cannot become unrestricted retrieval;
5. direct backend retrieval cannot silently bypass ACL enforcement;
6. unauthorized candidates cannot enter reranking;
7. unauthorized results cannot enter citation/context construction.

## Evidence

Trace:

`docs/security/evidence/phase10-action-10.3-retrieval-auth-trace.tsv`

Trace SHA-256:

`6c1896873b59c87d26ccfabdf57441bf4288795abc7fc112e08a08a29bcb4fd9`

Line-numbered source excerpts were generated for the highest-scoring symbols.

Excerpt SHA-256:

`a944c469723f62ef827f49e98f0944195dd4e516d1aa52b96482ae3b0beb7d3c`

## Safety

- database mutations: **0**
- HTTP requests: **0**
- external network requests: **0**
- production targets: **0**
- real credentials: **0**
- real customer data: **0**
- product source modifications: **0**

## Finding status

**NO NEW VULNERABILITY CLASSIFIED BY ACTION 10.3.**

The identified boundaries become the negative-test targets for Action 10.4.

## Completion

**ACTION 10.3: COMPLETE**

Next:

**Action 10.4 — bounded retrieval authorization negative tests**
