# Phase 3 Action 3.12 - Apply Foundations to mydemo007

## Observation class

**STATIC SOURCE MAPPING ONLY. RUNTIME SECURITY BEHAVIOR IS UNVERIFIED.**

- Branch: `security/phase-3-foundations`
- Baseline HEAD: `496f418006a6b3b7e731a25087d4530c9d8e0ffd`

## Integrated security-surface map

| Surface | Candidate files | Matching lines | Security question |
|---|---:|---:|---|
| Web and API entry points | 1612 | 9747 | Which inputs cross from an untrusted client into application logic? |
| Authentication | 1406 | 12666 | How is identity established and validated? |
| Sessions and tokens | 1881 | 38722 | How is authenticated state stored, transported, expired and revoked? |
| Authorization and ownership | 1665 | 13508 | Where are function-level and object-level access decisions enforced? |
| Tenant and organizational boundaries | 1323 | 13425 | Which identifiers participate in isolation between security domains? |
| Data access and persistence | 2546 | 35643 | Which components read or write security-sensitive state? |
| Downstream and external integrations | 2268 | 17364 | Where can data or authority cross into another service? |
| Cryptography and secrets | 1708 | 29486 | Where are confidentiality, integrity, signing or secret-management controls expected? |
| Deployment and transport controls | 747 | 7074 | Which deployment layers affect trust, transport and exposure? |
| Logging and error handling | 3391 | 34743 | Could errors or telemetry expose sensitive security context? |

### Web and API entry points

- `AGENTS.md`
- `backend/AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic_tenants/versions/d4e7a92c1b38_add_tenant_invite_counter.py`
- `backend/alembic/versions/01f8e6d95a33_populate_flow_mapping_data.py`
- `backend/alembic/versions/03bf8be6b53a_rework_kg_config.py`
- `backend/alembic/versions/07b98176f1de_code_interpreter_seed.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/0d9c7b6a5e4f_retain_user_usage_after_user_deletion.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/14162713706c_add_index_attempt_stage_metric_table.py`
- `backend/alembic/versions/16c37a30adf2_user_file_relationship_migration.py`

### Authentication

- `AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic_tenants/versions/3b9f09038764_add_read_only_kg_user.py`
- `backend/alembic_tenants/versions/8f3d2c7b91ae_add_user_tenant_mapping_oauth_account.py`
- `backend/alembic/versions/0816326d83aa_add_federated_connector_tables.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/1cb59a95b250_add_security_settings_table.py`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- `backend/alembic/versions/1f2a3b4c5d6e_add_internet_search_and_content_providers.py`
- `backend/alembic/versions/1f60f60c3401_embedding_model_search_settings.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/20f09b642ed0_backfill_write_chat_for_limited_service_.py`

### Sessions and tokens

- `backend/alembic/env.py`
- `backend/alembic_tenants/versions/b1c4e9d72f38_add_tenant_shard_map.py`
- `backend/alembic/versions/0568ccf46a6b_add_thread_specific_model_selection.py`
- `backend/alembic/versions/0cd424f32b1d_user_file_data_preparation_and_backfill.py`
- `backend/alembic/versions/0df3c40e902a_drop_demo_data_enabled_from_build_.py`
- `backend/alembic/versions/0ec213a5ffde_add_incognito_record_mode_to_chat_.py`
- `backend/alembic/versions/16c37a30adf2_user_file_relationship_migration.py`
- `backend/alembic/versions/1b8206b29c5d_add_user_delete_cascades.py`
- `backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py`
- `backend/alembic/versions/2666d766cb9b_google_oauth2.py`
- `backend/alembic/versions/28429dd43807_scheduled_tasks.py`
- `backend/alembic/versions/2b75d0a8ffcb_user_file_schema_cleanup.py`

### Authorization and ownership

- `backend/AGENTS.md`
- `backend/alembic_tenants/versions/3b9f09038764_add_read_only_kg_user.py`
- `backend/alembic/versions/03d085c5c38d_backfill_account_type.py`
- `backend/alembic/versions/03d710ccf29c_add_permission_sync_attempt_tables.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/1c36b3dc2f4e_add_full_exception_trace_to_permission_.py`
- `backend/alembic/versions/20f09b642ed0_backfill_write_chat_for_limited_service_.py`
- `backend/alembic/versions/25a5501dc766_group_permissions_phase1.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/351faebd379d_add_curator_fields.py`
- `backend/alembic/versions/39287906b97a_external_app_action_policies.py`
- `backend/alembic/versions/3a9b8d7c6e5f_add_mcp_known_provider_fields.py`

