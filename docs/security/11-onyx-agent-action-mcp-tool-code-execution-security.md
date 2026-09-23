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
