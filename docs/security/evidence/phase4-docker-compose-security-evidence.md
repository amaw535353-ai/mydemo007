# Phase 4 Action 4.3 - Docker & Compose Security Foundations Evidence

## Provenance

- Branch: `security/phase-4-cloud-devsecops`
- Baseline HEAD: `9d99fff3c026a0faecd5314db2614a81dcab5de2`

## Observation class

**STATIC SOURCE CANDIDATES ONLY. RUNTIME/DEPLOYMENT BEHAVIOR IS UNVERIFIED.**

## Review scope

Docker and Compose configuration, services, networks, environment variables, volumes, ports, health checks, dependency relationships, restart behavior and container-level configuration.

## Static observations

- Candidate files: **373**
- Matching lines: **1553**

## Representative candidate files

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
- `backend/alembic/versions/20f09b642ed0_backfill_write_chat_for_limited_service_.py`
- `backend/alembic/versions/213fd978c6d8_notifications.py`
- `backend/alembic/versions/2664261bfaab_add_cache_store_table.py`
- `backend/alembic/versions/2666d766cb9b_google_oauth2.py`
- `backend/alembic/versions/27c6ecc08586_permission_framework.py`
- `backend/alembic/versions/2d2304e27d8c_add_above_below_to_persona.py`
- `backend/alembic/versions/30c1d5744104_persona_datetime_aware.py`
- `backend/alembic/versions/325975216eb3_add_icon_color_and_icon_shape_to_persona.py`
- `backend/alembic/versions/351faebd379d_add_curator_fields.py`
- `backend/alembic/versions/369644546676_add_composite_index_for_index_attempt_.py`

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

Action 4.3 static mapping result: **PASS**
