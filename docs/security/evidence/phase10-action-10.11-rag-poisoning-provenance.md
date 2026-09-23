# Phase 10 — Action 10.11 RAG Poisoning and Provenance

## Objective

Assess whether malicious or conflicting retrieved content can overwrite trusted
provenance structure or forge citation identity.

## Tested properties

Synthetic poisoned document content contained:

- forged document numbers;
- forged security-notice content;
- forged citation references;
- control-shaped JSON;
- attacker-controlled metadata.

The retrieved text remained document data.

## Provenance identity

Citation numbers are assigned by application logic from the retrieved section's
document identity.

The synthetic document could not choose its structural citation number.

**PASS**

## SearchDoc identity

SearchDoc identity was derived from the retrieved chunk's document_id.

Poisoned document text did not alter that value.

**PASS**

## Citation processor

A synthetic citation mapping referenced one legitimate SearchDoc and one forged
document ID with no matching SearchDoc.

The citation processor retained only the citation that resolved to an actual
SearchDoc.

**PASS**

## Conflicting documents

Two documents using the same title but distinct document IDs remained separate
results with separate citation mappings.

**PASS**

## Retrieved-content instruction boundary

The Action 10.10 top-level security notice remains present and is structurally
separate from retrieved content.

A JSON-shaped document could not replace it.

## Finding classification

**NO CONFIRMED STRUCTURAL RAG-PROVENANCE BYPASS**

This action does not claim that retrieval ranking can always distinguish true
information from intentionally false information.

Semantic truthfulness and model behavior remain separate red-team concerns.

## Evidence level

Verified:

- direct deterministic unit/property behavior;
- source-level provenance flow.

Not claimed:

- production connector poisoning;
- real external content poisoning;
- model truthfulness under conflicting evidence.

## Evidence

Results:

`docs/security/evidence/phase10-action-10.11-rag-poisoning-provenance-results.txt`

SHA-256:

`43cb6b12986fc210e18160c7a43976712c8d7042b4248b6fee05d14af21b35d5`

Source trace:

`docs/security/evidence/phase10-action-10.11-rag-poisoning-provenance-source-trace.txt`

SHA-256:

`99becd2b0d720092347ae347c8940da81fb3a6b35e844123a52a1c409c5a1723`

Regression:

`backend/tests/unit/onyx/chat/test_rag_poisoning_provenance.py`

## Safety

- synthetic content only: **YES**
- database mutations: **0**
- HTTP requests: **0**
- external application network requests: **0**
- real credentials/data: **0**

## Completion

**ACTION 10.11: COMPLETE**

Result:

**RESULT=PHASE_10_ACTION_10_11_PASS**
