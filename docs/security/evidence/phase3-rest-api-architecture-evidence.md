# Phase 3 Action 3.6 - REST/API Architecture Evidence

## Observation class

**STATIC SOURCE CANDIDATES ONLY. RUNTIME API BEHAVIOR IS UNVERIFIED.**

- Branch: `security/phase-3-foundations`
- HEAD: `73deb98b14d0f865d0bd011ba1b7e4fbd950bb05`
- Scanned text files: **7451**
- Skipped large files: **1**
- Skipped binary files: **194**

## Candidate summary

| Concept | Candidate files | Matching lines |
|---|---:|---:|
| routes | 807 | 2818 |
| http_methods | 2965 | 24656 |
| path_parameters | 3887 | 32785 |
| query_parameters | 307 | 1188 |
| request_schema | 1023 | 5497 |
| response_schema | 58 | 243 |
| versioning | 502 | 1704 |
| openapi_swagger | 104 | 578 |
| pagination | 535 | 2234 |
| status_errors | 1021 | 5486 |
| content_types | 311 | 707 |
| authentication | 1053 | 7018 |
| authorization | 1081 | 5030 |
| rate_limit | 193 | 504 |
| idempotency | 13 | 20 |
| webhook_callback | 20 | 39 |

## Representative candidate paths

### routes

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.greptile/config.json`
- `.greptile/rules.md`
- `AGENTS.md`
- `CLAUDE.md`
- `backend/alembic_tenants/versions/d4e7a92c1b38_add_tenant_invite_counter.py`
- `backend/ee/onyx/configs/app_configs.py`
- `backend/ee/onyx/connectors/perm_sync_valid.py`
- `backend/ee/onyx/db/scim.py`
- `backend/ee/onyx/external_permissions/box/access.py`
- `backend/ee/onyx/external_permissions/box/group_sync.py`
- `backend/ee/onyx/external_permissions/confluence/space_access.py`
- `backend/ee/onyx/external_permissions/jira/group_sync.py`
- `backend/ee/onyx/external_permissions/jira/page_access.py`
- `backend/ee/onyx/hooks/executor.py`
- `backend/ee/onyx/main.py`
- Limited to 20 of 807 candidate files.

### http_methods

- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/check-pr/references/gitlab-api.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/greptile/greploop/references/gitlab-api.md`
- `.cursor/skills/merge-dependabot-prs/SKILL.md`
- `.cursor/skills/merge-dependabot-prs/references/graphql-queries.md`
- `.cursor/skills/playwright/SKILL.md`
- `.cursor/skills/sync-vendored-skills.sh`
- `.devcontainer/Dockerfile`
- `.devcontainer/init-firewall.sh`
- `.devcontainer/zshrc`
- `.pre-commit-config.yaml`
- `.vscode/.env.k8s.template`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `.zed/tasks.json`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `README.md`
- Limited to 20 of 2965 candidate files.

### path_parameters

- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/check-pr/references/gitlab-api.md`
- `.cursor/skills/greptile/check-pr/references/graphql-queries.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/greptile/greploop/references/gitlab-api.md`
- `.cursor/skills/greptile/greploop/references/graphql-queries.md`
- `.cursor/skills/merge-dependabot-prs/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.cursor/skills/sync-vendored-skills.sh`
- `.devcontainer/Dockerfile`
- `.devcontainer/devcontainer.json`
- `.pre-commit-config.yaml`
- `.vscode/.env.k8s.template`
- `.vscode/env_template.txt`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `.zed/debug.json`
- `.zed/dotenv_launch.py`
- `.zed/tasks.json`
- `AGENTS.md`
- Limited to 20 of 3887 candidate files.

### query_parameters

- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/check-pr/references/graphql-queries.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/greptile/greploop/references/graphql-queries.md`
- `backend/alembic/versions/949b4a92a401_remove_rt.py`
- `backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py`
- `backend/ee/onyx/db/analytics.py`
- `backend/ee/onyx/db/connector.py`
- `backend/ee/onyx/db/connector_credential_pair.py`
- `backend/ee/onyx/db/document_set.py`
- `backend/ee/onyx/db/mcp.py`
- `backend/ee/onyx/db/persona.py`
- `backend/ee/onyx/db/query_history.py`
- `backend/ee/onyx/db/saml.py`
- `backend/ee/onyx/db/usage_export.py`
- `backend/ee/onyx/db/user_group.py`
- `backend/ee/onyx/db/user_tenant_mapping.py`
- `backend/ee/onyx/external_permissions/salesforce/utils.py`
- `backend/ee/onyx/server/features/hooks/api.py`
- `backend/ee/onyx/server/query_history/api.py`
- Limited to 20 of 307 candidate files.

