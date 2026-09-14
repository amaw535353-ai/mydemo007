# Phase 3 Action 3.2 - Network Architecture and Protocol Foundations Evidence

## Observation class

**STATIC SOURCE OBSERVATION ONLY. RUNTIME NETWORK TOPOLOGY AND PROTOCOL USE ARE UNVERIFIED.**

## Baseline

- Branch: `security/phase-3-foundations`
- HEAD: `349dee89221347306180917645f6e9ba2e24eb9b`
- Scanned tracked text files: **7451**
- Skipped large files: **1**
- Skipped binary files: **194**

## Protocol candidate summary

| Protocol / technology | Candidate files | Matches |
|---|---:|---:|
| HTTP | 1128 | 2962 |
| HTTPS | 916 | 8082 |
| TCP | 86 | 176 |
| UDP | 4 | 10 |
| WebSocket | 42 | 380 |
| gRPC | 11 | 87 |
| DNS | 98 | 229 |
| TLS_SSL | 127 | 552 |
| SMTP | 11 | 28 |
| PostgreSQL | 488 | 1454 |
| Redis | 356 | 1866 |

## Network-control candidate summary

| Concept | Candidate files | Matches |
|---|---:|---:|
| bind_listen | 182 | 603 |
| port | 420 | 2087 |
| proxy_upstream | 375 | 1568 |
| ingress | 38 | 108 |
| egress | 102 | 230 |
| network | 246 | 600 |
| loopback | 240 | 623 |
| wildcard_bind | 216 | 1098 |

## Network configuration candidates

Candidate configuration paths discovered: **193**

