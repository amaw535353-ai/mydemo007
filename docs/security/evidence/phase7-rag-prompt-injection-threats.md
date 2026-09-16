# Phase 7 Action 7.7 - RAG, Retrieval and Prompt-Injection Threats

## Classification

The Phase 6 document/RAG lifecycle was statically mapped.

The following are threat hypotheses, not confirmed vulnerabilities.

---

## T7-07-01 - Cross-tenant retrieval

### Scenario

A Tenant Alpha query retrieves document content, chunks or derived information
belonging exclusively to Tenant Beta.

### Security properties

- tenant isolation;
- confidentiality;
- authorization.

### Later verification

Use uniquely identifiable synthetic Alpha/Beta documents and verify both
retrieval results and AI-visible context.

---

## T7-07-02 - Authorization metadata lost during indexing

### Scenario

Document ACL or tenant metadata is correct at ingestion but is absent,
incorrect or ignored in a derived retrieval representation.

Representations may include:

- chunks;
- embeddings;
- index records;
- search metadata.

### Security properties

- authorization;
- metadata integrity.

### Later verification

Trace fixture identifiers from source document through every available derived
representation.

---

## T7-07-03 - Indirect prompt injection from retrieved content

### Scenario

A malicious synthetic document contains instructions intended for the model,
such as attempting to override system rules or trigger unsafe actions.

### Security properties

- instruction integrity;
- safe AI behavior;
- tool safety.

### Later verification

Use synthetic adversarial documents with deterministic harmless markers.

No real secrets or harmful external actions are permitted.

---

## T7-07-04 - Retrieved-content data exfiltration

### Scenario

Malicious retrieved content causes the model to expose context the requesting
user should not receive.

### Security properties

- confidentiality;
- authorization;
- context isolation.

### Later verification

Use synthetic secret markers and verify whether unauthorized markers appear in
model-visible context or output.

---

## T7-07-05 - Stale revoked document remains retrievable

### Scenario

Access is revoked or content is deleted in the authoritative store while a
search/vector/cache representation remains accessible.

### Security properties

- revocation;
- deletion;
- lifecycle consistency.

### Boundaries

TB-C and TB-F.

### Later verification

Measure retrieval before and after synthetic revoke/delete events.

---

## T7-07-06 - Citation/provenance confusion

### Scenario

Generated output associates a claim with the wrong source or represents
untrusted content as trusted provenance.

### Security properties

- provenance;
- integrity;
- explainability.

### Later verification

Use documents with deterministic source identifiers and compare retrieved
content, generated statements and citations.

---

# Result

Action 7.7:

**RAG THREAT MODEL COMPLETE - LIVE RETRIEVAL TESTING DEFERRED**
