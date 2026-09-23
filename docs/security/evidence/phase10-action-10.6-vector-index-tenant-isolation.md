# Phase 10 — Action 10.6 Vector / Index Tenant Isolation

## Objective

Verify tenant isolation at vector/search-index boundaries and determine whether
missing tenant state fails closed in multi-tenant mode.

## OpenSearch

Verified:

- multi-tenant TenantState requires a tenant ID;
- identical document/chunk identities differ across tenants;
- multi-tenant schema contains the tenant field;
- Tenant Alpha queries contain only Tenant Alpha;
- Tenant Beta queries contain only Tenant Beta;
- single-tenant queries retain existing behavior.

**PASS**

## Application propagation

The normal search path populated current tenant identity into IndexFilters.

**PASS**

## H10-01 — Vespa missing-tenant fail-open

### Baseline

Before remediation, direct lower-level Vespa filter construction in
multi-tenant mode accepted:

`tenant_id=None`

and produced a query without a tenant restriction.

This was a lower-level fail-open security contract.

No public cross-tenant retrieval bypass was demonstrated because the tested
normal application path already injects tenant identity.

### Remediation

The Vespa filter builder now requires tenant identity in multi-tenant mode.

Missing tenant identity raises `ValueError`.

Single-tenant behavior remains unchanged.

### Regression

- focused regression suite: **PASS**
- missing tenant fails closed: **PASS**
- exact Tenant Alpha filter: **PASS**
- single-tenant compatibility: **PASS**

**H10-01: REMEDIATED**

## Classification

**NO PUBLIC CROSS-TENANT RETRIEVAL BYPASS CONFIRMED.**

The lower-level defense-in-depth weakness was reproduced, remediated and
regression-tested.

## Evidence

Results:

`docs/security/evidence/phase10-action-10.6-tenant-isolation-results.txt`

SHA-256:

`4496b085c1311169e19df7b2d01c07ed73a36a90eb06e5a38de6de777d9dfdb0`

Source trace:

`docs/security/evidence/phase10-action-10.6-tenant-isolation-source-trace.txt`

SHA-256:

`be95beaa5f24fa04fb4db81925dbb52d6877d85a0870406ae58bf9c9bd29cd9f`

Regression:

`backend/tests/unit/onyx/document_index/vespa/shared_utils/test_vespa_tenant_isolation.py`

## Safety

- synthetic tenants only: **YES**
- database mutations: **0**
- HTTP requests: **0**
- external network requests: **0**
- real data/credentials: **0**
- production targets: **0**

## Completion

**ACTION 10.6: COMPLETE**

Next:

**Action 10.7 — embedding security boundaries**
