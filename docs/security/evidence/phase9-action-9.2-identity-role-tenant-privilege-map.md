# Phase 9 — Action 9.2 Identity, Role, Tenant and Privilege Architecture Map

## Status

**COMPLETE — STATIC ARCHITECTURE RECONNAISSANCE**

This artifact records source-backed architecture and attack hypotheses only.
It does **not** claim runtime enforcement or a vulnerability.

## Assessment branch

`security/phase-9-identity-authorization-tenant-isolation`

## Starting handoff

Phase 8 closure:

`1dd9a2c89228e9b3bd88ca2e32ae41c27fde907e`

## Objective

Reconstruct the principal identity, credential, permission, tenant, ownership,
and privilege boundaries that Phase 9 must verify at runtime.

---

## 1. Identity and account classes

Source:

`backend/onyx/db/enums.py`

Observed account types:

- `STANDARD`
- `BOT`
- `EXT_PERM_USER`
- `SERVICE_ACCOUNT`
- `ANONYMOUS`

The source explicitly documents that `STANDARD` and `SERVICE_ACCOUNT`
participate in the group-based permission system while `BOT`, `EXT_PERM_USER`
and `ANONYMOUS` have fixed behavior.

Security consequence for Phase 9:

The runtime matrix must not treat every authenticated identity as equivalent.
Interactive users, service identities, external-permission identities, bots and
anonymous identities require distinct expected authorization behavior.

---

## 2. Primary authentication module

Source directory:

`backend/onyx/auth/`

Security-relevant modules observed include:

- `users.py`
- `session_tokens.py`
- `api_key.py`
- `pat.py`
- `jwt.py`
- `oidc_client.py`
- `oauth_refresher.py`
- `oauth_token_manager.py`
- `mobile_sso/`
- `sso_tenant_token.py`
- `permissions.py`
- `permission_projection.py`
- `scoped_permissions.py`

This establishes multiple authentication and identity paths rather than one
single session mechanism.

---

## 3. Interactive-user resolution boundary

Source:

`backend/onyx/auth/users.py`

Observed architecture:

- FastAPI Users is used for user authentication infrastructure.
- Cookie, bearer, JWT, Redis and database strategy primitives are imported.
- `optional_fastapi_current_user` resolves an active user optionally.
- `double_check_user(...)` is used as an additional application-layer check.
- `current_user(...)` invokes `double_check_user(...)` and rejects a limited
  user for ordinary protected access.
- `current_chat_accessible_user(...)` has a separate path that can admit the
  anonymous user when anonymous access is enabled.
- current user and current tenant context variables are imported and used.
- WebSocket authentication has a separate dependency path and applies user
  checks after token resolution.

Static security interpretation:

There are multiple identity-entry paths that must converge on equivalent
security properties where intended. Phase 9 must therefore test HTTP,
anonymous-chat, token and WebSocket identity resolution independently rather
than assuming one successful path proves the others.

---

## 4. Authentication cannot be globally disabled in the observed configuration path

Source:

`backend/onyx/auth/users.py`

Observed behavior:

`verify_auth_setting()` logs that `AUTH_TYPE='disabled'` is no longer supported
and states that authentication is always enabled.

The same startup path also checks `USER_AUTH_SECRET`. A real deployment with an
empty secret is rejected; development/integration-test modes downgrade this to
a warning.

The source states that this secret protects password-reset and
email-verification tokens, OAuth state and captcha cookies.

Runtime verification required:

- prove the active Phase 9 runtime is not using a development-only insecure
  secret configuration;
- prove authentication is actually required on protected routes;
- verify token-signing and state-management behavior rather than inferring it
  from startup code.

---

## 5. Permission model

Source:

`backend/onyx/auth/permissions.py`

Observed design:

- permissions are stored as grants and expanded through implied permissions;
- `FULL_ADMIN_PANEL_ACCESS` short-circuits to all permissions;
- Community Edition can auto-grant explicitly defined ungated capabilities;
- anonymous users are excluded from the Community Edition auto-grant path;
- permission authority is classified as `GLOBAL`, `SCOPED`, or `NONE`;
- `has_global_permission(...)` distinguishes unrestricted authority;
- `require_permission(...)` is a FastAPI dependency factory;
- request token scopes can cap user permissions;
- a token does not elevate a user merely because the token contains a scope;
- `allow_scope=True` admits a scoped manager to the handler but does not by
  itself authorize the target resource.

