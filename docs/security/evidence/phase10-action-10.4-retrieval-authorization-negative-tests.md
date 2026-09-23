# Phase 10 — Action 10.4 Retrieval Authorization Negative Tests

## Objective

Validate the fail-closed authorization properties identified by Action 10.3
without requiring a production search backend, real documents, real users or
external services.

These tests exercise the application/filter/query contracts directly.

## Tested boundaries

### 1. ACL derivation failure

A normal retrieval path with:

- `bypass_acl=False`;
- no precomputed ACL;
- no database session from which to derive ACL state;

was rejected.

**Result: PASS — fail closed.**

### 2. Empty ACL semantics

An explicit empty ACL survives application filter construction.

At the OpenSearch query layer, an empty ACL produces a visibility clause that
allows public documents only.

It does not become unrestricted retrieval.

**Result: PASS.**

### 3. User ACL semantics

A non-empty synthetic user ACL generates:

- public-document visibility; OR
- matching ACL-principal visibility.

**Result: PASS.**

### 4. Unauthorized document-set selection

A synthetic user-selected document set that the access check reports as
inaccessible was rejected before search execution.

**Result: PASS.**

### 5. Tenant propagation

With multi-tenant mode enabled synthetically, the current tenant identifier was
propagated to `IndexFilters` and then represented as a backend tenant filter.

**Result: PASS.**

### 6. Search pipeline propagation

A normal `ChunkSearchRequest` with `bypass_acl=False` propagated its ACL
filters through `_build_index_filters` into the `ChunkIndexRequest` supplied
to `search_chunks`.

**Result: PASS.**

### 7. Public search API

The public `SearchRequest` model does not expose `bypass_acl`.

The public search endpoint requires `Permission.READ_SEARCH` and constructs
`SearchTool` with:

`bypass_acl=False`

**Result: PASS.**

## Privileged unrestricted contract

The lower-level backend intentionally treats:

`access_control_list=None`

as unrestricted by ACL.

Likewise, application filter construction with explicit:

`bypass_acl=True`

produces an unrestricted ACL value.

This is an intentional privileged contract rather than a vulnerability by
itself.

Security therefore depends on ensuring untrusted/public callers cannot set or
reach that privileged state.

The tested public search API does not expose this flag.

## Important limitation

Action 10.4 is a direct boundary/property test.

It does not yet claim end-to-end runtime proof using synthetic indexed
documents for:

- Alice-versus-Bob retrieval;
- cross-tenant retrieval;
- deletion/revocation propagation;
- stale index behavior.

Those require a bounded synthetic indexing/runtime fixture in later Phase 10
actions.

## Evidence

Results:

`docs/security/evidence/phase10-action-10.4-negative-test-results.txt`

SHA-256:

`b07629264968f0f6be630683aa30a9efc854677da401e6d0a1cb3478f7422ac3`

## Safety

- synthetic identities only: **YES**
- database mutations: **0**
- HTTP requests: **0**
- external network requests: **0**
- production targets: **0**
- real credentials: **0**
- real customer data: **0**
- product source modifications: **0**

## Finding status

**NO RETRIEVAL AUTHORIZATION BYPASS CONFIRMED BY ACTION 10.4.**

One security-sensitive privileged contract remains explicitly tracked:

**ACL=None / bypass_acl=True means unrestricted retrieval and therefore must
remain unreachable from untrusted callers.**

## Completion

**ACTION 10.4: COMPLETE**

Next:

**Action 10.5 — chunk/index ACL persistence and propagation**
