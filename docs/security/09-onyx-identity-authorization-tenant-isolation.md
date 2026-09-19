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

## Action 9.6 - Agent, tool, action and delegated-authorization trace

Status: **COMPLETE**

Authorization continuity was traced from the authenticated user through agent/persona
access, tool attachment, per-turn tool narrowing, tool construction, delegated
credentials and final tool dispatch.

Confirmed source-backed patterns include:

- new chat sessions validate current agent/persona access;
- persona mutation uses owner/share/admin and scoped-manager authorization;
- disabled tools are skipped during runtime construction;
- `allowed_tool_ids` can narrow a turn's available tools;
- unknown model-requested tools are dropped by the runner;
- FileReaderTool accepts only server-authorized file IDs;
- custom OAuth and passthrough-auth paths use the acting user's credential context;
- newly attached MCP tools require access to the corresponding MCP server;
- MCP credential resolution distinguishes per-user, admin-shared and passthrough credentials and applies header precedence/denylisting.

Three follow-up hypotheses were identified:

`H9-14 — Foreign custom action attachment may delegate creator-stored credentials`

Custom action management has a creator/admin boundary, but the traced persona upsert
path does not show an equivalent authorization check for newly attached non-MCP custom
actions. Because custom actions may carry stored static headers, controlled runtime
verification must determine whether one user can attach and invoke another creator's
credential-bearing action. Tracking: GitHub Issue #3.

`H9-15 — Agent access revocation may not invalidate an existing chat-session capability`

New-session creation checks persona access, while the traced existing-session continuation
path reloads the owned session and its persona/tools without showing a fresh persona-share
check before tool construction. Tracking: GitHub Issue #4.

`H9-16 — Request-supplied MCP headers require explicit trust-policy verification`

The message request supports caller-provided `mcp_headers`, and MCP execution can use
additional headers in some no-managed-credential states. This may be intended delegated
authentication; runtime tests must prove it cannot exceed the configured MCP server policy.

None of these hypotheses is classified as a confirmed vulnerability by static analysis alone.

Evidence:

`docs/security/evidence/phase9-action-9.6-agent-tool-action-delegated-authorization-trace.md`

## Action 9.7 - Workload identity, service authentication and trust relationships

Status: **COMPLETE**

The workload-identity trace confirmed that service-account API keys map to synthetic
`SERVICE_ACCOUNT` users and inherit authorization through group membership. Key creation,
regeneration, group changes and deletion are coupled to service-account identity and
permission lifecycle, and multi-tenant key generation carries an explicit tenant signal.

Key source-backed properties include:

- service-account API-key administration is explicitly treated as a high-impact,
  admin-equivalent capability because group assignment can grant powerful permissions;
- clear API keys are generated with high entropy and stored by one-way hash plus masked display;
- key regeneration replaces the stored credential and recomputes effective permissions;
- key deletion removes both credential and synthetic principal;
- service-account requests resolve back to a concrete user principal for downstream authorization;
- no app-level SPIFFE/SPIRE or mTLS workload-identity implementation was established by this source trace, so infrastructure identity remains a deployment-layer verification item.

One runtime/policy hypothesis remains:

`H9-17 — Service-account interactive-session reachability`

`SERVICE_ACCOUNT` is classified as web-login-capable in source even though the account is
provisioned as a machine identity with a randomly generated, undisclosed password. Runtime
proof and product-policy confirmation are required before classification. Tracking:
GitHub Issue #5.

Evidence:

`docs/security/evidence/phase9-action-9.7-workload-identity-service-auth-trust-relationships.md`

`docs/security/evidence/phase9-action-9.7-runtime-test-pack.md`

## Action 9.8 - Secrets, API keys, credential delegation and cryptography assessment

Status: **COMPLETE**

Secret handling and cryptographic boundaries were traced across application-level
credential wrappers, API keys, PATs, OAuth/OIDC, MCP and JWT verification.

Confirmed source-backed controls include:

- `SensitiveValue` forces an explicit masked/raw decision and blocks common accidental
  string/JSON/Pydantic disclosure paths;
- API keys and PATs use high-entropy random generation and one-way SHA-256 lookup material;
- tool OAuth client secrets and user token sets use `EncryptedString` / `EncryptedJson`;
- OAuth token exchanges require HTTPS and pass through outbound SSRF controls;
- managed MCP credential headers take precedence over caller-supplied headers and denylisted
  header names such as `Host` are removed;
- external JWT verification pins the accepted algorithm to RS256 and applies configured
  audience/issuer constraints;
- the OIDC client performs issuer/config ownership validation and rejects present-but-unverified email claims.

Two additional boundaries require runtime/security-requirement validation:

`H9-18 — Credential-at-rest encryption integrity and fail-open behavior`