Important code contract:

The source explicitly describes `allow_scope=True` as **GATE 1** only. Handlers
using it must apply a **GATE 2** resource-scope check or they could expose an
unrestricted resource set to a scoped manager.

This is an attack hypothesis and review requirement, **not a confirmed defect**.

---

## 6. Scoped-manager authorization boundary

Source:

`backend/onyx/auth/scoped_permissions.py`

Observed design:

- `get_scoped_groups(...)` resolves groups managed by the user;
- `within_scope(...)` allows global authority immediately;
- scoped authority passes only when the target is non-public and the final
  current/requested groups are a non-empty subset of managed groups;
- `assert_within_scope(...)` raises insufficient-permission on failure;
- `assert_manages_group(...)` protects single-group operations;
- `assert_global(...)` provides a global-only gate for operations such as
  deletes that must not be available to scoped managers;
- denial paths emit audit events.

Critical Phase 9 test question:

For every route that uses the scoped-manager admission mechanism, determine
whether the matching resource-level GATE 2 check executes before state change or
sensitive data return.

---

## 7. Session-token lifecycle

Source:

`backend/onyx/auth/session_tokens.py`

Observed session value fields:

- `sub`
- `tenant_id`
- `issued_at`
- `expires_at`
- `logged_out_at`

Observed rejection classes:

- `EXPIRED`
- `TERMINATED`
- `NOT_FOUND`
- `MALFORMED`

Observed lifecycle properties:

- logical expiration is embedded in the stored token value;
- the physical Redis TTL can include a grace period;
- logout writes a tombstone instead of simply deleting the value;
- a logged-out token is classified as terminated;
- malformed and missing session entries are rejected;
- pre-upgrade session values receive compatibility handling;
- session tokens are distinguished from API keys, PATs and JWTs on shared
  bearer transport.

Tenant-security relevance:

`tenant_id` is embedded in the session-token value. Runtime testing must verify
that a session cannot be replayed or rebound across an unauthorized tenant and
that logout/revocation behavior remains tenant-correct.

---

## 8. API-key identity path

Source:

`backend/onyx/auth/api_key.py`

Observed behavior:

- API keys are generated using cryptographically random material;
- in multi-tenant mode, a tenant identifier can be encoded into the token
  structure before the random secret;
- current-format API keys are hashed using SHA-256 for lookup/storage handling;
- a deprecated API-key format has a compatibility hash path;
- display values are masked;
- both `Bearer <key>` and the historical raw-key format are accepted by the
  extraction function.

Phase 9 verification requirements:

- cross-tenant API-key use;
- disabled/deleted key behavior;
- service-account key scope;
- raw-versus-Bearer parsing equivalence;
- key-to-user/service identity binding;
- token permission cap behavior.

---

## 9. Personal Access Token path

Source:

`backend/onyx/auth/pat.py`

Observed behavior:

- PATs use cryptographically random values;
- multi-tenant PATs can carry an encoded tenant identifier;
- PAT lookup uses SHA-256 hashing;
- PATs require `Bearer` transport rather than accepting the API-key raw format;
- PATs may have an expiration or no expiration depending on creation options.

Phase 9 verification requirements:

- tenant binding;
- permission/scope binding;
- expiration enforcement;
- revocation;
- user disablement interaction;
- privilege changes after token creation.

---

## 10. JWT verification path

Source:

`backend/onyx/auth/jwt.py`

Observed behavior:

- JWT verification material can be loaded from JWKS or PEM;
- only `RS256` is accepted in the inspected decoder call;
- configured audience is supplied to JWT decoding;
- issuer is supplied to JWT decoding;
- audience verification is enabled when an expected audience is configured;
- issuer/audience/required-claim failures return rejection;
- dynamic public-key URLs are subjected to SSO URL validation and SSRF-safe
  fetching logic unless operator-pinned configuration is used;
- HTTPS is required on the protected dynamic-fetch path.

Phase 9 must distinguish configuration capability from actual runtime settings.
A secure verification implementation does not prove that audience/issuer values
are configured in the active laboratory.

---

## 11. Document and retrieval ACL boundary

Sources:

- `backend/onyx/access/access.py`
- `backend/onyx/access/models.py`

Observed behavior in `access.py`:

