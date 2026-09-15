# Phase 3 - Networking, Web, API, Identity, and Cryptography Foundations

## Phase status

Phase 3 status: **IN PROGRESS**.

## Baseline

- Phase 3 starting commit: `349dee89221347306180917645f6e9ba2e24eb9b`
- Working branch: `security/phase-3-foundations`
- Phase 2 static inventory: COMPLETE

## Action 3.2 - Network Architecture and Protocol Foundations

Status: **COMPLETE**.

### What

Identify source-level network architecture and protocol candidates and connect them to security engineering concepts.

### Where

Tracked project source and configuration files, excluding `docs/security/` evidence content.

### Why

An AI application security engineer must understand how clients, services, APIs, data stores, model providers, agents, tools, and infrastructure communicate before evaluating trust boundaries, authentication, encryption, exposure, SSRF, request routing, tenant isolation, or network-based attack paths.

### Network model

The following conceptual layers will be used during later security analysis:

- **Name resolution:** DNS converts names into reachable targets.
- **Network layer:** IP identifies network endpoints.
- **Transport layer:** TCP and UDP carry application traffic.
- **Application layer:** HTTP, HTTPS, WebSocket, gRPC, SMTP and service-specific protocols carry application semantics.
- **Transport protection:** TLS protects confidentiality and integrity when correctly configured.
- **Exposure controls:** bind addresses, listeners, ports, proxies, ingress and egress determine reachability.
- **Trust boundaries:** every transition between clients, services, tenants, tools, data stores and external providers must eventually be validated rather than assumed.

### Static observations

- HTTP: 1128 candidate files, 2962 matching lines.
- HTTPS: 916 candidate files, 8082 matching lines.
- TCP: 86 candidate files, 176 matching lines.
- UDP: 4 candidate files, 10 matching lines.
- WebSocket: 42 candidate files, 380 matching lines.
- gRPC: 11 candidate files, 87 matching lines.
- DNS: 98 candidate files, 229 matching lines.
- TLS_SSL: 127 candidate files, 552 matching lines.
- SMTP: 11 candidate files, 28 matching lines.
- PostgreSQL: 488 candidate files, 1454 matching lines.
- Redis: 356 candidate files, 1866 matching lines.

Network-control candidates:

- bind_listen: 182 candidate files, 603 matching lines.
- port: 420 candidate files, 2087 matching lines.
- proxy_upstream: 375 candidate files, 1568 matching lines.
- ingress: 38 candidate files, 108 matching lines.
- egress: 102 candidate files, 230 matching lines.
- network: 246 candidate files, 600 matching lines.
- loopback: 240 candidate files, 623 matching lines.
- wildcard_bind: 216 candidate files, 1098 matching lines.

### Security interpretation

These results establish where network and protocol concepts appear in source, but they do not prove which services are running, which ports are reachable, which protocol versions are negotiated, whether TLS is enforced, whether ingress/egress controls are effective, or whether any specific trust boundary is secure.

Runtime behavior remains deliberately unverified and will be tested only in later controlled local-lab actions.

### Evidence

`docs/security/evidence/phase3-network-protocol-foundations-evidence.md`

### Completion criteria

- Static protocol candidates enumerated: PASS
- Network-control candidates enumerated: PASS
- Candidate configuration surfaces identified: PASS
- Source-vs-runtime distinction preserved: PASS
- No external active testing performed: PASS

## Action 3.3 - DNS, IP, Ports, Sockets, and Routing

Status: **COMPLETE**.

### Foundations

- **DNS** maps names to network destinations; security concerns include
  resolver trust, rebinding, spoofing, internal-name exposure, and SSRF
  destination changes.
- **IP addressing** describes network location and reachability. Loopback,
  private, public, wildcard, IPv4, and IPv6 addresses have different
  exposure implications.
- **Ports** identify transport endpoints, not applications by themselves.
  A configured port does not prove that a service is running.
