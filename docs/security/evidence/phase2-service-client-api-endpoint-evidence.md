# Phase 2 - Service, Client, API and Endpoint Static Inventory Evidence

Static source definitions are inventory evidence, not proof that a component is deployed or reachable.

## Compose Service Definitions

| Compose file | Service |
| --- | --- |
| `backend/tests/integration/mock_services/docker-compose.mock-it-services.yml` | `mock_connector_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.craft.yml` | `api_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.craft.yml` | `background` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.craft.yml` | `sandbox-image-prepull` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.craft.yml` | `sandbox-proxy` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml` | `api_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml` | `background` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml` | `cache` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml` | `code-interpreter` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml` | `indexing_model_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml` | `inference_model_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml` | `minio` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml` | `nginx` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml` | `opensearch` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml` | `relational_db` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.dev.yml` | `web_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.onyx-lite.yml` | `api_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.onyx-lite.yml` | `background` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.onyx-lite.yml` | `cache` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.onyx-lite.yml` | `indexing_model_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.onyx-lite.yml` | `inference_model_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.onyx-lite.yml` | `minio` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.onyx-lite.yml` | `opensearch` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml` | `api_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml` | `background` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml` | `cache` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml` | `certbot` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml` | `code-interpreter` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml` | `indexing_model_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml` | `inference_model_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml` | `minio` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml` | `nginx` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml` | `opensearch` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml` | `relational_db` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.prod.yml` | `web_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml` | `api_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml` | `background` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml` | `cache` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml` | `code-interpreter` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml` | `indexing_model_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml` | `inference_model_server` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml` | `minio` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml` | `nginx` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml` | `opensearch` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml` | `relational_db` |
| `cli/internal/deploy/deployfiles/embedded/docker_compose/docker-compose.yml` | `web_server` |
| `deployment/docker_compose/docker-compose.airgap-test.yml` | `api_server` |
| `deployment/docker_compose/docker-compose.airgap-test.yml` | `inference_model_server` |
| `deployment/docker_compose/docker-compose.airgap-tls-test.yml` | `api_server` |
| `deployment/docker_compose/docker-compose.airgap-tls-test.yml` | `inference_model_server` |
| `deployment/docker_compose/docker-compose.airgap-tls-test.yml` | `tls_failure` |
| `deployment/docker_compose/docker-compose.craft.yml` | `api_server` |
| `deployment/docker_compose/docker-compose.craft.yml` | `background` |
| `deployment/docker_compose/docker-compose.craft.yml` | `sandbox-image-prepull` |
| `deployment/docker_compose/docker-compose.craft.yml` | `sandbox-proxy` |
| `deployment/docker_compose/docker-compose.dev.yml` | `api_server` |
| `deployment/docker_compose/docker-compose.dev.yml` | `background` |
| `deployment/docker_compose/docker-compose.dev.yml` | `cache` |
| `deployment/docker_compose/docker-compose.dev.yml` | `code-interpreter` |
| `deployment/docker_compose/docker-compose.dev.yml` | `indexing_model_server` |
| `deployment/docker_compose/docker-compose.dev.yml` | `inference_model_server` |
| `deployment/docker_compose/docker-compose.dev.yml` | `minio` |
| `deployment/docker_compose/docker-compose.dev.yml` | `nginx` |
| `deployment/docker_compose/docker-compose.dev.yml` | `opensearch` |
| `deployment/docker_compose/docker-compose.dev.yml` | `relational_db` |
| `deployment/docker_compose/docker-compose.dev.yml` | `web_server` |
| `deployment/docker_compose/docker-compose.mcp-api-key-test.yml` | `mcp_api_key_server` |
| `deployment/docker_compose/docker-compose.mcp-oauth-test.yml` | `mcp_oauth_server` |
| `deployment/docker_compose/docker-compose.mcp-oauth-test.yml` | `mock_oidc_idp` |
| `deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml` | `mcp_per_user_key_server` |
| `deployment/docker_compose/docker-compose.multitenant.yml` | `api_server` |
| `deployment/docker_compose/docker-compose.multitenant.yml` | `background` |
| `deployment/docker_compose/docker-compose.multitenant.yml` | `web_server` |
| `deployment/docker_compose/docker-compose.onyx-lite.yml` | `api_server` |
| `deployment/docker_compose/docker-compose.onyx-lite.yml` | `background` |
| `deployment/docker_compose/docker-compose.onyx-lite.yml` | `cache` |
| `deployment/docker_compose/docker-compose.onyx-lite.yml` | `indexing_model_server` |
| `deployment/docker_compose/docker-compose.onyx-lite.yml` | `inference_model_server` |
| `deployment/docker_compose/docker-compose.onyx-lite.yml` | `minio` |
| `deployment/docker_compose/docker-compose.onyx-lite.yml` | `opensearch` |
| `deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml` | `api_server` |
| `deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml` | `background` |
| `deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml` | `cache` |
| `deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml` | `code-interpreter` |
| `deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml` | `indexing_model_server` |
| `deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml` | `inference_model_server` |
| `deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml` | `minio` |
| `deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml` | `nginx` |
| `deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml` | `opensearch` |
| `deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml` | `relational_db` |
| `deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml` | `web_server` |
| `deployment/docker_compose/docker-compose.prod.yml` | `api_server` |
| `deployment/docker_compose/docker-compose.prod.yml` | `background` |
| `deployment/docker_compose/docker-compose.prod.yml` | `cache` |
| `deployment/docker_compose/docker-compose.prod.yml` | `certbot` |
| `deployment/docker_compose/docker-compose.prod.yml` | `code-interpreter` |
| `deployment/docker_compose/docker-compose.prod.yml` | `indexing_model_server` |
| `deployment/docker_compose/docker-compose.prod.yml` | `inference_model_server` |
| `deployment/docker_compose/docker-compose.prod.yml` | `minio` |
| `deployment/docker_compose/docker-compose.prod.yml` | `nginx` |
| `deployment/docker_compose/docker-compose.prod.yml` | `opensearch` |
| `deployment/docker_compose/docker-compose.prod.yml` | `relational_db` |
| `deployment/docker_compose/docker-compose.prod.yml` | `web_server` |
| `deployment/docker_compose/docker-compose.resources.yml` | `api_server` |
| `deployment/docker_compose/docker-compose.resources.yml` | `background` |
| `deployment/docker_compose/docker-compose.resources.yml` | `indexing_model_server` |
| `deployment/docker_compose/docker-compose.resources.yml` | `inference_model_server` |
| `deployment/docker_compose/docker-compose.resources.yml` | `nginx` |
| `deployment/docker_compose/docker-compose.resources.yml` | `relational_db` |
| `deployment/docker_compose/docker-compose.search-testing.yml` | `api_server` |
| `deployment/docker_compose/docker-compose.search-testing.yml` | `background` |
| `deployment/docker_compose/docker-compose.search-testing.yml` | `cache` |
| `deployment/docker_compose/docker-compose.search-testing.yml` | `indexing_model_server` |
| `deployment/docker_compose/docker-compose.search-testing.yml` | `inference_model_server` |
| `deployment/docker_compose/docker-compose.search-testing.yml` | `minio` |
| `deployment/docker_compose/docker-compose.search-testing.yml` | `nginx` |
| `deployment/docker_compose/docker-compose.search-testing.yml` | `opensearch` |
| `deployment/docker_compose/docker-compose.search-testing.yml` | `relational_db` |
| `deployment/docker_compose/docker-compose.search-testing.yml` | `web_server` |
| `deployment/docker_compose/docker-compose.template.yml` | `api_server` |
| `deployment/docker_compose/docker-compose.template.yml` | `background` |
| `deployment/docker_compose/docker-compose.template.yml` | `cache` |
| `deployment/docker_compose/docker-compose.template.yml` | `certbot` |
| `deployment/docker_compose/docker-compose.template.yml` | `code-interpreter` |
| `deployment/docker_compose/docker-compose.template.yml` | `indexing_model_server` |
| `deployment/docker_compose/docker-compose.template.yml` | `inference_model_server` |
| `deployment/docker_compose/docker-compose.template.yml` | `minio` |
| `deployment/docker_compose/docker-compose.template.yml` | `nginx` |
| `deployment/docker_compose/docker-compose.template.yml` | `opensearch` |
| `deployment/docker_compose/docker-compose.template.yml` | `relational_db` |
| `deployment/docker_compose/docker-compose.template.yml` | `web_server` |
| `deployment/docker_compose/docker-compose.yml` | `api_server` |
| `deployment/docker_compose/docker-compose.yml` | `background` |
| `deployment/docker_compose/docker-compose.yml` | `cache` |
| `deployment/docker_compose/docker-compose.yml` | `code-interpreter` |
| `deployment/docker_compose/docker-compose.yml` | `indexing_model_server` |
| `deployment/docker_compose/docker-compose.yml` | `inference_model_server` |
| `deployment/docker_compose/docker-compose.yml` | `minio` |
| `deployment/docker_compose/docker-compose.yml` | `nginx` |
| `deployment/docker_compose/docker-compose.yml` | `opensearch` |
| `deployment/docker_compose/docker-compose.yml` | `relational_db` |
| `deployment/docker_compose/docker-compose.yml` | `web_server` |
| `tools/profiling/docker-compose.yml` | `grafana` |
| `tools/profiling/docker-compose.yml` | `prometheus` |

## Helm/Kubernetes Resource Kinds

| File | Kind |
| --- | --- |
| `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml` | `Backup` |
| `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml` | `Cluster` |
| `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml` | `ClusterImageCatalog` |
| `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml` | `CustomResourceDefinition` |
| `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml` | `Database` |
| `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml` | `FailoverQuorum` |
| `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml` | `ImageCatalog` |
| `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml` | `Pooler` |
| `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml` | `Publication` |
| `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml` | `ScheduledBackup` |
| `deployment/helm/charts/onyx-cnpg-crds/crds/cnpg-crds.yaml` | `Subscription` |
| `deployment/helm/charts/onyx/templates/api-deployment.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/api-hpa.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/api-hpa.yaml` | `HorizontalPodAutoscaler` |
| `deployment/helm/charts/onyx/templates/api-scaledobject.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/api-scaledobject.yaml` | `ScaledObject` |
| `deployment/helm/charts/onyx/templates/api-service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates/api-servicemonitor.yaml` | `ServiceMonitor` |
| `deployment/helm/charts/onyx/templates/auth-secrets.yaml` | `Secret` |
| `deployment/helm/charts/onyx/templates/celery-beat.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-docfetching-hpa.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-docfetching-hpa.yaml` | `HorizontalPodAutoscaler` |
| `deployment/helm/charts/onyx/templates/celery-worker-docfetching-metrics-service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates/celery-worker-docfetching-scaledobject.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-docfetching-scaledobject.yaml` | `ScaledObject` |
| `deployment/helm/charts/onyx/templates/celery-worker-docfetching.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-docprocessing-hpa.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-docprocessing-hpa.yaml` | `HorizontalPodAutoscaler` |
| `deployment/helm/charts/onyx/templates/celery-worker-docprocessing-metrics-service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates/celery-worker-docprocessing-scaledobject.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-docprocessing-scaledobject.yaml` | `ScaledObject` |
| `deployment/helm/charts/onyx/templates/celery-worker-docprocessing.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-heavy-hpa.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-heavy-hpa.yaml` | `HorizontalPodAutoscaler` |
| `deployment/helm/charts/onyx/templates/celery-worker-heavy-metrics-service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates/celery-worker-heavy-scaledobject.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-heavy-scaledobject.yaml` | `ScaledObject` |
| `deployment/helm/charts/onyx/templates/celery-worker-heavy.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-light-hpa.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-light-hpa.yaml` | `HorizontalPodAutoscaler` |
| `deployment/helm/charts/onyx/templates/celery-worker-light-metrics-service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates/celery-worker-light-scaledobject.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-light-scaledobject.yaml` | `ScaledObject` |
| `deployment/helm/charts/onyx/templates/celery-worker-light.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-monitoring-hpa.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-monitoring-hpa.yaml` | `HorizontalPodAutoscaler` |
| `deployment/helm/charts/onyx/templates/celery-worker-monitoring-metrics-service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates/celery-worker-monitoring-scaledobject.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-monitoring-scaledobject.yaml` | `ScaledObject` |
| `deployment/helm/charts/onyx/templates/celery-worker-monitoring.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-primary-hpa.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-primary-hpa.yaml` | `HorizontalPodAutoscaler` |
| `deployment/helm/charts/onyx/templates/celery-worker-primary-metrics-service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates/celery-worker-primary-scaledobject.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-primary-scaledobject.yaml` | `ScaledObject` |
| `deployment/helm/charts/onyx/templates/celery-worker-primary.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks-hpa.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks-hpa.yaml` | `HorizontalPodAutoscaler` |
| `deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks-metrics-service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks-scaledobject.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks-scaledobject.yaml` | `ScaledObject` |
| `deployment/helm/charts/onyx/templates/celery-worker-scheduled-tasks.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-servicemonitors.yaml` | `ServiceMonitor` |
| `deployment/helm/charts/onyx/templates/celery-worker-user-file-processing-hpa.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-user-file-processing-hpa.yaml` | `HorizontalPodAutoscaler` |
| `deployment/helm/charts/onyx/templates/celery-worker-user-file-processing-scaledobject.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/celery-worker-user-file-processing-scaledobject.yaml` | `ScaledObject` |
| `deployment/helm/charts/onyx/templates/celery-worker-user-file-processing.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/configmap.yaml` | `ConfigMap` |
| `deployment/helm/charts/onyx/templates/discordbot.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/external-secret.yaml` | `ExternalSecret` |
| `deployment/helm/charts/onyx/templates/grafana-dashboards.yaml` | `ConfigMap` |
| `deployment/helm/charts/onyx/templates/indexing-model-deployment.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/indexing-model-service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates/inference-model-deployment.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/inference-model-service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates/ingress-api.yaml` | `Ingress` |
| `deployment/helm/charts/onyx/templates/ingress-mcp-oauth-callback.yaml` | `Ingress` |
| `deployment/helm/charts/onyx/templates/ingress-mcp.yaml` | `Ingress` |
| `deployment/helm/charts/onyx/templates/ingress-scim.yaml` | `Ingress` |
| `deployment/helm/charts/onyx/templates/ingress-webserver.yaml` | `Ingress` |
| `deployment/helm/charts/onyx/templates/lets-encrypt.yaml` | `ClusterIssuer` |
| `deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/mcp-server-service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates/mcp-server-servicemonitor.yaml` | `ServiceMonitor` |
| `deployment/helm/charts/onyx/templates/network-policy-sandbox-egress.yaml` | `NetworkPolicy` |
| `deployment/helm/charts/onyx/templates/network-policy-sandbox-push.yaml` | `NetworkPolicy` |
| `deployment/helm/charts/onyx/templates/nginx-conf.yaml` | `ConfigMap` |
| `deployment/helm/charts/onyx/templates/postgres-cluster.yaml` | `Cluster` |
| `deployment/helm/charts/onyx/templates/pre-delete-cleanup.yaml` | `Job` |
| `deployment/helm/charts/onyx/templates/pre-delete-cleanup.yaml` | `Role` |
| `deployment/helm/charts/onyx/templates/pre-delete-cleanup.yaml` | `RoleBinding` |
| `deployment/helm/charts/onyx/templates/pre-delete-cleanup.yaml` | `ServiceAccount` |
| `deployment/helm/charts/onyx/templates/sandbox-image-prepuller.yaml` | `DaemonSet` |
| `deployment/helm/charts/onyx/templates/sandbox-image-prepuller.yaml` | `NetworkPolicy` |
| `deployment/helm/charts/onyx/templates/sandbox-namespace.yaml` | `Namespace` |
| `deployment/helm/charts/onyx/templates/sandbox-podtemplate.yaml` | `PodTemplate` |
| `deployment/helm/charts/onyx/templates/sandbox-proxy/deployment.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/sandbox-proxy/networkpolicy-egress.yaml` | `NetworkPolicy` |
| `deployment/helm/charts/onyx/templates/sandbox-proxy/networkpolicy.yaml` | `NetworkPolicy` |
| `deployment/helm/charts/onyx/templates/sandbox-proxy/pdb.yaml` | `PodDisruptionBudget` |
| `deployment/helm/charts/onyx/templates/sandbox-proxy/rbac.yaml` | `Role` |
| `deployment/helm/charts/onyx/templates/sandbox-proxy/rbac.yaml` | `RoleBinding` |
| `deployment/helm/charts/onyx/templates/sandbox-proxy/rbac.yaml` | `ServiceAccount` |
| `deployment/helm/charts/onyx/templates/sandbox-proxy/service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates/sandbox-rbac.yaml` | `Role` |
| `deployment/helm/charts/onyx/templates/sandbox-rbac.yaml` | `RoleBinding` |
| `deployment/helm/charts/onyx/templates/sandbox-rbac.yaml` | `ServiceAccount` |
| `deployment/helm/charts/onyx/templates/serviceaccount.yaml` | `ServiceAccount` |
| `deployment/helm/charts/onyx/templates/slackbot.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/tests/test-connection.yaml` | `Pod` |
| `deployment/helm/charts/onyx/templates/tooling-pginto-configmap.yaml` | `ConfigMap` |
| `deployment/helm/charts/onyx/templates/webserver-deployment.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/webserver-hpa.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/webserver-hpa.yaml` | `HorizontalPodAutoscaler` |
| `deployment/helm/charts/onyx/templates/webserver-scaledobject.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates/webserver-scaledobject.yaml` | `ScaledObject` |
| `deployment/helm/charts/onyx/templates/webserver-service.yaml` | `Service` |
| `deployment/helm/charts/onyx/templates_disabled/background-deployment.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates_disabled/background-hpa.yaml` | `Deployment` |
| `deployment/helm/charts/onyx/templates_disabled/background-hpa.yaml` | `HorizontalPodAutoscaler` |
| `deployment/helm/charts/onyx/templates_disabled/onyx-secret.yaml` | `Secret` |
| `deployment/helm/charts/onyx/values.yaml` | `ClusterSecretStore` |

## Client Source Surfaces

| Source surface | Tracked files |
| --- | ---: |
| `web` | 2445 |
| `mobile` | 451 |
| `desktop` | 65 |
| `cli` | 171 |
| `widget` | 20 |
| `extensions` | 27 |

## Client API/Transport Candidates

- `cli/internal/api/client.go`
- `cli/internal/api/client_test.go`
- `cli/internal/api/errors.go`
- `cli/internal/api/image_test.go`
- `cli/internal/api/stream.go`
- `mobile/src/api/__tests__/query-keys.test.ts`
- `mobile/src/api/auth/__tests__/browserSso.test.ts`
- `mobile/src/api/auth/__tests__/providers.test.ts`
- `mobile/src/api/auth/__tests__/sessionManager.test.ts`
- `mobile/src/api/auth/__tests__/tokenStore.test.ts`
- `mobile/src/api/auth/browserSso.ts`
- `mobile/src/api/auth/instanceUrl.ts`
- `mobile/src/api/auth/providers.ts`
- `mobile/src/api/auth/refreshState.ts`
- `mobile/src/api/auth/sessionManager.ts`
- `mobile/src/api/auth/tokenStore.ts`
- `mobile/src/api/auth/useAuthConfig.ts`
- `mobile/src/api/auth/useBrowserLogin.ts`
- `mobile/src/api/auth/useEmailLogin.ts`
- `mobile/src/api/auth/useEmailSignup.ts`
- `mobile/src/api/auth/useLogout.ts`
- `mobile/src/api/auth/useSessionRefresh.ts`
- `mobile/src/api/chat/__tests__/projects.test.tsx`
- `mobile/src/api/chat/__tests__/sessions.test.tsx`
- `mobile/src/api/chat/__tests__/stream.test.ts`
- `mobile/src/api/chat/agentPreferences.ts`
- `mobile/src/api/chat/agents.ts`
- `mobile/src/api/chat/connectors.ts`
- `mobile/src/api/chat/llm.ts`
- `mobile/src/api/chat/projects.ts`
- `mobile/src/api/chat/sessions.ts`
- `mobile/src/api/chat/stream.ts`
- `mobile/src/api/client.ts`
- `mobile/src/api/config.ts`
- `mobile/src/api/errors.ts`
- `mobile/src/api/files/__tests__/upload.test.ts`
- `mobile/src/api/files/files.ts`
- `mobile/src/api/files/pickers.ts`
- `mobile/src/api/files/transport.ts`
- `mobile/src/api/files/upload.ts`
- `mobile/src/api/query-keys.ts`
- `mobile/src/api/settings.ts`
- `mobile/src/api/tools.ts`
- `mobile/src/api/types.ts`
- `mobile/src/components/auth/AuthGate.tsx`
- `mobile/src/components/auth/AuthMethods.tsx`
- `mobile/src/components/auth/AuthScreenShell.tsx`
- `mobile/src/components/auth/AuthSwitchLink.tsx`
- `mobile/src/components/auth/AuthUnreachable.tsx`
- `mobile/src/components/auth/EmailPasswordForm.tsx`
- `mobile/src/components/auth/ProviderSsoButton.tsx`
- `mobile/src/components/auth/__tests__/authRoute.test.ts`
- `mobile/src/components/auth/authRoute.ts`
- `mobile/src/query/__tests__/client.test.ts`
- `mobile/src/query/client.ts`
- `mobile/src/state/session.ts`
- `web/lib/opal/src/layouts/auth/AuthLayouts.stories.tsx`
- `web/lib/opal/src/layouts/auth/README.md`
- `web/lib/opal/src/layouts/auth/components.tsx`
- `web/lib/opal/src/layouts/auth/styles.css`
- `web/src/app/admin/connectors/[connector]/auth/callback/route.ts`
- `web/src/app/admin/connectors/[connector]/oauth/callback/page.tsx`
- `web/src/app/admin/connectors/[connector]/oauth/finalize/page.tsx`
- `web/src/app/admin/oauth-test/page.tsx`
- `web/src/app/api/[...path]/route.ts`
- `web/src/app/api/chat/mcp/oauth/callback/route.ts`
- `web/src/app/auth/__tests__/ssoCallbackRoutes.test.ts`
- `web/src/app/auth/create-account/page.tsx`
- `web/src/app/auth/error/AuthErrorContent.tsx`
- `web/src/app/auth/error/layout.tsx`
- `web/src/app/auth/error/page.tsx`
- `web/src/app/auth/forgot-password/page.tsx`
- `web/src/app/auth/forgot-password/utils.ts`
- `web/src/app/auth/impersonate/layout.tsx`
- `web/src/app/auth/impersonate/page.tsx`
- `web/src/app/auth/join/page.tsx`
- `web/src/app/auth/lib.ts`
- `web/src/app/auth/libSS.ts`
- `web/src/app/auth/login/CloudSSOSignIn.tsx`
- `web/src/app/auth/login/LoginPage.tsx`
- `web/src/app/auth/login/LoginText.tsx`
- `web/src/app/auth/login/ProviderSignInButton.tsx`
- `web/src/app/auth/login/page.tsx`
- `web/src/app/auth/logout/route.ts`
- `web/src/app/auth/oauth/callback/route.ts`
- `web/src/app/auth/oidc/callback/route.ts`
- `web/src/app/auth/reset-password/page.tsx`
- `web/src/app/auth/saml/callback/route.ts`
- `web/src/app/auth/signup/ReferralSourceSelector.tsx`
- `web/src/app/auth/signup/page.tsx`
- `web/src/app/auth/verify-email/Verify.tsx`
- `web/src/app/auth/verify-email/page.tsx`
- `web/src/app/auth/waiting-on-verification/RequestNewVerificationEmail.tsx`
- `web/src/app/auth/waiting-on-verification/page.tsx`
- `web/src/app/connector/oauth/callback/[source]/route.tsx`
- `web/src/app/craft/v1/apps/oauth/callback/page.tsx`
- `web/src/app/craft/v1/tasks/api.ts`
- `web/src/app/federated/oauth/callback/page.tsx`
- `web/src/app/mcp/oauth/callback/page.tsx`
- `web/src/app/oauth-config/callback/page.tsx`
- `web/src/components/auth/AuthErrorDisplay.tsx`
- `web/src/components/auth/AuthFlowContainer.tsx`
- `web/src/components/oauth/OAuthCallbackPage.tsx`
- `web/src/instrumentation-client.ts`
- `web/src/lib/auth/components.test.tsx`
- `web/src/lib/auth/components.tsx`
- `web/src/lib/auth/hooks.test.tsx`
- `web/src/lib/auth/hooks.ts`
- `web/src/lib/auth/paths.test.tsx`
- `web/src/lib/auth/paths.ts`
- `web/src/lib/auth/svc.ts`
- `web/src/lib/auth/svcSS.ts`
- `web/src/lib/auth/types.ts`
- `web/src/lib/auth/utils.ts`
- `web/src/lib/build/client.ts`
- `web/src/lib/connectors/oauth.test.ts`
- `web/src/lib/connectors/oauth.ts`
- `web/src/lib/notifications/api.ts`
- `web/src/lib/oauth/api.ts`
- `web/src/lib/oauth_utils.ts`
- `web/src/lib/skills/api.test.ts`
- `web/src/lib/skills/api.ts`
- `web/tests/e2e/admin/admin_auth.setup.ts`
- `web/tests/e2e/admin/admin_oauth_redirect_uri.spec.ts`
- `web/tests/e2e/admin/oauth_config/test_tool_oauth.spec.ts`
- `web/tests/e2e/auth/anonymous_chat.spec.ts`
- `web/tests/e2e/auth/email_verification.spec.ts`
- `web/tests/e2e/auth/login.spec.ts`
- `web/tests/e2e/auth/password_managements.spec.ts`
- `web/tests/e2e/auth/pat_management.spec.ts`
- `web/tests/e2e/auth/signup.spec.ts`
- `web/tests/e2e/chat/chat_session_not_found.spec.ts`
- `web/tests/e2e/mcp/mcp_oauth_flow.spec.ts`
- `web/tests/e2e/utils/auth.ts`
- `widget/src/services/api-service.ts`
- `widget/src/types/api-types.ts`

## Backend Static Route Definitions

| File | Line | Method | Local static path | Router object |
| --- | ---: | --- | --- | --- |
| `backend/ee/onyx/server/analytics/api.py` | 53 | `GET` | `/analytics/admin/query` | `router` |
| `backend/ee/onyx/server/analytics/api.py` | 85 | `GET` | `/analytics/admin/user` | `router` |
| `backend/ee/onyx/server/analytics/api.py` | 120 | `GET` | `/analytics/admin/onyxbot` | `router` |
| `backend/ee/onyx/server/analytics/api.py` | 156 | `GET` | `/analytics/admin/persona/messages` | `router` |
| `backend/ee/onyx/server/analytics/api.py` | 196 | `GET` | `/analytics/admin/persona/unique-users` | `router` |
| `backend/ee/onyx/server/analytics/api.py` | 236 | `GET` | `/analytics/assistant/{assistant_id}/stats` | `router` |
| `backend/ee/onyx/server/billing/api.py` | 168 | `POST` | `/admin/billing/create-checkout-session` | `router` |
| `backend/ee/onyx/server/billing/api.py` | 218 | `POST` | `/admin/billing/create-customer-portal-session` | `router` |
| `backend/ee/onyx/server/billing/api.py` | 282 | `GET` | `/admin/billing/billing-information` | `router` |
| `backend/ee/onyx/server/billing/api.py` | 357 | `POST` | `/admin/billing/seats/update` | `router` |
| `backend/ee/onyx/server/billing/api.py` | 404 | `POST` | `/admin/billing/end-trial` | `router` |
| `backend/ee/onyx/server/billing/api.py` | 433 | `GET` | `/admin/billing/stripe-publishable-key` | `router` |
| `backend/ee/onyx/server/billing/api.py` | 502 | `POST` | `/admin/billing/reset-connection` | `router` |
| `backend/ee/onyx/server/documents/cc_pair.py` | 32 | `GET` | `/manage/admin/cc-pair/{cc_pair_id}/sync-permissions` | `router` |
| `backend/ee/onyx/server/documents/cc_pair.py` | 55 | `POST` | `/manage/admin/cc-pair/{cc_pair_id}/sync-permissions` | `router` |
| `backend/ee/onyx/server/documents/cc_pair.py` | 111 | `GET` | `/manage/admin/cc-pair/{cc_pair_id}/sync-groups` | `router` |
| `backend/ee/onyx/server/documents/cc_pair.py` | 134 | `POST` | `/manage/admin/cc-pair/{cc_pair_id}/sync-groups` | `router` |
| `backend/ee/onyx/server/enterprise_settings/api.py` | 71 | `POST` | `/enterprise-settings/refresh-token` | `basic_router` |
| `backend/ee/onyx/server/enterprise_settings/api.py` | 131 | `PUT` | `/admin/enterprise-settings` | `admin_router` |
| `backend/ee/onyx/server/enterprise_settings/api.py` | 159 | `GET` | `/enterprise-settings` | `basic_router` |
| `backend/ee/onyx/server/enterprise_settings/api.py` | 169 | `PUT` | `/admin/enterprise-settings/logo` | `admin_router` |
| `backend/ee/onyx/server/enterprise_settings/api.py` | 213 | `GET` | `/enterprise-settings/logotype` | `basic_router` |
| `backend/ee/onyx/server/enterprise_settings/api.py` | 218 | `GET` | `/enterprise-settings/logo` | `basic_router` |
| `backend/ee/onyx/server/enterprise_settings/api.py` | 228 | `PUT` | `/admin/enterprise-settings/custom-analytics-script` | `admin_router` |
| `backend/ee/onyx/server/enterprise_settings/api.py` | 239 | `GET` | `/enterprise-settings/custom-analytics-script` | `basic_router` |
| `backend/ee/onyx/server/enterprise_settings/api.py` | 263 | `GET` | `/admin/enterprise-settings/scim/token` | `admin_router` |
| `backend/ee/onyx/server/enterprise_settings/api.py` | 292 | `POST` | `/admin/enterprise-settings/scim/token` | `admin_router` |
| `backend/ee/onyx/server/evals/api.py` | 16 | `POST` | `/evals/eval_run` | `router` |
| `backend/ee/onyx/server/features/hooks/api.py` | 198 | `GET` | `/admin/hooks/specs` | `router` |
| `backend/ee/onyx/server/features/hooks/api.py` | 219 | `GET` | `/admin/hooks` | `router` |
| `backend/ee/onyx/server/features/hooks/api.py` | 229 | `POST` | `/admin/hooks` | `router` |
| `backend/ee/onyx/server/features/hooks/api.py` | 265 | `GET` | `/admin/hooks/{hook_id}` | `router` |
| `backend/ee/onyx/server/features/hooks/api.py` | 276 | `PATCH` | `/admin/hooks/{hook_id}` | `router` |
| `backend/ee/onyx/server/features/hooks/api.py` | 351 | `DELETE` | `/admin/hooks/{hook_id}` | `router` |
| `backend/ee/onyx/server/features/hooks/api.py` | 362 | `POST` | `/admin/hooks/{hook_id}/activate` | `router` |
| `backend/ee/onyx/server/features/hooks/api.py` | 404 | `POST` | `/admin/hooks/{hook_id}/validate` | `router` |
| `backend/ee/onyx/server/features/hooks/api.py` | 432 | `POST` | `/admin/hooks/{hook_id}/deactivate` | `router` |
| `backend/ee/onyx/server/features/hooks/api.py` | 454 | `GET` | `/admin/hooks/{hook_id}/execution-logs` | `router` |
| `backend/ee/onyx/server/gateway/api.py` | 1392 | `GET` | `/v1/models` | `router` |
| `backend/ee/onyx/server/gateway/api.py` | 1404 | `POST` | `/v1/chat/completions` | `router` |
| `backend/ee/onyx/server/gateway/api.py` | 1428 | `POST` | `/v1/responses` | `router` |
| `backend/ee/onyx/server/gateway/api.py` | 1458 | `POST` | `/v1/messages` | `router` |
| `backend/ee/onyx/server/gateway/api.py` | 1491 | `POST` | `/v1/messages/count_tokens` | `router` |
| `backend/ee/onyx/server/license/api.py` | 53 | `GET` | `/license` | `router` |
| `backend/ee/onyx/server/license/api.py` | 79 | `GET` | `/license/seats` | `router` |
| `backend/ee/onyx/server/license/api.py` | 101 | `POST` | `/license/claim` | `router` |
| `backend/ee/onyx/server/license/api.py` | 176 | `POST` | `/license/upload` | `router` |
| `backend/ee/onyx/server/license/api.py` | 213 | `POST` | `/license/refresh` | `router` |
| `backend/ee/onyx/server/license/api.py` | 244 | `DELETE` | `/license` | `router` |
| `backend/ee/onyx/server/log_export/api.py` | 134 | `POST` | `/admin/log-export` | `router` |
| `backend/ee/onyx/server/log_export/api.py` | 236 | `GET` | `/admin/log-export/{export_id}` | `router` |
| `backend/ee/onyx/server/log_export/api.py` | 265 | `GET` | `/admin/log-export/{export_id}/download` | `router` |
| `backend/ee/onyx/server/manage/standard_answer.py` | 30 | `POST` | `/manage/admin/standard-answer` | `router` |
| `backend/ee/onyx/server/manage/standard_answer.py` | 47 | `GET` | `/manage/admin/standard-answer` | `router` |
| `backend/ee/onyx/server/manage/standard_answer.py` | 59 | `PATCH` | `/manage/admin/standard-answer/{standard_answer_id}` | `router` |
| `backend/ee/onyx/server/manage/standard_answer.py` | 86 | `DELETE` | `/manage/admin/standard-answer/{standard_answer_id}` | `router` |
| `backend/ee/onyx/server/manage/standard_answer.py` | 98 | `POST` | `/manage/admin/standard-answer/category` | `router` |
| `backend/ee/onyx/server/manage/standard_answer.py` | 111 | `GET` | `/manage/admin/standard-answer/category` | `router` |
| `backend/ee/onyx/server/manage/standard_answer.py` | 125 | `PATCH` | `/manage/admin/standard-answer/category/{standard_answer_category_id}` | `router` |
| `backend/ee/onyx/server/manage/standard_answer.py` | 150 | `DELETE` | `/manage/admin/standard-answer/category/{standard_answer_category_id}` | `router` |
| `backend/ee/onyx/server/oauth/api.py` | 23 | `POST` | `/prepare-authorization-request` | `router` |
| `backend/ee/onyx/server/oauth/confluence_cloud.py` | 145 | `POST` | `/connector/confluence/callback` | `router` |
| `backend/ee/onyx/server/oauth/confluence_cloud.py` | 258 | `GET` | `/connector/confluence/accessible-resources` | `router` |
| `backend/ee/onyx/server/oauth/confluence_cloud.py` | 322 | `POST` | `/connector/confluence/finalize` | `router` |
| `backend/ee/onyx/server/oauth/google_drive.py` | 110 | `POST` | `/connector/google-drive/callback` | `router` |
| `backend/ee/onyx/server/oauth/slack.py` | 99 | `POST` | `/connector/slack/callback` | `router` |
| `backend/ee/onyx/server/query_and_chat/query_backend.py` | 22 | `GET` | `/query/standard-answer` | `basic_router` |
| `backend/ee/onyx/server/query_and_chat/search_backend.py` | 53 | `POST` | `/search/search-flow-classification` | `router` |
| `backend/ee/onyx/server/query_and_chat/search_backend.py` | 96 | `POST` | `/search/send-search-message` | `router` |
| `backend/ee/onyx/server/query_and_chat/search_backend.py` | 170 | `GET` | `/search/search-history` | `router` |
| `backend/ee/onyx/server/query_history/api.py` | 158 | `GET` | `/admin/chat-sessions` | `router` |
| `backend/ee/onyx/server/query_history/api.py` | 203 | `GET` | `/admin/chat-session-history` | `router` |
| `backend/ee/onyx/server/query_history/api.py` | 247 | `GET` | `/admin/chat-session-history/{chat_session_id}` | `router` |
| `backend/ee/onyx/server/query_history/api.py` | 283 | `GET` | `/admin/query-history/list` | `router` |
| `backend/ee/onyx/server/query_history/api.py` | 311 | `POST` | `/admin/query-history/start-export` | `router` |
| `backend/ee/onyx/server/query_history/api.py` | 357 | `GET` | `/admin/query-history/export-status` | `router` |
| `backend/ee/onyx/server/query_history/api.py` | 391 | `GET` | `/admin/query-history/download` | `router` |
| `backend/ee/onyx/server/reporting/usage_export_api.py` | 36 | `POST` | `/admin/usage-report` | `router` |
| `backend/ee/onyx/server/reporting/usage_export_api.py` | 71 | `GET` | `/admin/usage-report/{report_name}` | `router` |
| `backend/ee/onyx/server/reporting/usage_export_api.py` | 96 | `GET` | `/admin/usage-report` | `router` |
| `backend/ee/onyx/server/scim/api.py` | 191 | `GET` | `/scim/v2/ServiceProviderConfig` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 197 | `GET` | `/scim/v2/ResourceTypes` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 216 | `GET` | `/scim/v2/Schemas` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 687 | `GET` | `/scim/v2/Users` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 733 | `GET` | `/scim/v2/Users/{user_id}` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 769 | `POST` | `/scim/v2/Users` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 916 | `PUT` | `/scim/v2/Users/{user_id}` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 1005 | `PATCH` | `/scim/v2/Users/{user_id}` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 1155 | `DELETE` | `/scim/v2/Users/{user_id}` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 1246 | `GET` | `/scim/v2/Groups` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 1285 | `GET` | `/scim/v2/Groups/{group_id}` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 1318 | `POST` | `/scim/v2/Groups` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 1395 | `PUT` | `/scim/v2/Groups/{group_id}` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 1462 | `PATCH` | `/scim/v2/Groups/{group_id}` | `scim_router` |
| `backend/ee/onyx/server/scim/api.py` | 1555 | `DELETE` | `/scim/v2/Groups/{group_id}` | `scim_router` |
| `backend/ee/onyx/server/tenants/admin_api.py` | 26 | `POST` | `/tenants/impersonate` | `router` |
| `backend/ee/onyx/server/tenants/anonymous_users_api.py` | 28 | `GET` | `/tenants/anonymous-user-path` | `router` |
| `backend/ee/onyx/server/tenants/anonymous_users_api.py` | 43 | `POST` | `/tenants/anonymous-user-path` | `router` |
| `backend/ee/onyx/server/tenants/anonymous_users_api.py` | 70 | `POST` | `/tenants/anonymous-user` | `router` |
| `backend/ee/onyx/server/tenants/billing_api.py` | 78 | `POST` | `/tenants/product-gating` | `router` |
| `backend/ee/onyx/server/tenants/billing_api.py` | 98 | `POST` | `/tenants/product-gating/full-sync` | `router` |
| `backend/ee/onyx/server/tenants/billing_api.py` | 118 | `POST` | `/tenants/tier-update` | `router` |
| `backend/ee/onyx/server/tenants/billing_api.py` | 146 | `GET` | `/tenants/billing-information` | `router` |
| `backend/ee/onyx/server/tenants/billing_api.py` | 155 | `POST` | `/tenants/seats/update` | `router` |
| `backend/ee/onyx/server/tenants/billing_api.py` | 165 | `POST` | `/tenants/create-customer-portal-session` | `router` |
| `backend/ee/onyx/server/tenants/billing_api.py` | 186 | `POST` | `/tenants/create-checkout-session` | `router` |
| `backend/ee/onyx/server/tenants/billing_api.py` | 209 | `POST` | `/tenants/create-subscription-session` | `router` |
| `backend/ee/onyx/server/tenants/billing_api.py` | 237 | `GET` | `/tenants/stripe-publishable-key` | `router` |
| `backend/ee/onyx/server/tenants/proxy.py` | 242 | `POST` | `/proxy/create-checkout-session` | `router` |
| `backend/ee/onyx/server/tenants/proxy.py` | 287 | `POST` | `/proxy/claim-license` | `router` |
| `backend/ee/onyx/server/tenants/proxy.py` | 332 | `POST` | `/proxy/create-customer-portal-session` | `router` |
| `backend/ee/onyx/server/tenants/proxy.py` | 374 | `GET` | `/proxy/billing-information` | `router` |
| `backend/ee/onyx/server/tenants/proxy.py` | 445 | `GET` | `/proxy/license/{tenant_id}` | `router` |
| `backend/ee/onyx/server/tenants/proxy.py` | 480 | `POST` | `/proxy/seats/update` | `router` |
| `backend/ee/onyx/server/tenants/team_membership_api.py` | 24 | `POST` | `/tenants/leave-team` | `router` |
| `backend/ee/onyx/server/tenants/tenant_management_api.py` | 27 | `GET` | `/tenants/existing-team-by-domain` | `router` |
| `backend/ee/onyx/server/tenants/user_invitations_api.py` | 43 | `POST` | `/tenants/users/invite/request` | `router` |
| `backend/ee/onyx/server/tenants/user_invitations_api.py` | 57 | `GET` | `/tenants/users/pending` | `router` |
| `backend/ee/onyx/server/tenants/user_invitations_api.py` | 65 | `POST` | `/tenants/users/invite/approve` | `router` |
| `backend/ee/onyx/server/tenants/user_invitations_api.py` | 74 | `POST` | `/tenants/users/invite/accept` | `router` |
| `backend/ee/onyx/server/tenants/user_invitations_api.py` | 96 | `POST` | `/tenants/users/invite/deny` | `router` |
| `backend/ee/onyx/server/token_rate_limits/api.py` | 51 | `GET` | `/admin/token-rate-limits/global` | `router` |
| `backend/ee/onyx/server/token_rate_limits/api.py` | 62 | `POST` | `/admin/token-rate-limits/global` | `router` |
| `backend/ee/onyx/server/token_rate_limits/api.py` | 81 | `PUT` | `/admin/token-rate-limits/rate-limit/{token_rate_limit_id}` | `router` |
| `backend/ee/onyx/server/token_rate_limits/api.py` | 100 | `DELETE` | `/admin/token-rate-limits/rate-limit/{token_rate_limit_id}` | `router` |
| `backend/ee/onyx/server/token_rate_limits/api.py` | 119 | `GET` | `/admin/token-rate-limits/user-groups` | `router` |
| `backend/ee/onyx/server/token_rate_limits/api.py` | 137 | `GET` | `/admin/token-rate-limits/user-group/{group_id}` | `router` |
| `backend/ee/onyx/server/token_rate_limits/api.py` | 157 | `POST` | `/admin/token-rate-limits/user-group/{group_id}` | `router` |
| `backend/ee/onyx/server/token_rate_limits/api.py` | 236 | `PUT` | `/admin/token-rate-limits/user-group/{group_id}/rate-limit/{rate_limit_id}` | `router` |
| `backend/ee/onyx/server/token_rate_limits/api.py` | 260 | `DELETE` | `/admin/token-rate-limits/user-group/{group_id}/rate-limit/{rate_limit_id}` | `router` |
| `backend/ee/onyx/server/token_rate_limits/api.py` | 281 | `GET` | `/admin/token-rate-limits/users` | `router` |
| `backend/ee/onyx/server/token_rate_limits/api.py` | 292 | `POST` | `/admin/token-rate-limits/users` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 83 | `GET` | `/manage/admin/user-group` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 136 | `GET` | `/manage/admin/user-group/{user_group_id}` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 171 | `GET` | `/manage/user-groups/minimal` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 194 | `GET` | `/manage/admin/permissions/registry` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 201 | `GET` | `/manage/admin/user-group/{user_group_id}/permissions` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 221 | `PUT` | `/manage/admin/user-group/{user_group_id}/permissions` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 268 | `POST` | `/manage/admin/user-group` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 302 | `PATCH` | `/manage/admin/user-group/rename` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 347 | `PATCH` | `/manage/admin/user-group/{user_group_id}/incognito` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 372 | `PATCH` | `/manage/admin/user-group/{user_group_id}` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 395 | `POST` | `/manage/admin/user-group/{user_group_id}/add-users` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 418 | `DELETE` | `/manage/admin/user-group/{user_group_id}` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 456 | `PATCH` | `/manage/admin/user-group/{user_group_id}/agents` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 526 | `PATCH` | `/manage/admin/user-group/{user_group_id}/document-sets` | `router` |
| `backend/ee/onyx/server/user_group/api.py` | 613 | `PUT` | `/manage/admin/user-group/{user_group_id}/manager` | `router` |
| `backend/model_server/encoders.py` | 173 | `POST` | `/encoder/bi-encoder-embed` | `router` |
| `backend/model_server/management_endpoints.py` | 9 | `GET` | `/api/health` | `router` |
| `backend/model_server/management_endpoints.py` | 14 | `GET` | `/api/gpu-status` | `router` |
| `backend/onyx/auth/users.py` | 1946 | `POST` | `/refresh` | `router` |
| `backend/onyx/auth/users.py` | 2782 | `GET` | `/authorize` | `router` |
| `backend/onyx/auth/users.py` | 2890 | `GET` | `/callback` | `router` |
| `backend/onyx/server/api_key/api.py` | 30 | `GET` | `/admin/api-key` | `router` |
| `backend/onyx/server/api_key/api.py` | 38 | `GET` | `/admin/api-key/{api_key_id}` | `router` |
| `backend/onyx/server/api_key/api.py` | 52 | `POST` | `/admin/api-key` | `router` |
| `backend/onyx/server/api_key/api.py` | 74 | `POST` | `/admin/api-key/{api_key_id}/regenerate` | `router` |
| `backend/onyx/server/api_key/api.py` | 93 | `PATCH` | `/admin/api-key/{api_key_id}` | `router` |
| `backend/onyx/server/api_key/api.py` | 116 | `DELETE` | `/admin/api-key/{api_key_id}` | `router` |
| `backend/onyx/server/auth/captcha_api.py` | 60 | `POST` | `/auth/captcha/oauth-verify` | `router` |
| `backend/onyx/server/auth/mobile.py` | 48 | `POST` | `/sso/exchange` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 117 | `GET` | `/manage/admin/cc-pair/{cc_pair_id}/index-attempts` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 159 | `GET` | `/manage/admin/index-attempt/{index_attempt_id}/stage-metrics` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 234 | `GET` | `/manage/admin/cc-pair/{cc_pair_id}/permission-sync-attempts` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 284 | `GET` | `/manage/admin/cc-pair/{cc_pair_id}/external-group-sync-attempts` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 337 | `GET` | `/manage/admin/cc-pair/{cc_pair_id}` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 469 | `PUT` | `/manage/admin/cc-pair/{cc_pair_id}/status` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 576 | `PUT` | `/manage/admin/cc-pair/{cc_pair_id}/name` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 610 | `PUT` | `/manage/admin/cc-pair/{cc_pair_id}/property` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 666 | `GET` | `/manage/admin/cc-pair/{cc_pair_id}/last_pruned` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 684 | `POST` | `/manage/admin/cc-pair/{cc_pair_id}/prune` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 740 | `GET` | `/manage/admin/cc-pair/{cc_pair_id}/get-docs-sync-status` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 753 | `GET` | `/manage/admin/cc-pair/{cc_pair_id}/errors` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 794 | `PUT` | `/manage/connector/{connector_id}/credential/{credential_id}` | `router` |
| `backend/onyx/server/documents/cc_pair.py` | 922 | `DELETE` | `/manage/connector/{connector_id}/credential/{credential_id}` | `router` |
| `backend/onyx/server/documents/connector.py` | 182 | `PUT` | `/manage/admin/connector/google-drive/service-account-credential` | `router` |
| `backend/onyx/server/documents/connector.py` | 202 | `PUT` | `/manage/admin/connector/gmail/service-account-credential` | `router` |
| `backend/onyx/server/documents/connector.py` | 221 | `GET` | `/manage/admin/connector/google-drive/check-auth/{credential_id}` | `router` |
| `backend/onyx/server/documents/connector.py` | 432 | `POST` | `/manage/admin/connector/file/upload` | `router` |
| `backend/onyx/server/documents/connector.py` | 441 | `GET` | `/manage/admin/connector/{connector_id}/files` | `router` |
| `backend/onyx/server/documents/connector.py` | 558 | `POST` | `/manage/admin/connector/{connector_id}/files/update` | `router` |
| `backend/onyx/server/documents/connector.py` | 782 | `GET` | `/manage/admin/connector` | `router` |
| `backend/onyx/server/documents/connector.py` | 815 | `GET` | `/manage/admin/connector/failed-indexing-status` | `router` |
| `backend/onyx/server/documents/connector.py` | 903 | `GET` | `/manage/admin/connector/status` | `router` |
| `backend/onyx/server/documents/connector.py` | 965 | `POST` | `/manage/admin/connector/indexing-status` | `router` |
| `backend/onyx/server/documents/connector.py` | 1457 | `POST` | `/manage/admin/connector` | `router` |
| `backend/onyx/server/documents/connector.py` | 1498 | `POST` | `/manage/admin/connector-with-mock-credential` | `router` |
| `backend/onyx/server/documents/connector.py` | 1587 | `PATCH` | `/manage/admin/connector/{connector_id}` | `router` |
| `backend/onyx/server/documents/connector.py` | 1634 | `DELETE` | `/manage/admin/connector/{connector_id}` | `router` |
| `backend/onyx/server/documents/connector.py` | 1663 | `POST` | `/manage/admin/connector/run-once` | `router` |
| `backend/onyx/server/documents/connector.py` | 1745 | `GET` | `/manage/connector/gmail/authorize/{credential_id}` | `router` |
| `backend/onyx/server/documents/connector.py` | 1766 | `GET` | `/manage/connector/google-drive/authorize/{credential_id}` | `router` |
| `backend/onyx/server/documents/connector.py` | 1787 | `GET` | `/manage/connector/gmail/callback` | `router` |
| `backend/onyx/server/documents/connector.py` | 1817 | `GET` | `/manage/connector/google-drive/callback` | `router` |
| `backend/onyx/server/documents/connector.py` | 1847 | `GET` | `/manage/connector` | `router` |
| `backend/onyx/server/documents/connector.py` | 1862 | `GET` | `/manage/indexed-sources` | `router` |
| `backend/onyx/server/documents/connector.py` | 1875 | `GET` | `/manage/connector/{connector_id}` | `router` |
| `backend/onyx/server/documents/connector.py` | 1904 | `POST` | `/manage/connector-request` | `router` |
| `backend/onyx/server/documents/connector.py` | 1991 | `GET` | `/manage/connector-status` | `router` |
| `backend/onyx/server/documents/credential.py` | 58 | `GET` | `/manage/admin/credential` | `router` |
| `backend/onyx/server/documents/credential.py` | 79 | `GET` | `/manage/admin/similar-credentials/{source_type}` | `router` |
| `backend/onyx/server/documents/credential.py` | 102 | `DELETE` | `/manage/admin/credential/{credential_id}` | `router` |
| `backend/onyx/server/documents/credential.py` | 122 | `PUT` | `/manage/admin/credential/swap` | `router` |
| `backend/onyx/server/documents/credential.py` | 168 | `POST` | `/manage/credential` | `router` |
| `backend/onyx/server/documents/credential.py` | 196 | `POST` | `/manage/credential/private-key` | `router` |
| `backend/onyx/server/documents/credential.py` | 263 | `GET` | `/manage/credential` | `router` |
| `backend/onyx/server/documents/credential.py` | 278 | `GET` | `/manage/credential/{credential_id}` | `router` |
| `backend/onyx/server/documents/credential.py` | 301 | `PUT` | `/manage/admin/credential/{credential_id}` | `router` |
| `backend/onyx/server/documents/credential.py` | 328 | `PUT` | `/manage/admin/credential/private-key/{credential_id}` | `router` |
| `backend/onyx/server/documents/credential.py` | 378 | `PATCH` | `/manage/credential/{credential_id}` | `router` |
| `backend/onyx/server/documents/credential.py` | 422 | `DELETE` | `/manage/credential/{credential_id}` | `router` |
| `backend/onyx/server/documents/credential.py` | 447 | `DELETE` | `/manage/credential/force/{credential_id}` | `router` |
| `backend/onyx/server/documents/credential_capabilities.py` | 133 | `POST` | `/manage/admin/credential/{credential_id}/capability-check` | `router` |
| `backend/onyx/server/documents/credential_capabilities.py` | 262 | `GET` | `/manage/admin/credential/{credential_id}/capability-report` | `router` |
| `backend/onyx/server/documents/credential_capabilities.py` | 307 | `GET` | `/manage/admin/credential/capability-reports` | `router` |
| `backend/onyx/server/documents/document.py` | 25 | `GET` | `/document/document-size-info` | `router` |
| `backend/onyx/server/documents/document.py` | 69 | `GET` | `/document/chunk-info` | `router` |
| `backend/onyx/server/documents/standard_oauth.py` | 196 | `GET` | `/connector/oauth/authorize/{source}` | `router` |
| `backend/onyx/server/documents/standard_oauth.py` | 241 | `GET` | `/connector/oauth/callback/{source}` | `router` |
| `backend/onyx/server/documents/standard_oauth.py` | 294 | `GET` | `/connector/oauth/details/{source}` | `router` |
| `backend/onyx/server/documents/targeted_reindex.py` | 77 | `POST` | `/manage/admin/indexing/targeted-reindex` | `router` |
| `backend/onyx/server/documents/targeted_reindex.py` | 171 | `GET` | `/manage/admin/indexing/targeted-reindex/{job_id}` | `router` |
| `backend/onyx/server/features/admin_banner/api.py` | 36 | `GET` | `/admin/banner` | `admin_router` |
| `backend/onyx/server/features/admin_banner/api.py` | 43 | `PUT` | `/admin/banner` | `admin_router` |
| `backend/onyx/server/features/admin_banner/api.py` | 64 | `DELETE` | `/admin/banner` | `admin_router` |
| `backend/onyx/server/features/build/api.py` | 56 | `GET` | `/build/admin/base-instructions` | `admin_router` |
| `backend/onyx/server/features/build/approvals/api.py` | 120 | `GET` | `/approvals/sessions/{session_id}/live` | `router` |
| `backend/onyx/server/features/build/approvals/api.py` | 144 | `POST` | `/approvals/{approval_id}/decision` | `router` |
| `backend/onyx/server/features/build/approvals/api.py` | 201 | `POST` | `/approvals/{approval_id}/session-grant` | `router` |
| `backend/onyx/server/features/build/debug.py` | 40 | `GET` | `/debug/opencode-logs/stream` | `router` |
| `backend/onyx/server/features/build/external_apps/api.py` | 158 | `POST` | `/apps/built-in` | `admin_router` |
| `backend/onyx/server/features/build/external_apps/api.py` | 203 | `PATCH` | `/apps/{external_app_id}` | `admin_router` |
| `backend/onyx/server/features/build/external_apps/api.py` | 277 | `POST` | `/apps/custom` | `admin_router` |
| `backend/onyx/server/features/build/external_apps/api.py` | 314 | `GET` | `/apps` | `admin_router` |
| `backend/onyx/server/features/build/external_apps/api.py` | 331 | `GET` | `/apps/built-in/options` | `admin_router` |
| `backend/onyx/server/features/build/external_apps/api.py` | 339 | `DELETE` | `/apps/{external_app_id}` | `admin_router` |
| `backend/onyx/server/features/build/external_apps/api.py` | 371 | `POST` | `/apps/{external_app_id}/credentials` | `router` |
| `backend/onyx/server/features/build/external_apps/api.py` | 402 | `DELETE` | `/apps/{external_app_id}/credentials` | `router` |
| `backend/onyx/server/features/build/external_apps/api.py` | 419 | `GET` | `/apps` | `router` |
| `backend/onyx/server/features/build/external_apps/api.py` | 436 | `POST` | `/apps/connect/{request_id}/decision` | `router` |
| `backend/onyx/server/features/build/external_apps/oauth.py` | 84 | `GET` | `/apps/{external_app_id}/oauth/start` | `router` |
| `backend/onyx/server/features/build/external_apps/oauth.py` | 134 | `POST` | `/apps/oauth/callback` | `router` |
| `backend/onyx/server/features/build/interactive_turns/api.py` | 108 | `GET` | `/sessions/{session_id}/turns/active` | `router` |
| `backend/onyx/server/features/build/interactive_turns/api.py` | 128 | `GET` | `/sessions/{session_id}/turns/{turn_id}/events` | `router` |
| `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py` | 142 | `GET` | `(dynamic/unspecified)` | `app` |
| `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py` | 147 | `GET` | `(dynamic/unspecified)` | `app` |
| `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py` | 154 | `POST` | `(dynamic/unspecified)` | `app` |
| `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py` | 189 | `POST` | `(dynamic/unspecified)` | `app` |
| `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py` | 216 | `POST` | `(dynamic/unspecified)` | `app` |
| `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py` | 263 | `POST` | `(dynamic/unspecified)` | `app` |
| `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py` | 298 | `POST` | `(dynamic/unspecified)` | `app` |
| `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py` | 333 | `POST` | `(dynamic/unspecified)` | `app` |
| `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py` | 367 | `POST` | `(dynamic/unspecified)` | `app` |
| `backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py` | 401 | `POST` | `(dynamic/unspecified)` | `app` |
| `backend/onyx/server/features/build/scheduled_tasks/api.py` | 397 | `GET` | `/scheduled-tasks` | `router` |
| `backend/onyx/server/features/build/scheduled_tasks/api.py` | 408 | `POST` | `/scheduled-tasks` | `router` |
| `backend/onyx/server/features/build/scheduled_tasks/api.py` | 457 | `GET` | `/scheduled-tasks/{task_id}` | `router` |
| `backend/onyx/server/features/build/scheduled_tasks/api.py` | 468 | `PATCH` | `/scheduled-tasks/{task_id}` | `router` |
| `backend/onyx/server/features/build/scheduled_tasks/api.py` | 521 | `DELETE` | `/scheduled-tasks/{task_id}` | `router` |
| `backend/onyx/server/features/build/scheduled_tasks/api.py` | 535 | `POST` | `/scheduled-tasks/{task_id}/run-now` | `router` |
| `backend/onyx/server/features/build/scheduled_tasks/api.py` | 558 | `GET` | `/scheduled-tasks/{task_id}/runs` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 87 | `GET` | `/sessions` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 105 | `POST` | `/sessions` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 164 | `GET` | `/sessions/{session_id}` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 201 | `POST` | `/sessions/{session_id}/skills/reload` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 212 | `GET` | `/sessions/{session_id}/sandbox-status` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 229 | `GET` | `/sessions/{session_id}/pre-provisioned-check` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 264 | `POST` | `/sessions/{session_id}/generate-name` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 281 | `PUT` | `/sessions/{session_id}/name` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 301 | `PATCH` | `/sessions/{session_id}/public` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 320 | `DELETE` | `/sessions/{session_id}` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 356 | `POST` | `/sessions/{session_id}/restore` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 435 | `POST` | `/sessions/{session_id}/snapshot` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 470 | `POST` | `/sessions/{session_id}/opencode-history-snapshot` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 500 | `GET` | `/sessions/{session_id}/artifacts` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 520 | `GET` | `/sessions/{session_id}/files` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 558 | `GET` | `/sessions/{session_id}/artifacts/{path:path}` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 609 | `GET` | `/sessions/{session_id}/export-docx/{path:path}` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 651 | `GET` | `/sessions/{session_id}/pptx-preview/{path:path}` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 678 | `GET` | `/sessions/{session_id}/webapp-info` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 700 | `GET` | `/sessions/{session_id}/webapp-download` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 730 | `GET` | `/sessions/{session_id}/download-directory/{path:path}` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 767 | `POST` | `/sessions/{session_id}/upload` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 818 | `DELETE` | `/sessions/{session_id}/files/{path:path}` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 870 | `GET` | `/sessions/{session_id}/scheduled-run-context` | `router` |
| `backend/onyx/server/features/build/session/api.py` | 922 | `GET` | `/sessions/{session_id}/scheduled-run-events` | `router` |
| `backend/onyx/server/features/build/session/messages.py` | 61 | `GET` | `/sessions/{session_id}/messages` | `router` |
| `backend/onyx/server/features/build/session/messages.py` | 80 | `POST` | `/sessions/{session_id}/send-message` | `router` |
| `backend/onyx/server/features/build/session/messages.py` | 217 | `POST` | `/sessions/{session_id}/subagents/{subagent_session_id}/send-message` | `router` |
| `backend/onyx/server/features/build/session/messages.py` | 289 | `POST` | `/sessions/{session_id}/interrupt` | `router` |
| `backend/onyx/server/features/build/user_library/api.py` | 151 | `GET` | `/user-library/tree` | `router` |
| `backend/onyx/server/features/build/user_library/api.py` | 179 | `POST` | `/user-library/upload` | `router` |
| `backend/onyx/server/features/build/user_library/api.py` | 283 | `POST` | `/user-library/upload-zip` | `router` |
| `backend/onyx/server/features/build/user_library/api.py` | 448 | `POST` | `/user-library/directories` | `router` |
| `backend/onyx/server/features/build/user_library/api.py` | 482 | `DELETE` | `/user-library/files/{document_id}` | `router` |
| `backend/onyx/server/features/build/webapp_proxy.py` | 394 | `GET` | `/build/sessions/{session_id}/webapp` | `public_build_router` |
| `backend/onyx/server/features/build/webapp_proxy.py` | 395 | `GET` | `/build/sessions/{session_id}/webapp/{path:path}` | `public_build_router` |
| `backend/onyx/server/features/default_assistant/api.py` | 26 | `GET` | `/admin/default-assistant/configuration` | `router` |
| `backend/onyx/server/features/default_assistant/api.py` | 50 | `PATCH` | `/admin/default-assistant` | `router` |
| `backend/onyx/server/features/document_set/api.py` | 47 | `POST` | `/manage/admin/document-set` | `router` |
| `backend/onyx/server/features/document_set/api.py` | 113 | `PATCH` | `/manage/admin/document-set` | `router` |
| `backend/onyx/server/features/document_set/api.py` | 181 | `DELETE` | `/manage/admin/document-set/{document_set_id}` | `router` |
| `backend/onyx/server/features/document_set/api.py` | 230 | `GET` | `/manage/admin/document-set/{document_set_id}` | `router` |
| `backend/onyx/server/features/document_set/api.py` | 284 | `GET` | `/manage/document-set` | `router` |
| `backend/onyx/server/features/document_set/api.py` | 336 | `GET` | `/manage/document-set-public` | `router` |
| `backend/onyx/server/features/hierarchy/api.py` | 68 | `GET` | `(dynamic/unspecified)` | `router` |
| `backend/onyx/server/features/hierarchy/api.py` | 96 | `POST` | `(dynamic/unspecified)` | `router` |
| `backend/onyx/server/features/hierarchy/api.py` | 152 | `GET` | `(dynamic/unspecified)` | `router` |
| `backend/onyx/server/features/image_generation/api.py` | 218 | `POST` | `/image-generation/generate` | `router` |
| `backend/onyx/server/features/input_prompt/api.py` | 30 | `GET` | `/input_prompt` | `basic_router` |
| `backend/onyx/server/features/input_prompt/api.py` | 44 | `GET` | `/input_prompt/{input_prompt_id}` | `basic_router` |
| `backend/onyx/server/features/input_prompt/api.py` | 59 | `POST` | `/input_prompt` | `basic_router` |
| `backend/onyx/server/features/input_prompt/api.py` | 82 | `PATCH` | `/input_prompt/{input_prompt_id}` | `basic_router` |
| `backend/onyx/server/features/input_prompt/api.py` | 106 | `DELETE` | `/input_prompt/{input_prompt_id}` | `basic_router` |
| `backend/onyx/server/features/input_prompt/api.py` | 124 | `DELETE` | `/admin/input_prompt/{input_prompt_id}` | `admin_router` |
| `backend/onyx/server/features/input_prompt/api.py` | 139 | `POST` | `/input_prompt/{input_prompt_id}/hide` | `basic_router` |
| `backend/onyx/server/features/mcp/api.py` | 620 | `POST` | `/admin/mcp/oauth/connect` | `admin_router` |
| `backend/onyx/server/features/mcp/api.py` | 632 | `POST` | `/mcp/oauth/connect` | `router` |
| `backend/onyx/server/features/mcp/api.py` | 887 | `POST` | `/mcp/oauth/callback` | `router` |
| `backend/onyx/server/features/mcp/api.py` | 998 | `POST` | `/mcp/user-credentials` | `router` |
| `backend/onyx/server/features/mcp/api.py` | 1098 | `DELETE` | `/mcp/user-credentials/{server_id}` | `router` |
| `backend/onyx/server/features/mcp/api.py` | 1318 | `GET` | `/mcp/servers/persona/{assistant_id}` | `router` |
| `backend/onyx/server/features/mcp/api.py` | 1347 | `GET` | `/mcp/servers` | `router` |
| `backend/onyx/server/features/mcp/api.py` | 1364 | `GET` | `/mcp/servers/craft` | `router` |
| `backend/onyx/server/features/mcp/api.py` | 1397 | `GET` | `/admin/mcp/server/{server_id}/tools` | `admin_router` |
| `backend/onyx/server/features/mcp/api.py` | 1413 | `GET` | `/admin/mcp/server/{server_id}/tools/snapshots` | `admin_router` |
| `backend/onyx/server/features/mcp/api.py` | 1480 | `GET` | `/mcp/server/{server_id}/tools` | `router` |
| `backend/onyx/server/features/mcp/api.py` | 2171 | `GET` | `/admin/mcp/servers/{server_id}` | `admin_router` |
| `backend/onyx/server/features/mcp/api.py` | 2203 | `GET` | `/admin/mcp/tools` | `admin_router` |
| `backend/onyx/server/features/mcp/api.py` | 2238 | `PATCH` | `/admin/mcp/server/{server_id}/status` | `admin_router` |
| `backend/onyx/server/features/mcp/api.py` | 2268 | `GET` | `/admin/mcp/servers` | `admin_router` |
| `backend/onyx/server/features/mcp/api.py` | 2319 | `GET` | `/admin/mcp/server/{server_id}/db-tools` | `admin_router` |
| `backend/onyx/server/features/mcp/api.py` | 2366 | `POST` | `/admin/mcp/servers/create` | `admin_router` |
| `backend/onyx/server/features/mcp/api.py` | 2441 | `POST` | `/admin/mcp/servers/update` | `admin_router` |
| `backend/onyx/server/features/mcp/api.py` | 2495 | `POST` | `/admin/mcp/server` | `admin_router` |
| `backend/onyx/server/features/mcp/api.py` | 2557 | `PATCH` | `/admin/mcp/server/{server_id}` | `admin_router` |
| `backend/onyx/server/features/mcp/api.py` | 2651 | `DELETE` | `/admin/mcp/server/{server_id}` | `admin_router` |
| `backend/onyx/server/features/mcp/client_metadata.py` | 46 | `GET` | `(dynamic/unspecified)` | `router` |
| `backend/onyx/server/features/notifications/api.py` | 114 | `GET` | `/notifications` | `router` |
| `backend/onyx/server/features/notifications/api.py` | 195 | `GET` | `/notifications/summary` | `router` |
| `backend/onyx/server/features/notifications/api.py` | 214 | `POST` | `/notifications/dismiss-all` | `router` |
| `backend/onyx/server/features/notifications/api.py` | 222 | `POST` | `/notifications/{notification_id}/dismiss` | `router` |
| `backend/onyx/server/features/oauth_config/api.py` | 84 | `POST` | `/admin/oauth-config/create` | `admin_router` |
| `backend/onyx/server/features/oauth_config/api.py` | 108 | `GET` | `/admin/oauth-config` | `admin_router` |
| `backend/onyx/server/features/oauth_config/api.py` | 118 | `GET` | `/admin/oauth-config/{oauth_config_id}` | `admin_router` |
| `backend/onyx/server/features/oauth_config/api.py` | 137 | `PUT` | `/admin/oauth-config/{oauth_config_id}` | `admin_router` |
| `backend/onyx/server/features/oauth_config/api.py` | 173 | `DELETE` | `/admin/oauth-config/{oauth_config_id}` | `admin_router` |
| `backend/onyx/server/features/oauth_config/api.py` | 199 | `POST` | `/oauth-config/initiate` | `router` |
| `backend/onyx/server/features/oauth_config/api.py` | 235 | `POST` | `/oauth-config/callback` | `router` |
| `backend/onyx/server/features/oauth_config/api.py` | 297 | `DELETE` | `/oauth-config/{oauth_config_id}/token` | `router` |
| `backend/onyx/server/features/password/api.py` | 19 | `POST` | `/password/change-password` | `router` |
| `backend/onyx/server/features/password/api.py` | 42 | `POST` | `/password/reset_password` | `router` |
| `backend/onyx/server/features/persona/api.py` | 166 | `PATCH` | `/admin/persona/{persona_id}/listed` | `admin_router` |
| `backend/onyx/server/features/persona/api.py` | 181 | `PATCH` | `/persona/{persona_id}/public` | `basic_router` |
| `backend/onyx/server/features/persona/api.py` | 203 | `PATCH` | `/admin/persona/{persona_id}/featured` | `admin_router` |
| `backend/onyx/server/features/persona/api.py` | 222 | `PATCH` | `/display-priorities` | `admin_agents_router` |
| `backend/onyx/server/features/persona/api.py` | 249 | `GET` | `/admin/persona` | `admin_router` |
| `backend/onyx/server/features/persona/api.py` | 264 | `GET` | `(dynamic/unspecified)` | `admin_agents_router` |
| `backend/onyx/server/features/persona/api.py` | 311 | `PATCH` | `/admin/persona/{persona_id}/undelete` | `admin_router` |
| `backend/onyx/server/features/persona/api.py` | 325 | `POST` | `/admin/persona/upload-image` | `admin_router` |
| `backend/onyx/server/features/persona/api.py` | 344 | `POST` | `/persona` | `basic_router` |
| `backend/onyx/server/features/persona/api.py` | 373 | `PATCH` | `/persona/{persona_id}` | `basic_router` |
| `backend/onyx/server/features/persona/api.py` | 401 | `GET` | `/persona/labels` | `basic_router` |
| `backend/onyx/server/features/persona/api.py` | 412 | `POST` | `/persona/labels` | `basic_router` |
| `backend/onyx/server/features/persona/api.py` | 429 | `PATCH` | `/admin/persona/label/{label_id}` | `admin_router` |
| `backend/onyx/server/features/persona/api.py` | 443 | `DELETE` | `/admin/persona/label/{label_id}` | `admin_router` |
| `backend/onyx/server/features/persona/api.py` | 485 | `PATCH` | `/persona/{persona_id}/share` | `basic_router` |
| `backend/onyx/server/features/persona/api.py` | 536 | `POST` | `/persona/{persona_id}/transfer-ownership` | `basic_router` |
| `backend/onyx/server/features/persona/api.py` | 562 | `DELETE` | `/persona/{persona_id}/share/me` | `basic_router` |
| `backend/onyx/server/features/persona/api.py` | 579 | `DELETE` | `/persona/{persona_id}` | `basic_router` |
| `backend/onyx/server/features/persona/api.py` | 627 | `GET` | `/persona` | `basic_router` |
| `backend/onyx/server/features/persona/api.py` | 647 | `GET` | `(dynamic/unspecified)` | `agents_router` |
| `backend/onyx/server/features/persona/api.py` | 695 | `GET` | `/persona/{persona_id}` | `basic_router` |
| `backend/onyx/server/features/persona/api.py` | 768 | `GET` | `/persona/{persona_id}/avatar` | `basic_router` |
| `backend/onyx/server/features/projects/api.py` | 146 | `GET` | `/user/projects` | `router` |
| `backend/onyx/server/features/projects/api.py` | 158 | `POST` | `/user/projects/create` | `router` |
| `backend/onyx/server/features/projects/api.py` | 174 | `POST` | `/user/projects/file/upload` | `router` |
| `backend/onyx/server/features/projects/api.py` | 237 | `GET` | `/user/projects/{project_id}` | `router` |
| `backend/onyx/server/features/projects/api.py` | 254 | `GET` | `/user/projects/files/{project_id}` | `router` |
| `backend/onyx/server/features/projects/api.py` | 279 | `DELETE` | `/user/projects/{project_id}/files/{file_id}` | `router` |
| `backend/onyx/server/features/projects/api.py` | 320 | `POST` | `/user/projects/{project_id}/files/{file_id}` | `router` |
| `backend/onyx/server/features/projects/api.py` | 369 | `GET` | `/user/projects/{project_id}/instructions` | `router` |
| `backend/onyx/server/features/projects/api.py` | 396 | `POST` | `/user/projects/{project_id}/instructions` | `router` |
| `backend/onyx/server/features/projects/api.py` | 430 | `GET` | `/user/projects/{project_id}/details` | `router` |
| `backend/onyx/server/features/projects/api.py` | 461 | `PATCH` | `/user/projects/{project_id}` | `router` |
| `backend/onyx/server/features/projects/api.py` | 489 | `DELETE` | `/user/projects/{project_id}` | `router` |
| `backend/onyx/server/features/projects/api.py` | 517 | `DELETE` | `/user/projects/file/{file_id}` | `router` |
| `backend/onyx/server/features/projects/api.py` | 578 | `GET` | `/user/projects/file/{file_id}` | `router` |
| `backend/onyx/server/features/projects/api.py` | 604 | `POST` | `/user/projects/file/statuses` | `router` |
| `backend/onyx/server/features/projects/api.py` | 631 | `POST` | `/user/projects/{project_id}/move_chat_session` | `router` |
| `backend/onyx/server/features/projects/api.py` | 651 | `POST` | `/user/projects/remove_chat_session` | `router` |
| `backend/onyx/server/features/projects/api.py` | 670 | `GET` | `/user/projects/session/{chat_session_id}/token-count` | `router` |
| `backend/onyx/server/features/projects/api.py` | 698 | `GET` | `/user/projects/session/{chat_session_id}/files` | `router` |
| `backend/onyx/server/features/projects/api.py` | 736 | `GET` | `/user/projects/{project_id}/token-count` | `router` |
| `backend/onyx/server/features/search/api.py` | 56 | `POST` | `/search` | `router` |
| `backend/onyx/server/features/skill/api.py` | 176 | `GET` | `/skills` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 189 | `PUT` | `/skills/{skill_id}/enabled` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 209 | `GET` | `/skills/{skill_id}` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 226 | `GET` | `/skills/{skill_id}/preview` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 243 | `POST` | `/skills/custom` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 288 | `POST` | `/skills/github/preview` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 313 | `POST` | `/skills/github/import` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 410 | `POST` | `/skills/custom/editor` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 503 | `GET` | `/skills/custom/{skill_id}/edit` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 521 | `POST` | `/skills/custom/bundle/inspect` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 553 | `PUT` | `/skills/custom/{skill_id}/bundle` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 598 | `POST` | `/skills/custom/{skill_id}/files` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 626 | `DELETE` | `/skills/custom/{skill_id}/files` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 654 | `PATCH` | `/skills/custom/{skill_id}` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 785 | `PATCH` | `/skills/custom/{skill_id}/share` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 863 | `POST` | `/skills/custom/{skill_id}/transfer-ownership` | `user_router` |
| `backend/onyx/server/features/skill/api.py` | 937 | `DELETE` | `/skills/custom/{skill_id}` | `user_router` |
| `backend/onyx/server/features/tool/api.py` | 148 | `POST` | `/admin/tool/custom` | `admin_router` |
| `backend/onyx/server/features/tool/api.py` | 175 | `PUT` | `/admin/tool/custom/{tool_id}` | `admin_router` |
| `backend/onyx/server/features/tool/api.py` | 210 | `DELETE` | `/admin/tool/custom/{tool_id}` | `admin_router` |
| `backend/onyx/server/features/tool/api.py` | 239 | `PATCH` | `/admin/tool/status` | `admin_router` |
| `backend/onyx/server/features/tool/api.py` | 296 | `POST` | `/admin/tool/custom/validate` | `admin_router` |
| `backend/onyx/server/features/tool/api.py` | 328 | `GET` | `/tool/openapi` | `router` |
| `backend/onyx/server/features/tool/api.py` | 353 | `GET` | `/tool/{tool_id}` | `router` |
| `backend/onyx/server/features/tool/api.py` | 371 | `GET` | `/tool` | `router` |
| `backend/onyx/server/features/usage/api.py` | 224 | `GET` | `/user/usage` | `user_usage_router` |
| `backend/onyx/server/features/usage/api.py` | 306 | `GET` | `/admin/usage/export` | `admin_usage_router` |
| `backend/onyx/server/features/usage/api.py` | 352 | `GET` | `/admin/usage/system` | `admin_usage_router` |
| `backend/onyx/server/features/usage/api.py` | 400 | `POST` | `/admin/usage/reset` | `admin_usage_router` |
| `backend/onyx/server/features/usage/api.py` | 424 | `GET` | `/admin/cost-overrides` | `router` |
| `backend/onyx/server/features/usage/api.py` | 432 | `PUT` | `/admin/cost-overrides` | `router` |
| `backend/onyx/server/features/usage/api.py` | 453 | `DELETE` | `/admin/cost-overrides/{model:path}` | `router` |
| `backend/onyx/server/features/user_oauth_token/api.py` | 23 | `GET` | `/user-oauth-token/status` | `router` |
| `backend/onyx/server/features/web_search/api.py` | 230 | `POST` | `/web-search/search` | `router` |
| `backend/onyx/server/features/web_search/api.py` | 273 | `POST` | `/web-search/search-lite` | `router` |
| `backend/onyx/server/features/web_search/api.py` | 289 | `POST` | `/web-search/open-urls` | `router` |
| `backend/onyx/server/federated/api.py` | 68 | `POST` | `/federated` | `router` |
| `backend/onyx/server/federated/api.py` | 113 | `GET` | `/federated/{id}/entities` | `router` |
| `backend/onyx/server/federated/api.py` | 155 | `GET` | `/federated/{id}/credentials/schema` | `router` |
| `backend/onyx/server/federated/api.py` | 200 | `GET` | `/federated/sources/{source}/configuration/schema` | `router` |
| `backend/onyx/server/federated/api.py` | 228 | `GET` | `/federated/sources/{source}/credentials/schema` | `router` |
| `backend/onyx/server/federated/api.py` | 259 | `POST` | `/federated/sources/{source}/credentials/validate` | `router` |
| `backend/onyx/server/federated/api.py` | 283 | `HEAD` | `/federated/{id}/entities/validate` | `router` |
| `backend/onyx/server/federated/api.py` | 327 | `GET` | `/federated/{id}/authorize` | `router` |
| `backend/onyx/server/federated/api.py` | 376 | `POST` | `/federated/callback` | `router` |
| `backend/onyx/server/federated/api.py` | 456 | `GET` | `/federated` | `router` |
| `backend/onyx/server/federated/api.py` | 476 | `GET` | `/federated/oauth-status` | `router` |
| `backend/onyx/server/federated/api.py` | 521 | `GET` | `/federated/{id}` | `router` |
| `backend/onyx/server/federated/api.py` | 567 | `PUT` | `/federated/{id}` | `router` |
| `backend/onyx/server/federated/api.py` | 599 | `DELETE` | `/federated/{id}` | `router` |
| `backend/onyx/server/federated/api.py` | 617 | `DELETE` | `/federated/{id}/oauth` | `router` |
| `backend/onyx/server/kg/api.py` | 58 | `GET` | `/admin/kg/exposed` | `admin_router` |
| `backend/onyx/server/kg/api.py` | 69 | `PUT` | `/admin/kg/reset` | `admin_router` |
| `backend/onyx/server/kg/api.py` | 82 | `GET` | `/admin/kg/config` | `admin_router` |
| `backend/onyx/server/kg/api.py` | 90 | `PUT` | `/admin/kg/config` | `admin_router` |
| `backend/onyx/server/kg/api.py` | 176 | `GET` | `/admin/kg/entity-types` | `admin_router` |
| `backend/onyx/server/kg/api.py` | 206 | `PUT` | `/admin/kg/entity-types` | `admin_router` |
| `backend/onyx/server/manage/administrative.py` | 61 | `GET` | `/manage/admin/doc-boosts` | `router` |
| `backend/onyx/server/manage/administrative.py` | 87 | `POST` | `/manage/admin/doc-boosts` | `router` |
| `backend/onyx/server/manage/administrative.py` | 102 | `POST` | `/manage/admin/doc-hidden` | `router` |
| `backend/onyx/server/manage/administrative.py` | 117 | `GET` | `/manage/admin/genai-api-key/validate` | `router` |
| `backend/onyx/server/manage/administrative.py` | 149 | `POST` | `/manage/admin/deletion-attempt` | `router` |
| `backend/onyx/server/manage/administrative.py` | 232 | `GET` | `/manage/admin/indexing/failed-documents` | `router` |
| `backend/onyx/server/manage/code_interpreter/api.py` | 23 | `GET` | `/admin/code-interpreter/health` | `admin_router` |
| `backend/onyx/server/manage/code_interpreter/api.py` | 38 | `GET` | `/admin/code-interpreter` | `admin_router` |
| `backend/onyx/server/manage/code_interpreter/api.py` | 47 | `PUT` | `/admin/code-interpreter` | `admin_router` |
| `backend/onyx/server/manage/discord_bot/api.py` | 65 | `GET` | `/manage/admin/discord-bot/config` | `router` |
| `backend/onyx/server/manage/discord_bot/api.py` | 82 | `POST` | `/manage/admin/discord-bot/config` | `router` |
| `backend/onyx/server/manage/discord_bot/api.py` | 109 | `DELETE` | `/manage/admin/discord-bot/config` | `router` |
| `backend/onyx/server/manage/discord_bot/api.py` | 133 | `DELETE` | `/manage/admin/discord-bot/service-api-key` | `router` |
| `backend/onyx/server/manage/discord_bot/api.py` | 156 | `GET` | `/manage/admin/discord-bot/guilds` | `router` |
| `backend/onyx/server/manage/discord_bot/api.py` | 166 | `POST` | `/manage/admin/discord-bot/guilds` | `router` |
| `backend/onyx/server/manage/discord_bot/api.py` | 184 | `GET` | `/manage/admin/discord-bot/guilds/{config_id}` | `router` |
| `backend/onyx/server/manage/discord_bot/api.py` | 197 | `PATCH` | `/manage/admin/discord-bot/guilds/{config_id}` | `router` |
| `backend/onyx/server/manage/discord_bot/api.py` | 220 | `DELETE` | `/manage/admin/discord-bot/guilds/{config_id}` | `router` |
| `backend/onyx/server/manage/discord_bot/api.py` | 247 | `GET` | `/manage/admin/discord-bot/guilds/{config_id}/channels` | `router` |
| `backend/onyx/server/manage/discord_bot/api.py` | 266 | `PATCH` | `/manage/admin/discord-bot/guilds/{guild_config_id}/channels/{channel_config_id}` | `router` |
| `backend/onyx/server/manage/embedding/api.py` | 38 | `POST` | `/admin/embedding/test-embedding` | `admin_router` |
| `backend/onyx/server/manage/embedding/api.py` | 70 | `GET` | `/admin/embedding` | `admin_router` |
| `backend/onyx/server/manage/embedding/api.py` | 79 | `GET` | `/admin/embedding/embedding-provider` | `admin_router` |
| `backend/onyx/server/manage/embedding/api.py` | 90 | `GET` | `/admin/embedding/embedding-provider/{provider_type}` | `admin_router` |
| `backend/onyx/server/manage/embedding/api.py` | 105 | `DELETE` | `/admin/embedding/embedding-provider/{provider_type}` | `admin_router` |
| `backend/onyx/server/manage/embedding/api.py` | 125 | `PUT` | `/admin/embedding/embedding-provider` | `admin_router` |
| `backend/onyx/server/manage/get_state.py` | 135 | `GET` | `/health/ready` | `router` |
| `backend/onyx/server/manage/get_state.py` | 187 | `GET` | `/health` | `router` |
| `backend/onyx/server/manage/get_state.py` | 199 | `GET` | `/auth/type` | `router` |
| `backend/onyx/server/manage/get_state.py` | 240 | `GET` | `/version` | `router` |
| `backend/onyx/server/manage/get_state.py` | 245 | `GET` | `/versions` | `router` |
| `backend/onyx/server/manage/image_generation/api.py` | 207 | `POST` | `/admin/image-generation/test` | `admin_router` |
| `backend/onyx/server/manage/image_generation/api.py` | 306 | `POST` | `/admin/image-generation/config` | `admin_router` |
| `backend/onyx/server/manage/image_generation/api.py` | 370 | `GET` | `/admin/image-generation/config` | `admin_router` |
| `backend/onyx/server/manage/image_generation/api.py` | 380 | `GET` | `/admin/image-generation/config/{image_provider_id}/credentials` | `admin_router` |
| `backend/onyx/server/manage/image_generation/api.py` | 400 | `PUT` | `/admin/image-generation/config/{image_provider_id}` | `admin_router` |
| `backend/onyx/server/manage/image_generation/api.py` | 498 | `DELETE` | `/admin/image-generation/config/{image_provider_id}` | `admin_router` |
| `backend/onyx/server/manage/image_generation/api.py` | 530 | `POST` | `/admin/image-generation/config/{image_provider_id}/default` | `admin_router` |
| `backend/onyx/server/manage/image_generation/api.py` | 543 | `DELETE` | `/admin/image-generation/config/{image_provider_id}/default` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 400 | `GET` | `/admin/llm/custom-provider-names` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 423 | `GET` | `/admin/llm/built-in/options` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 430 | `GET` | `/admin/llm/built-in/options/{provider_name}` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 442 | `POST` | `/admin/llm/test` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 506 | `POST` | `/admin/llm/test/default` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 521 | `GET` | `/admin/llm/provider` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 571 | `GET` | `/admin/llm/provider/{provider_id}` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 589 | `PUT` | `/admin/llm/provider` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 732 | `DELETE` | `/admin/llm/provider/{provider_id}` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 767 | `POST` | `/admin/llm/default` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 781 | `POST` | `/admin/llm/default-vision` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 795 | `POST` | `/admin/llm/default-chat-naming` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 809 | `DELETE` | `/admin/llm/default-chat-naming` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 820 | `POST` | `/admin/llm/default-craft` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 834 | `DELETE` | `/admin/llm/default-craft` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 844 | `GET` | `/admin/llm/auto-config` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 862 | `GET` | `/admin/llm/vision-providers` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 907 | `GET` | `/llm/provider` | `basic_router` |
| `backend/onyx/server/manage/llm/api.py` | 1052 | `GET` | `/llm/persona/{persona_id}/providers` | `basic_router` |
| `backend/onyx/server/manage/llm/api.py` | 1152 | `GET` | `/admin/llm/provider-contextual-cost` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 1235 | `POST` | `/admin/llm/bedrock/available-models` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 1434 | `POST` | `/admin/llm/ollama/available-models` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 1560 | `POST` | `/admin/llm/openrouter/available-models` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 1645 | `POST` | `/admin/llm/lm-studio/available-models` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 1768 | `POST` | `/admin/llm/litellm/available-models` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 1917 | `POST` | `/admin/llm/bifrost/available-models` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 2056 | `POST` | `/admin/llm/nebius-tokenfactory/available-models` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 2170 | `POST` | `/admin/llm/openai-compatible/available-models` | `admin_router` |
| `backend/onyx/server/manage/llm/api.py` | 2294 | `POST` | `/admin/llm/portkey/available-models` | `admin_router` |
| `backend/onyx/server/manage/oauth_test.py` | 47 | `GET` | `/admin/oauth-test/claims` | `router` |
| `backend/onyx/server/manage/opensearch_migration/api.py` | 23 | `GET` | `/admin/opensearch-migration/status` | `admin_router` |
| `backend/onyx/server/manage/opensearch_migration/api.py` | 42 | `GET` | `/admin/opensearch-migration/retrieval` | `admin_router` |
| `backend/onyx/server/manage/opensearch_migration/api.py` | 54 | `PUT` | `/admin/opensearch-migration/retrieval` | `admin_router` |
| `backend/onyx/server/manage/search_settings.py` | 96 | `POST` | `/search-settings/set-new-search-settings` | `router` |
| `backend/onyx/server/manage/search_settings.py` | 405 | `POST` | `/search-settings/cancel-new-embedding` | `router` |
| `backend/onyx/server/manage/search_settings.py` | 473 | `DELETE` | `/search-settings/delete-search-settings` | `router` |
| `backend/onyx/server/manage/search_settings.py` | 488 | `GET` | `/search-settings/get-current-search-settings` | `router` |
| `backend/onyx/server/manage/search_settings.py` | 497 | `GET` | `/search-settings/get-secondary-search-settings` | `router` |
| `backend/onyx/server/manage/search_settings.py` | 523 | `GET` | `/search-settings/reindex-progress` | `router` |
| `backend/onyx/server/manage/search_settings.py` | 536 | `GET` | `/search-settings/reindex-errors` | `router` |
| `backend/onyx/server/manage/search_settings.py` | 558 | `POST` | `/search-settings/reindex/port/resume` | `router` |
| `backend/onyx/server/manage/search_settings.py` | 597 | `GET` | `/search-settings/get-all-search-settings` | `router` |
| `backend/onyx/server/manage/search_settings.py` | 638 | `POST` | `/search-settings/update-inference-settings` | `router` |
| `backend/onyx/server/manage/search_settings.py` | 705 | `GET` | `/search-settings/unstructured-api-key-set` | `router` |
| `backend/onyx/server/manage/search_settings.py` | 713 | `PUT` | `/search-settings/upsert-unstructured-api-key` | `router` |
| `backend/onyx/server/manage/search_settings.py` | 721 | `DELETE` | `/search-settings/delete-unstructured-api-key` | `router` |
| `backend/onyx/server/manage/slack_bot.py` | 113 | `POST` | `/manage/admin/slack-app/channel` | `router` |
| `backend/onyx/server/manage/slack_bot.py` | 153 | `PATCH` | `/manage/admin/slack-app/channel/{slack_channel_config_id}` | `router` |
| `backend/onyx/server/manage/slack_bot.py` | 215 | `DELETE` | `/manage/admin/slack-app/channel/{slack_channel_config_id}` | `router` |
| `backend/onyx/server/manage/slack_bot.py` | 227 | `GET` | `/manage/admin/slack-app/channel` | `router` |
| `backend/onyx/server/manage/slack_bot.py` | 239 | `POST` | `/manage/admin/slack-app/bots` | `router` |
| `backend/onyx/server/manage/slack_bot.py` | 284 | `PATCH` | `/manage/admin/slack-app/bots/{slack_bot_id}` | `router` |
| `backend/onyx/server/manage/slack_bot.py` | 306 | `DELETE` | `/manage/admin/slack-app/bots/{slack_bot_id}` | `router` |
| `backend/onyx/server/manage/slack_bot.py` | 318 | `GET` | `/manage/admin/slack-app/bots/{slack_bot_id}` | `router` |
| `backend/onyx/server/manage/slack_bot.py` | 331 | `GET` | `/manage/admin/slack-app/bots` | `router` |
| `backend/onyx/server/manage/slack_bot.py` | 342 | `GET` | `/manage/admin/slack-app/bots/{bot_id}/config` | `router` |
| `backend/onyx/server/manage/sso/api.py` | 139 | `GET` | `/admin/sso/provider-type` | `admin_router` |
| `backend/onyx/server/manage/sso/api.py` | 148 | `GET` | `/admin/sso/provider` | `admin_router` |
| `backend/onyx/server/manage/sso/api.py` | 159 | `POST` | `/admin/sso/provider` | `admin_router` |
| `backend/onyx/server/manage/sso/api.py` | 196 | `PATCH` | `/admin/sso/provider/{provider_id}` | `admin_router` |
| `backend/onyx/server/manage/sso/api.py` | 236 | `POST` | `/admin/sso/provider/{provider_id}/enabled` | `admin_router` |
| `backend/onyx/server/manage/sso/api.py` | 331 | `POST` | `/admin/sso/domain/records` | `admin_router` |
| `backend/onyx/server/manage/sso/api.py` | 343 | `POST` | `/admin/sso/domain/verify-dns` | `admin_router` |
| `backend/onyx/server/manage/tracing/api.py` | 101 | `GET` | `/admin/tracing/providers` | `admin_router` |
| `backend/onyx/server/manage/tracing/api.py` | 115 | `POST` | `/admin/tracing/providers` | `admin_router` |
| `backend/onyx/server/manage/tracing/api.py` | 137 | `DELETE` | `/admin/tracing/providers/{provider_type}` | `admin_router` |
| `backend/onyx/server/manage/tracing/api.py` | 150 | `POST` | `/admin/tracing/providers/test` | `admin_router` |
| `backend/onyx/server/manage/tracing/api.py` | 178 | `POST` | `/admin/tracing/providers/{provider_type}/adopt-env` | `admin_router` |
| `backend/onyx/server/manage/users.py` | 156 | `PATCH` | `/manage/admin/users/admin-access` | `router` |
| `backend/onyx/server/manage/users.py` | 195 | `PATCH` | `/manage/admin/users/craft-enabled` | `router` |
| `backend/onyx/server/manage/users.py` | 239 | `POST` | `/manage/users/test-upsert-user` | `router` |
| `backend/onyx/server/manage/users.py` | 258 | `GET` | `/manage/users/accepted` | `router` |
| `backend/onyx/server/manage/users.py` | 338 | `GET` | `/manage/users/accepted/all` | `router` |
| `backend/onyx/server/manage/users.py` | 382 | `GET` | `/manage/users/counts` | `router` |
| `backend/onyx/server/manage/users.py` | 390 | `GET` | `/manage/users/invited` | `router` |
| `backend/onyx/server/manage/users.py` | 432 | `GET` | `/manage/users` | `router` |
| `backend/onyx/server/manage/users.py` | 514 | `GET` | `/manage/users/download` | `router` |
| `backend/onyx/server/manage/users.py` | 553 | `PUT` | `/manage/admin/users` | `router` |
| `backend/onyx/server/manage/users.py` | 733 | `PATCH` | `/manage/admin/remove-invited-user` | `router` |
| `backend/onyx/server/manage/users.py` | 768 | `PATCH` | `/manage/admin/deactivate-user` | `router` |
| `backend/onyx/server/manage/users.py` | 808 | `DELETE` | `/manage/admin/delete-user` | `router` |
| `backend/onyx/server/manage/users.py` | 865 | `PATCH` | `/manage/admin/activate-user` | `router` |
| `backend/onyx/server/manage/users.py` | 904 | `GET` | `/manage/admin/valid-domains` | `router` |
| `backend/onyx/server/manage/users.py` | 914 | `GET` | `/users` | `router` |
| `backend/onyx/server/manage/users.py` | 1037 | `GET` | `/me/permissions` | `router` |
| `backend/onyx/server/manage/users.py` | 1049 | `GET` | `/me` | `router` |
| `backend/onyx/server/manage/users.py` | 1167 | `PATCH` | `/temperature-default` | `router` |
| `backend/onyx/server/manage/users.py` | 1195 | `PATCH` | `/reasoning-effort-default` | `router` |
| `backend/onyx/server/manage/users.py` | 1206 | `PATCH` | `/temperature-override-enabled` | `router` |
| `backend/onyx/server/manage/users.py` | 1221 | `PATCH` | `/shortcut-enabled` | `router` |
| `backend/onyx/server/manage/users.py` | 1230 | `PATCH` | `/paste-as-tile` | `router` |
| `backend/onyx/server/manage/users.py` | 1239 | `PATCH` | `/auto-scroll` | `router` |
| `backend/onyx/server/manage/users.py` | 1248 | `PATCH` | `/user/theme-preference` | `router` |
| `backend/onyx/server/manage/users.py` | 1275 | `PATCH` | `/user/language` | `router` |
| `backend/onyx/server/manage/users.py` | 1286 | `PATCH` | `/user/chat-background` | `router` |
| `backend/onyx/server/manage/users.py` | 1295 | `PATCH` | `/user/default-app-mode` | `router` |
| `backend/onyx/server/manage/users.py` | 1304 | `PATCH` | `/user/default-model` | `router` |
| `backend/onyx/server/manage/users.py` | 1313 | `PATCH` | `/user/personalization` | `router` |
| `backend/onyx/server/manage/users.py` | 1361 | `PATCH` | `/user/pinned-assistants` | `router` |
| `backend/onyx/server/manage/users.py` | 1399 | `PATCH` | `/user/assistant-list/update/{assistant_id}` | `router` |
| `backend/onyx/server/manage/users.py` | 1421 | `GET` | `/user/assistant/preferences` | `router` |
| `backend/onyx/server/manage/users.py` | 1438 | `PATCH` | `/user/assistant/{assistant_id}/preferences` | `router` |
| `backend/onyx/server/manage/users.py` | 1451 | `GET` | `/user/files/recent` | `router` |
| `backend/onyx/server/manage/voice/api.py` | 172 | `GET` | `/admin/voice/providers` | `admin_router` |
| `backend/onyx/server/manage/voice/api.py` | 182 | `POST` | `/admin/voice/providers` | `admin_router` |
| `backend/onyx/server/manage/voice/api.py` | 258 | `DELETE` | `/admin/voice/providers/{provider_id}` | `admin_router` |
| `backend/onyx/server/manage/voice/api.py` | 272 | `POST` | `/admin/voice/providers/{provider_id}/activate-stt` | `admin_router` |
| `backend/onyx/server/manage/voice/api.py` | 284 | `POST` | `/admin/voice/providers/{provider_id}/deactivate-stt` | `admin_router` |
| `backend/onyx/server/manage/voice/api.py` | 296 | `POST` | `/admin/voice/providers/{provider_id}/activate-tts` | `admin_router` |
| `backend/onyx/server/manage/voice/api.py` | 311 | `POST` | `/admin/voice/providers/{provider_id}/deactivate-tts` | `admin_router` |
| `backend/onyx/server/manage/voice/api.py` | 323 | `POST` | `/admin/voice/providers/test` | `admin_router` |
| `backend/onyx/server/manage/voice/api.py` | 401 | `GET` | `/admin/voice/providers/{provider_id}/voices` | `admin_router` |
| `backend/onyx/server/manage/voice/api.py` | 425 | `GET` | `/admin/voice/voices` | `admin_router` |
| `backend/onyx/server/manage/voice/user_api.py` | 42 | `GET` | `/voice/status` | `router` |
| `backend/onyx/server/manage/voice/user_api.py` | 56 | `POST` | `/voice/transcribe` | `router` |
| `backend/onyx/server/manage/voice/user_api.py` | 145 | `POST` | `/voice/synthesize` | `router` |
| `backend/onyx/server/manage/voice/user_api.py` | 236 | `PATCH` | `/voice/settings` | `router` |
| `backend/onyx/server/manage/voice/user_api.py` | 258 | `POST` | `/voice/ws-token` | `router` |
| `backend/onyx/server/manage/web_search/api.py` | 69 | `GET` | `/admin/web-search/search-providers` | `admin_router` |
| `backend/onyx/server/manage/web_search/api.py` | 92 | `POST` | `/admin/web-search/search-providers` | `admin_router` |
| `backend/onyx/server/manage/web_search/api.py` | 154 | `DELETE` | `/admin/web-search/search-providers/{provider_id}` | `admin_router` |
| `backend/onyx/server/manage/web_search/api.py` | 166 | `POST` | `/admin/web-search/search-providers/{provider_id}/activate` | `admin_router` |
| `backend/onyx/server/manage/web_search/api.py` | 188 | `POST` | `/admin/web-search/search-providers/{provider_id}/deactivate` | `admin_router` |
| `backend/onyx/server/manage/web_search/api.py` | 199 | `POST` | `/admin/web-search/search-providers/test` | `admin_router` |
| `backend/onyx/server/manage/web_search/api.py` | 249 | `GET` | `/admin/web-search/content-providers` | `admin_router` |
| `backend/onyx/server/manage/web_search/api.py` | 272 | `POST` | `/admin/web-search/content-providers` | `admin_router` |
| `backend/onyx/server/manage/web_search/api.py` | 334 | `DELETE` | `/admin/web-search/content-providers/{provider_id}` | `admin_router` |
| `backend/onyx/server/manage/web_search/api.py` | 346 | `POST` | `/admin/web-search/content-providers/{provider_id}/activate` | `admin_router` |
| `backend/onyx/server/manage/web_search/api.py` | 368 | `POST` | `/admin/web-search/content-providers/reset-default` | `admin_router` |
| `backend/onyx/server/manage/web_search/api.py` | 383 | `POST` | `/admin/web-search/content-providers/{provider_id}/deactivate` | `admin_router` |
| `backend/onyx/server/manage/web_search/api.py` | 394 | `POST` | `/admin/web-search/content-providers/test` | `admin_router` |
| `backend/onyx/server/oidc_multi.py` | 314 | `GET` | `/auth/oidc/{provider_name}/authorize` | `router` |
| `backend/onyx/server/oidc_multi.py` | 382 | `GET` | `/auth/oidc/callback` | `router` |
| `backend/onyx/server/oidc_multi.py` | 422 | `GET` | `/auth/oidc/{provider_name}/callback` | `router` |
| `backend/onyx/server/onyx_api/ingestion.py` | 58 | `GET` | `/onyx-api/connector-docs/{cc_pair_id}` | `router` |
| `backend/onyx/server/onyx_api/ingestion.py` | 84 | `GET` | `/onyx-api/ingestion` | `router` |
| `backend/onyx/server/onyx_api/ingestion.py` | 101 | `POST` | `/onyx-api/ingestion` | `router` |
| `backend/onyx/server/onyx_api/ingestion.py` | 237 | `DELETE` | `/onyx-api/ingestion/{document_id}` | `router` |
| `backend/onyx/server/pat/api.py` | 44 | `GET` | `/user/pats/scopes` | `router` |
| `backend/onyx/server/pat/api.py` | 52 | `GET` | `/user/pats` | `router` |
| `backend/onyx/server/pat/api.py` | 62 | `POST` | `/user/pats` | `router` |
| `backend/onyx/server/pat/api.py` | 94 | `DELETE` | `/user/pats/{token_id}` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 198 | `GET` | `/chat/get-user-chat-sessions` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 257 | `PUT` | `/chat/update-chat-session-temperature` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 297 | `PUT` | `/chat/update-chat-session-reasoning` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 332 | `PUT` | `/chat/update-chat-session-model` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 349 | `GET` | `/chat/get-chat-session/{session_id}` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 462 | `POST` | `/chat/create-chat-session` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 545 | `PUT` | `/chat/rename-chat-session` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 616 | `PATCH` | `/chat/chat-session/{session_id}` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 652 | `DELETE` | `/chat/delete-all-chat-sessions` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 676 | `DELETE` | `/chat/delete-chat-session/{session_id}` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 713 | `GET` | `/chat/incognito-availability` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 725 | `POST` | `/chat/end-incognito-session/{session_id}` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 771 | `POST` | `/chat/send-chat-message` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 947 | `PUT` | `/chat/set-message-as-latest` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 968 | `PUT` | `/chat/set-preferred-response` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 992 | `POST` | `/chat/create-chat-message-feedback` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 1013 | `DELETE` | `/chat/remove-chat-message-feedback` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 1035 | `GET` | `/chat/max-selected-document-tokens` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 1064 | `GET` | `/chat/available-context-tokens/{session_id}` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 1118 | `POST` | `/chat/seed-chat-session-from-slack` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 1142 | `GET` | `/chat/file/{file_id:path}` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 1195 | `GET` | `/chat/search` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 1280 | `GET` | `/chat/chat-session/{session_id}/resume-stream` | `router` |
| `backend/onyx/server/query_and_chat/chat_backend.py` | 1360 | `POST` | `/chat/stop-chat-session/{chat_session_id}` | `router` |
| `backend/onyx/server/query_and_chat/query_backend.py` | 33 | `POST` | `/admin/search` | `admin_router` |
| `backend/onyx/server/query_and_chat/query_backend.py` | 82 | `GET` | `/query/valid-tags` | `basic_router` |
| `backend/onyx/server/saml_multi.py` | 255 | `GET` | `/auth/saml/authorize` | `router` |
| `backend/onyx/server/saml_multi.py` | 268 | `GET` | `/auth/saml/callback` | `router` |
| `backend/onyx/server/saml_multi.py` | 284 | `POST` | `/auth/saml/callback` | `router` |
| `backend/onyx/server/saml_multi.py` | 300 | `GET` | `/auth/saml/{provider_name}/authorize` | `router` |
| `backend/onyx/server/saml_multi.py` | 362 | `POST` | `/auth/saml/logout` | `router` |
| `backend/onyx/server/security/api.py` | 60 | `GET` | `/admin/security` | `admin_router` |
| `backend/onyx/server/security/api.py` | 67 | `GET` | `/admin/security/pinned-fields` | `admin_router` |
| `backend/onyx/server/security/api.py` | 75 | `PUT` | `/admin/security` | `admin_router` |
| `backend/onyx/server/settings/api.py` | 68 | `PATCH` | `/admin/settings` | `admin_router` |
| `backend/onyx/server/settings/api.py` | 149 | `GET` | `/settings` | `basic_router` |
| `backend/onyx/server/sso_discovery.py` | 147 | `POST` | `/auth/sso/discover` | `router` |
| `backend/tests/external_dependency_unit/server/test_feedback_rate_limiting.py` | 37 | `POST` | `/feedback` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_api_key.py` | 51 | `GET` | `/healthz` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_google_oauth.py` | 229 | `GET` | `/healthz` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_google_oauth.py` | 234 | `GET` | `/info` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_oauth.py` | 64 | `GET` | `/.well-known/oauth-protected-resource` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_oauth.py` | 65 | `GET` | `/.well-known/oauth-protected-resource/{_suffix:path}` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_oauth.py` | 82 | `GET` | `/healthz` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_per_user_key.py` | 200 | `GET` | `/healthz` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mock_oidc_idp.py` | 255 | `GET` | `/.well-known/oauth-authorization-server` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mock_oidc_idp.py` | 256 | `GET` | `/.well-known/openid-configuration` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mock_oidc_idp.py` | 260 | `GET` | `/jwks` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mock_oidc_idp.py` | 264 | `GET` | `/healthz` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mock_oidc_idp.py` | 268 | `GET` | `/test/status` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mock_oidc_idp.py` | 276 | `POST` | `/register` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mock_oidc_idp.py` | 304 | `GET` | `/authorize` | `app` |
| `backend/tests/integration/mock_services/mcp_test_server/run_mock_oidc_idp.py` | 329 | `POST` | `/token` | `app` |
| `backend/tests/integration/mock_services/mock_connector_server/main.py` | 24 | `POST` | `/set-behavior` | `app` |
| `backend/tests/integration/mock_services/mock_connector_server/main.py` | 31 | `GET` | `/get-documents` | `app` |
| `backend/tests/integration/mock_services/mock_connector_server/main.py` | 49 | `POST` | `/add-checkpoint` | `app` |
| `backend/tests/integration/mock_services/mock_connector_server/main.py` | 56 | `GET` | `/get-checkpoints` | `app` |
| `backend/tests/integration/mock_services/mock_connector_server/main.py` | 64 | `POST` | `/reset` | `app` |
| `backend/tests/integration/mock_services/mock_connector_server/main.py` | 71 | `GET` | `/health` | `app` |
| `backend/tests/unit/onyx/error_handling/test_error_contract.py` | 34 | `GET` | `/http-error` | `app` |
| `backend/tests/unit/onyx/error_handling/test_error_contract.py` | 38 | `GET` | `/dict-detail` | `app` |
| `backend/tests/unit/onyx/error_handling/test_error_contract.py` | 42 | `GET` | `/value-error` | `app` |
| `backend/tests/unit/onyx/error_handling/test_error_contract.py` | 46 | `POST` | `/validated` | `app` |
| `backend/tests/unit/onyx/error_handling/test_exceptions.py` | 52 | `GET` | `/boom` | `app` |
| `backend/tests/unit/onyx/error_handling/test_exceptions.py` | 56 | `GET` | `/boom-override` | `app` |
| `backend/tests/unit/onyx/error_handling/test_exceptions.py` | 64 | `GET` | `/boom-default-msg` | `app` |
| `backend/tests/unit/onyx/server/auth/test_captcha_api.py` | 23 | `GET` | `/auth/oauth/callback` | `app` |
| `backend/tests/unit/onyx/server/auth/test_captcha_api.py` | 27 | `POST` | `/auth/register` | `app` |
| `backend/tests/unit/onyx/server/auth/test_captcha_api.py` | 34 | `GET` | `/me` | `app` |
| `backend/tests/unit/onyx/server/auth/test_login_captcha_middleware.py` | 19 | `POST` | `/auth/login` | `app` |
| `backend/tests/unit/onyx/server/auth/test_login_captcha_middleware.py` | 23 | `POST` | `/auth/register` | `app` |
| `backend/tests/unit/onyx/server/auth/test_login_captcha_middleware.py` | 27 | `GET` | `/auth/login` | `app` |
| `backend/tests/unit/onyx/server/test_pool_metrics.py` | 253 | `GET` | `/api/test` | `app` |
| `backend/tests/unit/onyx/server/test_pool_metrics.py` | 257 | `GET` | `/api/items/{item_id}` | `app` |
| `backend/tests/unit/onyx/server/test_pool_metrics.py` | 272 | `GET` | `/api/items/{item_id}` | `app` |
| `backend/tests/unit/onyx/server/test_pool_metrics.py` | 285 | `GET` | `/api/test` | `app` |
| `backend/tests/unit/onyx/server/test_pool_metrics.py` | 298 | `GET` | `/api/health` | `app` |
| `backend/tests/unit/onyx/server/test_prometheus_instrumentation.py` | 177 | `GET` | `/slow` | `app` |
| `backend/tests/unit/onyx/server/test_prometheus_instrumentation.py` | 217 | `GET` | `/concurrent` | `app` |
| `backend/tests/unit/onyx/utils/test_client_ip.py` | 90 | `GET` | `/echo-ip` | `app` |
| `backend/tests/unit/shared_configs/test_user_id_contextvar.py` | 81 | `POST` | `/stream` | `app` |
| `backend/tests/unit/shared_configs/test_user_id_contextvar.py` | 111 | `GET` | `/plain` | `app` |
| `backend/tests/unit/shared_configs/test_user_id_contextvar.py` | 137 | `POST` | `/anonymous-stream` | `app` |

## Next.js Static Route Handlers

| File | Line | Method | Route path |
| --- | ---: | --- | --- |
| `web/src/app/admin/connectors/[connector]/auth/callback/route.ts` | 11 | `GET` | `/admin/connectors/[connector]/auth/callback` |
| `web/src/app/api/[...path]/route.ts` | 10 | `GET` | `/api/[...path]` |
| `web/src/app/api/[...path]/route.ts` | 18 | `POST` | `/api/[...path]` |
| `web/src/app/api/[...path]/route.ts` | 26 | `PUT` | `/api/[...path]` |
| `web/src/app/api/[...path]/route.ts` | 34 | `PATCH` | `/api/[...path]` |
| `web/src/app/api/[...path]/route.ts` | 42 | `DELETE` | `/api/[...path]` |
| `web/src/app/api/[...path]/route.ts` | 50 | `HEAD` | `/api/[...path]` |
| `web/src/app/api/[...path]/route.ts` | 58 | `OPTIONS` | `/api/[...path]` |
| `web/src/app/api/chat/mcp/oauth/callback/route.ts` | 8 | `GET` | `/api/chat/mcp/oauth/callback` |
| `web/src/app/auth/logout/route.ts` | 5 | `POST` | `/auth/logout` |
| `web/src/app/auth/oauth/callback/route.ts` | 21 | `GET` | `/auth/oauth/callback` |
| `web/src/app/auth/oidc/callback/route.ts` | 6 | `GET` | `/auth/oidc/callback` |
| `web/src/app/auth/saml/callback/route.ts` | 80 | `GET` | `/auth/saml/callback` |
| `web/src/app/auth/saml/callback/route.ts` | 84 | `POST` | `/auth/saml/callback` |
| `web/src/app/connector/oauth/callback/[source]/route.tsx` | 13 | `GET` | `/connector/oauth/callback/[source]` |
| `web/src/app/mcp/[[...path]]/route.ts` | 108 | `GET` | `/mcp/[[...path]]` |
| `web/src/app/mcp/[[...path]]/route.ts` | 109 | `POST` | `/mcp/[[...path]]` |
| `web/src/app/mcp/[[...path]]/route.ts` | 110 | `PUT` | `/mcp/[[...path]]` |
| `web/src/app/mcp/[[...path]]/route.ts` | 111 | `PATCH` | `/mcp/[[...path]]` |
| `web/src/app/mcp/[[...path]]/route.ts` | 112 | `DELETE` | `/mcp/[[...path]]` |
| `web/src/app/mcp/[[...path]]/route.ts` | 113 | `HEAD` | `/mcp/[[...path]]` |
| `web/src/app/mcp/[[...path]]/route.ts` | 114 | `OPTIONS` | `/mcp/[[...path]]` |

## Limitations

- Parent router prefixes may be applied elsewhere at include/mount time.
- Dynamic routes and programmatically generated routes may require later manual or runtime enumeration.
- Compose and Helm definitions may represent alternatives, tests, disabled components, or deployment options.
- No service is considered running merely because a definition exists.
- No endpoint is considered externally reachable merely because source code declares a route.
