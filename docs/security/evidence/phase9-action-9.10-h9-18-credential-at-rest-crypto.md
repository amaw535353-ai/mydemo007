# Phase 9 — Action 9.10 — H9-18 Credential-at-Rest Encryption

## Hypothesis

H9-18 evaluated credential-at-rest confidentiality, ciphertext integrity,
wrong-key behavior, and missing-key behavior.

## Storage-path reachability

The repository trace confirmed that credential-bearing ORM storage uses the
application encryption wrappers through `EncryptedString` and
`EncryptedJson`.

Observed:

- encryption write call sites: **6**
- decryption read call sites: **5**
- credential-related caller files: **4**
- encryption wrapper used for writes: **YES**
- credential storage path reachable: **YES**

Representative protected fields include credential JSON, provider API keys,
OAuth client secrets, encrypted PATs, and other `SensitiveValue` columns.

## Live deployment configuration

The local authorized laboratory reported:

- `ENCRYPTION_KEY_SECRET_CONFIGURED=NO`
- encryption-key value printed: **NO**

Therefore the current deployment does not enable application-level
credential-at-rest encryption for storage paths using this mechanism.

## Missing-key behavior

Synthetic validation confirmed:

- `NO_KEY_STORES_RAW_UTF8=TRUE`
- `NO_KEY_CONFIDENTIALITY=ABSENT`

When no encryption key is configured, the encryption implementation returns
raw UTF-8 bytes.

## Keyed confidentiality behavior

Synthetic keyed validation confirmed:

- encrypted bytes differ from plaintext: **TRUE**
- correct-key round trip: **TRUE**

The EE implementation therefore provides confidentiality when a key is
configured.

## Wrong-key behavior

Using an explicitly supplied wrong key produced:

- `WRONG_KEY_RAISED=TRUE`
- exception: `ValueError`

For this tested explicit-key path, wrong-key decryption fails closed rather
than returning the original secret.

## Ciphertext integrity

The EE implementation uses AES-CBC with a random IV and PKCS#7 padding but no
cryptographic authentication tag.

A one-bit modification to the IV produced:

- `TAMPER_RAISED=FALSE`
- `TAMPER_RETURNED_ORIGINAL=FALSE`
- `TAMPER_ACCEPTED_CORRUPTED_PLAINTEXT=TRUE`
- `CIPHERTEXT_AUTHENTICITY=ABSENT`

The keyed construction therefore does not provide authenticated integrity.

## Security disposition

**H9-18 — CONFIRMED SECURITY-PROPERTY / DEPLOYMENT-HARDENING FINDING**

Two distinct conditions were established:

1. **Current deployment confidentiality**
   - no `ENCRYPTION_KEY_SECRET` is configured;
   - credential-bearing storage paths reach the encryption wrappers;
   - missing-key behavior stores raw UTF-8 bytes.

2. **EE keyed cryptographic integrity**
   - AES-CBC provides keyed confidentiality;
   - ciphertext/IV modification is not cryptographically authenticated.

This finding is evidence-backed and complete for Action 9.10.

## Remediation requirement

Carry into Action 9.11 / 9.12:

- require an appropriate production encryption key where application-level
  secret encryption is expected;
- replace unauthenticated AES-CBC storage with an authenticated-encryption
  construction such as an AEAD design;
- version the ciphertext format;
- provide migration / rotation support for existing plaintext and CBC records;
- add negative tests for tampered ciphertext, wrong keys, malformed records,
  and missing production configuration;
- preserve fail-closed behavior during migration.

No cryptographic storage-format migration was performed during Action 9.10.

## Safety

- database mutations: **0**
- HTTP requests: **0**
- external network requests: **0**
- credential values printed: **0**
- source files modified during testing: **0**

## Evidence identities

- synthetic crypto validation SHA-256: `79fe7f849a2eae143bcde969a2f72ca5efa40a2bef5c7663c2933322c5ff83f9`
- credential storage-path trace SHA-256: `67ba9f46c455d22e508a2026471413bdd48e26a92998d80eb291991cb050a0e7`
