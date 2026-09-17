# Phase 9 - Onyx Identity, Authorization and Tenant Isolation

Phase 9 status: **IN PROGRESS**

## Objective

Verify identity, authentication, session, token, authorization, tenant-isolation,
workload-identity, credential, secret and cryptographic controls in the authorized
Onyx laboratory using synthetic identities and data.

## Immutable handoff

Phase 8 closure commit:

`1dd9a2c89228e9b3bd88ca2e32ae41c27fde907e`

Phase 8 decision:

**COMPLETE**

## Rules

- authorized Onyx laboratory only;
- synthetic users, tenants, documents, credentials and tokens only;
- no public Onyx deployment testing;
- no real production data or credentials;
- preserve explicit expected ALLOW/DENY outcomes;
- distinguish static observations from runtime verification;
- do not claim a vulnerability without reproducible evidence;
- use bounded requests, time, concurrency and resources;
- stop on unexpected external calls, real data, real credentials or scope uncertainty.

## Phase 9 security objectives

1. Authentication cannot be bypassed.
2. Sessions and tokens are issued, validated and revoked correctly.
3. Horizontal privilege escalation is prevented.
4. Vertical privilege escalation is prevented.
5. Cross-tenant access is prevented.
6. Object ownership and resource authorization are enforced.
7. Document, index, vector, memory, agent, tool and action authorization are assessed when applicable.
8. Delegated and service identities use least privilege.
9. Secrets and API keys remain isolated.
10. Cryptographic protections are correctly configured for the assessed deployment.
11. Authorization failures are observable and regression-testable.

## Accelerated action plan

- Action 9.1 - Engagement initialization and immutable handoff
- Action 9.2 - Identity, role, tenant and privilege architecture map
- Action 9.3 - Authentication, session and token lifecycle trace
- Action 9.4 - Authorization-policy and ownership-control trace
- Action 9.5 - Tenant, document, index, vector and memory authorization trace
- Action 9.6 - Agent, tool, action and delegated-authorization trace
- Action 9.7 - Workload identity, service authentication and trust relationships
- Action 9.8 - Secrets, API keys, credential delegation and cryptography assessment
- Action 9.9 - Authorization attack matrix and executable negative-test pack
- Action 9.10 - Runtime cross-user, cross-role and cross-tenant verification
- Action 9.11 - Finding validation, root cause and remediation
- Action 9.12 - Regression testing and security-effectiveness measurement
- Action 9.13 - Keycloak/OpenFGA/supporting-control transfer assessment
- Action 9.14 - Residual risk, assurance evidence and final completion gate

## Action 9.1 - Engagement initialization and immutable handoff

Status: **COMPLETE**

Evidence:

`docs/security/evidence/phase9-action-9.1-engagement-initialization.md`

## Action 9.2 - Identity, role, tenant and privilege architecture map

Status: **COMPLETE**

The assessed source was used to reconstruct the principal account classes,
authentication paths, permission-authority model, scoped-manager gates, session
token lifecycle, API-key/PAT/JWT paths, tenant signals and document/file ACL
boundaries.

Key source-backed architecture includes:

- `STANDARD`, `SERVICE_ACCOUNT`, `BOT`, `EXT_PERM_USER` and `ANONYMOUS` account classes;
- group-based permissions with `GLOBAL`, `SCOPED` and `NONE` authority;
- explicit GATE 1 route admission plus mandatory GATE 2 resource scoping for scoped managers;
- Redis-backed session values carrying subject, tenant, issuance, expiry and logout state;
- separate API-key, PAT and JWT credential paths;
- multi-tenant token structures carrying tenant information where applicable;
- ownership, sharing and document-ACL authorization paths.

No vulnerability is claimed from static architecture evidence alone.

Evidence:

`docs/security/evidence/phase9-action-9.2-identity-role-tenant-privilege-map.md`

## Action 9.3 - Authentication, session and token lifecycle trace

Status: **COMPLETE**

