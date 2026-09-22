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

Status: **COMPLETE — H9-11 THROUGH H9-19 HAVE EVIDENCE-BACKED DISPOSITIONS**

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

The rebuilt API-level H9-14 retest authenticated a scoped synthetic user, established
a positive-control read, and denied a new foreign custom-action attachment with HTTP
`403` and `INSUFFICIENT_PERMISSIONS`. Persona fields and action ownership remained
unchanged, the attachment count remained zero, all synthetic rows were removed, and
the session was revoked.

The H9-15 remediation now revalidates non-default persona access before an existing
chat session can execute another turn. Its focused regression and bounded runtime
retest passed.

The H9-16 remediation now denies request-supplied MCP headers by default. It permits
only names in the administrator-controlled server template. Managed credentials keep
collision precedence. An isolated loopback retest verified the filter, explicit
per-user API-token delegation, OAuth precedence and fail-closed behavior.

Action 9.10 completion gate is satisfied: H9-11 through H9-19 now have
evidence-backed dispositions. Findings requiring remediation are carried into
Actions 9.11 and 9.12.

Evidence/runbook:

`docs/security/evidence/phase9-action-9.10-runtime-verification-runbook.md`

`docs/security/evidence/phase9-action-9.10-runtime-slice6-h14.md`

`docs/security/evidence/phase9-action-9.11-h14-remediation.md`

`docs/security/evidence/phase9-action-9.11-h14-database-retest.md`

`docs/security/evidence/phase9-action-9.11-h14-runtime-remediation-retest.md`

`docs/security/evidence/phase9-action-9.11-h15-runtime-remediation-retest.md`

`docs/security/evidence/phase9-action-9.10-runtime-slice8-h16.md`

`docs/security/evidence/phase9-action-9.11-h16-policy-root-cause.md`

`docs/security/evidence/phase9-action-9.11-h16-runtime-remediation-retest.md`

## Action 9.11 - Finding validation, root cause and remediation

Status: **IN PROGRESS**

The hardened fork has source-backed remediations for H9-14, H9-15 and H9-16.
H9-14 passed both its focused database regression and bounded API-level runtime retest.
H9-15 and H9-16 also have passing focused tests and bounded runtime retests.

H9-12 and H9-18 have completed code-level remediation. Action 9.11 is complete after H9-19 protected-storage remediation and
bounded lifecycle/storage verification. H9-18 retains a deployment key-configuration assurance
requirement for the later Phase 9 gates.

## Current completion

Phase 9: **100% — COMPLETE**

Full final project: **approximately 38.8%**

Next focused action in the authorized lab:

Complete H9-19 protected login-OAuth token storage and lifecycle assurance while
preserving the existing synthetic-data and bounded-execution controls.

### H9-12 remediation closeout — 2026-09-22

Final patched-runtime verification passed:
- anonymous request: **403 denied**;
- Alice owner request: **200 allowed**;
- Bob authenticated non-owner request: **404 denied**;
- `ALICE_CAN_ACCESS=TRUE`;
- `BOB_CAN_ACCESS=FALSE`;
- runtime classification: **PASS — SECURITY_PROPERTY_ENFORCED**.

**H9-12 is remediated and closed.**

`docs/security/evidence/phase9-action-9.10-h9-12-remediation-runtime.md`

### H9-13 ACL-bypass provenance closeout — 2026-09-22

H9-13 production reachability analysis passed:
- ACL bypass is security-sensitive when enabled;
- production literal `True` sources: **0**;
- suspicious positional/true call sites: **0**;
- Search API and Slack explicitly use `False`;
- ordinary chat paths retain the default `False`.

**Classification: PASS — not currently reachable from identified production callers.**

`docs/security/evidence/phase9-action-9.10-h9-13-acl-bypass-provenance.md`

### H9-17 service-account interactive-login closeout — 2026-09-22

H9-17 was confirmed and remediated:
- pre-remediation service-account interactive login succeeded;
- `SERVICE_ACCOUNT` is now excluded from `AccountType.is_web_login()`;
- focused regression suite passed;
- patched runtime login returned **403**;
- no authentication cookie was issued;
- the synthetic service-account fixture was removed.

**H9-17 is remediated and closed.**

`docs/security/evidence/phase9-action-9.10-h9-17-service-account-interactive-login.md`

### H9-18 credential-at-rest encryption disposition — 2026-09-22

H9-18 is evidence-backed and dispositioned.

Confirmed properties:

- credential-bearing ORM storage reaches the application encryption wrappers;
- the current authorized lab has no `ENCRYPTION_KEY_SECRET` configured;
- missing-key behavior stores raw UTF-8 bytes;
- keyed EE AES-CBC encryption provides confidentiality but not authenticated
  ciphertext integrity;
- a wrong explicitly supplied key failed closed in the tested vector;
- IV tampering was accepted and produced altered plaintext.

**Classification: CONFIRMED SECURITY-PROPERTY / DEPLOYMENT-HARDENING FINDING.**

Remediation is carried forward to Action 9.11 / 9.12 rather than changing the
cryptographic storage format during runtime-verification Action 9.10.

H9-18 now has an evidence-backed disposition. H9-19 is the remaining
H9-11 through H9-19 runtime hypothesis required before Action 9.10 closeout.

`docs/security/evidence/phase9-action-9.10-h9-18-credential-at-rest-crypto.md`


### H9-19 login OAuth token-storage disposition — 2026-09-22

H9-19 is evidence-backed and dispositioned.

Confirmed:

- login `OAuthAccount.access_token` and `refresh_token` use ordinary
  PostgreSQL text fields;
