# Phase 5 Action 5.5 - Embeddings & Vector Search Foundations Evidence

## Provenance
- Branch: `security/phase-5-ai-foundations`
- Baseline HEAD: `075eb44feb87ddbbdb93acb93baf72b6f2254035`

## Observation boundary

**STATIC SOURCE CANDIDATES ONLY. AI RUNTIME BEHAVIOR IS UNVERIFIED.**

## Review scope

Embedding generation and models, vector representations, similarity search, vector stores/databases, collections, namespaces, metadata filters, indexing and vector-data lifecycle boundaries.

## Static observations
- Candidate files: **423**
- Matching lines: **3138**

## Representative candidate files

- `AGENTS.md`
- `backend/AGENTS.md`
- `backend/alembic/versions/1f60f60c3401_embedding_model_search_settings.py`
- `backend/alembic/versions/44f856ae2a4a_add_cloud_embedding_model.py`
- `backend/alembic/versions/495cb26ce93e_create_knowlege_graph_tables.py`
- `backend/alembic/versions/5d12a446f5c0_add_api_version_and_deployment_name_to_.py`
- `backend/alembic/versions/776b3bbe9092_remove_remaining_enums.py`
- `backend/alembic/versions/b7c2b63c4a03_add_background_reindex_enabled_field.py`
- `backend/alembic/versions/bceb1e139447_add_base_url_to_cloudembeddingprovider.py`
- `backend/alembic/versions/c7d1f0a4b8e2_add_doc_created_at_to_document.py`
- `backend/alembic/versions/d9ec13955951_remove__dim_suffix_from_model_name.py`
- `backend/alembic/versions/dbaa756c2ccf_embedding_models.py`
- `backend/alembic/versions/f17bf3b0d9f1_embedding_provider_by_provider_type.py`
- `backend/Dockerfile.model_server`
- `backend/ee/onyx/background/celery/tasks/log_export/tasks.py`
- `backend/ee/onyx/db/license.py`
- `backend/ee/onyx/server/gateway/openai_passthrough.py`
- `backend/ee/onyx/server/tenants/provisioning.py`
- `backend/model_server/encoders.py`
- `backend/onyx/auth/mobile_sso/code_store.py`

## Security questions
- Which data is converted into embeddings?
- Can embeddings represent sensitive information?
- Which embedding model/version generated each vector?
- How are tenant/user authorization constraints represented?
- Are authorization filters applied before returning vector results?
- Can metadata filters be attacker-controlled or omitted?
- How are vectors deleted after source access is revoked?
- Can poisoned content enter the vector index?
- Can one tenant query another tenant's vectors?

## Security interpretation

Static matches identify code/configuration that requires security reasoning.

They do not prove authorization correctness, tenant isolation, retrieval safety, memory isolation or runtime exploitability.

## Safety
- No embedding generated.
- No vector database contacted.
- No document ingested.
- No retrieval query executed.
- No reranker executed.
- No model invoked.
- No external AI API contacted.
- No real user data used.
- No real credential used.
- No paid service used.

## Result

Action 5.5 static foundation result: **PASS**
