# Phase 9 Action 9.7 — Workload Identity, Service Authentication and Trust Relationships

Status: **COMPLETE — static trace; runtime hypotheses remain**

## Objective

Trace workload and machine identities through provisioning, credential issuance, authorization, tenant binding and service trust boundaries. Distinguish application-enforced properties from deployment/infrastructure controls and avoid classifying a vulnerability without controlled runtime evidence.

## Scope and safety

- Authorized Onyx laboratory and repository only.
- Synthetic users, service accounts, groups, tenants and credentials only.
- No calls to real external services.
- No production secrets or customer data.
- Static source observations are not vulnerability claims.
- Runtime verification remains bounded by the Phase 9 engagement rules.

## Source paths traced

- `backend/onyx/server/api_key/api.py`
- `backend/onyx/server/api_key/models.py`
- `backend/onyx/db/api_key.py`
- `backend/onyx/auth/api_key.py`
- `backend/onyx/auth/users.py`
- `backend/onyx/db/enums.py`
- `backend/onyx/db/engine/sql_engine.py`

## 1. Workload-principal model

The current API-key implementation represents a service identity as two linked database objects:

1. an `ApiKey` credential row; and
2. a synthetic `User` row with `account_type=AccountType.SERVICE_ACCOUNT`.

`insert_api_key(...)` creates the synthetic user with:

- a generated UUID;
- a dummy API-key email address;
- a randomly generated password hash;
- `is_active=True`;
- `is_superuser=False`;
- `is_verified=True`;
- `account_type=SERVICE_ACCOUNT`.

The service account is then assigned to the groups supplied in `APIKeyArgs.group_ids`.

Security interpretation: workload authorization is intentionally projected through the same group/permission model used by human principals rather than through a separate hard-coded service-role table.

## 2. Provisioning and administration boundary

The `/admin/api-key` management surface requires `Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS` for list, read, create, regenerate, update and delete operations.

The create route contains an explicit design note that this permission is **admin-equivalent by design** because its holder can assign a service account to any group, including Admin.

`APIKeyArgs` accepts a name and a list of `group_ids`; the group set therefore defines the workload identity's effective privilege set.

Security interpretation:

- this is a deliberately high-impact administrative capability rather than a low-privilege self-service API-key feature;
- review of who receives `MANAGE_SERVICE_ACCOUNT_API_KEYS` is security-critical;
- callers must not interpret possession of this permission as narrowly limited key-management authority.

No defect is claimed from the documented admin-equivalent design.

## 3. Group-backed least privilege and change propagation

`insert_api_key(...)` assigns the synthetic service-account user to the requested groups.

`update_api_key(...)` replaces the service account's group memberships with the submitted group list. The underlying group setter recomputes permissions, and the source comment explicitly notes that edits repair stale key permissions.

`regenerate_api_key(...)` also recomputes the service-account user's permissions so credential rotation converges stale authorization state.

`remove_api_key(...)` deletes both the key and the associated synthetic user through the canonical user-deletion helper, including related membership/foreign-key state.

Security interpretation: identity lifecycle, credential lifecycle and permission lifecycle are coupled intentionally. A runtime matrix should still verify immediate privilege reduction after group removal, key regeneration and key deletion.

## 4. Credential generation and tenant binding

`generate_api_key(tenant_id)` behaves differently by deployment mode:

- single tenant: opaque random API key;
- multi tenant: key format includes a URL-encoded tenant identifier before the random secret component.

`insert_api_key(...)` and `regenerate_api_key(...)` obtain the current tenant from `get_current_tenant_id()` and pass it into key generation.

The key is stored as a one-way hash; only the display form and hash remain in the database after creation/rotation.

Tenant-aware database sessions provide a second boundary. `get_session()` reads `get_current_tenant_id()`, rejects the default schema as unauthenticated in multi-tenant mode, validates the schema name, and tenant sessions use SQLAlchemy `schema_translate_map={None: tenant_id}`.

Security interpretation:

- API keys have an explicit tenant signal in multi-tenant mode;
- key records and service-account users are accessed through tenant-bound database sessions;
- the absence of a separate `tenant_id` field on the key row is therefore not, by itself, evidence of cross-tenant key replay;
- cross-tenant replay remains a useful negative runtime test and should be expected to DENY.

## 5. Authentication result maps back to a user principal

`fetch_api_key_auth_result(...)` resolves a hashed credential by joining the `ApiKey` row to its associated `User` row and returns both the service-account principal and key metadata.

This preserves a concrete actor identity for downstream authorization and auditing instead of treating an API key as an unowned global bearer secret.

The authentication path should therefore be tested for:

