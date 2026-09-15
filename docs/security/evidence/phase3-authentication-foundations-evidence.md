# Phase 3 Action 3.7 - Authentication Foundations Evidence

## Observation class

**STATIC SOURCE CANDIDATES ONLY. RUNTIME AUTHENTICATION BEHAVIOR IS UNVERIFIED.**

- Branch: `security/phase-3-foundations`
- HEAD: `39307fcc954ef925e46fa89bc8add4a56ad87d38`
- Scanned text files: **7451**
- Skipped large files: **1**
- Skipped binary files: **194**

## Candidate summary

| Concept | Candidate files | Matching lines |
|---|---:|---:|
| login_logout | 299 | 1105 |
| password | 299 | 1158 |
| password_hashing | 3 | 81 |
| api_key | 512 | 3197 |
| bearer_token | 392 | 1276 |
| jwt | 54 | 185 |
| oauth | 363 | 2299 |
| oidc | 93 | 469 |
| saml | 69 | 240 |
| mfa | 3 | 11 |
| session_auth | 1356 | 13003 |
| auth_middleware | 246 | 664 |
| identity_claims | 307 | 1070 |
| token_expiry | 288 | 965 |
| refresh_token | 80 | 418 |
| password_reset | 29 | 68 |

## Representative candidates

### login_logout

- `.cursor/skills/greptile/README.md`
- `.cursor/skills/greptile/check-pr/references/graphql-queries.md`
- `.cursor/skills/greptile/cli-review/SKILL.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/greptile/greploop/references/graphql-queries.md`
- `.cursor/skills/playwright/SKILL.md`
- `.vscode/env_template.txt`
- `AGENTS.md`
- `CLAUDE.md`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`

### password

- `.devcontainer/devcontainer.json`
- `.vscode/.env.k8s.template`
- `.vscode/env_template.txt`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `AGENTS.md`
- `CLAUDE.md`
- `backend/Dockerfile.model_server`
- `backend/alembic/env.py`
- `backend/alembic/versions/495cb26ce93e_create_knowlege_graph_tables.py`

### password_hashing

- `backend/requirements/default.txt`
- `backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_per_user_key.py`
- `uv.lock`

### api_key

- `.greptile/config.json`
- `.greptile/rules.md`
- `backend/alembic/versions/03d085c5c38d_backfill_account_type.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/0d9c7b6a5e4f_retain_user_usage_after_user_deletion.py`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- `backend/alembic/versions/1f2a3b4c5d6e_add_internet_search_and_content_providers.py`
- `backend/alembic/versions/20f09b642ed0_backfill_write_chat_for_limited_service_.py`
- `backend/alembic/versions/3c9a65f1207f_seed_exa_provider_from_env.py`
- `backend/alembic/versions/401c1ac29467_add_tables_for_ui_based_llm_.py`

### bearer_token

- `.claude/claude-security-guidance.md`
- `.greptile/rules.md`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/582269841f06_add_granted_scopes_to_external_app_user_.py`
- `backend/alembic/versions/f3a9c1d4b7e2_provision_built_in_external_apps.py`
- `backend/ee/onyx/auth/users.py`
- `backend/ee/onyx/configs/license_enforcement_config.py`
- `backend/ee/onyx/db/scim.py`
- `backend/ee/onyx/external_permissions/sharepoint/permission_utils.py`

### jwt

- `backend/alembic/versions/e7c00417d1e5_add_jwt_auth_columns_to_security_.py`
- `backend/ee/onyx/auth/users.py`
- `backend/ee/onyx/configs/app_configs.py`
- `backend/ee/onyx/server/billing/service.py`
- `backend/ee/onyx/server/tenants/access.py`
- `backend/ee/onyx/server/tenants/admin_api.py`
- `backend/ee/onyx/server/tenants/proxy.py`
- `backend/onyx/auth/jwt.py`
- `backend/onyx/auth/login_claims_capture.py`
- `backend/onyx/auth/mobile_sso/code_store.py`

### oauth

- `.claude/claude-security-guidance.md`
- `.greptile/rules.md`
- `.vscode/env_template.txt`
- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `README.zh-CN.md`
- `backend/alembic/versions/2666d766cb9b_google_oauth2.py`
- `backend/alembic/versions/3a9b8d7c6e5f_add_mcp_known_provider_fields.py`
- `backend/alembic/versions/465f78d9b7f9_larger_access_tokens_for_oauth.py`