- `.devcontainer/Dockerfile`
- `.vscode/.env.k8s.template`
- `backend/Dockerfile`
- `backend/Dockerfile.model_server`
- `backend/onyx/background/celery/celery_k8s_probe.py`
- `backend/onyx/sandbox_proxy/ca_k8s.py`
- `backend/onyx/sandbox_proxy/identity_k8s.py`
- `backend/onyx/server/features/build/sandbox/image/Dockerfile`
- `backend/onyx/server/features/build/sandbox/kubernetes/k8s_client.py`
- `backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py`
- `backend/onyx/server/features/build/sandbox/kubernetes/scripts/bench-sandbox-spinup.sh`
- `backend/onyx/server/features/build/sandbox/kubernetes/sidecar_client.py`
- `backend/tests/external_dependency_unit/craft_helm/__init__.py`
- `backend/tests/external_dependency_unit/craft_helm/test_pod_spec.py`
- `backend/tests/external_dependency_unit/craft_helm/test_sandbox_image_prepuller.py`
- `backend/tests/integration/mock_services/docker-compose.mock-it-services.yml`
- `backend/tests/integration/mock_services/mock_connector_server/Dockerfile`
- `backend/tests/integration/tests/craft/docker_e2e/test_sandbox_network_posture_docker.py`
- `backend/tests/integration/tests/craft/k8s/conftest.py`
- `backend/tests/integration/tests/craft/k8s/k8s_db_fixtures.py`
- `backend/tests/integration/tests/craft/k8s/k8s_fixtures.py`
- `backend/tests/integration/tests/craft/k8s/test_approval_gate.py`
- `backend/tests/integration/tests/craft/k8s/test_browser.py`
- `backend/tests/integration/tests/craft/k8s/test_bun_node_modules_dedup.py`
- `backend/tests/integration/tests/craft/k8s/test_kubernetes_sandbox.py`
- `backend/tests/integration/tests/craft/k8s/test_kubernetes_sandbox_file_ops.py`
- `backend/tests/integration/tests/craft/k8s/test_messages_api_k8s.py`
- `backend/tests/integration/tests/craft/k8s/test_session_provisioning_api.py`
- `backend/tests/integration/tests/craft/k8s/test_skill_push.py`
- `backend/tests/integration/tests/craft/k8s/test_snapshot_restore.py`
- `backend/tests/integration/tests/craft/k8s/test_user_library_sync.py`
- `backend/tests/integration/tests/craft/k8s/test_webapp_preview.py`
- `backend/tests/unit/onyx/server/features/craft/sandbox/test_k8s_push_error_mapping.py`
- `backend/tests/unit/onyx/server/features/craft/sandbox/test_k8s_workspace_setup_sentinel.py`
- `backend/tests/unit/onyx/server/features/craft/test_kubernetes_sandbox_manager.py`
- `backend/tests/unit/sandbox_proxy/test_ca_k8s.py`
- `cli/Dockerfile`
- `cli/internal/deploy/deployfiles/embedded/data/nginx/app.conf.template`
- `cli/internal/deploy/deployfiles/embedded/data/nginx/app.conf.template.prod`
- `cli/internal/deploy/deployfiles/embedded/data/nginx/run-nginx.sh`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.craft.yml`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.onyx-lite.yml`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/env.nginx.template`
- `deployment/aws_ecs_fargate/cloudformation/services/onyx_nginx_service_template.yaml`
- `deployment/data/nginx/app.conf.template`
- `deployment/data/nginx/app.conf.template.no-letsencrypt`
- `deployment/data/nginx/app.conf.template.prod`
- `deployment/data/nginx/mcp.conf.inc.template`
- `deployment/data/nginx/mcp_upstream.conf.inc.template`
- `deployment/data/nginx/run-nginx.sh`
- `deployment/docker_compose/docker-compose.airgap-test.yml`
- `deployment/docker_compose/docker-compose.airgap-tls-test.yml`
- `deployment/docker_compose/docker-compose.craft.yml`
- `deployment/docker_compose/docker-compose.dev.yml`
- `deployment/docker_compose/docker-compose.mcp-api-key-test.yml`
- `deployment/docker_compose/docker-compose.mcp-oauth-test.yml`
- `deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml`
- `deployment/docker_compose/docker-compose.multitenant.yml`
- `deployment/docker_compose/docker-compose.onyx-lite.yml`
- `deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml`
- `deployment/docker_compose/docker-compose.prod.yml`
- `deployment/docker_compose/docker-compose.resources.yml`
- `deployment/docker_compose/docker-compose.search-testing.yml`
- `deployment/docker_compose/docker-compose.template.yml`
- `deployment/docker_compose/docker-compose.yml`
- `deployment/docker_compose/env.nginx.template`
- `deployment/helm/MIGRATION.md`
- `deployment/helm/README.md`
- `deployment/helm/charts/onyx-cnpg-crds/Chart.yaml`
- `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml`
- `deployment/helm/charts/onyx-cnpg-crds/values.yaml`
- `deployment/helm/charts/onyx/.gitignore`
- `deployment/helm/charts/onyx/.helmignore`
- `deployment/helm/charts/onyx/Chart.lock`
- `deployment/helm/charts/onyx/Chart.yaml`
- `deployment/helm/charts/onyx/SIZING.md`
- `deployment/helm/charts/onyx/ci/ct-values.yaml`
- `deployment/helm/charts/onyx/dashboards/indexing-pipeline.json`
- `deployment/helm/charts/onyx/dashboards/indexing-pruning.json`
- `deployment/helm/charts/onyx/dashboards/opensearch-search-latency.json`
- `deployment/helm/charts/onyx/dashboards/redis-queues.json`
- `deployment/helm/charts/onyx/scripts/check-cnpg-crds.sh`
- `deployment/helm/charts/onyx/templates/_helpers.tpl`
- `deployment/helm/charts/onyx/templates/api-deployment.yaml`
- `deployment/helm/charts/onyx/templates/api-hpa.yaml`
- `deployment/helm/charts/onyx/templates/api-scaledobject.yaml`
- `deployment/helm/charts/onyx/templates/api-service.yaml`
- `deployment/helm/charts/onyx/templates/api-servicemonitor.yaml`
- `deployment/helm/charts/onyx/templates/auth-secrets.yaml`
- `deployment/helm/charts/onyx/templates/celery-beat.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-docfetching-hpa.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-docfetching-metrics-service.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-docfetching-scaledobject.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-docfetching.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-docprocessing-hpa.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-docprocessing-metrics-service.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-docprocessing-scaledobject.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-docprocessing.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-heavy-hpa.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-heavy-metrics-service.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-heavy-scaledobject.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-heavy.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-light-hpa.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-light-metrics-service.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-light-scaledobject.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-light.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-monitoring-hpa.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-monitoring-metrics-service.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-monitoring-scaledobject.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-monitoring.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-primary-hpa.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-primary-metrics-service.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-primary-scaledobject.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-primary.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks-hpa.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks-metrics-service.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks-scaledobject.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-servicemonitors.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-user-file-processing-hpa.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-user-file-processing-scaledobject.yaml`
- `deployment/helm/charts/onyx/templates/celery-worker-user-file-processing.yaml`
- `deployment/helm/charts/onyx/templates/configmap.yaml`
- `deployment/helm/charts/onyx/templates/craft-kubernetes-version-check.yaml`
- `deployment/helm/charts/onyx/templates/craft-validation.yaml`
- `deployment/helm/charts/onyx/templates/discordbot.yaml`
- `deployment/helm/charts/onyx/templates/external-secret.yaml`
- `deployment/helm/charts/onyx/templates/extra-manifests.yaml`
- `deployment/helm/charts/onyx/templates/grafana-dashboards.yaml`
- `deployment/helm/charts/onyx/templates/indexing-model-deployment.yaml`
- `deployment/helm/charts/onyx/templates/indexing-model-service.yaml`
- `deployment/helm/charts/onyx/templates/inference-model-deployment.yaml`
- `deployment/helm/charts/onyx/templates/inference-model-service.yaml`
- `deployment/helm/charts/onyx/templates/ingress-api.yaml`
- `deployment/helm/charts/onyx/templates/ingress-mcp-oauth-callback.yaml`
- `deployment/helm/charts/onyx/templates/ingress-mcp.yaml`
- `deployment/helm/charts/onyx/templates/ingress-scim.yaml`
- `deployment/helm/charts/onyx/templates/ingress-webserver.yaml`
- `deployment/helm/charts/onyx/templates/legacy-vespa-check.yaml`
- `deployment/helm/charts/onyx/templates/lets-encrypt.yaml`
- `deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml`
- `deployment/helm/charts/onyx/templates/mcp-server-service.yaml`
- `deployment/helm/charts/onyx/templates/mcp-server-servicemonitor.yaml`
- `deployment/helm/charts/onyx/templates/network-policy-sandbox-egress.yaml`
- `deployment/helm/charts/onyx/templates/network-policy-sandbox-push.yaml`
- `deployment/helm/charts/onyx/templates/nginx-conf.yaml`
- `deployment/helm/charts/onyx/templates/postgres-cluster.yaml`
- `deployment/helm/charts/onyx/templates/pre-delete-cleanup.yaml`
- `deployment/helm/charts/onyx/templates/redis-tls-validation.yaml`
- `deployment/helm/charts/onyx/templates/sandbox-image-prepuller.yaml`
- `deployment/helm/charts/onyx/templates/sandbox-namespace.yaml`
- `deployment/helm/charts/onyx/templates/sandbox-podtemplate.yaml`
- `deployment/helm/charts/onyx/templates/sandbox-proxy/deployment.yaml`
- `deployment/helm/charts/onyx/templates/sandbox-proxy/networkpolicy-egress.yaml`
- `deployment/helm/charts/onyx/templates/sandbox-proxy/networkpolicy.yaml`
- `deployment/helm/charts/onyx/templates/sandbox-proxy/pdb.yaml`
- `deployment/helm/charts/onyx/templates/sandbox-proxy/rbac.yaml`
- `deployment/helm/charts/onyx/templates/sandbox-proxy/service.yaml`
- `deployment/helm/charts/onyx/templates/sandbox-rbac.yaml`
- `deployment/helm/charts/onyx/templates/serviceaccount.yaml`
- `deployment/helm/charts/onyx/templates/slackbot.yaml`
- `deployment/helm/charts/onyx/templates/tests/test-connection.yaml`
- `deployment/helm/charts/onyx/templates/tooling-pginto-configmap.yaml`
- `deployment/helm/charts/onyx/templates/webserver-deployment.yaml`
- `deployment/helm/charts/onyx/templates/webserver-hpa.yaml`
- `deployment/helm/charts/onyx/templates/webserver-scaledobject.yaml`
- `deployment/helm/charts/onyx/templates/webserver-service.yaml`
- `deployment/helm/charts/onyx/templates_disabled/background-deployment.yaml`
- `deployment/helm/charts/onyx/templates_disabled/background-hpa.yaml`
- `deployment/helm/charts/onyx/templates_disabled/onyx-secret.yaml`
- `deployment/helm/charts/onyx/values-ci.yaml`
- `deployment/helm/charts/onyx/values-lite.yaml`
- `deployment/helm/charts/onyx/values-localdev.yaml`
- `deployment/helm/charts/onyx/values.yaml`
- `deployment/helm/dev/craft-down.sh`
- `deployment/helm/dev/craft-up.sh`
- `deployment/helm/dev/k8s-down.sh`
- `deployment/helm/dev/k8s-up.sh`
- `deployment/helm/dev/refresh-images.sh`
- `docs/craft/dev/local-kubernetes.md`
- `docs/craft/docker/docker-compose-overview.md`
- `docs/craft/infra/sandbox-worker-network-policy.md`
- `docs/craft/kubernetes/craft-eks-runbook.md`
- `tools/loadtest/Dockerfile`
- `tools/loadtest/k8s/locust.yaml`
- `tools/loadtest/k8s/mock-llm.yaml`
- `tools/loadtest/mock_llm/Dockerfile`
- `tools/profiling/docker-compose.yml`
- `web/Dockerfile`
- `web/lib/opal/src/icons/network-graph.tsx`

## Representative protocol candidate paths

### HTTP

- `.claude/claude-security-guidance.md`
- `.cursor/skills/playwright/SKILL.md`
- `.devcontainer/claude-code/CLAUDE.md`
- `.devcontainer/devcontainer.json`
- `.greptile/config.json`
- `.greptile/rules.md`
- `.mcp.json`
- `.vscode/.env.k8s.template`
- `.vscode/env_template.txt`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `.zed/debug.json`
- `.zed/tasks.json`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/ee/onyx/connectors/perm_sync_valid.py`
- `backend/ee/onyx/document_index/vespa/app_config/cloud-services.xml.jinja`
- `backend/ee/onyx/external_permissions/box/access.py`
- `backend/ee/onyx/external_permissions/box/group_sync.py`
- `backend/ee/onyx/external_permissions/confluence/space_access.py`
- `backend/ee/onyx/hooks/executor.py`
- `backend/ee/onyx/server/billing/service.py`
- `backend/ee/onyx/server/enterprise_settings/api.py`
- `backend/ee/onyx/server/enterprise_settings/models.py`
- `backend/ee/onyx/server/features/hooks/api.py`
- `backend/ee/onyx/server/gateway/stream_bridge.py`
- `backend/ee/onyx/server/middleware/license_enforcement.py`
- Display limited to 30 of 1128 candidate files.

