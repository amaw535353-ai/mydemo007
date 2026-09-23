# Phase 10 — Action 10.7 Embedding Security Boundaries

## Objective

Assess the security boundary where document/chunk content becomes embeddings,
including tenant propagation, external-provider trust and failure-path data
exposure.

## Embedding path

The reviewed path is:

document
→ chunk
→ embedding input text
→ local model server or configured cloud embedding provider
→ embedding vector
→ IndexChunk
→ authorization enrichment
→ vector index

## Tenant and request context

The indexing embedder propagates:

- tenant ID;
- request ID;

through embedding calls.

For the local model-server path these become:

- X-Onyx-Tenant-ID;
- X-Onyx-Request-ID.

**PASS**

## H10-02 — embedding input exposure in failure paths

### Baseline

Synthetic confidential embedding input was reproduced in a debug logging path
when a provider operation failed.

The empty-input validation path also embedded supplied input content directly in
its exception message.

Additional provider-result validation could include corresponding raw input
texts in an exception.

### Remediation

Failure handling now records metadata only:

- text count;
- total character count;
- failed input indexes where relevant.

Raw embedding text is no longer intentionally added to these application
failure logs or exception messages.

### Regression

- provider failure does not log sentinel input: **PASS**
- empty-input error does not echo sentinel input: **PASS**
- invalid provider result does not echo sentinel input: **PASS**
- raw API key not observed in tested log path: **PASS**

**H10-02: REMEDIATED**

## Cloud provider trust boundary

When a cloud embedding provider is deliberately configured, document/chunk
content is sent to that provider for embedding.

This is an architectural data-egress boundary, not by itself a vulnerability.

Production deployments therefore require provider approval, data-handling
policy, contractual/privacy review and egress controls appropriate to the data.

**R10-EMB-01 remains a deployment/governance consideration.**

No cloud provider was contacted during this action.

## Authorization ordering

Embedding occurs before the later authorization-enrichment/vector-index write
stage.

Therefore ACL metadata protects retrieval from the vector index, but does not
prevent content from reaching the configured embedding provider.

This distinction is recorded explicitly for later privacy/DLP work.

## Evidence

Results:

`docs/security/evidence/phase10-action-10.7-embedding-security-results.txt`

SHA-256:

`1e4b4f68c8f81a3e25a1b32d98b9f4c5b0996272434b70c490d40117ba1da23c`

Source trace:

`docs/security/evidence/phase10-action-10.7-embedding-source-trace.txt`

SHA-256:

`6163ad8b83913cafa819eb4dcf2056c63b592a65ffc9a26cecdc538c7f4e6ad6`

Regression:

`backend/tests/unit/onyx/natural_language_processing/test_embedding_security_boundaries.py`

## Safety

- synthetic content only: **YES**
- external provider calls: **0**
- database mutations: **0**
- HTTP requests: **0**
- external network requests: **0**
- real credentials/data: **0**

## Completion

**ACTION 10.7: COMPLETE**

Next:

**Action 10.8 — reranker authorization/security**
