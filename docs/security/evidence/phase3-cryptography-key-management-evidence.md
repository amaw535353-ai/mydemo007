# Phase 3 Action 3.11 - Cryptographic Primitives & Key Management Evidence

## Observation class

**STATIC SOURCE CANDIDATES ONLY. RUNTIME BEHAVIOR IS UNVERIFIED.**

- Branch: `security/phase-3-foundations`
- HEAD: `1e01b858675304a6cc11e61a40c4e47001f0225b`
- Candidate files: **706**
- Matching lines: **16135**

## Review scope

Hashing, HMAC, KDFs, symmetric/asymmetric cryptography, signing, encryption, randomness, certificates and key management.

## Representative candidates

- `AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic/versions/01f8e6d95a33_populate_flow_mapping_data.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py`
- `backend/alembic/versions/2c7f9d3a84a0_add_pat_type_and_encrypted_pat.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/3c9a65f1207f_seed_exa_provider_from_env.py`
- `backend/alembic/versions/582269841f06_add_granted_scopes_to_external_app_user_.py`
- `backend/alembic/versions/7f5b159041be_skill_built_in_id_discriminator.py`
- `backend/alembic/versions/8f3b2c91d4e7_backfill_legacy_callback_on_seeded_sso_.py`
- `backend/alembic/versions/989bc57562e4_seed_browser_built_in_skill.py`
- `backend/alembic/versions/ae62505e3acc_add_saml_accounts.py`
- `backend/alembic/versions/b4950827c0dd_encrypt_external_app_credentials.py`
- `backend/alembic/versions/b51c6844d1df_seed_memory_tool.py`
- `backend/alembic/versions/b6d184cfdaf3_skills.py`
- `backend/alembic/versions/c5d9662b3c50_seed_craft_documentation_built_in_skill.py`

## Interpretation

Static candidates do not prove runtime security enforcement.

## Safety

- No credential submitted.
- No token replayed.
- No authorization bypass attempted.
- No role/session/cookie modified.
- No private-key contents displayed.
- No external service contacted.
