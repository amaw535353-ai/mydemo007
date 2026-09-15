# Phase 3 Action 3.14 - Practical Verification Evidence
## Scope
This action performed bounded runtime verification in an authorized,
synthetic, loopback-only local harness and verified Phase 3 evidence
integrity.
**The runtime observations below apply to the synthetic harness only.**
They do not prove that mydemo007, Onyx, a hosted deployment or any
production system enforces the same behavior.
## Provenance
- Branch: `security/phase-3-foundations`
- Baseline HEAD: `c449436bf4092f70977238256263b3b3d7c2578f`
- Network target: `127.0.0.1:62153`
- External services contacted: **NO**
- Real credentials used: **NO**
- Synthetic HTTP requests: **8**
## Evidence-integrity verification
- Manifest rows verified: **11**
- Manifest SHA-256 checks: **PASS**
- Manifest byte-count checks: **PASS**
- Mermaid diagrams present: **PASS**
- Runtime limitation marker preserved: **PASS**
## Local HTTP/authentication/authorization verification
| Check | Expected | Observed | Result |
|---|---:|---:|---|
| Public request | 200 | 200 | PASS |
| Protected without credential | 401 | 401 | PASS |
| Protected with invalid synthetic token | 401 | 401 | PASS |
| Protected with valid synthetic token | 200 | 200 | PASS |
| Admin resource as non-admin | 403 | 403 | PASS |
| Admin resource as synthetic admin | 200 | 200 | PASS |
| Owned resource | 200 | 200 | PASS |
| Other-owned resource | 403 | 403 | PASS |
## Cookie verification
- Secure: **PASS**
- HttpOnly: **PASS**
- SameSite=Strict: **PASS**
## Cryptographic foundation verification
- SHA-256 deterministic digest: **PASS**
- HMAC-SHA256 deterministic keyed integrity: **PASS**
- Plain digest differs from keyed HMAC: **PASS**
## Interpretation
The harness demonstrates the practical distinction between:
- unauthenticated and authenticated requests;
- authentication and authorization;
- role-based access decisions;
- object-ownership decisions;
- state carried through security-sensitive HTTP headers;
- unkeyed hashing and keyed message authentication.
It is runtime evidence for the local synthetic control harness only.
Application-specific runtime security effectiveness remains a
later-phase verification responsibility.
## Safety and boundedness
- Loopback-only listener: **PASS**
- Maximum HTTP requests: **8**
- Per-request timeout: **3 seconds**
- Synthetic token only: **PASS**
- Synthetic role only: **PASS**
- No real user/customer data: **PASS**
- No external API or identity provider: **PASS**
- Harness terminated after verification: **PASS**
## Result
Harness result: **PASS**
Action 3.14 result: **PASS**
