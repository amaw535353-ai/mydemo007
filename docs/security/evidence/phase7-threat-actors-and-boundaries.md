# Phase 7 Action 7.4 - Threat Actors and Trust Boundaries

## Threat actors

### TA-01 Unauthenticated external actor

Capabilities:

- submit reachable requests;
- manipulate request inputs;
- attempt authentication/session abuse.

Primary interests:

- unauthorized access;
- information disclosure;
- resource exhaustion.

### TA-02 Authenticated ordinary user

Capabilities:

- use legitimate application functionality;
- control application inputs;
- create conversations;
- interact with authorized data.

Primary interests:

- horizontal privilege escalation;
- accessing another user's resources;
- manipulating business logic.

### TA-03 Cross-tenant authenticated user

Capabilities:

- possesses valid identity in Tenant A;
- controls Tenant A inputs.

Primary interests:

- accessing Tenant B documents;
- retrieving Tenant B embeddings/context;
- accessing Tenant B conversations;
- invoking Tenant B capabilities.

### TA-04 Malicious document/content author

Capabilities:

- influences content later processed or retrieved by RAG.

Primary interests:

- indirect prompt injection;
- misleading model behavior;
- unauthorized tool influence;
- data exfiltration through model behavior.

### TA-05 Malicious or compromised tool/MCP endpoint

Capabilities:

- returns attacker-controlled tool metadata or results;
- may receive application-originated arguments.

Primary interests:

- credential misuse;
- instruction injection;
- sensitive-data collection;
- unsafe side effects.

### TA-06 Compromised external/model dependency

Capabilities:

- receives data sent across provider boundaries;
- returns untrusted output.

Primary interests:

- data exposure;
- integrity manipulation;
- dependency abuse.

### TA-07 Privileged insider or misconfigured administrator

Capabilities:

- elevated configuration or administrative permissions.

Primary interests/risk:

- accidental or intentional over-privilege;
- unsafe configuration;
- inappropriate data access.

### TA-08 Automated abusive client

Capabilities:

- repeated requests;
- parallel requests;
- oversized workloads;
- expensive AI/RAG/tool operations.

Primary interests:

- denial of service;
- economic/resource exhaustion.

---

# Trust Boundaries

## TB-A - Browser/User -> Application

Security controls expected:

- authentication;
- session protection;
- request validation;
- route authorization;
- object authorization.

Threat examples:

- identity spoofing;
- session misuse;
- IDOR/BOLA;
- parameter manipulation.

## TB-B - Identity/Tenant Context -> Protected Data

Security controls expected:

- tenant resolution;
- ownership enforcement;
- tenant-scoped queries;
- access metadata enforcement.

Threat examples:

- cross-tenant access;
- confused tenant context;
- stale permissions;
- authorization bypass.

## TB-C - Documents -> RAG/Retrieval -> Model Context

Security controls expected:

- ingestion authorization;
- metadata integrity;
- tenant filtering;
- ACL filtering;
- untrusted-content handling.

Threat examples:

- cross-tenant retrieval;
- malicious retrieved instructions;
- poisoned context;
- unauthorized document disclosure.

## TB-D - Application -> Model Provider

Security controls expected:

- data minimization;
- provider configuration;
- credential protection;
- egress restrictions;
- resource limits.

Threat examples:

- sensitive prompt leakage;
- provider credential exposure;
- uncontrolled external calls;
- excessive token/resource use.

## TB-E - Model -> Tool/MCP/Code Execution

Security controls expected:

- capability allowlisting;
- authorization;
- argument validation;
- credential scoping;
- confirmation where necessary;
- sandboxing;
- execution/resource limits.

Threat examples:

- prompt-to-tool escalation;
- unauthorized tool invocation;
- malicious arguments;
- credential leakage;
- arbitrary code execution;
- external side effects.

## TB-F - Application -> Database/Queue/Cache/Index/Object Storage

Security controls expected:

- tenant-aware persistence;
- lifecycle consistency;
- revocation propagation;
- deletion propagation;
- integrity controls.

Threat examples:

- stale authorization state;
- deleted content remaining retrievable;
- stale cache permissions;
- asynchronous race conditions;
- reappearance of revoked data.

---

## Phase 6 limitation inherited

These boundaries are evidence-backed architectural surfaces.

Their runtime security effectiveness has not yet been proven.

Therefore every threat identified here remains a threat hypothesis until a
later authorized verification phase supplies executable evidence.
