# Phase 7 Action 7.2 - Threat-Model Charter

## Purpose

Convert the evidence-backed Phase 6 Onyx architecture into a formal security
threat model and derive testable security requirements for later verification.

## Target

Onyx repository baseline:

`160f9b143605ca45a85bd387b5bd173840bab15d`

## Evidence inheritance

Phase 7 inherits the Phase 6 evidence describing:

- application architecture;
- identity and request context;
- tenant-aware data paths;
- document ingestion and RAG;
- LLM/chat generation;
- agents/actions/tools;
- MCP;
- code-execution boundaries;
- persistence;
- queues and caches;
- deletion and revocation;
- credentials and external dependencies;
- synthetic security fixtures;
- local mock-service contracts.

## Evidence classes

Every Phase 7 statement must be classified as one of:

1. OBSERVED
   Directly supported by Phase 6 source/configuration evidence.

2. THREAT HYPOTHESIS
   A plausible failure or attack requiring later verification.

3. SECURITY REQUIREMENT
   A property that the system should satisfy.

4. VERIFIED FINDING
   Requires later executable evidence.

Phase 7 does not convert a threat hypothesis into a vulnerability claim.

## Safety boundary

- authorized local learning environment only;
- synthetic data only;
- no production/customer data;
- no production credentials;
- no paid services;
- no uncontrolled external APIs;
- no active exploitation required for this phase;
- no assumption that static controls work at runtime.

## Primary security properties

Phase 7 evaluates threats against:

- confidentiality;
- integrity;
- availability;
- authentication;
- authorization;
- tenant isolation;
- ownership;
- least privilege;
- provenance;
- privacy;
- lifecycle consistency;
- safe AI/tool execution;
- auditability;
- bounded resource consumption.

## Completion condition

Phase 7 must produce:

- threat actors;
- protected assets;
- trust boundaries;
- misuse/abuse cases;
- structured threat register;
- risk prioritization;
- security requirements;
- threat-to-requirement traceability;
- residual-risk register;
- later-test mapping.