- inactive service-account denial;
- deleted key denial;
- regenerated old-key denial;
- group/permission changes taking effect on subsequent requests;
- tenant mismatch denial.

## 6. Interactive-login boundary

`AccountType.is_web_login()` returns false only for `BOT` and `EXT_PERM_USER`. Consequently, `SERVICE_ACCOUNT` is considered a web-login-capable account type.

At the same time, service-account provisioning deliberately gives the synthetic user a random generated password hash that is not returned as a human login credential.

The OAuth account-linking path also treats any account with `is_web_login()==True` as an existing web-login-compatible identity rather than a placeholder that must be upgraded to `STANDARD`.

This creates an important policy question:

### H9-17 — Service-account interactive-session reachability

A service account is intended as a machine/workload identity, yet its account type is web-login eligible. Static analysis alone does not prove that a user can obtain a usable browser password/session for it, nor that such access would violate intended product policy.

Required controlled runtime verification:

1. Create a synthetic service-account API key under an authorized admin identity.
2. Confirm API-key use succeeds only with the group-derived permissions expected for that service account.
3. Attempt normal interactive/password login using only credentials legitimately exposed by the product; expected result must be defined from product policy.
4. If an authorized admin reset path permits setting/resetting a service-account password, use a synthetic temporary password and test browser/mobile session creation.
5. Compare effective permissions reached by an interactive service-account session with the API-key workload identity.
6. Test logout/revocation behavior.
7. Test OAuth linking only against an approved local/mock identity provider if available.
8. Classify a finding only if interactive access is reproducible and contradicts the intended service-account boundary or bypasses the intended workload credential/permission controls.

Until runtime evidence and intended policy are established, H9-17 remains a hypothesis.

## 7. Service-to-service and internal-worker trust

The application source traced in this action shows service identities primarily through API-key-backed synthetic users and application-level authorization.

No explicit SPIFFE/SPIRE-style workload identity or application-managed mTLS client-certificate authorization mechanism was identified in the searched application paths. This does **not** establish that the deployed platform lacks mTLS, service-mesh identity, ingress authentication or infrastructure PKI; those controls can exist outside the application repository/runtime layer inspected here.

Disposition:

- application-layer service identity: assessed here;
- infrastructure mTLS / workload PKI: **not established by this source trace** and must be verified against deployment configuration in the relevant infrastructure/cloud phase;
- certificate rotation and cryptographic configuration: carried into Action 9.8 where applicable.

No vulnerability is claimed from an application repository not implementing infrastructure-layer mTLS itself.

## 8. Trust-relationship matrix

| Trust transition | Static control observed | Runtime expectation |
| --- | --- | --- |
| Admin → service-account creation | `MANAGE_SERVICE_ACCOUNT_API_KEYS` | unauthorized actor DENY |
| Service account → group privileges | explicit group assignment | only group-derived privileges ALLOW |
| Group change → existing key | permission recomputation on update | removed privilege DENY immediately on next request |
| Key regeneration → old credential | stored hash replaced | old key DENY, new key ALLOW |
| Key deletion → principal | key plus synthetic user cleanup | deleted key DENY |
| API key → tenant | tenant encoded in MT key + tenant-bound DB schema | wrong tenant DENY |
| API key → user principal | hashed key joins `ApiKey` to `User` | concrete service-account actor preserved |
| Service account → interactive web login | account type reports web-login eligible | policy/runtime proof required — H9-17 |
| Workload → infrastructure service | no app-level mTLS mechanism established | verify deployment-layer control separately |

## 9. Runtime tests queued for Actions 9.9–9.10

- SA-01 unauthorized API-key administration → DENY.
- SA-02 key assigned to low-privilege group → only expected endpoints ALLOW.
- SA-03 removed group privilege using same key → formerly allowed operation DENY.
- SA-04 regenerate key → old key DENY; new key ALLOW.
- SA-05 delete key → deleted credential DENY.
- SA-06 deactivate associated service-account user → key DENY.
- SA-07 cross-tenant replay → DENY.
- SA-08 service account interactive login → expected outcome per documented policy; H9-17.
- SA-09 OAuth-link attempt for service identity, local mock IdP only if applicable → must not create unintended privilege amplification.
- SA-10 audit attribution → key operations and service-account requests retain attributable actor/key metadata where designed.

## Conclusion

The current implementation provides a concrete workload identity model: tenant-aware API keys map to synthetic service-account users whose authorization derives from group membership, and the administrative API explicitly treats service-account key management as an admin-equivalent capability.

The strongest unresolved boundary is **H9-17**, because `SERVICE_ACCOUNT` is classified as web-login capable. This requires product-policy confirmation and controlled runtime proof before any vulnerability classification.

No confirmed vulnerability is claimed from Action 9.7 static analysis alone.
