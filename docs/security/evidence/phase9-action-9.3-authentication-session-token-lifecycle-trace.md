# Phase 9 — Action 9.3 Authentication, Session and Token Lifecycle Trace

## Status

**STATIC TRACE COMPLETE**

Runtime effectiveness is not inferred from this artifact.

## Objective

Trace each supported authentication/credential path from credential presentation through validation, user resolution, tenant/session context, refresh, expiry, logout/revocation behavior, and downstream permission enforcement.

## Source-backed authentication surfaces

### 1. Browser session authentication

Onyx selects the primary browser authentication strategy from `AUTH_BACKEND`:

- Redis-backed stateful sessions;
- PostgreSQL-backed stateful access tokens;
- single-tenant JWT sessions.

The browser transport is cookie-based.

### 2. Mobile bearer authentication

The mobile authentication backend uses the same strategy as the configured browser backend but exposes the credential as a Bearer token. This means browser and mobile transports can share the same underlying session/token semantics.

### 3. Externally verified JWT bearer authentication

When a JWT verification public-key URL is configured, `optional_user` can resolve a Bearer JWT independently of the primary fastapi-users session backend.

Observed verification controls include:

- RS256 algorithm restriction;
- public-key/JWKS retrieval;
- optional configured audience enforcement;
- optional configured issuer enforcement;
- HTTPS/SSRF-safe public-key retrieval for DB-origin configuration;
- JWT-to-user resolution.

### 4. Personal Access Tokens (PATs)

PATs:

- use a dedicated prefix;
- require Bearer transport;
- are SHA-256 hashed before lookup;
- may encode a tenant identifier in multi-tenant mode;
- resolve to a user;
- expose token scopes in `request.state.token_scopes`.

The permission layer then caps the user’s effective authority by the PAT scopes.

### 5. API keys

API keys:

- use a dedicated prefix;
- may be presented as Bearer or in the historical raw format;
- are hashed before lookup;
- may encode a tenant identifier in multi-tenant mode;
- resolve to a user/service identity through the database lookup path.

### 6. OAuth/OIDC/SSO-linked identities

The authentication path contains OAuth/OIDC identity association and refresh logic. Near-expiry OAuth access tokens are refreshed best-effort. `double_check_user` rejects a user whose stored OIDC expiry is past unless an explicit include-expired flow is used.

## Redis session lifecycle

### Issuance

`TenantAwareRedisStrategy.write_token` generates a random session token and stores a structured value containing:

- `sub` / user ID;
- tenant ID;
- issued-at timestamp;
- logical expiry timestamp.

The physical Redis TTL extends beyond logical expiry by a grace period so rejection reason can still be classified after logical expiry.

### Read / validation

The Redis strategy reads the token value and classifies it as one of:

- live;
- expired;
- terminated;
- not found;
- malformed.

API-key, PAT, and JWT bearer values are explicitly excluded from being misclassified as missing Redis sessions.

### Refresh

A live Redis session refresh extends logical expiry while preserving the original issue time. A non-live or missing session results in a newly issued session token.

### Logout / termination

Redis logout overwrites the token with a tombstone rather than simply deleting it. This lets subsequent requests distinguish an explicit sign-out from an anomalous missing token.

## PostgreSQL session lifecycle

The PostgreSQL mode uses a `RefreshableDatabaseStrategy` backed by an access-token database. The strategy is stateful and supports token refresh by updating persisted token state.

Exact logout/delete behavior is delegated to the database strategy/framework path and remains a runtime verification item; this static trace does not claim revocation effectiveness.

## Single-tenant JWT session lifecycle

### Issuance

The JWT strategy creates a signed token containing at least:

- subject/user ID;
- audience;
- issued-at timestamp;
- expiry based on the configured session lifetime.

### Refresh

JWT refresh issues a new JWT with a new expiry.

### Logout / revocation property

The JWT strategy documents that the previously issued JWT remains valid until natural expiry. `destroy_token` is a no-op because the token is stateless and no server-side revocation state is consulted.

