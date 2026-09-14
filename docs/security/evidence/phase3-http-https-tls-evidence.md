# Phase 3 Action 3.4 - HTTP, HTTPS and TLS Evidence

## Observation class

**STATIC SOURCE CANDIDATES ONLY. NO RUNTIME HTTP OR TLS BEHAVIOR VERIFIED.**

- Branch: `security/phase-3-foundations`
- HEAD: `f25948e9768a4e07d842fac1194e4ff428f2c956`
- Scanned text files: **7451**
- Skipped large files: **1**
- Skipped binary files: **194**

## Candidate summary

| Concept | Files | Matching lines |
|---|---:|---:|
| http_url | 744 | 1574 |
| https_url | 867 | 7898 |
| http_methods | 3064 | 25980 |
| http_headers | 1071 | 4041 |
| cookies | 78 | 153 |
| cors | 19 | 29 |
| hsts | 1 | 1 |
| tls_ssl | 108 | 405 |
| certificate_trust | 55 | 192 |
| tls_verify_disabled | 6 | 12 |
| proxy_forwarding | 89 | 305 |
| redirects | 196 | 479 |

## Representative candidate paths

### http_url

- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/claude-code/CLAUDE.md`
- `.devcontainer/devcontainer.json`
- `.vscode/.env.k8s.template`
- `.vscode/env_template.txt`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `.zed/debug.json`
- `.zed/tasks.json`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `backend/ee/onyx/server/oauth/confluence_cloud.py`
- `backend/model_server/main.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/configs/saml_config/template.settings.json`
- `backend/onyx/connectors/box/connector.py`
- `backend/onyx/connectors/freshdesk/connector.py`
- `backend/onyx/connectors/gong/connector.py`
- `backend/onyx/connectors/highspot/client.py`
- Limited to 20 of 744 candidate files.

### https_url

- `.cursor/mcp.json`
- `.cursor/skills/greptile/README.md`
- `.cursor/skills/greptile/cli-review/SKILL.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.cursor/skills/sync-vendored-skills.sh`
- `.devcontainer/Dockerfile`
- `.devcontainer/init-firewall.sh`
- `.mcp.json`
- `.pre-commit-config.yaml`
- `.vscode/.env.k8s.template`
- `.vscode/env_template.txt`
- `CONTRIBUTING.md`
- `README.md`
- `README.zh-CN.md`
- `SECURITY.md`
- `backend/Dockerfile`
- `backend/Dockerfile.model_server`
- `backend/alembic/README.md`
- `backend/alembic/env.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- Limited to 20 of 867 candidate files.

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
- Limited to 20 of 3064 candidate files.

### http_headers

- `.claude/claude-security-guidance.md`
- `.cursor/skills/greptile/check-pr/SKILL.md`
- `.cursor/skills/greptile/greploop/SKILL.md`
- `.cursor/skills/merge-dependabot-prs/SKILL.md`
- `.cursor/skills/onyx-cli/SKILL.md`
- `.devcontainer/Dockerfile`
- `.devcontainer/README.md`
- `.devcontainer/claude-code/CLAUDE.md`
- `.devcontainer/devcontainer.json`
- `.devcontainer/init-dev-user.sh`
- `.devcontainer/init-firewall.sh`
- `.devcontainer/zshrc`
- `.greptile/rules.md`
- `.pre-commit-config.yaml`
- `.vscode/.env.k8s.template`
- `.vscode/tasks.json`
- `AGENTS.md`
- `CLAUDE.md`
- `backend/alembic/env.py`
- `backend/alembic/versions/28429dd43807_scheduled_tasks.py`
- Limited to 20 of 1071 candidate files.

### cookies

- `.devcontainer/Dockerfile`
- `.vscode/env_template.txt`
- `SECURITY.md`
- `backend/alembic/versions/c7e9f4a3b2d1_add_python_tool.py`
- `backend/ee/onyx/external_permissions/confluence/space_access.py`
- `backend/ee/onyx/server/tenants/admin_api.py`
- `backend/ee/onyx/server/tenants/anonymous_users_api.py`
- `backend/onyx/auth/mobile_sso/tokens.py`
- `backend/onyx/auth/pat.py`
- `backend/onyx/auth/sso_web_error.py`
- `backend/onyx/auth/users.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/connectors/confluence/onyx_confluence.py`
- `backend/onyx/connectors/salesforce/OAUTH.md`
- `backend/onyx/connectors/salesforce/blacklist.py`
- `backend/onyx/document_index/opensearch/schema.py`
- `backend/onyx/federated_connectors/oauth_utils.py`
- `backend/onyx/federated_connectors/slack/federated_connector.py`
- `backend/onyx/federated_connectors/slack/models.py`
- `backend/onyx/oauth/authorization_attempt.py`
- Limited to 20 of 78 candidate files.

### cors

