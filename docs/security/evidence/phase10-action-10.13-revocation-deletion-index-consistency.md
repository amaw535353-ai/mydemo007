# Phase 10 — Action 10.13 Revocation, Deletion and Index Consistency

## Objective

Verify authorization revocation and deletion consistency across the indexed
representation, including reindex/backfill race handling.

## H10-06 — stale OpenSearch public flag

### Baseline

OpenSearch represents document authorization using both:

- a dedicated `public` field;
- an access-control-list field.

The metadata permission-update path updated the ACL but did not update the
dedicated public field.

A deterministic synthetic property test changed a document from public to
private and confirmed:

- ACL update was generated;
- public-field update was absent.

This could leave an indexed document with stale `public=true` after permission
revocation.

**H10-06 BASELINE: CONFIRMED**

This is a property-level authorization/revocation defect.

No public deployment exploitation was attempted or claimed.

### Remediation

OpenSearch metadata permission updates now update both:

`ACCESS_CONTROL_LIST_FIELD_NAME`

and:

`PUBLIC_FIELD_NAME = update_request.access.is_public`

The change covers both public→private revocation and private→public transition.

**H10-06: REMEDIATED**

## Delete consistency

OpenSearch deletion constructs a tenant-aware deletion query.

The OpenSearch index-pair wrapper fans deletion to both primary and secondary
indices when the secondary exists.

**PASS**

## Tenant identity

The same synthetic document/chunk identity under tenant-alpha and tenant-beta
produced distinct multi-tenant OpenSearch chunk IDs.

**PASS**

## Reindex/backfill race

During an active primary backfill, a missing indexed document is surfaced as
`SecondaryIndexDocumentMissingError` instead of silently clearing sync state.

This preserves deferred synchronization rather than allowing a stale port copy
to become authoritative.

**PASS**

## Concurrent modification watermark

Document metadata synchronization snapshots `doc.last_modified` before index
I/O and supplies the snapshot through `synced_as_of` when marking the document
synced.

This preserves a later concurrent modification as stale/pending rather than
incorrectly declaring the newer state synchronized.

**PASS**

## Evidence level

Verified:

- deterministic synthetic OpenSearch metadata-update properties;
- tenant-specific chunk identity;
- tenant-scoped delete construction;
- primary/secondary delete fanout;
- missing-document deferred behavior;
- source-level synchronization watermark.

Not claimed:

- production-scale eventual consistency;
- live connector permission-revocation latency;
- live distributed Postgres/Redis/OpenSearch race reproduction;
- a public exploit.

Therefore:

**DESIGN/PROPERTY VERIFIED**

but:

**END-TO-END EVENTUAL REVOCATION RUNTIME: NOT CLAIMED**

## Evidence

Results:

`docs/security/evidence/phase10-action-10.13-revocation-consistency-results.txt`

SHA-256:

`6c632fef15dc70ce263ea0932d791404026c58ddd846be747e7ab10045c1eb1c`

Source trace:

`docs/security/evidence/phase10-action-10.13-revocation-consistency-source-trace.txt`

SHA-256:

`73f4ca43b87dbf040089bdf2339b5d45c79423e436149233ad81b4d8da606e34`

Regression:

`backend/tests/unit/onyx/document_index/opensearch/test_revocation_index_consistency.py`

## Safety

- synthetic documents/identities: **YES**
- HTTP requests: **0**
- external application network requests: **0**
- production targets: **0**
- real credentials/data: **0**

## Completion

**ACTION 10.13: COMPLETE**

**H10-06: REMEDIATED**

**RESULT=PHASE_10_ACTION_10_13_PASS**
