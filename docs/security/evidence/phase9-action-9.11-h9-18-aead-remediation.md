# Phase 9 — Action 9.11 — H9-18 AEAD Remediation

## Finding

H9-18 established that the previous keyed EE secret-storage format used
AES-CBC with PKCS#7 padding but no authenticated integrity.

The assessed local deployment also had no `ENCRYPTION_KEY_SECRET`, causing
the compatibility path to store raw UTF-8 values.

## Root cause

The historical keyed format was:

`IV || AES-CBC ciphertext`

No authentication tag protected the IV or ciphertext.

The historical rotation logic also treated any record decryptable using the
current key as already rotated. That would incorrectly skip legacy CBC records
encrypted using the same key.

## Remediation

New keyed secret writes now use a versioned authenticated-encryption envelope:

`ONYXAEAD1: || 12-byte nonce || AES-GCM ciphertext/tag`

Properties verified:

- authenticated AES-GCM encryption;
- random nonce per write;
- explicit versioned envelope;
- tampering fails closed;
- wrong-key reads fail closed;
- missing-key reads of versioned ciphertext fail closed;
- malformed authenticated ciphertext does not fall back to plaintext.

## Legacy migration

Legacy records remain readable specifically for migration:

- raw UTF-8 records;
- historical AES-CBC records.

Legacy records are not considered current.

The rotation helper now skips a record only when:

1. it has the current authenticated format; and
2. authenticated decryption using the current key succeeds.

This ensures same-key legacy CBC is still migrated.

## Real PostgreSQL proof

A bounded synthetic PostgreSQL fixture proved:

- plaintext -> AEAD: **PASS**
- AEAD decrypt after migration: **PASS**
- second rotation idempotently skipped: **PASS**
- same-current-key legacy CBC -> AEAD: **PASS**
- final rotation idempotently skipped: **PASS**
- fixture cleanup: **PASS**
- existing application rows modified: **0**

The synthetic table was removed after validation.

## Test-runner limitation

The current host, API container and pinned backend image did not provide
`pytest`.

No dependency installation or network retrieval was performed solely to obtain
a test runner.

Validation instead consisted of:

- Python syntax compilation;
- direct cryptographic security-property regression;
- rotation-format regression;
- real PostgreSQL migration proof.

Repository regression tests were extended for execution in the normal project
test environment when its test dependencies are available.

## Remaining deployment assurance

The assessed lab still has no configured `ENCRYPTION_KEY_SECRET`.

Therefore:

- the authenticated-integrity implementation defect is remediated;
- the migration mechanism is verified;
- production application-level confidentiality still depends on configuring
  and protecting the encryption key and migrating legacy records.

That configuration requirement remains a Phase 9 deployment-assurance item.

## Safety

- existing application rows modified: **0**
- maximum synthetic rows: **1**
- synthetic fixture retained: **NO**
- HTTP requests: **0**
- external network requests: **0**
- real credentials: **0**

## Evidence identities

- reconstructed design record SHA-256: `f8004d853d5cff58ee942cec9250a8836f16d82637a155986f06aad8d41b2376`
- PostgreSQL proof SHA-256: `f35b2c4f415569af8439aa6a9ad040e89dcab395f3fda45abec7861f1c027442`
- final crypto regression SHA-256: `61dfeabf2d2a0f7f06ca0d89d7f9b3b71096dcf7e11f6f0f8252f68b5f8cfe63`