The base/MIT encryption path stores raw UTF-8 bytes. The EE override can encrypt using
AES-CBC with random IV and PKCS#7 padding when `ENCRYPTION_KEY_SECRET` is configured,
but falls back to raw bytes when it is absent. The traced CBC construction has no
cryptographic authentication tag/MAC and directly trims configured key bytes to an AES
key size. This is a cryptographic property, not yet a vulnerability classification.
Tracking: GitHub Issue #6.

`H9-19 — Login OAuth access/refresh tokens use ordinary Text storage`

Login-provider `OAuthAccount.access_token` and `refresh_token` fields are ordinary
`Text`, while tool-specific OAuth token sets and client credentials use encrypted
sensitive models. The runtime tool path can use the login access token for passthrough
authentication. The storage property is confirmed; risk classification still depends on
the deployment threat model, storage controls and explicit secret-at-rest requirements.
Tracking: GitHub Issue #7.

H9-16 remains carried forward for delegated MCP-header trust-policy verification.

Evidence:

`docs/security/evidence/phase9-action-9.8-secrets-api-keys-credential-delegation-cryptography.md`

## Action 9.9 - Authorization attack matrix and executable negative-test pack

Status: **COMPLETE**

The static hypotheses and baseline authorization controls are now converted into a bounded
runtime test design with explicit actors, expected ALLOW/DENY outcomes, evidence fields,
stop conditions and automatic PASS / FAIL / REVIEW / SKIP dispositions.

The pack includes:

- anonymous/protected-route controls;
- global-admin and scoped-manager controls;
- horizontal chat ownership checks;
- vertical administrator checks;
- PAT token-scope enforcement;
- H9-11 scoped `/manage/users` data filtering;
- H9-12 cross-user generated-image retrieval;
- H9-13 search ACL-bypass provenance;
- H9-14 foreign custom-action attachment/credential delegation;
- H9-15 agent-revocation behavior for new and existing sessions;
- H9-16 request-supplied MCP-header policy;
- service-account privilege reduction, rotation, deletion, disable and cross-tenant replay;
- H9-17 interactive service-account reachability;
- H9-18 credential-at-rest confidentiality/integrity checks;
- H9-19 login OAuth token-storage/lifecycle checks.

The executable runner fails closed outside loopback, requires `PHASE9_RUN=1`, caps timeout
and response size, runs sequentially, does not follow redirects, does not print credentials,
and records body length/SHA-256 rather than raw response bodies. `404` denials are REVIEW
rather than automatic PASS unless paired positive-control evidence establishes route/resource
validity.

Evidence and executable pack:

`docs/security/evidence/phase9-action-9.9-authorization-attack-matrix-negative-test-pack.md`

`scripts/security/phase9_negative_authz_runner.py`

Runtime execution is in progress in the authorized synthetic Onyx laboratory.

## Action 9.10 - Runtime cross-user, cross-role and cross-tenant verification

Status: **IN PROGRESS — H9-14 DATABASE RETEST PASSED; RUNTIME RETEST PENDING**

Repository-side execution tooling is prepared:

- `scripts/security/phase9_runtime_verify.sh` validates branch lineage, clean worktree,
  loopback-only target reachability, Python syntax, and produces immutable execution metadata;
- `scripts/security/phase9_negative_authz_runner.py` executes the bounded negative-test matrix;
- `scripts/security/phase9_results_to_markdown.py` converts runtime JSON into a sanitized
  PASS / FAIL / REVIEW / SKIP decision record without credentials or raw response bodies;
- the runtime runbook defines H9-11 through H9-19 proof requirements and the completion gate.

Completed runtime slices confirmed H9-11 and H9-12. A transactional H9-14 test also
confirmed that Bob could attach Alice's custom action at the business-logic layer.

The H9-14 test made no HTTP request. It did not transmit a stored header. It rolled back
all synthetic objects and verified cleanup.

The security-hardened fork now requires creator or actions-administrator authority for
new custom-action attachments. Existing attachments remain during ordinary agent edits.

The focused database regression suite passed all five authorization cases at runtime
HEAD `7496d92599f26d2e2050643832ef091aa6025493`. Each case used an outer transaction
that rolled back at teardown.

Action 9.10 remains incomplete until the authorized local laboratory rebuilds the patched
API service and verifies the API-level denial.

Evidence/runbook:

`docs/security/evidence/phase9-action-9.10-runtime-verification-runbook.md`

`docs/security/evidence/phase9-action-9.10-runtime-slice6-h14.md`

`docs/security/evidence/phase9-action-9.11-h14-remediation.md`

`docs/security/evidence/phase9-action-9.11-h14-database-retest.md`

## Current completion

Phase 9: **64.3%**

Full final project: **approximately 38.8%**

Next focused action in the authorized lab:

Rebuild the API service from the patched branch. Then rerun the bounded H9-14 attachment
test. The expected result is denial with no persistent database change.
