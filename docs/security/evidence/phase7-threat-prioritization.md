# Phase 7 Action 7.13 - Threat Verification Prioritization

## Important interpretation

This document does **not** assign vulnerability severity.

No vulnerability has yet been demonstrated.

The priority below answers:

> Which threat hypotheses should receive executable verification earliest?

Priority reflects:

1. potential security impact;
2. proximity to major trust boundaries;
3. cross-tenant or privilege consequences;
4. capability for external side effects;
5. uncertainty caused by missing runtime evidence.

---

# P1 - Verify first

These hypotheses can directly affect tenant isolation, authorization,
confidentiality or privileged execution.

- T7-05-01 - missing authentication enforcement
- T7-05-02 - broken object-level authorization
- T7-05-03 - request/state manipulation
- T7-05-05 - cross-request state confusion

- T7-06-01 - tenant-context confusion
- T7-06-02 - horizontal privilege escalation
- T7-06-03 - vertical privilege escalation
- T7-06-04 - ACL/revocation propagation failure
- T7-06-05 - tenant-scoping omission

- T7-07-01 - cross-tenant retrieval
- T7-07-02 - authorization metadata lost during indexing
- T7-07-03 - indirect prompt injection
- T7-07-04 - retrieved-content data exfiltration
- T7-07-05 - stale revoked document remains retrievable

- T7-08-01 - unauthorized sensitive context sent to provider
- T7-08-03 - provider credential exposure
- T7-08-04 - untrusted model output treated as trusted control data

- T7-09-01 - model-to-tool authority escalation
- T7-09-02 - tool argument injection
- T7-09-03 - malicious MCP metadata/tool description
- T7-09-04 - credential disclosure to tool/MCP
- T7-09-05 - unsafe code execution/sandbox failure

- T7-10-01 - revoked authorization remains effective
- T7-10-02 - deleted document remains retrievable
- T7-10-04 - revoked credential remains effective
- T7-10-05 - asynchronous race restores stale security state

---

# P2 - Verify after P1

Important resilience, integrity and abuse hypotheses:

- T7-05-04 - workflow sequencing bypass
- T7-05-06 - Web/API resource exhaustion

- T7-06-06 - privileged configuration overreach

- T7-07-06 - citation/provenance confusion

- T7-08-02 - provider-routing/configuration confusion
- T7-08-05 - unbounded model consumption
- T7-08-06 - sensitive AI context in observability surfaces

- T7-09-06 - recursive/chained capability exhaustion

- T7-10-03 - deleted conversation remains accessible
- T7-10-06 - lifecycle event not auditable

- T7-11-01 - request flooding
- T7-11-02 - oversized input exhaustion
- T7-11-03 - expensive RAG amplification
- T7-11-04 - agent/tool recursion
- T7-11-05 - queue/retry amplification
- T7-11-06 - storage/log amplification

---

# Counts

- P1: 26
- P2: 16
- Total: 42

No P3 category is currently used because every recorded threat is considered
relevant enough for eventual verification.

---

# Result

Action 7.13:

**THREAT VERIFICATION PRIORITY ESTABLISHED**

This is a test-order decision, not a vulnerability severity rating.