### HTTPS

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
- `backend/alembic/versions/3350a25df58e_add_sheets_and_slides_hosts_to_google_.py`
- `backend/alembic/versions/46625e4745d4_remove_native_enum.py`
- `backend/alembic/versions/77d07dffae64_forcibly_remove_more_enum_types_from_.py`
- `backend/alembic/versions/f3a9c1d4b7e2_provision_built_in_external_apps.py`
- `backend/alembic_tenants/env.py`
- `backend/ee/LICENSE`
- `backend/ee/onyx/configs/app_configs.py`
- `backend/ee/onyx/db/user_tenant_mapping.py`
- `backend/ee/onyx/external_permissions/confluence/doc_sync.py`
- `backend/ee/onyx/external_permissions/confluence/group_sync.py`
- Display limited to 30 of 916 candidate files.

### TCP

- `.devcontainer/init-firewall.sh`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/connectors/sharepoint/connector.py`
- `backend/onyx/db/engine/sql_engine.py`
- `backend/onyx/hooks/models.py`
- `backend/onyx/sandbox_proxy/addons/gate.py`
- `backend/onyx/server/features/build/sandbox/docker/dev_mode_serve.py`
- `backend/onyx/server/features/build/sandbox/image/firewall-init.sh`
- `backend/onyx/server/features/build/sandbox/image/opencode-plugins/webapp.ts`
- `backend/onyx/server/features/build/sandbox/kubernetes/k8s_client.py`
- `backend/onyx/server/features/build/sandbox/opencode/serve_client.py`
- `backend/tests/integration/tests/gateway_clients/README.md`
- `backend/tests/integration/tests/gateway_clients/conftest.py`
- `backend/tests/integration/tests/gateway_clients/run_with_server.sh`
- `backend/tests/unit/ee/onyx/server/features/hooks/test_api.py`
- `backend/tests/unit/onyx/auth/test_signup_rate_limit.py`
- `backend/tests/unit/onyx/connectors/sharepoint/test_streaming_download_retry.py`
- `backend/tests/unit/onyx/server/features/craft/sandbox/test_cold_pod_retry.py`
- `backend/tests/unit/onyx/server/features/craft/sandbox/test_k8s_push_error_mapping.py`
- `backend/tests/unit/sandbox_proxy/test_response_streaming.py`
- `cli/internal/deploy/deployfiles/embedded/data/nginx/app.conf.template`
- `cli/internal/deploy/deployfiles/embedded/data/nginx/app.conf.template.prod`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/env.template`
- `cli/internal/deploy/install/dev_test.go`
- `cli/internal/deploy/install/lifecycle_test.go`
- `cli/internal/deploy/install/prod_test.go`
- `cli/internal/deploy/install/status.go`
- `cli/internal/deploy/install/upgrade_test.go`
- `cli/internal/deploy/resources/resources.go`
- `cli/internal/deploy/resources/resources_test.go`
- Display limited to 30 of 86 candidate files.