### oidc

- `.vscode/env_template.txt`
- `README.md`
- `README.zh-CN.md`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/8f3b2c91d4e7_backfill_legacy_callback_on_seeded_sso_.py`
- `backend/onyx/auth/login_claims_capture.py`
- `backend/onyx/auth/mobile_sso/__init__.py`
- `backend/onyx/auth/mobile_sso/sso_completion.py`
- `backend/onyx/auth/oauth_refresher.py`
- `backend/onyx/auth/oidc_client.py`

### saml

- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `README.zh-CN.md`
- `backend/alembic/versions/ae62505e3acc_add_saml_accounts.py`
- `backend/onyx/auth/login_claims_capture.py`
- `backend/onyx/auth/mobile_sso/__init__.py`
- `backend/onyx/auth/mobile_sso/sso_completion.py`
- `backend/onyx/auth/oauth_refresher.py`
- `backend/onyx/auth/sso_web_error.py`

### mfa

- `backend/onyx/skills/builtin/browser/SKILL.md`
- `backend/tests/daily/connectors/box/README.md`
- `backend/tests/evals/connector_filter_eval/scope_eval_cases.py`

### session_auth

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

### auth_middleware

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/README.md`
- `.cursor/skills/greptile/cli-review/SKILL.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/Dockerfile`
- `backend/alembic/versions/f7ca3e2f45d9_migrate_no_auth_data_to_placeholder.py`
- `backend/ee/onyx/server/billing/service.py`
- `backend/ee/onyx/server/enterprise_settings/api.py`
- `backend/ee/onyx/server/evals/api.py`

### identity_claims

- `.cursor/skills/greptile/LICENSE`
- `.cursor/skills/sync-vendored-skills.sh`
- `LICENSE`
- `backend/alembic/versions/5ae8240accb3_add_research_agent_database_tables_and_.py`
- `backend/alembic/versions/a852cbe15577_new_chat_history.py`
- `backend/alembic_tenants/versions/a754e4f72e60_add_tenant_sso_domain_routing.py`
- `backend/ee/LICENSE`
- `backend/ee/onyx/auth/sso_domain_verification.py`
- `backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py`
- `backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py`

### token_expiry

- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/alembic/versions/0816326d83aa_add_federated_connector_tables.py`
- `backend/alembic/versions/2664261bfaab_add_cache_store_table.py`
- `backend/alembic/versions/2666d766cb9b_google_oauth2.py`
- `backend/alembic/versions/5e1c073d48a3_add_personal_access_token_table.py`
- `backend/alembic/versions/ae62505e3acc_add_saml_accounts.py`
- `backend/ee/onyx/auth/users.py`
- `backend/ee/onyx/background/celery/tasks/beat_schedule.py`
- `backend/ee/onyx/background/celery/tasks/cloud/tasks.py`

### refresh_token

- `backend/alembic/versions/2666d766cb9b_google_oauth2.py`
- `backend/alembic/versions/cf90764725d8_larger_refresh_tokens.py`
- `backend/ee/onyx/server/enterprise_settings/api.py`
- `backend/ee/onyx/server/oauth/confluence_cloud.py`
- `backend/ee/onyx/server/oauth/google_drive.py`
- `backend/onyx/auth/login_claims_capture.py`
- `backend/onyx/auth/mobile_sso/tokens.py`
- `backend/onyx/auth/oauth_refresher.py`
- `backend/onyx/auth/oauth_token_manager.py`
- `backend/onyx/auth/users.py`

### password_reset

- `.vscode/env_template.txt`
- `backend/onyx/auth/email_utils.py`
- `backend/onyx/auth/users.py`
- `backend/onyx/server/auth_check.py`
- `backend/onyx/skills/builtin/browser/SKILL.md`
- `backend/onyx/utils/audit.py`
- `backend/scripts/search_loadtest.py`
- `backend/tests/unit/onyx/auth/test_auth_audit_events.py`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/env.template`
- `deployment/docker_compose/env.template`

## Interpretation

Authentication verifies identity. Authorization separately determines what that identity may do.

Static matches do not prove password safety, credential validation, MFA enforcement, token verification, token expiry, issuer/audience validation, session security or revocation.

## Safety

- No login attempt was performed.
- No password was tested.
- No credential was submitted.
- No token was replayed.
- No identity provider was contacted.
- No external service was contacted.
