# Phase 4 Action 4.7 - Secrets & Credential Management Foundations Evidence

## Provenance

- Branch: `security/phase-4-cloud-devsecops`
- Baseline HEAD: `f3a5326a371ca451f14c6243302f0dc713b98e79`

## Observation class

**STATIC SOURCE CANDIDATES ONLY. EXECUTION AND ENFORCEMENT ARE UNVERIFIED.**

## Review scope

Secrets, credentials, API keys, tokens, environment-based secret injection, secret stores, masking, rotation and configuration boundaries without exposing secret values.

## Static observations

- Candidate files: **2622**
- Matching lines: **34727**

## Representative candidate files

- `AGENTS.md`
- `backend/AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic_tenants/versions/3b9f09038764_add_read_only_kg_user.py`
- `backend/alembic/versions/03d710ccf29c_add_permission_sync_attempt_tables.py`
- `backend/alembic/versions/0816326d83aa_add_federated_connector_tables.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/0cd424f32b1d_user_file_data_preparation_and_backfill.py`
- `backend/alembic/versions/0ebb1d516877_add_ccpair_deletion_failure_message.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/15326fcec57e_introduce_onyx_apis.py`
- `backend/alembic/versions/1b8206b29c5d_add_user_delete_cascades.py`
- `backend/alembic/versions/1cb59a95b250_add_security_settings_table.py`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- `backend/alembic/versions/1f2a3b4c5d6e_add_internet_search_and_content_providers.py`
- `backend/alembic/versions/1f60f60c3401_embedding_model_search_settings.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py`
- `backend/alembic/versions/20f09b642ed0_backfill_write_chat_for_limited_service_.py`
- `backend/alembic/versions/238b84885828_add_foreign_key_to_user__external_user_.py`

## Security interpretation

These are review candidates only.

Static matches do not prove:

- that a CI/CD workflow actually executes;
- that a discovered credential is real;
- that a dependency is vulnerable;
- that dependency pinning is complete;
- that an SBOM is actually produced;
- that signatures or attestations are verified;
- that provenance is trustworthy;
- that build permissions are least-privileged.

## Safety

- No workflow triggered.
- No secret value printed.
- No credential used.
- No package installed.
- No dependency scanner executed.
- No artifact uploaded.
- No artifact signed.
- No registry contacted.
- No cloud resource used.
- No paid service used.

## Result

Action 4.7 static mapping result: **PASS**