### UDP

- `.devcontainer/init-firewall.sh`
- `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml`
- `deployment/helm/charts/onyx/templates/network-policy-sandbox-egress.yaml`
- `desktop/src-tauri/Cargo.lock`

### WebSocket

- `backend/onyx/auth/users.py`
- `backend/onyx/onyxbot/slack/listener.py`
- `backend/onyx/redis/redis_pool.py`
- `backend/onyx/server/features/build/sandbox/image/initial-requirements.txt`
- `backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py`
- `backend/onyx/server/features/build/webapp_proxy.py`
- `backend/onyx/server/manage/voice/user_api.py`
- `backend/onyx/server/manage/voice/websocket_api.py`
- `backend/onyx/skills/builtin/browser/SKILL.md`
- `backend/onyx/voice/providers/azure.py`
- `backend/onyx/voice/providers/elevenlabs.py`
- `backend/onyx/voice/providers/openai.py`
- `backend/requirements/default.txt`
- `backend/requirements/dev.txt`
- `backend/requirements/ee.txt`
- `backend/requirements/model_server.txt`
- `backend/tests/integration/tests/craft/k8s/test_approval_gate.py`
- `backend/tests/unit/onyx/server/features/craft/test_rewrite_asset_paths.py`
- `backend/tests/unit/onyx/server/manage/voice/test_streaming_transcription.py`
- `backend/tests/unit/onyx/voice/providers/test_azure_provider.py`
- `backend/tests/unit/onyx/voice/providers/test_elevenlabs_provider.py`
- `backend/tests/unit/onyx/voice/providers/test_openai_provider.py`
- `backend/tests/unit/shared_configs/test_user_id_contextvar.py`
- `cli/internal/deploy/deployfiles/embedded/data/nginx/app.conf.template`
- `cli/internal/deploy/deployfiles/embedded/data/nginx/app.conf.template.prod`
- `deployment/data/nginx/app.conf.template`
- `deployment/data/nginx/app.conf.template.no-letsencrypt`
- `deployment/data/nginx/app.conf.template.prod`
- `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml`
- `deployment/helm/charts/onyx/templates/discordbot.yaml`
- Display limited to 30 of 42 candidate files.