The authentication lifecycle was traced across browser sessions, mobile bearer
sessions, externally verified JWTs, PATs, API keys and OAuth/OIDC-linked identities.

Key source-backed lifecycle properties include:

- configurable Redis, PostgreSQL or single-tenant JWT primary session strategies;
- a mobile Bearer backend reusing the selected primary session strategy;
- Redis sessions with subject, tenant, issue time, logical expiry and logout tombstone state;
- Redis rejection classification for expired, terminated, missing and malformed sessions;
- PAT authentication with explicit token-scope capping of user permissions;
- API-key authentication with a separate credential-resolution path;
- external JWT signature validation restricted to RS256 with optional audience and issuer enforcement;
- additional post-authentication verification and OIDC-expiry checks;
- stateless JWT logout behavior where an issued JWT cannot be server-side invalidated and remains valid until natural expiry.

The stateless JWT revocation characteristic is recorded for explicit runtime and
residual-risk verification and is not classified as a vulnerability by static
analysis alone.

Evidence:

`docs/security/evidence/phase9-action-9.3-authentication-session-token-lifecycle-trace.md`

## Action 9.4 - Authorization-policy and ownership-control trace

Status: **COMPLETE**

The authorization chain was traced from effective permissions through GLOBAL / SCOPED /
NONE authority, PAT scope capping, GATE 1 route admission, GATE 2 managed-resource
scoping, and resource-specific owner/ACL/sharing checks.

Confirmed source-backed patterns include:

- owner-bound chat reads, updates and deletes using authenticated user IDs;
- explicit public-shared chat handling;
- full-admin gating for high-impact user administration;
- scoped connector management with resource-level GATE 2 controls;
- read-side managed-scope SQL primitives for scoped-manager resources.

A high-priority static hypothesis was also identified:

`H9-11 — Scoped manager may receive user rows outside managed groups`

`GET /manage/users` uses `READ_USERS` with `allow_scope=True`, while the traced route
body does not show an explicit managed-group GATE 2 filter before serializing users.
This is queued for controlled runtime verification and is **not** classified as a
vulnerability by static analysis alone.

Evidence:

`docs/security/evidence/phase9-action-9.4-authorization-policy-ownership-control-trace.md`

## Action 9.5 - Tenant, document, index, vector and memory authorization trace

Status: **COMPLETE**

Authorization continuity was traced across the tenant context, PostgreSQL schema,
document/user-file ACL construction, search filters, vector/index queries and user
memory persistence.

Confirmed source-backed patterns include:

- multi-tenant request context failing closed when tenant context is absent;
- tenant-aware SQL sessions using schema translation;
- document-index `TenantState` derived from the current tenant;
- search `IndexFilters` carrying both tenant and requesting-user ACL information;
- OpenSearch applying tenant and ACL filters as ANDed authorization predicates;
- least-permissive document access when ACL metadata is missing;
- connector-file reads mirroring document retrieval ACLs;
- user memories read and mutated using the authenticated user's ID.

Two follow-up hypotheses were identified:

`H9-12 — Generated chat image cross-user authorization exception`

`CHAT_IMAGE_GEN` file records are deliberately accepted by `user_can_access_chat_file`
without owner/chat/document ACL resolution. Cross-user and cross-tenant runtime tests
are required before classification.

`H9-13 — Search ACL-bypass caller provenance`

`ChunkSearchRequest` and `SearchTool` contain an explicit `bypass_acl` mode. The mode
may be legitimate for trusted system flows, but Phase 9 must prove that no public,
agent-controlled or delegated untrusted path can cause it to become true.

Neither hypothesis is classified as a confirmed vulnerability by static analysis alone.

Evidence:

`docs/security/evidence/phase9-action-9.5-tenant-document-index-vector-memory-authorization-trace.md`

## Current completion

Phase 9: **35.7%**

Full final project: **approximately 37.6%**

Next:

**Action 9.6 - Agent, tool, action and delegated-authorization trace**
