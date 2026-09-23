# Phase 11 — Action 11.1 Initialization and Immutable Handoff

## Parent

Phase 10 completion SHA:

`f074eadd545eebe408330998b579ca3e800ff9db`

Phase 10 status:

**COMPLETE — 18/18 ACTIONS**

Phase 10 confirmed findings/hardenings:

- H10-01 — REMEDIATED
- H10-02 — REMEDIATED
- H10-03 — REMEDIATED
- H10-04 — HARDENED
- H10-05 — REMEDIATED
- H10-06 — REMEDIATED

Confirmed Phase 10 findings knowingly left unremediated:

**0**

## Phase 11 branch

`security/phase-11-agent-action-mcp-tool-code-execution-security`

## Objective

Assess security boundaries introduced when the AI application can select,
authorize, invoke and compose tools, actions, MCP services and code-execution
capabilities.

Phase 11 independently verifies whether application identity, tenant
authorization, user intent and safety constraints survive the complete
agent/action/tool lifecycle.

## In-scope security surfaces

- agent planning and tool selection;
- tool registration and discovery;
- tool arguments and schemas;
- tool authorization;
- user versus system authority;
- MCP clients and servers;
- MCP authentication and headers;
- credential delegation;
- action confirmation;
- side effects and mutation boundaries;
- tool-result trust;
- indirect prompt injection into tool use;
- confused-deputy behavior;
- cross-user and cross-tenant tool access;
- SSRF/network-capable tools;
- file-system tools;
- shell/code execution;
- subprocess boundaries;
- secrets exposed to tools;
- tool chaining;
- loops and recursive actions;
- resource/cost exhaustion;
- auditability and provenance;
- revocation;
- failure and rollback behavior.

## Authorized laboratory boundary

Testing remains restricted to the owned local/Codespaces project.

Allowed:

- repository source;
- pinned local Docker images;
- loopback/local synthetic services;
- local mock MCP;
- local mock LLM;
- local webhook receiver;
- local email mock;
- synthetic identities;
- synthetic credentials;
- deterministic unit/property tests;
- bounded integration tests.

Outside scope unless separately approved:

- public Onyx deployments;
- third-party MCP servers;
- production accounts;
- real credentials;
- real customer data;
- public exploit attempts;
- paid APIs;
- uncontrolled Internet targets.

GitHub fetch/push is permitted only as repository control-plane synchronization.

## Resource limits

Default test limits remain:

- duration ≤ 60 seconds;
- concurrency ≤ 10;
- requests ≤ 100;
- file size ≤ 1 MB;
- synthetic data only.

## Stop conditions

Stop the affected test if any of the following occurs:

- unexpected external application network access;
- real credential or customer-data discovery;
- authorization scope becomes unclear;
- execution becomes unbounded;
- uncontrolled code execution occurs outside the defined test harness;
- test side effects cannot be confidently rolled back.

## Phase 11 security invariants

1. A model must not gain authority merely by requesting a tool.
2. Tool authorization must derive from trusted application/user context.
3. Tool arguments must not choose another user's or tenant's authority.
4. Retrieved or tool-produced content remains untrusted data.
5. MCP metadata and headers must not become an implicit trust bypass.
6. Credentials must be scoped to the intended tool and operation.
7. Side-effecting actions must respect confirmation/authorization policy.
8. Tool chaining must not amplify privileges.
9. Code execution must remain explicitly bounded and isolated.
10. Network-capable tools must respect destination/scope controls.
11. Revoked authorization must not remain usable through cached tool state.
12. Tool failures must fail safely without leaking secrets.
13. Tool actions must remain attributable and auditable.
14. Agent loops must remain resource bounded.
15. Security-sensitive tool paths require deterministic regression evidence.

## Evidence-strength terminology

Phase 11 must distinguish:

- STATIC/SOURCE VERIFIED
- PROPERTY VERIFIED
- UNIT VERIFIED
- MOCK INTEGRATION VERIFIED
- BOUNDED LOCAL RUNTIME VERIFIED
- PRODUCTION RUNTIME NOT CLAIMED

Absence of an observed bypass must not be described as proof that arbitrary
agent/model behavior is safe.

## Finding discipline

A security finding requires:

1. deterministic synthetic reproduction;
2. concrete security impact within the authorized lab;
3. identified root cause;
4. minimal remediation when appropriate;
5. regression evidence;
6. explicit evidence-strength limitations.

Harness, dependency and environment failures are not product vulnerabilities.

## Completion rule

Phase 11 cannot be marked complete until:

- every planned action has evidence;
- every confirmed finding has a disposition;
- representative regressions pass;
- residual risk is explicit;
- Git state is clean;
- local and remote branch heads match;
- production/compliance claims remain bounded by actual evidence.

## Result

**ACTION 11.1: COMPLETE**

**RESULT=PHASE_11_ACTION_11_1_PASS**