### gRPC

- `backend/requirements/default.txt`
- `backend/requirements/dev.txt`
- `backend/requirements/ee.txt`
- `backend/requirements/model_server.txt`
- `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml`
- `terraform-provider-onyx/go.mod`
- `terraform-provider-onyx/go.sum`
- `tools/loadtest/onyx_client/stream_parser.py`
- `tools/ods/go.mod`
- `tools/ods/go.sum`
- `uv.lock`

### DNS

- `.devcontainer/init-firewall.sh`
- `.vscode/.env.k8s.template`
- `.vscode/tasks.json`
- `backend/ee/onyx/auth/sso_domain_verification.py`
- `backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py`
- `backend/ee/onyx/db/tenant_sso_domain.py`
- `backend/ee/onyx/server/features/hooks/api.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/onyx/auth/jwt.py`
- `backend/onyx/auth/oauth_refresher.py`
- `backend/onyx/auth/oauth_token_manager.py`
- `backend/onyx/auth/sso_url_guard.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/configs/constants.py`
- `backend/onyx/connectors/web/connector.py`
- `backend/onyx/db/models.py`
- `backend/onyx/sandbox_proxy/addons/gate.py`
- `backend/onyx/server/features/build/AGENTS.template.md`
- `backend/onyx/server/features/build/sandbox/README.md`
- `backend/onyx/server/features/build/sandbox/docker/dev_mode_serve.py`
- `backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py`
- `backend/onyx/server/features/build/sandbox/image/firewall-init.sh`
- `backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py`
- `backend/onyx/server/features/mcp/api.py`
- `backend/onyx/server/features/mcp/ssrf.py`
- `backend/onyx/server/features/web_search/api.py`
- `backend/onyx/server/manage/sso/api.py`
- `backend/onyx/server/manage/users.py`
- `backend/onyx/skills/builtin/notion/notion_api.py`
- `backend/onyx/utils/external_endpoint.py`
- Display limited to 30 of 98 candidate files.

