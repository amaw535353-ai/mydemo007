# Phase 3 Action 3.5 - Web Request/Response Lifecycle Evidence

## Observation class

**STATIC SOURCE CANDIDATES ONLY. RUNTIME REQUEST FLOW IS UNVERIFIED.**

## Baseline

- Branch: `security/phase-3-foundations`
- HEAD: `03428967f450de4dbcedf20f1033fbb2f74de4fc`
- Scanned text files: **7451**
- Skipped large files: **1**
- Skipped binary files: **194**

## Lifecycle candidate summary

| Stage | Candidate files | Matching lines |
|---|---:|---:|
| routes_endpoints | 2087 | 11650 |
| request | 1171 | 6983 |
| response | 1264 | 11680 |
| middleware | 62 | 220 |
| authentication | 617 | 2262 |
| authorization | 1117 | 5249 |
| validation | 1143 | 4170 |
| session_cookie | 1328 | 10892 |
| data_access | 1226 | 6039 |
| downstream_service | 2111 | 9897 |
| error_handling | 2550 | 16376 |
| serialization | 1321 | 7314 |

## Representative candidate paths

### routes_endpoints

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/check-pr/references/gitlab-api.md`
- `.cursor/skills/greptile/check-pr/references/graphql-queries.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/greptile/greploop/references/gitlab-api.md`
- `.cursor/skills/greptile/greploop/references/graphql-queries.md`
- `.cursor/skills/merge-dependabot-prs/references/graphql-queries.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/claude-code/CLAUDE.md`
- `.devcontainer/dnsmasq.conf`
- `.devcontainer/init-firewall.sh`
- `.greptile/config.json`
- `.greptile/rules.md`
- `.mcp.json`
- `.vscode/.env.k8s.template`
- `.vscode/env_template.txt`
- Limited to 20 of 2087 candidate files.

### request

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/check-pr/references/gitlab-api.md`
- `.cursor/skills/greptile/check-pr/references/graphql-queries.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/greptile/greploop/references/graphql-queries.md`
- `.cursor/skills/merge-dependabot-prs/references/graphql-queries.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.greptile/rules.md`
- `.vscode/launch.json`
- `.zed/debug.json`
- `.zed/dotenv_launch.py`
- `CONTRIBUTING.md`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/alembic/versions/06a38a307492_add_chat_message_request_params.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/4d545225fd82_action_approval_multi_action_shape.py`
- `backend/alembic/versions/81c22b1e2e78_hierarchy_nodes_v1.py`
- Limited to 20 of 1171 candidate files.

### response

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/check-pr/references/gitlab-api.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/greptile/greploop/references/gitlab-api.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.greptile/rules.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/5e6f7a8b9c0d_update_default_persona_prompt.py`
- `backend/alembic/versions/7e490836d179_nullify_default_system_prompt.py`
- `backend/alembic/versions/87c52ec39f84_update_default_system_prompt.py`
- `backend/alembic/versions/90e3b9af7da4_tag_fix.py`
- `backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py`
- `backend/ee/onyx/db/analytics.py`
- `backend/ee/onyx/db/license.py`
- `backend/ee/onyx/external_permissions/confluence/constants.py`
- Limited to 20 of 1264 candidate files.

### middleware

- `.claude/claude-security-guidance.md`
- `backend/Dockerfile.model_server`
- `backend/ee/onyx/configs/license_enforcement_config.py`
- `backend/ee/onyx/configs/multi_tenant_gating_config.py`
- `backend/ee/onyx/db/license.py`
- `backend/ee/onyx/main.py`
- `backend/ee/onyx/server/enterprise_settings/api.py`
- `backend/ee/onyx/server/metrics/license_metrics.py`
- `backend/ee/onyx/server/middleware/license_enforcement.py`
- `backend/ee/onyx/server/middleware/tenant_tracking.py`
- `backend/ee/onyx/server/middleware/tier_gate.py`
- `backend/ee/onyx/server/scim/auth.py`
- `backend/ee/onyx/utils/license.py`
- `backend/model_server/main.py`
- `backend/onyx/auth/users.py`
- `backend/onyx/background/celery/tasks/docprocessing/tasks.py`
- `backend/onyx/background/indexing/run_targeted_reindex.py`
- `backend/onyx/main.py`
- `backend/onyx/mcp_server/api.py`
- `backend/onyx/server/auth/captcha_api.py`
- Limited to 20 of 62 candidate files.