- **Sockets** join an address, transport protocol and port into a
  communication endpoint.
- **Routing** determines where traffic travels between networks and trust
  boundaries.
- **Proxies** can terminate, forward, transform or authorize traffic and
  therefore frequently become security boundaries.

### Static observations

- dns: 1172 candidate files, 5955 matching lines.
- ipv4: 177 candidate files, 689 matching lines.
- ipv6: 625 candidate files, 4477 matching lines.
- localhost: 238 candidate files, 593 matching lines.
- wildcard_bind: 80 candidate files, 126 matching lines.
- port: 1131 candidate files, 6888 matching lines.
- socket: 85 candidate files, 273 matching lines.
- listen_bind: 183 candidate files, 613 matching lines.
- routing: 852 candidate files, 3379 matching lines.
- proxy: 375 candidate files, 1568 matching lines.

### Security interpretation

This action maps source-level addressing, name-resolution, port, socket,
routing and proxy surfaces. Static candidates must not be treated as proof
of actual runtime exposure.

Runtime listeners, DNS resolution, active routes, firewall policy and
reachability remain unverified.

### Evidence

`docs/security/evidence/phase3-dns-ip-port-socket-routing-evidence.md`

### Completion criteria

- DNS candidates enumerated: PASS
- IP-address candidates enumerated: PASS
- Port candidates enumerated: PASS
- Socket candidates enumerated: PASS
- Routing/proxy candidates enumerated: PASS
- No active network probing performed: PASS
- Source-vs-runtime distinction preserved: PASS

## Action 3.4 - HTTP, HTTPS, and TLS

Status: **COMPLETE**.

### Foundations

- HTTP uses request/response semantics.
- Requests contain methods, targets, headers and optionally bodies.
- Responses contain status codes, headers and optionally bodies.
- HTTPS is HTTP transported through TLS.
- TLS provides confidentiality and integrity when correctly configured.
- Certificate validation helps establish peer identity.
- Cookies, CORS, HSTS, redirects and forwarded headers are
  security-relevant controls.
- Reverse proxies and TLS termination points can form trust boundaries.

### Static observations

- http_url: 744 candidate files, 1574 matching lines.
- https_url: 867 candidate files, 7898 matching lines.
- http_methods: 3064 candidate files, 25980 matching lines.
- http_headers: 1071 candidate files, 4041 matching lines.
- cookies: 78 candidate files, 153 matching lines.
- cors: 19 candidate files, 29 matching lines.
- hsts: 1 candidate files, 1 matching lines.
- tls_ssl: 108 candidate files, 405 matching lines.
- certificate_trust: 55 candidate files, 192 matching lines.
- tls_verify_disabled: 6 candidate files, 12 matching lines.
- proxy_forwarding: 89 candidate files, 305 matching lines.
- redirects: 196 candidate files, 479 matching lines.

### Security interpretation

Static discovery does not prove runtime exposure, HTTPS enforcement,
TLS negotiation, certificate validity, cookie behavior, CORS policy,
HSTS enforcement or proxy-header trust.

TLS-verification-disable matches are review candidates only.

### Evidence

`docs/security/evidence/phase3-http-https-tls-evidence.md`

### Completion criteria

- HTTP candidates enumerated: PASS
- HTTPS candidates enumerated: PASS
- HTTP method/header candidates enumerated: PASS
- Cookie/CORS/HSTS candidates enumerated: PASS
- TLS/certificate candidates enumerated: PASS
- TLS-verification-disable candidates identified: PASS
- No active HTTP/TLS probing performed: PASS
- Source-vs-runtime distinction preserved: PASS

