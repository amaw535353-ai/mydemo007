# Phase 10 — Action 10.2 RAG Data Flow and Authorization Inventory

## Objective

Identify the source-code surfaces participating in the Onyx RAG, retrieval,
reranking, context and memory pipeline, and identify candidate locations where
authorization-related state intersects those surfaces.

This action is a discovery inventory, not a vulnerability verdict.

## Data-flow model

The initial security data flow is:

source / connector
→ ingestion
→ parsing
→ document representation
→ chunking
→ authorization metadata
→ embedding
→ vector/search index
→ retrieval query
→ authorization/filter construction
→ candidate retrieval
→ reranking
→ context construction
→ LLM prompt
→ citations/source rendering
→ conversation/application memory

Deletion, permission changes and connector revocation must propagate through
all persisted or cached representations.

## Static discovery

Total grouped RAG/authorization candidate rows:

**219**

Files containing both RAG and authorization signals:

**1183**

Database/model signals:

**95**

Deletion/revocation/reindex source signals:

**1608**

Zero matches in an individual discovery category are treated as an inventory
gap to investigate rather than automatically classified as a vulnerability.

## Authorization invariants for Action 10.3

The next trace must establish:

1. where authenticated user/tenant identity enters retrieval;
2. where document permissions become search/index filters;
3. whether filtering occurs before candidate retrieval;
4. whether direct vector/index callers can bypass authorization;
5. whether chunks retain their parent document authorization relationship;
6. whether reranking can receive unauthorized candidates;
7. whether citations can reveal denied source metadata;
8. whether permission changes invalidate retrievable representations;
9. whether deletion/revocation propagates to indexed data;
10. whether retrieval caches can outlive authorization;
11. whether memory can cross user/session/tenant boundaries;
12. exactly which retrieved fields become LLM context.

## Evidence

Static grouped inventory:

`docs/security/evidence/phase10-action-10.2-static-inventory.tsv`

SHA-256:

`35eb5b1d2d553889a665604af57b038d515f6927bb46d8fd33507aed9cc84a9f`

Detailed discovery output SHA-256:

`c595a5531e48b429537ac18fafc6c743e6a723fcf2cc7ed9db5fe12136dbbfde`

## Safety

- database mutations: **0**
- HTTP requests: **0**
- external network requests: **0**
- real credentials: **0**
- real customer data: **0**
- production targets: **0**
- source-code modifications: **0**

Only project documentation/evidence artifacts were created.

## Interpretation

Keyword and co-location matches identify code-reading priorities only.

They do not prove that authorization exists, is absent, or is correct.

Concrete call-path tracing is required before making a security finding.

## Completion

**ACTION 10.2: COMPLETE**

Next:

**Action 10.3 — retrieval authorization and ACL propagation trace**
