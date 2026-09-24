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