### TLS_SSL

- `backend/alembic/env.py`
- `backend/alembic_tenants/env.py`
- `backend/ee/onyx/server/features/hooks/api.py`
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
- `backend/onyx/connectors/sharepoint/connector.py`
- `backend/onyx/connectors/web/connector.py`
- `backend/onyx/db/engine/async_sql_engine.py`
- `backend/onyx/db/engine/iam_auth.py`
- `backend/onyx/db/engine/pg_ssl.py`
- `backend/onyx/db/engine/sql_engine.py`
- `backend/onyx/document_index/opensearch/client.py`
- `backend/onyx/file_store/file_store.py`
- `backend/onyx/redis/iam_auth.py`
- `backend/onyx/redis/redis_pool.py`
- `backend/onyx/sandbox_proxy/addons/gate.py`
- `backend/onyx/server/features/build/AGENTS.template.md`
- `backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py`
- `backend/onyx/server/features/build/sandbox/image/entrypoint.sh`
- `backend/onyx/server/features/build/sandbox/image/firewall-init.sh`
- `backend/onyx/skills/builtin/browser/SKILL.md`
- `backend/onyx/utils/tls.py`
- Display limited to 30 of 127 candidate files.

### SMTP

- `.vscode/env_template.txt`
- `backend/onyx/auth/email_utils.py`
- `backend/onyx/auth/users.py`
- `backend/tests/unit/onyx/auth/test_smtp_no_auth.py`
- `backend/tests/unit/onyx/auth/test_verification_email_tenant_context.py`
- `backend/tests/unit/onyx/connectors/gmail/thread.json`
- `backend/tests/unit/onyx/server/manage/test_bulk_invite_limit.py`
- `cli/internal/deploy/deployfiles/embedded/docker_compose/env.prod.template`
- `deployment/docker_compose/docker-compose.multitenant.yml`
- `deployment/docker_compose/env.prod.template`
- `deployment/helm/charts/onyx/values.yaml`

