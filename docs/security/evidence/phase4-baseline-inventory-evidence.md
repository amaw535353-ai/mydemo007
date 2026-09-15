# Phase 4 Action 4.1 - Baseline & Cloud/DevSecOps Inventory Evidence

## Provenance

- Source Phase 3 commit: `a10f928e88d29a5a3c225b29371a87886cda2a64`
- Working branch: `security/phase-4-cloud-devsecops`
- Phase 4 starting commit: `a10f928e88d29a5a3c225b29371a87886cda2a64`

## Observation class

**STATIC SOURCE CANDIDATES ONLY. RUNTIME/DEPLOYMENT BEHAVIOR IS UNVERIFIED.**

## Security surface inventory

| Surface | Candidate files | Matching lines |
|---|---:|---:|
| docker | 211 | 676 |
| docker_compose | 235 | 576 |
| kubernetes | 223 | 1572 |
| helm | 83 | 366 |
| github_actions_ci | 48 | 71 |
| cicd_general | 183 | 734 |
| terraform_iac | 1076 | 4855 |
| other_iac | 3 | 8 |
| dependencies | 60 | 704 |
| dependency_security | 26 | 137 |
| secrets_credentials | 2408 | 31739 |
| environment_config | 458 | 2432 |
| container_privilege | 50 | 228 |
| filesystem_mounts | 403 | 2029 |
| network_exposure | 159 | 352 |
| registry_artifacts | 325 | 2103 |
| sbom | 2 | 9 |
| signing_provenance | 120 | 348 |
| security_scanning | 2 | 4 |
| build_supply_chain | 86 | 221 |
| logging_observability | 1084 | 9818 |

## Representative candidates

### docker

- `backend/alembic_tenants/versions/3b9f09038764_add_read_only_kg_user.py`
- `backend/alembic/versions/01f8e6d95a33_populate_flow_mapping_data.py`
- `backend/alembic/versions/03bf8be6b53a_rework_kg_config.py`
- `backend/alembic/versions/07b98176f1de_code_interpreter_seed.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/0cd424f32b1d_user_file_data_preparation_and_backfill.py`
- `backend/alembic/versions/0d9c7b6a5e4f_retain_user_usage_after_user_deletion.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/16c37a30adf2_user_file_relationship_migration.py`
- `backend/alembic/versions/17135ac06582_add_incognito_to_user_usage.py`

### docker_compose

- `backend/alembic/versions/0568ccf46a6b_add_thread_specific_model_selection.py`
- `backend/alembic/versions/05c07bf07c00_add_search_doc_relevance_details.py`
- `backend/alembic/versions/08a1eda20fe1_add_earliest_indexing_to_connector.py`
- `backend/alembic/versions/0a2b51deb0b8_add_starter_prompts.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/0f7ff6d75b57_add_index_to_index_attempt_time_created.py`
- `backend/alembic/versions/15326fcec57e_introduce_onyx_apis.py`
- `backend/alembic/versions/173cae5bba26_port_config_store.py`
- `backend/alembic/versions/1a03d2c2856b_add_indexes_to_document__tag.py`
- `backend/alembic/versions/1f60f60c3401_embedding_model_search_settings.py`

### kubernetes

- `backend/onyx/background/celery/apps/app_base.py`
- `backend/onyx/background/celery/celery_k8s_probe.py`
- `backend/onyx/background/celery/tasks/monitoring/tasks.py`
- `backend/onyx/sandbox_proxy/backend.py`
- `backend/onyx/sandbox_proxy/ca_k8s.py`
- `backend/onyx/sandbox_proxy/identity_k8s.py`
- `backend/onyx/server/features/build/configs.py`
- `backend/onyx/server/features/build/debug.py`
- `backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py`
- `backend/onyx/server/features/build/sandbox/factory.py`

### helm

- `backend/ee/onyx/external_permissions/sharepoint/permission_utils.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/db/engine/sql_engine.py`
- `backend/onyx/indexing/chunker.py`
- `backend/onyx/sandbox_proxy/mcp_jsonrpc.py`
- `backend/onyx/server/features/build/sandbox/image/Dockerfile`
- `backend/onyx/server/features/build/sandbox/image/.dockerignore`
- `backend/onyx/server/features/build/sandbox/image/README.md`
- `backend/onyx/server/features/build/sandbox/nextjs_dev.py`
- `backend/onyx/server/features/build/sandbox/README.md`

### github_actions_ci

- `backend/onyx/connectors/github/connector.py`
- `backend/onyx/indexing/indexing_pipeline.py`
- `backend/onyx/server/features/build/sandbox/image/README.md`
- `backend/onyx/server/features/build/sandbox/image/templates/outputs/web/components/component-example.tsx`
- `backend/tests/evals/connector_filter_eval/README.md`
- `backend/tests/evals/connector_filter_eval/test_filter_extraction_regression.py`
- `backend/tests/external_dependency_unit/craft/test_sandbox_lifecycle.py`
- `backend/tests/integration/tests/gateway_clients/conftest.py`
- `backend/tests/integration/tests/pruning/website/js/jquery.js`
- `backend/tests/README.md`