### authentication

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/README.md`
- `.cursor/skills/greptile/check-pr/references/graphql-queries.md`
- `.cursor/skills/greptile/cli-review/SKILL.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/greptile/greploop/references/graphql-queries.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/Dockerfile`
- `.greptile/rules.md`
- `.vscode/env_template.txt`
- `AGENTS.md`
- `CLAUDE.md`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/f3a9c1d4b7e2_provision_built_in_external_apps.py`
- `backend/alembic/versions/f7ca3e2f45d9_migrate_no_auth_data_to_placeholder.py`
- `backend/ee/onyx/auth/users.py`
- `backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py`
- Limited to 20 of 617 candidate files.

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
- Limited to 20 of 1117 candidate files.

### validation

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/cli-review/SKILL.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.cursor/skills/sync-vendored-skills.sh`
- `.devcontainer/init-firewall.sh`
- `.greptile/rules.md`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `.zed/tasks.json`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/alembic/README.md`
- `backend/alembic/env.py`
- `backend/alembic/run_multitenant_migrations.py`
- `backend/alembic/versions/0cd424f32b1d_user_file_data_preparation_and_backfill.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/2b75d0a8ffcb_user_file_schema_cleanup.py`
- Limited to 20 of 1143 candidate files.

### session_cookie

- `.claude/claude-security-guidance.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/README.md`
- `.greptile/rules.md`
- `.zed/debug.json`
- `CONTRIBUTING.md`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/alembic/env.py`
- `backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py`
- `backend/alembic/versions/28429dd43807_scheduled_tasks.py`
- `backend/alembic/versions/2f80c6a2550f_add_chat_session_specific_temperature_.py`
- `backend/alembic/versions/34fe28843029_craft_artifact_index_and_receipts.py`
- `backend/alembic/versions/36e9220ab794_update_kg_trigger_functions.py`
- `backend/alembic/versions/38eda64af7fe_add_chat_session_sharing.py`
- `backend/alembic/versions/3debc2b55899_durable_craft_provisioning_lifecycle.py`
- `backend/alembic/versions/4ee1287bd26a_add_multiple_slack_bot_support.py`
- `backend/alembic/versions/505c488f6662_merge_default_assistants_into_unified.py`
- `backend/alembic/versions/80696cf850ae_add_chat_session_to_query_event.py`
- Limited to 20 of 1328 candidate files.

### data_access

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/check-pr/references/graphql-queries.md`
- `.cursor/skills/greptile/cli-review/SKILL.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/greptile/greploop/references/graphql-queries.md`
- `.cursor/skills/merge-dependabot-prs/SKILL.md`
- `.cursor/skills/merge-dependabot-prs/references/graphql-queries.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.greptile/config.json`
- `.greptile/rules.md`
- `.pre-commit-config.yaml`
- `.vscode/launch.json`
- `.zed/tasks.json`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `README.md`
- `SECURITY.md`
- Limited to 20 of 1226 candidate files.

### downstream_service

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/README.md`
- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/claude-code/CLAUDE.md`
- `.greptile/files.json`
- `.greptile/rules.md`
- `.vscode/.env.k8s.template`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `.zed/debug.json`
- `.zed/tasks.json`
- `AGENTS.md`
- `CLAUDE.md`
- `SECURITY.md`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- Limited to 20 of 2111 candidate files.

### error_handling

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/cli-review/SKILL.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.cursor/skills/sync-vendored-skills.sh`
- `.devcontainer/claude-code/CLAUDE.md`
- `.devcontainer/init-dev-user.sh`
- `.greptile/config.json`
- `.greptile/rules.md`
- `.pre-commit-config.yaml`
- `.vscode/tasks.json`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/alembic/README.md`
- `backend/alembic/env.py`
- `backend/alembic/run_multitenant_migrations.py`
- Limited to 20 of 2550 candidate files.

### serialization

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/check-pr/references/gitlab-api.md`
- `.cursor/skills/greptile/check-pr/references/graphql-queries.md`
- `.cursor/skills/greptile/cli-review/SKILL.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/greptile/greploop/references/gitlab-api.md`
- `.cursor/skills/merge-dependabot-prs/SKILL.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/devcontainer.json`
- `.devcontainer/init-dev-user.sh`
- `.gitignore`
- `.greptile/config.json`
- `.greptile/rules.md`
- `.pre-commit-config.yaml`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- Limited to 20 of 1321 candidate files.

## Security interpretation

A web request can cross routing, middleware, authentication, authorization, validation, business logic, data access and downstream-service trust boundaries before a response is returned.

Static discovery does not prove execution order or security enforcement at runtime.

## Safety

- No web request was sent.
- No endpoint was contacted.
- No authentication attempt occurred.
- No database query was executed.
- No downstream service was contacted.
