# Phase 3 Foundations - Architecture and Trust-Boundary Diagrams
## Provenance
- Branch: `security/phase-3-foundations`
- Source HEAD: `2e7a5ef92090aa6997f1841d4dba440618cbf306`
- Basis: Phase 3 static source mapping and evidence
- Runtime status: **UNVERIFIED**
## Request and security-control flow
```mermaid
flowchart LR
    U[External Client]
    T[HTTP / HTTPS / TLS]
    R[Routes and API Handlers]
    A[Authentication]
    S[Session / Cookie / Token State]
    Z[Authorization / Ownership / Tenant Checks]
    B[Business Logic]
    D[(Data Stores)]
    X[Downstream Services / Webhooks]
    U --> T
    T --> R
    R --> A
    A --> S
    S --> Z
    Z --> B
    B --> D
    B --> X
```
### Security interpretation
Each transition can become a trust decision. Runtime verification must
determine which transitions actually exist and whether the expected
controls execute before sensitive actions.
## Identity and authorization model
```mermaid
flowchart TD
    I[Identity]
    AU[Authentication]
    P[Principal / Actor]
    RO[Role]
    PE[Permission]
    RE[Requested Resource]
    OW[Ownership]
    TE[Tenant Boundary]
    DE{Authorization Decision}
    AL[Allow]
    DN[Deny]
    I --> AU
    AU --> P
    P --> RO
    RO --> PE
    P --> DE
    PE --> DE
    RE --> OW
    OW --> DE
    TE --> DE
    DE --> AL
    DE --> DN
```
## Trust-boundary model
```mermaid
flowchart LR
    subgraph B1["Boundary 1 - Untrusted Client"]
        C[Client Input]
    end
    subgraph B2["Boundary 2 - Application"]
        API[Web / API]
        ID[Identity State]
        AUTHZ[Authorization]
        LOGIC[Business Logic]
    end
    subgraph B3["Boundary 3 - Persistence"]
        DB[(Database / Storage)]
    end
    subgraph B4["Boundary 4 - External Integration"]
        EXT[External / Downstream Service]
    end
    C --> API
    API --> ID
    ID --> AUTHZ
    AUTHZ --> LOGIC
    LOGIC --> DB
    LOGIC --> EXT
```
## Evidence limitations
These diagrams are security-analysis models derived from static
candidates. They are not assertions of confirmed runtime architecture.
Action 3.14 must verify representative paths using the authorized local
lab before runtime conclusions are made.
