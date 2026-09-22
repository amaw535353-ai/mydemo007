# Phase 9 — Action 9.11 — H9-19 OAuth Token Storage Remediation

## Finding

Login OAuth account `access_token` and `refresh_token` values were stored
in PostgreSQL `TEXT` columns.

The existing refresh/expiry/rotation lifecycle operated correctly, but the
token values did not use the application's protected secret-storage mechanism.

## Root cause

`OAuthAccount.access_token` and `OAuthAccount.refresh_token` were ordinary
text ORM fields.

Existing login OAuth consumers expect ordinary Python strings, while the
general `EncryptedString` type exposes a `SensitiveValue` wrapper.

A direct replacement would therefore alter an established runtime contract.

## Remediation

A dedicated `EncryptedOAuthToken` SQLAlchemy type now:

- inherits the hardened encrypted binary storage behavior;
- uses the H9-18 versioned AES-GCM mechanism for keyed writes;
- stores values using binary PostgreSQL storage;
- unwraps the decrypted value back to ordinary `str` for existing login OAuth
  consumers.

Both OAuth token fields use this type.

## Schema migration

Alembic revision:

`919019aead01`

converts:

- `oauth_account.access_token`: TEXT -> BYTEA
- `oauth_account.refresh_token`: TEXT -> BYTEA

Existing text is preserved losslessly with PostgreSQL UTF-8 byte conversion.

Application-level AEAD migration remains a separate key-aware operation using
the H9-18 rotation mechanism.

## Real PostgreSQL proof

A maximum of one synthetic OAuth row was used.

Verified:

- original columns were TEXT: **PASS**
- Alembic TEXT -> BYTEA upgrade: **PASS**
- access-token conversion lossless: **PASS**
- refresh-token conversion lossless: **PASS**
- legacy BYTEA still returned ordinary strings: **PASS**
- rotation discovers both OAuth token fields: **PASS**
- access token migrated to versioned AEAD: **PASS**
- refresh token migrated to versioned AEAD: **PASS**
- ORM contract after AEAD migration remains `str`: **PASS**
- simulated refresh replacement writes encrypted ciphertext: **PASS**
- replacement round-trip: **PASS**
- repeated rotation is idempotent: **PASS**
- downgrade refuses while AEAD ciphertext is present: **PASS**
- synthetic row cleanup: **PASS**
- original database revision restored: **PASS**
- original TEXT schema restored after proof: **PASS**
- pre-existing OAuth rows modified: **0**

No provider network call was performed.

## Lifecycle assurance

Existing login-OAuth refresh behavior remains structurally unchanged:

- token expiry tracking remains present;
- refresh-token replacement remains supported;
- access-token replacement remains supported;
- existing locking/refresh lifecycle is not rewritten by this remediation.

The storage remediation protects tokens at rest when an encryption key is
configured.

Explicit provider-side token revocation was not established by the earlier
trace and is not claimed here. That remains a residual lifecycle-assurance item
for the Phase 9 final-risk gate.

## Deployment assurance

Application-level confidentiality requires a configured and protected
`ENCRYPTION_KEY_SECRET`.

Deployment rollout must include:

1. schema migration to binary token columns;
2. configured encryption key;
3. key-aware secret rotation/migration for legacy byte records;
4. verification before retiring rollback material.

## Test environment

The available runtime images do not contain `pytest`.

Validation therefore used:

- syntax validation;
- direct SQLAlchemy type regression;
- authenticated-encryption property checks;
- real Alembic migration;
- real PostgreSQL storage;
- real key-rotation behavior;
- explicit cleanup and rollback.

## Safety

- pre-existing OAuth rows modified: **0**
- maximum synthetic OAuth rows: **1**
- retained synthetic OAuth rows: **0**
- provider HTTP requests: **0**
- external network requests: **0**
- real OAuth credentials: **0**

## Evidence identities

- PostgreSQL migration proof SHA-256: `ddddf2526582ea28120a3aa0994c5b2793941ca6d836828f0309a723fc5be58e`
- final model regression SHA-256: `b1816241324fe50c9af93182c3f2c154119662d2f183d832eaeccaf59951e453`

## Status

**H9-19 STORAGE REMEDIATION: PASS**