### cicd_general

- `backend/AGENTS.md`
- `backend/alembic/versions/bc9e56f2fb96_polymorphic_gated_app.py`
- `backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py`
- `backend/ee/onyx/db/document.py`
- `backend/ee/onyx/external_permissions/post_query_censoring.py`
- `backend/ee/onyx/search/process_search_query.py`
- `backend/ee/onyx/server/metrics/license_metrics.py`
- `backend/ee/onyx/server/query_and_chat/search_backend.py`
- `backend/ee/onyx/server/scim/api.py`
- `backend/ee/onyx/server/tenants/product_gating.py`

### terraform_iac

- `AGENTS.md`
- `backend/AGENTS.md`
- `backend/alembic/versions/01f8e6d95a33_populate_flow_mapping_data.py`
- `backend/alembic/versions/177de57c21c9_display_custom_llm_models.py`
- `backend/alembic/versions/19c0ccb01687_migrate_to_contextual_rag_model.py`
- `backend/alembic/versions/1d78c0ca7853_remove_voice_provider_deleted_column.py`
- `backend/alembic/versions/1e0a3e4226f7_move_ollama_api_key_from_custom_config_.py`
- `backend/alembic/versions/1f2a3b4c5d6e_add_internet_search_and_content_providers.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/287021f3b46c_add_voice_provider_api_secret.py`

### other_iac

- `deployment/aws_ecs_fargate/cloudformation/deploy.sh`
- `deployment/aws_ecs_fargate/cloudformation/uninstall.sh`
- `web/src/app/craft/components/CometEdge.stories.tsx`

### dependencies

- `backend/Dockerfile`
- `backend/Dockerfile.model_server`
- `backend/onyx/prompts/coding_agent/coding_agent.py`
- `backend/onyx/server/features/build/sandbox/base.py`
- `backend/onyx/server/features/build/sandbox/image/Dockerfile`
- `backend/onyx/server/features/build/sandbox/image/.dockerignore`
- `backend/onyx/server/features/build/sandbox/image/initial-requirements.txt`
- `backend/onyx/server/features/build/sandbox/image/opencode-plugins/webapp.ts`
- `backend/onyx/server/features/build/sandbox/image/README.md`
- `backend/onyx/server/features/build/sandbox/image/templates/outputs/web/AGENTS.md`

### dependency_security

- `backend/tests/daily/connectors/salesforce/test_salesforce_data.json`
- `.cursor/skills/merge-dependabot-prs/SKILL.md`
- `.greptile/config.json`
- `tools/ods-audit/pyproject.toml`
- `tools/ods-audit/README.md`
- `tools/ods/go.mod`
- `tools/ods/go.sum`
- `tools/ods/internal/audit/actions.go`
- `tools/ods/internal/audit/actions_test.go`
- `tools/ods/internal/audit/audit.go`

### secrets_credentials

- `AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic_tenants/versions/3b9f09038764_add_read_only_kg_user.py`
- `backend/alembic/versions/03d710ccf29c_add_permission_sync_attempt_tables.py`
- `backend/alembic/versions/0816326d83aa_add_federated_connector_tables.py`
- `backend/alembic/versions/0a98909f2757_enable_encrypted_fields.py`
- `backend/alembic/versions/0cd424f32b1d_user_file_data_preparation_and_backfill.py`
- `backend/alembic/versions/0ebb1d516877_add_ccpair_deletion_failure_message.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/15326fcec57e_introduce_onyx_apis.py`

### environment_config

