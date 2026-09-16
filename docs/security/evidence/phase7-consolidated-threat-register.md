# Phase 7 Action 7.12 - Consolidated Threat Register

## Classification

Every entry below is currently a **THREAT HYPOTHESIS**.

The register does not claim that any threat is an exploitable vulnerability.

Runtime findings require later executable verification.

## Register

| Threat ID | Domain | Threat | Source evidence |
|---|---|---|---|
| T7-05-01 | Web/API/Business Logic | Missing authentication enforcement | `docs/security/evidence/phase7-web-api-business-logic-threats.md` |
| T7-05-02 | Web/API/Business Logic | Broken object-level authorization | `docs/security/evidence/phase7-web-api-business-logic-threats.md` |
| T7-05-03 | Web/API/Business Logic | Request parameter or state manipulation | `docs/security/evidence/phase7-web-api-business-logic-threats.md` |
| T7-05-04 | Web/API/Business Logic | Workflow sequencing bypass | `docs/security/evidence/phase7-web-api-business-logic-threats.md` |
| T7-05-05 | Web/API/Business Logic | Cross-request state confusion | `docs/security/evidence/phase7-web-api-business-logic-threats.md` |
| T7-05-06 | Web/API/Business Logic | Web/API resource exhaustion | `docs/security/evidence/phase7-web-api-business-logic-threats.md` |
| T7-06-01 | Identity/Auth/Tenant | Tenant-context confusion | `docs/security/evidence/phase7-identity-authorization-tenant-threats.md` |
| T7-06-02 | Identity/Auth/Tenant | Horizontal privilege escalation | `docs/security/evidence/phase7-identity-authorization-tenant-threats.md` |
| T7-06-03 | Identity/Auth/Tenant | Vertical privilege escalation | `docs/security/evidence/phase7-identity-authorization-tenant-threats.md` |
| T7-06-04 | Identity/Auth/Tenant | Group or ACL propagation failure | `docs/security/evidence/phase7-identity-authorization-tenant-threats.md` |
| T7-06-05 | Identity/Auth/Tenant | Tenant-scoping omission in a data-access path | `docs/security/evidence/phase7-identity-authorization-tenant-threats.md` |
| T7-06-06 | Identity/Auth/Tenant | Privileged configuration overreach | `docs/security/evidence/phase7-identity-authorization-tenant-threats.md` |
| T7-07-01 | RAG/Retrieval/Prompt Injection | Cross-tenant retrieval | `docs/security/evidence/phase7-rag-prompt-injection-threats.md` |
| T7-07-02 | RAG/Retrieval/Prompt Injection | Authorization metadata lost during indexing | `docs/security/evidence/phase7-rag-prompt-injection-threats.md` |
| T7-07-03 | RAG/Retrieval/Prompt Injection | Indirect prompt injection from retrieved content | `docs/security/evidence/phase7-rag-prompt-injection-threats.md` |
| T7-07-04 | RAG/Retrieval/Prompt Injection | Retrieved-content data exfiltration | `docs/security/evidence/phase7-rag-prompt-injection-threats.md` |
| T7-07-05 | RAG/Retrieval/Prompt Injection | Stale revoked document remains retrievable | `docs/security/evidence/phase7-rag-prompt-injection-threats.md` |
| T7-07-06 | RAG/Retrieval/Prompt Injection | Citation/provenance confusion | `docs/security/evidence/phase7-rag-prompt-injection-threats.md` |
| T7-08-01 | Model/Provider/Data Boundary | Unauthorized sensitive context sent to model provider | `docs/security/evidence/phase7-model-provider-data-boundary-threats.md` |
| T7-08-02 | Model/Provider/Data Boundary | Provider-routing or configuration confusion | `docs/security/evidence/phase7-model-provider-data-boundary-threats.md` |
| T7-08-03 | Model/Provider/Data Boundary | Provider credential exposure | `docs/security/evidence/phase7-model-provider-data-boundary-threats.md` |
| T7-08-04 | Model/Provider/Data Boundary | Untrusted model output treated as trusted control data | `docs/security/evidence/phase7-model-provider-data-boundary-threats.md` |
| T7-08-05 | Model/Provider/Data Boundary | Unbounded model consumption | `docs/security/evidence/phase7-model-provider-data-boundary-threats.md` |
| T7-08-06 | Model/Provider/Data Boundary | Sensitive AI context retained in observability surfaces | `docs/security/evidence/phase7-model-provider-data-boundary-threats.md` |
| T7-09-01 | Agent/Tool/MCP/Execution | Model-to-tool authority escalation | `docs/security/evidence/phase7-agent-tool-mcp-execution-threats.md` |
| T7-09-02 | Agent/Tool/MCP/Execution | Tool argument injection | `docs/security/evidence/phase7-agent-tool-mcp-execution-threats.md` |
| T7-09-03 | Agent/Tool/MCP/Execution | Malicious MCP metadata or tool description | `docs/security/evidence/phase7-agent-tool-mcp-execution-threats.md` |
| T7-09-04 | Agent/Tool/MCP/Execution | Credential disclosure to tool or MCP server | `docs/security/evidence/phase7-agent-tool-mcp-execution-threats.md` |
| T7-09-05 | Agent/Tool/MCP/Execution | Unsafe code execution or sandbox boundary failure | `docs/security/evidence/phase7-agent-tool-mcp-execution-threats.md` |
| T7-09-06 | Agent/Tool/MCP/Execution | Recursive or chained capability exhaustion | `docs/security/evidence/phase7-agent-tool-mcp-execution-threats.md` |
| T7-10-01 | Lifecycle/Revocation/Deletion | Revoked authorization remains effective | `docs/security/evidence/phase7-lifecycle-revocation-deletion-threats.md` |
| T7-10-02 | Lifecycle/Revocation/Deletion | Deleted document remains retrievable | `docs/security/evidence/phase7-lifecycle-revocation-deletion-threats.md` |
| T7-10-03 | Lifecycle/Revocation/Deletion | Deleted conversation remains accessible | `docs/security/evidence/phase7-lifecycle-revocation-deletion-threats.md` |
| T7-10-04 | Lifecycle/Revocation/Deletion | Credential revocation does not terminate effective capability | `docs/security/evidence/phase7-lifecycle-revocation-deletion-threats.md` |
| T7-10-05 | Lifecycle/Revocation/Deletion | Asynchronous race restores stale security state | `docs/security/evidence/phase7-lifecycle-revocation-deletion-threats.md` |
| T7-10-06 | Lifecycle/Revocation/Deletion | Security-significant lifecycle event is not auditable | `docs/security/evidence/phase7-lifecycle-revocation-deletion-threats.md` |
| T7-11-01 | Abuse/Availability/Economic | Request flooding | `docs/security/evidence/phase7-abuse-availability-economic-threats.md` |
| T7-11-02 | Abuse/Availability/Economic | Oversized input exhaustion | `docs/security/evidence/phase7-abuse-availability-economic-threats.md` |
| T7-11-03 | Abuse/Availability/Economic | Expensive RAG query amplification | `docs/security/evidence/phase7-abuse-availability-economic-threats.md` |
| T7-11-04 | Abuse/Availability/Economic | Agent/tool recursion or fan-out | `docs/security/evidence/phase7-abuse-availability-economic-threats.md` |
| T7-11-05 | Abuse/Availability/Economic | Queue starvation or retry amplification | `docs/security/evidence/phase7-abuse-availability-economic-threats.md` |
| T7-11-06 | Abuse/Availability/Economic | Storage/log amplification | `docs/security/evidence/phase7-abuse-availability-economic-threats.md` |

## Register statistics

- Total threat hypotheses: **42**
- Unique threat identifiers: **42**
- Threat domains: **7**

## Evidence rule

A threat may move from THREAT HYPOTHESIS to VERIFIED FINDING only when
authorized executable evidence demonstrates the behavior.

# Result

**42 THREAT HYPOTHESES CONSOLIDATED**
