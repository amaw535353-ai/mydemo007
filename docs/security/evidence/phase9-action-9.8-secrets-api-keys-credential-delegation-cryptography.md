# Phase 9 Action 9.8 — Secrets, API Keys, Credential Delegation and Cryptography

Status: **COMPLETE — static trace; runtime hypotheses remain**

## Objective

Trace how Onyx creates, stores, masks, rotates, delegates and validates secrets and bearer credentials, then assess the cryptographic constructions protecting those values. Separate application guarantees from edition/deployment controls and do not classify a vulnerability without the required product-policy and runtime evidence.

## Scope and safety

- Authorized Onyx repository and local/synthetic lab only.
- No real OAuth, MCP, model-provider, connector, customer or production credentials.
- Do not copy raw secret values into commits, issues, screenshots or portfolio evidence.
- Runtime tests remain bounded by Phase 9 limits and are deferred to Actions 9.9–9.10.
- Static cryptographic properties are recorded as properties/hypotheses until mapped to an explicit security requirement and runtime configuration.

## Source paths traced

- `backend/onyx/utils/encryption.py`
- `backend/ee/onyx/utils/encryption.py`
- `backend/onyx/utils/sensitive.py`
- `backend/onyx/db/models.py`
- `backend/onyx/auth/api_key.py`
- `backend/onyx/db/api_key.py`
- `backend/onyx/auth/pat.py`
- `backend/onyx/auth/oauth_token_manager.py`
- `backend/onyx/db/oauth_config.py`
- `backend/onyx/tools/tool_constructor.py`
- `backend/onyx/server/features/mcp/credentials.py`
- `backend/onyx/tools/tool_implementations/mcp/mcp_tool.py`
- `backend/onyx/auth/jwt.py`
- `backend/onyx/auth/oidc_client.py`
- `backend/onyx/configs/app_configs.py`

## 1. Sensitive-value handling and accidental-disclosure controls

The database layer defines `EncryptedString` and `EncryptedJson` types that wrap loaded or assigned values in `SensitiveValue`.

`SensitiveValue` requires callers to make an explicit masking decision through `get_value(apply_mask=True/False)` and blocks ordinary `str`, iteration, subscripting and direct JSON/Pydantic serialization. Its default masked path uses `mask_string` or recursive credential-dictionary masking.

The shared encryption utilities additionally:

- mask most environment-variable values before logging;
- sanitize credential-bearing URLs;
- reject masked placeholders at credential-write boundaries;
- restore intentionally round-tripped masked values from the stored secret rather than persisting the mask itself.

Security interpretation: the source has deliberate defenses against accidental secret disclosure and masked-placeholder corruption. Runtime/log review should verify these controls remain effective at API boundaries.

## 2. Application-level encryption is edition and configuration dependent

The base/MIT `_encrypt_string` implementation does not provide cryptographic encryption; it returns `input_str.encode()` and the paired decrypt function decodes the bytes. The source explicitly logs that the MIT version does not support encryption of secrets.

The EE override changes the behavior when `ENCRYPTION_KEY_SECRET` is available:

- the configured key is converted directly to bytes and trimmed to 32, 24 or 16 bytes;
- keys shorter than 16 bytes are rejected;
- a fresh 16-byte IV is generated;
- plaintext is padded with PKCS#7;
- encryption uses AES-CBC;
- the stored value is `IV || ciphertext`.

If the effective EE encryption key is absent, the EE implementation also returns plaintext UTF-8 bytes.

The traced construction does not append an authentication tag or MAC, so confidentiality and ciphertext integrity are separate concerns. The key material is trimmed directly rather than derived with a KDF.

### H9-18 — Credential-at-rest encryption integrity and fail-open behavior

This is a source-backed cryptographic property, not yet a vulnerability classification.

Required runtime/policy questions:

1. Which edition/deployment mode is actually running?
2. Is `ENCRYPTION_KEY_SECRET` set, without exposing its value?
3. Are `EncryptedString`/`EncryptedJson` rows ciphertext or plaintext in the assessed deployment?
4. Does the product security requirement require authenticated encryption at the application layer?
5. Is database/storage encryption at rest an independent compensating control?
6. Is ciphertext modification detected cryptographically?
7. What is the supported key-rotation and rollback procedure?

