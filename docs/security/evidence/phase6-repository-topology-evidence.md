# Phase 6 Action 6.2 - Documentation and Repository Topology Evidence
## Purpose
Perform source-only reconnaissance of the exact pinned Onyx revision before
runtime execution or deeper architectural interpretation.
This action records **observed repository structure and candidate paths**.
Path-name matches are discovery heuristics only and are not yet proof of
runtime behavior, trust boundaries, or vulnerabilities.
## Baseline verification
- Evidence branch: `security/phase-6-onyx-baseline`
- Action 6.1 parent: `9c56aa64cbe958d0e134fb421904aba8bf6b1772`
- Onyx repository: `https://github.com/onyx-dot-app/onyx.git`
- Onyx local path: `/home/ahmed/projects/onyx-phase6`
- Onyx branch observed: `main`
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Target working tree clean: PASS
## Repository measurements
- Root objects: 44
- Root directories: 20
- Total tracked files: 7751
- Documentation/governance candidates captured: 200
- Build/package candidates captured: 25
- Deployment/infrastructure candidates captured: 250
- Security path candidates captured: 300
- AI/RAG/agent path candidates captured: 400
- Data/queue/storage path candidates captured: 300
## Top-Level Repository Objects
```text
.claude
.cursor
.devcontainer
.git-blame-ignore-revs
.gitattributes
.github
.gitignore
.greptile
.mcp.json
.oxfmtrc.json
.pre-commit-config.yaml
.python-version
.secretsignore
.vscode
.zed
AGENTS.md
CLAUDE.md
CONTRIBUTING.md
LICENSE
Makefile
README.md
README.zh-CN.md
SECURITY.md
backend
bun.lock
cli
contributor_ip_assignment
cr.yaml
ct.yaml
cubic.yaml
deployment
desktop
docker-bake.hcl
docs
examples
extensions
mobile
package.json
pyproject.toml
terraform-provider-onyx
tools
uv.lock
web
widget
```
## File Counts by Top-Level Area
```text
    3769  backend
    2430  web
     451  mobile
     231  tools
     228  deployment
     171  cli
     136  terraform-provider-onyx
      73  docs
      66  .github
      65  desktop
      27  extensions
      24  [root]
      20  widget
      18  .cursor
      13  examples
       9  .devcontainer
       6  .zed
       6  .vscode
       3  .greptile
       3  .claude
       2  contributor_ip_assignment
```
## Root Documentation Headings
```text

===== README.md =====
# Onyx - The Open Source AI Platform
## ⭐ Features
## 🚀 Deployment Modes
#### Onyx Lite
#### Standard Onyx
## 🏢 Onyx for Enterprise
## 📚 Licensing
## 👪 Community
## 💡 Contributing

===== SECURITY.md =====
# Security Policy
## Supported Versions
## Reporting a Vulnerability
## Response Expectations
## Scope
## Safe Harbor

===== CONTRIBUTING.md =====
# Contributing to Onyx
## Table of Contents
## Contribution Opportunities
## Contribution Process
### 1. Get the feature or enhancement approved
### 2. Get the design approved
### 3. IP attribution for EE contributions
### 4. Review and testing
### Implicit agreements
## Development Setup
### Prerequisites
### Backend: Python Requirements
### Frontend: Node Dependencies
### Formatting and Linting
#### Backend
#### Frontend
## Running the Application
### VSCode Debugger (Recommended)
#### Initial Setup
#### Using the Debugger
### Manually Running for Development
#### Docker containers for external software
#### Running Onyx locally
#### Wrapping up
### Running on a Local Kubernetes Cluster
### Running in Docker
## macOS-Specific Notes
### Setting up Python
### Setting up Docker
### Formatting and Linting
## Engineering Best Practices
### Principles and Collaboration
### Style and Maintainability
#### Comments and readability
#### Errors and exceptions
#### Typing
#### State, objects, and boundaries
#### Naming
#### Correctness by construction
### Performance and Correctness
### Repository Conventions
#### Where code lives
#### Pydantic and modeling
#### Data conventions
#### Logging
#### Encapsulation
#### SQLAlchemy guidance
#### Trunk-based development and feature flags
#### Miscellaneous
## Release Process
## Getting Help
## Enterprise Edition Contributions
```
## Documentation and Governance Candidates
Bounded to first 200 path matches.
```text
.cursor/skills/greptile/LICENSE
.cursor/skills/greptile/README.md
.devcontainer/README.md
.github/CODEOWNERS
.zed/README.md
CONTRIBUTING.md
LICENSE
README.md
README.zh-CN.md
SECURITY.md
backend/alembic/README.md
backend/alembic_tenants/README.md
backend/ee/LICENSE
backend/ee/onyx/db/license.py
backend/ee/onyx/utils/license.py
backend/generated/README.md
backend/model_server/legacy/README.md
backend/onyx/background/README.md
backend/onyx/chat/README.md
backend/onyx/connectors/README.md
backend/onyx/db/README.md
backend/onyx/document_index/opensearch/README.md
backend/onyx/evals/README.md
backend/onyx/file_store/README.md
backend/onyx/llm/prompt_cache/README.md
backend/onyx/mcp_server/README.md
backend/onyx/server/features/build/sandbox/README.md
backend/onyx/server/features/build/sandbox/image/README.md
backend/onyx/utils/jsonriver/LICENSE
backend/requirements/README.md
backend/scripts/debugging/litellm/README
backend/scripts/tenant_cleanup/README.md
backend/slackbot_images/README.md
backend/tests/README.md
backend/tests/daily/connectors/box/README.md
backend/tests/daily/connectors/coda/README.md
backend/tests/evals/connector_filter_eval/README.md
backend/tests/integration/README.md
backend/tests/integration/tests/gateway_clients/README.md
backend/tests/integration/tests/pruning/website/readme.txt
backend/tests/regression/answer_quality/README.md
backend/tests/regression/search_quality/README.md
cli/README.md
cli/internal/deploy/deployfiles/embedded/docker_compose/README.md
cli/internal/markdown/lexers/LICENSE
cli/internal/markdown/lexers/README.md
deployment/README.md
deployment/aws_ecs_fargate/cloudformation/README.md
deployment/docker_compose/README.md
deployment/helm/README.md
deployment/terraform/modules/aws/README.md
deployment/terraform/modules/azure/README.md
desktop/README.md
docs/AUDIT_LOGGING.md
docs/METRICS.md
docs/craft/craft-main-plan.md
docs/craft/dev/local-compose-craft.md
docs/craft/dev/local-kubernetes.md
docs/craft/docker/docker-compose-overview.md
docs/craft/features/compact-command.md
docs/craft/features/egress-proxy-and-approvals/README.md
docs/craft/features/external-apps/action-policies.md
docs/craft/features/external-apps/cloud-managed-app-credentials.md
docs/craft/features/external-apps/egress-proxy-action-policy-enforcement.md
docs/craft/features/external-apps/external-app-skill-action-availability.md
docs/craft/features/external-apps/oauth-token-refresh.md
docs/craft/features/scheduled-tasks/overview.md
docs/craft/features/scheduled-tasks/pre-approvals.md
docs/craft/features/scheduled-tasks/tests.md
docs/craft/features/search/craft-search.md
docs/craft/features/streaming/docker-opencode-serve.md
docs/craft/features/streaming/drop-acp-layer.md
docs/craft/features/streaming/opencode-serve-client.md
docs/craft/features/streaming/preserve-opencode-sessions.md
docs/craft/features/streaming/shared-acp-exec-client.md
docs/craft/features/subagents/2026-05-28-subagents-view-design.md
docs/craft/features/user-library-sync.md
docs/craft/fix-live-scheduled-task-runs.md
docs/craft/infra/image-architecture.md
docs/craft/infra/sandbox-worker-network-policy.md
docs/craft/infra/snapshot-retention.md
docs/craft/issues/opencode-serve-deploy-gotchas.md
docs/craft/issues/opencode-serve-event-stream-pitfalls.md
docs/craft/kubernetes/craft-eks-runbook.md
docs/craft/lazy-webapp-provisioning.md
docs/craft/legacy/v0_craft_architecture.md
docs/craft/sandbox/image-and-spinup.md
docs/craft/sandbox/sandbox-exec-sidecar.md
docs/craft/sandbox/sandbox-podtemplate.md
docs/craft/specs/browser-use.md
docs/craft/ui/packet-rendering-overhaul.md
docs/craft/ui/sidebar-cleanup.md
docs/group-manager-scoped-permissions/00-index.md
docs/group-manager-scoped-permissions/01-research.md
docs/group-manager-scoped-permissions/02-high-level-design.md
docs/group-manager-scoped-permissions/03-detailed-design.md
docs/group-manager-scoped-permissions/04-implementation-plan.md
docs/group-manager-scoped-permissions/05-pr-roadmap.md
docs/group-manager-scoped-permissions/07-ui-capability-model-design.md
docs/group-manager-scoped-permissions/10-branch-audit-anon-and-service-accounts.md
docs/mobile-chat/00-index.md
docs/mobile-chat/01-research.md
docs/mobile-chat/02-high-level-design.md
docs/mobile-chat/03-detailed-design.md
docs/mobile-chat/04-implementation-plan.md
docs/mobile-chat/05-pr-roadmap.md
docs/mobile-chat/06-unified-chat-surface.md
docs/mobile-chat/9a-citations/00-index.md
docs/mobile-chat/9a-citations/01-research.md
docs/mobile-chat/9a-citations/02-high-level-design.md
docs/mobile-chat/9a-citations/03-detailed-design.md
docs/mobile-chat/9a-citations/04-implementation-plan.md
docs/mobile-chat/9a-citations/05-pr-roadmap.md
docs/mobile-chat/9b-timeline/00-index.md
docs/mobile-chat/9b-timeline/01-research.md
docs/mobile-chat/9b-timeline/02-high-level-design.md
docs/mobile-chat/9b-timeline/03-detailed-design.md
docs/mobile-chat/9b-timeline/04-implementation-plan.md
docs/mobile-chat/9b-timeline/05-pr-roadmap.md
docs/mobile-chat/input-bar-controls/00-index.md
docs/mobile-chat/input-bar-controls/01-research.md
docs/mobile-chat/input-bar-controls/02-high-level-design.md
docs/mobile-chat/input-bar-controls/03-detailed-design.md
docs/mobile-chat/input-bar-controls/04-implementation-plan.md
docs/mobile-chat/input-bar-controls/05-pr-roadmap.md
docs/usage/usage-reports.md
examples/widget/README.md
extensions/chrome/LICENSE
extensions/chrome/README.md
mobile/README.md
mobile/patches/README.md
terraform-provider-onyx/LICENSE
terraform-provider-onyx/README.md
terraform-provider-onyx/docs/data-sources/connectors.md
terraform-provider-onyx/docs/data-sources/embedding_providers.md
terraform-provider-onyx/docs/data-sources/llm_providers.md
terraform-provider-onyx/docs/data-sources/settings.md
terraform-provider-onyx/docs/index.md
terraform-provider-onyx/docs/resources/agent.md
terraform-provider-onyx/docs/resources/api_key.md
terraform-provider-onyx/docs/resources/cc_pair.md
terraform-provider-onyx/docs/resources/connector.md
terraform-provider-onyx/docs/resources/credential.md
terraform-provider-onyx/docs/resources/custom_tool.md
terraform-provider-onyx/docs/resources/document_set.md
terraform-provider-onyx/docs/resources/embedding_provider.md
terraform-provider-onyx/docs/resources/llm_provider.md
terraform-provider-onyx/docs/resources/llm_provider_default.md
terraform-provider-onyx/docs/resources/mcp_server.md
terraform-provider-onyx/docs/resources/settings.md
terraform-provider-onyx/docs/resources/user_group.md
terraform-provider-onyx/examples/bootstrap/README.md
tools/loadtest/README.md
tools/ods-audit/README.md
tools/ods/README.md
tools/profiling/README.md
web/.storybook/README.md
web/README.md
web/lib/opal/NOTICE.md
web/lib/opal/README.md
web/lib/opal/scripts/README.md
web/lib/opal/src/components/README.md
web/lib/opal/src/components/buttons/attachment-item-button/README.md
web/lib/opal/src/components/buttons/button/README.md
web/lib/opal/src/components/buttons/copy-button/README.md
web/lib/opal/src/components/buttons/filter-button/README.md
web/lib/opal/src/components/buttons/line-item-button/README.md
web/lib/opal/src/components/buttons/link-button/README.md
web/lib/opal/src/components/buttons/open-button/README.md
web/lib/opal/src/components/buttons/select-button/README.md
web/lib/opal/src/components/buttons/sidebar-tab/README.md
web/lib/opal/src/components/buttons/text-button/README.md
web/lib/opal/src/components/calendar/README.md
web/lib/opal/src/components/cards/card/README.md
web/lib/opal/src/components/cards/empty-message-card/README.md
web/lib/opal/src/components/cards/message-card/README.md
web/lib/opal/src/components/cards/select-card/README.md
web/lib/opal/src/components/code/README.md
web/lib/opal/src/components/divider/README.md
web/lib/opal/src/components/end-of-list/README.md
web/lib/opal/src/components/icon-container/README.md
web/lib/opal/src/components/inputs/booleans/input-checkbox/README.md
web/lib/opal/src/components/inputs/booleans/input-switch/README.md
web/lib/opal/src/components/inputs/chrono/input-date-picker/README.md
web/lib/opal/src/components/inputs/chrono/input-date-range-picker/README.md
web/lib/opal/src/components/inputs/chrono/input-time/README.md
web/lib/opal/src/components/inputs/input-avatar/README.md
web/lib/opal/src/components/inputs/input-file/README.md
web/lib/opal/src/components/inputs/input-image/README.md
web/lib/opal/src/components/inputs/input-key-value/README.md
web/lib/opal/src/components/inputs/input-list/README.md
web/lib/opal/src/components/inputs/input-number/README.md
web/lib/opal/src/components/inputs/input-password-type-in/README.md
web/lib/opal/src/components/inputs/input-text-area/README.md
web/lib/opal/src/components/inputs/input-type-in/README.md
web/lib/opal/src/components/inputs/selections/input-combo-box/README.md
web/lib/opal/src/components/inputs/selections/input-multi-select/README.md
web/lib/opal/src/components/inputs/selections/input-single-select/README.md
web/lib/opal/src/components/loader/README.md
web/lib/opal/src/components/modal/README.md
```
## Build and Package Candidates
Bounded to first 200 path matches.
```text
Makefile
backend/onyx/server/features/build/sandbox/image/templates/outputs/web/package.json
cli/go.mod
cli/go.sum
cli/pyproject.toml
desktop/package.json
desktop/src-tauri/Cargo.lock
desktop/src-tauri/Cargo.toml
examples/widget/package.json
mobile/package.json
package.json
pyproject.toml
terraform-provider-onyx/go.mod
terraform-provider-onyx/go.sum
tools/ods-audit/pyproject.toml
tools/ods/go.mod
tools/ods/go.sum
tools/ods/pyproject.toml
web/lib/opal/package.json
web/lib/shared/package.json
web/package.json
web/tools/oxlint/anti-slop/package.json
web/tools/oxlint/i18n/package.json
web/tools/type-check/package.json
widget/package.json
```
## Deployment and Infrastructure Candidates
Bounded to first 250 path matches.
```text
.devcontainer/Dockerfile
.github/workflows/deployment.yml
backend/Dockerfile
backend/Dockerfile.model_server
backend/onyx/server/features/build/sandbox/image/Dockerfile
backend/onyx/server/features/build/sandbox/image/templates/outputs/web/components/ui/chart.tsx
backend/onyx/server/features/build/sandbox/kubernetes/k8s_client.py
backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py
backend/onyx/server/features/build/sandbox/kubernetes/scripts/bench-sandbox-spinup.sh
backend/onyx/server/features/build/sandbox/kubernetes/sidecar_client.py
backend/onyx/skills/builtin/pptx/charts.md
backend/onyx/skills/builtin/pptx/scripts/chart.py
backend/tests/integration/mock_services/docker-compose.mock-it-services.yml
backend/tests/integration/mock_services/mock_connector_server/Dockerfile
backend/tests/integration/tests/craft/k8s/conftest.py
backend/tests/integration/tests/craft/k8s/k8s_db_fixtures.py
backend/tests/integration/tests/craft/k8s/k8s_fixtures.py
backend/tests/integration/tests/craft/k8s/test_approval_gate.py
backend/tests/integration/tests/craft/k8s/test_browser.py
backend/tests/integration/tests/craft/k8s/test_bun_node_modules_dedup.py
backend/tests/integration/tests/craft/k8s/test_kubernetes_sandbox.py
backend/tests/integration/tests/craft/k8s/test_kubernetes_sandbox_file_ops.py
backend/tests/integration/tests/craft/k8s/test_messages_api_k8s.py
backend/tests/integration/tests/craft/k8s/test_session_provisioning_api.py
backend/tests/integration/tests/craft/k8s/test_skill_push.py
backend/tests/integration/tests/craft/k8s/test_snapshot_restore.py
backend/tests/integration/tests/craft/k8s/test_user_library_sync.py
backend/tests/integration/tests/craft/k8s/test_webapp_preview.py
cli/Dockerfile
cli/cmd/deploy.go
cli/internal/deploy/deployfiles/embedded/data/nginx/app.conf.template
cli/internal/deploy/deployfiles/embedded/data/nginx/app.conf.template.prod
cli/internal/deploy/deployfiles/embedded/data/nginx/run-nginx.sh
cli/internal/deploy/deployfiles/embedded/docker_compose/README.md
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.craft.yml
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.onyx-lite.yml
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml
cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml
cli/internal/deploy/deployfiles/embedded/docker_compose/env.nginx.template
cli/internal/deploy/deployfiles/embedded/docker_compose/env.prod.template
cli/internal/deploy/deployfiles/embedded/docker_compose/env.template
cli/internal/deploy/deployfiles/files.go
cli/internal/deploy/deployfiles/sync_test.go
cli/internal/deploy/dockercmd/compose.go
cli/internal/deploy/dockercmd/docker.go
cli/internal/deploy/dockercmd/dockercmd_test.go
cli/internal/deploy/dockercmd/provision_darwin_ops.go
cli/internal/deploy/dockercmd/provision_linux_ops.go
cli/internal/deploy/dockercmd/provision_windows_ops.go
cli/internal/deploy/dockercmd/runner.go
cli/internal/deploy/install/dev_test.go
cli/internal/deploy/install/diagnose.go
cli/internal/deploy/install/diagnose_test.go
cli/internal/deploy/install/envfile.go
cli/internal/deploy/install/envfile_test.go
cli/internal/deploy/install/files.go
cli/internal/deploy/install/install.go
cli/internal/deploy/install/install_test.go
cli/internal/deploy/install/lifecycle_test.go
cli/internal/deploy/install/logs.go
cli/internal/deploy/install/offline_test.go
cli/internal/deploy/install/options.go
cli/internal/deploy/install/override_test.go
cli/internal/deploy/install/plan.go
cli/internal/deploy/install/prod_test.go
cli/internal/deploy/install/progress.go
cli/internal/deploy/install/progress_test.go
cli/internal/deploy/install/sandbox.go
cli/internal/deploy/install/status.go
cli/internal/deploy/install/stop.go
cli/internal/deploy/install/uninstall.go
cli/internal/deploy/install/upgrade.go
cli/internal/deploy/install/upgrade_test.go
cli/internal/deploy/paths/paths.go
cli/internal/deploy/paths/paths_test.go
cli/internal/deploy/prompt/prompt.go
cli/internal/deploy/prompt/prompt_test.go
cli/internal/deploy/release/release.go
cli/internal/deploy/release/release_test.go
cli/internal/deploy/resources/disk_unix.go
cli/internal/deploy/resources/disk_windows.go
cli/internal/deploy/resources/resources.go
cli/internal/deploy/resources/resources_test.go
cli/internal/deploy/state/state.go
cli/internal/deploy/state/state_test.go
cli/internal/deploy/ui/ui.go
cli/internal/deploy/ui/ui_test.go
deployment/.gitignore
deployment/README.md
deployment/aws_ecs_fargate/cloudformation/README.md
deployment/aws_ecs_fargate/cloudformation/deploy.sh
deployment/aws_ecs_fargate/cloudformation/onyx_acm_template.yaml
deployment/aws_ecs_fargate/cloudformation/onyx_cluster_template.yaml
deployment/aws_ecs_fargate/cloudformation/onyx_config.jsonl
deployment/aws_ecs_fargate/cloudformation/onyx_efs_template.yaml
deployment/aws_ecs_fargate/cloudformation/services/onyx_backend_api_server_service_template.yaml
deployment/aws_ecs_fargate/cloudformation/services/onyx_backend_background_server_service_template.yaml
deployment/aws_ecs_fargate/cloudformation/services/onyx_model_server_indexing_service_template.yaml
deployment/aws_ecs_fargate/cloudformation/services/onyx_model_server_inference_service_template.yaml
deployment/aws_ecs_fargate/cloudformation/services/onyx_nginx_service_template.yaml
deployment/aws_ecs_fargate/cloudformation/services/onyx_postgres_service_template.yaml
deployment/aws_ecs_fargate/cloudformation/services/onyx_redis_service_template.yaml
deployment/aws_ecs_fargate/cloudformation/services/onyx_vespaengine_service_template.yaml
deployment/aws_ecs_fargate/cloudformation/services/onyx_web_server_service_template.yaml
deployment/aws_ecs_fargate/cloudformation/uninstall.sh
deployment/data/nginx/app.conf.template
deployment/data/nginx/app.conf.template.no-letsencrypt
deployment/data/nginx/app.conf.template.prod
deployment/data/nginx/mcp.conf.inc.template
deployment/data/nginx/mcp_upstream.conf.inc.template
deployment/data/nginx/run-nginx.sh
deployment/docker_compose/README.md
deployment/docker_compose/docker-compose.airgap-test.yml
deployment/docker_compose/docker-compose.airgap-tls-test.yml
deployment/docker_compose/docker-compose.craft.yml
deployment/docker_compose/docker-compose.dev.yml
deployment/docker_compose/docker-compose.mcp-api-key-test.yml
deployment/docker_compose/docker-compose.mcp-oauth-test.yml
deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml
deployment/docker_compose/docker-compose.multitenant.yml
deployment/docker_compose/docker-compose.onyx-lite.yml
deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml
deployment/docker_compose/docker-compose.prod.yml
deployment/docker_compose/docker-compose.resources.yml
deployment/docker_compose/docker-compose.search-testing.yml
deployment/docker_compose/docker-compose.template.yml
deployment/docker_compose/docker-compose.yml
deployment/docker_compose/env.nginx.template
deployment/docker_compose/env.prod.template
deployment/docker_compose/env.template
deployment/docker_compose/init-letsencrypt.sh
deployment/docker_compose/install.ps1
deployment/docker_compose/install.sh
deployment/helm/MIGRATION.md
deployment/helm/README.md
deployment/helm/charts/onyx-cnpg-crds/Chart.yaml
deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml
deployment/helm/charts/onyx-cnpg-crds/values.yaml
deployment/helm/charts/onyx/.gitignore
deployment/helm/charts/onyx/.helmignore
deployment/helm/charts/onyx/Chart.lock
deployment/helm/charts/onyx/Chart.yaml
deployment/helm/charts/onyx/SIZING.md
deployment/helm/charts/onyx/ci/ct-values.yaml
deployment/helm/charts/onyx/dashboards/indexing-pipeline.json
deployment/helm/charts/onyx/dashboards/indexing-pruning.json
deployment/helm/charts/onyx/dashboards/opensearch-search-latency.json
deployment/helm/charts/onyx/dashboards/redis-queues.json
deployment/helm/charts/onyx/scripts/check-cnpg-crds.sh
deployment/helm/charts/onyx/templates/_helpers.tpl
deployment/helm/charts/onyx/templates/api-deployment.yaml
deployment/helm/charts/onyx/templates/api-hpa.yaml
deployment/helm/charts/onyx/templates/api-scaledobject.yaml
deployment/helm/charts/onyx/templates/api-service.yaml
deployment/helm/charts/onyx/templates/api-servicemonitor.yaml
deployment/helm/charts/onyx/templates/auth-secrets.yaml
deployment/helm/charts/onyx/templates/celery-beat.yaml
deployment/helm/charts/onyx/templates/celery-worker-docfetching-hpa.yaml
deployment/helm/charts/onyx/templates/celery-worker-docfetching-metrics-service.yaml
deployment/helm/charts/onyx/templates/celery-worker-docfetching-scaledobject.yaml
deployment/helm/charts/onyx/templates/celery-worker-docfetching.yaml
deployment/helm/charts/onyx/templates/celery-worker-docprocessing-hpa.yaml
deployment/helm/charts/onyx/templates/celery-worker-docprocessing-metrics-service.yaml
deployment/helm/charts/onyx/templates/celery-worker-docprocessing-scaledobject.yaml
deployment/helm/charts/onyx/templates/celery-worker-docprocessing.yaml
deployment/helm/charts/onyx/templates/celery-worker-heavy-hpa.yaml
deployment/helm/charts/onyx/templates/celery-worker-heavy-metrics-service.yaml
deployment/helm/charts/onyx/templates/celery-worker-heavy-scaledobject.yaml
deployment/helm/charts/onyx/templates/celery-worker-heavy.yaml
deployment/helm/charts/onyx/templates/celery-worker-light-hpa.yaml
deployment/helm/charts/onyx/templates/celery-worker-light-metrics-service.yaml
deployment/helm/charts/onyx/templates/celery-worker-light-scaledobject.yaml
deployment/helm/charts/onyx/templates/celery-worker-light.yaml
deployment/helm/charts/onyx/templates/celery-worker-monitoring-hpa.yaml
deployment/helm/charts/onyx/templates/celery-worker-monitoring-metrics-service.yaml
deployment/helm/charts/onyx/templates/celery-worker-monitoring-scaledobject.yaml
deployment/helm/charts/onyx/templates/celery-worker-monitoring.yaml
deployment/helm/charts/onyx/templates/celery-worker-primary-hpa.yaml
deployment/helm/charts/onyx/templates/celery-worker-primary-metrics-service.yaml
deployment/helm/charts/onyx/templates/celery-worker-primary-scaledobject.yaml
deployment/helm/charts/onyx/templates/celery-worker-primary.yaml
deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks-hpa.yaml
deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks-metrics-service.yaml
deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks-scaledobject.yaml
deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks.yaml
deployment/helm/charts/onyx/templates/celery-worker-servicemonitors.yaml
deployment/helm/charts/onyx/templates/celery-worker-user-file-processing-hpa.yaml
deployment/helm/charts/onyx/templates/celery-worker-user-file-processing-scaledobject.yaml
deployment/helm/charts/onyx/templates/celery-worker-user-file-processing.yaml
deployment/helm/charts/onyx/templates/configmap.yaml
deployment/helm/charts/onyx/templates/craft-kubernetes-version-check.yaml
deployment/helm/charts/onyx/templates/craft-validation.yaml
deployment/helm/charts/onyx/templates/discordbot.yaml
deployment/helm/charts/onyx/templates/external-secret.yaml
deployment/helm/charts/onyx/templates/extra-manifests.yaml
deployment/helm/charts/onyx/templates/grafana-dashboards.yaml
deployment/helm/charts/onyx/templates/indexing-model-deployment.yaml
deployment/helm/charts/onyx/templates/indexing-model-service.yaml
deployment/helm/charts/onyx/templates/inference-model-deployment.yaml
deployment/helm/charts/onyx/templates/inference-model-service.yaml
deployment/helm/charts/onyx/templates/ingress-api.yaml
deployment/helm/charts/onyx/templates/ingress-mcp-oauth-callback.yaml
deployment/helm/charts/onyx/templates/ingress-mcp.yaml
deployment/helm/charts/onyx/templates/ingress-scim.yaml
deployment/helm/charts/onyx/templates/ingress-webserver.yaml
deployment/helm/charts/onyx/templates/legacy-vespa-check.yaml
deployment/helm/charts/onyx/templates/lets-encrypt.yaml
deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml
deployment/helm/charts/onyx/templates/mcp-server-service.yaml
deployment/helm/charts/onyx/templates/mcp-server-servicemonitor.yaml
deployment/helm/charts/onyx/templates/network-policy-sandbox-egress.yaml
deployment/helm/charts/onyx/templates/network-policy-sandbox-push.yaml
deployment/helm/charts/onyx/templates/nginx-conf.yaml
deployment/helm/charts/onyx/templates/postgres-cluster.yaml
deployment/helm/charts/onyx/templates/pre-delete-cleanup.yaml
deployment/helm/charts/onyx/templates/redis-tls-validation.yaml
deployment/helm/charts/onyx/templates/sandbox-image-prepuller.yaml
deployment/helm/charts/onyx/templates/sandbox-namespace.yaml
deployment/helm/charts/onyx/templates/sandbox-podtemplate.yaml
deployment/helm/charts/onyx/templates/sandbox-proxy/deployment.yaml
deployment/helm/charts/onyx/templates/sandbox-proxy/networkpolicy-egress.yaml
deployment/helm/charts/onyx/templates/sandbox-proxy/networkpolicy.yaml
deployment/helm/charts/onyx/templates/sandbox-proxy/pdb.yaml
deployment/helm/charts/onyx/templates/sandbox-proxy/rbac.yaml
deployment/helm/charts/onyx/templates/sandbox-proxy/service.yaml
deployment/helm/charts/onyx/templates/sandbox-rbac.yaml
deployment/helm/charts/onyx/templates/serviceaccount.yaml
deployment/helm/charts/onyx/templates/slackbot.yaml
deployment/helm/charts/onyx/templates/tests/test-connection.yaml
deployment/helm/charts/onyx/templates/tooling-pginto-configmap.yaml
deployment/helm/charts/onyx/templates/webserver-deployment.yaml
deployment/helm/charts/onyx/templates/webserver-hpa.yaml
deployment/helm/charts/onyx/templates/webserver-scaledobject.yaml
deployment/helm/charts/onyx/templates/webserver-service.yaml
deployment/helm/charts/onyx/templates_disabled/background-deployment.yaml
deployment/helm/charts/onyx/templates_disabled/background-hpa.yaml
deployment/helm/charts/onyx/templates_disabled/onyx-secret.yaml
deployment/helm/charts/onyx/values-ci.yaml
deployment/helm/charts/onyx/values-lite.yaml
deployment/helm/charts/onyx/values.yaml
deployment/helm/dev/craft-down.sh
deployment/helm/dev/craft-up.sh
deployment/helm/dev/k8s-down.sh
deployment/helm/dev/k8s-up.sh
deployment/helm/dev/refresh-images.sh
deployment/helm/dev/values-localdev.yaml
deployment/terraform/modules/aws/README.md
deployment/terraform/modules/aws/eks/main.tf
deployment/terraform/modules/aws/eks/outputs.tf
```
## Security-Relevant Path Candidates
Bounded to first 300 path matches.
These are path-name heuristics, not validated security controls.
```text
.claude/claude-security-guidance.md
.secretsignore
SECURITY.md
backend/alembic/run_multitenant_migrations.py
backend/alembic/versions/01c63968ff8f_add_ssrf_protection_level_to_security_.py
backend/alembic/versions/03d710ccf29c_add_permission_sync_attempt_tables.py
backend/alembic/versions/1c36b3dc2f4e_add_full_exception_trace_to_permission_.py
backend/alembic/versions/1cb59a95b250_add_security_settings_table.py
backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py
backend/alembic/versions/25a5501dc766_group_permissions_phase1.py
backend/alembic/versions/2666d766cb9b_google_oauth2.py
backend/alembic/versions/27c6ecc08586_permission_framework.py
backend/alembic/versions/287021f3b46c_add_voice_provider_api_secret.py
backend/alembic/versions/2f80c6a2550f_add_chat_session_specific_temperature_.py
backend/alembic/versions/38eda64af7fe_add_chat_session_sharing.py
backend/alembic/versions/3d1cca026fe8_add_oauth_config_and_user_tokens.py
backend/alembic/versions/465f78d9b7f9_larger_access_tokens_for_oauth.py
backend/alembic/versions/4a951134c801_moved_status_to_connector_credential_.py
backend/alembic/versions/4ea2c93919c1_add_type_to_credentials.py
backend/alembic/versions/503883791c39_add_effective_permissions.py
backend/alembic/versions/5809c0787398_add_chat_sessions.py
backend/alembic/versions/5e1c073d48a3_add_personal_access_token_table.py
backend/alembic/versions/61ff3651add4_add_permission_syncing.py
backend/alembic/versions/6756efa39ada_id_uuid_for_chat_session.py
backend/alembic/versions/6d387b3196c2_basic_auth.py
backend/alembic/versions/703313b75876_add_tokenratelimit_tables.py
backend/alembic/versions/72bdc9929a46_permission_auto_sync_framework.py
backend/alembic/versions/767f1c2a00eb_count_chat_tokens.py
backend/alembic/versions/77962d18fd41_add_run_id_to_credential_capability_.py
backend/alembic/versions/795b20b85b4b_add_llm_group_permissions_control.py
backend/alembic/versions/800f48024ae9_add_id_to_connectorcredentialpair.py
backend/alembic/versions/80696cf850ae_add_chat_session_to_query_event.py
backend/alembic/versions/849b21c732f8_add_demo_data_enabled_to_build_session.py
backend/alembic/versions/8a87bd6ec550_associate_index_attempts_with_ccpair.py
backend/alembic/versions/8d1297b43210_add_cache_creation_tokens_to_user_usage.py
backend/alembic/versions/8f2c4a1d9e3b_agent_sharing_permissions_and_ownership.py
backend/alembic/versions/8f3b2c91d4e7_backfill_legacy_callback_on_seeded_sso_.py
backend/alembic/versions/9cc89a7b96de_track_stale_build_session_skills.py
backend/alembic/versions/a4c9d2e7f1b8_skill_sharing_permissions.py
backend/alembic/versions/b02d7b35e48b_add_opencode_serve_fields_to_build_session.py
backend/alembic/versions/b30353be4eec_add_mcp_auth_performer.py
backend/alembic/versions/b4950827c0dd_encrypt_external_app_credentials.py
backend/alembic/versions/b4ef3ae0bf6e_add_user_oauth_token_to_slack_bot.py
backend/alembic/versions/b8a5e7068be5_add_scopes_to_personal_access_token.py
backend/alembic/versions/c2cc933f0a40_add_chat_session_reasoning_effort_override.py
backend/alembic/versions/c7f2e1b4a9d3_add_sharing_scope_to_build_session.py
backend/alembic/versions/c8e316473aaa_make_user_role_nullable.py
backend/alembic/versions/cf90764725d8_larger_refresh_tokens.py
backend/alembic/versions/df90f43d9ab2_add_credential_capability_report_table.py
backend/alembic/versions/dfbe9e93d3c7_extended_role_for_non_web.py
backend/alembic/versions/e0ea2ae62e51_add_index_on_chat_session_user_id_and_.py
backend/alembic/versions/e4ed20ddae7c_swap_credentials_hierarchy_fk_on_update_.py
backend/alembic/versions/e7c00417d1e5_add_jwt_auth_columns_to_security_.py
backend/alembic/versions/e86866a9c78a_add_persona_to_chat_session.py
backend/alembic/versions/e8f0d2a38171_add_status_to_mcp_server_and_make_auth_.py
backend/alembic/versions/ea9771dd828c_associate_external_apps_with_skills.py
backend/alembic/versions/ecab2b3f1a3b_add_overrides_to_the_chat_session.py
backend/alembic/versions/f1ca58b2f2ec_add_passthrough_auth_to_tool.py
backend/alembic/versions/f57f35403f6c_add_index_on_chat_message_chat_session_.py
backend/alembic/versions/f6b0949ea33d_copy_telemetry_secrets_to_encrypted_kv.py
backend/alembic/versions/f7ca3e2f45d9_migrate_no_auth_data_to_placeholder.py
backend/alembic/versions/feead2911109_add_opensearch_tenant_migration_columns.py
backend/alembic_tenants/README.md
backend/alembic_tenants/__init__.py
backend/alembic_tenants/env.py
backend/alembic_tenants/script.py.mako
backend/alembic_tenants/versions/14a83a331951_create_usertenantmapping_table.py
backend/alembic_tenants/versions/34e3630c7f32_lowercase_multi_tenant_user_auth.py
backend/alembic_tenants/versions/3b45e0018bf1_add_new_available_tenant_table.py
backend/alembic_tenants/versions/3b9f09038764_add_read_only_kg_user.py
backend/alembic_tenants/versions/8f3d2c7b91ae_add_user_tenant_mapping_oauth_account.py
backend/alembic_tenants/versions/a4f6ee863c47_mapping_for_anonymous_user_path.py
backend/alembic_tenants/versions/a754e4f72e60_add_tenant_sso_domain_routing.py
backend/alembic_tenants/versions/ac842f85f932_new_column_user_tenant_mapping.py
backend/alembic_tenants/versions/b1c4e9d72f38_add_tenant_shard_map.py
backend/alembic_tenants/versions/d4e7a92c1b38_add_tenant_invite_counter.py
backend/ee/onyx/auth/__init__.py
backend/ee/onyx/auth/sso_domain_verification.py
backend/ee/onyx/auth/users.py
backend/ee/onyx/background/celery/tasks/doc_permission_syncing/__init__.py
backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py
backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/__init__.py
backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py
backend/ee/onyx/background/celery/tasks/tenant_provisioning/__init__.py
backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py
backend/ee/onyx/configs/multi_tenant_gating_config.py
backend/ee/onyx/db/connector_credential_pair.py
backend/ee/onyx/db/tenant_sso_domain.py
backend/ee/onyx/db/token_limit.py
backend/ee/onyx/db/user_tenant_mapping.py
backend/ee/onyx/external_permissions/__init__.py
backend/ee/onyx/external_permissions/box/access.py
backend/ee/onyx/external_permissions/box/doc_sync.py
backend/ee/onyx/external_permissions/box/group_sync.py
backend/ee/onyx/external_permissions/canvas/access.py
backend/ee/onyx/external_permissions/canvas/doc_sync.py
backend/ee/onyx/external_permissions/canvas/group_sync.py
backend/ee/onyx/external_permissions/confluence/__init__.py
backend/ee/onyx/external_permissions/confluence/constants.py
backend/ee/onyx/external_permissions/confluence/doc_sync.py
backend/ee/onyx/external_permissions/confluence/group_sync.py
backend/ee/onyx/external_permissions/confluence/page_access.py
backend/ee/onyx/external_permissions/confluence/space_access.py
backend/ee/onyx/external_permissions/github/doc_sync.py
backend/ee/onyx/external_permissions/github/group_sync.py
backend/ee/onyx/external_permissions/github/utils.py
backend/ee/onyx/external_permissions/gmail/doc_sync.py
backend/ee/onyx/external_permissions/google_drive/__init__.py
backend/ee/onyx/external_permissions/google_drive/doc_sync.py
backend/ee/onyx/external_permissions/google_drive/folder_retrieval.py
backend/ee/onyx/external_permissions/google_drive/group_sync.py
backend/ee/onyx/external_permissions/google_drive/models.py
backend/ee/onyx/external_permissions/google_drive/permission_retrieval.py
backend/ee/onyx/external_permissions/jira/__init__.py
backend/ee/onyx/external_permissions/jira/doc_sync.py
backend/ee/onyx/external_permissions/jira/group_sync.py
backend/ee/onyx/external_permissions/jira/models.py
backend/ee/onyx/external_permissions/jira/page_access.py
backend/ee/onyx/external_permissions/microsoft_utils/__init__.py
backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py
backend/ee/onyx/external_permissions/perm_sync_types.py
backend/ee/onyx/external_permissions/post_query_censoring.py
backend/ee/onyx/external_permissions/salesforce/postprocessing.py
backend/ee/onyx/external_permissions/salesforce/utils.py
backend/ee/onyx/external_permissions/sharepoint/doc_sync.py
backend/ee/onyx/external_permissions/sharepoint/group_sync.py
backend/ee/onyx/external_permissions/sharepoint/permission_utils.py
backend/ee/onyx/external_permissions/slack/channel_access.py
backend/ee/onyx/external_permissions/slack/doc_sync.py
backend/ee/onyx/external_permissions/slack/group_sync.py
backend/ee/onyx/external_permissions/slack/utils.py
backend/ee/onyx/external_permissions/sync_params.py
backend/ee/onyx/external_permissions/teams/doc_sync.py
backend/ee/onyx/external_permissions/utils.py
backend/ee/onyx/server/auth_check.py
backend/ee/onyx/server/middleware/tenant_tracking.py
backend/ee/onyx/server/oauth/api.py
backend/ee/onyx/server/oauth/api_router.py
backend/ee/onyx/server/oauth/confluence_cloud.py
backend/ee/onyx/server/oauth/google_drive.py
backend/ee/onyx/server/oauth/slack.py
backend/ee/onyx/server/query_and_chat/token_limit.py
backend/ee/onyx/server/scim/auth.py
backend/ee/onyx/server/tenant_usage_limits.py
backend/ee/onyx/server/tenants/__init__.py
backend/ee/onyx/server/tenants/access.py
backend/ee/onyx/server/tenants/admin_api.py
backend/ee/onyx/server/tenants/anonymous_user_path.py
backend/ee/onyx/server/tenants/anonymous_users_api.py
backend/ee/onyx/server/tenants/api.py
backend/ee/onyx/server/tenants/billing.py
backend/ee/onyx/server/tenants/billing_api.py
backend/ee/onyx/server/tenants/models.py
backend/ee/onyx/server/tenants/product_gating.py
backend/ee/onyx/server/tenants/provisioning.py
backend/ee/onyx/server/tenants/proxy.py
backend/ee/onyx/server/tenants/schema_management.py
backend/ee/onyx/server/tenants/team_membership_api.py
backend/ee/onyx/server/tenants/tenant_management_api.py
backend/ee/onyx/server/tenants/tier_management.py
backend/ee/onyx/server/tenants/user_invitations_api.py
backend/ee/onyx/server/token_rate_limits/api.py
backend/onyx/auth/__init__.py
backend/onyx/auth/anonymous_user.py
backend/onyx/auth/api_key.py
backend/onyx/auth/captcha.py
backend/onyx/auth/constants.py
backend/onyx/auth/disposable_email_validator.py
backend/onyx/auth/email_utils.py
backend/onyx/auth/invited_users.py
backend/onyx/auth/jwt.py
backend/onyx/auth/login_claims_capture.py
backend/onyx/auth/mobile_sso/__init__.py
backend/onyx/auth/mobile_sso/code_store.py
backend/onyx/auth/mobile_sso/sso_completion.py
backend/onyx/auth/mobile_sso/tokens.py
backend/onyx/auth/oauth_refresher.py
backend/onyx/auth/oauth_token_manager.py
backend/onyx/auth/oidc_client.py
backend/onyx/auth/pat.py
backend/onyx/auth/permission_projection.py
backend/onyx/auth/permissions.py
backend/onyx/auth/pkce.py
backend/onyx/auth/schemas.py
backend/onyx/auth/scoped_permissions.py
backend/onyx/auth/session_tokens.py
backend/onyx/auth/signup_rate_limit.py
backend/onyx/auth/sso_tenant_token.py
backend/onyx/auth/sso_url_guard.py
backend/onyx/auth/sso_web_error.py
backend/onyx/auth/users.py
backend/onyx/auth/utils.py
backend/onyx/chat/citation_processor.py
backend/onyx/chat/token_budget.py
backend/onyx/connectors/credentials_provider.py
backend/onyx/connectors/google_utils/google_auth.py
backend/onyx/connectors/microsoft_utils/graph_auth.py
backend/onyx/connectors/salesforce/OAUTH.md
backend/onyx/connectors/salesforce/auth.py
backend/onyx/connectors/zoom/recordings/session_types.py
backend/onyx/db/auth.py
backend/onyx/db/connector_credential_pair.py
backend/onyx/db/credential_capability.py
backend/onyx/db/credentials.py
backend/onyx/db/engine/iam_auth.py
backend/onyx/db/engine/tenant_utils.py
backend/onyx/db/oauth_config.py
backend/onyx/db/permission_sync_attempt.py
backend/onyx/db/permissions.py
backend/onyx/db/scoped_permissions.py
backend/onyx/db/security_settings.py
backend/onyx/db/sso_provider.py
backend/onyx/db/tenant_invite_counter.py
backend/onyx/db/tenant_shard.py
backend/onyx/db/token_limit.py
backend/onyx/external_apps/credentials.py
backend/onyx/external_apps/token_refresh.py
backend/onyx/external_apps/token_utils.py
backend/onyx/federated_connectors/oauth_utils.py
backend/onyx/llm/prompt_cache/processor.py
backend/onyx/mcp_server/auth.py
backend/onyx/oauth/authorization_attempt.py
backend/onyx/oauth/models.py
backend/onyx/onyxbot/discord/DISCORD_MULTITENANT_README.md
backend/onyx/redis/iam_auth.py
backend/onyx/redis/redis_tenant_work_gating.py
backend/onyx/redis/tenant_redis_client.py
backend/onyx/sandbox_proxy/credential_injection.py
backend/onyx/secondary_llm_flows/chat_session_naming.py
backend/onyx/server/auth/__init__.py
backend/onyx/server/auth/captcha_api.py
backend/onyx/server/auth/mobile.py
backend/onyx/server/auth_check.py
backend/onyx/server/documents/credential.py
backend/onyx/server/documents/credential_capabilities.py
backend/onyx/server/documents/standard_oauth.py
backend/onyx/server/features/build/db/build_session.py
backend/onyx/server/features/build/external_apps/oauth.py
backend/onyx/server/features/build/sandbox/image/opencode-plugins/session-proxy-tag.ts
backend/onyx/server/features/build/sandbox/session_workspace.py
backend/onyx/server/features/build/session/api.py
backend/onyx/server/features/build/session/errors.py
backend/onyx/server/features/build/session/interrupt_signal.py
backend/onyx/server/features/build/session/llm_config.py
backend/onyx/server/features/build/session/locks.py
backend/onyx/server/features/build/session/manager.py
backend/onyx/server/features/build/session/md_to_docx.py
backend/onyx/server/features/build/session/messages.py
backend/onyx/server/features/build/session/models.py
backend/onyx/server/features/build/session/naming.py
backend/onyx/server/features/build/session/sandbox_lifecycle.py
backend/onyx/server/features/build/session/session_ready.py
backend/onyx/server/features/build/session/streaming.py
backend/onyx/server/features/mcp/credentials.py
backend/onyx/server/features/mcp/oauth.py
backend/onyx/server/features/mcp/oauth_flow.py
backend/onyx/server/features/oauth_config/__init__.py
backend/onyx/server/features/oauth_config/api.py
backend/onyx/server/features/oauth_config/models.py
backend/onyx/server/features/user_oauth_token/__init__.py
backend/onyx/server/features/user_oauth_token/api.py
backend/onyx/server/manage/oauth_test.py
backend/onyx/server/manage/sso/__init__.py
backend/onyx/server/manage/sso/api.py
backend/onyx/server/manage/sso/models.py
backend/onyx/server/manage/validate_tokens.py
backend/onyx/server/metrics/metrics_auth.py
backend/onyx/server/metrics/per_tenant.py
backend/onyx/server/query_and_chat/session_loading.py
backend/onyx/server/query_and_chat/token_limit.py
backend/onyx/server/security/__init__.py
backend/onyx/server/security/api.py
backend/onyx/server/security/models.py
backend/onyx/server/security/store.py
backend/onyx/server/sso_discovery.py
backend/onyx/server/tenant_usage_limits.py
backend/onyx/server/token_rate_limits/models.py
backend/onyx/tracing/braintrust_tracing_processor.py
backend/onyx/tracing/dynamic_processor.py
backend/onyx/tracing/framework/processor_interface.py
backend/onyx/tracing/langfuse_tracing_processor.py
backend/onyx/tracing/processors/__init__.py
backend/onyx/tracing/processors/user_usage_processor.py
backend/onyx/utils/credential_audit.py
backend/onyx/utils/jsonriver/tokenize.py
backend/onyx/utils/tenant.py
backend/scripts/debugging/onyx_list_tenants.py
backend/scripts/reencrypt_secrets.py
backend/scripts/tenant_cleanup/QUICK_START_NO_BASTION.md
backend/scripts/tenant_cleanup/README.md
backend/scripts/tenant_cleanup/activity_utils.py
backend/scripts/tenant_cleanup/check_no_bastion_setup.py
backend/scripts/tenant_cleanup/no_bastion_analyze_tenants.py
backend/scripts/tenant_cleanup/no_bastion_cleanup_tenants.py
backend/scripts/tenant_cleanup/no_bastion_cleanup_utils.py
backend/scripts/tenant_cleanup/no_bastion_mark_connectors.py
backend/scripts/tenant_cleanup/on_pod_scripts/check_documents_deleted.py
backend/scripts/tenant_cleanup/on_pod_scripts/check_tenant_activity.py
backend/scripts/tenant_cleanup/on_pod_scripts/cleanup_tenant_schema.py
backend/scripts/tenant_cleanup/on_pod_scripts/execute_connector_deletion.py
```
## AI / RAG / Agent / Tool Path Candidates
Bounded to first 400 path matches.
These are discovery candidates only. Runtime roles remain unverified.
```text
.cursor/mcp.json
.github/actions/build-model-server-image/action.yml
.github/actions/run-nightly-provider-chat-test/action.yml
.github/workflows/nightly-llm-provider-chat.yml
.github/workflows/pr-connector-filter-eval.yml
.github/workflows/pr-python-connector-tests.yml
.github/workflows/pr-python-model-tests.yml
.github/workflows/pr-recommended-models-chat-test.yml
.github/workflows/release-devtools.yml
.github/workflows/reusable-nightly-llm-provider-chat.yml
.github/workflows/update-recommended-models.yml
.mcp.json
AGENTS.md
backend/AGENTS.md
backend/Dockerfile.model_server
backend/alembic/versions/0568ccf46a6b_add_thread_specific_model_selection.py
backend/alembic/versions/05c07bf07c00_add_search_doc_relevance_details.py
backend/alembic/versions/06a38a307492_add_chat_message_request_params.py
backend/alembic/versions/0816326d83aa_add_federated_connector_tables.py
backend/alembic/versions/08a1eda20fe1_add_earliest_indexing_to_connector.py
backend/alembic/versions/0a2b51deb0b8_add_starter_prompts.py
backend/alembic/versions/0ec213a5ffde_add_incognito_record_mode_to_chat_.py
backend/alembic/versions/177de57c21c9_display_custom_llm_models.py
backend/alembic/versions/18b5b2524446_add_is_clarification_to_chat_message.py
backend/alembic/versions/19c0ccb01687_migrate_to_contextual_rag_model.py
backend/alembic/versions/1a03d2c2856b_add_indexes_to_document__tag.py
backend/alembic/versions/1f2a3b4c5d6e_add_internet_search_and_content_providers.py
backend/alembic/versions/1f60f60c3401_embedding_model_search_settings.py
backend/alembic/versions/20f09b642ed0_backfill_write_chat_for_limited_service_.py
backend/alembic/versions/2955778aa44c_add_chunk_count_to_document.py
backend/alembic/versions/2a391f840e85_add_last_refreshed_at_mcp_server.py
backend/alembic/versions/2c2430828bdf_add_unique_constraint_to_inputprompt_.py
backend/alembic/versions/2f80c6a2550f_add_chat_session_specific_temperature_.py
backend/alembic/versions/33cb72ea4d80_single_tool_call_per_message.py
backend/alembic/versions/33ea50e88f24_foreign_key_input_prompts.py
backend/alembic/versions/3879338f8ba1_add_tool_table.py
backend/alembic/versions/38eda64af7fe_add_chat_session_sharing.py
backend/alembic/versions/3934b1bc7b62_update_github_connector_repo_name_to_.py
backend/alembic/versions/3a7802814195_add_alternate_assistant_to_chat_message.py
backend/alembic/versions/3a9b8d7c6e5f_add_mcp_known_provider_fields.py
backend/alembic/versions/3c5e35aa9af0_polling_document_count.py
backend/alembic/versions/3c6531f32351_add_back_input_prompts.py
backend/alembic/versions/3fc5d75723b3_add_doc_metadata_field_in_document_model.py
backend/alembic/versions/401c1ac29467_add_tables_for_ui_based_llm_.py
backend/alembic/versions/40926a4dab77_reset_userfile_document_id_migrated_.py
backend/alembic/versions/41fa44bef321_remove_default_prompt_shortcuts.py
backend/alembic/versions/44f856ae2a4a_add_cloud_embedding_model.py
backend/alembic/versions/473a1a7ca408_add_display_model_names_to_llm_provider.py
backend/alembic/versions/4794bc13e484_update_prompt_length.py
backend/alembic/versions/47a07e1a38f1_fix_invalid_model_configurations_state.py
backend/alembic/versions/48d14957fe80_add_support_for_custom_tools.py
backend/alembic/versions/4a951134c801_moved_status_to_connector_credential_.py
backend/alembic/versions/4cebcbc9b2ae_add_tab_index_to_tool_call.py
backend/alembic/versions/4f8a2b3c1d9e_add_open_url_tool.py
backend/alembic/versions/4ff2545411ad_contextual_rag_model_configuration_fk.py
backend/alembic/versions/50b683a8295c_add_additional_retrieval_controls_to_.py
backend/alembic/versions/52a219fb5233_add_last_synced_and_last_modified_to_document_table.py
backend/alembic/versions/565c5b57a573_add_available_in_craft_to_mcp_server.py
backend/alembic/versions/57122d037335_add_python_tool_on_default.py
backend/alembic/versions/57b53544726e_add_document_set_tables.py
backend/alembic/versions/5809c0787398_add_chat_sessions.py
backend/alembic/versions/5ae8240accb3_add_research_agent_database_tables_and_.py
backend/alembic/versions/5b29123cd710_nullable_search_settings_for_historic_.py
backend/alembic/versions/5e6f7a8b9c0d_update_default_persona_prompt.py
backend/alembic/versions/5f4b8568a221_add_removed_documents_to_index_attempt.py
backend/alembic/versions/62c3a055a141_add_file_names_to_file_connector_config.py
backend/alembic/versions/643a84a42a33_add_user_configured_names_to_llmprovider.py
backend/alembic/versions/64bd5677aeb6_add_image_input_support_to_model_config.py
backend/alembic/versions/66a70ddc0652_user_chat_defaults.py
backend/alembic/versions/6756efa39ada_id_uuid_for_chat_session.py
backend/alembic/versions/699221885109_nullify_default_task_prompt.py
backend/alembic/versions/73e9983e5091_add_search_query_table.py
backend/alembic/versions/7477a5f5d728_added_model_defaults_for_users.py
backend/alembic/versions/7547d982db8f_chat_folders.py
backend/alembic/versions/767f1c2a00eb_count_chat_tokens.py
backend/alembic/versions/78ebc66946a0_remove_reranking_from_search_settings.py
backend/alembic/versions/795b20b85b4b_add_llm_group_permissions_control.py
backend/alembic/versions/7a70b7664e37_add_model_configuration_table.py
backend/alembic/versions/7bd55f264e1b_add_display_name_to_model_configuration.py
backend/alembic/versions/7cb492013621_code_interpreter_server_model.py
backend/alembic/versions/7ccea01261f6_store_chat_retrieval_docs.py
backend/alembic/versions/7e490836d179_nullify_default_system_prompt.py
backend/alembic/versions/7ed603b64d5a_add_mcp_server_and_connection_config_.py
backend/alembic/versions/7f99be1cb9f5_add_index_for_getting_documents_just_by_.py
backend/alembic/versions/800f48024ae9_add_id_to_connectorcredentialpair.py
backend/alembic/versions/80696cf850ae_add_chat_session_to_query_event.py
backend/alembic/versions/8188861f4e92_csv_to_tabular_chat_file_type.py
backend/alembic/versions/81c4872d9666_add_search_settings_port_columns.py
backend/alembic/versions/87c52ec39f84_update_default_system_prompt.py
backend/alembic/versions/8aabb57f3b49_restructure_document_indices.py
backend/alembic/versions/8e1ac4f39a9f_enable_contextual_retrieval.py
backend/alembic/versions/8e26726b7683_chat_context_addition.py
backend/alembic/versions/8f2c4a1d9e3b_agent_sharing_permissions_and_ownership.py
backend/alembic/versions/904451035c9b_store_tool_details.py
backend/alembic/versions/90b409d06e50_add_chat_compression_fields.py
backend/alembic/versions/91d150c361f6_add_file_id_to_documents.py
backend/alembic/versions/91fd3b470d1a_remove_documentsource_from_tag.py
backend/alembic/versions/947b94d2ebf1_cascade_document_set_group_deletion.py
backend/alembic/versions/94dc3d0236f8_make_document_set_description_optional.py
backend/alembic/versions/9618d5038140_add_custom_display_name_to_model_.py
backend/alembic/versions/96a5702df6aa_mcp_tool_enabled.py
backend/alembic/versions/98a5008d8711_agent_tracking.py
backend/alembic/versions/9a0296d7421e_add_is_auto_mode_to_llm_provider.py
backend/alembic/versions/9c00a2bccb83_chat_message_agentic.py
backend/alembic/versions/9d1543a37106_add_processing_duration_seconds_to_chat_.py
backend/alembic/versions/9d97fecfab7f_added_retrieved_docs_to_query_event.py
backend/alembic/versions/9drpiiw74ljy_add_config_to_federated_connector.py
backend/alembic/versions/9f696734098f_combine_search_and_chat.py
backend/alembic/versions/a01bf2971c5d_update_default_tool_descriptions.py
backend/alembic/versions/a1b2c3d4e5f7_drop_agent_search_metrics_table.py
backend/alembic/versions/a2b3c4d5e6f7_remove_fast_default_model_name.py
backend/alembic/versions/a3f8b2c1d4e5_add_preferred_response_id_to_chat_message.py
backend/alembic/versions/a4f23d6b71c8_add_llm_provider_persona_restrictions.py
backend/alembic/versions/a5370af8f8a0_persona_default_model_fk.py
backend/alembic/versions/a6fcd3d631f9_replace_document_sync_index_with_partial.py
backend/alembic/versions/a7c3e2b1d4f8_remove_multilingual_expansion_from_search_settings.py
backend/alembic/versions/a852cbe15577_new_chat_history.py
backend/alembic/versions/a8c2065484e6_add_auto_scroll_to_user_model.py
backend/alembic/versions/abbfec3a5ac5_merge_prompt_into_persona.py
backend/alembic/versions/ac5eaac849f9_add_last_pruned_to_connector_table.py
backend/alembic/versions/ad99acb9be41_add_system_llm_usage.py
backend/alembic/versions/b156fa702355_chat_reworked.py
backend/alembic/versions/b30353be4eec_add_mcp_auth_performer.py
backend/alembic/versions/b51c6844d1df_seed_memory_tool.py
backend/alembic/versions/b558f51620b4_pause_finished_user_file_connectors.py
backend/alembic/versions/b6c7d8e9f0a1_drop_persona_llm_override_strings.py
backend/alembic/versions/b7e9a3c1d2f4_add_is_public_to_mcp_server.py
backend/alembic/versions/b7ec9b5b505f_adjust_prompt_length.py
backend/alembic/versions/ba98eba0f66a_add_support_for_litellm_proxy_in_.py
backend/alembic/versions/baf71f781b9e_add_llm_model_version_override_to_.py
backend/alembic/versions/bceb1e139447_add_base_url_to_cloudembeddingprovider.py
backend/alembic/versions/bd7c3bf8beba_migrate_agent_responses_to_research_.py
backend/alembic/versions/be87a654d5af_persona_new_default_model_configuration_.py
backend/alembic/versions/bf7a81109301_delete_input_prompts.py
backend/alembic/versions/c0c937d5c9e5_llm_provider_deprecate_fields.py
backend/alembic/versions/c1d2e3f4a5b6_add_deep_research_tool.py
backend/alembic/versions/c2cc933f0a40_add_chat_session_reasoning_effort_override.py
backend/alembic/versions/c5d9662b3c50_seed_craft_documentation_built_in_skill.py
backend/alembic/versions/c5eae4a75a1b_add_chat_message__standard_answer_table.py
backend/alembic/versions/c7d1f0a4b8e2_add_doc_created_at_to_document.py
backend/alembic/versions/c7e9f4a3b2d1_add_python_tool.py
backend/alembic/versions/c99d76fcd298_add_nullable_to_persona_id_in_chat_.py
backend/alembic/versions/ca04500b9ee8_add_cascade_deletes_to_agent_tables.py
backend/alembic/versions/cbc03e08d0f3_add_opensearch_migration_tables.py
backend/alembic/versions/d09fc20a3c66_seed_builtin_tools.py
backend/alembic/versions/d25168c2beee_tool_name_consistency.py
backend/alembic/versions/d3fd499c829c_add_file_reader_tool.py
backend/alembic/versions/d5c86e2c6dc6_add_cascade_delete_to_search_query_user_.py
backend/alembic/versions/d7111c1238cd_remove_document_ids.py
backend/alembic/versions/d9ec13955951_remove__dim_suffix_from_model_name.py
backend/alembic/versions/da42808081e3_migrate_jira_connectors_to_new_format.py
backend/alembic/versions/dab04867cd88_add_composite_index_to_document_by_.py
backend/alembic/versions/dba7f71618f5_onyx_custom_tool_flow.py
backend/alembic/versions/dbaa756c2ccf_embedding_models.py
backend/alembic/versions/dd55634b8532_add_per_model_llm_settings.py
backend/alembic/versions/df46c75b714e_add_default_vision_provider_to_llm_.py
backend/alembic/versions/e0a68a81d434_add_chat_feedback.py
backend/alembic/versions/e0ea2ae62e51_add_index_on_chat_session_user_id_and_.py
backend/alembic/versions/e1392f05e840_added_input_prompts.py
backend/alembic/versions/e2875ce6454b_rename_python_tool_llm_facing_name.py
backend/alembic/versions/e4334d5b33ba_add_deployment_name_to_llmprovider.py
backend/alembic/versions/e6a4bbc13fe4_add_index_for_retrieving_latest_index_.py
backend/alembic/versions/e86866a9c78a_add_persona_to_chat_session.py
backend/alembic/versions/e8f0d2a38171_add_status_to_mcp_server_and_make_auth_.py
backend/alembic/versions/e91df4e935ef_private_personas_documentsets.py
backend/alembic/versions/ea418a384b9d_add_document_content_hash.py
backend/alembic/versions/ecab2b3f1a3b_add_overrides_to_the_chat_session.py
backend/alembic/versions/ee3f4b47fad5_added_alternate_model_to_chat_message.py
backend/alembic/versions/eec4fc85ef28_add_llm_custom_config_env_injection_to_.py
backend/alembic/versions/ef7da92f7213_add_files_to_chatmessage.py
backend/alembic/versions/f0db5f1c6370_optional_llm_provider_name.py
backend/alembic/versions/f17bf3b0d9f1_embedding_provider_by_provider_type.py
backend/alembic/versions/f1ca58b2f2ec_add_passthrough_auth_to_tool.py
backend/alembic/versions/f32615f71aeb_add_custom_headers_to_tools.py
backend/alembic/versions/f3c9e59c3b07_seed_coding_agent_tool.py
backend/alembic/versions/f5437cc136c5_delete_non_search_assistants.py
backend/alembic/versions/f57f35403f6c_add_index_on_chat_message_chat_session_.py
backend/alembic/versions/f71470ba9274_add_prompt_length_limit.py
backend/alembic/versions/f8a9b2c3d4e5_add_research_answer_purpose_to_chat_message.py
backend/alembic/versions/f9b8c7d6e5a4_update_parent_question_id_foreign_key_to_research_agent_iteration.py
backend/alembic/versions/fb80bdd256de_add_chat_background_to_user.py
backend/alembic/versions/fe958f19e42b_add_mcp_config_hash_to_sandbox_and_.py
backend/alembic/versions/febe9eaa0644_add_document_set_persona_relationship_.py
backend/alembic/versions/feead2911109_add_opensearch_tenant_migration_columns.py
backend/alembic/versions/ffc707a226b4_basic_document_metadata.py
backend/ee/onyx/connectors/capability_applicability.py
backend/ee/onyx/connectors/capability_checks.py
backend/ee/onyx/connectors/perm_sync_valid.py
backend/ee/onyx/db/connector.py
backend/ee/onyx/db/connector_credential_pair.py
backend/ee/onyx/db/document.py
backend/ee/onyx/db/document_set.py
backend/ee/onyx/db/mcp.py
backend/ee/onyx/db/search.py
backend/ee/onyx/document_index/vespa/app_config/cloud-services.xml.jinja
backend/ee/onyx/external_permissions/google_drive/folder_retrieval.py
backend/ee/onyx/external_permissions/google_drive/models.py
backend/ee/onyx/external_permissions/google_drive/permission_retrieval.py
backend/ee/onyx/external_permissions/jira/models.py
backend/ee/onyx/prompts/__init__.py
backend/ee/onyx/prompts/query_expansion.py
backend/ee/onyx/prompts/search_flow_classification.py
backend/ee/onyx/search/process_search_query.py
backend/ee/onyx/secondary_llm_flows/__init__.py
backend/ee/onyx/secondary_llm_flows/query_expansion.py
backend/ee/onyx/secondary_llm_flows/search_flow_classification.py
backend/ee/onyx/server/billing/models.py
backend/ee/onyx/server/documents/cc_pair.py
backend/ee/onyx/server/enterprise_settings/models.py
backend/ee/onyx/server/license/models.py
backend/ee/onyx/server/log_export/models.py
backend/ee/onyx/server/log_export/storage.py
backend/ee/onyx/server/query_and_chat/__init__.py
backend/ee/onyx/server/query_and_chat/models.py
backend/ee/onyx/server/query_and_chat/query_backend.py
backend/ee/onyx/server/query_and_chat/search_backend.py
backend/ee/onyx/server/query_and_chat/streaming_models.py
backend/ee/onyx/server/query_and_chat/token_limit.py
backend/ee/onyx/server/query_history/models.py
backend/ee/onyx/server/reporting/usage_export_models.py
backend/ee/onyx/server/scim/models.py
backend/ee/onyx/server/tenants/models.py
backend/ee/onyx/server/user_group/models.py
backend/model_server/__init__.py
backend/model_server/__main__.py
backend/model_server/ca_certs.py
backend/model_server/constants.py
backend/model_server/encoders.py
backend/model_server/legacy/README.md
backend/model_server/legacy/__init__.py
backend/model_server/legacy/custom_models.py
backend/model_server/legacy/onyx_torch_model.py
backend/model_server/legacy/reranker.py
backend/model_server/main.py
backend/model_server/management_endpoints.py
backend/model_server/utils.py
backend/onyx/access/models.py
backend/onyx/background/celery/tasks/connector_deletion/__init__.py
backend/onyx/background/celery/tasks/connector_deletion/tasks.py
backend/onyx/background/celery/tasks/llm_model_update/__init__.py
backend/onyx/background/celery/tasks/llm_model_update/tasks.py
backend/onyx/background/celery/tasks/models.py
backend/onyx/background/celery/tasks/opensearch_migration/__init__.py
backend/onyx/background/celery/tasks/opensearch_migration/constants.py
backend/onyx/background/celery/tasks/opensearch_migration/tasks.py
backend/onyx/background/celery/tasks/opensearch_migration/transformer.py
backend/onyx/background/celery/tasks/shared/RetryDocumentIndex.py
backend/onyx/background/celery/tasks/vespa/document_sync.py
backend/onyx/background/indexing/models.py
backend/onyx/chat/COMPRESSION.md
backend/onyx/chat/README.md
backend/onyx/chat/__init__.py
backend/onyx/chat/chat_processing_checker.py
backend/onyx/chat/chat_state.py
backend/onyx/chat/chat_utils.py
backend/onyx/chat/citation_processor.py
backend/onyx/chat/citation_utils.py
backend/onyx/chat/compression.py
backend/onyx/chat/emitter.py
backend/onyx/chat/incognito.py
backend/onyx/chat/incognito_context.py
backend/onyx/chat/llm_loop.py
backend/onyx/chat/llm_step.py
backend/onyx/chat/models.py
backend/onyx/chat/process_message.py
backend/onyx/chat/prompt_utils.py
backend/onyx/chat/save_chat.py
backend/onyx/chat/stop_signal_checker.py
backend/onyx/chat/stream_buffer.py
backend/onyx/chat/token_budget.py
backend/onyx/chat/tool_call_args_streaming.py
backend/onyx/coding_agent/__init__.py
backend/onyx/coding_agent/mock_tools.py
backend/onyx/coding_agent/models.py
backend/onyx/configs/agent_configs.py
backend/onyx/configs/chat_configs.py
backend/onyx/configs/embedding_configs.py
backend/onyx/configs/llm_configs.py
backend/onyx/configs/model_configs.py
backend/onyx/configs/research_configs.py
backend/onyx/configs/tool_configs.py
backend/onyx/connectors/README.md
backend/onyx/connectors/__init__.py
backend/onyx/connectors/airtable/airtable_connector.py
backend/onyx/connectors/asana/__init__.py
backend/onyx/connectors/asana/asana_api.py
backend/onyx/connectors/asana/connector.py
backend/onyx/connectors/axero/__init__.py
backend/onyx/connectors/axero/connector.py
backend/onyx/connectors/bitbucket/__init__.py
backend/onyx/connectors/bitbucket/connector.py
backend/onyx/connectors/bitbucket/utils.py
backend/onyx/connectors/blob/__init__.py
backend/onyx/connectors/blob/connector.py
backend/onyx/connectors/bookstack/__init__.py
backend/onyx/connectors/bookstack/client.py
backend/onyx/connectors/bookstack/connector.py
backend/onyx/connectors/box/__init__.py
backend/onyx/connectors/box/access.py
backend/onyx/connectors/box/connector.py
backend/onyx/connectors/box/models.py
backend/onyx/connectors/braintrust/__init__.py
backend/onyx/connectors/braintrust/connector.py
backend/onyx/connectors/canvas/__init__.py
backend/onyx/connectors/canvas/access.py
backend/onyx/connectors/canvas/client.py
backend/onyx/connectors/canvas/connector.py
backend/onyx/connectors/capabilities.py
backend/onyx/connectors/capability_checks/applicability.py
backend/onyx/connectors/capability_checks/models.py
backend/onyx/connectors/capability_checks/recorder.py
backend/onyx/connectors/capability_checks/registry.py
backend/onyx/connectors/capability_checks/runner.py
backend/onyx/connectors/clickup/__init__.py
backend/onyx/connectors/clickup/connector.py
backend/onyx/connectors/coda/__init__.py
backend/onyx/connectors/coda/connector.py
backend/onyx/connectors/confluence/__init__.py
backend/onyx/connectors/confluence/access.py
backend/onyx/connectors/confluence/connector.py
backend/onyx/connectors/confluence/models.py
backend/onyx/connectors/confluence/onyx_confluence.py
backend/onyx/connectors/confluence/user_profile_override.py
backend/onyx/connectors/confluence/utils.py
backend/onyx/connectors/connector_runner.py
backend/onyx/connectors/credentials_provider.py
backend/onyx/connectors/cross_connector_utils/__init__.py
backend/onyx/connectors/cross_connector_utils/miscellaneous_utils.py
backend/onyx/connectors/cross_connector_utils/rate_limit_wrapper.py
backend/onyx/connectors/cross_connector_utils/section_utils.py
backend/onyx/connectors/cross_connector_utils/tabular_section_utils.py
backend/onyx/connectors/discord/__init__.py
backend/onyx/connectors/discord/connector.py
backend/onyx/connectors/discourse/__init__.py
backend/onyx/connectors/discourse/connector.py
backend/onyx/connectors/document360/__init__.py
backend/onyx/connectors/document360/connector.py
backend/onyx/connectors/document360/utils.py
backend/onyx/connectors/dropbox/__init__.py
backend/onyx/connectors/dropbox/connector.py
backend/onyx/connectors/drupal_wiki/__init__.py
backend/onyx/connectors/drupal_wiki/connector.py
backend/onyx/connectors/drupal_wiki/models.py
backend/onyx/connectors/drupal_wiki/utils.py
backend/onyx/connectors/egnyte/connector.py
backend/onyx/connectors/exceptions.py
backend/onyx/connectors/factory.py
backend/onyx/connectors/file/__init__.py
backend/onyx/connectors/file/connector.py
backend/onyx/connectors/fireflies/__init__.py
backend/onyx/connectors/fireflies/connector.py
backend/onyx/connectors/freshdesk/__init__,py
backend/onyx/connectors/freshdesk/connector.py
backend/onyx/connectors/gitbook/__init__.py
backend/onyx/connectors/gitbook/connector.py
backend/onyx/connectors/github/__init__.py
backend/onyx/connectors/github/connector.py
backend/onyx/connectors/github/models.py
backend/onyx/connectors/github/rate_limit_utils.py
backend/onyx/connectors/github/utils.py
backend/onyx/connectors/gitlab/__init__.py
backend/onyx/connectors/gitlab/connector.py
backend/onyx/connectors/gmail/__init__.py
backend/onyx/connectors/gmail/connector.py
backend/onyx/connectors/gong/__init__.py
backend/onyx/connectors/gong/connector.py
backend/onyx/connectors/google_drive/__init__.py
backend/onyx/connectors/google_drive/connector.py
backend/onyx/connectors/google_drive/constants.py
backend/onyx/connectors/google_drive/doc_conversion.py
backend/onyx/connectors/google_drive/file_retrieval.py
backend/onyx/connectors/google_drive/models.py
backend/onyx/connectors/google_drive/section_extraction.py
backend/onyx/connectors/google_site/__init__.py
backend/onyx/connectors/google_site/connector.py
backend/onyx/connectors/google_utils/__init__.py
backend/onyx/connectors/google_utils/google_auth.py
backend/onyx/connectors/google_utils/google_kv.py
backend/onyx/connectors/google_utils/google_utils.py
backend/onyx/connectors/google_utils/resources.py
backend/onyx/connectors/google_utils/shared_constants.py
backend/onyx/connectors/guru/__init__.py
backend/onyx/connectors/guru/connector.py
backend/onyx/connectors/highspot/__init__.py
backend/onyx/connectors/highspot/client.py
backend/onyx/connectors/highspot/connector.py
backend/onyx/connectors/highspot/utils.py
backend/onyx/connectors/hubspot/__init__.py
backend/onyx/connectors/hubspot/connector.py
backend/onyx/connectors/hubspot/rate_limit.py
backend/onyx/connectors/imap/__init__.py
backend/onyx/connectors/imap/connector.py
backend/onyx/connectors/imap/models.py
backend/onyx/connectors/interfaces.py
backend/onyx/connectors/jira/__init__.py
backend/onyx/connectors/jira/access.py
backend/onyx/connectors/jira/connector.py
backend/onyx/connectors/jira/utils.py
backend/onyx/connectors/linear/__init__.py
backend/onyx/connectors/linear/connector.py
```
## Data / Queue / Storage Path Candidates
Bounded to first 300 path matches.
```text
.github/actions/login-ecr-pullthrough-cache/action.yml
.github/workflows/pr-database-tests.yml
backend/alembic/run_multitenant_migrations.py
backend/alembic/versions/08a1eda20fe1_add_earliest_indexing_to_connector.py
backend/alembic/versions/0f7ff6d75b57_add_index_to_index_attempt_time_created.py
backend/alembic/versions/14162713706c_add_index_attempt_stage_metric_table.py
backend/alembic/versions/16c37a30adf2_user_file_relationship_migration.py
backend/alembic/versions/1a03d2c2856b_add_indexes_to_document__tag.py
backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py
backend/alembic/versions/2664261bfaab_add_cache_store_table.py
backend/alembic/versions/2f95e36923e6_add_indexing_coordination.py
backend/alembic/versions/31bd8c17325e_targeted_reindex_schema.py
backend/alembic/versions/34fe28843029_craft_artifact_index_and_receipts.py
backend/alembic/versions/369644546676_add_composite_index_for_index_attempt_.py
backend/alembic/versions/3bd4c84fe72f_improved_index.py
backend/alembic/versions/43cbbb3f5e6a_rename_index_origin_to_index_recursively.py
backend/alembic/versions/47433d30de82_create_indexattempt_table.py
backend/alembic/versions/4a1e4b1c89d2_add_indexing_to_userfilestatus.py
backend/alembic/versions/4cebcbc9b2ae_add_tab_index_to_tool_call.py
backend/alembic/versions/5ae8240accb3_add_research_agent_database_tables_and_.py
backend/alembic/versions/5e84129c8be3_add_docs_indexed_column_to_index_.py
backend/alembic/versions/5f4b8568a221_add_removed_documents_to_index_attempt.py
backend/alembic/versions/6a804aeb4830_duplicated_no_harm_user_file_migration.py
backend/alembic/versions/7f99be1cb9f5_add_index_for_getting_documents_just_by_.py
backend/alembic/versions/856bcbe14d79_add_missing_fk_indexes_for_hot_tables.py
backend/alembic/versions/8a87bd6ec550_associate_index_attempts_with_ccpair.py
backend/alembic/versions/8d1297b43210_add_cache_creation_tokens_to_user_usage.py
backend/alembic/versions/8f43500ee275_add_index.py
backend/alembic/versions/a3795dce87be_migration_confluence_to_be_explicit.py
backend/alembic/versions/a6fcd3d631f9_replace_document_sync_index_with_partial.py
backend/alembic/versions/abe7378b8217_add_indexing_trigger_to_cc_pair.py
backend/alembic/versions/b3f1c9a27d84_add_index_reclaim_columns.py
backend/alembic/versions/b7c2b63c4a03_add_background_reindex_enabled_field.py
backend/alembic/versions/b85f02ec1308_fix_file_type_migration.py
backend/alembic/versions/c5b692fa265c_add_index_attempt_errors_table.py
backend/alembic/versions/c7bc8cc2921d_drop_unused_kg_indexes.py
backend/alembic/versions/c7bf5721733e_add_has_been_indexed_to_.py
backend/alembic/versions/cbc03e08d0f3_add_opensearch_migration_tables.py
backend/alembic/versions/d129f37b3d87_add_error_tracking_fields_to_index_.py
backend/alembic/versions/d61e513bef0a_add_total_docs_for_index_attempt.py
backend/alembic/versions/dab04867cd88_add_composite_index_to_document_by_.py
backend/alembic/versions/e0ea2ae62e51_add_index_on_chat_session_user_id_and_.py
backend/alembic/versions/e6a4bbc13fe4_add_index_for_retrieving_latest_index_.py
backend/alembic/versions/ec3ec2eabf7b_index_from_beginning.py
backend/alembic/versions/f13db29f3101_add_composite_index_for_last_modified_.py
backend/alembic/versions/f57f35403f6c_add_index_on_chat_message_chat_session_.py
backend/alembic/versions/feead2911109_add_opensearch_tenant_migration_columns.py
backend/ee/onyx/background/celery/apps/docfetching.py
backend/ee/onyx/background/celery/apps/docprocessing.py
backend/ee/onyx/background/celery/apps/heavy.py
backend/ee/onyx/background/celery/apps/light.py
backend/ee/onyx/background/celery/apps/monitoring.py
backend/ee/onyx/background/celery/apps/primary.py
backend/ee/onyx/background/celery/apps/scheduled_tasks.py
backend/ee/onyx/background/celery/apps/user_file_processing.py
backend/ee/onyx/background/celery/tasks/beat_schedule.py
backend/ee/onyx/background/celery/tasks/cleanup/__init__.py
backend/ee/onyx/background/celery/tasks/cleanup/tasks.py
backend/ee/onyx/background/celery/tasks/cloud/__init__.py
backend/ee/onyx/background/celery/tasks/cloud/tasks.py
backend/ee/onyx/background/celery/tasks/doc_permission_syncing/__init__.py
backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py
backend/ee/onyx/background/celery/tasks/external_group_syncing/__init__.py
backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py
backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py
backend/ee/onyx/background/celery/tasks/hooks/__init__.py
backend/ee/onyx/background/celery/tasks/hooks/tasks.py
backend/ee/onyx/background/celery/tasks/license_notifications/__init__.py
backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py
backend/ee/onyx/background/celery/tasks/license_reclaim/__init__.py
backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py
backend/ee/onyx/background/celery/tasks/log_export/tasks.py
backend/ee/onyx/background/celery/tasks/query_history/__init__.py
backend/ee/onyx/background/celery/tasks/query_history/tasks.py
backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/__init__.py
backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py
backend/ee/onyx/background/celery/tasks/tenant_provisioning/__init__.py
backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py
backend/ee/onyx/background/celery/tasks/ttl_management/__init__.py
backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py
backend/ee/onyx/background/celery/tasks/usage_reporting/__init__.py
backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py
backend/ee/onyx/background/celery/tasks/vespa/__init__.py
backend/ee/onyx/background/celery/tasks/vespa/tasks.py
backend/ee/onyx/background/celery_utils.py
backend/ee/onyx/db/__init__.py
backend/ee/onyx/db/analytics.py
backend/ee/onyx/db/connector.py
backend/ee/onyx/db/connector_credential_pair.py
backend/ee/onyx/db/document.py
backend/ee/onyx/db/document_set.py
backend/ee/onyx/db/external_perm.py
backend/ee/onyx/db/hierarchy.py
backend/ee/onyx/db/license.py
backend/ee/onyx/db/mcp.py
backend/ee/onyx/db/persona.py
backend/ee/onyx/db/query_history.py
backend/ee/onyx/db/saml.py
backend/ee/onyx/db/scim.py
backend/ee/onyx/db/search.py
backend/ee/onyx/db/standard_answer.py
backend/ee/onyx/db/tenant_sso_domain.py
backend/ee/onyx/db/token_limit.py
backend/ee/onyx/db/usage_export.py
backend/ee/onyx/db/user_group.py
backend/ee/onyx/db/user_tenant_mapping.py
backend/ee/onyx/document_index/vespa/app_config/cloud-services.xml.jinja
backend/ee/onyx/server/billing/billing_cache.py
backend/ee/onyx/server/log_export/storage.py
backend/onyx/background/celery/apps/app_base.py
backend/onyx/background/celery/apps/beat.py
backend/onyx/background/celery/apps/client.py
backend/onyx/background/celery/apps/docfetching.py
backend/onyx/background/celery/apps/docprocessing.py
backend/onyx/background/celery/apps/heavy.py
backend/onyx/background/celery/apps/light.py
backend/onyx/background/celery/apps/monitoring.py
backend/onyx/background/celery/apps/primary.py
backend/onyx/background/celery/apps/scheduled_tasks.py
backend/onyx/background/celery/apps/task_formatters.py
backend/onyx/background/celery/apps/user_file_processing.py
backend/onyx/background/celery/celery_k8s_probe.py
backend/onyx/background/celery/celery_redis.py
backend/onyx/background/celery/celery_utils.py
backend/onyx/background/celery/configs/base.py
backend/onyx/background/celery/configs/beat.py
backend/onyx/background/celery/configs/client.py
backend/onyx/background/celery/configs/docfetching.py
backend/onyx/background/celery/configs/docprocessing.py
backend/onyx/background/celery/configs/heavy.py
backend/onyx/background/celery/configs/light.py
backend/onyx/background/celery/configs/monitoring.py
backend/onyx/background/celery/configs/primary.py
backend/onyx/background/celery/configs/scheduled_tasks.py
backend/onyx/background/celery/configs/user_file_processing.py
backend/onyx/background/celery/memory_monitoring.py
backend/onyx/background/celery/tasks/beat_schedule.py
backend/onyx/background/celery/tasks/build/__init__.py
backend/onyx/background/celery/tasks/build/tasks.py
backend/onyx/background/celery/tasks/capability_checks/__init__.py
backend/onyx/background/celery/tasks/capability_checks/tasks.py
backend/onyx/background/celery/tasks/connector_deletion/__init__.py
backend/onyx/background/celery/tasks/connector_deletion/tasks.py
backend/onyx/background/celery/tasks/docfetching/__init__.py
backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py
backend/onyx/background/celery/tasks/docfetching/tasks.py
backend/onyx/background/celery/tasks/docfetching/worker_shutdown.py
backend/onyx/background/celery/tasks/docprocessing/__init__.py
backend/onyx/background/celery/tasks/docprocessing/batch_counters.py
backend/onyx/background/celery/tasks/docprocessing/heartbeat.py
backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py
backend/onyx/background/celery/tasks/docprocessing/tasks.py
backend/onyx/background/celery/tasks/docprocessing/utils.py
backend/onyx/background/celery/tasks/evals/__init__.py
backend/onyx/background/celery/tasks/evals/tasks.py
backend/onyx/background/celery/tasks/hierarchyfetching/__init__.py
backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py
backend/onyx/background/celery/tasks/index_reclaim/__init__.py
backend/onyx/background/celery/tasks/index_reclaim/tasks.py
backend/onyx/background/celery/tasks/llm_model_update/__init__.py
backend/onyx/background/celery/tasks/llm_model_update/tasks.py
backend/onyx/background/celery/tasks/models.py
backend/onyx/background/celery/tasks/monitoring/__init__.py
backend/onyx/background/celery/tasks/monitoring/tasks.py
backend/onyx/background/celery/tasks/opensearch_migration/__init__.py
backend/onyx/background/celery/tasks/opensearch_migration/constants.py
backend/onyx/background/celery/tasks/opensearch_migration/tasks.py
backend/onyx/background/celery/tasks/opensearch_migration/transformer.py
backend/onyx/background/celery/tasks/port/__init__.py
backend/onyx/background/celery/tasks/port/tasks.py
backend/onyx/background/celery/tasks/pruning/__init__.py
backend/onyx/background/celery/tasks/pruning/tasks.py
backend/onyx/background/celery/tasks/scheduled_tasks/__init__.py
backend/onyx/background/celery/tasks/scheduled_tasks/tasks.py
backend/onyx/background/celery/tasks/shared/RetryDocumentIndex.py
backend/onyx/background/celery/tasks/shared/__init__.py
backend/onyx/background/celery/tasks/shared/tasks.py
backend/onyx/background/celery/tasks/user_file_processing/__init__.py
backend/onyx/background/celery/tasks/user_file_processing/tasks.py
backend/onyx/background/celery/tasks/vespa/__init__.py
backend/onyx/background/celery/tasks/vespa/document_sync.py
backend/onyx/background/celery/tasks/vespa/tasks.py
backend/onyx/background/celery/versioned_apps/beat.py
backend/onyx/background/celery/versioned_apps/client.py
backend/onyx/background/celery/versioned_apps/docfetching.py
backend/onyx/background/celery/versioned_apps/docprocessing.py
backend/onyx/background/celery/versioned_apps/heavy.py
backend/onyx/background/celery/versioned_apps/light.py
backend/onyx/background/celery/versioned_apps/monitoring.py
backend/onyx/background/celery/versioned_apps/primary.py
backend/onyx/background/celery/versioned_apps/scheduled_tasks.py
backend/onyx/background/celery/versioned_apps/user_file_processing.py
backend/onyx/background/indexing/checkpointing_utils.py
backend/onyx/background/indexing/dask_utils.py
backend/onyx/background/indexing/index_attempt_utils.py
backend/onyx/background/indexing/job_client.py
backend/onyx/background/indexing/memory_tracer.py
backend/onyx/background/indexing/models.py
backend/onyx/background/indexing/run_docfetching.py
backend/onyx/background/indexing/run_targeted_reindex.py
backend/onyx/cache/factory.py
backend/onyx/cache/interface.py
backend/onyx/cache/locks.py
backend/onyx/cache/postgres_backend.py
backend/onyx/cache/redis_backend.py
backend/onyx/connectors/salesforce/sqlite_functions.py
backend/onyx/db/README.md
backend/onyx/db/__init__.py
backend/onyx/db/_deprecated/pg_file_store.py
backend/onyx/db/admin_banner.py
backend/onyx/db/api_key.py
backend/onyx/db/auth.py
backend/onyx/db/background_error.py
backend/onyx/db/chat.py
backend/onyx/db/chat_search.py
backend/onyx/db/chunk.py
backend/onyx/db/code_interpreter.py
backend/onyx/db/connector.py
backend/onyx/db/connector_alerts.py
backend/onyx/db/connector_credential_pair.py
backend/onyx/db/constants.py
backend/onyx/db/credential_capability.py
backend/onyx/db/credentials.py
backend/onyx/db/dal.py
backend/onyx/db/deletion_attempt.py
backend/onyx/db/discord_bot.py
backend/onyx/db/document.py
backend/onyx/db/document_access.py
backend/onyx/db/document_set.py
backend/onyx/db/encrypted_kv_store.py
backend/onyx/db/engine/__init__.py
backend/onyx/db/engine/async_sql_engine.py
backend/onyx/db/engine/connection_warmup.py
backend/onyx/db/engine/iam_auth.py
backend/onyx/db/engine/pg_ssl.py
backend/onyx/db/engine/shard_registry.py
backend/onyx/db/engine/shard_routing.py
backend/onyx/db/engine/shard_version.py
backend/onyx/db/engine/sql_engine.py
backend/onyx/db/engine/tenant_utils.py
backend/onyx/db/engine/time_utils.py
backend/onyx/db/entities.py
backend/onyx/db/entity_type.py
backend/onyx/db/enums.py
backend/onyx/db/external_app.py
backend/onyx/db/federated.py
backend/onyx/db/feedback.py
backend/onyx/db/file_content.py
backend/onyx/db/file_record.py
backend/onyx/db/gated_app.py
backend/onyx/db/hierarchy.py
backend/onyx/db/hook.py
backend/onyx/db/image_generation.py
backend/onyx/db/incognito.py
backend/onyx/db/index_attempt.py
backend/onyx/db/index_attempt_metrics.py
backend/onyx/db/index_attempt_metrics_models.py
backend/onyx/db/indexing_coordination.py
backend/onyx/db/input_prompt.py
backend/onyx/db/kg_config.py
backend/onyx/db/kg_temp_view.py
backend/onyx/db/llm.py
backend/onyx/db/llm_usage.py
backend/onyx/db/mcp.py
backend/onyx/db/memory.py
backend/onyx/db/models.py
backend/onyx/db/notification.py
backend/onyx/db/oauth_config.py
backend/onyx/db/opensearch_migration.py
backend/onyx/db/pat.py
backend/onyx/db/permission_sync_attempt.py
backend/onyx/db/permissions.py
backend/onyx/db/persona.py
backend/onyx/db/persona_sharing.py
backend/onyx/db/pinned_personas.py
backend/onyx/db/port_attempt.py
backend/onyx/db/port_orphan_candidate.py
backend/onyx/db/projects.py
backend/onyx/db/pydantic_type.py
backend/onyx/db/relationships.py
backend/onyx/db/release_notes.py
backend/onyx/db/rotate_encryption_key.py
backend/onyx/db/saml.py
backend/onyx/db/scheduled_task.py
backend/onyx/db/scoped_permissions.py
backend/onyx/db/search_settings.py
backend/onyx/db/security_settings.py
backend/onyx/db/seeding/chat_history_seeding.py
backend/onyx/db/skill.py
backend/onyx/db/slack_bot.py
backend/onyx/db/slack_channel_config.py
backend/onyx/db/sso_provider.py
backend/onyx/db/swap_index.py
backend/onyx/db/sync_record.py
backend/onyx/db/system_usage.py
backend/onyx/db/tag.py
backend/onyx/db/targeted_reindex.py
backend/onyx/db/tasks.py
backend/onyx/db/tenant_invite_counter.py
backend/onyx/db/tenant_shard.py
```
## File Extension Profile
Top 30 extensions by tracked-file count.
```text
    3452  .py
    1755  .tsx
     853  .ts
     369  .go
     281  .md
     130  .png
     119  .yaml
      89  .yml
      89  .json
      81  .tf
      79  .css
      49  .svg
      46  .js
      43  .sh
      39  .xsd
      28  .jpg
      27  [no-extension]
      23  .xml
      23  .template
      19  .gitignore
      16  .html
      15  .pdf
      14  .txt
       9  .rs
       8  .lock
       8  .hcl
       7  .mjs
       5  .toml
       4  .jinja
       4  .example
```
## Safety Record
During Action 6.2:
- Application execution: NO
- Docker execution: NO
- Dependency installation: NO
- Database migration: NO
- External AI provider invocation: NO
- Network vulnerability probing: NO
- Production data usage: NO
- Production credentials: NO
- Source modifications in Onyx: NO
## Interpretation Boundary
This action establishes repository topology only.
The following remain unverified and must be established through later
reverse-engineering actions:
- actual runtime components;
- startup sequence;
- service-to-service communication;
- authentication and session flow;
- authorization enforcement points;
- tenant boundaries;
- document ingestion flow;
- retrieval and reranking flow;
- LLM request flow;
- agent/tool execution flow;
- MCP integration behavior;
- persistence and cache behavior;
- deletion/revocation propagation;
- logging and telemetry behavior.
## Result
Action 6.2 documentation and repository topology reconnaissance: **PASS**.
