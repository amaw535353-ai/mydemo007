# Phase 4 Action 4.4 - Kubernetes Security Foundations Evidence

## Provenance

- Branch: `security/phase-4-cloud-devsecops`
- Baseline HEAD: `de506d40d8a315518b4359283f2a4c791fb30428`

## Observation class

**STATIC SOURCE CANDIDATES ONLY. RUNTIME/DEPLOYMENT BEHAVIOR IS UNVERIFIED.**

## Review scope

Kubernetes workload and service definitions, namespaces, RBAC, service accounts, Secrets, ConfigMaps, ingress, network policy, workload security contexts and resource controls.

## Static observations

- Candidate files: **319**
- Matching lines: **2435**

## Representative candidate files

- `backend/ee/onyx/db/license.py`
- `backend/ee/onyx/server/oauth/confluence_cloud.py`
- `backend/ee/onyx/server/query_and_chat/token_limit.py`
- `backend/ee/onyx/server/scim/api.py`
- `backend/ee/onyx/server/seeding.py`
- `backend/ee/onyx/server/token_rate_limits/api.py`
- `backend/model_server/legacy/custom_models.py`
- `backend/onyx/auth/mobile_sso/code_store.py`
- `backend/onyx/auth/permission_projection.py`
- `backend/onyx/background/celery/apps/app_base.py`
- `backend/onyx/background/celery/celery_k8s_probe.py`
- `backend/onyx/background/celery/tasks/monitoring/tasks.py`
- `backend/onyx/background/celery/tasks/shared/RetryDocumentIndex.py`
- `backend/onyx/connectors/slack/source_operations.py`
- `backend/onyx/context/search/retrieval/search_runner.py`
- `backend/onyx/db/user_usage.py`
- `backend/onyx/document_index/disabled.py`
- `backend/onyx/document_index/interfaces_new.py`
- `backend/onyx/document_index/opensearch/opensearch_document_index.py`
- `backend/onyx/document_index/vespa/chunk_retrieval.py`

## Security interpretation

The matches identify source/configuration review candidates only.

They do not prove:

- that a container is actually built or executed;
- that a workload is deployed;
- that Kubernetes or Docker is reachable;
- that privilege controls are effective at runtime;
- that images are trusted or vulnerability-free.

## Safety

- No container started.
- No image pulled.
- No image pushed.
- No Kubernetes cluster contacted.
- No deployment executed.
- No registry contacted.
- No cloud resource created.
- No secret value displayed.
- No billable resource used.

## Result

Action 4.4 static mapping result: **PASS**
