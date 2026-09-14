# Phase 3 Action 3.3 - DNS, IP, Ports, Sockets, and Routing Evidence

## Observation class

**STATIC SOURCE CANDIDATES ONLY; RUNTIME NETWORK STATE UNVERIFIED.**

## Baseline

- Branch: `security/phase-3-foundations`
- HEAD: `87d56dc0a56f865bc483f4fcf12d8ca5a29f41e7`
- Scanned text files: **7451**
- Skipped large files: **1**
- Skipped binary files: **194**

## Candidate summary

| Concept | Candidate files | Matching lines |
|---|---:|---:|
| dns | 1172 | 5955 |
| ipv4 | 177 | 689 |
| ipv6 | 625 | 4477 |
| localhost | 238 | 593 |
| wildcard_bind | 80 | 126 |
| port | 1131 | 6888 |
| socket | 85 | 273 |
| listen_bind | 183 | 613 |
| routing | 852 | 3379 |
| proxy | 375 | 1568 |

## Representative candidate paths

### dns

- `.cursor/skills/greptile/README.md`
- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/check-pr/references/gitlab-api.md`
- `.cursor/skills/greptile/check-pr/references/graphql-queries.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/greptile/greploop/references/gitlab-api.md`
- `.cursor/skills/greptile/greploop/references/graphql-queries.md`
- `.cursor/skills/merge-dependabot-prs/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/Dockerfile`
- `.devcontainer/dnsmasq.conf`
- `.devcontainer/init-firewall.sh`
- `.pre-commit-config.yaml`
- `.vscode/.env.k8s.template`
- `.vscode/tasks.json`
- `.zed/dotenv_launch.py`
- `AGENTS.md`
- `CLAUDE.md`
- `SECURITY.md`
- `backend/Dockerfile`
- `backend/Dockerfile.model_server`
- `backend/alembic/env.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/31bd8c17325e_targeted_reindex_schema.py`
- `backend/alembic/versions/7a70b7664e37_add_model_configuration_table.py`
- `backend/alembic/versions/8f3b2c91d4e7_backfill_legacy_callback_on_seeded_sso_.py`
- `backend/alembic/versions/99ecd56cb2ce_scheduled_task_pre_approvals.py`
- `backend/alembic/versions/b7a7eee5aa15_add_checkpointing_failure_handling.py`
- `backend/alembic/versions/c7bc8cc2921d_drop_unused_kg_indexes.py`
- `backend/ee/onyx/auth/sso_domain_verification.py`
- `backend/ee/onyx/background/celery/tasks/cloud/tasks.py`
- `backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py`
- `backend/ee/onyx/configs/license_enforcement_config.py`
- `backend/ee/onyx/connectors/capability_checks.py`
- `backend/ee/onyx/db/persona.py`
- `backend/ee/onyx/db/scim.py`
- `backend/ee/onyx/db/tenant_sso_domain.py`
- `backend/ee/onyx/db/user_group.py`
- `backend/ee/onyx/db/user_tenant_mapping.py`
- `backend/ee/onyx/external_permissions/box/access.py`
- Display limited to 40 of 1172 files.

### ipv4

- `.devcontainer/dnsmasq.conf`
- `.devcontainer/init-firewall.sh`
- `.pre-commit-config.yaml`
- `backend/ee/onyx/server/scim/api.py`
- `backend/ee/onyx/server/scim/filtering.py`
- `backend/model_server/main.py`
- `backend/onyx/auth/users.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/configs/saml_config/template.settings.json`
- `backend/onyx/connectors/xenforo/connector.py`
- `backend/onyx/mcp_server/README.md`
- `backend/onyx/sandbox_proxy/addons/gate.py`
- `backend/onyx/sandbox_proxy/server.py`
- `backend/onyx/server/features/build/db/build_session.py`
- `backend/onyx/server/features/build/sandbox/README.md`
- `backend/onyx/server/features/build/sandbox/docker/dev_mode_serve.py`
- `backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py`
- `backend/onyx/server/features/build/sandbox/image/browser-cli.sh`
- `backend/onyx/server/features/build/sandbox/image/entrypoint.sh`
- `backend/onyx/server/features/build/sandbox/image/opencode-plugins/webapp.ts`
- `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py`
- `backend/onyx/server/features/build/sandbox/image/templates/outputs/web/public/window.svg`
- `backend/onyx/server/features/build/sandbox/nextjs_dev.py`
- `backend/onyx/server/metrics/metrics_server.py`
- `backend/onyx/server/security/models.py`
- `backend/onyx/skills/builtin/browser/SKILL.md`
- `backend/onyx/utils/playwright_fetch.py`
- `backend/onyx/utils/url.py`
- `backend/onyx/utils/variable_functionality.py`
- `backend/requirements/default.txt`
- `backend/requirements/dev.txt`
- `backend/requirements/model_server.txt`
- `backend/scripts/celery_purge_queue.py`
- `backend/scripts/restart_containers.sh`
- `backend/scripts/sources_selection_analysis.py`
- `backend/shared_configs/configs.py`
- `backend/tests/airgap/tls_failure_server.py`
- `backend/tests/external_dependency_unit/auth/test_jwt_passthrough.py`
- `backend/tests/external_dependency_unit/craft_helm/test_pod_spec.py`
- `backend/tests/external_dependency_unit/file_store/test_azure_blob_file_store.py`
- Display limited to 40 of 177 files.

### ipv6

- `backend/Dockerfile.model_server`
- `backend/alembic/versions/01c63968ff8f_add_ssrf_protection_level_to_security_.py`
- `backend/alembic/versions/01f8e6d95a33_populate_flow_mapping_data.py`
- `backend/alembic/versions/027381bce97c_add_shortcut_option_for_users.py`
- `backend/alembic/versions/03bf8be6b53a_rework_kg_config.py`
- `backend/alembic/versions/03d085c5c38d_backfill_account_type.py`
- `backend/alembic/versions/03d710ccf29c_add_permission_sync_attempt_tables.py`
- `backend/alembic/versions/0568ccf46a6b_add_thread_specific_model_selection.py`
- `backend/alembic/versions/05c07bf07c00_add_search_doc_relevance_details.py`
- `backend/alembic/versions/06a38a307492_add_chat_message_request_params.py`
- `backend/alembic/versions/07b98176f1de_code_interpreter_seed.py`
- `backend/alembic/versions/0816326d83aa_add_federated_connector_tables.py`
- `backend/alembic/versions/08a1eda20fe1_add_earliest_indexing_to_connector.py`
- `backend/alembic/versions/09995b8811eb_add_theme_preference_to_user.py`
- `backend/alembic/versions/0a2b51deb0b8_add_starter_prompts.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/0bb4558f35df_add_scim_username_to_scim_user_mapping.py`
- `backend/alembic/versions/0cd424f32b1d_user_file_data_preparation_and_backfill.py`
- `backend/alembic/versions/0d9c7b6a5e4f_retain_user_usage_after_user_deletion.py`
- `backend/alembic/versions/0df3c40e902a_drop_demo_data_enabled_from_build_.py`
- `backend/alembic/versions/0ebb1d516877_add_ccpair_deletion_failure_message.py`
- `backend/alembic/versions/0ec213a5ffde_add_incognito_record_mode_to_chat_.py`
- `backend/alembic/versions/0f7ff6d75b57_add_index_to_index_attempt_time_created.py`
- `backend/alembic/versions/114a638452db_add_default_app_mode_to_user.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/14162713706c_add_index_attempt_stage_metric_table.py`
- `backend/alembic/versions/15326fcec57e_introduce_onyx_apis.py`
- `backend/alembic/versions/16c37a30adf2_user_file_relationship_migration.py`
- `backend/alembic/versions/17135ac06582_add_incognito_to_user_usage.py`
- `backend/alembic/versions/173cae5bba26_port_config_store.py`
- `backend/alembic/versions/175ea04c7087_add_user_preferences.py`
- `backend/alembic/versions/177de57c21c9_display_custom_llm_models.py`
- `backend/alembic/versions/19c0ccb01687_migrate_to_contextual_rag_model.py`
- `backend/alembic/versions/1a03d2c2856b_add_indexes_to_document__tag.py`
- `backend/alembic/versions/1b10e1fda030_add_additional_data_to_notifications.py`
- `backend/alembic/versions/1b8206b29c5d_add_user_delete_cascades.py`
- `backend/alembic/versions/1c36b3dc2f4e_add_full_exception_trace_to_permission_.py`
- `backend/alembic/versions/1cb59a95b250_add_security_settings_table.py`
- `backend/alembic/versions/1d78c0ca7853_remove_voice_provider_deleted_column.py`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- Display limited to 40 of 625 files.

### localhost

- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/claude-code/CLAUDE.md`
- `.devcontainer/dnsmasq.conf`
- `.devcontainer/init-firewall.sh`
- `.vscode/.env.k8s.template`
- `.vscode/env_template.txt`
- `.vscode/launch.json`
- `.zed/debug.json`
- `.zed/tasks.json`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `backend/alembic.ini`
- `backend/ee/onyx/server/oauth/confluence_cloud.py`
- `backend/ee/onyx/server/oauth/google_drive.py`
- `backend/ee/onyx/server/oauth/slack.py`
- `backend/model_server/main.py`
- `backend/onyx/auth/users.py`
- `backend/onyx/background/celery/configs/base.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/configs/constants.py`
- `backend/onyx/configs/saml_config/template.settings.json`
- `backend/onyx/document_index/vespa_constants.py`
- `backend/onyx/file_store/README.md`
- `backend/onyx/llm/multi_llm.py`
- `backend/onyx/mcp_server/README.md`
- `backend/onyx/server/features/build/AGENTS.template.md`
- `backend/onyx/server/features/build/sandbox/base.py`
- `backend/onyx/server/features/build/sandbox/docker/dev_mode_serve.py`
- `backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py`
- `backend/onyx/server/features/build/sandbox/image/browser-cli.sh`
- `backend/onyx/server/features/build/sandbox/image/opencode-plugins/webapp.ts`
- `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py`
- `backend/onyx/server/features/build/sandbox/nextjs_dev.py`
- `backend/onyx/server/features/build/session/models.py`
- `backend/onyx/server/features/mcp/api.py`
- `backend/onyx/server/settings/models.py`
- `backend/onyx/skills/builtin/browser/SKILL.md`
- `backend/onyx/tools/tool_implementations/custom/custom_tool.py`
- `backend/onyx/utils/client_ip.py`
- Display limited to 40 of 238 files.