## Action 3.5 - Web Application Request/Response Lifecycle
Status: **COMPLETE**.
### Request/response lifecycle
1. A client constructs a request.
2. DNS and routing direct traffic.
3. A listener or reverse proxy may receive it.
4. Routing selects an application handler.
5. Middleware may inspect or transform the request.
6. Authentication establishes identity.
7. Authorization evaluates permission.
8. Input validation constrains attacker-controlled data.
9. Business logic performs the operation.
10. Databases or downstream services may be contacted.
11. Exceptional paths are handled.
12. Response data is serialized.
13. Status, headers, cookies and body return to the client.
Every transition can represent a security boundary.
### Static observations
- routes_endpoints: 2087 candidate files, 11650 matching lines.
- request: 1171 candidate files, 6983 matching lines.
- response: 1264 candidate files, 11680 matching lines.
- middleware: 62 candidate files, 220 matching lines.
- authentication: 617 candidate files, 2262 matching lines.
- authorization: 1117 candidate files, 5249 matching lines.
- validation: 1143 candidate files, 4170 matching lines.
- session_cookie: 1328 candidate files, 10892 matching lines.
- data_access: 1226 candidate files, 6039 matching lines.
- downstream_service: 2111 candidate files, 9897 matching lines.
- error_handling: 2550 candidate files, 16376 matching lines.
- serialization: 1321 candidate files, 7314 matching lines.

### Security interpretation
Static discovery does not prove:
- actual runtime execution order;
- universal middleware coverage;
- authentication before sensitive operations;
- correct authorization enforcement;
- complete input validation;
- tenant-safe data access;
- safe downstream service calls;
- secure error handling;
- secure response behavior.
Those properties require deeper controlled analysis.
### Evidence
`docs/security/evidence/phase3-web-request-response-lifecycle-evidence.md`
### Completion criteria
- Route/endpoint candidates mapped: PASS
- Request/response candidates mapped: PASS
- Middleware candidates mapped: PASS
- Authentication/authorization candidates mapped: PASS
- Validation candidates mapped: PASS
- Data/downstream candidates mapped: PASS
- Error/serialization candidates mapped: PASS
- Request lifecycle security model documented: PASS
- No active runtime testing performed: PASS
- Static-vs-runtime distinction preserved: PASS
## Action 3.6 - REST/API Architecture
Status: **COMPLETE**.
### Foundations
REST/API security requires reasoning about:
1. Resources and endpoint definitions.
2. HTTP methods and state changes.
3. Path identifiers and object references.
4. Query parameters.
5. Request bodies and schemas.
6. Response schemas.
7. Status and error behavior.
8. Content types and serialization.
9. Authentication.
10. Authorization.
11. Object ownership.
12. Tenant isolation.
13. Pagination.
14. Rate limiting.
15. Idempotency and replay.
16. API versioning.
17. OpenAPI/Swagger descriptions.
18. Webhooks and callbacks.
A valid API request is not automatically an authorized request.
A valid object identifier does not establish ownership or permission.
Authentication establishes identity. Authorization determines whether
that identity may perform the requested operation.
### Static observations
- routes: 807 candidate files, 2818 matching lines.
- http_methods: 2965 candidate files, 24656 matching lines.
- path_parameters: 3887 candidate files, 32785 matching lines.
- query_parameters: 307 candidate files, 1188 matching lines.
- request_schema: 1023 candidate files, 5497 matching lines.
- response_schema: 58 candidate files, 243 matching lines.
- versioning: 502 candidate files, 1704 matching lines.
- openapi_swagger: 104 candidate files, 578 matching lines.
- pagination: 535 candidate files, 2234 matching lines.
- status_errors: 1021 candidate files, 5486 matching lines.
- content_types: 311 candidate files, 707 matching lines.
- authentication: 1053 candidate files, 7018 matching lines.
- authorization: 1081 candidate files, 5030 matching lines.
- rate_limit: 193 candidate files, 504 matching lines.
- idempotency: 13 candidate files, 20 matching lines.
- webhook_callback: 20 candidate files, 39 matching lines.

