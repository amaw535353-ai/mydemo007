# Phase 11 — Action 11.14 Findings, Regression and Framework Mapping

## Findings closure

| ID | Root cause | Disposition |
|---|---|---|
| H11-01 | Arbitrary tool output entered the next LLM cycle without a generic instruction/data boundary | REMEDIATED |
| H11-02 | Custom OpenAPI actions used schema-derived destinations without applying the shared outbound SSRF policy immediately before execution | MITIGATED WITH DOCUMENTED DNS TOCTOU RESIDUAL |
| H11-03 | Generic tool tracing recorded arbitrary argument values and full tool-result content | REMEDIATED |
| H11-04 | Production LLM loop did not supply the existing tool-runner fan-out cap | REMEDIATED |

Confirmed findings/hardenings:

**4**

Fully remediated:

**3**

Mitigated with explicit residual risk:

**1**

Confirmed findings without a disposition:

**0**

## Cross-cutting root causes

Phase 11 findings cluster around four reusable AI-product security lessons:

1. model/tool output is data, not authority;
2. every credentialed outbound path requires its own destination control;
3. observability must not automatically copy AI/tool payloads;
4. resource limits must be connected at the production call site, not merely
   implemented in a lower-level helper.

## Regression gate

Ten Phase-11 security regression files executed actual tests and passed,
including the integrated bounded-agent runtime harness.

**PHASE 11 REGRESSION GATE: PASS**

Results:

`docs/security/evidence/phase11-action-11.14-regression-results.txt`

SHA-256:

`17fee7cd9e41ab0b959e6ad9b547dadc0af6e7b8d4162f51f0d811844702bb71`

## Engineering framework crosswalk

This is an engineering crosswalk, not certification.

### NIST AI RMF / GenAI Profile

Phase 11 contributes evidence to:

- GOVERN — explicit tool authority, residual risk and responsibility boundaries;
- MAP — agent/MCP/tool/credential/code-execution trust boundaries;
- MEASURE — negative tests and adversarial agent properties;
- MANAGE — remediation, runtime bounds and regression controls.

### NIST SSDF

The work supports secure-development practices around:

- security requirements;
- secure implementation;
- vulnerability reproduction;
- remediation;
- regression verification.

### OWASP GenAI / LLM security

Phase 11 addresses themes including:

- indirect prompt injection;
- excessive agency;
- sensitive-information disclosure;
- insecure tool/plugin design;
- unsafe downstream action handling;
- resource exhaustion.

### OWASP Agentic application security

Directly exercised agentic controls include:

- tool authorization;
- MCP trust;
- credential delegation;
- approval boundaries;
- tool-result trust;
- action destination safety;
- code-execution containment;
- bounded autonomy.

### MITRE ATLAS

The assessment contributes adversarial-AI evidence around:

- prompt manipulation;
- abuse of agentic capabilities;
- information disclosure;
- persistence through tools/state;
- resource abuse.

### OWASP ASVS principles

Conventional application-security principles reinforced include:

- authorization;
- tenant/user identity propagation;
- SSRF prevention;
- sensitive-data handling;
- secure logging;
- resource management;
- business-logic security.

## Residual risks

Explicit Phase-11 residuals include:

- DNS validation-to-connect race on the generic custom-action requests
  transport;
- tool-specific exception and stack-trace content;
- third-party MCP/provider behavior;
- production OAuth/provider revocation behavior;
- unknown kernel/container vulnerabilities;
- real-model resistance to sophisticated indirect prompt injection;
- production-scale latency/cost behavior;
- operator configuration and incident response.

## Responsibility split

Application engineering owns correct authority propagation and safe tool
implementation.

Security engineering owns threat modeling, negative testing, remediation
verification, attack-matrix maintenance and residual-risk communication.

Operations owns production provider configuration, networking, telemetry,
container runtime, monitoring and incident response.

## Completion

**ACTION 11.14: COMPLETE**

**PHASE 11 REGRESSION GATE: PASS**

**UNADDRESSED CONFIRMED PHASE 11 FINDINGS: 0**

**RESULT=PHASE_11_ACTION_11_14_PASS**
