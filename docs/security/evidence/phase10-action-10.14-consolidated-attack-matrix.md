# Phase 10 — Action 10.14 Consolidated RAG Security Attack Matrix

## Scope

This matrix consolidates Actions 10.1 through 10.13.

It distinguishes deterministic source/unit/property evidence from stronger
production-runtime claims.

| ID | Surface | Synthetic attack/property | Expected secure behavior | Observed result | Finding/control | Residual risk | Status |
|---|---|---|---|---|---|---|---|
| P10-01 | Retrieval authorization | Unauthorized identity requests protected document | Retrieval ACL denies unauthorized content | Negative authorization properties passed | Action 10.4 | Full production connector runtime not claimed | PASS |
| P10-02 | Chunk/index ACL propagation | ACL lost during chunk/index transformation | Authorization metadata persists through index representation | ACL persistence/transformation verified | Action 10.5 | Distributed runtime propagation remains later verification | PASS |
| P10-03 | Vector tenant isolation | Missing tenant filter or same document ID across tenants | Tenant isolation fails closed and identities remain distinct | Missing-tenant path remediated and tenant identity verified | H10-01 | Live multi-node tenant test remains limited | REMEDIATED |
| P10-04 | Embedding boundary | Embedding failure logs raw sensitive input | Failure telemetry excludes raw input | Logging boundary remediated | H10-02 | Configured provider egress remains an explicit trust boundary | REMEDIATED |
| P10-05 | Reranker | Unauthorized candidate enters reranker | Only authorized candidates can reach reranking | No active reachable reranker; future guardrail recorded | R10-RERANK-01 | Future reranker reintroduction | PASS/GUARDRAIL |
| P10-06 | Context expansion | Authorized center chunk expands into content requiring post-query censoring | Expanded content is recensored before LLM context | Synthetic bypass reproduced and remediated | H10-03 | External provider semantics vary | REMEDIATED |
| P10-07 | Retrieved prompt injection | Retrieved document says to override instructions/call tools | Retrieved text remains untrusted data | Explicit selection/expansion/final-context boundaries added | H10-04 | Model behavior cannot be guaranteed by prompt text alone | HARDENED |
| P10-08 | Citation/provenance | Document forges structural citation IDs/security fields | Provenance derives from trusted retrieved objects | Poisoned structural text remained data; forged unmatched citation rejected | Action 10.11 | Semantic truthfulness/ranking remains model/content risk | PASS |
| P10-09 | RAG poisoning | Conflicting documents attempt to collapse provenance | Distinct sources remain attributable | Distinct document IDs/citations preserved | Action 10.11 | Malicious source credibility still requires policy/product controls | PASS |
| P10-10 | Memory ownership | Memory text attempts to change owner/user/tenant | Persistence owner derives from trusted user context | User-ID ownership path verified; no owner selector exposed | Action 10.12 | Live Alpha/Beta DB runtime deferred | PASS |
| P10-11 | Memory prompt injection | Stored memory instructs secondary LLM to override task | Memory/chat fields treated as data | Explicit memory trust boundary added | H10-05 | Real-model resistance deferred | REMEDIATED |
| P10-12 | Revocation | Public document becomes private but indexed public state remains stale | ACL and public state update together | Stale-public property reproduced and remediated | H10-06 | Distributed eventual-consistency latency not measured | REMEDIATED |
| P10-13 | Delete consistency | Deleted document remains in secondary/other tenant | Delete fans to intended indices and stays tenant scoped | Tenant-aware delete and primary/secondary fanout verified | Action 10.13 | Production-scale delete timing not measured | PASS |
| P10-14 | Reindex race | Stale backfill overwrites/reinstalls old authorization | Missing/backfill state defers sync and preserves newer DB watermark | Typed missing signal and synced_as_of watermark verified | Action 10.13 | Live race reproduction deferred | PASS |

## Confirmed Phase 10 findings/remediations

### H10-01
Vespa multi-tenant missing-tenant fail-open.

**REMEDIATED**

### H10-02
Embedding failure path could expose raw embedding inputs in logs/errors.

**REMEDIATED**

### H10-03
Context expansion occurred after post-query censoring without re-censoring the
new adjacent chunks.

**REMEDIATED**

### H10-04
Retrieved-content prompts lacked a sufficiently explicit instruction/data
boundary.

**HARDENED**

### H10-05
Memory-update secondary prompt lacked an explicit untrusted memory/chat-data
boundary.

**REMEDIATED**

### H10-06
OpenSearch permission metadata updates changed the ACL but not the independent
public field, allowing stale public state across public→private revocation.

**REMEDIATED**

## Representative regression gate

The bounded offline negative-security suite reran representative tests covering:

- embedding security;
- context reauthorization;
- retrieved-content prompt boundaries;
- RAG poisoning/provenance;
- memory security;
- revocation/index consistency.

All selected tests passed.

Results:

`docs/security/evidence/phase10-action-10.14-negative-test-results.txt`

SHA-256:

`8f7287b406e42b0e5ca2c2351dd531a1422b6832c22440657385ece5d88a0f92`

## Evidence limitations

This action is a consolidation/regression gate, not a claim of complete
production-runtime coverage.

Still reserved for later Phase 10 actions:

- bounded synthetic runtime integration;
- consolidated finding/root-cause/remediation review;
- final framework/control mapping;
- residual-risk/final completion gate.

## Safety

- synthetic/offline tests: **YES**
- HTTP requests: **0**
- external application network requests: **0**
- production targets: **0**
- real data/credentials: **0**

## Completion

**ACTION 10.14: COMPLETE**

**RESULT=PHASE_10_ACTION_10_14_PASS**