- `backend/onyx/configs/app_configs.py`
- `backend/onyx/main.py`
- `backend/onyx/mcp_server/README.md`
- `backend/onyx/mcp_server/api.py`
- `backend/onyx/server/auth/captcha_api.py`
- `backend/onyx/server/features/build/sandbox/image/templates/outputs/web/bun.lock`
- `backend/onyx/server/features/build/webapp_proxy.py`
- `backend/onyx/skills/builtin/browser/SKILL.md`
- `backend/shared_configs/configs.py`
- `backend/tests/integration/tests/craft/webapp_preview.py`
- `backend/tests/integration/tests/pruning/website/js/jquery.js`
- `backend/tests/unit/onyx/server/auth/test_captcha_api.py`
- `backend/tests/unit/onyx/server/features/craft/test_rewrite_asset_paths.py`
- `backend/tests/unit/onyx/server/features/craft/test_webapp_proxy_header_stripping.py`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/env.template`
- `deployment/docker_compose/env.template`
- `deployment/helm/README.md`
- `deployment/helm/charts/onyx/values.yaml`
- `uv.lock`

### hsts

- `web/next.config.js`

### tls_ssl

- `backend/alembic/env.py`
- `backend/alembic_tenants/env.py`
- `backend/model_server/ca_certs.py`
- `backend/model_server/main.py`
- `backend/onyx/auth/login_claims_capture.py`
- `backend/onyx/auth/mobile_sso/code_store.py`
- `backend/onyx/auth/oauth_token_manager.py`
- `backend/onyx/background/celery/apps/docprocessing.py`
- `backend/onyx/background/celery/apps/user_file_processing.py`
- `backend/onyx/background/celery/configs/base.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/connectors/google_utils/google_utils.py`
- `backend/onyx/connectors/web/connector.py`
- `backend/onyx/db/engine/async_sql_engine.py`
- `backend/onyx/db/engine/iam_auth.py`
- `backend/onyx/db/engine/pg_ssl.py`
- `backend/onyx/db/engine/sql_engine.py`
- `backend/onyx/document_index/opensearch/client.py`
- `backend/onyx/file_store/file_store.py`
- `backend/onyx/redis/iam_auth.py`
- Limited to 20 of 108 candidate files.

### certificate_trust

- `backend/ee/onyx/server/features/hooks/api.py`
- `backend/onyx/background/celery/configs/base.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/connectors/sharepoint/connector.py`
- `backend/onyx/db/engine/iam_auth.py`
- `backend/onyx/db/engine/pg_ssl.py`
- `backend/onyx/document_index/opensearch/client.py`
- `backend/onyx/redis/redis_pool.py`
- `backend/onyx/server/features/build/sandbox/image/entrypoint.sh`
- `backend/onyx/skills/builtin/browser/SKILL.md`
- `backend/onyx/utils/tls.py`
- `backend/onyx/utils/url.py`
- `backend/scripts/debugging/opensearch/opensearch_debug.py`
- `backend/tests/airgap/tls_failure_server.py`
- `backend/tests/daily/connectors/sharepoint/test_sharepoint_connector.py`
- `backend/tests/external_dependency_unit/auth/test_permission_projection_contract.py`
- `backend/tests/external_dependency_unit/craft_helm/test_pod_spec.py`
- `backend/tests/integration/connector_job_tests/sharepoint/conftest.py`
- `backend/tests/integration/mock_services/mcp_test_server/run_mock_oidc_idp.py`
- `backend/tests/integration/tests/mcp_oauth/conftest.py`
- Limited to 20 of 55 candidate files.

### tls_verify_disabled

- `backend/onyx/background/celery/celery_utils.py`
- `backend/onyx/db/engine/pg_ssl.py`
- `backend/onyx/document_index/vespa/shared_utils/utils.py`
- `backend/onyx/utils/tls.py`
- `backend/tests/unit/onyx/db/engine/test_postgres_ssl.py`
- `backend/tests/unit/onyx/utils/test_tls.py`

### proxy_forwarding

- `.devcontainer/README.md`
- `.devcontainer/claude-code/CLAUDE.md`
- `backend/ee/onyx/server/billing/api.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/ee/onyx/server/gateway/api.py`
- `backend/onyx/auth/signup_rate_limit.py`
- `backend/onyx/chat/chat_state.py`
- `backend/onyx/chat/process_message.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/connectors/blob/connector.py`
- `backend/onyx/llm/multi_llm.py`
- `backend/onyx/sandbox_proxy/addons/gate.py`
- `backend/onyx/server/auth/captcha_api.py`
- `backend/onyx/server/features/build/AGENTS.template.md`
- `backend/onyx/server/features/build/sandbox/README.md`
- `backend/onyx/server/features/build/sandbox/image/templates/outputs/web/bun.lock`
- `backend/onyx/server/features/build/sandbox/opencode/serve_client.py`
- `backend/onyx/server/features/build/session/streaming.py`
- `backend/onyx/server/features/build/webapp_proxy.py`
- `backend/onyx/server/middleware/api_prefix.py`
- Limited to 20 of 89 candidate files.

### redirects

- `.claude/claude-security-guidance.md`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/8f3b2c91d4e7_backfill_legacy_callback_on_seeded_sso_.py`
- `backend/ee/onyx/server/billing/api.py`
- `backend/ee/onyx/server/billing/service.py`
- `backend/ee/onyx/server/tenants/proxy.py`
- `backend/onyx/auth/captcha.py`
- `backend/onyx/auth/jwt.py`
- `backend/onyx/auth/mobile_sso/sso_completion.py`
- `backend/onyx/auth/sso_url_guard.py`
- `backend/onyx/auth/sso_web_error.py`
- `backend/onyx/auth/users.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/configs/saml_config/template.settings.json`
- `backend/onyx/connectors/freshdesk/connector.py`
- `backend/onyx/connectors/web/connector.py`
- `backend/onyx/connectors/zoom/client.py`
- `backend/onyx/db/sso_provider.py`
- `backend/onyx/external_apps/providers/google_base.py`
- `backend/onyx/external_apps/providers/hubspot.py`
- Limited to 20 of 196 candidate files.

## Security interpretation

These results are static candidates only. They do not prove runtime HTTP exposure, HTTPS enforcement, TLS versions, certificate validity, cookie behavior, CORS/HSTS enforcement, proxy trust, or vulnerabilities.

`tls_verify_disabled` matches require contextual review and are not confirmed vulnerabilities.

## Safety

- No HTTP request sent.
- No HTTPS request sent.
- No TLS handshake performed.
- No live certificate retrieved.
- No external endpoint contacted.