### wildcard_bind

- `backend/model_server/main.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/sandbox_proxy/server.py`
- `backend/onyx/server/features/build/db/build_session.py`
- `backend/onyx/server/features/build/sandbox/docker/dev_mode_serve.py`
- `backend/onyx/server/features/build/sandbox/image/entrypoint.sh`
- `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py`
- `backend/onyx/server/features/build/sandbox/nextjs_dev.py`
- `backend/onyx/server/metrics/metrics_server.py`
- `backend/onyx/utils/url.py`
- `backend/scripts/restart_containers.sh`
- `backend/shared_configs/configs.py`
- `backend/tests/airgap/tls_failure_server.py`
- `backend/tests/external_dependency_unit/file_store/test_azure_blob_file_store.py`
- `backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_api_key.py`
- `backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_no_auth.py`
- `backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_per_user_key.py`
- `backend/tests/integration/mock_services/mcp_test_server/run_mock_oidc_idp.py`
- `backend/tests/integration/mock_services/mock_connector_server/Dockerfile`
- `backend/tests/integration/tests/mcp_oauth/conftest.py`
- `backend/tests/integration/tests/pruning/test_pruning.py`
- `backend/tests/unit/onyx/server/features/craft/sandbox/test_docker_manager_config.py`
- `backend/tests/unit/onyx/server/features/craft/sandbox/test_docker_serve_plumbing.py`
- `backend/tests/unit/onyx/server/features/craft/test_nextjs_dev.py`
- `backend/tests/unit/onyx/server/features/mcp/test_mcp_ssrf.py`
- `backend/tests/unit/onyx/utils/test_url_ssrf.py`
- `backend/tests/unit/server/metrics/test_metrics_server.py`
- `cli/README.md`
- `cli/cmd/serve.go`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.craft.yml`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml`
- `cli/internal/deploy/install/dev_test.go`
- `cli/internal/deploy/install/lifecycle_test.go`
- `cli/internal/deploy/install/status.go`
- `cli/internal/deploy/install/upgrade_test.go`
- `deployment/aws_ecs_fargate/cloudformation/onyx_efs_template.yaml`
- `deployment/aws_ecs_fargate/cloudformation/services/onyx_backend_api_server_service_template.yaml`
- `deployment/aws_ecs_fargate/cloudformation/services/onyx_backend_background_server_service_template.yaml`
- Display limited to 40 of 80 files.