Tracking: **GitHub Issue #6**.

## 3. API-key generation, storage and rotation

Current API keys are generated with Python `secrets.token_urlsafe(...)`; multi-tenant keys include the URL-encoded tenant identifier before the random secret portion.

Current keys are transformed with SHA-256 before database lookup/storage. The source notes that a salt is unnecessary for this design because the input is a high-entropy randomly generated bearer secret rather than a human password. The database stores the hash and a masked display form; the full key is returned only in the creation/regeneration result.

A deprecated API-key format still has a compatibility hash path using `sha256_crypt` with the configured work factor.

Lifecycle controls traced in Action 9.7 also replace the stored hash during regeneration and remove the associated synthetic service-account user when the key is deleted.

Security interpretation: the current bearer secret is not stored reversibly in the `ApiKey` row. Runtime tests must still prove old-key rejection after rotation/deletion and verify no raw key reaches logs or telemetry.

## 4. Personal access tokens

PATs use `secrets.token_urlsafe(...)` for generation and SHA-256 for stored lookup material. In multi-tenant mode the tenant identifier is encoded into the token format. PAT presentation requires the Bearer scheme, unlike legacy-compatible API-key parsing which also permits the historical raw-key form.

PAT expiration may be explicit or absent (`None` means no expiration). Phase 9 runtime testing should therefore inventory whether non-expiring PATs are permitted by policy and verify deletion/revocation behavior, while avoiding duplicate testing already covered by the authentication/session trace.

No defect is claimed from SHA-256 storage of high-entropy randomly generated PATs.

## 5. Tool OAuth client secrets and user tokens

`OAuthConfig.client_id` and `OAuthConfig.client_secret` use `EncryptedString`; tool-specific `OAuthUserToken.token_data` uses `EncryptedJson`. The token manager explicitly unwraps these sensitive values only when required for authorization-code exchange or refresh.

The OAuth token client enforces HTTPS-only token endpoints and applies the configured outbound SSRF policy. It computes access-token expiry, refreshes when possible, preserves a refresh token when the provider omits a replacement, and writes the refreshed token set back through the encrypted token model.

Security interpretation: tool-specific OAuth credentials are intentionally routed through the sensitive/encrypted storage abstraction and HTTPS-only exchange path.

## 6. Login OAuth tokens have a different storage boundary

`OAuthAccount`, the login-provider account model, overrides `access_token` and `refresh_token` as ordinary SQLAlchemy `Text` columns. These fields are not declared as `EncryptedString`/`EncryptedJson` in the traced model.

The tool-construction path can read `user.oauth_accounts[0].access_token` and use it for custom-action passthrough authentication when the action is configured for that mode.

### H9-19 — Login OAuth access/refresh tokens are application-plaintext DB fields

The storage property itself is confirmed by source. A vulnerability classification still depends on the deployment threat model, database-at-rest controls, token lifetime/scope, and the product's requirement for application-level secret encryption.

Runtime verification must use a local/mock OAuth provider, inspect storage without recording raw token values, test unlink/logout/revocation cleanup and confirm passthrough-auth forwarding does not log or expose the token.

Tracking: **GitHub Issue #7**.

## 7. MCP credential isolation and precedence

The MCP credential path stores connection configuration in the sensitive/encrypted model and resolves the effective credential based on server authentication type and performer:

- per-user API token/OAuth uses the user's connection config;
- admin-performed authentication can use the admin connection config;
- passthrough OAuth uses the acting user's login OAuth token;
- generated authentication headers take precedence over stored/caller-supplied headers;
- denylisted MCP headers such as `Host` are stripped.

Request-supplied MCP headers remain separately tracked as H9-16 because, in states without managed credentials, additional headers can intentionally participate in delegated authentication. Runtime policy proof is still required.

## 8. JWT verification and signing-algorithm boundaries

