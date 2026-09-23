# Phase 11 — Action 11.2 Agent / Tool / MCP Architecture Inventory

## Objective

Map the complete agent/tool authority path before adversarial testing.

## Primary surfaces

The source inventory identifies the following security domains.

### Tool construction

Primary implementation:

`backend/onyx/tools/tool_constructor.py`

Responsibilities include:

- persona-attached tool selection;
- enabled/disabled state;
- allowed-tool filtering;
- built-in tool construction;
- custom OpenAPI action construction;
- OAuth/passthrough credential selection;
- MCP tool construction;
- trusted user identity propagation.

### Tool dispatch

Primary implementation:

`backend/onyx/tools/tool_runner.py`

Responsibilities include:

- model-requested tool-call matching;
- unknown-tool rejection;
- bounded concurrency;
- tool-specific trusted override arguments;
- exception handling;
- tool-result processing.

### MCP

Primary surfaces include:

- MCP tool wrapper;
- MCP client;
- MCP credential resolution;
- authentication templates;
- request-header policy;
- OAuth;
- SSRF controls;
- MCP server access controls.

### External actions

The external-app subsystem contains:

- action recognition;
- endpoint policies;
- credential availability;
- action attribution;
- external provider implementations.

### Approval boundary

The sandbox proxy and action-approval subsystem contains:

- action matching;
- ALWAYS / ASK / DENY decisions;
- approval persistence;
- session grants;
- credential injection;
- side-effect authorization.

### Sandbox / code execution

Security surfaces include:

- Python/code interpreter;
- coding agent;
- sandbox lifecycle;
- proxy egress;
- credential injection;
- filesystem operations;
- subprocess execution;
- network controls.

## Phase 11 fixed action plan

1. 11.1 — immutable handoff / scope / safety charter
2. 11.2 — agent/tool/MCP architecture inventory
3. 11.3 — tool authority / selection / dispatch
4. 11.4 — MCP authentication / headers / credentials / SSRF
5. 11.5 — side-effect approval / confused-deputy boundaries
6. 11.6 — tool-result trust / indirect prompt injection
7. 11.7 — custom/external action credential delegation
8. 11.8 — network / URL / SSRF / destination controls
9. 11.9 — Python / shell / code-execution / filesystem isolation
10. 11.10 — credential / secret exposure and telemetry
11. 11.11 — tool chaining / recursion / resource exhaustion
12. 11.12 — consolidated agent attack matrix / negative tests
13. 11.13 — bounded synthetic agent runtime verification
14. 11.14 — findings / regression / framework mapping
15. 11.15 — residual risk / final completion gate

## Evidence strength

This action is:

**STATIC / SOURCE INVENTORY VERIFIED**

It does not itself prove security controls.

## Completion

**ACTION 11.2: COMPLETE**

**RESULT=PHASE_11_ACTION_11_2_PASS**