- `AGENTS.md`
- `backend/AGENTS.md`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/3c9a65f1207f_seed_exa_provider_from_env.py`
- `backend/alembic/versions/62c3a055a141_add_file_names_to_file_connector_config.py`
- `backend/alembic/versions/90e3b9af7da4_tag_fix.py`
- `backend/alembic/versions/f3a9c1d4b7e2_provision_built_in_external_apps.py`
- `backend/alembic/versions/f7ca3e2f45d9_migrate_no_auth_data_to_placeholder.py`

### container_privilege

- `backend/ee/onyx/server/scim/api.py`
- `backend/onyx/connectors/capability_checks/models.py`
- `backend/onyx/connectors/source_operations.py`
- `backend/onyx/db/llm.py`
- `backend/onyx/db/persona.py`
- `backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py`
- `backend/onyx/server/features/build/sandbox/README.md`
- `backend/onyx/server/features/mcp/client.py`
- `backend/onyx/server/gateway/models.py`
- `backend/onyx/server/manage/llm/models.py`

### filesystem_mounts

- `backend/alembic/versions/7b9b952abdf6_update_entities.py`
- `backend/Dockerfile`
- `backend/Dockerfile.model_server`
- `backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py`
- `backend/ee/onyx/server/tenants/api.py`
- `backend/ee/onyx/server/token_rate_limits/api.py`
- `backend/model_server/ca_certs.py`
- `backend/onyx/background/celery/configs/docprocessing.py`
- `backend/onyx/background/celery/tasks/docprocessing/tasks.py`
- `backend/onyx/background/celery/tasks/docprocessing/utils.py`

### network_exposure

- `backend/alembic/versions/03bf8be6b53a_rework_kg_config.py`
- `backend/alembic/versions/495cb26ce93e_create_knowlege_graph_tables.py`
- `backend/model_server/main.py`
- `backend/onyx/configs/app_configs.py`
- `backend/onyx/deep_research/models.py`
- `backend/onyx/kg/models.py`
- `backend/onyx/sandbox_proxy/server.py`
- `backend/onyx/server/features/build/configs.py`
- `backend/onyx/server/features/build/db/build_session.py`
- `backend/onyx/server/features/build/sandbox/docker/dev_mode_serve.py`

### registry_artifacts

- `backend/AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py`
- `backend/alembic/versions/34fe28843029_craft_artifact_index_and_receipts.py`
- `backend/alembic/versions/989bc57562e4_seed_browser_built_in_skill.py`
- `backend/Dockerfile`
- `backend/Dockerfile.model_server`
- `backend/ee/onyx/background/celery/tasks/log_export/tasks.py`
- `backend/ee/onyx/connectors/capability_checks.py`
- `backend/ee/onyx/secondary_llm_flows/query_expansion.py`

### sbom

- `tools/ods/go.mod`
- `tools/ods/go.sum`

### signing_provenance

- `backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py`
- `backend/ee/onyx/db/license.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/ee/onyx/server/gateway/api.py`
- `backend/ee/onyx/server/license/api.py`
- `backend/ee/onyx/server/license/models.py`
- `backend/ee/onyx/server/tenants/proxy.py`
- `backend/ee/onyx/utils/license_notifications.py`
- `backend/ee/onyx/utils/license.py`
- `backend/onyx/auth/login_claims_capture.py`

### security_scanning

- `backend/tests/unit/onyx/tools/tool_implementations/websearch/data/tartan.txt`
- `pyproject.toml`

### build_supply_chain

- `AGENTS.md`
- `backend/Dockerfile`
- `backend/Dockerfile.model_server`
- `backend/onyx/llm/multi_llm.py`
- `backend/onyx/llm/well_known_providers/constants.py`
- `backend/onyx/mcp_server/README.md`
- `backend/onyx/server/features/build/configs.py`
- `backend/onyx/server/features/build/sandbox/image/Dockerfile`
- `backend/onyx/server/features/build/sandbox/image/.dockerignore`
- `backend/onyx/server/features/build/sandbox/image/README.md`

### logging_observability

- `backend/AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic.ini`
- `backend/alembic_tenants/env.py`
- `backend/alembic/versions/0cd424f32b1d_user_file_data_preparation_and_backfill.py`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/14162713706c_add_index_attempt_stage_metric_table.py`
- `backend/alembic/versions/16c37a30adf2_user_file_relationship_migration.py`
- `backend/alembic/versions/1c36b3dc2f4e_add_full_exception_trace_to_permission_.py`
- `backend/alembic/versions/2b75d0a8ffcb_user_file_schema_cleanup.py`
## Security interpretation
This inventory establishes candidate Cloud-Native and DevSecOps
security surfaces. It does not prove:
- that a container image is actually built;
- that Kubernetes is actually deployed;
- that a CI/CD workflow actually executes;
- that an IaC resource actually exists;
- that a secret is real or exposed;
- that a dependency is vulnerable;
- that a container runs privileged;
- that a port is externally reachable;
- that an SBOM is generated;
- that artifact signing or provenance is enforced;
- that security scanners run successfully.
Runtime and pipeline behavior must be verified separately.
## Phase 4 security questions
Later Phase 4 work must answer:
1. How are application artifacts built?
2. Which base images and dependencies are trusted?
3. Which identities can modify or trigger builds?
4. Where do secrets enter the pipeline?
5. What permissions do containers receive?
6. Which filesystems and host resources are mounted?
7. Which services and ports become reachable?
8. How are dependencies pinned and updated?
9. Are builds reproducible?
10. Are artifacts scanned?
11. Is an SBOM produced?
12. Are artifacts signed or attested?
13. Can CI/CD workflows be modified by untrusted input?
14. Are deployment privileges least-privileged?
15. Is infrastructure configuration reviewed as code?
16. Are logs and build artifacts protected from secret leakage?
17. Can compromised dependencies affect the build?
18. Can compromised build infrastructure affect production artifacts?
## Safety
- No cloud resource created.
- No container started.
- No Kubernetes cluster contacted.
- No CI workflow triggered.
- No deployment executed.
- No registry contacted.
- No secret values displayed.
- No package installed.
- No external security scanner contacted.
- No billable resource used.
## Result
Action 4.1 inventory result: **PASS**