- anonymous users receive only the public-document ACL pattern in the inspected
  base implementation;
- ordinary users receive ACL identities derived from current/prior email plus
  public access;
- document access defaults to a least-permissive null access object when access
  information does not yet exist;
- user-file access considers ownership and sharing relationships;
- chat-file access checks multiple asset classes;
- owned files can be admitted;
- persona-associated files may be accessible when the persona is public, owned,
  or directly shared;
- chat-message files can be accessible when the chat session belongs to the
  user or is publicly shared;
- connector-backed file access eventually delegates to document ACL logic.

Notable explicit TODO:

The inspected code currently treats `CHAT_IMAGE_GEN` file records as accessible
because the bytes are stored before the linking tool-call row is written. This
is recorded as a source observation and future attack surface; no unauthorized
runtime access is claimed by this Phase 9 action.

---

## 12. Tenant boundary model

Source-backed tenant signals identified during this action include:

- tenant context variables in `users.py`;
- tenant-specific synchronous/async database-session helpers imported by the
  authentication module;
- `tenant_id` in session token values;
- tenant information encoded into API keys and PATs in multi-tenant mode;
- tenant-aware email/member validation paths;
- tenant-specific database migration structure under `backend/alembic_tenants`.

Phase 8 already proved that request-controlled tenant/schema selection is a
security-sensitive trust boundary. Phase 9 therefore treats tenant identity,
session tenant context, token tenant hints and database tenant selection as
separate values that must not become attacker-interchangeable.

---

## 13. Reconstructed security decision flow

```text
credential / session / SSO / JWT / PAT / API key
                     |
                     v
             identity resolution
                     |
                     +--> account type
                     +--> active/limited/anonymous state
                     +--> tenant context
                     |
                     v
              permission resolution
                     |
             +-------+-------+
             |               |
           GLOBAL          SCOPED
             |               |
             |           GATE 1 reach
             |               |
             |           GATE 2 resource scope
             |               |
             +-------+-------+
                     |
                     v
          ownership / ACL / resource rule
                     |
                     v
     document / connector / agent / action / data
```

---

## 14. Phase 9 attack hypotheses produced by Action 9.2

### H9-AUTH-01 — identity-path divergence

Different authentication mechanisms may not enforce identical user-state,
tenant-state or permission requirements.

### H9-AUTHZ-02 — scoped-manager GATE 2 omission

A route may use `allow_scope=True` but fail to apply the mandatory resource
scope gate.

### H9-AUTHZ-03 — admin-override overreach

A route may rely on an overly broad administrative permission instead of a
narrow operation-specific token, or expose behavior inconsistent with the
intended permission registry.

### H9-TENANT-04 — token/session tenant confusion

Tenant identity derived from session, API key, PAT, request context or database
session may diverge or be rebound incorrectly.

### H9-TOKEN-05 — stale token authority

Logout, expiry, user disablement, permission reduction or key revocation may
not immediately remove effective authority on every authentication path.

### H9-ACL-06 — resource authorization divergence

Ownership, sharing, persona ACL, chat ACL and connector-document ACL paths may
produce inconsistent decisions for the same underlying file/document.

### H9-WS-07 — WebSocket/HTTP policy divergence

WebSocket identity resolution may differ from normal HTTP access behavior.

### H9-ANON-08 — anonymous surface expansion

Anonymous-chat access may reach capabilities beyond the intended public/chat
surface.

These hypotheses require runtime or route-specific source tracing before any
finding can be confirmed.

---

## 15. Evidence-backed priority order for the next actions

1. Resolve `current_user`, `optional_user`, anonymous and credential resolution
   paths.
2. Trace session creation, refresh, logout and tombstone behavior.
3. Trace PAT/API-key/JWT resolution into a concrete `User` plus token scopes.
4. Enumerate every `require_permission(...)` route and identify GLOBAL versus
   `allow_scope=True` entry conditions.
5. For scoped routes, prove the matching GATE 2 resource check.
6. Map tenant context from credential to database session.
7. Build owner/non-owner/cross-tenant/low-privilege runtime fixtures.

---

## Result

**PASS — identity, role, tenant and privilege architecture reconstructed from the assessed source.**

No Phase 9 vulnerability is claimed by Action 9.2.

Next:

**Action 9.3 — Authentication, session and token lifecycle trace.**