This is an explicit lifecycle property to test and document. It is not labeled a vulnerability by this action.

## Current-user post-authentication checks

After user resolution, `double_check_user` performs additional checks before the identity is accepted by ordinary protected routes.

Observed checks include:

- configured email-verification requirement;
- OIDC expiry enforcement;
- authentication failure does not silently fall back to anonymous access;
- ordinary `current_user` rejects limited users;
- chat-specific dependency may allow a configured anonymous user path.

## Authorization coupling

Authentication alone is not sufficient for privileged operations.

`require_permission` combines:

1. the user’s resolved permission authority; and
2. the authenticating token’s scope cap, when token scopes are present.

Therefore a PAT can authenticate as a user but still be denied when the PAT’s scopes do not imply the required permission.

## Tenant-relevant lifecycle observations

Source inspection shows tenant information is carried or encoded in multiple credential paths:

- Redis session values carry `tenant_id`;
- multi-tenant PATs encode tenant information in the token format;
- multi-tenant API keys encode tenant information in the token format;
- the auth/user code imports tenant context variables and tenant-specific database session helpers.

This action does **not** yet prove that every credential is correctly bound to the tenant during every downstream request. That property moves into the Phase 9 tenant-authorization trace and runtime matrix.

## Security-relevant design properties to verify at runtime

### Session lifecycle

- expired Redis session must be rejected;
- terminated Redis session must be rejected;
- malformed Redis session must fail closed;
- Redis token missing after grace period must fail closed;
- refresh must not revive a terminated token unexpectedly;
- logout from one client must have the expected effect on replay from another client.

### PostgreSQL sessions

- expired persisted session must be rejected;
- logout must invalidate persisted state as intended;
- refreshed token state must obey configured lifetime;
- deleted/disabled user handling must fail closed.

### JWT session backend

- logout followed by replay of the old JWT must match the documented stateless behavior;
- refresh must not be mistaken for revocation of the previous JWT;
- expiry must be enforced;
- forged/modified JWT must be rejected;
- wrong signing key must be rejected.

### External JWT verification

- non-RS256 token must be rejected;
- invalid signature must be rejected;
- incorrect configured audience must be rejected;
- incorrect configured issuer must be rejected;
- unknown/missing signing key must fail closed;
- unsafe DB-configured key URLs must be rejected under configured SSRF policy.

### PATs

- invalid PAT must be rejected;
- expired/revoked PAT must be rejected where supported by persistence state;
- PAT lacking required scope must be denied even if its user holds the permission;
- PAT must not escape its tenant context;
- raw non-Bearer PAT presentation must be rejected.

### API keys

- invalid/revoked API key must be rejected;
- service-account privileges must remain least-privilege;
- API key must not cross tenant boundaries;
- historical raw-key transport must be tested as an explicit compatibility surface.

### User-state enforcement

- unverified user must be rejected when verification is required;
- expired OIDC-linked identity must be rejected on ordinary protected routes;
- limited user must be rejected by `current_user` routes;
- a failed real authentication attempt must not downgrade into anonymous access.

## Preliminary lifecycle model

```text
Credential presented
    |
    +--> Session cookie / mobile bearer
    |       |
    |       +--> Redis / PostgreSQL / JWT strategy
    |
    +--> External JWT bearer
    |       +--> signature + aud/iss validation
    |
    +--> PAT bearer
    |       +--> hash -> DB -> user + token scopes
    |
    +--> API key
            +--> hash -> DB -> user/service identity

                |
                v
          Resolved identity
                |
                v
       double_check_user()
                |
        verified / expiry / state
                |
                v
         current_user / route
                |
                v
       require_permission()
                |
      user authority ∩ token scopes
                |
                v
        resource authorization
```

## Findings decision

No vulnerability is declared by Action 9.3.

The stateless JWT logout/replay property is recorded as a security-relevant design characteristic requiring runtime verification and residual-risk documentation when that backend is used.

## Completion result

**PASS — authentication, session and token lifecycle trace captured.**

## Next

**Action 9.4 — Authorization-policy and ownership-control trace.**
