# Phase 11 — Onyx Agent / Action / MCP / Tool / Code-Execution Security

## Status

**Phase 11: IN PROGRESS**

## Parent

Phase 10 final SHA:

`f074eadd545eebe408330998b579ca3e800ff9db`

## Objective

Assess the security properties of Onyx agentic capabilities across planning,
tool selection, action execution, MCP integration, credential use, side effects
and code-execution boundaries.

## Core security invariants

- model output is not authorization;
- tool authority derives from trusted user/application context;
- cross-user and cross-tenant tool access fails closed;
- MCP boundaries preserve identity and authorization;
- tool arguments cannot arbitrarily select stronger credentials or identities;
- untrusted retrieved/tool content cannot legitimately authorize actions;
- side effects respect explicit authorization and confirmation policy;
- secrets are minimized and scoped;
- network and code-execution capabilities remain bounded;
- tool chains cannot amplify privileges;
- failures fail safely;
- actions remain attributable and auditable;
- recursive/agent execution remains resource bounded.

## Safety boundary

Phase 11 remains restricted to the authorized local synthetic laboratory.

No public exploitation, real credentials, real customer data or uncontrolled
external execution is authorized.

## Action 11.1 — Initialization and immutable handoff

Phase 11 was created directly from the completed Phase 10 SHA.

Authorization, test scope, safety boundary, evidence terminology, stop
conditions and completion requirements were recorded before technical
agent/tool testing begins.

**Action 11.1 status: COMPLETE.**

## Phase 11 action plan

Phase 11 uses 15 actions from immutable initialization through final residual
risk closure.

The assessment preserves separate evidence and commits per action even when
multiple actions are executed in an accelerated batch.

## Action 11.2 — Agent / tool / MCP architecture inventory

Action 11.2 mapped tool construction, execution, MCP, credentials, approvals,
external actions, sandboxing, networking and code-execution surfaces.

The inventory is a discovery artifact rather than a vulnerability claim.

**Action 11.2 status: COMPLETE.**

## Action 11.3 — Tool authority, selection and dispatch

Action 11.3 verified that executable tool authority comes from the
application-constructed tool set rather than arbitrary model-requested names.

Unknown tools are dropped and execution capacity can bound the tool batch.

The first synthetic harness run omitted the required emitter; correcting the
harness allowed the intended security properties to execute successfully.

**Action 11.3 status: COMPLETE.**

## Action 11.4 — MCP authentication, credential and SSRF boundaries

Action 11.4 verified MCP request-header policy, managed credential precedence,
per-user credential constraints, guarded MCP HTTP transport and sandbox-side
user-access enforcement.

No MCP authorization or credential bypass was confirmed.

**Action 11.4 status: COMPLETE.**

## Action 11.5 — Action approval and confused-deputy boundaries

Action 11.5 verified strictest-policy behavior, ASK approval scope, MCP
fail-closed policy defaults and removal of in-band session authority before
forwarding requests.

No confused-deputy or approval bypass was confirmed.

**Action 11.5 status: COMPLETE.**

## Action 11.6 — Tool-result trust and indirect prompt injection

Action 11.6 identified a generic instruction-integrity gap: arbitrary tool
output was replayed directly into the next LLM cycle without a common
instruction/data trust boundary.

All replayed tool results are now explicitly labeled untrusted and unable to
legitimately change identity, authorization, approval or credential scope.

**H11-01: REMEDIATED.**

**Action 11.6 status: COMPLETE.**

## Action 11.7 — Custom / external credential delegation

Action 11.7 traced custom-tool and external-app credential authority to trusted
authenticated user or sandbox identity.

OAuth configuration linking and incompatible custom Authorization/passthrough
configuration have explicit gates.

No credential-delegation bypass was confirmed.

**Action 11.7 status: COMPLETE.**

## Action 11.8 — Network / URL / SSRF controls

Action 11.8 identified that custom OpenAPI actions did not apply the common
outbound SSRF policy immediately before execution.

Custom actions now validate their destination using the administrator-controlled
SSRF policy and do not automatically follow redirects.

**H11-02: MITIGATED.**

A DNS validation-to-connect race remains explicitly recorded as residual risk.

**Action 11.8 status: COMPLETE.**

## Action 11.9 — Code execution and filesystem isolation

Action 11.9 verified container privilege reduction, resource limits, absence of
a sandbox Docker-socket mount, filesystem traversal containment and bounded
Python file staging/execution properties.

No host escape was confirmed.

Production kernel/container escape testing is not claimed.

**Action 11.9 status: COMPLETE.**

## Action 11.10 — Secret and telemetry boundaries

Action 11.10 confirmed that generic tool tracing recorded arbitrary tool
argument values and complete tool-result content.

Tracing now preserves structural observability while excluding arbitrary
argument values, nested values and tool-output content.

The generic error-span paths also use structural argument summaries.

**H11-03: REMEDIATED.**

Tool-specific exception strings and stack traces remain explicit residual
review areas.

**Action 11.10 status: COMPLETE.**

## Action 11.11 — Tool chaining and resource exhaustion

Action 11.11 verified that the LLM cycle itself is finite, but identified an
application-level resource gap: the production LLM loop passed no tool fan-out
cap to a runner that already supported one.

Per-cycle tool execution is now capped at 10 calls.

**H11-04: REMEDIATED.**

The resulting agent path has finite cycle, per-cycle fan-out and per-tool
execution bounds.

**Action 11.11 status: COMPLETE.**

## Action 11.12 — Consolidated agent security attack matrix

Action 11.12 consolidated tool authority, MCP, approval, indirect
tool-result injection, delegated credentials, SSRF, sandbox execution,
telemetry and resource-exhaustion attack paths.

Nine representative Phase 11 negative-security test files executed and passed.

**Action 11.12 status: COMPLETE.**

## Action 11.13 — Bounded synthetic agent runtime

Action 11.13 executed an integrated repository-code scenario spanning bounded
tool dispatch, untrusted tool-result handling, MCP header authority, managed
credential precedence, action approval, custom-action SSRF prevention and trace
content minimization.

The integrated synthetic runtime passed with Docker networking disabled.

**Action 11.13 status: COMPLETE.**
