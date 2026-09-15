# Phase 5 Action 5.6 - RAG, Retrieval & Reranking Foundations Evidence

## Provenance
- Branch: `security/phase-5-ai-foundations`
- Baseline HEAD: `c62d822d00e191fde9349eac5d18b4ee8ae91705`

## Observation boundary

**STATIC SOURCE CANDIDATES ONLY. AI RUNTIME BEHAVIOR IS UNVERIFIED.**

## Review scope

RAG ingestion and retrieval paths, document chunking, retrieval queries, ranking and reranking, source metadata, citations, authorization propagation and untrusted retrieved-content boundaries.

## Static observations
- Candidate files: **1250**
- Matching lines: **8827**

## Representative candidate files

- `AGENTS.md`
- `backend/AGENTS.md`
- `backend/alembic/versions/12635f6655b7_drive_canonical_ids.py`
- `backend/alembic/versions/19c0ccb01687_migrate_to_contextual_rag_model.py`
- `backend/alembic/versions/1f60f60c3401_embedding_model_search_settings.py`
- `backend/alembic/versions/1fc2904131a3_add_sso_provider_table_and_seed_from_env.py`
- `backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py`
- `backend/alembic/versions/23957775e5f5_remove_feedback_foreignkey_constraint.py`
- `backend/alembic/versions/28429dd43807_scheduled_tasks.py`
- `backend/alembic/versions/3a78dba1080a_user_file_legacy_data_cleanup.py`
- `backend/alembic/versions/495cb26ce93e_create_knowlege_graph_tables.py`
- `backend/alembic/versions/4ff2545411ad_contextual_rag_model_configuration_fk.py`
- `backend/alembic/versions/50b683a8295c_add_additional_retrieval_controls_to_.py`
- `backend/alembic/versions/5e6f7a8b9c0d_update_default_persona_prompt.py`
- `backend/alembic/versions/73e9983e5091_add_search_query_table.py`
- `backend/alembic/versions/77d07dffae64_forcibly_remove_more_enum_types_from_.py`
- `backend/alembic/versions/78ebc66946a0_remove_reranking_from_search_settings.py`
- `backend/alembic/versions/7f5b159041be_skill_built_in_id_discriminator.py`
- `backend/alembic/versions/81c22b1e2e78_hierarchy_nodes_v1.py`
- `backend/alembic/versions/8818cf73fa1a_drop_include_citations.py`

## Security questions
- Is authorization checked before retrieval results enter model context?
- Are document ACLs preserved through chunking and indexing?
- What happens when a user's source access is revoked?
- Can stale chunks remain retrievable?
- Can retrieved documents contain malicious instructions?
- Is retrieved content treated as data rather than trusted instruction?
- Can an attacker poison ingestion or retrieval sources?
- Can top-k, filters or reranking change authorization outcomes?
- Can citations prove which sources influenced an answer?

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

Action 5.6 static foundation result: **PASS**