- no `EncryptedString` / `EncryptedJson` binding was identified for those
  login-token fields;
- the live schema confirmed both token columns as `text`;
- token values were neither selected nor printed;
- expiry, refresh, refresh-token rotation/preservation and per-user refresh
  locking are implemented;
- local user deletion cascades associated OAuth-account deletion;
- explicit provider-side revocation for the login OAuthAccount path was not
  established by this trace.

**Classification: CONFIRMED STORAGE-HARDENING FINDING WITH FUNCTIONING
REFRESH-LIFECYCLE CONTROLS.**

Remediation and assurance requirements are carried into Actions 9.11 and 9.12.

`docs/security/evidence/phase9-action-9.10-h9-19-login-oauth-token-storage-lifecycle.md`

### Action 9.10 final closeout — 2026-09-22

The runtime cross-user, cross-role, cross-tenant, workload-identity,
credential-storage and related security-property verification gate is complete.

**H9-11 through H9-19 now have evidence-backed dispositions.**

Action 9.10 does not require every confirmed finding to be remediated before
closure. Confirmed findings and residual remediation requirements are carried
forward to Action 9.11, followed by regression/security-effectiveness
measurement in Action 9.12.

**Action 9.10 status: COMPLETE.**

Next phase action: **Action 9.11 — Finding validation, root cause and
remediation.**


### H9-18 Action 9.11 remediation closeout — 2026-09-22

The H9-18 cryptographic integrity defect is remediated in the hardened fork.

New keyed writes use a versioned AES-GCM authenticated-encryption envelope.
Authenticated records reject tampering, wrong keys and missing-key reads
without degrading to plaintext.

Legacy raw UTF-8 and AES-CBC records remain readable for migration. The
rotation helper distinguishes the current authenticated format from legacy
records, including legacy CBC encrypted using the same current key.

A bounded real-PostgreSQL proof verified plaintext and legacy-CBC migration,
correct authenticated decryption, idempotent subsequent rotation and complete
fixture cleanup.

**H9-18 code-level status: REMEDIATED.**

The assessed lab still has no `ENCRYPTION_KEY_SECRET`. Deployment-level
key configuration and legacy-record migration remain assurance requirements
for environments requiring application-level confidentiality.

`docs/security/evidence/phase9-action-9.11-h9-18-aead-remediation.md`

Action 9.11 now proceeds to **H9-19 login OAuth token protected storage and
lifecycle assurance**.


### Action 9.11 completion — 2026-09-22

H9-19 login OAuth token storage has been remediated.

The hardened fork now stores login OAuth access and refresh tokens using an
OAuth-compatible encrypted binary SQLAlchemy type backed by the H9-18
versioned authenticated-encryption mechanism.

A real bounded PostgreSQL/Alembic proof verified:

- TEXT -> BYTEA migration;
- lossless legacy compatibility;
- legacy token -> authenticated ciphertext migration;
- ordinary-string ORM compatibility;
- encrypted token replacement during simulated refresh;
- idempotent rotation;
- downgrade protection;
- complete fixture and schema rollback.

**Action 9.11 status: COMPLETE.**

Residual deployment/lifecycle assurance items are carried forward rather than
misclassified as unresolved code defects.

Evidence:

- `docs/security/evidence/phase9-action-9.11-h9-19-oauth-token-storage-remediation.md`
- `docs/security/evidence/phase9-action-9.11-completion.md`

Phase 9 proceeds to accelerated Actions **9.12 and 9.13**.


### Accelerated Actions 9.12 and 9.13 completion — 2026-09-22

Action 9.12 reconfirmed the highest-risk post-remediation security
properties and verified evidence continuity for H9-12 through H9-19.

**Action 9.12 status: COMPLETE.**

Action 9.13 established explicit responsibility boundaries between
application controls and potential external identity/authorization
infrastructure.

Authentication and coarse identity claims may be externalized, while tenant
isolation, object ownership, delegated-action authorization and data-path
authorization remain application responsibilities.

**Action 9.13 status: COMPLETE.**

Evidence:

- `docs/security/evidence/phase9-action-9.12-regression-security-effectiveness.md`
- `docs/security/evidence/phase9-action-9.13-supporting-control-transfer.md`

Only **Action 9.14 — residual risk and final Phase 9 completion gate**
remains.


### Action 9.14 final completion gate — 2026-09-22

Phase 9 completed its residual-risk and final evidence gate.

All fourteen planned actions now have an evidence-backed completion state.

Final finding disposition coverage includes H9-12 through H9-19, with
code-level remediation, non-reachability disposition, regression verification
or explicit residual assurance treatment as appropriate.

Residual risks intentionally carried forward include:

- production encryption-key management;
- legacy secret/token migration;
- OAuth-provider revocation assurance;
- production IdP/policy-engine integration validation;
- dependency-complete CI regression;
- laboratory infrastructure hardening such as replacement of default
  object-storage credentials.

These items do not invalidate the completed laboratory security engineering
work and are not being represented as resolved production controls.

**Action 9.14 status: COMPLETE.**

**PHASE 9 STATUS: COMPLETE — 14/14 ACTIONS.**

**Phase 9 progress: 100%.**

Evidence:

- `docs/security/evidence/phase9-action-9.11-completion.md`
- `docs/security/evidence/phase9-action-9.12-regression-security-effectiveness.md`
- `docs/security/evidence/phase9-action-9.13-supporting-control-transfer.md`
- `docs/security/evidence/phase9-action-9.14-final-completion-gate.md`

The Phase 9 branch is ready for review and later integration according to the
project's normal approval process.