### Security interpretation
Later controlled analysis must verify:
- route reachability;
- authentication requirements;
- function-level authorization;
- object-level authorization;
- tenant isolation;
- request validation;
- state-transition rules;
- pagination and resource limits;
- abuse/rate controls;
- replay and idempotency behavior;
- webhook trust boundaries;
- error behavior.
Static source discovery alone does not prove these controls.
### Evidence
`docs/security/evidence/phase3-rest-api-architecture-evidence.md`
### Completion criteria
- Routes and methods mapped: PASS
- Path/query parameter candidates mapped: PASS
- Request/response schemas mapped: PASS
- Status/content-type candidates mapped: PASS
- Versioning/API-documentation candidates mapped: PASS
- Authentication/authorization candidates mapped: PASS
- Pagination/rate-limit candidates mapped: PASS
- Idempotency candidates mapped: PASS
- Webhook/callback candidates mapped: PASS
- No active API testing performed: PASS
- Static-vs-runtime distinction preserved: PASS
## Action 3.7 - Authentication Foundations

Status: **COMPLETE**.

### Foundations

Authentication establishes or verifies **who or what is acting**.

Relevant mechanisms include:

1. Username/password authentication.
2. Password hashing.
3. API keys.
4. Bearer tokens.
5. JWT.
6. OAuth.
7. OpenID Connect.
8. SAML.
9. Sessions.
10. MFA and WebAuthn.
11. Token expiry.
12. Refresh tokens.
13. Password-reset flows.
14. Identity claims.
15. Authentication middleware.

Authentication is distinct from authorization. Successful
authentication does not automatically grant permission to a resource.

### Static observations

- login_logout: 299 candidate files, 1105 matching lines.
- password: 299 candidate files, 1158 matching lines.
- password_hashing: 3 candidate files, 81 matching lines.
- api_key: 512 candidate files, 3197 matching lines.
- bearer_token: 392 candidate files, 1276 matching lines.
- jwt: 54 candidate files, 185 matching lines.
- oauth: 363 candidate files, 2299 matching lines.
- oidc: 93 candidate files, 469 matching lines.
- saml: 69 candidate files, 240 matching lines.
- mfa: 3 candidate files, 11 matching lines.
- session_auth: 1356 candidate files, 13003 matching lines.
- auth_middleware: 246 candidate files, 664 matching lines.
- identity_claims: 307 candidate files, 1070 matching lines.
- token_expiry: 288 candidate files, 965 matching lines.
- refresh_token: 80 candidate files, 418 matching lines.
- password_reset: 29 candidate files, 68 matching lines.

### Security interpretation

Later controlled testing must verify credential validation, password
storage, enumeration resistance, brute-force protection, MFA, token
signature/issuer/audience/expiry validation, refresh-token handling,
session invalidation, logout/revocation and password-reset integrity.

Static source discovery alone does not prove those controls.

### Evidence

`docs/security/evidence/phase3-authentication-foundations-evidence.md`

### Completion criteria

- Authentication mechanisms mapped: PASS
- Password/password-hashing candidates mapped: PASS
- API-key/token candidates mapped: PASS
- OAuth/OIDC/SAML candidates mapped: PASS
- MFA/WebAuthn candidates mapped: PASS
- Sessions and identity claims mapped: PASS
- Expiry/refresh/reset candidates mapped: PASS
- No active authentication testing performed: PASS
- Static-vs-runtime distinction preserved: PASS

## Action 3.8 - Sessions, Cookies & Tokens

Status: **COMPLETE**.

### Review scope

Sessions, cookie security, CSRF, bearer/JWT/access/refresh tokens, expiry, rotation, revocation and browser storage.

### Static observations

- Candidate files: 2035
- Matching lines: 40287

### Security interpretation

Static discovery identifies review candidates only.
Runtime verification remains required.

### Evidence

`docs/security/evidence/phase3-session-cookie-token-evidence.md`

### Completion criteria

- Static mapping: PASS
- Evidence recorded: PASS
- No active runtime testing: PASS
- Static/runtime distinction: PASS

## Phase 3 Completion Gate

Phase 3 remains **IN PROGRESS**.
