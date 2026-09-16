# Phase 7 - Onyx Threat Modeling and Security Requirements

Phase 7 status: **IN PROGRESS**

## Objective

Transform the evidence-backed Onyx architecture established during Phase 6
into a formal threat model, prioritized threat register, and testable security
requirements for subsequent security-testing phases.

## Baseline

Pinned Onyx revision:

`160f9b143605ca45a85bd387b5bd173840bab15d`

Phase 6 completion parent:

`117775de892781d20eac4762bc464a21ab6b99d6`

## Evidence discipline

Phase 7 distinguishes:

- observed architecture;
- threat hypotheses;
- security requirements;
- verified vulnerabilities.

A plausible threat is not automatically a vulnerability.

## Actions

### Action 7.1 - Phase 7 branch initialization

Status: **COMPLETE**

Branch:

`security/phase-7-threat-model`

### Action 7.2 - Threat-model charter

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase7-threat-model-charter.md`

### Action 7.3 - Security assets and objectives

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase7-assets-security-objectives.md`

### Action 7.4 - Threat actors and trust boundaries

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase7-threat-actors-and-boundaries.md`

## Actions 7.5 through 7.9

### Action 7.5 - Web, API and business-logic threats

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase7-web-api-business-logic-threats.md`

### Action 7.6 - Identity, authorization and tenant-isolation threats

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase7-identity-authorization-tenant-threats.md`

### Action 7.7 - RAG, retrieval and prompt-injection threats

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase7-rag-prompt-injection-threats.md`

### Action 7.8 - Model, provider and data-boundary threats

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase7-model-provider-data-boundary-threats.md`

### Action 7.9 - Agent, tool, MCP and code-execution threats

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase7-agent-tool-mcp-execution-threats.md`

## Current threat-model status

Phase 7 now contains threat hypotheses covering:

- web/API/business logic;
- authentication and authorization;
- tenant isolation;
- RAG and retrieval;
- indirect prompt injection;
- model/provider boundaries;
- sensitive AI context;
- agents and tools;
- MCP;
- code execution;
- resource/economic abuse.

None of these threat hypotheses is represented as a confirmed vulnerability
without later executable evidence.

## Next

Actions 7.10 through 7.14:

- lifecycle/deletion/revocation threats;
- availability and abuse threats;
- structured consolidated threat register;
- risk prioritization;
- testable security requirements.

---

## Action 7.10 - Lifecycle, revocation and deletion threats

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase7-lifecycle-revocation-deletion-threats.md`

## Action 7.11 - Abuse, availability and economic threats

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase7-abuse-availability-economic-threats.md`

## Action 7.12 - Consolidated threat register

Status: **COMPLETE**

Threat hypotheses:

**42**

Evidence:

`docs/security/evidence/phase7-consolidated-threat-register.md`

## Action 7.13 - Threat verification prioritization

Status: **COMPLETE**

Priority classes:

- P1: 26
- P2: 16

These classes represent verification order, not vulnerability severity.

Evidence:

`docs/security/evidence/phase7-threat-prioritization.md`

## Action 7.14 - Testable security requirements and traceability

Status: **COMPLETE**

Security requirements:

**25**

Evidence:

`docs/security/evidence/phase7-security-requirements-traceability.md`

## Current Phase 7 state

Completed actions:

**7.1 through 7.14**

Threat hypotheses:

**42**

Testable security requirements:

**25**

Confirmed vulnerabilities:

**0 claimed by Phase 7**

Runtime security properties:

**NOT YET ASSUMED VERIFIED**

## Remaining Phase 7 work

Action 7.15:

**Final Phase 7 completion-gate audit and handoff into executable security
testing.**
