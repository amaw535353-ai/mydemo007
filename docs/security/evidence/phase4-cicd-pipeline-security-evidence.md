# Phase 4 Action 4.6 - CI/CD Pipeline Security Foundations Evidence

## Provenance

- Branch: `security/phase-4-cloud-devsecops`
- Baseline HEAD: `e620a9baf8af9dd3b5833e7f08f6ec45da9b4229`

## Observation class

**STATIC SOURCE CANDIDATES ONLY. EXECUTION AND ENFORCEMENT ARE UNVERIFIED.**

## Review scope

CI/CD workflows, triggers, runners, workflow permissions, actions, artifacts, environment protection, OIDC, deployment jobs and untrusted pull-request/build-input boundaries.

## Static observations

- Candidate files: **1204**
- Matching lines: **5904**

## Representative candidate files

- `backend/AGENTS.md`
- `backend/alembic.ini`
- `backend/alembic/README.md`
- `backend/alembic_tenants/versions/b1c4e9d72f38_add_tenant_shard_map.py`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py`
- `backend/alembic/versions/28429dd43807_scheduled_tasks.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/34fe28843029_craft_artifact_index_and_receipts.py`
- `backend/alembic/versions/5d12a446f5c0_add_api_version_and_deployment_name_to_.py`
- `backend/alembic/versions/77962d18fd41_add_run_id_to_credential_capability_.py`
- `backend/alembic/versions/7f5b159041be_skill_built_in_id_discriminator.py`
- `backend/alembic/versions/856bcbe14d79_add_missing_fk_indexes_for_hot_tables.py`
- `backend/alembic/versions/8f3b2c91d4e7_backfill_legacy_callback_on_seeded_sso_.py`
- `backend/alembic/versions/9087b548dd69_seed_default_image_gen_config.py`
- `backend/alembic/versions/989bc57562e4_seed_browser_built_in_skill.py`
- `backend/alembic/versions/bc9e56f2fb96_polymorphic_gated_app.py`
- `backend/alembic/versions/c5d9662b3c50_seed_craft_documentation_built_in_skill.py`
- `backend/alembic/versions/c71a18ea7d07_add_is_manager_and_is_group_manager.py`

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

Action 4.6 static mapping result: **PASS**
