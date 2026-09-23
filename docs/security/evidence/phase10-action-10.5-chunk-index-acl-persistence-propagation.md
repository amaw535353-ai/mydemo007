# Phase 10 — Action 10.5 Chunk / Index ACL Persistence and Propagation

## Objective

Verify that authorization metadata remains structurally represented from the
document-access model through chunk/index storage and the Vespa-to-OpenSearch
migration path.

## Tested security path

DocumentAccess
→ canonical ACL principals
→ DocMetadataAwareIndexChunk.access
→ OpenSearch public/ACL separation
→ DocumentChunk security fields
→ OpenSearch schema

Migration path:

Vespa ACL
→ public-marker extraction
→ OpenSearch public boolean
→ OpenSearch ACL-principal list

## Results

### ACL representation

Private document access preserved synthetic:

- user principals;
- internal groups;
- external users;
- external groups.

Public documents explicitly carried the public marker.

**PASS**

### Public/private separation

The OpenSearch conversion removes the public marker from the ACL principal
array while retaining actual principals.

A private empty ACL remains private rather than being widened to public.

**PASS**

### Chunk persistence

A synthetic private chunk serialized with:

- `public=false`;
- its expected ACL principal.

**PASS**

### Schema

The single-tenant OpenSearch schema contains:

- public visibility;
- ACL principals;

and omits the tenant field.

The multi-tenant schema contains:

- public visibility;
- ACL principals;
- tenant identity.

**PASS**

### Migration

The Vespa-to-OpenSearch conversion preserved:

- public state;
- user principals;
- group principals;
- private ACL state.

A missing source ACL became:

- public = false;
- ACL = empty.

It did not become public.

**PASS**

## Security interpretation

The tested indexing representations preserve authorization metadata and
distinguish three materially different states:

1. public;
2. ACL-restricted;
3. private with no authorized principal.

No tested conversion silently widened private access.

## Evidence

Property-test results:

`docs/security/evidence/phase10-action-10.5-acl-persistence-results.txt`

SHA-256:

`7f295918231f97e4e6cdb4b489352e01aeeca21549b5ce522b880ca1ae8b91df`

Source trace:

`docs/security/evidence/phase10-action-10.5-acl-index-source-trace.txt`

SHA-256:

`e79c91eeed75ad2bd70c3415d4a0c354e9501b9641a2adfbc31476f779558d43`

## Limitations

This action validates in-process representation and transformation.

It does not yet claim runtime proof of:

- actual indexed Alice/Bob isolation;
- cross-tenant search isolation;
- permission revocation after indexing;
- deletion propagation;
- stale-index behavior.

## Safety

- synthetic data/identities only: **YES**
- database mutations: **0**
- HTTP requests: **0**
- external network requests: **0**
- product source modifications: **0**
- production targets: **0**

## Finding status

**NO ACL PERSISTENCE OR PROPAGATION BYPASS CONFIRMED BY ACTION 10.5.**

## Completion

**ACTION 10.5: COMPLETE**

Next:

**Action 10.6 — vector/index tenant isolation**