### PostgreSQL

- `.claude/claude-security-guidance.md`
- `.devcontainer/Dockerfile`
- `.devcontainer/claude-code/CLAUDE.md`
- `.greptile/rules.md`
- `.vscode/.env.k8s.template`
- `.vscode/tasks.json`
- `.zed/tasks.json`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/Dockerfile`
- `backend/alembic/README.md`
- `backend/alembic/versions/03bf8be6b53a_rework_kg_config.py`
- `backend/alembic/versions/06a38a307492_add_chat_message_request_params.py`
- `backend/alembic/versions/0816326d83aa_add_federated_connector_tables.py`
- `backend/alembic/versions/0a2b51deb0b8_add_starter_prompts.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/173cae5bba26_port_config_store.py`
- `backend/alembic/versions/177de57c21c9_display_custom_llm_models.py`
- `backend/alembic/versions/1b10e1fda030_add_additional_data_to_notifications.py`
- `backend/alembic/versions/1cb59a95b250_add_security_settings_table.py`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- `backend/alembic/versions/1f2a3b4c5d6e_add_internet_search_and_content_providers.py`
- `backend/alembic/versions/1f60f60c3401_embedding_model_search_settings.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py`
- `backend/alembic/versions/20f09b642ed0_backfill_write_chat_for_limited_service_.py`
- `backend/alembic/versions/26b931506ecb_default_chosen_assistants_to_none.py`
- Display limited to 30 of 488 candidate files.

### Redis

- `.claude/claude-security-guidance.md`
- `.devcontainer/claude-code/CLAUDE.md`
- `.greptile/rules.md`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `README.md`
- `README.zh-CN.md`
- `backend/AGENTS.md`
- `backend/CLAUDE.md`
- `backend/alembic/versions/2f95e36923e6_add_indexing_coordination.py`
- `backend/ee/onyx/background/celery/tasks/cloud/tasks.py`
- `backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py`
- `backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py`
- `backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py`
- `backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py`
- `backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py`
- `backend/ee/onyx/background/celery/tasks/vespa/tasks.py`
- `backend/ee/onyx/configs/multi_tenant_gating_config.py`
- `backend/ee/onyx/db/license.py`
- `backend/ee/onyx/server/billing/api.py`
- `backend/ee/onyx/server/billing/billing_cache.py`
- `backend/ee/onyx/server/documents/cc_pair.py`
- `backend/ee/onyx/server/license/api.py`
- `backend/ee/onyx/server/license/models.py`
- `backend/ee/onyx/server/log_export/api.py`
- `backend/ee/onyx/server/middleware/license_enforcement.py`
- `backend/ee/onyx/server/middleware/tenant_tracking.py`
- `backend/ee/onyx/server/middleware/tier_gate.py`
- `backend/ee/onyx/server/oauth/api.py`
- Display limited to 30 of 356 candidate files.

## Evidence safety

- No external network connection was made by the scanner.
- No runtime service was contacted.
- No credential or secret value was recorded.
- Source lines are intentionally omitted.
- Counts represent keyword/static candidates, not confirmed runtime behavior.