The external JWT verification path resolves PEM/JWKS public-key material and calls the decoder with `algorithms=["RS256"]`, preventing algorithm selection from being driven by the token itself. Audience verification is enabled when an expected audience is configured, and expected issuer is likewise passed when configured.

For database-origin public-key URLs, the code applies IdP URL validation plus SSRF-safe HTTPS fetching. Environment-pinned key URLs are treated as trusted operator configuration and fetched directly.

The application configuration also defines an HS256 algorithm for the application's own JWT mode. Cryptographic-algorithm choice is therefore explicit rather than token-controlled, but overall algorithm agility is limited and should be treated as a design/operations consideration rather than an Action 9.8 vulnerability by itself.

## 9. OIDC/OAuth hardening controls

The OIDC client adds issuer/configuration-origin validation to defend against provider mix-up and rejects present-but-unverified email claims. Token-exchange failure logging is restricted to the standard RFC 6749 error fields rather than dumping arbitrary response bodies.

The generic OAuth helper supports PKCE S256 when a code challenge/verifier is supplied. Login OIDC configuration exposes `OIDC_PKCE_ENABLED`, which is disabled by default for backward compatibility. That configuration should be included in the deployment-hardening review; no standalone vulnerability is claimed solely because PKCE is optional in source.

## 10. Secret and crypto runtime matrix queued for Actions 9.9–9.10

| ID | Test | Expected result |
| --- | --- | --- |
| SC-01 | Create/regenerate synthetic API key | full secret shown only at issuance; DB keeps hash/masked display |
| SC-02 | Use old API key after regeneration | DENY |
| SC-03 | Use deleted API key | DENY |
| SC-04 | Create PAT and inspect persistence | raw PAT absent from DB/logs; only expected hash/display metadata stored |
| SC-05 | Expired/deleted PAT | DENY |
| SC-06 | Persist synthetic `EncryptedString`/`EncryptedJson` under assessed edition | storage matches documented encryption state |
| SC-07 | Repeat same plaintext under enabled EE encryption | ciphertext differs because IV differs |
| SC-08 | Mutate copied ciphertext in isolated DB | integrity behavior recorded; evaluate H9-18 |
| SC-09 | Rotate encryption key using synthetic data | supported migration/rollback proven or gap documented |
| SC-10 | Mock tool-OAuth token persistence | sensitive/encrypted storage path confirmed |
| SC-11 | Mock login-OAuth token persistence | evaluate H9-19 without recording secret values |
| SC-12 | Passthrough-auth custom action to approved local receiver | acting user's token only; no cross-user token reuse or logging |
| SC-13 | MCP caller-supplied Authorization vs managed credential | managed credential precedence holds; evaluate H9-16 |
| SC-14 | External JWT with wrong algorithm | DENY |
| SC-15 | External JWT wrong configured audience/issuer | DENY when those constraints are configured |
| SC-16 | OIDC login with PKCE enabled/disabled in local mock IdP | behavior matches deployment policy; no secret leakage |

## 11. Findings disposition

- **H9-18:** open cryptographic requirement/runtime hypothesis — Issue #6.
- **H9-19:** confirmed storage property, risk classification pending threat model/runtime — Issue #7.
- **H9-16:** delegated MCP-header trust-policy hypothesis carried forward from Action 9.6.
- **H9-17:** service-account interactive-session hypothesis from Action 9.7 is now tracked in Issue #5.

No confirmed vulnerability is declared by Action 9.8 static analysis alone.

## Conclusion

Onyx has deliberate secret-handling controls: high-entropy API/PAT generation, one-way bearer-secret storage, masked display forms, `SensitiveValue` disclosure friction, encrypted/sensitive types for many connector/OAuth/MCP values, HTTPS-only OAuth token exchanges, fixed external JWT verification algorithms, and defensive secret/error logging.

The strongest unresolved boundaries are the edition/configuration-dependent at-rest encryption construction (**H9-18**) and the different storage treatment of login OAuth access/refresh tokens (**H9-19**). Both are now queued for controlled synthetic verification and explicit security-requirement mapping before classification.