### Tenant and organizational boundaries

- `backend/AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic.ini`
- `backend/alembic/README.md`
- `backend/alembic/run_multitenant_migrations.py`
- `backend/alembic_tenants/versions/14a83a331951_create_usertenantmapping_table.py`
- `backend/alembic_tenants/versions/34e3630c7f32_lowercase_multi_tenant_user_auth.py`
- `backend/alembic_tenants/versions/3b45e0018bf1_add_new_available_tenant_table.py`
- `backend/alembic_tenants/versions/8f3d2c7b91ae_add_user_tenant_mapping_oauth_account.py`
- `backend/alembic_tenants/versions/a4f6ee863c47_mapping_for_anonymous_user_path.py`
- `backend/alembic_tenants/versions/a754e4f72e60_add_tenant_sso_domain_routing.py`
- `backend/alembic_tenants/versions/ac842f85f932_new_column_user_tenant_mapping.py`

### Data access and persistence

- `AGENTS.md`
- `backend/AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic.ini`
- `backend/alembic/README.md`
- `backend/alembic/run_multitenant_migrations.py`
- `backend/alembic/script.py.mako`
- `backend/alembic_tenants/env.py`
- `backend/alembic_tenants/script.py.mako`
- `backend/alembic_tenants/versions/14a83a331951_create_usertenantmapping_table.py`
- `backend/alembic_tenants/versions/3b45e0018bf1_add_new_available_tenant_table.py`
- `backend/alembic_tenants/versions/3b9f09038764_add_read_only_kg_user.py`

### Downstream and external integrations

- `AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic/README.md`
- `backend/alembic_tenants/env.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/3350a25df58e_add_sheets_and_slides_hosts_to_google_.py`
- `backend/alembic/versions/46625e4745d4_remove_native_enum.py`
- `backend/alembic/versions/77d07dffae64_forcibly_remove_more_enum_types_from_.py`
- `backend/alembic/versions/8f3b2c91d4e7_backfill_legacy_callback_on_seeded_sso_.py`
- `backend/alembic/versions/90e3b9af7da4_tag_fix.py`

### Cryptography and secrets

- `AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic/versions/0816326d83aa_add_federated_connector_tables.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/2666d766cb9b_google_oauth2.py`
- `backend/alembic/versions/287021f3b46c_add_voice_provider_api_secret.py`
- `backend/alembic/versions/2c7f9d3a84a0_add_pat_type_and_encrypted_pat.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/3a9b8d7c6e5f_add_mcp_known_provider_fields.py`

### Deployment and transport controls

- `AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic_tenants/env.py`
- `backend/alembic/versions/ba98eba0f66a_add_support_for_litellm_proxy_in_.py`
- `backend/Dockerfile`
- `backend/Dockerfile.model_server`
- `backend/ee/LICENSE`
- `backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py`
- `backend/ee/onyx/configs/app_configs.py`
- `backend/ee/onyx/configs/license_enforcement_config.py`
- `backend/ee/onyx/external_permissions/sharepoint/permission_utils.py`
- `backend/ee/onyx/server/auth_check.py`

### Logging and error handling

- `AGENTS.md`
- `backend/AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic.ini`
- `backend/alembic/README.md`
- `backend/alembic/run_multitenant_migrations.py`
- `backend/alembic_tenants/env.py`
- `backend/alembic_tenants/versions/3b9f09038764_add_read_only_kg_user.py`
- `backend/alembic/versions/03d710ccf29c_add_permission_sync_attempt_tables.py`
- `backend/alembic/versions/0cd424f32b1d_user_file_data_preparation_and_backfill.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/16c37a30adf2_user_file_relationship_migration.py`
## Integrated security reasoning
The important engineering question is not whether a security-related
keyword exists. The important question is how untrusted input, identity,
authority and sensitive data move through the system.
A later runtime review must trace representative requests from ingress
through authentication, authorization, business logic, persistence and
downstream integrations.
## Required controlled verification later
- Confirm real route reachability.
- Confirm authentication requirements.
- Confirm session/token lifecycle.
- Confirm function-level authorization.
- Confirm object ownership enforcement.
- Confirm tenant isolation.
- Confirm input validation and state transitions.
- Confirm sensitive-data handling.
- Confirm transport assumptions.
- Confirm cryptographic validation.
- Confirm safe logging and error behavior.
## Safety
- No runtime request was sent.
- No identity was impersonated.
- No authorization bypass was attempted.
- No credential or token was used.
- No cross-tenant access was attempted.
- No external service was contacted.
- No secret contents were displayed.