### port

- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/Dockerfile`
- `.devcontainer/claude-code/CLAUDE.md`
- `.devcontainer/devcontainer.json`
- `.devcontainer/init-firewall.sh`
- `.vscode/.env.k8s.template`
- `.vscode/env_template.txt`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `.zed/debug.json`
- `.zed/tasks.json`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `backend/Dockerfile.model_server`
- `backend/alembic/env.py`
- `backend/alembic/versions/01c63968ff8f_add_ssrf_protection_level_to_security_.py`
- `backend/alembic/versions/01f8e6d95a33_populate_flow_mapping_data.py`
- `backend/alembic/versions/027381bce97c_add_shortcut_option_for_users.py`
- `backend/alembic/versions/03bf8be6b53a_rework_kg_config.py`
- `backend/alembic/versions/03d710ccf29c_add_permission_sync_attempt_tables.py`
- `backend/alembic/versions/0568ccf46a6b_add_thread_specific_model_selection.py`
- `backend/alembic/versions/05c07bf07c00_add_search_doc_relevance_details.py`
- `backend/alembic/versions/06a38a307492_add_chat_message_request_params.py`
- `backend/alembic/versions/07b98176f1de_code_interpreter_seed.py`
- `backend/alembic/versions/0816326d83aa_add_federated_connector_tables.py`
- `backend/alembic/versions/08a1eda20fe1_add_earliest_indexing_to_connector.py`
- `backend/alembic/versions/09995b8811eb_add_theme_preference_to_user.py`
- `backend/alembic/versions/0a2b51deb0b8_add_starter_prompts.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/0bb4558f35df_add_scim_username_to_scim_user_mapping.py`
- `backend/alembic/versions/0cd424f32b1d_user_file_data_preparation_and_backfill.py`
- `backend/alembic/versions/0df3c40e902a_drop_demo_data_enabled_from_build_.py`
- `backend/alembic/versions/0ebb1d516877_add_ccpair_deletion_failure_message.py`
- `backend/alembic/versions/0ec213a5ffde_add_incognito_record_mode_to_chat_.py`
- `backend/alembic/versions/0f7ff6d75b57_add_index_to_index_attempt_time_created.py`
- `backend/alembic/versions/114a638452db_add_default_app_mode_to_user.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/14162713706c_add_index_attempt_stage_metric_table.py`
- Display limited to 40 of 1131 files.

### socket

- `backend/ee/onyx/server/log_export/collection.py`
- `backend/ee/onyx/server/log_export/storage.py`
- `backend/ee/onyx/server/middleware/license_enforcement.py`
- `backend/ee/onyx/utils/license.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/configs/chat_configs.py`
- `backend/onyx/configs/constants.py`
- `backend/onyx/connectors/google_utils/google_utils.py`
- `backend/onyx/connectors/sharepoint/connector.py`
- `backend/onyx/connectors/web/connector.py`
- `backend/onyx/db/engine/sql_engine.py`
- `backend/onyx/llm/multi_llm.py`
- `backend/onyx/onyxbot/slack/listener.py`
- `backend/onyx/redis/redis_pool.py`
- `backend/onyx/sandbox_proxy/addons/gate.py`
- `backend/onyx/sandbox_proxy/identity_docker.py`
- `backend/onyx/server/features/build/AGENTS.template.md`
- `backend/onyx/server/features/build/db/build_session.py`
- `backend/onyx/server/features/build/sandbox/README.md`
- `backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py`
- `backend/onyx/server/features/build/sandbox/docker/internal/exec_helpers.py`
- `backend/onyx/server/features/build/sandbox/image/firewall-init.sh`
- `backend/onyx/server/features/build/sandbox/kubernetes/k8s_client.py`
- `backend/onyx/server/manage/voice/websocket_api.py`
- `backend/onyx/server/metrics/metrics_server.py`
- `backend/onyx/skills/builtin/browser/SKILL.md`
- `backend/onyx/skills/builtin/pptx/scripts/office/soffice.py`
- `backend/onyx/utils/url.py`
- `backend/onyx/voice/providers/elevenlabs.py`
- `backend/onyx/voice/providers/openai.py`
- `backend/tests/airgap/tls_failure_server.py`
- `backend/tests/external_dependency_unit/file_store/test_azure_blob_file_store.py`
- `backend/tests/external_dependency_unit/sandbox_proxy/test_identity_docker_lookup.py`
- `backend/tests/external_dependency_unit/voice/test_openai_streaming.py`
- `backend/tests/integration/tests/craft/docker_e2e/test_sandbox_network_posture_docker.py`
- `backend/tests/integration/tests/gateway_clients/README.md`
- `backend/tests/integration/tests/gateway_clients/conftest.py`
- `backend/tests/integration/tests/mcp/test_craft_mcp_servers.py`
- `backend/tests/integration/tests/mcp/test_mcp_client_no_auth_flow.py`
- `backend/tests/integration/tests/mcp_oauth/conftest.py`
- Display limited to 40 of 85 files.

### listen_bind

- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/devcontainer.json`
- `.devcontainer/dnsmasq.conf`
- `.devcontainer/init-dev-user.sh`
- `.devcontainer/zshrc`
- `backend/alembic/env.py`
- `backend/alembic/versions/0cd424f32b1d_user_file_data_preparation_and_backfill.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/16c37a30adf2_user_file_relationship_migration.py`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/2b75d0a8ffcb_user_file_schema_cleanup.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/3350a25df58e_add_sheets_and_slides_hosts_to_google_.py`
- `backend/alembic/versions/36e9220ab794_update_kg_trigger_functions.py`
- `backend/alembic/versions/3a78dba1080a_user_file_legacy_data_cleanup.py`
- `backend/alembic/versions/3c9a65f1207f_seed_exa_provider_from_env.py`
- `backend/alembic/versions/3debc2b55899_durable_craft_provisioning_lifecycle.py`
- `backend/alembic/versions/4ee1287bd26a_add_multiple_slack_bot_support.py`
- `backend/alembic/versions/7547d982db8f_chat_folders.py`
- `backend/alembic/versions/7cc3fcc116c1_user_file_uuid_primary_key_swap.py`
- `backend/alembic/versions/8f3b2c91d4e7_backfill_legacy_callback_on_seeded_sso_.py`
- `backend/alembic/versions/90e3b9af7da4_tag_fix.py`
- `backend/alembic/versions/949b4a92a401_remove_rt.py`
- `backend/alembic/versions/989bc57562e4_seed_browser_built_in_skill.py`
- `backend/alembic/versions/9b66d3156fc6_user_file_schema_additions.py`
- `backend/alembic/versions/b156fa702355_chat_reworked.py`
- `backend/alembic/versions/b30353be4eec_add_mcp_auth_performer.py`
- `backend/alembic/versions/c5d9662b3c50_seed_craft_documentation_built_in_skill.py`
- `backend/alembic/versions/c9e2cd766c29_add_s3_file_store_table.py`
- `backend/alembic/versions/e0ea2ae62e51_add_index_on_chat_session_user_id_and_.py`
- `backend/alembic/versions/e8f0d2a38171_add_status_to_mcp_server_and_make_auth_.py`
- `backend/alembic/versions/ea9771dd828c_associate_external_apps_with_skills.py`
- `backend/alembic/versions/f3a9c1d4b7e2_provision_built_in_external_apps.py`
- `backend/alembic/versions/f57f35403f6c_add_index_on_chat_message_chat_session_.py`
- `backend/ee/onyx/background/celery/tasks/cloud/tasks.py`
- `backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py`
- `backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py`
- `backend/ee/onyx/background/celery/tasks/query_history/tasks.py`
- Display limited to 40 of 183 files.

### routing

- `.claude/claude-security-guidance.md`
- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/Dockerfile`
- `.devcontainer/claude-code/CLAUDE.md`
- `.devcontainer/init-firewall.sh`
- `.greptile/config.json`
- `.greptile/rules.md`
- `.vscode/.env.k8s.template`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/alembic_tenants/versions/b1c4e9d72f38_add_tenant_shard_map.py`
- `backend/ee/onyx/auth/sso_domain_verification.py`
- `backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py`
- `backend/ee/onyx/configs/license_enforcement_config.py`
- `backend/ee/onyx/connectors/capability_checks.py`
- `backend/ee/onyx/db/analytics.py`
- `backend/ee/onyx/db/scim.py`
- `backend/ee/onyx/db/standard_answer.py`
- `backend/ee/onyx/db/tenant_sso_domain.py`
- `backend/ee/onyx/db/user_group.py`
- `backend/ee/onyx/external_permissions/slack/doc_sync.py`
- `backend/ee/onyx/main.py`
- `backend/ee/onyx/server/analytics/api.py`
- `backend/ee/onyx/server/billing/api.py`
- `backend/ee/onyx/server/billing/service.py`
- `backend/ee/onyx/server/documents/cc_pair.py`
- `backend/ee/onyx/server/enterprise_settings/api.py`
- `backend/ee/onyx/server/evals/api.py`
- `backend/ee/onyx/server/features/hooks/api.py`
- `backend/ee/onyx/server/gateway/__init__.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/ee/onyx/server/gateway/api.py`
- `backend/ee/onyx/server/gateway/openai_passthrough.py`
- `backend/ee/onyx/server/gateway/stream_bridge.py`
- `backend/ee/onyx/server/license/api.py`
- `backend/ee/onyx/server/log_export/api.py`
- `backend/ee/onyx/server/manage/standard_answer.py`
- Display limited to 40 of 852 files.

### proxy

- `.cursor/skills/merge-dependabot-prs/SKILL.md`
- `.cursor/skills/sync-vendored-skills.sh`
- `.devcontainer/claude-code/CLAUDE.md`
- `.devcontainer/dnsmasq.conf`
- `.devcontainer/init-firewall.sh`
- `.greptile/config.json`
- `.vscode/.env.k8s.template`
- `.vscode/tasks.json`
- `Makefile`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/alembic/versions/ba98eba0f66a_add_support_for_litellm_proxy_in_.py`
- `backend/alembic/versions/df0c7ad8a076_added_deletion_attempt_table.py`
- `backend/alembic/versions/f3a9c1d4b7e2_provision_built_in_external_apps.py`
- `backend/ee/onyx/configs/app_configs.py`
- `backend/ee/onyx/configs/license_enforcement_config.py`
- `backend/ee/onyx/external_permissions/sharepoint/permission_utils.py`
- `backend/ee/onyx/server/auth_check.py`
- `backend/ee/onyx/server/billing/api.py`
- `backend/ee/onyx/server/billing/service.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/ee/onyx/server/gateway/api.py`
- `backend/ee/onyx/server/gateway/openai_passthrough.py`
- `backend/ee/onyx/server/gateway/stream_bridge.py`
- `backend/ee/onyx/server/license/api.py`
- `backend/ee/onyx/server/tenants/api.py`
- `backend/ee/onyx/server/tenants/billing.py`
- `backend/ee/onyx/server/tenants/proxy.py`
- `backend/ee/onyx/utils/license.py`
- `backend/onyx/auth/users.py`
- `backend/onyx/background/celery/tasks/docfetching/tasks.py`
- `backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py`
- `backend/onyx/background/celery/tasks/monitoring/tasks.py`
- `backend/onyx/background/indexing/run_targeted_reindex.py`
- `backend/onyx/chat/incognito.py`
- `backend/onyx/chat/llm_loop.py`
- `backend/onyx/chat/process_message.py`
- `backend/onyx/chat/save_chat.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/configs/chat_configs.py`
- Display limited to 40 of 375 files.

## Security interpretation

DNS candidates identify potential name-resolution surfaces. IP and bind-address candidates identify possible addressing and exposure decisions. Port and socket candidates identify possible transport endpoints. Routing and proxy candidates identify possible traffic-flow and trust-boundary transitions.

None of these static observations prove that an address is assigned, a port is listening, a socket is reachable, DNS resolves as shown, or a route/proxy is active at runtime.

## Safety

- No DNS lookup was performed.
- No port scan was performed.
- No socket connection was opened.
- No service was contacted.
- No external network testing occurred.