### request_schema

- `.claude/claude-security-guidance.md`
- `.greptile/rules.md`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `.zed/tasks.json`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/alembic/README.md`
- `backend/alembic/env.py`
- `backend/alembic/run_multitenant_migrations.py`
- `backend/alembic/versions/0cd424f32b1d_user_file_data_preparation_and_backfill.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/2b75d0a8ffcb_user_file_schema_cleanup.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/31bd8c17325e_targeted_reindex_schema.py`
- `backend/alembic/versions/351faebd379d_add_curator_fields.py`
- `backend/alembic/versions/366c05b6f485_create_action_approval.py`
- `backend/alembic/versions/36e9220ab794_update_kg_trigger_functions.py`
- `backend/alembic/versions/47a07e1a38f1_fix_invalid_model_configurations_state.py`
- `backend/alembic/versions/495cb26ce93e_create_knowlege_graph_tables.py`
- Limited to 20 of 1023 candidate files.

### response_schema

- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/ee/onyx/server/evals/api.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/ee/onyx/server/gateway/api.py`
- `backend/ee/onyx/server/gateway/openai_passthrough.py`
- `backend/ee/onyx/server/middleware/license_enforcement.py`
- `backend/ee/onyx/server/middleware/tenant_tracking.py`
- `backend/ee/onyx/server/middleware/tier_gate.py`
- `backend/ee/onyx/server/oauth/api.py`
- `backend/ee/onyx/server/oauth/confluence_cloud.py`
- `backend/ee/onyx/server/oauth/google_drive.py`
- `backend/ee/onyx/server/oauth/slack.py`
- `backend/ee/onyx/server/query_and_chat/search_backend.py`
- `backend/ee/onyx/server/scim/api.py`
- `backend/onyx/auth/users.py`
- `backend/onyx/error_handling/exceptions.py`
- `backend/onyx/hooks/points/base.py`
- `backend/onyx/hooks/points/document_ingestion.py`
- `backend/onyx/hooks/points/document_push.py`
- Limited to 20 of 58 candidate files.

### versioning

