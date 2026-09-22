# Phase 9 — Action 9.10 — H9-19 Login OAuth Token Storage and Lifecycle

## Hypothesis

H9-19 evaluated storage protection and lifecycle handling for login-provider
OAuth access and refresh tokens represented by `OAuthAccount`.

## Storage model

`OAuthAccount` declares:

- `access_token` as ordinary SQL `Text`;
- `refresh_token` as ordinary SQL `Text`.

Repository analysis found:

- login OAuth ordinary-text token declarations: **2**
- login OAuth encrypted declaration hits: **0**
- application encryption binding: **NOT FOUND**

This differs from numerous other sensitive fields in the same application
which use `EncryptedString` or `EncryptedJson`.

## Live database metadata

The authorized local database metadata confirmed:

- `oauth_account.access_token`: PostgreSQL `text`
- `oauth_account.refresh_token`: PostgreSQL `text`
- `oauth_account.expires_at`: integer

The lab contained zero `oauth_account` rows at the time of inspection.

No access-token or refresh-token values were selected or printed.

## Application-level encryption

**No application-level encryption binding was identified for login
`OAuthAccount.access_token` or `refresh_token`.**

This property is independent of whether `ENCRYPTION_KEY_SECRET` is configured:
these fields do not use the application's encrypted SQLAlchemy decorators.

The current lab additionally reported:

- `ENCRYPTION_KEY_SECRET_CONFIGURED=NO`

## Refresh lifecycle controls

Source tracing established an implemented refresh lifecycle:

- access-token expiry is tracked;
- refresh begins inside a five-minute expiry window;
- a per-user asynchronous lock coalesces concurrent refresh attempts;
- the OAuth row is refreshed inside the lock;
- rotated refresh tokens returned by an IdP are persisted;
- when the provider does not return a replacement refresh token, the existing
  refresh token is preserved;
- updated access token, refresh token and expiry are written through
  `update_oauth_account`.

These controls reduce refresh races and support providers that rotate refresh
tokens.

## Deletion / revocation lifecycle

The `User.oauth_accounts` relationship uses:

`cascade="all, delete-orphan"`

so deleting the local user removes associated login OAuth account rows.

The trace also located an OAuth-token revocation endpoint for the application's
separate configurable OAuth-token subsystem.

However, this Action 9.10 trace did **not establish an explicit provider-side
token-revocation operation for login `OAuthAccount` access/refresh tokens**.

That distinction is preserved as a remediation/review requirement rather than
being assumed.

## Security disposition

**H9-19 — CONFIRMED STORAGE-HARDENING FINDING WITH FUNCTIONING REFRESH-LIFECYCLE CONTROLS**

Confirmed:

1. login access and refresh tokens are stored in ordinary database text fields;
2. no application encryption decorator protects those fields;
3. refresh/rotation/expiry handling is implemented;
4. local user deletion cascades OAuth-account deletion;
5. provider-side revocation for the login-token path was not established.

This is an evidence-backed disposition sufficient to complete Action 9.10.

## Remediation / assurance requirements

Carry into Action 9.11 / 9.12:

- migrate login OAuth bearer and refresh tokens to an appropriate protected
  secret-storage representation;
- align the design with the authenticated-encryption requirements identified
  by H9-18;
- provide a migration strategy for existing ordinary-text OAuth rows;
- preserve refresh-token rotation semantics and concurrency controls;
- verify logout, unlink, user deletion and provider-revocation expectations;
- add tests proving raw token values do not persist in ordinary unprotected
  application columns after migration;
- verify token values never enter logs or evidence artifacts.

No token-storage migration was performed during runtime-verification
Action 9.10.

## Safety

- database mutations: **0**
- HTTP requests: **0**
- token values selected: **0**
- token values printed: **0**
- external network requests: **0**
- source files changed during testing: **0**

## Evidence identity

- storage/lifecycle trace SHA-256: `7a10f5bef76c25894fcd1e2501d28c234d8ed3defa61d0db7f6c992c2bbe19e6`