- `.cursor/skills/greptile/greploop/SKILL.md`
- `README.md`
- `README.zh-CN.md`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/401c1ac29467_add_tables_for_ui_based_llm_.py`
- `backend/alembic/versions/5d12a446f5c0_add_api_version_and_deployment_name_to_.py`
- `backend/alembic/versions/9087b548dd69_seed_default_image_gen_config.py`
- `backend/ee/onyx/configs/license_enforcement_config.py`
- `backend/ee/onyx/main.py`
- `backend/ee/onyx/server/auth_check.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/ee/onyx/server/gateway/api.py`
- `backend/ee/onyx/server/gateway/openai_passthrough.py`
- `backend/ee/onyx/server/oauth/confluence_cloud.py`
- `backend/ee/onyx/server/oauth/google_drive.py`
- `backend/ee/onyx/server/oauth/slack.py`
- `backend/ee/onyx/server/scim/api.py`
- `backend/ee/onyx/server/scim/filtering.py`
- `backend/ee/onyx/server/scim/models.py`
- `backend/ee/onyx/server/scim/schema_definitions.py`
- Limited to 20 of 502 candidate files.

### openapi_swagger

- `.greptile/rules.md`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `.zed/tasks.json`
- `backend/ee/onyx/server/middleware/tenant_tracking.py`
- `backend/onyx/auth/permission_projection.py`
- `backend/onyx/auth/permissions.py`
- `backend/onyx/auth/users.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/connectors/document360/connector.py`
- `backend/onyx/connectors/notion/connector.py`
- `backend/onyx/db/models.py`
- `backend/onyx/db/tools.py`
- `backend/onyx/main.py`
- `backend/onyx/server/auth_check.py`
- `backend/onyx/server/features/mcp/models.py`
- `backend/onyx/server/features/tool/api.py`
- `backend/onyx/server/metrics/prometheus_setup.py`
- `backend/onyx/tools/tool_implementations/custom/custom_tool.py`
- `backend/onyx/tools/tool_implementations/custom/openapi_parsing.py`
- Limited to 20 of 104 candidate files.

### pagination

- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/check-pr/references/graphql-queries.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/greptile/greploop/references/graphql-queries.md`
- `.cursor/skills/sync-vendored-skills.sh`
- `.gitignore`
- `.vscode/env_template.txt`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/d3fd499c829c_add_file_reader_tool.py`
- `backend/alembic/versions/e3e324f5d32c_port_attempt_user_scope_and_userfile_.py`
- `backend/ee/onyx/db/query_history.py`
- `backend/ee/onyx/db/scim.py`
- `backend/ee/onyx/external_permissions/box/access.py`
- `backend/ee/onyx/external_permissions/box/group_sync.py`
- `backend/ee/onyx/external_permissions/sharepoint/permission_utils.py`
- `backend/ee/onyx/external_permissions/slack/doc_sync.py`
- `backend/ee/onyx/server/log_export/collection.py`
- `backend/ee/onyx/server/query_history/api.py`
- `backend/ee/onyx/server/scim/api.py`
- `backend/onyx/auth/login_claims_capture.py`
- Limited to 20 of 535 candidate files.

### status_errors

- `.cursor/skills/onyx-cli/SKILL.md`
- `.greptile/config.json`
- `.greptile/rules.md`
- `CONTRIBUTING.md`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/alembic/README.md`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/689433b0d8de_add_hook_and_hook_execution_log_tables.py`
- `backend/alembic/versions/e2875ce6454b_rename_python_tool_llm_facing_name.py`
- `backend/ee/onyx/auth/users.py`
- `backend/ee/onyx/connectors/perm_sync_valid.py`
- `backend/ee/onyx/db/query_history.py`
- `backend/ee/onyx/db/usage_export.py`
- `backend/ee/onyx/external_permissions/box/access.py`
- `backend/ee/onyx/external_permissions/box/group_sync.py`
- `backend/ee/onyx/external_permissions/canvas/access.py`
- `backend/ee/onyx/external_permissions/canvas/group_sync.py`
- `backend/ee/onyx/external_permissions/confluence/page_access.py`
- `backend/ee/onyx/external_permissions/confluence/space_access.py`
- Limited to 20 of 1021 candidate files.

### content_types

- `backend/ee/onyx/server/billing/service.py`
- `backend/ee/onyx/server/enterprise_settings/store.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/ee/onyx/server/gateway/openai_passthrough.py`
- `backend/ee/onyx/server/license/api.py`
- `backend/ee/onyx/server/log_export/storage.py`
- `backend/ee/onyx/server/oauth/confluence_cloud.py`
- `backend/ee/onyx/server/oauth/google_drive.py`
- `backend/ee/onyx/server/oauth/slack.py`
- `backend/ee/onyx/server/query_and_chat/search_backend.py`
- `backend/ee/onyx/server/scim/api.py`
- `backend/ee/onyx/server/tenant_usage_limits.py`
- `backend/ee/onyx/server/tenants/billing.py`
- `backend/ee/onyx/server/tenants/provisioning.py`
- `backend/ee/onyx/server/tenants/proxy.py`
- `backend/ee/onyx/utils/license.py`
- `backend/onyx/auth/jwt.py`
- `backend/onyx/auth/oauth_refresher.py`
- `backend/onyx/auth/oauth_token_manager.py`
- `backend/onyx/auth/users.py`
- Limited to 20 of 311 candidate files.

### authentication

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/cli-review/SKILL.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/Dockerfile`
- `.greptile/config.json`
- `.greptile/rules.md`
- `.vscode/env_template.txt`
- `README.md`
- `README.zh-CN.md`
- `backend/alembic/versions/03d085c5c38d_backfill_account_type.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/0d9c7b6a5e4f_retain_user_usage_after_user_deletion.py`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- `backend/alembic/versions/1f2a3b4c5d6e_add_internet_search_and_content_providers.py`
- `backend/alembic/versions/20f09b642ed0_backfill_write_chat_for_limited_service_.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/3a9b8d7c6e5f_add_mcp_known_provider_fields.py`
- `backend/alembic/versions/3c9a65f1207f_seed_exa_provider_from_env.py`
- `backend/alembic/versions/401c1ac29467_add_tables_for_ui_based_llm_.py`
- Limited to 20 of 1053 candidate files.

### authorization

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/LICENSE`
- `.cursor/skills/greptile/cli-review/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `LICENSE`
- `README.md`
- `README.zh-CN.md`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/alembic/versions/03d085c5c38d_backfill_account_type.py`
- `backend/alembic/versions/03d710ccf29c_add_permission_sync_attempt_tables.py`
- `backend/alembic/versions/1c36b3dc2f4e_add_full_exception_trace_to_permission_.py`
- `backend/alembic/versions/20f09b642ed0_backfill_write_chat_for_limited_service_.py`
- `backend/alembic/versions/25a5501dc766_group_permissions_phase1.py`
- `backend/alembic/versions/27c6ecc08586_permission_framework.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/351faebd379d_add_curator_fields.py`
- Limited to 20 of 1081 candidate files.

### rate_limit

- `.cursor/skills/merge-dependabot-prs/SKILL.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `backend/alembic/versions/703313b75876_add_tokenratelimit_tables.py`
- `backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py`
- `backend/ee/onyx/db/token_limit.py`
- `backend/ee/onyx/external_permissions/github/utils.py`
- `backend/ee/onyx/external_permissions/slack/doc_sync.py`
- `backend/ee/onyx/main.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/ee/onyx/server/gateway/api.py`
- `backend/ee/onyx/server/gateway/openai_passthrough.py`
- `backend/ee/onyx/server/token_rate_limits/api.py`
- `backend/model_server/encoders.py`
- `backend/model_server/main.py`
- `backend/model_server/utils.py`
- `backend/onyx/auth/signup_rate_limit.py`
- `backend/onyx/background/celery/celery_utils.py`
- `backend/onyx/background/celery/tasks/port/tasks.py`
- `backend/onyx/chat/models.py`
- `backend/onyx/configs/app_configs.py`
- Limited to 20 of 193 candidate files.

### idempotency

- `backend/ee/onyx/server/tenants/billing.py`
- `backend/ee/onyx/utils/license_notifications.py`
- `backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py`
- `backend/tests/external_dependency_unit/craft/test_sandbox_lifecycle.py`
- `backend/tests/external_dependency_unit/ee/onyx/utils/test_license_notifications.py`
- `backend/tests/external_dependency_unit/llm/test_llm_provider_auto_mode.py`
- `backend/tests/unit/ee/onyx/server/tenants/test_billing_seat_enforcement.py`
- `backend/tests/unit/onyx/tracing/test_tracing_setup.py`
- `docs/craft/craft-main-plan.md`
- `docs/craft/features/egress-proxy-and-approvals/README.md`
- `docs/mobile-chat/input-bar-controls/03-detailed-design.md`
- `docs/mobile-chat/input-bar-controls/04-implementation-plan.md`
- `docs/mobile-chat/input-bar-controls/05-pr-roadmap.md`

### webhook_callback

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `backend/ee/onyx/server/billing/api.py`
- `backend/ee/onyx/server/billing/service.py`
- `backend/ee/onyx/server/tenants/proxy.py`
- `backend/onyx/onyxbot/slack/handlers/handle_buttons.py`
- `backend/onyx/server/saml_multi.py`
- `backend/tests/integration/tests/mcp_oauth/test_mcp_oauth_cimd_integration.py`
- `backend/tests/unit/ee/onyx/server/billing/test_proxy.py`
- `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml`
- `deployment/helm/charts/onyx/values.yaml`
- `deployment/helm/dev/k8s-up.sh`
- `deployment/terraform/modules/azure/README.md`
- `deployment/terraform/modules/azure/aks/main.tf`
- `deployment/terraform/modules/azure/aks/outputs.tf`
- `deployment/terraform/modules/azure/aks/tests/aks.tftest.hcl`
- `web/lib/opal/src/icons/index.ts`
- `web/src/app/admin/billing/page.test.tsx`
- `web/src/app/admin/billing/page.tsx`
- `web/tests/e2e/chat/chat_message_rendering.spec.ts`

## Security interpretation

Static API discovery identifies candidate routes, parameters, schemas, authentication, authorization and abuse-control surfaces. It does not prove runtime reachability or correct security enforcement.

## Safety

- No API request was sent.
- No endpoint was contacted.
- No token or credential was tested.
- No webhook was invoked.
- No external service was contacted.
