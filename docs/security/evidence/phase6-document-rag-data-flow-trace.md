# Phase 6 Action 6.6 - Document and RAG Data-Flow Trace
## Purpose
Trace the document and retrieval-augmented-generation data path through the
exact pinned Onyx source revision.
Target model:
connector or upload -> fetch -> processing -> chunking -> embedding ->
indexing -> access/tenant metadata -> search/retrieval -> access filtering ->
reranking -> AI context assembly.
This is a static source trace only.
## Verified Baseline
- Evidence branch: `security/phase-6-onyx-baseline`
- Action 6.5 parent: `44846498a050f676025a259e5ebdd02502c0015e`
- Onyx repository: `https://github.com/onyx-dot-app/onyx.git`
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx source clean: PASS
## RAG-Relevant Source Inventory
Captured paths: 502
```text
backend/ee/onyx/access/access.py
backend/ee/onyx/access/hierarchy_access.py
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
backend/ee/onyx/background/task_name_builders.py
backend/ee/onyx/connectors/capability_applicability.py
backend/ee/onyx/connectors/capability_checks.py
backend/ee/onyx/connectors/perm_sync_valid.py
backend/ee/onyx/document_index/vespa/app_config/cloud-services.xml.jinja
backend/ee/onyx/search/process_search_query.py
backend/ee/onyx/server/documents/cc_pair.py
backend/ee/onyx/server/query_and_chat/__init__.py
backend/ee/onyx/server/query_and_chat/models.py
backend/ee/onyx/server/query_and_chat/query_backend.py
backend/ee/onyx/server/query_and_chat/search_backend.py
backend/ee/onyx/server/query_and_chat/streaming_models.py
backend/ee/onyx/server/query_and_chat/token_limit.py
backend/onyx/access/__init__.py
backend/onyx/access/access.py
backend/onyx/access/hierarchy_access.py
backend/onyx/access/models.py
backend/onyx/access/utils.py
backend/onyx/background/README.md
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
backend/onyx/background/error_logging.py
backend/onyx/background/indexing/checkpointing_utils.py
backend/onyx/background/indexing/dask_utils.py
backend/onyx/background/indexing/index_attempt_utils.py
backend/onyx/background/indexing/job_client.py
backend/onyx/background/indexing/memory_tracer.py
backend/onyx/background/indexing/models.py
backend/onyx/background/indexing/run_docfetching.py
backend/onyx/background/indexing/run_targeted_reindex.py
backend/onyx/background/periodic_poller.py
backend/onyx/background/task_utils.py
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
backend/onyx/connectors/loopio/__init__.py
backend/onyx/connectors/loopio/connector.py
backend/onyx/connectors/lumapps/__init__.py
backend/onyx/connectors/lumapps/client.py
backend/onyx/connectors/lumapps/connector.py
backend/onyx/connectors/lumapps/models.py
backend/onyx/connectors/lumapps/utils.py
backend/onyx/connectors/mediawiki/__init__.py
backend/onyx/connectors/mediawiki/family.py
backend/onyx/connectors/mediawiki/wiki.py
backend/onyx/connectors/microsoft_utils/__init__.py
backend/onyx/connectors/microsoft_utils/drive_items.py
backend/onyx/connectors/microsoft_utils/graph_auth.py
backend/onyx/connectors/microsoft_utils/graph_client.py
backend/onyx/connectors/microsoft_utils/graph_env.py
backend/onyx/connectors/mock_connector/connector.py
backend/onyx/connectors/models.py
backend/onyx/connectors/notion/__init__.py
backend/onyx/connectors/notion/connector.py
backend/onyx/connectors/outline/__init__.py
backend/onyx/connectors/outline/client.py
backend/onyx/connectors/outline/connector.py
backend/onyx/connectors/productboard/__init__.py
backend/onyx/connectors/productboard/connector.py
backend/onyx/connectors/registry.py
backend/onyx/connectors/salesforce/OAUTH.md
backend/onyx/connectors/salesforce/__init__.py
backend/onyx/connectors/salesforce/auth.py
backend/onyx/connectors/salesforce/blacklist.py
backend/onyx/connectors/salesforce/connector.py
backend/onyx/connectors/salesforce/doc_conversion.py
backend/onyx/connectors/salesforce/models.py
backend/onyx/connectors/salesforce/onyx_salesforce.py
backend/onyx/connectors/salesforce/salesforce_calls.py
backend/onyx/connectors/salesforce/shelve_stuff/old_test_salesforce_shelves.py
backend/onyx/connectors/salesforce/shelve_stuff/shelve_functions.py
backend/onyx/connectors/salesforce/shelve_stuff/shelve_utils.py
backend/onyx/connectors/salesforce/shelve_stuff/test_salesforce_shelves.py
backend/onyx/connectors/salesforce/sqlite_functions.py
backend/onyx/connectors/salesforce/utils.py
backend/onyx/connectors/sharepoint/__init__.py
backend/onyx/connectors/sharepoint/connector.py
backend/onyx/connectors/sharepoint/connector_utils.py
backend/onyx/connectors/slab/__init__.py
backend/onyx/connectors/slab/connector.py
backend/onyx/connectors/slack/__init__.py
backend/onyx/connectors/slack/access.py
backend/onyx/connectors/slack/capability_checks.py
backend/onyx/connectors/slack/connector.py
backend/onyx/connectors/slack/models.py
backend/onyx/connectors/slack/source_operations.py
backend/onyx/connectors/slack/utils.py
backend/onyx/connectors/source_operations.py
backend/onyx/connectors/teams/__init__.py
backend/onyx/connectors/teams/connector.py
backend/onyx/connectors/teams/models.py
backend/onyx/connectors/teams/utils.py
backend/onyx/connectors/testrail/__init__.py
backend/onyx/connectors/testrail/connector.py
backend/onyx/connectors/web/__init__.py
backend/onyx/connectors/web/connector.py
backend/onyx/connectors/wikipedia/__init__.py
backend/onyx/connectors/wikipedia/connector.py
backend/onyx/connectors/xenforo/__init__.py
backend/onyx/connectors/xenforo/connector.py
backend/onyx/connectors/zendesk/__init__.py
backend/onyx/connectors/zendesk/connector.py
backend/onyx/connectors/zoom/client.py
backend/onyx/connectors/zoom/connector.py
backend/onyx/connectors/zoom/models.py
backend/onyx/connectors/zoom/recordings/discovery.py
backend/onyx/connectors/zoom/recordings/models.py
backend/onyx/connectors/zoom/recordings/processing.py
backend/onyx/connectors/zoom/recordings/session_types.py
backend/onyx/connectors/zoom/recordings/vtt.py
backend/onyx/connectors/zulip/__init__.py
backend/onyx/connectors/zulip/connector.py
backend/onyx/connectors/zulip/schemas.py
backend/onyx/connectors/zulip/utils.py
backend/onyx/document_index/FILTER_SEMANTICS.md
backend/onyx/document_index/__init__.py
backend/onyx/document_index/chunk_content_enrichment.py
backend/onyx/document_index/disabled.py
backend/onyx/document_index/document_index_utils.py
backend/onyx/document_index/document_metadata.py
backend/onyx/document_index/factory.py
backend/onyx/document_index/interfaces_new.py
backend/onyx/document_index/opensearch/README.md
backend/onyx/document_index/opensearch/client.py
backend/onyx/document_index/opensearch/cluster_settings.py
backend/onyx/document_index/opensearch/constants.py
backend/onyx/document_index/opensearch/index_reclaim.py
backend/onyx/document_index/opensearch/opensearch_document_index.py
backend/onyx/document_index/opensearch/port_copy.py
backend/onyx/document_index/opensearch/schema.py
backend/onyx/document_index/opensearch/search.py
backend/onyx/document_index/opensearch/string_filtering.py
backend/onyx/document_index/vespa/__init__.py
backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja
backend/onyx/document_index/vespa/app_config/services.xml.jinja
backend/onyx/document_index/vespa/app_config/validation-overrides.xml.jinja
backend/onyx/document_index/vespa/chunk_retrieval.py
backend/onyx/document_index/vespa/deletion.py
backend/onyx/document_index/vespa/indexing_utils.py
backend/onyx/document_index/vespa/internal_types.py
backend/onyx/document_index/vespa/kg_interactions.py
backend/onyx/document_index/vespa/shared_utils/utils.py
backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py
backend/onyx/document_index/vespa/vespa_document_index.py
backend/onyx/document_index/vespa_constants.py
backend/onyx/file_store/README.md
backend/onyx/file_store/azure_blob_file_store.py
backend/onyx/file_store/constants.py
backend/onyx/file_store/document_batch_storage.py
backend/onyx/file_store/file_store.py
backend/onyx/file_store/gcs_file_store.py
backend/onyx/file_store/models.py
backend/onyx/file_store/postgres_file_store.py
backend/onyx/file_store/s3_key_utils.py
backend/onyx/file_store/serving.py
backend/onyx/file_store/staging.py
backend/onyx/file_store/utils.py
backend/onyx/indexing/__init__.py
backend/onyx/indexing/adapters/document_indexing_adapter.py
backend/onyx/indexing/adapters/user_file_indexing_adapter.py
backend/onyx/indexing/chunk_batch_store.py
backend/onyx/indexing/chunker.py
backend/onyx/indexing/chunking/__init__.py
backend/onyx/indexing/chunking/document_chunker.py
backend/onyx/indexing/chunking/image_section_chunker.py
backend/onyx/indexing/chunking/section_chunker.py
backend/onyx/indexing/chunking/tabular_section_chunker/__init__.py
backend/onyx/indexing/chunking/tabular_section_chunker/analysis.py
backend/onyx/indexing/chunking/tabular_section_chunker/sheet_descriptor.py
backend/onyx/indexing/chunking/tabular_section_chunker/tabular_section_chunker.py
backend/onyx/indexing/chunking/tabular_section_chunker/total_descriptor.py
backend/onyx/indexing/chunking/tabular_section_chunker/util.py
backend/onyx/indexing/chunking/text_section_chunker.py
backend/onyx/indexing/content_classification.py
backend/onyx/indexing/document_push.py
backend/onyx/indexing/embedder.py
backend/onyx/indexing/indexing_heartbeat.py
backend/onyx/indexing/indexing_pipeline.py
backend/onyx/indexing/models.py
backend/onyx/indexing/persistent_indexing.py
backend/onyx/indexing/port_reembed.py
backend/onyx/indexing/vector_db_insertion.py
backend/onyx/llm/__init__.py
backend/onyx/llm/api_surfaces.py
backend/onyx/llm/constants.py
backend/onyx/llm/cost.py
backend/onyx/llm/cost_overrides.py
backend/onyx/llm/custom_config_mapping.py
backend/onyx/llm/exceptions.py
backend/onyx/llm/factory.py
backend/onyx/llm/interfaces.py
backend/onyx/llm/litellm_singleton/__init__.py
backend/onyx/llm/litellm_singleton/config.py
backend/onyx/llm/litellm_singleton/monkey_patches.py
backend/onyx/llm/model_capabilities.py
backend/onyx/llm/model_metadata_enrichments.json
backend/onyx/llm/model_name_parser.py
backend/onyx/llm/model_response.py
backend/onyx/llm/models.py
backend/onyx/llm/multi_llm.py
backend/onyx/llm/override_models.py
backend/onyx/llm/prompt_cache/README.md
backend/onyx/llm/prompt_cache/__init__.py
backend/onyx/llm/prompt_cache/cache_manager.py
backend/onyx/llm/prompt_cache/models.py
backend/onyx/llm/prompt_cache/processor.py
backend/onyx/llm/prompt_cache/providers/__init__.py
backend/onyx/llm/prompt_cache/providers/anthropic.py
backend/onyx/llm/prompt_cache/providers/base.py
backend/onyx/llm/prompt_cache/providers/factory.py
backend/onyx/llm/prompt_cache/providers/noop.py
backend/onyx/llm/prompt_cache/providers/openai.py
backend/onyx/llm/prompt_cache/providers/vertex.py
backend/onyx/llm/prompt_cache/utils.py
backend/onyx/llm/request_context.py
backend/onyx/llm/tracing_wrap.py
backend/onyx/llm/utils.py
backend/onyx/llm/well_known_providers/auto_update_models.py
backend/onyx/llm/well_known_providers/auto_update_service.py
backend/onyx/llm/well_known_providers/constants.py
backend/onyx/llm/well_known_providers/llm_provider_options.py
backend/onyx/llm/well_known_providers/models.py
backend/onyx/llm/well_known_providers/recommended-models.json
backend/onyx/prompts/__init__.py
backend/onyx/prompts/basic_memory.py
backend/onyx/prompts/chat_prompts.py
backend/onyx/prompts/chat_tools.py
backend/onyx/prompts/coding_agent/__init__.py
backend/onyx/prompts/coding_agent/coding_agent.py
backend/onyx/prompts/compression_prompts.py
backend/onyx/prompts/constants.py
backend/onyx/prompts/contextual_retrieval.py
backend/onyx/prompts/deep_research/__init__.py
backend/onyx/prompts/deep_research/dr_tool_prompts.py
backend/onyx/prompts/deep_research/orchestration_layer.py
backend/onyx/prompts/deep_research/research_agent.py
backend/onyx/prompts/federated_search.py
backend/onyx/prompts/filter_extration.py
backend/onyx/prompts/image_analysis.py
backend/onyx/prompts/kg_prompts.py
backend/onyx/prompts/prompt_template.py
backend/onyx/prompts/prompt_utils.py
backend/onyx/prompts/search_prompts.py
backend/onyx/prompts/tool_prompts.py
backend/onyx/prompts/user_info.py
backend/onyx/server/documents/__init__.py
backend/onyx/server/documents/cc_pair.py
backend/onyx/server/documents/connector.py
backend/onyx/server/documents/credential.py
backend/onyx/server/documents/credential_capabilities.py
backend/onyx/server/documents/document.py
backend/onyx/server/documents/document_utils.py
backend/onyx/server/documents/models.py
backend/onyx/server/documents/private_key_types.py
backend/onyx/server/documents/standard_oauth.py
backend/onyx/server/documents/targeted_reindex.py
backend/onyx/server/query_and_chat/__init__.py
backend/onyx/server/query_and_chat/chat_backend.py
backend/onyx/server/query_and_chat/chat_utils.py
backend/onyx/server/query_and_chat/models.py
backend/onyx/server/query_and_chat/placement.py
backend/onyx/server/query_and_chat/query_backend.py
backend/onyx/server/query_and_chat/session_loading.py
backend/onyx/server/query_and_chat/streaming_models.py
backend/onyx/server/query_and_chat/token_limit.py
```
## Connector Document Acquisition
Evidence lines: 500
```text
HEAD:backend/ee/onyx/access/access.py:8:    fetch_user_groups_for_documents,
HEAD:backend/ee/onyx/access/access.py:27:def _get_access_for_document(
HEAD:backend/ee/onyx/access/access.py:54:        for document_id, group_names in fetch_user_groups_for_documents(
HEAD:backend/ee/onyx/access/access.py:100:        # If the document is determined to be "public" externally (through a SYNC connector)
HEAD:backend/ee/onyx/access/access.py:111:        # To avoid collisions of group namings between connectors, they need to be prefixed
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:158:        # to ~10k+ inactive tenants. A small number of cleanup tasks (connector deletion,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:22:from ee.onyx.db.connector_credential_pair import get_all_auto_sync_cc_pairs
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:49:from onyx.connectors.factory import validate_ccpair_for_user
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:50:from onyx.db.connector import mark_cc_pair_as_permissions_synced
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:51:from onyx.db.connector_credential_pair import get_connector_credential_pair_from_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:53:    get_document_ids_for_connector_credential_pair,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:54:    get_documents_for_connector_credential_pair_limited_columns,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:55:    upsert_document_by_connector_credential_pair,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:64:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:71:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:82:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:83:from onyx.redis.redis_connector_doc_perm_sync import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:84:    RedisConnectorPermissionSync,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:85:    RedisConnectorPermissionSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:163:def _is_external_doc_permissions_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:170:    if cc_pair.status != ConnectorCredentialPairStatus.ACTIVE:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:173:    sync_config = get_source_perm_sync_config(cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:175:        logger.error("No sync config found for %s", cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:179:        logger.error("No doc sync config found for %s", cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:221:        OnyxRedisLocks.CHECK_CONNECTOR_DOC_PERMISSIONS_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:292:            if key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:329:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:341:        if redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:344:        if redis_connector.delete.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:347:        if redis_connector.prune.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:350:        redis_connector.permissions.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:351:        redis_connector.permissions.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:353:        custom_task_id = f"{redis_connector.permissions.generator_task_key}_{uuid4()}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:368:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:369:        payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:375:        redis_connector.permissions.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:378:            OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:383:            queue=OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:390:        redis_connector.permissions.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:410:    name=OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:417:def connector_permission_sync_generator_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:423:    Permission sync task that handles document permission syncing for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:438:            connector_credential_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:445:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:456:                f"connector_permission_sync_generator_task - timed out waiting for fence to be ready: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:457:                f"fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:462:        if not redis_connector.permissions.fenced:  # The fence must exist
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:463:            error_msg = f"connector_permission_sync_generator_task - fence not found: fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:467:        payload = redis_connector.permissions.payload  # The payload must exist
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:470:                "connector_permission_sync_generator_task: payload invalid or not found"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:477:                "connector_permission_sync_generator_task - Waiting for fence: fence=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:478:                redis_connector.permissions.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:486:            "connector_permission_sync_generator_task - Fence found, continuing...: fence=%s payload_id=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:487:            redis_connector.permissions.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:493:        OnyxRedisLocks.CONNECTOR_DOC_PERMISSIONS_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:494:        + f"_{redis_connector.cc_pair_id}",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:509:    connector_type: str = "unknown"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:517:            cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:520:                eager_load_connector=True,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:521:                eager_load_credential=True,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:525:                    f"No connector credential pair found for id: {cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:530:                    cc_pair.connector.id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:531:                    cc_pair.credential.id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:539:                        f"Unable to create connector credential pair for id: {cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:548:            source_type = cc_pair.connector.source
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:549:            connector_type = source_type.value
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:571:            payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:575:            new_payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:581:            redis_connector.permissions.set_fence(new_payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:584:                redis_connector, lock, r, timeout_seconds=JOB_TIMEOUT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:587:            connector_id = cc_pair.connector.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:588:            credential_id = cc_pair.credential.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:590:        # lets each connector decide which existing docs are now missing and should
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:597:                    get_documents_for_connector_credential_pair_limited_columns(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:599:                        connector_id=connector_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:600:                        credential_id=credential_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:607:                return get_document_ids_for_connector_credential_pair(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:609:                    connector_id=connector_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:610:                    credential_id=credential_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:613:        # cc_pair is detached: connectors may read eager-loaded connector/credential
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:624:            f"RedisConnector.permissions.generate_tasks starting. cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:635:            result = redis_connector.permissions.update_db(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:638:                source_string=connector_type,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:639:                connector_id=connector_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:640:                credential_id=credential_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:647:            f"RedisConnector.permissions.generate_tasks finished. "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:651:        inc_doc_perm_sync_docs_processed(connector_type, tasks_generated)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:653:            inc_doc_perm_sync_errors(connector_type, docs_with_errors)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:666:        redis_connector.permissions.generator_complete = tasks_generated
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:687:        redis_connector.permissions.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:688:        redis_connector.permissions.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:689:        redis_connector.permissions.set_fence(None)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:692:        observe_doc_perm_sync_duration(time.monotonic() - sync_start, connector_type)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:713:    connector_id: int,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:714:    credential_id: int,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:748:                    upsert_document_by_connector_credential_pair(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:750:                        connector_id=connector_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:751:                        credential_id=credential_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:779:            f"element_update_permissions exceptioned: {element_type}={element_id}, {connector_id=} {credential_id=}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:784:            f"element_update_permissions completed: {element_type}={element_id}, {connector_id=} {credential_id=}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:811:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:820:        if not key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:873:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:882:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:885:    if not redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:892:        payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:901:        redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:915:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:920:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:925:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:943:    for member in r.sscan_iter(redis_connector.permissions.taskset_key):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:961:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:965:    # if redis_connector_index.generator_locked():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:972:    if redis_connector.permissions.active():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:984:    redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:993:        redis_connector: RedisConnector,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:999:        self.redis_connector: RedisConnector = redis_connector
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1013:        if self.redis_connector.stop.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1026:                    self.redis_connector.cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1034:            self.redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1069:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1078:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1079:    if not redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1082:    initial = redis_connector.permissions.generator_complete
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1087:        payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1097:    remaining = redis_connector.permissions.get_remaining()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1136:    redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:6:from onyx.db.connector import mark_cc_pair_as_external_group_synced
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:7:from onyx.db.connector_credential_pair import get_connector_credential_pairs_for_source
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:8:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:12:    db_session: Session, cc_pair: ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:14:    if not source_group_sync_is_cc_pair_agnostic(cc_pair.connector.source):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:17:    cc_pairs = get_connector_credential_pairs_for_source(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:18:        db_session, cc_pair.connector.source
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:24:    db_session: Session, cc_pair: ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:16:from ee.onyx.db.connector_credential_pair import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:50:from onyx.db.connector_credential_pair import get_connector_credential_pair_from_id
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:54:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:58:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:66:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:67:from onyx.redis.redis_connector_ext_group_sync import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:68:    RedisConnectorExternalGroupSync,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:69:    RedisConnectorExternalGroupSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:118:def _is_external_group_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:127:    if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:133:    sync_config = get_source_perm_sync_config(cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:136:            f"Skipping group sync for CC Pair {cc_pair.id} - no sync config found for {cc_pair.connector.source}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:140:    # If there is not group sync function for the connector, we don't run the sync
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:144:            f"Skipping group sync for CC Pair {cc_pair.id} - no group sync config found for {cc_pair.connector.source}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:176:        OnyxRedisLocks.CHECK_CONNECTOR_EXTERNAL_GROUP_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:199:                    status=ConnectorCredentialPairStatus.ACTIVE,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:281:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:285:        if redis_connector.external_group_sync.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:292:        redis_connector.external_group_sync.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:293:        redis_connector.external_group_sync.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:308:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:310:        payload = RedisConnectorExternalGroupSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:316:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:318:        custom_task_id = f"{redis_connector.external_group_sync.taskset_key}_{uuid4()}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:321:            OnyxCeleryTask.CONNECTOR_EXTERNAL_GROUP_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:326:            queue=OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:332:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:352:    name=OnyxCeleryTask.CONNECTOR_EXTERNAL_GROUP_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:359:def connector_external_group_sync_generator_task(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:365:    External group sync task for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:369:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:380:                f"connector_external_group_sync_generator_task - timed out waiting for fence to be ready: "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:381:                f"fence={redis_connector.external_group_sync.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:386:        if not redis_connector.external_group_sync.fenced:  # The fence must exist
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:388:                f"connector_external_group_sync_generator_task - fence not found: "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:389:                f"fence={redis_connector.external_group_sync.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:394:        payload = redis_connector.external_group_sync.payload  # The payload must exist
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:396:            msg = "connector_external_group_sync_generator_task: payload invalid or not found"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:402:                "connector_external_group_sync_generator_task - Waiting for fence: fence=%s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:403:                redis_connector.external_group_sync.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:409:            "connector_external_group_sync_generator_task - Fence found, continuing...: fence=%s payload_id=%s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:410:            redis_connector.external_group_sync.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:416:        OnyxRedisLocks.CONNECTOR_EXTERNAL_GROUP_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:417:        + f"_{redis_connector.cc_pair_id}",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:430:        redis_connector.external_group_sync.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:465:        redis_connector.external_group_sync.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:466:        redis_connector.external_group_sync.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:470:        redis_connector.external_group_sync.set_fence(None)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:485:    connector_type: str = "unknown"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:489:            connector_credential_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:499:        connector_type = _timed_perform_external_group_sync(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:506:        observe_group_sync_duration(time.monotonic() - sync_start, connector_type)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:516:        cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:519:            eager_load_credential=True,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:522:            raise ValueError(f"No connector credential pair found for id: {cc_pair_id}")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:524:        source_type = cc_pair.connector.source
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:525:        connector_type = source_type.value
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:606:                        source=cc_pair.connector.source,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:618:                    source=cc_pair.connector.source,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:633:            inc_group_sync_errors(connector_type)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:642:        observe_group_sync_upsert_duration(cumulative_upsert_time, connector_type)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:671:        inc_group_sync_groups_processed(connector_type, total_groups_processed)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:672:        inc_group_sync_users_processed(connector_type, total_users_processed)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:676:    return connector_type
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:688:        OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:697:        if not key_str.startswith(RedisConnectorExternalGroupSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:742:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:754:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:757:    if not redis_connector.external_group_sync.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:761:        payload = redis_connector.external_group_sync.payload
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:772:        redis_connector.external_group_sync.reset()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:783:        payload.celery_task_id, OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:787:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:792:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:799:    if redis_connector.external_group_sync.active():
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:814:    redis_connector.external_group_sync.reset()
HEAD:backend/ee/onyx/connectors/capability_applicability.py:4:resolution never depends on per-connector check modules: a broken or heavy check
HEAD:backend/ee/onyx/connectors/capability_applicability.py:15:from onyx.connectors.capabilities import CredentialCapability
HEAD:backend/ee/onyx/connectors/capability_applicability.py:20:) -> set[CredentialCapability]:
HEAD:backend/ee/onyx/connectors/capability_applicability.py:22:    applicable: set[CredentialCapability] = set()
HEAD:backend/ee/onyx/connectors/capability_applicability.py:24:        applicable.add(CredentialCapability.DOC_PERMISSION_SYNC)
HEAD:backend/ee/onyx/connectors/capability_applicability.py:26:        applicable.add(CredentialCapability.EXTERNAL_GROUP_SYNC)
HEAD:backend/ee/onyx/connectors/capability_checks.py:3:Fetched by ``onyx.connectors.capability_checks.registry`` via
HEAD:backend/ee/onyx/connectors/capability_checks.py:5:implementations stay in the OSS connector modules, mirroring the
HEAD:backend/ee/onyx/connectors/capability_checks.py:9:from ee.onyx.connectors.capability_applicability import (
HEAD:backend/ee/onyx/connectors/capability_checks.py:12:from ee.onyx.connectors.perm_sync_valid import source_has_perm_sync_probe
HEAD:backend/ee/onyx/connectors/capability_checks.py:14:from onyx.connectors.capability_checks.models import (
HEAD:backend/ee/onyx/connectors/capability_checks.py:17:    CredentialCapability,
HEAD:backend/ee/onyx/connectors/capability_checks.py:19:from onyx.connectors.slack.capability_checks import (
HEAD:backend/ee/onyx/connectors/capability_checks.py:22:from onyx.connectors.source_operations import get_source_operations_class
HEAD:backend/ee/onyx/connectors/capability_checks.py:24:# Named perm-sync checks per source. Per-connector work registers named checks
HEAD:backend/ee/onyx/connectors/capability_checks.py:48:        self, source: DocumentSource, capability: CredentialCapability
HEAD:backend/ee/onyx/connectors/capability_checks.py:58:        assert context.connector is not None, (
HEAD:backend/ee/onyx/connectors/capability_checks.py:59:            "The runner guarantees an instance of a connector."
HEAD:backend/ee/onyx/connectors/capability_checks.py:61:        context.connector.validate_perm_sync()
HEAD:backend/ee/onyx/connectors/capability_checks.py:80:    registered_by_capability: dict[CredentialCapability, list[CapabilityCheck]] = {
HEAD:backend/ee/onyx/connectors/capability_checks.py:81:        CredentialCapability.DOC_PERMISSION_SYNC: (
HEAD:backend/ee/onyx/connectors/capability_checks.py:84:        CredentialCapability.EXTERNAL_GROUP_SYNC: (
HEAD:backend/ee/onyx/connectors/capability_checks.py:93:        "source-operations gateway; migrate the connector first."
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:5:from onyx.connectors.box.connector import BoxConnector
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:6:from onyx.connectors.canvas.connector import CanvasConnector
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:7:from onyx.connectors.confluence.connector import ConfluenceConnector
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:8:from onyx.connectors.factory import identify_connector_class
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:9:from onyx.connectors.google_drive.connector import GoogleDriveConnector
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:10:from onyx.connectors.interfaces import BaseConnector
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:11:from onyx.connectors.sharepoint.connector import SharepointConnector
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:14:def validate_canvas_perm_sync(connector: CanvasConnector) -> None:
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:15:    connector.probe_course_user_email_visibility()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:16:    connector.probe_account_user_listing_permission()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:19:def validate_confluence_perm_sync(connector: ConfluenceConnector) -> None:
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:21:    Validate that the connector is configured correctly for permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:26:    misconfiguration surfaces at connector creation time -- with an
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:30:    connector.probe_rest_space_permissions_admin_access()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:33:def validate_drive_perm_sync(connector: GoogleDriveConnector) -> None:
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:35:    Validate that the connector is configured correctly for permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:39:    connector creation instead of every external-group-sync tick.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:41:    connector.probe_directory_admin_permission()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:44:def validate_box_perm_sync(connector: BoxConnector) -> None:
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:48:    groups' / 'Manage users' scopes fails at connector creation instead of
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:51:    connector.probe_group_listing_permission()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:54:def validate_sharepoint_perm_sync(connector: SharepointConnector) -> None:
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:56:    Validate that the connector is configured correctly for permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:63:    Probe both here so misconfigured apps fail fast at connector creation
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:66:    connector.probe_role_assignments_permission()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:67:    connector.probe_group_members_permission()
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:70:# The single source of truth for which connectors carry a real perm-sync probe:
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:73:# ``source_has_perm_sync_probe``. Values take the matching connector subclass;
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:75:_VALIDATOR_BY_CONNECTOR_CLASS: dict[type[BaseConnector], Callable[[Any], None]] = {
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:76:    BoxConnector: validate_box_perm_sync,
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:77:    CanvasConnector: validate_canvas_perm_sync,
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:78:    ConfluenceConnector: validate_confluence_perm_sync,
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:79:    GoogleDriveConnector: validate_drive_perm_sync,
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:80:    SharepointConnector: validate_sharepoint_perm_sync,
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:84:def validate_perm_sync(connector: BaseConnector) -> None:
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:86:    Override this if your connector needs to validate permissions syncing.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:91:    for connector_class, validator in _VALIDATOR_BY_CONNECTOR_CLASS.items():
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:92:        if isinstance(connector, connector_class):
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:93:            validator(connector)
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:101:    Mirrors the isinstance dispatch above (``issubclass``, so a connector class
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:103:    sources with a connector class; callers gate on sync-capability first.
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:105:    connector_class = identify_connector_class(source)
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:107:        issubclass(connector_class, probe_class)
HEAD:backend/ee/onyx/connectors/perm_sync_valid.py:108:        for probe_class in _VALIDATOR_BY_CONNECTOR_CLASS
HEAD:backend/ee/onyx/db/connector.py:5:from onyx.db.models import Connector
HEAD:backend/ee/onyx/db/connector.py:11:def fetch_sources_with_connectors(db_session: Session) -> list[DocumentSource]:
HEAD:backend/ee/onyx/db/connector.py:12:    sources = db_session.query(distinct(Connector.source)).all()
HEAD:backend/ee/onyx/db/connector_credential_pair.py:5:from onyx.db.connector_credential_pair import get_connector_credential_pair
HEAD:backend/ee/onyx/db/connector_credential_pair.py:6:from onyx.db.enums import AccessType, ConnectorCredentialPairStatus
HEAD:backend/ee/onyx/db/connector_credential_pair.py:8:    Connector,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:9:    ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:10:    UserGroup__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:17:def _delete_connector_credential_pair_user_groups_relationship__no_commit(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:18:    db_session: Session, connector_id: int, credential_id: int
HEAD:backend/ee/onyx/db/connector_credential_pair.py:20:    cc_pair = get_connector_credential_pair(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:22:        connector_id=connector_id,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:23:        credential_id=credential_id,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:27:            f"ConnectorCredentialPair with connector_id: {connector_id} and credential_id: {credential_id} not found"
HEAD:backend/ee/onyx/db/connector_credential_pair.py:30:    stmt = delete(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:31:        UserGroup__ConnectorCredentialPair.cc_pair_id == cc_pair.id,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:40:    status: ConnectorCredentialPairStatus | None = None,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:41:) -> list[ConnectorCredentialPair]:
HEAD:backend/ee/onyx/db/connector_credential_pair.py:47:        db_session.query(ConnectorCredentialPair)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:48:        .join(ConnectorCredentialPair.connector)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:49:        .filter(Connector.source == source_type)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:50:        .order_by(ConnectorCredentialPair.id)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:54:        query = query.filter(ConnectorCredentialPair.access_type == access_type)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:57:        query = query.filter(ConnectorCredentialPair.status == status)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:65:) -> list[ConnectorCredentialPair]:
HEAD:backend/ee/onyx/db/connector_credential_pair.py:67:        db_session.query(ConnectorCredentialPair)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:69:            ConnectorCredentialPair.access_type == AccessType.SYNC,
HEAD:backend/ee/onyx/db/document.py:37:        document = DbDocument(
HEAD:backend/ee/onyx/db/document.py:79:        document = DbDocument(
HEAD:backend/ee/onyx/db/document_set.py:10:    ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/document_set.py:12:    DocumentSet__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/document_set.py:59:    off that. Re-applies update_document_set's constraint that a private set's connectors
HEAD:backend/ee/onyx/db/document_set.py:105:                    DocumentSet__ConnectorCredentialPair.connector_credential_pair_id
HEAD:backend/ee/onyx/db/document_set.py:107:                    DocumentSet__ConnectorCredentialPair.document_set_id.in_(
HEAD:backend/ee/onyx/db/document_set.py:110:                    DocumentSet__ConnectorCredentialPair.is_current.is_(True),
HEAD:backend/ee/onyx/db/document_set.py:148:def fetch_document_sets(
HEAD:backend/ee/onyx/db/document_set.py:152:) -> list[tuple[DocumentSet, list[ConnectorCredentialPair]]]:
HEAD:backend/ee/onyx/db/document_set.py:197:        tuple[DocumentSet, list[ConnectorCredentialPair]]
HEAD:backend/ee/onyx/db/document_set.py:201:        # Fetch the associated ConnectorCredentialPairs
HEAD:backend/ee/onyx/db/document_set.py:203:            db_session.query(ConnectorCredentialPair)
HEAD:backend/ee/onyx/db/document_set.py:205:                DocumentSet__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/document_set.py:206:                ConnectorCredentialPair.id
HEAD:backend/ee/onyx/db/document_set.py:207:                == DocumentSet__ConnectorCredentialPair.connector_credential_pair_id,
HEAD:backend/ee/onyx/db/document_set.py:210:                DocumentSet__ConnectorCredentialPair.document_set_id == document_set.id,
HEAD:backend/ee/onyx/db/hierarchy.py:1:"""EE hierarchy access control for source and connector permissions."""
HEAD:backend/ee/onyx/db/hierarchy.py:11:from onyx.db.connector_credential_pair import build_user_cc_pair_access_filter
HEAD:backend/ee/onyx/db/hierarchy.py:13:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/db/hierarchy.py:18:    ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/hierarchy.py:20:    HierarchyNodeByConnectorCredentialPair,
HEAD:backend/ee/onyx/db/hierarchy.py:24:def _build_connector_access_filter(user_id: UUID) -> ColumnElement[bool]:
HEAD:backend/ee/onyx/db/hierarchy.py:25:    """Grant the connector-level access applied to indexed documents."""
HEAD:backend/ee/onyx/db/hierarchy.py:26:    node_cc_pair = HierarchyNodeByConnectorCredentialPair
HEAD:backend/ee/onyx/db/hierarchy.py:27:    cc_pair = ConnectorCredentialPair
HEAD:backend/ee/onyx/db/hierarchy.py:35:                cc_pair.connector_id == node_cc_pair.connector_id,
HEAD:backend/ee/onyx/db/hierarchy.py:36:                cc_pair.credential_id == node_cc_pair.credential_id,
HEAD:backend/ee/onyx/db/hierarchy.py:41:            cc_pair.status != ConnectorCredentialPairStatus.DELETING,
HEAD:backend/ee/onyx/db/hierarchy.py:53:    """Grant access through the node ACL or an associated connector."""
HEAD:backend/ee/onyx/db/hierarchy.py:67:        access_filters.append(_build_connector_access_filter(user_id))
HEAD:backend/ee/onyx/db/user_group.py:24:from onyx.db.connector_credential_pair import (
HEAD:backend/ee/onyx/db/user_group.py:26:    get_connector_credential_pair_from_id,
HEAD:backend/ee/onyx/db/user_group.py:31:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/db/user_group.py:37:    ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:38:    Credential,
HEAD:backend/ee/onyx/db/user_group.py:39:    Credential__UserGroup,
HEAD:backend/ee/onyx/db/user_group.py:41:    DocumentByConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:44:    FederatedConnector__DocumentSet,
HEAD:backend/ee/onyx/db/user_group.py:55:    UserGroup__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:103:def _cleanup_credential__user_group_relationships__no_commit(
HEAD:backend/ee/onyx/db/user_group.py:108:    db_session.query(Credential__UserGroup).filter(
HEAD:backend/ee/onyx/db/user_group.py:109:        Credential__UserGroup.user_group_id == user_group_id
HEAD:backend/ee/onyx/db/user_group.py:185:    stmt = select(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/user_group.py:186:        UserGroup__ConnectorCredentialPair.user_group_id == user_group_id
HEAD:backend/ee/onyx/db/user_group.py:190:            UserGroup__ConnectorCredentialPair.is_current == False  # noqa: E712
HEAD:backend/ee/onyx/db/user_group.py:221:        .selectinload(UserGroup__ConnectorCredentialPair.cc_pair)
HEAD:backend/ee/onyx/db/user_group.py:223:            selectinload(ConnectorCredentialPair.connector),
HEAD:backend/ee/onyx/db/user_group.py:224:            selectinload(ConnectorCredentialPair.credential).selectinload(
HEAD:backend/ee/onyx/db/user_group.py:225:                Credential.user
HEAD:backend/ee/onyx/db/user_group.py:229:            selectinload(DocumentSet.connector_credential_pairs).selectinload(
HEAD:backend/ee/onyx/db/user_group.py:230:                ConnectorCredentialPair.connector
HEAD:backend/ee/onyx/db/user_group.py:234:            selectinload(DocumentSet.federated_connectors).selectinload(
HEAD:backend/ee/onyx/db/user_group.py:235:                FederatedConnector__DocumentSet.federated_connector
HEAD:backend/ee/onyx/db/user_group.py:246:                selectinload(DocumentSet.connector_credential_pairs).selectinload(
HEAD:backend/ee/onyx/db/user_group.py:247:                    ConnectorCredentialPair.connector
HEAD:backend/ee/onyx/db/user_group.py:251:                selectinload(DocumentSet.federated_connectors).selectinload(
HEAD:backend/ee/onyx/db/user_group.py:252:                    FederatedConnector__DocumentSet.federated_connector
HEAD:backend/ee/onyx/db/user_group.py:350:            DocumentByConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:351:            Document.id == DocumentByConnectorCredentialPair.id,
HEAD:backend/ee/onyx/db/user_group.py:354:            ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:356:                DocumentByConnectorCredentialPair.connector_id
HEAD:backend/ee/onyx/db/user_group.py:357:                == ConnectorCredentialPair.connector_id,
HEAD:backend/ee/onyx/db/user_group.py:358:                DocumentByConnectorCredentialPair.credential_id
HEAD:backend/ee/onyx/db/user_group.py:359:                == ConnectorCredentialPair.credential_id,
HEAD:backend/ee/onyx/db/user_group.py:363:            UserGroup__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:364:            UserGroup__ConnectorCredentialPair.cc_pair_id == ConnectorCredentialPair.id,
HEAD:backend/ee/onyx/db/user_group.py:368:            UserGroup__ConnectorCredentialPair.user_group_id == UserGroup.id,
HEAD:backend/ee/onyx/db/user_group.py:377:def fetch_documents_for_user_group_paginated(
HEAD:backend/ee/onyx/db/user_group.py:386:            DocumentByConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:387:            Document.id == DocumentByConnectorCredentialPair.id,
HEAD:backend/ee/onyx/db/user_group.py:390:            ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:392:                DocumentByConnectorCredentialPair.connector_id
HEAD:backend/ee/onyx/db/user_group.py:393:                == ConnectorCredentialPair.connector_id,
HEAD:backend/ee/onyx/db/user_group.py:394:                DocumentByConnectorCredentialPair.credential_id
HEAD:backend/ee/onyx/db/user_group.py:395:                == ConnectorCredentialPair.credential_id,
HEAD:backend/ee/onyx/db/user_group.py:399:            UserGroup__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:400:            UserGroup__ConnectorCredentialPair.cc_pair_id == ConnectorCredentialPair.id,
HEAD:backend/ee/onyx/db/user_group.py:404:            UserGroup__ConnectorCredentialPair.user_group_id == UserGroup.id,
HEAD:backend/ee/onyx/db/user_group.py:418:def fetch_user_groups_for_documents(
HEAD:backend/ee/onyx/db/user_group.py:423:    Fetches all user groups that have access to the given documents.
HEAD:backend/ee/onyx/db/user_group.py:430:            UserGroup__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:431:            UserGroup.id == UserGroup__ConnectorCredentialPair.user_group_id,
HEAD:backend/ee/onyx/db/user_group.py:434:            ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:436:                ConnectorCredentialPair.id
HEAD:backend/ee/onyx/db/user_group.py:437:                == UserGroup__ConnectorCredentialPair.cc_pair_id,
HEAD:backend/ee/onyx/db/user_group.py:438:                ConnectorCredentialPair.access_type != AccessType.SYNC,
HEAD:backend/ee/onyx/db/user_group.py:442:            DocumentByConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:444:                DocumentByConnectorCredentialPair.connector_id
HEAD:backend/ee/onyx/db/user_group.py:445:                == ConnectorCredentialPair.connector_id,
HEAD:backend/ee/onyx/db/user_group.py:446:                DocumentByConnectorCredentialPair.credential_id
HEAD:backend/ee/onyx/db/user_group.py:447:                == ConnectorCredentialPair.credential_id,
HEAD:backend/ee/onyx/db/user_group.py:450:        .join(Document, Document.id == DocumentByConnectorCredentialPair.id)
HEAD:backend/ee/onyx/db/user_group.py:452:        .where(UserGroup__ConnectorCredentialPair.is_current == True)  # noqa: E712
HEAD:backend/ee/onyx/db/user_group.py:455:        .where(ConnectorCredentialPair.status != ConnectorCredentialPairStatus.DELETING)
HEAD:backend/ee/onyx/db/user_group.py:502:) -> list[UserGroup__ConnectorCredentialPair]:
HEAD:backend/ee/onyx/db/user_group.py:505:        UserGroup__ConnectorCredentialPair(
HEAD:backend/ee/onyx/db/user_group.py:567:        select(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/user_group.py:568:            UserGroup__ConnectorCredentialPair.user_group_id == user_group_id
HEAD:backend/ee/onyx/db/user_group.py:693:    here because both write paths reach it, and because connectors ride in the same PATCH
HEAD:backend/ee/onyx/db/user_group.py:694:    payload as membership — there is no group-side connector route to guard, unlike agents
HEAD:backend/ee/onyx/db/user_group.py:707:            "A default system group holds only members, so it can't take connectors.",
HEAD:backend/ee/onyx/db/user_group.py:720:    out-of-scope connector to the group, granting its members access. Admins /
HEAD:backend/ee/onyx/db/user_group.py:740:            select(ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/user_group.py:741:                ConnectorCredentialPair.id.in_(added_cc_pair_ids)
HEAD:backend/ee/onyx/db/user_group.py:751:                f"Connector credential pair '{cc_pair_id}' not found.",
HEAD:backend/ee/onyx/db/user_group.py:756:            permission=Permission.MANAGE_CONNECTORS,
HEAD:backend/ee/onyx/db/user_group.py:1038:    _cleanup_credential__user_group_relationships__no_commit(
HEAD:backend/ee/onyx/db/user_group.py:1097:    """Deletes all rows from UserGroup__ConnectorCredentialPair where the
HEAD:backend/ee/onyx/db/user_group.py:1098:    connector_credential_pair_id matches the given cc_pair_id.
HEAD:backend/ee/onyx/db/user_group.py:1100:    Should be used very carefully (only for connectors that are being deleted)."""
HEAD:backend/ee/onyx/db/user_group.py:1101:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/ee/onyx/db/user_group.py:1106:        raise ValueError(f"Connector Credential Pair '{cc_pair_id}' does not exist")
HEAD:backend/ee/onyx/db/user_group.py:1108:    if cc_pair.status != ConnectorCredentialPairStatus.DELETING:
HEAD:backend/ee/onyx/db/user_group.py:1110:            f"Connector Credential Pair '{cc_pair_id}' is not in the DELETING state. status={cc_pair.status}"
HEAD:backend/ee/onyx/db/user_group.py:1113:    delete_stmt = delete(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/user_group.py:1114:        UserGroup__ConnectorCredentialPair.cc_pair_id == cc_pair_id,
HEAD:backend/ee/onyx/external_permissions/box/access.py:15:from onyx.connectors.box.connector import (
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:4:    FetchAllDocumentsFunction,
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:5:    FetchAllDocumentsIdsFunction,
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:10:from onyx.connectors.box.connector import BoxConnector
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:18:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:19:    fetch_all_existing_docs_fn: FetchAllDocumentsFunction,  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:20:    fetch_all_existing_docs_ids_fn: FetchAllDocumentsIdsFunction,
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:23:    box_connector = BoxConnector(**cc_pair.connector.connector_specific_config)
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:24:    box_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:31:        slim_connector=box_connector,
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:6:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:7:from onyx.connectors.box.connector import (
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:8:    BOX_ENTERPRISE_ID_CREDENTIAL_KEY,
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:9:    BoxConnector,
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:15:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:56:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:58:    creds = credential_json(cc_pair)
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:59:    enterprise_id = creds[BOX_ENTERPRISE_ID_CREDENTIAL_KEY]
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:60:    connector = BoxConnector(**cc_pair.connector.connector_specific_config)
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:61:    connector.load_credentials(creds)
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:62:    client = connector.enterprise_client
HEAD:backend/ee/onyx/external_permissions/canvas/access.py:6:from onyx.connectors.canvas.client import CanvasApiClient
HEAD:backend/ee/onyx/external_permissions/canvas/access.py:7:from onyx.connectors.canvas.connector import (
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:4:    FetchAllDocumentsFunction,
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:5:    FetchAllDocumentsIdsFunction,
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:10:from onyx.connectors.canvas.connector import CanvasConnector
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:18:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:19:    fetch_all_existing_docs_fn: FetchAllDocumentsFunction,  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:20:    fetch_all_existing_docs_ids_fn: FetchAllDocumentsIdsFunction,
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:23:    canvas_connector = CanvasConnector(**cc_pair.connector.connector_specific_config)
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:24:    canvas_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:31:        slim_connector=canvas_connector,
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:5:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:6:from onyx.connectors.canvas.connector import (
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:7:    CanvasConnector,
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:13:from onyx.connectors.interfaces import SecondsSinceUnixEpoch
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:14:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:22:def _fetch_account_user_emails(connector: CanvasConnector) -> set[str]:
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:24:    for page in connector.canvas_client.paginate(
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:35:    connector: CanvasConnector,
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:39:    for page in connector.canvas_client.paginate(
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:50:    connector: CanvasConnector,
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:56:    for assignment in connector._list_assignments(course_id):
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:63:    for announcement in connector._list_announcements(
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:75:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:77:    connector = CanvasConnector(**cc_pair.connector.connector_specific_config)
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:78:    connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:80:        datetime_to_utc(cc_pair.connector.indexing_start).timestamp()
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:81:        if cc_pair.connector.indexing_start is not None
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:86:    for course in connector._list_courses():
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:87:        context = build_course_permission_context(connector.canvas_client, course.id)
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:95:            connector,
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:109:                user_emails=list(_fetch_canvas_group_emails(connector, group_id)),
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:120:            user_emails=list(_fetch_account_user_emails(connector)),
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:9:    FetchAllDocumentsFunction,
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:10:    FetchAllDocumentsIdsFunction,
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:15:from onyx.connectors.confluence.connector import ConfluenceConnector
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:16:from onyx.connectors.credentials_provider import OnyxDBCredentialsProvider
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:17:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:29:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:30:    fetch_all_existing_docs_fn: FetchAllDocumentsFunction,  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:31:    fetch_all_existing_docs_ids_fn: FetchAllDocumentsIdsFunction,
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:35:    Fetches document permissions from Confluence and yields DocExternalAccess objects.
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:36:    Compares fetched documents against existing documents in the DB for the connector.
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:39:    confluence_connector = ConfluenceConnector(
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:40:        **cc_pair.connector.connector_specific_config
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:43:    provider = OnyxDBCredentialsProvider(
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:44:        get_current_tenant_id(), "confluence", cc_pair.credential_id
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:46:    confluence_connector.set_credentials_provider(provider)
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:53:        slim_connector=confluence_connector,
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:7:from onyx.connectors.confluence.onyx_confluence import (
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:11:from onyx.connectors.credentials_provider import OnyxDBCredentialsProvider
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:13:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:162:    cc_pair: ConnectorCredentialPair,
```
Connector source code provides candidate mechanisms for acquiring documents
from configured sources.
No real connector was invoked during this action.
## User File and Upload Ingestion
Evidence lines: 450
```text
HEAD:backend/ee/onyx/access/access.py:16:from onyx.access.access import collect_user_file_access
HEAD:backend/ee/onyx/access/access.py:20:from onyx.db.models import User, UserFile
HEAD:backend/ee/onyx/access/access.py:21:from onyx.db.user_file import fetch_user_files_with_access_relationships
HEAD:backend/ee/onyx/access/access.py:122:def _collect_user_file_group_names(user_file: UserFile) -> set[str]:
HEAD:backend/ee/onyx/access/access.py:124:    relationships on a UserFile (skipping deleted personas)."""
HEAD:backend/ee/onyx/access/access.py:126:    for persona in user_file.assistants:
HEAD:backend/ee/onyx/access/access.py:134:def get_access_for_user_files_impl(
HEAD:backend/ee/onyx/access/access.py:135:    user_file_ids: list[str],
HEAD:backend/ee/onyx/access/access.py:141:    Uses a single DB query (via fetch_user_files_with_access_relationships)
HEAD:backend/ee/onyx/access/access.py:146:    user_files = fetch_user_files_with_access_relationships(
HEAD:backend/ee/onyx/access/access.py:147:        user_file_ids, db_session, eager_load_groups=True
HEAD:backend/ee/onyx/access/access.py:149:    return build_access_for_user_files_impl(user_files)
HEAD:backend/ee/onyx/access/access.py:152:def build_access_for_user_files_impl(
HEAD:backend/ee/onyx/access/access.py:153:    user_files: list[UserFile],
HEAD:backend/ee/onyx/access/access.py:155:    """EE version: works on pre-loaded UserFile objects.
HEAD:backend/ee/onyx/access/access.py:161:    for user_file in user_files:
HEAD:backend/ee/onyx/access/access.py:162:        if user_file.user is None:
HEAD:backend/ee/onyx/access/access.py:163:            result[str(user_file.id)] = DocumentAccess.build(
HEAD:backend/ee/onyx/access/access.py:172:        emails, is_public = collect_user_file_access(user_file)
HEAD:backend/ee/onyx/access/access.py:173:        group_names = _collect_user_file_group_names(user_file)
HEAD:backend/ee/onyx/access/access.py:174:        result[str(user_file.id)] = DocumentAccess.build(
HEAD:backend/ee/onyx/background/celery/apps/user_file_processing.py:2:from onyx.background.celery.apps.user_file_processing import celery_app
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:84:    if stored.source == LicenseSource.MANUAL_UPLOAD:
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:104:        if payload.source == LicenseSource.MANUAL_UPLOAD:
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:7:    collect_logs_into_file_store,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:46:    receipt = collect_logs_into_file_store(
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:22:from onyx.file_store.file_store import get_default_file_store
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:102:            get_default_file_store().save_file(
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:112:                file_id=report_name,
HEAD:backend/ee/onyx/configs/license_enforcement_config.py:26:#   /license - Fetch, upload, or check license status
HEAD:backend/ee/onyx/db/persona.py:13:    mark_persona_user_files_for_sync,
HEAD:backend/ee/onyx/db/persona.py:202:        mark_persona_user_files_for_sync(persona_id, db_session)
HEAD:backend/ee/onyx/db/usage_export.py:19:from onyx.file_store.file_store import get_default_file_store
HEAD:backend/ee/onyx/db/usage_export.py:188:    file_store = get_default_file_store()
HEAD:backend/ee/onyx/db/usage_export.py:190:    return file_store.read_file(
HEAD:backend/ee/onyx/db/usage_export.py:191:        file_id=report_display_name, mode="b", use_tempfile=True
HEAD:backend/ee/onyx/db/user_group.py:256:            selectinload(Persona.user_files),
HEAD:backend/ee/onyx/external_permissions/box/access.py:29:# Every accepted Box collaboration role except `uploader` can read or preview.
HEAD:backend/ee/onyx/external_permissions/box/access.py:35:    "previewer uploader",
HEAD:backend/ee/onyx/external_permissions/box/access.py:36:    "viewer uploader",
HEAD:backend/ee/onyx/external_permissions/box/access.py:89:            if role_value != "uploader":
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:5:from fastapi import APIRouter, Depends, HTTPException, Response, UploadFile, status
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:12:    AnalyticsScriptUpload,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:23:    upload_logo,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:44:from onyx.file_store.file_store import get_default_file_store
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:45:from onyx.file_store.serving import resolve_inline_disposition
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:238:    file: UploadFile,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:242:    upload_logo(file=file, is_logotype=is_logotype)
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:269:        file_store = get_default_file_store()
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:270:        onyx_file = file_store.get_file_with_mime_type(get_logo_filename())
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:285:        file_store = get_default_file_store()
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:286:        onyx_file = file_store.get_file_with_mime_type(get_logotype_filename())
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:314:def upload_custom_analytics_script(
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:315:    script_upload: AnalyticsScriptUpload,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:319:        store_analytics_script(script_upload)
HEAD:backend/ee/onyx/server/enterprise_settings/models.py:133:class AnalyticsScriptUpload(BaseModel):
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:6:from fastapi import UploadFile
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:11:    AnalyticsScriptUpload,
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:22:from onyx.file_store.file_store import get_default_file_store
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:121:def store_analytics_script(analytics_script_upload: AnalyticsScriptUpload) -> None:
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:124:        or analytics_script_upload.secret_key != _CUSTOM_ANALYTICS_SECRET_KEY
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:128:    get_kv_store().store(KV_CUSTOM_ANALYTICS_SCRIPT_KEY, analytics_script_upload.script)
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:175:def upload_logo(file: UploadFile | str, is_logotype: bool = False) -> bool:
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:177:        logger.notice("Uploading logo from local path %s", file)
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:189:        logger.notice("Uploading logo from uploaded file")
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:215:    file_store = get_default_file_store()
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:216:    file_store.save_file(
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:221:        file_id=_LOGOTYPE_FILENAME if is_logotype else _LOGO_FILENAME,
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:147:            # shared org key, and an auto container's file_ids reference
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:148:            # org-scoped uploads; only a bare "auto" form is allowed.
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:150:                isinstance(container, dict) and container.get("file_ids")
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:155:                    "or uploaded files are not supported by the Onyx gateway.",
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:168:                    and part.get("file_id")
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:170:                    # References an uploaded file under our shared org key;
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:174:                        "file_id references are not supported by the Onyx "
HEAD:backend/ee/onyx/server/license/api.py:5:2. Upload a license file manually (for air-gapped deployments)
HEAD:backend/ee/onyx/server/license/api.py:14:from fastapi import APIRouter, Depends, File, UploadFile
HEAD:backend/ee/onyx/server/license/api.py:27:    LicenseUploadResponse,
HEAD:backend/ee/onyx/server/license/api.py:181:@router.post("/upload")
HEAD:backend/ee/onyx/server/license/api.py:182:async def upload_license(
HEAD:backend/ee/onyx/server/license/api.py:183:    license_file: UploadFile = File(...),
HEAD:backend/ee/onyx/server/license/api.py:186:) -> LicenseUploadResponse:
HEAD:backend/ee/onyx/server/license/api.py:188:    Upload a license file manually (self-hosted only).
HEAD:backend/ee/onyx/server/license/api.py:196:            "License upload is only available for self-hosted deployments",
HEAD:backend/ee/onyx/server/license/api.py:212:    return LicenseUploadResponse(
HEAD:backend/ee/onyx/server/license/api.py:214:        message=f"License uploaded successfully. {payload.seats} seats, expires {payload.expires_at.date()}",
HEAD:backend/ee/onyx/server/license/models.py:19:    MANUAL_UPLOAD = "manual_upload"
HEAD:backend/ee/onyx/server/license/models.py:65:            else LicenseSource.MANUAL_UPLOAD
HEAD:backend/ee/onyx/server/license/models.py:117:    """Response after license fetch/upload."""
HEAD:backend/ee/onyx/server/license/models.py:124:class LicenseUploadResponse(BaseModel):
HEAD:backend/ee/onyx/server/license/models.py:125:    """Response after license upload."""
HEAD:backend/ee/onyx/server/log_export/api.py:21:    collect_logs_into_file_store,
HEAD:backend/ee/onyx/server/log_export/api.py:40:from onyx.file_store.constants import STANDARD_CHUNK_SIZE
HEAD:backend/ee/onyx/server/log_export/api.py:103:    "user_file_processing": OnyxCeleryQueues.USER_FILE_PROCESSING,
HEAD:backend/ee/onyx/server/log_export/api.py:221:        collect_logs_into_file_store(
HEAD:backend/ee/onyx/server/log_export/collection.py:18:from onyx.file_store.constants import MAX_IN_MEMORY_SIZE
HEAD:backend/ee/onyx/server/log_export/collection.py:55:    """Returns the directories this process writes file logs to.
HEAD:backend/ee/onyx/server/log_export/models.py:8:    UPLOADED = "uploaded"
HEAD:backend/ee/onyx/server/log_export/models.py:11:    # ``UPLOADED`` instead.
HEAD:backend/ee/onyx/server/log_export/models.py:28:    # Number of log files in the uploaded piece; 0 unless ``status`` is
HEAD:backend/ee/onyx/server/log_export/models.py:29:    # ``UPLOADED``.
HEAD:backend/ee/onyx/server/log_export/models.py:31:    # Size of the uploaded piece zip in bytes; 0 unless ``status`` is
HEAD:backend/ee/onyx/server/log_export/models.py:32:    # ``UPLOADED``.
HEAD:backend/ee/onyx/server/log_export/models.py:61:    piece_file_ids: list[str]
HEAD:backend/ee/onyx/server/log_export/storage.py:33:from onyx.file_store.constants import MAX_IN_MEMORY_SIZE, STANDARD_CHUNK_SIZE
HEAD:backend/ee/onyx/server/log_export/storage.py:34:from onyx.file_store.file_store import get_default_file_store
HEAD:backend/ee/onyx/server/log_export/storage.py:39:LOG_EXPORT_FILE_ID_PREFIX = "log_export/"
HEAD:backend/ee/onyx/server/log_export/storage.py:57:def export_file_id_prefix(export_id: str) -> str:
HEAD:backend/ee/onyx/server/log_export/storage.py:59:    return f"{LOG_EXPORT_FILE_ID_PREFIX}{export_id}/"
HEAD:backend/ee/onyx/server/log_export/storage.py:62:def piece_file_id(export_id: str, hostname: str) -> str:
HEAD:backend/ee/onyx/server/log_export/storage.py:64:    return f"{export_file_id_prefix(export_id)}piece_{hostname}.zip"
HEAD:backend/ee/onyx/server/log_export/storage.py:67:def receipt_file_id(export_id: str, worker_name: str) -> str:
HEAD:backend/ee/onyx/server/log_export/storage.py:69:    return f"{export_file_id_prefix(export_id)}receipt_{worker_name}.json"
HEAD:backend/ee/onyx/server/log_export/storage.py:72:def manifest_file_id(export_id: str) -> str:
HEAD:backend/ee/onyx/server/log_export/storage.py:74:    return f"{export_file_id_prefix(export_id)}{BUNDLE_MANIFEST_FILE_NAME}"
HEAD:backend/ee/onyx/server/log_export/storage.py:79:    get_default_file_store().save_file(
HEAD:backend/ee/onyx/server/log_export/storage.py:84:        file_id=manifest_file_id(manifest.export_id),
HEAD:backend/ee/onyx/server/log_export/storage.py:95:    file_store = get_default_file_store()
HEAD:backend/ee/onyx/server/log_export/storage.py:96:    prefix = export_file_id_prefix(export_id)
HEAD:backend/ee/onyx/server/log_export/storage.py:97:    file_ids = {record.file_id for record in file_store.list_files_by_prefix(prefix)}
HEAD:backend/ee/onyx/server/log_export/storage.py:98:    if manifest_file_id(export_id) not in file_ids:
HEAD:backend/ee/onyx/server/log_export/storage.py:101:        file_store.read_file(manifest_file_id(export_id)).read()
HEAD:backend/ee/onyx/server/log_export/storage.py:104:        LogExportReceipt.model_validate_json(file_store.read_file(file_id).read())
HEAD:backend/ee/onyx/server/log_export/storage.py:105:        for file_id in sorted(file_ids)
HEAD:backend/ee/onyx/server/log_export/storage.py:106:        if file_id.removeprefix(prefix).startswith("receipt_")
HEAD:backend/ee/onyx/server/log_export/storage.py:108:    piece_file_ids = sorted(
HEAD:backend/ee/onyx/server/log_export/storage.py:109:        file_id
HEAD:backend/ee/onyx/server/log_export/storage.py:110:        for file_id in file_ids
HEAD:backend/ee/onyx/server/log_export/storage.py:111:        if file_id.removeprefix(prefix).startswith("piece_")
HEAD:backend/ee/onyx/server/log_export/storage.py:114:        manifest=manifest, receipts=receipts, piece_file_ids=piece_file_ids
HEAD:backend/ee/onyx/server/log_export/storage.py:142:        "Contents: one piece_<hostname>.zip per host that uploaded logs, plus",
HEAD:backend/ee/onyx/server/log_export/storage.py:152:        if receipt.status is not LogExportReceiptStatus.UPLOADED:
HEAD:backend/ee/onyx/server/log_export/storage.py:176:    file_store = get_default_file_store()
HEAD:backend/ee/onyx/server/log_export/storage.py:188:        prefix = export_file_id_prefix(snapshot.manifest.export_id)
HEAD:backend/ee/onyx/server/log_export/storage.py:189:        for piece_id in snapshot.piece_file_ids:
HEAD:backend/ee/onyx/server/log_export/storage.py:192:                file_store.read_file(piece_id, use_tempfile=True) as piece_stream,
HEAD:backend/ee/onyx/server/log_export/storage.py:202:        log_file_count=len(snapshot.piece_file_ids),
HEAD:backend/ee/onyx/server/log_export/storage.py:207:def collect_logs_into_file_store(
HEAD:backend/ee/onyx/server/log_export/storage.py:215:    Uploads ``piece_{hostname}.zip`` unless a piece for this hostname already
HEAD:backend/ee/onyx/server/log_export/storage.py:218:    container can all pass it and redundantly upload the same piece (harmless,
HEAD:backend/ee/onyx/server/log_export/storage.py:219:    since ``save_file`` upserts), each reporting ``UPLOADED``.
HEAD:backend/ee/onyx/server/log_export/storage.py:240:    file_store = get_default_file_store()
HEAD:backend/ee/onyx/server/log_export/storage.py:248:        piece_id = piece_file_id(export_id, hostname)
HEAD:backend/ee/onyx/server/log_export/storage.py:249:        existing_file_ids = {
HEAD:backend/ee/onyx/server/log_export/storage.py:250:            record.file_id
HEAD:backend/ee/onyx/server/log_export/storage.py:251:            for record in file_store.list_files_by_prefix(
HEAD:backend/ee/onyx/server/log_export/storage.py:252:                export_file_id_prefix(export_id)
HEAD:backend/ee/onyx/server/log_export/storage.py:255:        if piece_id in existing_file_ids:
HEAD:backend/ee/onyx/server/log_export/storage.py:277:                    file_store.save_file(
HEAD:backend/ee/onyx/server/log_export/storage.py:282:                        file_id=piece_id,
HEAD:backend/ee/onyx/server/log_export/storage.py:284:                    status = LogExportReceiptStatus.UPLOADED
HEAD:backend/ee/onyx/server/log_export/storage.py:308:    file_store.save_file(
HEAD:backend/ee/onyx/server/log_export/storage.py:313:        file_id=receipt_file_id(export_id, worker_name),
HEAD:backend/ee/onyx/server/log_export/storage.py:325:    file_store = get_default_file_store()
HEAD:backend/ee/onyx/server/log_export/storage.py:327:    for record in file_store.list_files_by_prefix(LOG_EXPORT_FILE_ID_PREFIX):
HEAD:backend/ee/onyx/server/log_export/storage.py:330:        file_store.delete_file(record.file_id, error_on_missing=False)
HEAD:backend/ee/onyx/server/query_history/api.py:49:from onyx.file_store.file_store import get_default_file_store
HEAD:backend/ee/onyx/server/query_history/api.py:373:    file_store = get_default_file_store()
HEAD:backend/ee/onyx/server/query_history/api.py:376:    has_file = file_store.has_file(
HEAD:backend/ee/onyx/server/query_history/api.py:377:        file_id=report_name,
HEAD:backend/ee/onyx/server/query_history/api.py:400:    file_store = get_default_file_store()
HEAD:backend/ee/onyx/server/query_history/api.py:401:    has_file = file_store.has_file(
HEAD:backend/ee/onyx/server/query_history/api.py:402:        file_id=report_name,
HEAD:backend/ee/onyx/server/query_history/api.py:409:            csv_stream = file_store.read_file(report_name)
HEAD:backend/ee/onyx/server/query_history/models.py:259:        task_id = extract_task_id_from_query_history_report_name(file.file_id)
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:24:from onyx.file_store.constants import STANDARD_CHUNK_SIZE
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:31:from onyx.file_store.constants import MAX_IN_MEMORY_SIZE
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:32:from onyx.file_store.file_store import FileStore, get_default_file_store
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:54:    file_store: FileStore,
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:99:        file_id = file_store.save_file(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:106:    return file_id
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:111:    file_store: FileStore,
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:131:        file_id = file_store.save_file(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:138:    return file_id
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:142:    file_store: FileStore,
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:186:        file_id = file_store.save_file(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:193:    return file_id
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:197:    file_store: FileStore,
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:238:        return file_store.save_file(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:248:    file_store: FileStore,
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:263:    branding = load_report_branding(file_store)
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:266:    return file_store.save_file(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:281:    file_store = get_default_file_store()
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:284:    intermediate_file_ids: list[str] = []
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:286:        messages_file_id = generate_chat_messages_report(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:287:            db_session, file_store, report_id, normalized_period
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:289:        intermediate_file_ids.append(messages_file_id)
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:290:        users_file_id = generate_user_report(db_session, file_store, report_id)
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:291:        intermediate_file_ids.append(users_file_id)
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:299:        usage_breakdown_file_id = generate_usage_breakdown_report(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:300:            file_store, report_id, usage_rows
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:302:        intermediate_file_ids.append(usage_breakdown_file_id)
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:303:        system_usage_file_id = generate_system_usage_report(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:304:            file_store, report_id, system_usage_rows
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:306:        intermediate_file_ids.append(system_usage_file_id)
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:309:        pdf_file_id: str | None = None
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:311:            pdf_file_id = generate_usage_report_pdf(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:313:                file_store,
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:322:            intermediate_file_ids.append(pdf_file_id)
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:334:                chat_messages_tmpfile = file_store.read_file(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:335:                    messages_file_id, mode="b", use_tempfile=True
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:343:                users_tmpfile = file_store.read_file(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:344:                    users_file_id, mode="b", use_tempfile=True
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:348:                usage_breakdown_tmpfile = file_store.read_file(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:349:                    usage_breakdown_file_id, mode="b", use_tempfile=True
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:353:                system_usage_tmpfile = file_store.read_file(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:354:                    system_usage_file_id, mode="b", use_tempfile=True
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:358:                if pdf_file_id is not None:
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:359:                    pdf_tmpfile = file_store.read_file(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:360:                        pdf_file_id, mode="b", use_tempfile=True
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:366:            # store zip blob to file_store
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:368:            file_store.save_file(
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:373:                file_id=report_name,
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:376:        for file_id in intermediate_file_ids:
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:378:                file_store.delete_file(file_id, error_on_missing=False)
HEAD:backend/ee/onyx/server/reporting/usage_export_generation.py:381:                    "Failed to delete temporary usage report file %s", file_id
HEAD:backend/ee/onyx/server/reporting/usage_report_branding.py:13:from onyx.file_store.file_store import FileStore
HEAD:backend/ee/onyx/server/reporting/usage_report_branding.py:31:def _read_logo(file_store: FileStore, file_id: str) -> bytes | None:
HEAD:backend/ee/onyx/server/reporting/usage_report_branding.py:33:        stored = file_store.get_file_with_mime_type(file_id)
HEAD:backend/ee/onyx/server/reporting/usage_report_branding.py:35:        logger.exception("Failed to read logo %s for the usage report", file_id)
HEAD:backend/ee/onyx/server/reporting/usage_report_branding.py:41:    # ReportLab cannot rasterize SVG, the common upload.
HEAD:backend/ee/onyx/server/reporting/usage_report_branding.py:44:            "Usage report cannot draw logo %s of type %s", file_id, stored.mime_type
HEAD:backend/ee/onyx/server/reporting/usage_report_branding.py:51:def load_report_branding(file_store: FileStore) -> ReportBranding:
HEAD:backend/ee/onyx/server/reporting/usage_report_branding.py:58:        logo = _read_logo(file_store, get_logotype_filename())
HEAD:backend/ee/onyx/server/reporting/usage_report_branding.py:60:        logo = _read_logo(file_store, get_logo_filename())
HEAD:backend/ee/onyx/server/seeding.py:11:    AnalyticsScriptUpload,
HEAD:backend/ee/onyx/server/seeding.py:15:from ee.onyx.server.enterprise_settings.store import store_analytics_script, upload_logo
HEAD:backend/ee/onyx/server/seeding.py:239:        logger.notice("Uploading logo")
HEAD:backend/ee/onyx/server/seeding.py:240:        upload_logo(file=logo_path)
HEAD:backend/ee/onyx/server/seeding.py:250:            analytics_script = AnalyticsScriptUpload(
HEAD:backend/ee/onyx/utils/license.py:138:    at once and needing a hand-uploaded file.
HEAD:backend/onyx/db/_deprecated/pg_file_store.py:11:from onyx.file_store.constants import MAX_IN_MEMORY_SIZE, STANDARD_CHUNK_SIZE
HEAD:backend/onyx/db/chat.py:28:from onyx.file_store.file_store import get_default_file_store
HEAD:backend/onyx/db/chat.py:29:from onyx.file_store.models import FileDescriptor
HEAD:backend/onyx/db/chat.py:55:                selectinload(Persona.user_files),
HEAD:backend/onyx/db/chat.py:225:    file_store = get_default_file_store()
HEAD:backend/onyx/db/chat.py:228:            if file_info.get("user_file_id"):
HEAD:backend/onyx/db/chat.py:231:            file_store.delete_file(file_id=file_info["id"], error_on_missing=False)
HEAD:backend/onyx/db/chat.py:257:        # Caller-supplied only for incognito, where uploads name the session
HEAD:backend/onyx/db/connector.py:38:def check_user_files_exist(db_session: Session) -> bool:
HEAD:backend/onyx/db/connector.py:45:    from onyx.db.enums import UserFileStatus
HEAD:backend/onyx/db/connector.py:46:    from onyx.db.models import UserFile
HEAD:backend/onyx/db/connector.py:48:    stmt = select(exists(UserFile).where(UserFile.status == UserFileStatus.COMPLETED))
HEAD:backend/onyx/db/connector_credential_pair.py:93:    USER_FILE = "user_file"
HEAD:backend/onyx/db/document.py:58:from onyx.file_store.staging import delete_files_best_effort
HEAD:backend/onyx/db/document.py:885:                    file_id=doc.file_id,
HEAD:backend/onyx/db/document.py:902:        "file_id": insert_stmt.excluded.file_id,
HEAD:backend/onyx/db/document.py:1204:def get_file_ids_for_document_ids(
HEAD:backend/onyx/db/document.py:1208:    """Return the non-null `file_id` values attached to the given documents."""
HEAD:backend/onyx/db/document.py:1212:        db_session.query(DbDocument.file_id)
HEAD:backend/onyx/db/document.py:1214:        .filter(DbDocument.file_id.isnot(None))
HEAD:backend/onyx/db/document.py:1217:    return [row.file_id for row in rows if row.file_id is not None]
HEAD:backend/onyx/db/document.py:1220:def get_document_id_to_file_id_map(
HEAD:backend/onyx/db/document.py:1224:    """Return a `{document_id: file_id}` map for docs that have a file_id."""
HEAD:backend/onyx/db/document.py:1228:        db_session.query(DbDocument.id, DbDocument.file_id)
HEAD:backend/onyx/db/document.py:1230:        .filter(DbDocument.file_id.isnot(None))
HEAD:backend/onyx/db/document.py:1233:    return {doc_id: file_id for doc_id, file_id in rows}
HEAD:backend/onyx/db/document.py:1288:    file_ids_to_delete = get_file_ids_for_document_ids(
HEAD:backend/onyx/db/document.py:1297:    delete_files_best_effort(file_ids_to_delete)
HEAD:backend/onyx/db/enums.py:294:class UserFileStatus(str, PyEnum):
HEAD:backend/onyx/db/external_app.py:373:                bundle_file_id=None,
HEAD:backend/onyx/db/file_content.py:8:def get_file_content_by_file_id(
HEAD:backend/onyx/db/file_content.py:9:    file_id: str,
HEAD:backend/onyx/db/file_content.py:12:    record = db_session.query(FileContent).filter_by(file_id=file_id).first()
HEAD:backend/onyx/db/file_content.py:15:            f"File content for file_id {file_id} does not exist or was deleted"
HEAD:backend/onyx/db/file_content.py:20:def get_file_content_by_file_id_optional(
HEAD:backend/onyx/db/file_content.py:21:    file_id: str,
HEAD:backend/onyx/db/file_content.py:24:    return db_session.query(FileContent).filter_by(file_id=file_id).first()
HEAD:backend/onyx/db/file_content.py:28:    file_id: str,
HEAD:backend/onyx/db/file_content.py:34:    race conditions when concurrent calls target the same file_id."""
HEAD:backend/onyx/db/file_content.py:36:        file_id=file_id,
HEAD:backend/onyx/db/file_content.py:41:        index_elements=[FileContent.file_id],
HEAD:backend/onyx/db/file_content.py:50:    return db_session.get(FileContent, file_id)  # ty: ignore[invalid-return-type]
HEAD:backend/onyx/db/file_content.py:53:def transfer_file_content_file_id(
HEAD:backend/onyx/db/file_content.py:54:    old_file_id: str,
HEAD:backend/onyx/db/file_content.py:55:    new_file_id: str,
HEAD:backend/onyx/db/file_content.py:58:    """Move a file_content row from old_file_id to new_file_id in-place.
HEAD:backend/onyx/db/file_content.py:62:    new_file_id already exists in file_record (FK target)."""
HEAD:backend/onyx/db/file_content.py:65:        .filter_by(file_id=old_file_id)
HEAD:backend/onyx/db/file_content.py:66:        .update({"file_id": new_file_id})
HEAD:backend/onyx/db/file_content.py:70:            f"File content for file_id {old_file_id} does not exist or was deleted"
HEAD:backend/onyx/db/file_content.py:74:def delete_file_content_by_file_id(
HEAD:backend/onyx/db/file_content.py:75:    file_id: str,
HEAD:backend/onyx/db/file_content.py:78:    db_session.query(FileContent).filter_by(file_id=file_id).delete()
HEAD:backend/onyx/db/file_record.py:9:from onyx.file_store.constants import INCOGNITO_SESSION_METADATA_KEY
HEAD:backend/onyx/db/file_record.py:20:                    FileRecord.file_id.like(f"{QUERY_REPORT_NAME_PREFIX}-%"),
HEAD:backend/onyx/db/file_record.py:29:def get_filerecord_by_file_id_optional(
HEAD:backend/onyx/db/file_record.py:30:    file_id: str,
HEAD:backend/onyx/db/file_record.py:33:    return db_session.query(FileRecord).filter_by(file_id=file_id).first()
HEAD:backend/onyx/db/file_record.py:45:def get_filerecord_by_file_id(
HEAD:backend/onyx/db/file_record.py:46:    file_id: str,
HEAD:backend/onyx/db/file_record.py:49:    filestore = db_session.query(FileRecord).filter_by(file_id=file_id).first()
HEAD:backend/onyx/db/file_record.py:53:            f"File by id {file_id} does not exist or was deleted"
HEAD:backend/onyx/db/file_record.py:59:def get_filerecords_by_file_ids(
HEAD:backend/onyx/db/file_record.py:60:    file_ids: list[str],
HEAD:backend/onyx/db/file_record.py:65:    if not file_ids:
HEAD:backend/onyx/db/file_record.py:68:        db_session.scalars(select(FileRecord).where(FileRecord.file_id.in_(file_ids)))
HEAD:backend/onyx/db/file_record.py:82:        .where(FileRecord.file_id.in_(file_sizes.keys()))
HEAD:backend/onyx/db/file_record.py:86:        .values(file_size=case(file_sizes, value=FileRecord.file_id))
HEAD:backend/onyx/db/file_record.py:97:        db_session.query(FileRecord).filter(FileRecord.file_id.like(f"{prefix}%")).all()
HEAD:backend/onyx/db/file_record.py:101:def delete_filerecord_by_file_id(
HEAD:backend/onyx/db/file_record.py:102:    file_id: str,
HEAD:backend/onyx/db/file_record.py:105:    db_session.query(FileRecord).filter_by(file_id=file_id).delete()
HEAD:backend/onyx/db/file_record.py:109:    file_id: str,
HEAD:backend/onyx/db/file_record.py:118:        FileRecord.file_id == file_id,
HEAD:backend/onyx/db/file_record.py:123:def get_staged_file_ids_by_index_attempt_id(
HEAD:backend/onyx/db/file_record.py:127:    """Return every `INDEXING_STAGING` file_id tagged with this attempt."""
HEAD:backend/onyx/db/file_record.py:130:            select(FileRecord.file_id)
HEAD:backend/onyx/db/file_record.py:140:def get_staged_file_ids_for_cc_pair_excluding_attempt(
HEAD:backend/onyx/db/file_record.py:146:    """Return `INDEXING_STAGING` file_ids for this cc_pair eligible for
HEAD:backend/onyx/db/file_record.py:164:            select(FileRecord.file_id)
HEAD:backend/onyx/db/file_record.py:184:    file_id: str,
HEAD:backend/onyx/db/file_record.py:195:    race conditions when concurrent calls target the same file_id.
HEAD:backend/onyx/db/file_record.py:208:        file_id=file_id,
HEAD:backend/onyx/db/file_record.py:218:        index_elements=[FileRecord.file_id],
HEAD:backend/onyx/db/file_record.py:231:    return db_session.get(FileRecord, file_id)  # ty: ignore[invalid-return-type]
HEAD:backend/onyx/db/file_record.py:234:def get_incognito_file_ids(session_id: str, db_session: Session) -> list[str]:
HEAD:backend/onyx/db/file_record.py:238:            select(FileRecord.file_id).where(
HEAD:backend/onyx/db/incognito.py:3:A file's privacy is decided when it is uploaded. The client mints the session
HEAD:backend/onyx/db/incognito.py:4:id when incognito is switched on and sends it with every upload, so a file
HEAD:backend/onyx/db/incognito.py:6:the client's word for whether the upload is private.
HEAD:backend/onyx/db/incognito.py:17:from onyx.db.enums import IncognitoRecordMode, UserFileStatus
HEAD:backend/onyx/db/incognito.py:18:from onyx.db.models import ChatSession, User__UserGroup, UserFile, UserGroup
HEAD:backend/onyx/db/incognito.py:45:    client-side, so uploads can name a session that no message ever created.
HEAD:backend/onyx/db/incognito.py:59:def mark_user_files_deleting(db_session: Session, file_ids: Sequence[UUID]) -> None:
HEAD:backend/onyx/db/incognito.py:61:    if not file_ids:
HEAD:backend/onyx/db/incognito.py:64:        update(UserFile)
HEAD:backend/onyx/db/incognito.py:65:        .where(UserFile.id.in_(file_ids))
HEAD:backend/onyx/db/incognito.py:66:        .values(status=UserFileStatus.DELETING)
HEAD:backend/onyx/db/incognito.py:70:def mark_incognito_user_files_deleting(
HEAD:backend/onyx/db/incognito.py:73:    """Queue a session's uploads for deletion. Caller commits.
HEAD:backend/onyx/db/incognito.py:75:    Keyed on the session rather than a caller-supplied id list, so an upload
HEAD:backend/onyx/db/incognito.py:80:        UserFile.incognito_session_id == chat_session_id,
HEAD:backend/onyx/db/incognito.py:81:        UserFile.status != UserFileStatus.DELETING,
HEAD:backend/onyx/db/incognito.py:84:        conditions.append(UserFile.user_id == user_id)
HEAD:backend/onyx/db/incognito.py:85:    file_ids = list(db_session.scalars(select(UserFile.id).where(*conditions)).all())
HEAD:backend/onyx/db/incognito.py:86:    mark_user_files_deleting(db_session, file_ids)
HEAD:backend/onyx/db/incognito.py:87:    return file_ids
HEAD:backend/onyx/db/incognito.py:90:def _stale_upload_conditions() -> list[Any]:
HEAD:backend/onyx/db/incognito.py:91:    """Uploads old enough for a sweep to consider, whatever claims them."""
HEAD:backend/onyx/db/incognito.py:94:        # Matches ix_user_file_incognito_sweep's partial predicate.
HEAD:backend/onyx/db/incognito.py:95:        UserFile.incognito.is_(True),
HEAD:backend/onyx/db/incognito.py:96:        UserFile.status != UserFileStatus.DELETING,
HEAD:backend/onyx/db/incognito.py:97:        UserFile.last_accessed_at < cutoff,
HEAD:backend/onyx/db/incognito.py:101:def stale_unadopted_upload_ids(db_session: Session) -> list[UUID]:
HEAD:backend/onyx/db/incognito.py:102:    """Stale uploads no session ever claimed.
HEAD:backend/onyx/db/incognito.py:109:            select(UserFile.id)
HEAD:backend/onyx/db/incognito.py:110:            .where(*_stale_upload_conditions(), UserFile.incognito_session_id.is_(None))
HEAD:backend/onyx/db/incognito.py:111:            .order_by(UserFile.last_accessed_at)
HEAD:backend/onyx/db/incognito.py:118:    """Sessions holding stale uploads whose liveness decides their fate.
HEAD:backend/onyx/db/incognito.py:121:    thousands of uploads costs a single slot. Sessions that persist content are
HEAD:backend/onyx/db/incognito.py:131:        select(UserFile.incognito_session_id)
HEAD:backend/onyx/db/incognito.py:132:        .outerjoin(ChatSession, ChatSession.id == UserFile.incognito_session_id)
HEAD:backend/onyx/db/incognito.py:134:            *_stale_upload_conditions(),
HEAD:backend/onyx/db/incognito.py:135:            UserFile.incognito_session_id.is_not(None),
HEAD:backend/onyx/db/incognito.py:138:        .group_by(UserFile.incognito_session_id)
HEAD:backend/onyx/db/incognito.py:139:        .order_by(func.min(UserFile.last_accessed_at))
HEAD:backend/onyx/db/incognito.py:147:def touch_incognito_uploads_for_sessions(
HEAD:backend/onyx/db/incognito.py:150:    """Restart the orphan clock on these sessions' uploads. Caller commits.
HEAD:backend/onyx/db/incognito.py:159:        update(UserFile)
HEAD:backend/onyx/db/incognito.py:161:            UserFile.incognito_session_id.in_(chat_session_ids),
HEAD:backend/onyx/db/incognito.py:162:            UserFile.status != UserFileStatus.DELETING,
HEAD:backend/onyx/db/incognito.py:168:def stale_upload_ids_for_sessions(
HEAD:backend/onyx/db/incognito.py:171:    """The stale uploads these sessions hold."""
HEAD:backend/onyx/db/incognito.py:176:            select(UserFile.id).where(
HEAD:backend/onyx/db/incognito.py:177:                *_stale_upload_conditions(),
HEAD:backend/onyx/db/incognito.py:178:                UserFile.incognito_session_id.in_(chat_session_ids),
HEAD:backend/onyx/db/models.py:124:    UserFileStatus,
HEAD:backend/onyx/db/models.py:129:from onyx.file_store.models import FileDescriptor
HEAD:backend/onyx/db/models.py:493:    files: Mapped[list["UserFile"]] = relationship("UserFile", back_populates="user")
HEAD:backend/onyx/db/models.py:1128:    file_id: Mapped[str | None] = mapped_column(String, nullable=True)
HEAD:backend/onyx/db/models.py:4243:    uploaded_image_id: Mapped[str | None] = mapped_column(String, nullable=True)
HEAD:backend/onyx/db/models.py:4304:    # Relationship to UserFile
HEAD:backend/onyx/db/models.py:4305:    user_files: Mapped[list["UserFile"]] = relationship(
HEAD:backend/onyx/db/models.py:4306:        "UserFile",
HEAD:backend/onyx/db/models.py:4307:        secondary="persona__user_file",
HEAD:backend/onyx/db/models.py:4343:class Persona__UserFile(Base):
HEAD:backend/onyx/db/models.py:4344:    __tablename__ = "persona__user_file"
HEAD:backend/onyx/db/models.py:4349:    user_file_id: Mapped[UUID] = mapped_column(
HEAD:backend/onyx/db/models.py:4350:        ForeignKey("user_file.id", ondelete="CASCADE"), primary_key=True
HEAD:backend/onyx/db/models.py:4845:    file_id: Mapped[str] = mapped_column(String, primary_key=True)
HEAD:backend/onyx/db/models.py:4873:    Used when FILE_STORE_BACKEND=postgres to avoid needing S3/MinIO."""
HEAD:backend/onyx/db/models.py:4877:    file_id: Mapped[str] = mapped_column(
HEAD:backend/onyx/db/models.py:4879:        ForeignKey("file_record.file_id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:4907:    # row is a custom (admin-uploaded) skill and bundle_file_id is set.
HEAD:backend/onyx/db/models.py:4908:    # Exactly one of (built_in_skill_id, bundle_file_id) is non-null —
HEAD:backend/onyx/db/models.py:4914:    bundle_file_id: Mapped[str | None] = mapped_column(String, nullable=True)
HEAD:backend/onyx/db/models.py:4969:            "(built_in_skill_id IS NULL) <> (bundle_file_id IS NULL)",
HEAD:backend/onyx/db/models.py:5452:    report_name: Mapped[str] = mapped_column(ForeignKey("file_record.file_id"))
HEAD:backend/onyx/db/models.py:5508:class Project__UserFile(Base):
HEAD:backend/onyx/db/models.py:5509:    __tablename__ = "project__user_file"
HEAD:backend/onyx/db/models.py:5514:    user_file_id: Mapped[UUID] = mapped_column(
HEAD:backend/onyx/db/models.py:5515:        ForeignKey("user_file.id"), primary_key=True
HEAD:backend/onyx/db/models.py:5523:            "ix_project__user_file_project_id_created_at",
HEAD:backend/onyx/db/models.py:5541:    user_files: Mapped[list["UserFile"]] = relationship(
HEAD:backend/onyx/db/models.py:5542:        "UserFile",
HEAD:backend/onyx/db/models.py:5543:        secondary=Project__UserFile.__table__,
HEAD:backend/onyx/db/models.py:5558:class UserFile(Base):
HEAD:backend/onyx/db/models.py:5559:    __tablename__ = "user_file"
HEAD:backend/onyx/db/models.py:5564:        secondary=Persona__UserFile.__table__,
HEAD:backend/onyx/db/models.py:5565:        back_populates="user_files",
HEAD:backend/onyx/db/models.py:5567:    file_id: Mapped[str] = mapped_column(nullable=False)
HEAD:backend/onyx/db/models.py:5577:    status: Mapped[UserFileStatus] = mapped_column(
HEAD:backend/onyx/db/models.py:5578:        Enum(UserFileStatus, native_enum=False, name="userfilestatus"),
HEAD:backend/onyx/db/models.py:5580:        default=UserFileStatus.PROCESSING,
HEAD:backend/onyx/db/models.py:5582:    # Privacy is decided when the file is uploaded, from the toggle state, so
HEAD:backend/onyx/db/models.py:5599:    # reindex-port dirty bit: the secondary index is stale/missing for this file (content
HEAD:backend/onyx/db/models.py:5618:        secondary=Project__UserFile.__table__,
HEAD:backend/onyx/db/models.py:5619:        back_populates="user_files",
HEAD:backend/onyx/db/models.py:5627:            "ix_user_file_incognito_sweep",
HEAD:backend/onyx/db/models.py:5634:            "ix_user_file_secondary_reconcile_pending",
HEAD:backend/onyx/db/models.py:5639:        Index("ix_user_file_user_status_id", "user_id", "status", "id"),
HEAD:backend/onyx/db/models.py:5641:            "ix_user_file_user_id_completed",
HEAD:backend/onyx/db/models.py:6522:    archive_file_id: Mapped[str | None] = mapped_column(String, nullable=True)
HEAD:backend/onyx/db/models.py:6590:    # Coalescing key so multi-request provider flows (a Slack upload spans
HEAD:backend/onyx/db/persona.py:40:    UserFile,
HEAD:backend/onyx/db/persona.py:374:        mark_persona_user_files_for_sync(persona_id, db_session)
HEAD:backend/onyx/db/persona.py:641:        converted_user_file_ids = None
HEAD:backend/onyx/db/persona.py:642:        if create_persona_request.user_file_ids is not None:
HEAD:backend/onyx/db/persona.py:644:                converted_user_file_ids = [
HEAD:backend/onyx/db/persona.py:645:                    UUID(str_id) for str_id in create_persona_request.user_file_ids
HEAD:backend/onyx/db/persona.py:648:                raise ValueError("Invalid user_file_ids; must be UUID strings")
HEAD:backend/onyx/db/persona.py:665:            uploaded_image_id=create_persona_request.uploaded_image_id,
HEAD:backend/onyx/db/persona.py:672:            user_file_ids=converted_user_file_ids,
HEAD:backend/onyx/db/persona.py:810:    mark_persona_user_files_for_sync(persona_id, db_session)
HEAD:backend/onyx/db/persona.py:948:    mark_persona_user_files_for_sync(persona_id, db_session)
HEAD:backend/onyx/db/persona.py:994:    mark_persona_user_files_for_sync(persona_id, db_session)
HEAD:backend/onyx/db/persona.py:1115:        selectinload(Persona.user_files),
HEAD:backend/onyx/db/persona.py:1311:        selectinload(Persona.user_files),
HEAD:backend/onyx/db/persona.py:1436:    affected_file_ids = [uf.id for uf in persona.user_files]
HEAD:backend/onyx/db/persona.py:1437:    if affected_file_ids:
HEAD:backend/onyx/db/persona.py:1438:        _mark_files_need_persona_sync(db_session, affected_file_ids)
HEAD:backend/onyx/db/persona.py:1453:    affected_file_ids = [uf.id for uf in persona.user_files]
HEAD:backend/onyx/db/persona.py:1454:    if affected_file_ids:
HEAD:backend/onyx/db/persona.py:1455:        _mark_files_need_persona_sync(db_session, affected_file_ids)
HEAD:backend/onyx/db/persona.py:1522:def mark_persona_user_files_for_sync(
HEAD:backend/onyx/db/persona.py:1530:        .options(selectinload(Persona.user_files))
HEAD:backend/onyx/db/persona.py:1536:    file_ids = [uf.id for uf in persona.user_files]
HEAD:backend/onyx/db/persona.py:1537:    _mark_files_need_persona_sync(db_session, file_ids)
HEAD:backend/onyx/db/persona.py:1542:    user_file_ids: list[UUID],
HEAD:backend/onyx/db/persona.py:1544:    """Flag the given UserFile rows so the background sync task picks them up
HEAD:backend/onyx/db/persona.py:1546:    if not user_file_ids:
HEAD:backend/onyx/db/persona.py:1548:    db_session.query(UserFile).filter(UserFile.id.in_(user_file_ids)).update(
HEAD:backend/onyx/db/persona.py:1549:        {UserFile.needs_persona_sync: True},
HEAD:backend/onyx/db/persona.py:1570:    uploaded_image_id: str | None = None,
HEAD:backend/onyx/db/persona.py:1579:    user_file_ids: list[UUID] | None = None,
HEAD:backend/onyx/db/persona.py:1685:    # Fetch and attach user_files by IDs
HEAD:backend/onyx/db/persona.py:1686:    user_files = None
HEAD:backend/onyx/db/persona.py:1687:    if user_file_ids is not None:
HEAD:backend/onyx/db/persona.py:1688:        user_files = (
```
User-uploaded files form a separate ingestion surface and therefore require
their own ownership and access-control analysis.
## Indexing Orchestration
Evidence lines: 550
```text
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:22:from ee.onyx.db.connector_credential_pair import get_all_auto_sync_cc_pairs
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:50:from onyx.db.connector import mark_cc_pair_as_permissions_synced
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:64:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:71:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:81:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:163:def _is_external_doc_permissions_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:166:    if cc_pair.access_type != AccessType.SYNC:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:170:    if cc_pair.status != ConnectorCredentialPairStatus.ACTIVE:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:173:    sync_config = get_source_perm_sync_config(cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:175:        logger.error("No sync config found for %s", cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:179:        logger.error("No doc sync config found for %s", cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:182:    # if indexing also does perm sync, don't start running doc_sync until at
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:183:    # least one indexing is done
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:186:        and cc_pair.last_successful_index_time is None
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:191:    last_perm_sync = cc_pair.last_time_perm_sync
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:231:        cc_pair_ids_to_sync: list[int] = []
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:233:            cc_pairs = get_all_auto_sync_cc_pairs(db_session)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:235:            cc_pair_ids_to_sync.extend(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:236:                cc_pair.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:237:                for cc_pair in cc_pairs
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:238:                if _is_external_doc_permissions_sync_due(cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:242:        # whenever doc-permission sync has any due cc_pairs to dispatch.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:243:        if cc_pair_ids_to_sync:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:247:        for cc_pair_id in cc_pair_ids_to_sync:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:249:                self.app, cc_pair_id, r, tenant_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:255:                f"Permissions sync queued: cc_pair={cc_pair_id} id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:319:    cc_pair_id: int,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:329:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:361:                    entity_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:380:                cc_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:396:            f"Unexpected try_creating_permissions_sync_task exception: cc_pair={cc_pair_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:404:        f"try_creating_permissions_sync_task finished: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:419:    cc_pair_id: int,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:432:    doc_permission_sync_ctx_dict["cc_pair_id"] = cc_pair_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:438:            connector_credential_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:442:            f"Created doc permission sync attempt: {attempt_id} for cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:445:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:494:        + f"_{redis_connector.cc_pair_id}",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:502:            f"Permission sync task already running, exiting...: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:517:            cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:519:                cc_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:523:            if cc_pair is None:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:525:                    f"No connector credential pair found for id: {cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:530:                    cc_pair.connector.id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:531:                    cc_pair.credential.id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:532:                    cc_pair.access_type,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:539:                        f"Unable to create connector credential pair for id: {cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:543:                    f"validate_ccpair_permissions_sync exceptioned: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:548:            source_type = cc_pair.connector.source
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:564:                    f"No doc sync func found for {source_type} with cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:567:            logger.info("Syncing docs for %s with cc_pair=%s", source_type, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:573:                raise ValueError(f"No fence payload found: cc_pair={cc_pair_id}")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:587:            connector_id = cc_pair.connector.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:588:            credential_id = cc_pair.credential.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:613:        # cc_pair is detached: connectors may read eager-loaded connector/credential
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:617:            cc_pair,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:624:            f"RedisConnector.permissions.generate_tasks starting. cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:631:                    f"cc_pair={cc_pair_id} "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:648:            f"cc_pair={cc_pair_id} tasks_generated={tasks_generated} docs_with_errors={docs_with_errors}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:673:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:676:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:697:        f"Permission sync finished: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:747:                    # If a new document was created, we associate it with the cc_pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:845:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:846:    This can happen if the indexing worker hard crashes or is terminated.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:857:    2.2. The indexing watchdog checks the spawned task.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:873:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:874:    if cc_pair_id_str is None:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:880:    cc_pair_id = int(cc_pair_id_str)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:882:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:897:            f"cc_pair={cc_pair_id} "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:979:        f"cc_pair={cc_pair_id} "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:988:class PermissionSyncCallback(IndexingHeartbeatInterface):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1023:                    "PermissionSyncCallback - task timeout exceeded: elapsed=%ss timeout=%ss cc_pair=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1026:                    self.redis_connector.cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1069:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1070:    if cc_pair_id_str is None:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1072:            f"monitor_ccpair_permissions_taskset: could not parse cc_pair_id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1076:    cc_pair_id = int(cc_pair_id_str)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1078:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1099:        f"Permissions sync progress: cc_pair={cc_pair_id} id={payload.id} remaining={remaining} initial={initial}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1106:            "cc_pair_id": cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1116:    mark_cc_pair_as_permissions_synced(db_session, int(cc_pair_id), payload.started)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1118:        f"Permissions sync finished: cc_pair={cc_pair_id} id={payload.id} num_synced={initial}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1124:        data={"cc_pair_id": cc_pair_id},
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1130:        entity_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:4:    source_group_sync_is_cc_pair_agnostic,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:6:from onyx.db.connector import mark_cc_pair_as_external_group_synced
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:8:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:11:def _get_all_cc_pair_ids_to_mark_as_group_synced(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:12:    db_session: Session, cc_pair: ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:14:    if not source_group_sync_is_cc_pair_agnostic(cc_pair.connector.source):
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:15:        return [cc_pair.id]
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:17:    cc_pairs = get_connector_credential_pairs_for_source(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:18:        db_session, cc_pair.connector.source
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:20:    return [cc_pair.id for cc_pair in cc_pairs]
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:23:def mark_all_relevant_cc_pairs_as_external_group_synced(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:24:    db_session: Session, cc_pair: ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:28:    cc_pair_ids = _get_all_cc_pair_ids_to_mark_as_group_synced(db_session, cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:29:    for cc_pair_id in cc_pair_ids:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:30:        mark_cc_pair_as_external_group_synced(db_session, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:14:    mark_all_relevant_cc_pairs_as_external_group_synced,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:17:    get_all_auto_sync_cc_pairs,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:18:    get_cc_pairs_by_source,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:27:    get_all_cc_pair_agnostic_group_sync_sources,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:54:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:58:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:118:def _is_external_group_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:121:    if cc_pair.access_type != AccessType.SYNC:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:123:            f"Received non-sync CC Pair {cc_pair.id} for external group sync. Actual access type: {cc_pair.access_type}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:127:    if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:129:            f"Skipping group sync for CC Pair {cc_pair.id} - CC Pair is being deleted"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:133:    sync_config = get_source_perm_sync_config(cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:136:            f"Skipping group sync for CC Pair {cc_pair.id} - no sync config found for {cc_pair.connector.source}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:144:            f"Skipping group sync for CC Pair {cc_pair.id} - no group sync config found for {cc_pair.connector.source}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:149:    last_ext_group_sync = cc_pair.last_time_external_group_sync
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:188:        cc_pair_ids_to_sync: list[int] = []
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:190:            cc_pairs = get_all_auto_sync_cc_pairs(db_session)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:192:            # For some sources, we only want to sync one cc_pair per source type
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:193:            for source in get_all_cc_pair_agnostic_group_sync_sources():
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:194:                # These are ordered by cc_pair id so the first one is the one we want
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:195:                cc_pairs_to_dedupe = get_cc_pairs_by_source(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:199:                    status=ConnectorCredentialPairStatus.ACTIVE,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:201:                # dedupe cc_pairs to only keep the first one
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:202:                for cc_pair_to_remove in cc_pairs_to_dedupe[1:]:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:203:                    cc_pairs = [
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:204:                        cc_pair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:205:                        for cc_pair in cc_pairs
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:206:                        if cc_pair.id != cc_pair_to_remove.id
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:209:            cc_pair_ids_to_sync.extend(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:210:                cc_pair.id
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:211:                for cc_pair in cc_pairs
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:212:                if _is_external_group_sync_due(cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:216:        # whenever external-group sync has any due cc_pairs to dispatch.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:217:        if cc_pair_ids_to_sync:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:221:        for cc_pair_id in cc_pair_ids_to_sync:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:223:                self.app, cc_pair_id, r, tenant_id
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:229:                f"External group sync queued: cc_pair={cc_pair_id} id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:273:    cc_pair_id: int,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:281:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:288:                cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:301:                    entity_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:323:                cc_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:338:            f"Unexpected try_creating_external_group_sync_task exception: cc_pair={cc_pair_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:341:            f"Unexpected exception while trying to create external group sync task: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:346:        f"try_creating_external_group_sync_task finished: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:361:    cc_pair_id: int,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:369:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:383:            emit_background_error(msg, cc_pair_id=cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:391:            emit_background_error(msg, cc_pair_id=cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:397:            emit_background_error(msg, cc_pair_id=cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:417:        + f"_{redis_connector.cc_pair_id}",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:424:            f"External group sync task already running, exiting...: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:433:            cc_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:440:                entity_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:447:            f"External group sync exceptioned: cc_pair={cc_pair_id} payload_id={payload.id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:450:            f"External group sync exceptioned: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:453:        msg = f"External group sync exceptioned: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:455:        emit_background_error(msg + f"\n\n{e}", cc_pair_id=cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:460:                entity_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:475:        f"External group sync finished: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:480:    cc_pair_id: int,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:489:            connector_credential_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:493:            "Created external group sync attempt: %s for cc_pair=%s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:495:            cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:500:            cc_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:510:    cc_pair_id: int,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:516:        cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:518:            cc_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:521:        if cc_pair is None:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:522:            raise ValueError(f"No connector credential pair found for id: {cc_pair_id}")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:524:        source_type = cc_pair.connector.source
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:528:            msg = f"No sync config found for {source_type} for cc_pair: {cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:529:            emit_background_error(msg, cc_pair_id=cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:534:            msg = f"No group sync config found for {source_type} for cc_pair: {cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:535:            emit_background_error(msg, cc_pair_id=cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:548:            "Removing stale external groups from prior cycle for %s for cc_pair: %s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:550:            cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:552:        remove_stale_external_groups(db_session, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:555:            "Marking old external groups as stale for %s for cc_pair: %s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:557:            cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:559:        mark_old_external_groups_as_stale(db_session, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:566:            "Syncing external groups for %s for cc_pair: %s", source_type, cc_pair_id
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:575:            external_user_group_generator = ext_group_sync_func(tenant_id, cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:584:                        f"cc_pair={cc_pair_id} "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:604:                        cc_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:606:                        source=cc_pair.connector.source,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:616:                    cc_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:618:                    source=cc_pair.connector.source,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:635:                "Error syncing external groups for %s for cc_pair: %s %s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:637:                cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:645:            "Removing stale external groups for %s for cc_pair: %s",
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:647:            cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:649:        remove_stale_external_groups(db_session, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:674:        mark_all_relevant_cc_pairs_as_external_group_synced(db_session, cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:717:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:718:    This can happen if the indexing worker hard crashes or is terminated.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:729:    2.2. The indexing watchdog checks the spawned task.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:742:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:743:    if cc_pair_id_str is None:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:751:    cc_pair_id = int(cc_pair_id_str)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:754:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:766:            f"cc_pair={cc_pair_id} "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:770:        emit_background_error(msg, cc_pair_id=cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:791:        # the celery task was prefetched and is reserved within the indexing worker
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:807:            f"cc_pair={cc_pair_id} "
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:811:        cc_pair_id=cc_pair_id,
HEAD:backend/onyx/background/README.md:5:1. Pulling/Indexing documents (from connectors)
HEAD:backend/onyx/background/README.md:7:3. Cleaning up checkpoints and logic around indexing work (indexing indexing checkpoints and index attempt metadata)
HEAD:backend/onyx/background/README.md:16:| Light                     | `apps/light.py`                | `vespa_metadata_sync`, `connector_deletion`, `doc_permissions_upsert`, `checkpoint_cleanup`, `index_attempt_cleanup` |
HEAD:backend/onyx/background/README.md:57:| `check_for_indexing`              | 15s       | Scans for connectors needing indexing → dispatches to `DOCFETCHING` queue                  |
HEAD:backend/onyx/background/README.md:62:| `check_for_checkpoint_cleanup`    | 1h        | Cleans up old indexing checkpoints                                                         |
HEAD:backend/onyx/background/README.md:63:| `check_for_index_attempt_cleanup` | 30m       | Cleans up old index attempts                                                               |
HEAD:backend/onyx/background/README.md:93:Docprocessing and Docfetching are for indexing documents:
HEAD:backend/onyx/background/README.md:96:- Docprocessing retrieves batches, runs the indexing pipeline (chunking, embedding), and indexes into the Document Index
HEAD:backend/onyx/background/celery/apps/app_base.py:39:    ENABLE_OPENSEARCH_INDEXING_FOR_ONYX,
HEAD:backend/onyx/background/celery/apps/app_base.py:154:    # prefixes observed when a pruning task finishes and an indexing task
HEAD:backend/onyx/background/celery/apps/app_base.py:237:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:238:        if cc_pair_id is not None:
HEAD:backend/onyx/background/celery/apps/app_base.py:239:            RedisConnectorDelete.remove_from_taskset(int(cc_pair_id), task_id, r)
HEAD:backend/onyx/background/celery/apps/app_base.py:243:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:244:        if cc_pair_id is not None:
HEAD:backend/onyx/background/celery/apps/app_base.py:245:            RedisConnectorPrune.remove_from_taskset(int(cc_pair_id), task_id, r)
HEAD:backend/onyx/background/celery/apps/app_base.py:249:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:250:        if cc_pair_id is not None:
HEAD:backend/onyx/background/celery/apps/app_base.py:252:                int(cc_pair_id), task_id, r
HEAD:backend/onyx/background/celery/apps/app_base.py:257:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:258:        if cc_pair_id is not None:
HEAD:backend/onyx/background/celery/apps/app_base.py:260:                int(cc_pair_id), task_id, r
HEAD:backend/onyx/background/celery/apps/app_base.py:690:    if ENABLE_OPENSEARCH_INDEXING_FOR_ONYX:
HEAD:backend/onyx/background/celery/apps/docfetching.py:26:from onyx.server.metrics.indexing_task_metrics import (
HEAD:backend/onyx/background/celery/apps/docfetching.py:27:    on_indexing_task_postrun,
HEAD:backend/onyx/background/celery/apps/docfetching.py:28:    on_indexing_task_prerun,
HEAD:backend/onyx/background/celery/apps/docfetching.py:52:    on_indexing_task_prerun(task_id, task, kwargs)
HEAD:backend/onyx/background/celery/apps/docfetching.py:68:    on_indexing_task_postrun(task_id, task, kwargs, state)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:27:from onyx.server.metrics.indexing_task_metrics import (
HEAD:backend/onyx/background/celery/apps/docprocessing.py:28:    on_indexing_task_postrun,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:29:    on_indexing_task_prerun,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:53:    on_indexing_task_prerun(task_id, task, kwargs)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:70:    on_indexing_task_postrun(task_id, task, kwargs, state)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:117:    # rkuo: Transient errors keep happening in the indexing watchdog threads.
HEAD:backend/onyx/background/celery/apps/monitoring.py:86:        from onyx.server.metrics.indexing_pipeline_setup import (
HEAD:backend/onyx/background/celery/apps/monitoring.py:87:            setup_indexing_pipeline_metrics,
HEAD:backend/onyx/background/celery/apps/monitoring.py:90:        setup_indexing_pipeline_metrics(sender.app)
HEAD:backend/onyx/background/celery/apps/monitoring.py:91:        logger.info("Prometheus indexing pipeline collectors registered")
HEAD:backend/onyx/background/celery/apps/monitoring.py:94:        logger.exception("Failed to register Prometheus indexing pipeline collectors")
HEAD:backend/onyx/background/celery/apps/monitoring.py:101:    Isolated from the indexing-pipeline registration on purpose: that one gates
HEAD:backend/onyx/background/celery/apps/primary.py:29:from onyx.db.index_attempt import get_index_attempt, mark_attempt_canceled
HEAD:backend/onyx/background/celery/apps/primary.py:30:from onyx.db.indexing_coordination import IndexingCoordination
HEAD:backend/onyx/background/celery/apps/primary.py:207:        potentially_orphaned_ids = IndexingCoordination.get_orphaned_index_attempt_ids(
HEAD:backend/onyx/background/celery/apps/primary.py:212:            attempt = get_index_attempt(db_session, attempt_id)
HEAD:backend/onyx/background/celery/apps/primary.py:214:            # handle case where not started or docfetching is done but indexing is not
HEAD:backend/onyx/background/celery/apps/primary.py:233:                    f"index_attempt={attempt.id} "
HEAD:backend/onyx/background/celery/apps/primary.py:234:                    f"cc_pair={attempt.connector_credential_pair_id} "
HEAD:backend/onyx/background/celery/apps/user_file_processing.py:63:    # rkuo: Transient errors keep happening in the indexing watchdog threads.
HEAD:backend/onyx/background/celery/celery_redis.py:71:    There can be other tasks in here besides indexing tasks, so this is mostly useful
HEAD:backend/onyx/background/celery/celery_redis.py:83:    Unacked entries belonging to the indexing queues are "prefetched", so this gives
HEAD:backend/onyx/background/celery/celery_redis.py:188:    # filter for and create an indexing specific inspect object
HEAD:backend/onyx/background/celery/celery_utils.py:36:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/onyx/background/celery/celery_utils.py:148:    callback: IndexingHeartbeatInterface | None = None,
HEAD:backend/onyx/background/celery/celery_utils.py:306:    e.g. /tmp/onyx_k8s_indexing_readiness.txt
HEAD:backend/onyx/background/celery/configs/docprocessing.py:22:# Indexing worker specific ... this lets us track the transition to STARTED in redis
HEAD:backend/onyx/background/celery/configs/docprocessing.py:24:# indexing tasks are not high volume
HEAD:backend/onyx/background/celery/memory_monitoring.py:11:    INDEXING_WORKER_MEMORY_LIMIT_MB,
HEAD:backend/onyx/background/celery/memory_monitoring.py:12:    INDEXING_WORKER_TRACEMALLOC,
HEAD:backend/onyx/background/celery/memory_monitoring.py:85:# --- Near-limit memory diagnostics for spawned indexing workers ---
HEAD:backend/onyx/background/celery/memory_monitoring.py:86:# When a worker's RSS crosses a fraction of INDEXING_WORKER_MEMORY_LIMIT_MB,
HEAD:backend/onyx/background/celery/memory_monitoring.py:98:def start_memory_observer(index_attempt_id: int) -> MemoryObserver | None:
HEAD:backend/onyx/background/celery/memory_monitoring.py:101:    if INDEXING_WORKER_MEMORY_LIMIT_MB <= 0:
HEAD:backend/onyx/background/celery/memory_monitoring.py:104:    if INDEXING_WORKER_TRACEMALLOC and not tracemalloc.is_tracing():
HEAD:backend/onyx/background/celery/memory_monitoring.py:110:        args=(index_attempt_id, stop_event),
HEAD:backend/onyx/background/celery/memory_monitoring.py:111:        name=f"memory-observer-{index_attempt_id}",
HEAD:backend/onyx/background/celery/memory_monitoring.py:126:def _observe(index_attempt_id: int, stop_event: threading.Event) -> None:
HEAD:backend/onyx/background/celery/memory_monitoring.py:127:    report_threshold_mb = int(INDEXING_WORKER_MEMORY_LIMIT_MB * _REPORT_FRACTION)
HEAD:backend/onyx/background/celery/memory_monitoring.py:136:        _report(index_attempt_id, rss_mb)
HEAD:backend/onyx/background/celery/memory_monitoring.py:141:def _report(index_attempt_id: int, rss_mb: int) -> None:
HEAD:backend/onyx/background/celery/memory_monitoring.py:143:        "Indexing worker memory nearing the limit: attempt=%s rss_mb=%s limit_mb=%s",
HEAD:backend/onyx/background/celery/memory_monitoring.py:144:        index_attempt_id,
HEAD:backend/onyx/background/celery/memory_monitoring.py:146:        INDEXING_WORKER_MEMORY_LIMIT_MB,
HEAD:backend/onyx/background/celery/memory_monitoring.py:151:            "tracemalloc is disabled; set INDEXING_WORKER_TRACEMALLOC=true to "
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:12:    ENABLE_OPENSEARCH_INDEXING_FOR_ONYX,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:83:        "name": "check-for-indexing",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:84:        "task": OnyxCeleryTask.CHECK_FOR_INDEXING,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:145:        "task": OnyxCeleryTask.CHECK_FOR_INDEX_ATTEMPT_CLEANUP,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:317:    ENABLE_OPENSEARCH_INDEXING_FOR_ONYX
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:339:    "check-for-indexing",
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:38:from onyx.db.document_set import delete_document_set_cc_pair_relationship__no_commit
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:41:    ConnectorCredentialPairStatus,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:42:    IndexingStatus,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:47:from onyx.db.index_attempt import delete_index_attempts, get_recent_attempts_for_cc_pair
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:93:            recent_index_attempts = get_recent_attempts_for_cc_pair(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:94:                cc_pair_id=redis_connector.cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:100:                recent_index_attempts
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:101:                and recent_index_attempts[0].status == IndexingStatus.IN_PROGRESS
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:102:                and recent_index_attempts[0].celery_task_id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:104:                app.control.revoke(recent_index_attempts[0].celery_task_id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:106:                    f"Revoked indexing task {recent_index_attempts[0].celery_task_id}."
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:109:            task_logger.exception("Exception while revoking indexing task")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:177:        # collect cc_pair_ids and note whether any are in DELETING status
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:178:        cc_pair_ids: list[int] = []
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:179:        has_deleting_cc_pair = False
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:181:            cc_pairs = get_connector_credential_pairs(db_session)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:182:            for cc_pair in cc_pairs:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:183:                cc_pair_ids.append(cc_pair.id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:184:                if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:185:                    has_deleting_cc_pair = True
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:187:        # Tenant-work-gating hook: mark only when at least one cc_pair is in
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:188:        # DELETING status. Marking on bare cc_pair existence would keep
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:189:        # nearly every tenant in the active set since most have cc_pairs
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:191:        if has_deleting_cc_pair:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:194:        # try running cleanup on the cc_pair_ids
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:195:        for cc_pair_id in cc_pair_ids:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:197:                redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:199:                    try_generate_document_cc_pair_cleanup_tasks(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:200:                        self.app, cc_pair_id, db_session, lock_beat, tenant_id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:260:def try_generate_document_cc_pair_cleanup_tasks(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:262:    cc_pair_id: int,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:271:    Will raise TaskDependencyError if dependent tasks such as indexing and pruning are
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:278:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:287:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:289:        cc_pair_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:291:    if not cc_pair:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:294:    if cc_pair.status != ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:299:            entity_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:314:        # do not proceed if connector indexing or connector pruning are running
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:317:            recent_index_attempts = get_recent_attempts_for_cc_pair(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:318:                cc_pair_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:324:                recent_index_attempts
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:325:                and recent_index_attempts[0].status == IndexingStatus.IN_PROGRESS
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:327:                inc_deletion_blocked(tenant_id, "indexing")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:329:                    "Connector deletion - Delayed (indexing in progress): "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:330:                    f"cc_pair={cc_pair_id} "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:340:                db_session, cc_pair_id, search_settings.id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:347:                    f"cc_pair={cc_pair_id} "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:354:                f"Connector deletion - Delayed (pruning in progress): cc_pair={cc_pair_id}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:360:                f"Connector deletion - Delayed (permissions in progress): cc_pair={cc_pair_id}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:368:            f"RedisConnectorDeletion.generate_tasks starting. cc_pair={cc_pair_id}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:379:                entity_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:400:            f"RedisConnectorDeletion.generate_tasks finished. cc_pair={cc_pair_id} tasks_generated={tasks_generated}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:417:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:418:    if cc_pair_id_str is None:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:419:        task_logger.warning(f"could not parse cc_pair_id from {fence_key}")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:422:    cc_pair_id = int(cc_pair_id_str)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:424:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:429:            f"Connector deletion - fence payload invalid: cc_pair={cc_pair_id}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:443:                entity_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:451:        cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:453:            cc_pair_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:457:        if not cc_pair:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:459:                f"Connector deletion - cc_pair not found: cc_pair={cc_pair_id}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:465:                db_session, cc_pair.connector_id, cc_pair.credential_id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:469:                # deletion was in progress. Likely a bug gating off pruning and indexing
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:474:                    f"cc_pair={cc_pair_id} "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:488:            delete_index_attempts(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:490:                cc_pair_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:496:                cc_pair_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:500:                cc_pair_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:504:            delete_document_set_cc_pair_relationship__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:506:                connector_id=cc_pair.connector_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:507:                credential_id=cc_pair.credential_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:513:                "delete_user_group_cc_pair_relationship__no_commit",
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:517:                cc_pair_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:525:            # Store IDs before potentially expiring cc_pair
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:526:            connector_id_to_delete = cc_pair.connector_id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:527:            credential_id_to_delete = cc_pair.credential_id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:528:            source = cc_pair.connector.source
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:541:            # Expire the cc_pair to ensure SQLAlchemy doesn't try to manage its state
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:542:            # related to the deleted DocumentByConnectorCredentialPair during commit
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:543:            db_session.expire(cc_pair)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:551:            # Join rows cascade off the cc_pair; drop nodes no other connector still owns.
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:583:                                f"cc_pair={cc_pair_id}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:586:                    f"Connector deletion hierarchy cleanup: cc_pair={cc_pair_id} "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:593:                entity_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:609:            add_deletion_failure_message(db_session, cc_pair_id, error_message)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:613:                entity_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:621:                f"cc_pair={cc_pair_id} connector={connector_id_to_delete} credential={credential_id_to_delete}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:632:        f"cc_pair={cc_pair_id} "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:687:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:688:    This can happen if the indexing worker hard crashes or is terminated.
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:699:    2.2. The indexing watchdog checks the spawned task.
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:715:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:716:    if cc_pair_id_str is None:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:722:    cc_pair_id = int(cc_pair_id_str)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:724:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:739:            f"cc_pair={cc_pair_id} "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:799:        f"cc_pair={cc_pair_id} "
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:14:from onyx.db.enums import ConnectorCredentialPairStatus
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:15:from onyx.db.index_attempt import mark_attempt_failed
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:16:from onyx.db.indexing_coordination import IndexingCoordination
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:17:from onyx.db.models import ConnectorCredentialPair, SearchSettings
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:23:    cc_pair: ConnectorCredentialPair,
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:30:    """Checks for any conditions that should block the indexing task from being
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:34:    is used to trigger indexing immediately.
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:41:    # we need to serialize any attempt to trigger indexing since it can be triggered
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:44:        DANSWER_REDIS_FUNCTION_LOCK_PREFIX + "try_creating_indexing_task",
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:52:    index_attempt_id = None
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:55:        db_session.refresh(cc_pair)
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:56:        if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:60:        custom_task_id = f"docfetching_{cc_pair.id}_{search_settings.id}_{uuid4()}"
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:64:        index_attempt_id = IndexingCoordination.try_create_index_attempt(
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:66:            cc_pair_id=cc_pair.id,
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:72:        if index_attempt_id is None:
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:73:            # Another indexing attempt is already running
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:76:        # Use higher priority for first-time indexing to ensure new connectors
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:77:        # get processed before re-indexing of existing connectors
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:78:        has_successful_attempt = cc_pair.last_successful_index_time is not None
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:89:                index_attempt_id=index_attempt_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:90:                cc_pair_id=cc_pair.id,
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:103:            f"cc_pair={cc_pair.id} "
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:105:            f"attempt_id={index_attempt_id} "
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:109:        return index_attempt_id
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:113:            f"try_creating_indexing_task - Unexpected exception: cc_pair={cc_pair.id} search_settings={search_settings.id}"
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:117:        if index_attempt_id is not None:
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:118:            mark_attempt_failed(index_attempt_id, db_session)
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:125:    return index_attempt_id
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:23:from onyx.background.celery.tasks.docprocessing.tasks import ConnectorIndexingLogBuilder
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:24:from onyx.background.celery.tasks.docprocessing.utils import IndexingCallback
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:27:    IndexingWatchdogTerminalStatus,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:30:from onyx.background.indexing.job_client import (
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:35:from onyx.background.indexing.run_docfetching import run_docfetching_entrypoint
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:36:from onyx.configs.app_configs import INDEXING_WORKER_MEMORY_LIMIT_MB
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:38:    CELERY_INDEXING_WATCHDOG_CONNECTOR_TIMEOUT,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:39:    CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:45:from onyx.db.enums import IndexingStatus
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:46:from onyx.db.index_attempt import (
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:47:    get_index_attempt,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:52:from onyx.db.indexing_coordination import IndexingCoordination
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:54:from onyx.server.metrics.connector_health_metrics import on_index_attempt_status_change
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:63:def _verify_indexing_attempt(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:64:    index_attempt_id: int,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:65:    cc_pair_id: int,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:69:    Verify that the indexing attempt exists and is in the correct state.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:73:        attempt = get_index_attempt(db_session, index_attempt_id)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:77:                f"docfetching_task - IndexAttempt not found: attempt_id={index_attempt_id}",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:78:                code=IndexingWatchdogTerminalStatus.FENCE_NOT_FOUND.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:81:        if attempt.connector_credential_pair_id != cc_pair_id:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:83:                f"docfetching_task - CC pair mismatch: expected={cc_pair_id} actual={attempt.connector_credential_pair_id}",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:84:                code=IndexingWatchdogTerminalStatus.FENCE_MISMATCH.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:90:                code=IndexingWatchdogTerminalStatus.FENCE_MISMATCH.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:94:            IndexingStatus.NOT_STARTED,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:95:            IndexingStatus.IN_PROGRESS,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:98:                f"docfetching_task - Invalid attempt status: attempt_id={index_attempt_id} status={attempt.status}",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:99:                code=IndexingWatchdogTerminalStatus.FENCE_MISMATCH.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:103:        if IndexingCoordination.check_cancellation_requested(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:104:            db_session, index_attempt_id
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:107:                f"docfetching_task - Cancellation requested: attempt_id={index_attempt_id}",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:108:                code=IndexingWatchdogTerminalStatus.BLOCKED_BY_STOP_SIGNAL.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:112:        "docfetching_task - IndexAttempt verified: attempt_id=%s cc_pair=%s search_settings=%s",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:113:        index_attempt_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:114:        cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:121:    index_attempt_id: int,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:122:    cc_pair_id: int,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:129:    some stuff, but basically it just calls run_indexing_entrypoint.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:133:    This will cause the primary worker to abort the indexing attempt and clean up.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:136:    # Start heartbeat for this indexing attempt
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:137:    heartbeat_thread, stop_event = start_heartbeat(index_attempt_id)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:139:    memory_observer = start_memory_observer(index_attempt_id)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:142:            app, index_attempt_id, cc_pair_id, search_settings_id, is_ee, tenant_id
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:151:    index_attempt_id: int,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:152:    cc_pair_id: int,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:157:    # Since connector_indexing_proxy_task spawns a new process using this function as
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:167:        "Indexing spawned task starting: attempt=%s tenant=%s cc_pair=%s search_settings=%s",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:168:        index_attempt_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:170:        cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:174:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:179:            f"Indexing will not start because connector deletion is in progress: "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:180:            f"attempt={index_attempt_id} "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:181:            f"cc_pair={cc_pair_id} "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:183:            code=IndexingWatchdogTerminalStatus.BLOCKED_BY_DELETION.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:188:            f"Indexing will not start because a connector stop signal was detected: "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:189:            f"attempt={index_attempt_id} "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:190:            f"cc_pair={cc_pair_id} "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:192:            code=IndexingWatchdogTerminalStatus.BLOCKED_BY_STOP_SIGNAL.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:195:    # Verify the indexing attempt exists and is valid
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:197:    _verify_indexing_attempt(index_attempt_id, cc_pair_id, search_settings_id)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:201:            attempt = get_index_attempt(db_session, index_attempt_id)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:204:                    f"Index attempt not found: index_attempt={index_attempt_id}",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:205:                    code=IndexingWatchdogTerminalStatus.INDEX_ATTEMPT_MISMATCH.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:208:            cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:210:                cc_pair_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:213:            if not cc_pair:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:215:                    f"cc_pair not found: cc_pair={cc_pair_id}",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:216:                    code=IndexingWatchdogTerminalStatus.INDEX_ATTEMPT_MISMATCH.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:220:        callback = IndexingCallback(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:225:            "Indexing spawned task running entrypoint: attempt=%s tenant=%s cc_pair=%s search_settings=%s",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:226:            index_attempt_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:228:            cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:235:            index_attempt_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:237:            cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:244:            f"Indexing task failed: attempt={index_attempt_id} "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:246:            f"cc_pair={cc_pair_id} "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:248:            code=IndexingWatchdogTerminalStatus.CONNECTOR_VALIDATION_ERROR.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:253:            "Indexing spawned task failed: attempt=%s tenant=%s cc_pair=%s search_settings=%s",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:254:            index_attempt_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:256:            cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:271:        "Indexing spawned task finished: attempt=%s cc_pair=%s search_settings=%s",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:272:        index_attempt_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:273:        cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:284:    index_attempt_id: int,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:285:    log_builder: ConnectorIndexingLogBuilder,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:294:        result.status = IndexingWatchdogTerminalStatus.SUCCEEDED
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:304:        index_attempt = get_index_attempt(db_session, index_attempt_id)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:305:        if index_attempt and index_attempt.total_batches is not None:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:309:        result.status = IndexingWatchdogTerminalStatus.SUCCEEDED
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:312:                "Indexing watchdog - spawned task has non-zero exit code but completion signal is OK. Continuing...",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:318:            result.status = IndexingWatchdogTerminalStatus.from_code(result.exit_code)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:334:    index_attempt_id: int,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:335:    cc_pair_id: int,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:340:    This task is the entrypoint for the full indexing pipeline, which is composed of two tasks:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:342:    This task is spawned by "try_creating_indexing_task" which is called in the "check_for_indexing" task.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:347:    1)  determines parameters of the indexing attempt (which connector indexing function to run,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:360:    6) update document and indexing metadata in postgres
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:366:    - docfetching proxy tasks are spawned by check_for_indexing. The proxy then runs the docfetching_task wrapped in a watchdog.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:375:    How we deal with failures/ partial indexing:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:381:    - Heartbeat spawned in docfetching and docprocessing is how check_for_indexing monitors liveliness
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:410:        cc_pair_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:412:        index_attempt_id=index_attempt_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:415:    log_builder = ConnectorIndexingLogBuilder(ctx)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:419:            "Indexing watchdog - starting",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:433:        index_attempt_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:434:        cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:441:        result.status = IndexingWatchdogTerminalStatus.SPAWN_FAILED
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:444:                "Indexing watchdog - finished",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:455:            result.status = IndexingWatchdogTerminalStatus.SPAWN_NOT_ALIVE
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:458:                    "Indexing watchdog - finished",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:474:            "Indexing watchdog - spawn succeeded",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:487:            index_attempt = get_index_attempt(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:489:                index_attempt_id=index_attempt_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:490:                eager_load_cc_pair=True,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:492:            if not index_attempt:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:496:                index_attempt.connector_credential_pair.connector.source.value
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:499:            cc_pair = index_attempt.connector_credential_pair
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:500:            on_index_attempt_status_change(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:503:                cc_pair_id=cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:504:                connector_name=cc_pair.connector.name or f"cc_pair_{cc_pair_id}",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:518:                    IndexingWatchdogTerminalStatus.TERMINATED_BY_WORKER_SHUTDOWN
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:522:                        attempt = get_index_attempt(db_session, index_attempt_id)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:525:                                index_attempt_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:527:                                "Indexing worker shutting down (deploy or "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:534:                            "Indexing watchdog - transient exception marking index "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:540:                        CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:545:                            "Indexing watchdog - exception while terminating "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:557:                        job, result.connector_source, index_attempt_id, log_builder
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:562:                            "Indexing watchdog - spawned task exceptioned"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:577:                        "indexing_worker",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:579:                            "cc_pair_id": cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:581:                            "index_attempt_id": index_attempt_id,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:591:                if INDEXING_WORKER_MEMORY_LIMIT_MB > 0:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:599:                    if rss_mb is not None and rss_mb > INDEXING_WORKER_MEMORY_LIMIT_MB:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:602:                                "Indexing watchdog - memory limit exceeded; "
```
Static evidence shows background/indexing orchestration code connecting source
acquisition to downstream document processing and indexing.
## Document Processing and Chunking
Evidence lines: 249
```text
HEAD:backend/onyx/background/README.md:96:- Docprocessing retrieves batches, runs the indexing pipeline (chunking, embedding), and indexes into the Document Index
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/tasks.py:86:    The first time we see no continuation token map and non-zero chunks
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/tasks.py:182:            continuation_token_map, total_chunks_migrated = get_vespa_visit_state(
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/tasks.py:297:                    continuation_token_map, total_chunks_migrated = (
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:7:from onyx.document_index.opensearch.schema import DocumentChunk
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:188:) -> tuple[list[DocumentChunk], list[dict[str, Any]]]:
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:189:    result: list[DocumentChunk] = []
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:307:            opensearch_chunk = DocumentChunk(
HEAD:backend/onyx/chat/llm_step.py:1295:                    citation_processor.process_token(content_chunk)
HEAD:backend/onyx/configs/app_configs.py:59:BLURB_SIZE = 128  # Number Encoder Tokens included in the chunk blurb
HEAD:backend/onyx/configs/app_configs.py:1501:# Finer grained chunking for more detail retention
HEAD:backend/onyx/configs/app_configs.py:1502:# Slightly larger since the sentence aware split is a max cutoff so most minichunks will be under MINI_CHUNK_SIZE
HEAD:backend/onyx/configs/app_configs.py:1503:# tokens. But we need it to be at least as big as 1/4th chunk size to avoid having a tiny mini-chunk at the end
HEAD:backend/onyx/configs/app_configs.py:1504:MINI_CHUNK_SIZE = 150
HEAD:backend/onyx/configs/constants.py:54:# For chunking/processing chunks
HEAD:backend/onyx/connectors/blob/connector.py:57:DOWNLOAD_CHUNK_SIZE = 1024 * 1024
HEAD:backend/onyx/connectors/blob/connector.py:280:        chunk_size = min(
HEAD:backend/onyx/connectors/blob/connector.py:281:            DOWNLOAD_CHUNK_SIZE, self.size_threshold + SIZE_THRESHOLD_BUFFER
HEAD:backend/onyx/connectors/blob/connector.py:284:        for chunk in body.iter_chunks(chunk_size=chunk_size):
HEAD:backend/onyx/connectors/box/connector.py:71:_DOWNLOAD_CHUNK_SIZE = 1024 * 1024
HEAD:backend/onyx/connectors/box/connector.py:386:            while chunk := stream.read(_DOWNLOAD_CHUNK_SIZE):
HEAD:backend/onyx/connectors/egnyte/connector.py:323:                for chunk in response.iter_content(chunk_size=8192):
HEAD:backend/onyx/connectors/fireflies/connector.py:61:# Onyx's content-hash check skips re-chunking/re-embedding anything already indexed.
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:228:CHUNK_SIZE_BUFFER = 64  # extra bytes past the limit to read
HEAD:backend/onyx/connectors/google_drive/doc_conversion.py:307:        response_bytes, request, chunksize=size_threshold + CHUNK_SIZE_BUFFER
HEAD:backend/onyx/connectors/google_drive/section_extraction.py:85:_DOCS_FETCH_CHUNK_SIZE = 1024 * 1024
HEAD:backend/onyx/connectors/google_drive/section_extraction.py:105:        for chunk in response.iter_content(chunk_size=_DOCS_FETCH_CHUNK_SIZE):
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:89:STREAM_CHUNK_SIZE = 64 * 1024
HEAD:backend/onyx/connectors/microsoft_utils/drive_items.py:391:                for chunk in resp.iter_content(STREAM_CHUNK_SIZE):
HEAD:backend/onyx/db/_deprecated/pg_file_store.py:11:from onyx.file_store.constants import MAX_IN_MEMORY_SIZE, STANDARD_CHUNK_SIZE
HEAD:backend/onyx/db/_deprecated/pg_file_store.py:46:            chunk = content.read(STANDARD_CHUNK_SIZE)
HEAD:backend/onyx/db/_deprecated/pg_file_store.py:99:                chunk = large_object.read(STANDARD_CHUNK_SIZE)
HEAD:backend/onyx/db/chunk.py:28:        chunk_document_id = f"{data.document_id}__{chunk_in_doc_id}"
HEAD:backend/onyx/db/chunk.py:32:                ChunkStats.id == chunk_document_id,
HEAD:backend/onyx/db/index_attempt_metrics_models.py:44:    CHUNKING = "CHUNKING"
HEAD:backend/onyx/db/index_attempt_metrics_models.py:93:    IndexAttemptStage.CHUNKING: StageScope.BATCH_LEVEL,
HEAD:backend/onyx/db/opensearch_migration.py:257:        Tuple of (continuation_token_map, total_chunks_migrated).
HEAD:backend/onyx/db/opensearch_migration.py:273:    return continuation_token_map, record.total_chunks_migrated
HEAD:backend/onyx/document_index/interfaces_new.py:13:from onyx.document_index.opensearch.constants import DEFAULT_MAX_CHUNK_SIZE
HEAD:backend/onyx/document_index/interfaces_new.py:91:    # A given document can have multiple chunking strategies.
HEAD:backend/onyx/document_index/interfaces_new.py:92:    max_chunk_size: int = DEFAULT_MAX_CHUNK_SIZE
HEAD:backend/onyx/document_index/interfaces_new.py:349:        the chunking does not introduce overlaps between the chunks. If there
HEAD:backend/onyx/document_index/opensearch/client.py:37:    DEFAULT_MAX_CHUNK_SIZE,
HEAD:backend/onyx/document_index/opensearch/client.py:45:    MAX_CHUNK_SIZE_FIELD_NAME,
HEAD:backend/onyx/document_index/opensearch/client.py:47:    DocumentChunk,
HEAD:backend/onyx/document_index/opensearch/client.py:48:    DocumentChunkWithoutVectors,
HEAD:backend/onyx/document_index/opensearch/client.py:544:    schema when it returns a DocumentChunk. Make the class, or at least the
HEAD:backend/onyx/document_index/opensearch/client.py:906:        document: DocumentChunk,
HEAD:backend/onyx/document_index/opensearch/client.py:936:            max_chunk_size=document.max_chunk_size,
HEAD:backend/onyx/document_index/opensearch/client.py:986:        documents: list[DocumentChunk],
HEAD:backend/onyx/document_index/opensearch/client.py:1039:                max_chunk_size=document.max_chunk_size,
HEAD:backend/onyx/document_index/opensearch/client.py:1522:    def get_document(self, document_chunk_id: str) -> DocumentChunk:
HEAD:backend/onyx/document_index/opensearch/client.py:1560:        return DocumentChunk.model_validate(document_chunk_source)
HEAD:backend/onyx/document_index/opensearch/client.py:1568:    ) -> list[SearchHit[DocumentChunkWithoutVectors]]:
HEAD:backend/onyx/document_index/opensearch/client.py:1636:        search_hits: list[SearchHit[DocumentChunkWithoutVectors]] = []
HEAD:backend/onyx/document_index/opensearch/client.py:1646:            search_hit = SearchHit[DocumentChunkWithoutVectors](
HEAD:backend/onyx/document_index/opensearch/client.py:1647:                document_chunk=DocumentChunkWithoutVectors.model_validate(
HEAD:backend/onyx/document_index/opensearch/client.py:1805:    ) -> tuple[list[DocumentChunkWithoutVectors], list[object] | None, str]:
HEAD:backend/onyx/document_index/opensearch/client.py:1808:        Filters to regular chunks (max_chunk_size == DEFAULT_MAX_CHUNK_SIZE),
HEAD:backend/onyx/document_index/opensearch/client.py:1866:        chunks: list[DocumentChunkWithoutVectors] = []
HEAD:backend/onyx/document_index/opensearch/client.py:1874:            chunks.append(DocumentChunkWithoutVectors.model_validate(source))
HEAD:backend/onyx/document_index/opensearch/client.py:1887:    ) -> Iterator[list[DocumentChunkWithoutVectors]]:
HEAD:backend/onyx/document_index/opensearch/client.py:1947:                        {"term": {MAX_CHUNK_SIZE_FIELD_NAME: DEFAULT_MAX_CHUNK_SIZE}},
HEAD:backend/onyx/document_index/opensearch/constants.py:1:# Default value for the maximum number of tokens a chunk can hold, if none is
HEAD:backend/onyx/document_index/opensearch/constants.py:6:DEFAULT_MAX_CHUNK_SIZE = 512
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:57:    DocumentChunk,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:58:    DocumentChunkWithoutVectors,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:134:    chunk: DocumentChunkWithoutVectors,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:201:) -> DocumentChunk:
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:220:    return DocumentChunk(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:460:            chunk_batch: list[DocumentChunk] = [
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:632:            # TODO(andrei): Nit but consider if we can use DocumentChunk here so
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:759:            search_hits: list[SearchHit[DocumentChunkWithoutVectors]] = []
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:771:                max_chunk_size=chunk_request.max_chunk_size,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:828:        search_hits: list[SearchHit[DocumentChunkWithoutVectors]] = self._client.search(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:875:        search_hits: list[SearchHit[DocumentChunkWithoutVectors]] = self._client.search(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:919:        search_hits: list[SearchHit[DocumentChunkWithoutVectors]] = self._client.search(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:953:        search_hits: list[SearchHit[DocumentChunkWithoutVectors]] = self._client.search(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:971:        self, chunks: list[DocumentChunk], use_create_only: bool = False
HEAD:backend/onyx/document_index/opensearch/port_copy.py:25:from onyx.document_index.opensearch.schema import DocumentChunkWithoutVectors
HEAD:backend/onyx/document_index/opensearch/port_copy.py:46:    embedding tokenizer is always resolved (reproduces the chunker's metadata-tail skip);
HEAD:backend/onyx/document_index/opensearch/port_copy.py:99:    pages: Iterable[list[DocumentChunkWithoutVectors]]
HEAD:backend/onyx/document_index/opensearch/port_copy.py:109:        by_doc: dict[str, list[DocumentChunkWithoutVectors]] = defaultdict(list)
HEAD:backend/onyx/document_index/opensearch/port_copy.py:134:        # re-added one, whose forward-written chunks are unmarked. DocumentChunk is
HEAD:backend/onyx/document_index/opensearch/schema.py:24:    DEFAULT_MAX_CHUNK_SIZE,
HEAD:backend/onyx/document_index/opensearch/schema.py:60:MAX_CHUNK_SIZE_FIELD_NAME = "max_chunk_size"
HEAD:backend/onyx/document_index/opensearch/schema.py:81:    max_chunk_size: int = DEFAULT_MAX_CHUNK_SIZE,
HEAD:backend/onyx/document_index/opensearch/schema.py:91:    opensearch_doc_chunk_id_suffix: str = f"__{max_chunk_size}__{chunk_index}"
HEAD:backend/onyx/document_index/opensearch/schema.py:137:class DocumentChunkWithoutVectors(BaseModel):
HEAD:backend/onyx/document_index/opensearch/schema.py:153:    # The maximum number of tokens this chunk's content can hold. Previously
HEAD:backend/onyx/document_index/opensearch/schema.py:157:    max_chunk_size: int = DEFAULT_MAX_CHUNK_SIZE
HEAD:backend/onyx/document_index/opensearch/schema.py:217:            f"DocumentChunk(document_id={self.document_id}, chunk_index={self.chunk_index}, "
HEAD:backend/onyx/document_index/opensearch/schema.py:292:        DocumentChunk. This assumes the final serialized model excludes None
HEAD:backend/onyx/document_index/opensearch/schema.py:319:                    f"Bug: An existing TenantState object was supplied to the DocumentChunk model "
HEAD:backend/onyx/document_index/opensearch/schema.py:338:class DocumentChunk(DocumentChunkWithoutVectors):
HEAD:backend/onyx/document_index/opensearch/schema.py:352:            f"DocumentChunk(document_id={self.document_id}, chunk_index={self.chunk_index}, "
HEAD:backend/onyx/document_index/opensearch/schema.py:379:        DocumentChunk class above.
HEAD:backend/onyx/document_index/opensearch/schema.py:570:                # The maximum number of tokens this chunk's content can hold.
HEAD:backend/onyx/document_index/opensearch/schema.py:571:                MAX_CHUNK_SIZE_FIELD_NAME: {"type": "integer"},
HEAD:backend/onyx/document_index/opensearch/search.py:34:    MAX_CHUNK_SIZE_FIELD_NAME,
HEAD:backend/onyx/document_index/opensearch/search.py:183:        max_chunk_size: int,
HEAD:backend/onyx/document_index/opensearch/search.py:202:            max_chunk_size: Document chunks are categorized by the maximum
HEAD:backend/onyx/document_index/opensearch/search.py:231:            max_chunk_size=max_chunk_size,
HEAD:backend/onyx/document_index/opensearch/search.py:298:            max_chunk_size=None,
HEAD:backend/onyx/document_index/opensearch/search.py:884:        max_chunk_size: int | None = None,
HEAD:backend/onyx/document_index/opensearch/search.py:933:            max_chunk_size: The type of chunk to retrieve, specified by the
HEAD:backend/onyx/document_index/opensearch/search.py:936:                NOTE: See DocumentChunk.max_chunk_size.
HEAD:backend/onyx/document_index/opensearch/search.py:1359:        if max_chunk_size is not None:
HEAD:backend/onyx/document_index/opensearch/search.py:1361:                {"term": {MAX_CHUNK_SIZE_FIELD_NAME: {"value": max_chunk_size}}}
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:467:#     return [chunk["id"].split("::", 1)[-1] for chunk in document_chunks]
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1067:        raw_chunks, next_continuation_token_map = get_all_chunks_paginated(
HEAD:backend/onyx/file_store/constants.py:2:STANDARD_CHUNK_SIZE = 10 * 1024 * 1024  # 10MB chunks
HEAD:backend/onyx/file_store/file_store.py:446:            for chunk in response["Body"].iter_chunks(chunk_size=8 * 1024 * 1024):
HEAD:backend/onyx/file_store/postgres_file_store.py:45:STREAM_CHUNK_SIZE = 8 * 1024 * 1024  # 8 MB
HEAD:backend/onyx/file_store/postgres_file_store.py:78:        chunk = lobj.read(STREAM_CHUNK_SIZE)
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:121:    ) -> "DocumentChunkEnricher":
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:141:        enricher = DocumentChunkEnricher(
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:269:class DocumentChunkEnricher:
HEAD:backend/onyx/indexing/chunker.py:7:    MINI_CHUNK_SIZE,
HEAD:backend/onyx/indexing/chunker.py:17:from onyx.indexing.chunking import DocumentChunker, extract_blurb
HEAD:backend/onyx/indexing/chunker.py:32:# Tokens reserved per chunk for the contextual-RAG doc summary + chunk context.
HEAD:backend/onyx/indexing/chunker.py:139:        mini_chunk_size: int = MINI_CHUNK_SIZE,
HEAD:backend/onyx/indexing/chunker.py:143:        self.chunk_token_limit = chunk_token_limit
HEAD:backend/onyx/indexing/chunker.py:163:            chunk_size=blurb_size,
HEAD:backend/onyx/indexing/chunker.py:170:            chunk_size=chunk_token_limit,
HEAD:backend/onyx/indexing/chunker.py:178:                chunk_size=mini_chunk_size,
HEAD:backend/onyx/indexing/chunker.py:186:        self._document_chunker = DocumentChunker(
HEAD:backend/onyx/indexing/chunker.py:198:            logger.debug("Chunking %s", document.semantic_identifier)
HEAD:backend/onyx/indexing/chunker.py:222:        if metadata_tokens >= self.chunk_token_limit * MAX_METADATA_PERCENTAGE:
HEAD:backend/onyx/indexing/chunker.py:255:        if content_token_limit <= CHUNK_MIN_CONTENT:
HEAD:backend/onyx/indexing/chunker.py:263:        if content_token_limit <= CHUNK_MIN_CONTENT:
HEAD:backend/onyx/indexing/chunker.py:265:            content_token_limit = self.chunk_token_limit
HEAD:backend/onyx/indexing/chunking/__init__.py:1:from onyx.indexing.chunking.document_chunker import DocumentChunker
HEAD:backend/onyx/indexing/chunking/__init__.py:2:from onyx.indexing.chunking.section_chunker import extract_blurb
HEAD:backend/onyx/indexing/chunking/__init__.py:5:    "DocumentChunker",
HEAD:backend/onyx/indexing/chunking/document_chunker.py:9:from onyx.indexing.chunking.image_section_chunker import ImageChunker
HEAD:backend/onyx/indexing/chunking/document_chunker.py:10:from onyx.indexing.chunking.section_chunker import (
HEAD:backend/onyx/indexing/chunking/document_chunker.py:15:from onyx.indexing.chunking.tabular_section_chunker import TabularChunker
HEAD:backend/onyx/indexing/chunking/document_chunker.py:16:from onyx.indexing.chunking.text_section_chunker import TextChunker
HEAD:backend/onyx/indexing/chunking/document_chunker.py:25:class DocumentChunker:
HEAD:backend/onyx/indexing/chunking/document_chunker.py:28:    Drop-in replacement for `Chunker._chunk_document_with_sections`.
HEAD:backend/onyx/indexing/chunking/image_section_chunker.py:2:from onyx.indexing.chunking.section_chunker import (
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/__init__.py:1:from onyx.indexing.chunking.tabular_section_chunker.tabular_section_chunker import (
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/sheet_descriptor.py:1:from onyx.indexing.chunking.tabular_section_chunker.analysis import SheetAnalysis
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/sheet_descriptor.py:2:from onyx.indexing.chunking.tabular_section_chunker.util import label, pack_lines
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/tabular_section_chunker.py:9:from onyx.indexing.chunking.section_chunker import (
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/tabular_section_chunker.py:15:from onyx.indexing.chunking.tabular_section_chunker.analysis import (
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/tabular_section_chunker.py:19:from onyx.indexing.chunking.tabular_section_chunker.sheet_descriptor import (
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/tabular_section_chunker.py:22:from onyx.indexing.chunking.tabular_section_chunker.total_descriptor import (
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/tabular_section_chunker.py:156:    candidate_tokens = column_header_tokens + NEWLINE_TOKENS + chunk_tokens
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/tabular_section_chunker.py:163:        candidate_tokens = sheet_header_tokens + NEWLINE_TOKENS + chunk_tokens
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/tabular_section_chunker.py:168:    return [_TokenizedText(text=chunk, token_count=chunk_tokens)]
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/total_descriptor.py:3:from onyx.indexing.chunking.tabular_section_chunker.analysis import (
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/total_descriptor.py:7:from onyx.indexing.chunking.tabular_section_chunker.util import label, pack_lines
HEAD:backend/onyx/indexing/chunking/text_section_chunker.py:7:from onyx.indexing.chunking.section_chunker import (
HEAD:backend/onyx/indexing/embedder.py:125:        if they exist. If there is no space for it, it would have been thrown out at the chunking step.
HEAD:backend/onyx/indexing/indexing_pipeline.py:661:            # This is again verified later in the pipeline after chunking but at that point there should
HEAD:backend/onyx/indexing/indexing_pipeline.py:715:                        "Split the document into smaller parts to index it."
HEAD:backend/onyx/indexing/indexing_pipeline.py:958:    doc_tokens = tokenizer.encode(chunks_by_doc[0].source_document.get_text_content())
HEAD:backend/onyx/indexing/indexing_pipeline.py:1008:    doc_content = tokenizer_trim_middle(doc_tokens, trunc_doc_chunk_tokens, tokenizer)
HEAD:backend/onyx/indexing/indexing_pipeline.py:1108:        llm.config.max_input_tokens - prompt_tokens - chunk_token_limit
HEAD:backend/onyx/indexing/indexing_pipeline.py:1119:                chunks_by_doc, llm, tokenizer, trunc_doc_chunk_tokens, doc_tokens
HEAD:backend/onyx/indexing/indexing_pipeline.py:1463:    logger.debug("Starting chunking")
HEAD:backend/onyx/indexing/indexing_pipeline.py:1466:    with time_stage_if_set(IndexAttemptStage.CHUNKING, attempt_id):
HEAD:backend/onyx/indexing/indexing_pipeline.py:1485:                chunk_token_limit=chunker.chunk_token_limit * 2,
HEAD:backend/onyx/indexing/port_reembed.py:28:Only regular chunks are handled (the port reads `max_chunk_size ==
HEAD:backend/onyx/indexing/port_reembed.py:29:DEFAULT_MAX_CHUNK_SIZE`); writes are idempotent (create-only: re-creating an
HEAD:backend/onyx/indexing/port_reembed.py:53:    DocumentChunk,
HEAD:backend/onyx/indexing/port_reembed.py:54:    DocumentChunkWithoutVectors,
HEAD:backend/onyx/indexing/port_reembed.py:123:def rebuild_semantic_tail(chunk: DocumentChunkWithoutVectors) -> str:
HEAD:backend/onyx/indexing/port_reembed.py:136:    semantic_tail: str, max_chunk_size: int, tokenizer: BaseTokenizer
HEAD:backend/onyx/indexing/port_reembed.py:144:    tail differently and flip the threshold. `max_chunk_size` is the chunk budget (equal
HEAD:backend/onyx/indexing/port_reembed.py:145:    for both: ported chunks are all DEFAULT_MAX_CHUNK_SIZE)."""
HEAD:backend/onyx/indexing/port_reembed.py:149:    return metadata_tokens < max_chunk_size * MAX_METADATA_PERCENTAGE
HEAD:backend/onyx/indexing/port_reembed.py:153:    chunk: DocumentChunkWithoutVectors, present_tokenizer: BaseTokenizer
HEAD:backend/onyx/indexing/port_reembed.py:181:        semantic_tail, chunk.max_chunk_size, present_tokenizer
HEAD:backend/onyx/indexing/port_reembed.py:187:def _title_prefix(chunk: DocumentChunkWithoutVectors) -> str:
HEAD:backend/onyx/indexing/port_reembed.py:197:    chunk: DocumentChunkWithoutVectors, embed_input: str
HEAD:backend/onyx/indexing/port_reembed.py:238:    stored_chunks: list[DocumentChunkWithoutVectors],
HEAD:backend/onyx/indexing/port_reembed.py:269:    stored_chunks: list[DocumentChunkWithoutVectors],
HEAD:backend/onyx/indexing/port_reembed.py:274:) -> list[DocumentChunk]:
HEAD:backend/onyx/indexing/port_reembed.py:277:    Returns DocumentChunks ready to write to the FUTURE index. For MODEL_ONLY only
HEAD:backend/onyx/indexing/port_reembed.py:284:    each chunk independently, so the caller may split a document across calls.
HEAD:backend/onyx/indexing/port_reembed.py:304:        recover_embedding_input(chunk, present_tokenizer) for chunk in stored_chunks
HEAD:backend/onyx/indexing/port_reembed.py:315:        DocumentChunk(
HEAD:backend/onyx/indexing/port_reembed.py:324:def _bare_contents(stored_chunks: list[DocumentChunkWithoutVectors]) -> list[str]:
HEAD:backend/onyx/indexing/port_reembed.py:342:    stored_chunks: list[DocumentChunkWithoutVectors], bare_contents: list[str]
HEAD:backend/onyx/indexing/port_reembed.py:365:    chunk: DocumentChunkWithoutVectors, future_embedding_tokenizer: BaseTokenizer
HEAD:backend/onyx/indexing/port_reembed.py:373:        semantic_tail, chunk.max_chunk_size, future_embedding_tokenizer
HEAD:backend/onyx/indexing/port_reembed.py:380:    stored_chunks: list[DocumentChunkWithoutVectors],
HEAD:backend/onyx/indexing/port_reembed.py:383:) -> list[DocumentChunk]:
HEAD:backend/onyx/indexing/port_reembed.py:390:    pairs_by_doc: dict[str, list[tuple[DocumentChunkWithoutVectors, str]]] = (
HEAD:backend/onyx/indexing/port_reembed.py:446:                chunk_token_limit=ctx.chunk_token_limit,
HEAD:backend/onyx/indexing/port_reembed.py:453:    results: list[DocumentChunk] = []
HEAD:backend/onyx/indexing/port_reembed.py:463:            DocumentChunk(
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:233:                prompt_tokens=chunk.get("prompt_eval_count", 0),
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:234:                completion_tokens=chunk.get("eval_count", 0),
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:235:                total_tokens=chunk.get("prompt_eval_count", 0)
HEAD:backend/onyx/llm/utils.py:477:        num_input_tokens += num_input_chunks * (
HEAD:backend/onyx/llm/utils.py:485:        # A single MAX_CONTEXT_TOKENS worth of output is generated per chunk
HEAD:backend/onyx/llm/utils.py:486:        num_output_tokens += num_input_chunks * MAX_CONTEXT_TOKENS
HEAD:backend/onyx/natural_language_processing/utils.py:186:_ENCODE_CHUNK_SIZE = 500_000
HEAD:backend/onyx/natural_language_processing/utils.py:194:    """Count tokens, chunking the input to avoid tiktoken stack overflow.
HEAD:backend/onyx/natural_language_processing/utils.py:201:    if len(text) <= _ENCODE_CHUNK_SIZE:
HEAD:backend/onyx/natural_language_processing/utils.py:204:    for start in range(0, len(text), _ENCODE_CHUNK_SIZE):
HEAD:backend/onyx/natural_language_processing/utils.py:205:        total += len(tokenizer.encode(text[start : start + _ENCODE_CHUNK_SIZE]))
HEAD:backend/onyx/natural_language_processing/utils.py:229:    for start in range(0, len(text), _ENCODE_CHUNK_SIZE):
HEAD:backend/onyx/natural_language_processing/utils.py:230:        token_ids.extend(tokenizer.encode(text[start : start + _ENCODE_CHUNK_SIZE]))
HEAD:backend/onyx/natural_language_processing/utils.py:264:def tokenizer_trim_chunks(
HEAD:backend/onyx/natural_language_processing/utils.py:271:        new_content = tokenizer_trim_content(chunk.content, max_chunk_toks, tokenizer)
HEAD:backend/onyx/server/documents/document.py:104:        content=chunk_content, num_tokens=len(tokenizer_encode(chunk_content))
HEAD:backend/onyx/server/documents/models.py:288:        IndexAttemptStage.CHUNKING,
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:262:    chunk_size: int = 64 * 1024,
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:270:        chunk_size=chunk_size,
HEAD:backend/onyx/server/features/build/sandbox/docker/internal/exec_helpers.py:228:        for stream_type, frame in _iter_frames(sock, chunk_size=64 * 1024):
HEAD:backend/onyx/server/features/build/sandbox/docker/internal/exec_helpers.py:246:    chunk_size: int = 64 * 1024,
HEAD:backend/onyx/server/features/build/sandbox/docker/internal/exec_helpers.py:263:        for stream_type, frame in _iter_frames(sock, chunk_size=chunk_size):
HEAD:backend/onyx/server/features/build/sandbox/docker/internal/exec_helpers.py:283:    sock: socket.socket, *, chunk_size: int
HEAD:backend/onyx/server/features/build/sandbox/docker/internal/exec_helpers.py:294:            chunk = sock.recv(min(remaining, chunk_size))
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/manifest.py:45:_HASH_CHUNK_SIZE = 1024 * 1024
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/manifest.py:87:        while chunk := os.read(fd, _HASH_CHUNK_SIZE):
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/sidecar_client.py:37:_SIDECAR_CHUNK_SIZE = 8 * 1024 * 1024
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/sidecar_client.py:248:                        resp.iter_bytes(chunk_size=_SIDECAR_CHUNK_SIZE)
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/sidecar_client.py:267:            return iter(lambda: archive_file.read(_SIDECAR_CHUNK_SIZE), b"")
HEAD:backend/onyx/server/features/build/user_library/api.py:105:            f"(more than {file_cap}). Try splitting the document into smaller files.",
HEAD:backend/onyx/server/features/build/webapp_proxy.py:165:        async for chunk in response.aiter_bytes(chunk_size=8192):
HEAD:backend/onyx/server/manage/llm/api.py:1165:    - The per-token cost of the LLM used to generate the doc_summary and chunk_context
HEAD:backend/onyx/server/manage/voice/user_api.py:34:UPLOAD_READ_CHUNK_SIZE = 8192
HEAD:backend/onyx/server/manage/voice/user_api.py:79:    while chunk := await audio.read(UPLOAD_READ_CHUNK_SIZE):
HEAD:backend/onyx/server/manage/voice/websocket_api.py:365:    chunk_size = len(chunk)
HEAD:backend/onyx/server/manage/voice/websocket_api.py:368:    if chunk_size > WS_MAX_MESSAGE_SIZE:
HEAD:backend/onyx/server/manage/voice/websocket_api.py:370:            "Streaming transcription: message too large (%s bytes)", chunk_size
HEAD:backend/onyx/server/manage/voice/websocket_api.py:376:    if state.total_bytes + chunk_size > WS_MAX_TOTAL_BYTES:
HEAD:backend/onyx/server/manage/voice/websocket_api.py:379:            state.total_bytes + chunk_size,
HEAD:backend/onyx/server/manage/voice/websocket_api.py:387:    state.total_bytes += chunk_size
HEAD:backend/onyx/server/manage/voice/websocket_api.py:391:        chunk_size,
HEAD:backend/onyx/server/manage/voice/websocket_api.py:645:            chunk_size = len(message["bytes"])
HEAD:backend/onyx/server/manage/voice/websocket_api.py:648:            if chunk_size > WS_MAX_MESSAGE_SIZE:
HEAD:backend/onyx/server/manage/voice/websocket_api.py:650:                    "Chunked transcription: message too large (%s bytes)", chunk_size
HEAD:backend/onyx/server/manage/voice/websocket_api.py:658:            if total_bytes + chunk_size > WS_MAX_TOTAL_BYTES:
HEAD:backend/onyx/server/manage/voice/websocket_api.py:661:                    total_bytes + chunk_size,
HEAD:backend/onyx/server/manage/voice/websocket_api.py:669:            total_bytes += chunk_size
HEAD:backend/onyx/server/manage/voice/websocket_api.py:673:                chunk_size,
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:213:    # If max_chunks_per_section is specified, only count tokens for selected chunks
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:251:            section, token_counter, max_chunks_per_section
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:445:            search_settings: Pre-fetched SearchSettings for chunking config
HEAD:backend/onyx/utils/github.py:337:            for chunk in response.iter_content(chunk_size=64 * 1024):
HEAD:backend/onyx/utils/jsonriver/tokenize.py:208:    Tokenizer for chunk-based JSON parsing
HEAD:backend/onyx/voice/providers/openai.py:626:                async for chunk in response.iter_bytes(chunk_size=8192):
```
Chunking is a security-relevant transformation boundary because metadata,
document identity, ACL information and tenant identity must remain correctly
associated with derived chunks.
## Embedding Generation
Evidence lines: 550
```text
HEAD:backend/model_server/__main__.py:1:"""Process entry point for the model server (`python -m model_server`).
HEAD:backend/model_server/__main__.py:3:The `DISABLE_MODEL_SERVER` gate runs here, ahead of `model_server.main`'s heavy ML
HEAD:backend/model_server/__main__.py:10:from shared_configs.configs import DISABLE_MODEL_SERVER
HEAD:backend/model_server/__main__.py:16:    if DISABLE_MODEL_SERVER:
HEAD:backend/model_server/__main__.py:19:        logger.notice("DISABLE_MODEL_SERVER is set; skipping model server startup.")
HEAD:backend/model_server/__main__.py:23:    from model_server.main import run_server
HEAD:backend/model_server/encoders.py:7:from model_server.utils import simple_log_function_time
HEAD:backend/model_server/encoders.py:11:from shared_configs.model_server_models import Embedding, EmbedRequest, EmbedResponse
HEAD:backend/model_server/encoders.py:24:def get_embedding_model(
HEAD:backend/model_server/encoders.py:30:    pre-warms rotary caches once, and wraps encode() with a lock to avoid cache races.
HEAD:backend/model_server/encoders.py:44:            _ = st_model.encode(
HEAD:backend/model_server/encoders.py:49:                normalize_embeddings=False,
HEAD:backend/model_server/encoders.py:82:def _concurrent_embedding(
HEAD:backend/model_server/encoders.py:83:    texts: list[str], model: "SentenceTransformer", normalize_embeddings: bool
HEAD:backend/model_server/encoders.py:85:    """Synchronous wrapper for concurrent_embedding to use with run_in_executor."""
HEAD:backend/model_server/encoders.py:88:            return model.encode(texts, normalize_embeddings=normalize_embeddings)
HEAD:backend/model_server/encoders.py:92:            # concurrent embedding, hence we retry (the specific error is
HEAD:backend/model_server/encoders.py:96:    return model.encode(texts, normalize_embeddings=normalize_embeddings)
HEAD:backend/model_server/encoders.py:100:async def embed_text(
HEAD:backend/model_server/encoders.py:104:    normalize_embeddings: bool,
HEAD:backend/model_server/encoders.py:107:) -> list[Embedding]:
HEAD:backend/model_server/encoders.py:109:        logger.error("Empty strings provided for embedding")
HEAD:backend/model_server/encoders.py:110:        raise ValueError("Empty strings are not allowed for embedding.")
HEAD:backend/model_server/encoders.py:113:        logger.error("No texts provided for embedding")
HEAD:backend/model_server/encoders.py:114:        raise ValueError("No texts provided for embedding.")
HEAD:backend/model_server/encoders.py:127:            "Embedding %s texts with %s total characters with local model: %s",
HEAD:backend/model_server/encoders.py:135:        local_model = get_embedding_model(
HEAD:backend/model_server/encoders.py:138:        # Run CPU-bound embedding in a thread pool
HEAD:backend/model_server/encoders.py:139:        embeddings_vectors = await asyncio.get_event_loop().run_in_executor(
HEAD:backend/model_server/encoders.py:141:            lambda: _concurrent_embedding(
HEAD:backend/model_server/encoders.py:142:                prefixed_texts, local_model, normalize_embeddings
HEAD:backend/model_server/encoders.py:145:        embeddings = [
HEAD:backend/model_server/encoders.py:146:            embedding if isinstance(embedding, list) else embedding.tolist()
HEAD:backend/model_server/encoders.py:147:            for embedding in embeddings_vectors
HEAD:backend/model_server/encoders.py:159:            "event=embedding_model texts=%s chars=%s model=%s gpu=%s elapsed=%s",
HEAD:backend/model_server/encoders.py:167:        logger.error("Model name not specified for embedding")
HEAD:backend/model_server/encoders.py:168:        raise ValueError("Model name must be provided to run embeddings.")
HEAD:backend/model_server/encoders.py:170:    return embeddings
HEAD:backend/model_server/encoders.py:189:            f"Model server embedding endpoint should only be used for local models. "
HEAD:backend/model_server/encoders.py:197:        raise ValueError("Empty strings are not allowed for embedding.")
HEAD:backend/model_server/encoders.py:207:        embeddings = await embed_text(
HEAD:backend/model_server/encoders.py:211:            normalize_embeddings=embed_request.normalize_embeddings,
HEAD:backend/model_server/encoders.py:215:        return EmbedResponse(embeddings=embeddings)
HEAD:backend/model_server/encoders.py:223:            "Error during embedding process: provider=%s model=%s",
HEAD:backend/model_server/encoders.py:228:            status_code=500, detail=f"Error during embedding process: {e}"
HEAD:backend/model_server/legacy/custom_models.py:12:# from model_server.constants import MODEL_WARM_UP_STRING
HEAD:backend/model_server/legacy/custom_models.py:13:# from model_server.legacy.onyx_torch_model import ConnectorClassifier
HEAD:backend/model_server/legacy/custom_models.py:14:# from model_server.legacy.onyx_torch_model import HybridClassifier
HEAD:backend/model_server/legacy/custom_models.py:15:# from model_server.utils import simple_log_function_time
HEAD:backend/model_server/legacy/custom_models.py:22:# from shared_configs.model_server_models import IntentRequest
HEAD:backend/model_server/legacy/custom_models.py:23:# from shared_configs.model_server_models import IntentResponse
HEAD:backend/model_server/legacy/reranker.py:8:# from model_server.utils import simple_log_function_time
HEAD:backend/model_server/legacy/reranker.py:11:# from shared_configs.model_server_models import RerankRequest
HEAD:backend/model_server/legacy/reranker.py:12:# from shared_configs.model_server_models import RerankResponse
HEAD:backend/model_server/main.py:16:from model_server.ca_certs import configure_trusted_ca_bundle
HEAD:backend/model_server/main.py:17:from model_server.encoders import router as encoders_router
HEAD:backend/model_server/main.py:18:from model_server.management_endpoints import router as management_router
HEAD:backend/model_server/main.py:19:from model_server.utils import get_cgroup_cpu_limit, get_gpu_type
HEAD:backend/model_server/main.py:29:    MODEL_SERVER_PORT,
HEAD:backend/model_server/main.py:154:    # `--host 0.0.0.0`; MODEL_SERVER_HOST is a client-side address and must not
HEAD:backend/model_server/main.py:160:        str(MODEL_SERVER_PORT),
HEAD:backend/model_server/main.py:163:    uvicorn.run(app, host=host, port=MODEL_SERVER_PORT)
HEAD:backend/model_server/management_endpoints.py:3:from model_server.constants import GPUStatus
HEAD:backend/model_server/management_endpoints.py:4:from model_server.utils import get_gpu_type
HEAD:backend/model_server/utils.py:10:from model_server.constants import GPUStatus
HEAD:backend/onyx/auth/api_key.py:47:        return hashlib.sha256(api_key.encode("utf-8")).hexdigest()
HEAD:backend/onyx/auth/captcha.py:111:    digest = hashlib.sha256(token.encode("utf-8")).hexdigest()
HEAD:backend/onyx/auth/captcha.py:265:        f"onyx-captcha-cookie-v1::{USER_AUTH_SECRET}".encode("utf-8")
HEAD:backend/onyx/auth/captcha.py:274:        _cookie_signing_key(), str(expiry).encode("utf-8"), hashlib.sha256
HEAD:backend/onyx/auth/captcha.py:293:        _cookie_signing_key(), str(expiry).encode("utf-8"), hashlib.sha256
HEAD:backend/onyx/auth/email_utils.py:251:        encoded_image = base64.b64encode(image_data).decode()
HEAD:backend/onyx/auth/login_claims_capture.py:166:    if len(payload.encode("utf-8")) > _MAX_SNAPSHOT_BYTES:
HEAD:backend/onyx/auth/login_claims_capture.py:170:        if len(payload.encode("utf-8")) > _MAX_SNAPSHOT_BYTES:
HEAD:backend/onyx/auth/oauth_token_manager.py:68:    return urlunparse(parsed._replace(query=urlencode(query)))
HEAD:backend/onyx/auth/oauth_token_manager.py:113:        f"{params.authorization_url}{separator}{urlencode(query)}"
HEAD:backend/onyx/auth/pat.py:25:    return hashlib.sha256(token.encode("utf-8")).hexdigest()
HEAD:backend/onyx/auth/pkce.py:14:    digest = hashlib.sha256(code_verifier.encode("ascii")).digest()
HEAD:backend/onyx/auth/pkce.py:15:    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
HEAD:backend/onyx/auth/users.py:2561:    state_hash = hashlib.sha256(state.encode("utf-8")).hexdigest()
HEAD:backend/onyx/background/README.md:96:- Docprocessing retrieves batches, runs the indexing pipeline (chunking, embedding), and indexes into the Document Index
HEAD:backend/onyx/background/celery/celery_redis.py:92:    queue_marker = f'"{queue}"'.encode("utf-8")
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:140:    INDEXING_MODEL_SERVER_HOST,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:141:    INDEXING_MODEL_SERVER_PORT,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:614:                # NOTE: _run_indexing doesn't update connectors if the index attempt is the future embedding model
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:868:        EmbeddingModel,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:929:                    embedding_model = EmbeddingModel.from_db_model(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:931:                        server_host=INDEXING_MODEL_SERVER_HOST,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:932:                        server_port=INDEXING_MODEL_SERVER_PORT,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:937:                        embedding_model=embedding_model,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1034:                    # to prevent continued indexing retry attempts burning through embedding credits.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1035:                    # NOTE: only for Cloud, since most self-hosted users use self-hosted embedding
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1487:    the indexing pipeline (embedding + vector store indexing).
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1758:        # the slow embedding + Vespa work begins, returning the connection to the pool.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1796:            embedding_model = DefaultIndexingEmbedder.from_db_search_settings(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1827:        # Session is now closed; no connection held during embedding.
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1858:            embedder=embedding_model,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1986:        # NOTE: Thread-local event loops in embedding threads are cleaned up automatically
HEAD:backend/onyx/background/celery/tasks/docprocessing/utils.py:266:    # NOTE: during an embedding model switch over, the following logic
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/tasks.py:209:                embedding_dim=indexing_setting.final_embedding_dim,
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/tasks.py:210:                embedding_precision=indexing_setting.embedding_precision,
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:19:    EMBEDDINGS,
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:20:    FULL_CHUNK_EMBEDDING_KEY,
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:33:    TITLE_EMBEDDING,
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:46:    TITLE_EMBEDDING,
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:48:    EMBEDDINGS,
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:72:def _extract_content_vector(embeddings: Any) -> list[float]:
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:73:    """Extracts the full chunk embedding vector from Vespa's embeddings tensor.
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:75:    Vespa stores embeddings as a tensor<float>(t{},x[dim]) where 't' maps
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:76:    embedding names (like "full_chunk") to vectors. The API can return this in
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:86:        ValueError: If the embeddings format is not supported.
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:89:        The full chunk content embedding vector as a list of floats.
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:91:    if isinstance(embeddings, dict):
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:93:        full_chunk_embedding = embeddings.get(FULL_CHUNK_EMBEDDING_KEY)
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:94:        if isinstance(full_chunk_embedding, list):
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:97:            if not full_chunk_embedding:
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:98:                raise ValueError("Full chunk embedding is empty.")
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:99:            if isinstance(full_chunk_embedding[0], float):
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:100:                return full_chunk_embedding
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:103:        blocks = embeddings.get("blocks")
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:105:            full_chunk_embedding = blocks.get(FULL_CHUNK_EMBEDDING_KEY)
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:106:            if isinstance(full_chunk_embedding, list):
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:109:                if not full_chunk_embedding:
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:110:                    raise ValueError("Full chunk embedding is empty.")
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:111:                if isinstance(full_chunk_embedding[0], float):
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:112:                    return full_chunk_embedding
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:114:    raise ValueError(f"Unknown embedding format: {type(embeddings)}")
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:117:def _extract_title_vector(title_embedding: Any | None) -> list[float] | None:
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:118:    """Extract the title embedding vector.
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:120:    Returns None if no title embedding exists.
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:122:    Vespa returns title_embedding as tensor<float>(x[dim]) which can be in
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:132:        ValueError: If the title embedding format is not supported.
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:135:        The title embedding vector as a list of floats.
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:137:    if title_embedding is None:
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:141:    if isinstance(title_embedding, list):
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:144:        if not title_embedding:
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:146:        if isinstance(title_embedding[0], float):
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:147:            return title_embedding
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:150:    if isinstance(title_embedding, dict):
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:152:        values = title_embedding.get("values")
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:161:    raise ValueError(f"Unknown title embedding format: {type(title_embedding)}")
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:221:                vespa_chunk.get(TITLE_EMBEDDING)
HEAD:backend/onyx/background/celery/tasks/opensearch_migration/transformer.py:234:                vespa_chunk[EMBEDDINGS]
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:110:# burning embedding spend ~2880x/day.
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:291:    the file store, and marks the file as COMPLETED.  Skips embedding and
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:315:        token_count: int | None = len(encode(combined_text))
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:421:        embedding_model = DefaultIndexingEmbedder.from_db_search_settings(
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:435:                embedder=embedding_model,
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:482:    """Index one user file into the secondary (reindex-port target) index, re-embedding with
HEAD:backend/onyx/background/indexing/checkpointing_utils.py:37:        content=BytesIO(checkpoint.model_dump_json().encode()),
HEAD:backend/onyx/cache/postgres_backend.py:46:    return str(value).encode()
HEAD:backend/onyx/cache/postgres_backend.py:344:                        return (key.encode(), value)
HEAD:backend/onyx/cache/postgres_backend.py:354:            f"{self._tenant_id}:{name}".encode(), usedforsecurity=False
HEAD:backend/onyx/chat/compression.py:469:            summary_token_count = len(tokenizer.encode(summary_text))
HEAD:backend/onyx/chat/incognito_context.py:156:    payload = f"{context.version + 1}:".encode() + body
HEAD:backend/onyx/chat/incognito_context.py:163:            str(context.version).encode(),
HEAD:backend/onyx/chat/incognito_context.py:165:            str(INCOGNITO_CONTEXT_TTL_SECONDS).encode(),
HEAD:backend/onyx/chat/process_message.py:793:        user_token_count = len(default_tokenizer.encode(message_text))
HEAD:backend/onyx/chat/process_message.py:1462:                        len(get_tokenizer(None, None).encode(partial_answer))
HEAD:backend/onyx/chat/save_chat.py:87:            tool_call_tokens = len(default_tokenizer.encode(arguments_json_str))
HEAD:backend/onyx/chat/save_chat.py:239:            default_tokenizer.encode(sanitized_message_text)
HEAD:backend/onyx/chat/stream_buffer.py:112:        payload = zlib.compress("".join(self._pending).encode("utf-8"))
HEAD:backend/onyx/configs/app_configs.py:99:# Cache query embeddings in the configured cache backend so identical queries
HEAD:backend/onyx/configs/app_configs.py:100:# (across users / agentic sub-queries) don't re-hit the embedding provider.
HEAD:backend/onyx/configs/app_configs.py:101:QUERY_EMBEDDING_CACHE_ENABLED = (
HEAD:backend/onyx/configs/app_configs.py:102:    os.environ.get("QUERY_EMBEDDING_CACHE_ENABLED", "true").lower() == "true"
HEAD:backend/onyx/configs/app_configs.py:105:    QUERY_EMBEDDING_CACHE_TTL_S := int(
HEAD:backend/onyx/configs/app_configs.py:106:        os.environ.get("QUERY_EMBEDDING_CACHE_TTL_S", "900")
HEAD:backend/onyx/configs/app_configs.py:108:) > 0, "QUERY_EMBEDDING_CACHE_TTL_S must be positive."
HEAD:backend/onyx/configs/app_configs.py:1489:# When swapping to a new embedding model, a secondary index is created in the background, to conserve
HEAD:backend/onyx/configs/app_configs.py:1526:# Enable multi-threaded embedding model calls for parallel processing
HEAD:backend/onyx/configs/app_configs.py:1527:# Note: only applies for API-based embedding models
HEAD:backend/onyx/configs/app_configs.py:1528:INDEXING_EMBEDDING_MODEL_NUM_THREADS = int(
HEAD:backend/onyx/configs/app_configs.py:1529:    os.environ.get("INDEXING_EMBEDDING_MODEL_NUM_THREADS") or 8
HEAD:backend/onyx/configs/app_configs.py:1621:# Average summary embeddings for contextual rag (not yet implemented)
HEAD:backend/onyx/configs/app_configs.py:1622:AVERAGE_SUMMARY_EMBEDDINGS = (
HEAD:backend/onyx/configs/app_configs.py:1623:    os.environ.get("AVERAGE_SUMMARY_EMBEDDINGS", "false").lower() == "true"
HEAD:backend/onyx/configs/embedding_configs.py:3:from onyx.db.enums import EmbeddingPrecision
HEAD:backend/onyx/configs/embedding_configs.py:6:class _BaseEmbeddingModel(BaseModel):
HEAD:backend/onyx/configs/embedding_configs.py:7:    """Private model for defining base embedding model configurations."""
HEAD:backend/onyx/configs/embedding_configs.py:14:class SupportedEmbeddingModel(BaseModel):
HEAD:backend/onyx/configs/embedding_configs.py:18:    embedding_precision: EmbeddingPrecision
HEAD:backend/onyx/configs/embedding_configs.py:21:# Base embedding model configurations (without precision)
HEAD:backend/onyx/configs/embedding_configs.py:22:_BASE_EMBEDDING_MODELS = [
HEAD:backend/onyx/configs/embedding_configs.py:24:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:29:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:34:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:39:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:44:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:49:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:50:        name="openai/text-embedding-3-large",
HEAD:backend/onyx/configs/embedding_configs.py:52:        index_name="danswer_chunk_openai_text_embedding_3_large",
HEAD:backend/onyx/configs/embedding_configs.py:54:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:55:        name="openai/text-embedding-3-large",
HEAD:backend/onyx/configs/embedding_configs.py:57:        index_name="danswer_chunk_text_embedding_3_large",
HEAD:backend/onyx/configs/embedding_configs.py:59:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:60:        name="openai/text-embedding-3-small",
HEAD:backend/onyx/configs/embedding_configs.py:62:        index_name="danswer_chunk_openai_text_embedding_3_small",
HEAD:backend/onyx/configs/embedding_configs.py:64:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:65:        name="openai/text-embedding-3-small",
HEAD:backend/onyx/configs/embedding_configs.py:67:        index_name="danswer_chunk_text_embedding_3_small",
HEAD:backend/onyx/configs/embedding_configs.py:69:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:70:        name="google/gemini-embedding-001",
HEAD:backend/onyx/configs/embedding_configs.py:72:        index_name="danswer_chunk_gemini_embedding_001",
HEAD:backend/onyx/configs/embedding_configs.py:74:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:75:        name="google/text-embedding-005",
HEAD:backend/onyx/configs/embedding_configs.py:77:        index_name="danswer_chunk_text_embedding_005",
HEAD:backend/onyx/configs/embedding_configs.py:79:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:80:        name="google/gemini-embedding-2-preview",
HEAD:backend/onyx/configs/embedding_configs.py:82:        index_name="danswer_chunk_gemini_embedding_2_preview",
HEAD:backend/onyx/configs/embedding_configs.py:84:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:85:        name="google/gemini-embedding-2",
HEAD:backend/onyx/configs/embedding_configs.py:87:        index_name="danswer_chunk_gemini_embedding_2",
HEAD:backend/onyx/configs/embedding_configs.py:89:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:94:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:99:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:104:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:110:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:113:        index_name="danswer_chunk_nomic_ai_nomic_embed_text_v1",
HEAD:backend/onyx/configs/embedding_configs.py:115:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:118:        index_name="danswer_chunk_nomic_embed_text_v1",
HEAD:backend/onyx/configs/embedding_configs.py:120:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:125:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:130:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:135:    _BaseEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:143:SUPPORTED_EMBEDDING_MODELS = [
HEAD:backend/onyx/configs/embedding_configs.py:146:        SupportedEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:150:            embedding_precision=EmbeddingPrecision.BFLOAT16,
HEAD:backend/onyx/configs/embedding_configs.py:152:        for model in _BASE_EMBEDDING_MODELS
HEAD:backend/onyx/configs/embedding_configs.py:158:        SupportedEmbeddingModel(
HEAD:backend/onyx/configs/embedding_configs.py:162:            embedding_precision=EmbeddingPrecision.FLOAT,
HEAD:backend/onyx/configs/embedding_configs.py:164:        for model in _BASE_EMBEDDING_MODELS
HEAD:backend/onyx/configs/model_configs.py:7:# Embedding/Reranking Model Configs
HEAD:backend/onyx/configs/model_configs.py:16:# IDEALLY, YOU SHOULD CHANGE EMBEDDING MODELS VIA THE UI
HEAD:backend/onyx/configs/model_configs.py:21:DOC_EMBEDDING_DIM = int(os.environ.get("DOC_EMBEDDING_DIM") or 768)
HEAD:backend/onyx/configs/model_configs.py:22:NORMALIZE_EMBEDDINGS = (
HEAD:backend/onyx/configs/model_configs.py:23:    os.environ.get("NORMALIZE_EMBEDDINGS") or "true"
HEAD:backend/onyx/configs/model_configs.py:28:OLD_DEFAULT_MODEL_DOC_EMBEDDING_DIM = 384
HEAD:backend/onyx/configs/model_configs.py:29:OLD_DEFAULT_MODEL_NORMALIZE_EMBEDDINGS = False
HEAD:backend/onyx/configs/model_configs.py:40:# User's set embedding batch size overrides the default encoding batch sizes
HEAD:backend/onyx/configs/model_configs.py:41:EMBEDDING_BATCH_SIZE = int(os.environ.get("EMBEDDING_BATCH_SIZE") or 0) or None
HEAD:backend/onyx/configs/model_configs.py:43:BATCH_SIZE_ENCODE_CHUNKS = EMBEDDING_BATCH_SIZE or 8
HEAD:backend/onyx/configs/model_configs.py:45:BATCH_SIZE_ENCODE_CHUNKS_FOR_API_EMBEDDING_SERVICES = EMBEDDING_BATCH_SIZE or 512
HEAD:backend/onyx/connectors/braintrust/connector.py:303:        return self.raw_file_callback(io.BytesIO(csv_text.encode("utf-8")), "text/csv")
HEAD:backend/onyx/connectors/capability_checks/models.py:153:    return hashlib.sha256(canonical.encode()).hexdigest()
HEAD:backend/onyx/connectors/cross_connector_utils/tabular_section_utils.py:77:    csv_file_id = stage(io.BytesIO(text.encode("utf-8")), "text/csv")
HEAD:backend/onyx/connectors/file/connector.py:217:                extraction_result.text_content.encode("utf-8", errors="replace")
HEAD:backend/onyx/connectors/fireflies/connector.py:61:# Onyx's content-hash check skips re-chunking/re-embedding anything already indexed.
HEAD:backend/onyx/connectors/freshdesk/connector.py:113:        # Skip fields that aren't useful for embedding
HEAD:backend/onyx/connectors/gong/connector.py:445:        self.auth_token_basic = base64.b64encode(combined.encode("utf-8")).decode(
HEAD:backend/onyx/connectors/highspot/client.py:95:        encoded_auth = base64.b64encode(auth.encode()).decode()
HEAD:backend/onyx/connectors/jira/connector.py:423:    if len(ticket_content.encode("utf-8")) > JIRA_CONNECTOR_MAX_TICKET_SIZE:
HEAD:backend/onyx/connectors/lumapps/client.py:67:        raw = f"{self.application_id}:{self.api_key}".encode()
HEAD:backend/onyx/connectors/lumapps/client.py:68:        return "Basic " + base64.b64encode(raw).decode()
HEAD:backend/onyx/connectors/microsoft_utils/graph_auth.py:82:            pkcs12.load_key_and_certificates(pfx_data, password.encode("utf-8"))
HEAD:backend/onyx/connectors/models.py:252:        # If title is explicitly empty, return a None here for embedding purposes
HEAD:backend/onyx/connectors/models.py:328:        return hashlib.md5(raw.encode(), usedforsecurity=False).hexdigest()
HEAD:backend/onyx/connectors/salesforce/connector.py:284:        query = urlencode(
HEAD:backend/onyx/connectors/web/connector.py:157:      the page or embedding the contents
HEAD:backend/onyx/context/search/federated/slack_search.py:1285:        tokenizer=embedder.embedding_model.tokenizer,
HEAD:backend/onyx/context/search/models.py:54:            embedding_precision=search_settings.embedding_precision,
HEAD:backend/onyx/context/search/pipeline.py:29:from onyx.natural_language_processing.search_nlp_models import EmbeddingModel
HEAD:backend/onyx/context/search/pipeline.py:281:    embedding_model: EmbeddingModel | None = None,
HEAD:backend/onyx/context/search/pipeline.py:333:        embedding_model=embedding_model,
HEAD:backend/onyx/context/search/retrieval/search_runner.py:14:from onyx.context.search.utils import get_query_embedding, inference_section_from_chunks
HEAD:backend/onyx/context/search/retrieval/search_runner.py:20:from onyx.natural_language_processing.search_nlp_models import EmbeddingModel
HEAD:backend/onyx/context/search/retrieval/search_runner.py:55:    embedding_model: EmbeddingModel | None = None,
HEAD:backend/onyx/context/search/retrieval/search_runner.py:57:    query_embedding = get_query_embedding(
HEAD:backend/onyx/context/search/retrieval/search_runner.py:60:        embedding_model=embedding_model,
HEAD:backend/onyx/context/search/retrieval/search_runner.py:68:        query_embedding=query_embedding,
HEAD:backend/onyx/context/search/retrieval/search_runner.py:94:    embedding_model: EmbeddingModel | None = None,
HEAD:backend/onyx/context/search/retrieval/search_runner.py:136:            # search without computing an embedding. This branch is currently
HEAD:backend/onyx/context/search/retrieval/search_runner.py:149:                    (query_request, document_index, db_session, embedding_model),
HEAD:backend/onyx/context/search/utils.py:8:    QUERY_EMBEDDING_CACHE_ENABLED,
HEAD:backend/onyx/context/search/utils.py:9:    QUERY_EMBEDDING_CACHE_TTL_S,
HEAD:backend/onyx/context/search/utils.py:21:from onyx.natural_language_processing.query_embedding_cache import (
HEAD:backend/onyx/context/search/utils.py:22:    cache_query_embeddings,
HEAD:backend/onyx/context/search/utils.py:23:    get_cached_query_embeddings,
HEAD:backend/onyx/context/search/utils.py:26:from onyx.natural_language_processing.search_nlp_models import EmbeddingModel
HEAD:backend/onyx/context/search/utils.py:29:from shared_configs.configs import MODEL_SERVER_HOST, MODEL_SERVER_PORT
HEAD:backend/onyx/context/search/utils.py:31:from shared_configs.model_server_models import Embedding
HEAD:backend/onyx/context/search/utils.py:84:def get_query_embeddings(
HEAD:backend/onyx/context/search/utils.py:87:    embedding_model: EmbeddingModel | None = None,
HEAD:backend/onyx/context/search/utils.py:88:) -> list[Embedding]:
HEAD:backend/onyx/context/search/utils.py:90:    if embedding_model is None:
HEAD:backend/onyx/context/search/utils.py:92:            raise ValueError("Either db_session or embedding_model must be provided")
HEAD:backend/onyx/context/search/utils.py:94:        embedding_model = EmbeddingModel.from_db_model(
HEAD:backend/onyx/context/search/utils.py:96:            server_host=MODEL_SERVER_HOST,
HEAD:backend/onyx/context/search/utils.py:97:            server_port=MODEL_SERVER_PORT,
HEAD:backend/onyx/context/search/utils.py:101:        # supplied an embedding_model.
HEAD:backend/onyx/context/search/utils.py:104:    result: list[Embedding] = []
HEAD:backend/onyx/context/search/utils.py:106:        QUERY_EMBEDDING_CACHE_ENABLED and bool(queries) and search_settings is not None
HEAD:backend/onyx/context/search/utils.py:110:            record_cache_skipped(embedding_model.provider_type, count=len(queries))
HEAD:backend/onyx/context/search/utils.py:111:        result = embedding_model.encode(queries, text_type=EmbedTextType.QUERY)
HEAD:backend/onyx/context/search/utils.py:113:            "Bug: The length of embeddings does not match the length of queries."
HEAD:backend/onyx/context/search/utils.py:118:    cached = get_cached_query_embeddings(
HEAD:backend/onyx/context/search/utils.py:121:        provider_type=embedding_model.provider_type,
HEAD:backend/onyx/context/search/utils.py:122:        ttl_seconds=QUERY_EMBEDDING_CACHE_TTL_S,
HEAD:backend/onyx/context/search/utils.py:129:            "Bug: The length of embeddings does not match the length of queries."
HEAD:backend/onyx/context/search/utils.py:134:    fresh_embeddings = embedding_model.encode(
HEAD:backend/onyx/context/search/utils.py:138:    cache_query_embeddings(
HEAD:backend/onyx/context/search/utils.py:140:        embeddings=fresh_embeddings,
HEAD:backend/onyx/context/search/utils.py:142:        provider_type=embedding_model.provider_type,
HEAD:backend/onyx/context/search/utils.py:143:        ttl_seconds=QUERY_EMBEDDING_CACHE_TTL_S,
HEAD:backend/onyx/context/search/utils.py:146:    fresh_iter = iter(fresh_embeddings)
HEAD:backend/onyx/context/search/utils.py:153:        "Bug: The length of embeddings does not match the length of queries."
HEAD:backend/onyx/context/search/utils.py:159:def get_query_embedding(
HEAD:backend/onyx/context/search/utils.py:162:    embedding_model: EmbeddingModel | None = None,
HEAD:backend/onyx/context/search/utils.py:163:) -> Embedding:
HEAD:backend/onyx/context/search/utils.py:164:    return get_query_embeddings(
HEAD:backend/onyx/context/search/utils.py:165:        [query], db_session=db_session, embedding_model=embedding_model
HEAD:backend/onyx/db/connector_credential_pair.py:903:        # For embedding swap checks, include PAUSED and exclude DELETING or INVALID
HEAD:backend/onyx/db/engine/sql_engine.py:258:            # (e.g. minutes of embedding + vector-db writes between
HEAD:backend/onyx/db/enums.py:286:class EmbeddingPrecision(str, PyEnum):
HEAD:backend/onyx/db/index_attempt.py:959:            error_msg="Canceled due to embedding model swap",
HEAD:backend/onyx/db/index_attempt.py:997:    any embedding model that not present/future"""
HEAD:backend/onyx/db/index_attempt.py:1037:    """Collect all of the Index Attempts that are successful and for the specified embedding model
HEAD:backend/onyx/db/index_attempt.py:1061:    """Collect all of the Index Attempts that are successful and for the specified embedding model,
HEAD:backend/onyx/db/index_attempt_metrics.py:270:    batch (e.g. per ``EmbeddingModel.encode`` call) and we want to flush a
HEAD:backend/onyx/db/index_attempt_metrics_models.py:46:    EMBEDDING = "EMBEDDING"
HEAD:backend/onyx/db/index_attempt_metrics_models.py:95:    IndexAttemptStage.EMBEDDING: StageScope.BATCH_LEVEL,
HEAD:backend/onyx/db/llm.py:9:from onyx.db.models import CloudEmbeddingProvider as CloudEmbeddingProviderModel
HEAD:backend/onyx/db/llm.py:32:from onyx.server.manage.embedding.models import (
HEAD:backend/onyx/db/llm.py:33:    CloudEmbeddingProvider,
HEAD:backend/onyx/db/llm.py:34:    CloudEmbeddingProviderCreationRequest,
HEAD:backend/onyx/db/llm.py:45:from shared_configs.enums import EmbeddingProvider
HEAD:backend/onyx/db/llm.py:228:def _resolve_embedding_api_key(
HEAD:backend/onyx/db/llm.py:233:    """Pick the api_key to store for an embedding provider."""
HEAD:backend/onyx/db/llm.py:240:    return _restore_masked_embedding_api_key(incoming, existing)
HEAD:backend/onyx/db/llm.py:243:def _restore_masked_embedding_api_key(
HEAD:backend/onyx/db/llm.py:279:def upsert_cloud_embedding_provider(
HEAD:backend/onyx/db/llm.py:280:    db_session: Session, provider: CloudEmbeddingProviderCreationRequest
HEAD:backend/onyx/db/llm.py:281:) -> CloudEmbeddingProvider:
HEAD:backend/onyx/db/llm.py:283:        db_session.query(CloudEmbeddingProviderModel)
HEAD:backend/onyx/db/llm.py:291:        updates["api_key"] = _resolve_embedding_api_key(
HEAD:backend/onyx/db/llm.py:300:        creation["api_key"] = _resolve_embedding_api_key(
HEAD:backend/onyx/db/llm.py:305:        new_provider = CloudEmbeddingProviderModel(**creation)
HEAD:backend/onyx/db/llm.py:311:    return CloudEmbeddingProvider.from_request(existing_provider)
HEAD:backend/onyx/db/llm.py:615:def fetch_existing_embedding_providers(
HEAD:backend/onyx/db/llm.py:617:) -> list[CloudEmbeddingProviderModel]:
HEAD:backend/onyx/db/llm.py:618:    return list(db_session.scalars(select(CloudEmbeddingProviderModel)).all())
HEAD:backend/onyx/db/llm.py:924:def fetch_embedding_provider(
HEAD:backend/onyx/db/llm.py:925:    db_session: Session, provider_type: EmbeddingProvider
HEAD:backend/onyx/db/llm.py:926:) -> CloudEmbeddingProviderModel | None:
HEAD:backend/onyx/db/llm.py:928:        select(CloudEmbeddingProviderModel).where(
HEAD:backend/onyx/db/llm.py:929:            CloudEmbeddingProviderModel.provider_type == provider_type
HEAD:backend/onyx/db/llm.py:1019:def remove_embedding_provider(
HEAD:backend/onyx/db/llm.py:1020:    db_session: Session, provider_type: EmbeddingProvider
HEAD:backend/onyx/db/llm.py:1026:    # Delete the embedding provider
HEAD:backend/onyx/db/llm.py:1028:        delete(CloudEmbeddingProviderModel).where(
HEAD:backend/onyx/db/llm.py:1029:            CloudEmbeddingProviderModel.provider_type == provider_type
HEAD:backend/onyx/db/models.py:80:    EmbeddingPrecision,
HEAD:backend/onyx/db/models.py:140:from shared_configs.enums import EmbeddingProvider
HEAD:backend/onyx/db/models.py:2266:    provider_type: Mapped[EmbeddingProvider | None] = mapped_column(
HEAD:backend/onyx/db/models.py:2267:        ForeignKey("embedding_provider.provider_type"), nullable=True
HEAD:backend/onyx/db/models.py:2270:    # Type of switchover to perform when switching embedding models
HEAD:backend/onyx/db/models.py:2315:    embedding_precision: Mapped[EmbeddingPrecision] = mapped_column(
HEAD:backend/onyx/db/models.py:2316:        Enum(EmbeddingPrecision, native_enum=False),
HEAD:backend/onyx/db/models.py:2317:        default=EmbeddingPrecision.FLOAT,
HEAD:backend/onyx/db/models.py:2321:    # a small performance hit. More details in the `Reducing embedding dimensions`
HEAD:backend/onyx/db/models.py:2323:    # https://platform.openai.com/docs/guides/embeddings#embedding-models
HEAD:backend/onyx/db/models.py:2339:    cloud_provider: Mapped["CloudEmbeddingProvider"] = relationship(
HEAD:backend/onyx/db/models.py:2340:        "CloudEmbeddingProvider",
HEAD:backend/onyx/db/models.py:2351:            "ix_embedding_model_present_unique",
HEAD:backend/onyx/db/models.py:2357:            "ix_embedding_model_future_unique",
HEAD:backend/onyx/db/models.py:2371:        return f"<EmbeddingModel(model_name='{self.model_name}', status='{self.status}',\
HEAD:backend/onyx/db/models.py:2411:    def final_embedding_dim(self) -> int:
HEAD:backend/onyx/db/models.py:2416:        multipass: bool, model_name: str, provider_type: EmbeddingProvider | None
HEAD:backend/onyx/db/models.py:2427:            and provider_type != EmbeddingProvider.COHERE
HEAD:backend/onyx/db/models.py:2582:    # The two below may be slightly out of sync if user switches Embedding Model
HEAD:backend/onyx/db/models.py:2590:    # Nullable because in the past, we didn't allow swapping out embedding models live
HEAD:backend/onyx/db/models.py:2722:    re-embedding under FUTURE settings. Doc-id cursor, distinct from IndexAttempt."""
HEAD:backend/onyx/db/models.py:3852:class CloudEmbeddingProvider(Base):
HEAD:backend/onyx/db/models.py:3853:    __tablename__ = "embedding_provider"
HEAD:backend/onyx/db/models.py:3855:    provider_type: Mapped[EmbeddingProvider] = mapped_column(
HEAD:backend/onyx/db/models.py:3856:        Enum(EmbeddingProvider), primary_key=True
HEAD:backend/onyx/db/models.py:3869:        return f"<EmbeddingProvider(type='{self.provider_type}')>"
HEAD:backend/onyx/db/release_notes.py:76:        link = f"{DOCS_CHANGELOG_BASE_URL}#{version_anchor}?{urlencode(utm_params)}"
HEAD:backend/onyx/db/search_settings.py:10:from onyx.db.llm import fetch_embedding_provider
HEAD:backend/onyx/db/search_settings.py:12:    CloudEmbeddingProvider,
HEAD:backend/onyx/db/search_settings.py:18:from onyx.server.manage.embedding.models import (
HEAD:backend/onyx/db/search_settings.py:19:    CloudEmbeddingProvider as ServerCloudEmbeddingProvider,
HEAD:backend/onyx/db/search_settings.py:23:from shared_configs.enums import EmbeddingProvider
HEAD:backend/onyx/db/search_settings.py:56:    embedding_model = SearchSettings(
HEAD:backend/onyx/db/search_settings.py:67:        embedding_precision=search_settings.embedding_precision,
HEAD:backend/onyx/db/search_settings.py:79:    db_session.add(embedding_model)
HEAD:backend/onyx/db/search_settings.py:85:    return embedding_model
HEAD:backend/onyx/db/search_settings.py:88:def get_embedding_provider_from_provider_type(
HEAD:backend/onyx/db/search_settings.py:89:    db_session: Session, provider_type: EmbeddingProvider
HEAD:backend/onyx/db/search_settings.py:90:) -> CloudEmbeddingProvider | None:
HEAD:backend/onyx/db/search_settings.py:91:    query = select(CloudEmbeddingProvider).where(
HEAD:backend/onyx/db/search_settings.py:92:        CloudEmbeddingProvider.provider_type == provider_type
HEAD:backend/onyx/db/search_settings.py:98:def get_current_db_embedding_provider(
HEAD:backend/onyx/db/search_settings.py:100:) -> ServerCloudEmbeddingProvider | None:
HEAD:backend/onyx/db/search_settings.py:106:    embedding_provider = fetch_embedding_provider(
HEAD:backend/onyx/db/search_settings.py:110:    if embedding_provider is None:
HEAD:backend/onyx/db/search_settings.py:111:        raise RuntimeError("No embedding provider exists for this model.")
HEAD:backend/onyx/db/search_settings.py:113:    current_embedding_provider = ServerCloudEmbeddingProvider.from_request(
HEAD:backend/onyx/db/search_settings.py:114:        cloud_provider_model=embedding_provider
HEAD:backend/onyx/db/search_settings.py:117:    return current_embedding_provider
HEAD:backend/onyx/db/search_settings.py:285:def user_has_overridden_embedding_model() -> bool:
HEAD:backend/onyx/db/swap_index.py:69:        # Expire jobs for the now past index/embedding model
HEAD:backend/onyx/db/swap_index.py:162:                    embedding_dim=new_search_settings.final_embedding_dim,
HEAD:backend/onyx/db/swap_index.py:163:                    embedding_precision=new_search_settings.embedding_precision,
HEAD:backend/onyx/db/users.py:159:        f"{_MEMBERSHIP_LOCK_NAMESPACE}:{tenant_id}".encode()
HEAD:backend/onyx/document_index/chunk_content_enrichment.py:11:def generate_enriched_content_for_chunk_embedding(chunk: DocAwareChunk) -> str:
HEAD:backend/onyx/document_index/disabled.py:12:from onyx.db.enums import EmbeddingPrecision
HEAD:backend/onyx/document_index/disabled.py:21:from shared_configs.model_server_models import Embedding
HEAD:backend/onyx/document_index/disabled.py:36:        embedding_dim: int,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:37:        embedding_precision: EmbeddingPrecision,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:73:        query_embedding: Embedding,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:92:        query_embedding: Embedding,  # noqa: ARG002
HEAD:backend/onyx/document_index/factory.py:43:        embedding_dim=indexing_setting.final_embedding_dim,
HEAD:backend/onyx/document_index/factory.py:44:        embedding_precision=indexing_setting.embedding_precision,
HEAD:backend/onyx/document_index/factory.py:67:        secondary_embedding_dim=secondary_indexing_setting.final_embedding_dim,
HEAD:backend/onyx/document_index/factory.py:68:        secondary_embedding_precision=secondary_indexing_setting.embedding_precision,
HEAD:backend/onyx/document_index/factory.py:90:            secondary_embedding_dim=None,
HEAD:backend/onyx/document_index/factory.py:91:            secondary_embedding_precision=None,
HEAD:backend/onyx/document_index/factory.py:106:        secondary_embedding_dim=secondary_indexing_setting.final_embedding_dim,
HEAD:backend/onyx/document_index/factory.py:107:        secondary_embedding_precision=secondary_indexing_setting.embedding_precision,
HEAD:backend/onyx/document_index/interfaces_new.py:12:from onyx.db.enums import EmbeddingPrecision
HEAD:backend/onyx/document_index/interfaces_new.py:15:from shared_configs.model_server_models import Embedding
HEAD:backend/onyx/document_index/interfaces_new.py:152:    # Source creation time. Patched onto existing chunks without re-embedding when
HEAD:backend/onyx/document_index/interfaces_new.py:200:        embedding_dim: int,
HEAD:backend/onyx/document_index/interfaces_new.py:201:        embedding_precision: EmbeddingPrecision,
HEAD:backend/onyx/document_index/interfaces_new.py:212:            embedding_dim: Vector dimensionality for the vector similarity part
HEAD:backend/onyx/document_index/interfaces_new.py:214:            embedding_precision: Precision of the values of the vectors for the
HEAD:backend/onyx/document_index/interfaces_new.py:372:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/interfaces_new.py:385:            query_embedding: Vector representation of the query. Must be of the
HEAD:backend/onyx/document_index/interfaces_new.py:428:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/interfaces_new.py:435:            query_embedding: Vector representation of the query. Must be of the
HEAD:backend/onyx/document_index/opensearch/README.md:29:Embedding models do not have a uniform distribution from 0 to 1. The values typically cluster strongly around 0.6 to 0.8 but also
HEAD:backend/onyx/document_index/opensearch/README.md:61:Because the Title is included in the Contents for both embedding and keyword searches, the Title scores are very low relative to
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:23:from onyx.db.enums import EmbeddingPrecision
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:74:from shared_configs.model_server_models import Embedding
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:224:        # the title_embedding in the embedder. This method falls back to
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:227:        title_vector=chunk.title_embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:229:        content_vector=chunk.embeddings.full_embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:281:    Each kind of embedding used should correspond to a different instance of
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:293:        embedding_dim: The dimensionality of the embeddings used for the index.
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:294:        embedding_precision: The precision of the embeddings used for the index.
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:301:        embedding_dim: int,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:302:        embedding_precision: EmbeddingPrecision,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:315:                    embedding_dim=embedding_dim, embedding_precision=embedding_precision
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:334:        embedding_dim: int,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:335:        embedding_precision: EmbeddingPrecision,  # noqa: ARG002
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:350:            embedding_dim: Vector dimensionality for the vector similarity part
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:352:            embedding_precision: Precision of the values of the vectors for the
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:360:            "[OpenSearchDocumentIndex] Verifying and creating index %s if necessary, with embedding dimension %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:362:            embedding_dim,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:375:                embedding_dim, self._tenant_state.multitenant
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:795:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:815:            query_vector=query_embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:895:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:907:            query_embedding=query_embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1016:        # Embedding info needed at verify-and-create time per index.
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1018:        secondary_embedding_dim: int | None = None,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1019:        secondary_embedding_precision: EmbeddingPrecision | None = None,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1027:        dim_set = secondary_embedding_dim is not None
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1028:        precision_set = secondary_embedding_precision is not None
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1031:                "Bug: Secondary OpenSearchDocumentIndex, secondary_embedding_dim, and "
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1032:                "secondary_embedding_precision must all be set together or all be None. Got: "
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1033:                f"secondary={secondary_set}, embedding_dim={dim_set}, "
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1034:                f"embedding_precision={precision_set}."
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1038:        self._secondary_embedding_dim = secondary_embedding_dim
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1039:        self._secondary_embedding_precision = secondary_embedding_precision
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1044:        embedding_dim: int,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1045:        embedding_precision: EmbeddingPrecision,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1048:            embedding_dim, embedding_precision
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1051:            assert self._secondary_embedding_dim is not None, (
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1052:                "Bug: Secondary embedding dimension is not set."
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1054:            assert self._secondary_embedding_precision is not None, (
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1055:                "Bug: Secondary embedding precision is not set."
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1058:                self._secondary_embedding_dim, self._secondary_embedding_precision
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1107:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1115:            query_embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1135:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1140:            query_embedding, filters, num_to_retrieve
HEAD:backend/onyx/document_index/opensearch/port_copy.py:36:from shared_configs.configs import DOC_EMBEDDING_CONTEXT_SIZE
HEAD:backend/onyx/document_index/opensearch/port_copy.py:46:    embedding tokenizer is always resolved (reproduces the chunker's metadata-tail skip);
HEAD:backend/onyx/document_index/opensearch/port_copy.py:49:    future_embedding_tokenizer = get_tokenizer(
HEAD:backend/onyx/document_index/opensearch/port_copy.py:56:            future_embedding_tokenizer=future_embedding_tokenizer,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:71:        future_embedding_tokenizer=future_embedding_tokenizer,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:76:        chunk_token_limit=DOC_EMBEDDING_CONTEXT_SIZE * 2,
HEAD:backend/onyx/document_index/opensearch/schema.py:92:    encoded_suffix_length: int = len(opensearch_doc_chunk_id_suffix.encode("utf-8"))
HEAD:backend/onyx/document_index/opensearch/schema.py:104:            opensearch_doc_chunk_id_tenant_prefix.encode("utf-8")
HEAD:backend/onyx/document_index/opensearch/schema.py:127:            document_id.encode("utf-8"), digest_size=digest_size
HEAD:backend/onyx/document_index/opensearch/schema.py:400:            vector_dimension: The dimension of vector embeddings. Must be a
HEAD:backend/onyx/document_index/opensearch/search.py:67:        # Since the titles are included in the contents, the embedding matches
HEAD:backend/onyx/document_index/opensearch/search.py:358:            query_vector: The vector embedding of the text to query for.
HEAD:backend/onyx/document_index/opensearch/search.py:535:        query_embedding: list[float],
HEAD:backend/onyx/document_index/opensearch/search.py:549:            query_embedding: The vector embedding of the text to query for.
HEAD:backend/onyx/document_index/opensearch/search.py:587:                query_embedding,
HEAD:backend/onyx/document_index/opensearch/search.py:730:            query_vector: The vector embedding of the query to search for.
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:44:    if len(filtered_document_id.encode("utf-8")) >= max_encoded_length:
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:30:        # Must have an additional field for whether to skip title embeddings
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:31:        # This information cannot be extracted from either the title field nor title embedding
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:52:        # Title embedding (x1)
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:53:        field title_embedding type tensor<{{ embedding_precision }}>(x[{{ dim }}]) {
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:59:        # Content embeddings (chunk + optional mini chunks embeddings)
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:61:        field embeddings type tensor<{{ embedding_precision }}>(t{},x[{{ dim }}]) {
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:231:            query(query_embedding) tensor<float>(x[{{ dim }}])
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:236:                # If no good matching titles, then it should use the context embeddings rather than having some
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:239:                max(closeness(field, embeddings), closeness(field, title_embedding))
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:245:            expression: query(title_content_ratio) * closeness(field, title_embedding) + (1 - query(title_content_ratio)) * closeness(field, embeddings)
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:257:                            ((1 - query(title_content_ratio)) * normalize_linear(closeness(field, embeddings)))
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:288:            closeness(field, title_embedding)
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:289:            closeness(field, embeddings)
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:293:            closest(embeddings)
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:300:            query(query_embedding) tensor<float>(x[{{ dim }}])
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:305:                # If no good matching titles, then it should use the context embeddings rather than having some
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:308:                max(closeness(field, embeddings), closeness(field, title_embedding))
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:326:                            ((1 - query(title_content_ratio)) * normalize_linear(closeness(field, embeddings)))
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:357:            closeness(field, title_embedding)
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:358:            closeness(field, embeddings)
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:362:            closest(embeddings)
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:41:    EMBEDDINGS,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:42:    FULL_CHUNK_EMBEDDING_KEY,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:54:    SKIP_TITLE_EMBEDDING,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:59:    TITLE_EMBEDDING,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:156:    embeddings = chunk.embeddings
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:158:    embeddings_name_vector_map = {FULL_CHUNK_EMBEDDING_KEY: embeddings.full_embedding}
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:160:    if embeddings.mini_chunk_embeddings:
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:161:        for ind, m_c_embed in enumerate(embeddings.mini_chunk_embeddings):
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:162:            embeddings_name_vector_map[f"mini_chunk_{ind}"] = m_c_embed
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:188:        SKIP_TITLE_EMBEDDING: not title,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:209:        EMBEDDINGS: embeddings_name_vector_map,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:210:        TITLE_EMBEDDING: chunk.title_embedding,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:34:from onyx.db.enums import EmbeddingPrecision
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:96:from shared_configs.model_server_models import Embedding
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:192:    primary_embedding_dim: int,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:193:    primary_embedding_precision: EmbeddingPrecision,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:195:    secondary_embedding_dim: int | None,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:196:    secondary_embedding_precision: EmbeddingPrecision | None,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:256:        "services.xml": services.encode("utf-8"),
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:257:        "validation-overrides.xml": overrides.encode("utf-8"),
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:267:        dim=primary_embedding_dim,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:268:        embedding_precision=primary_embedding_precision.value,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:271:    zip_dict[f"schemas/{primary_index_name}.sd"] = schema.encode("utf-8")
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:274:        if secondary_embedding_dim is None:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:275:            raise ValueError("Secondary index embedding dimension is required")
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:276:        if secondary_embedding_precision is None:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:277:            raise ValueError("Secondary index embedding precision is required")
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:281:            dim=secondary_embedding_dim,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:282:            embedding_precision=secondary_embedding_precision.value,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:284:        zip_dict[f"schemas/{secondary_index_name}.sd"] = upcoming_schema.encode("utf-8")
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:298:    embedding_dims: list[int],
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:299:    embedding_precisions: list[EmbeddingPrecision],
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:349:        "services.xml": services.encode("utf-8"),
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:350:        "validation-overrides.xml": overrides.encode("utf-8"),
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:359:        embedding_dim = embedding_dims[i]
```
Embedding/model-server integration is present in source.
No embedding request was executed.
## Document and Chunk Index Writes
Evidence lines: 189
```text
HEAD:backend/onyx/document_index/chunk_content_enrichment.py:54:        # backend/onyx/document_index/vespa/vespa_document_index.py but I don't
HEAD:backend/onyx/document_index/chunk_content_enrichment.py:56:        # from the output of get_title_for_document_index, which is not
HEAD:backend/onyx/document_index/disabled.py:13:from onyx.document_index.interfaces_new import (
HEAD:backend/onyx/document_index/document_index_utils.py:13:from onyx.document_index.vespa.internal_types import EnrichedDocumentIndexingInfo
HEAD:backend/onyx/document_index/document_metadata.py:3:Previously declared in the now-removed `onyx.document_index.interfaces` module.
HEAD:backend/onyx/document_index/document_metadata.py:4:Used by the indexing pipeline / Postgres upsert layer; not part of the search
HEAD:backend/onyx/document_index/factory.py:11:from onyx.document_index.disabled import DisabledDocumentIndex
HEAD:backend/onyx/document_index/factory.py:12:from onyx.document_index.interfaces_new import DocumentIndex, TenantState
HEAD:backend/onyx/document_index/factory.py:13:from onyx.document_index.opensearch.opensearch_document_index import (
HEAD:backend/onyx/document_index/factory.py:14:    OpenSearchDocumentIndex,
HEAD:backend/onyx/document_index/factory.py:17:from onyx.document_index.vespa.vespa_document_index import (
HEAD:backend/onyx/document_index/factory.py:18:    VespaDocumentIndex,
HEAD:backend/onyx/document_index/factory.py:30:def build_opensearch_document_index(
HEAD:backend/onyx/document_index/factory.py:32:) -> OpenSearchDocumentIndex:
HEAD:backend/onyx/document_index/factory.py:36:    not the primary+secondary pair `get_default_document_index` returns. Shared
HEAD:backend/onyx/document_index/factory.py:40:    return OpenSearchDocumentIndex(
HEAD:backend/onyx/document_index/factory.py:53:    primary = build_opensearch_document_index(search_settings)
HEAD:backend/onyx/document_index/factory.py:63:    secondary = build_opensearch_document_index(secondary_search_settings)
HEAD:backend/onyx/document_index/factory.py:79:    primary = VespaDocumentIndex(
HEAD:backend/onyx/document_index/factory.py:96:    secondary = VespaDocumentIndex(
HEAD:backend/onyx/document_index/factory.py:111:def get_default_document_index(
HEAD:backend/onyx/document_index/interfaces_new.py:13:from onyx.document_index.opensearch.constants import DEFAULT_MAX_CHUNK_SIZE
HEAD:backend/onyx/document_index/opensearch/client.py:35:from onyx.document_index.interfaces_new import TenantState
HEAD:backend/onyx/document_index/opensearch/client.py:36:from onyx.document_index.opensearch.constants import (
HEAD:backend/onyx/document_index/opensearch/client.py:41:from onyx.document_index.opensearch.schema import (
HEAD:backend/onyx/document_index/opensearch/client.py:51:from onyx.document_index.opensearch.search import DEFAULT_OPENSEARCH_MAX_RESULT_WINDOW
HEAD:backend/onyx/document_index/opensearch/client.py:317:            # including bulk indexing. When exceeded, the client will raise a
HEAD:backend/onyx/document_index/opensearch/client.py:984:    def bulk_index_documents(
HEAD:backend/onyx/document_index/opensearch/client.py:991:        """Bulk indexes documents.
HEAD:backend/onyx/document_index/opensearch/client.py:993:        Raises if there are any errors during the bulk index. It should be
HEAD:backend/onyx/document_index/opensearch/client.py:1014:            Exception: There was an error during the bulk index. This
HEAD:backend/onyx/document_index/opensearch/client.py:1017:            BulkIndexError: There was an error during the bulk index. This is a
HEAD:backend/onyx/document_index/opensearch/client.py:1026:            "Bulk indexing %s documents for tenant %s. update_if_exists=%s "
HEAD:backend/onyx/document_index/opensearch/client.py:1069:            # on the BulkIndexError that bulk raises)
HEAD:backend/onyx/document_index/opensearch/client.py:1081:                f"Bulk index for index {self._index_name}: successful operations ({successes}) "
HEAD:backend/onyx/document_index/opensearch/client.py:1086:            "Successfully bulk indexed %s documents (%s benign version conflicts).",
HEAD:backend/onyx/document_index/opensearch/client.py:1097:        Any, BulkIndexError.errors -> List[Any]); they are raw {op_type: {...}}
HEAD:backend/onyx/document_index/opensearch/client.py:1115:                f"Failed to bulk index documents for index {self._index_name}. "
HEAD:backend/onyx/document_index/opensearch/client.py:1363:            BulkIndexError: There was an error during the bulk update. This is a
HEAD:backend/onyx/document_index/opensearch/client.py:1376:            "Bulk updating %s document chunks for index %s.",
HEAD:backend/onyx/document_index/opensearch/client.py:1472:                    f"Failed to bulk update document chunks for index {self._index_name}. "
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:9:from onyx.document_index.interfaces_new import TenantState
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:10:from onyx.document_index.opensearch.client import OpenSearchIndexClient
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:11:from onyx.document_index.opensearch.schema import TENANT_ID_FIELD_NAME
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:5:from opensearchpy.helpers.errors import BulkIndexError
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:25:from onyx.document_index.chunk_content_enrichment import (
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:29:from onyx.document_index.interfaces_new import (
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:38:from onyx.document_index.opensearch.client import (
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:46:from onyx.document_index.opensearch.cluster_settings import OPENSEARCH_CLUSTER_SETTINGS
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:47:from onyx.document_index.opensearch.constants import OpenSearchSearchType
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:48:from onyx.document_index.opensearch.schema import (
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:62:from onyx.document_index.opensearch.search import (
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:203:    _title = chunk.source_document.get_title_for_document_index()
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:223:        # Use get_title_for_document_index to match the logic used when creating
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:265:        # DocMetadataAwareIndexChunk and instead using OpenSearchDocumentIndex's
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:274:class OpenSearchDocumentIndex(DocumentIndex):
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:360:            "[OpenSearchDocumentIndex] Verifying and creating index %s if necessary, with embedding dimension %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:440:            "[OpenSearchDocumentIndex] Indexing %s chunks from %s documents for index %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:446:        document_indexing_results: list[DocumentInsertionRecord] = []
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:479:                # existed. We record the result before bulk_index_documents
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:482:                document_indexing_results.append(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:491:                self._client.bulk_index_documents(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:495:            except BulkIndexError as e:
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:504:                    "Failed to bulk index documents: %s. Refreshing index and trying again.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:508:                self._client.bulk_index_documents(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:532:        return document_indexing_results
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:561:            "[OpenSearchDocumentIndex] Deleting document %s from index %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:622:            "[OpenSearchDocumentIndex] Processing %s chunk requests for index %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:671:                    "[OpenSearchDocumentIndex] Tried to update %s with no specified update fields. This will be a no-op.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:688:                        "[OpenSearchDocumentIndex] Skipping update for document %s: "
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:700:                        "[OpenSearchDocumentIndex] Skipping update for document %s: "
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:753:            "[OpenSearchDocumentIndex] Retrieving %s chunks for index %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:805:            "[OpenSearchDocumentIndex] Hybrid retrieving %s chunks for index %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:858:            "[OpenSearchDocumentIndex] Keyword retrieving %s chunks for index %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:902:            "[OpenSearchDocumentIndex] Semantic retrieving %s chunks for index %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:944:            "[OpenSearchDocumentIndex] Randomly retrieving %s chunks for index %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:983:            "[OpenSearchDocumentIndex] Indexing %s raw chunks for index %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:991:        self._client.bulk_index_documents(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1014:        primary: OpenSearchDocumentIndex,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1015:        secondary: OpenSearchDocumentIndex | None,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1031:                "Bug: Secondary OpenSearchDocumentIndex, secondary_embedding_dim, and "
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1152:    def primary(self) -> OpenSearchDocumentIndex:
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1156:    def secondary(self) -> OpenSearchDocumentIndex | None:
HEAD:backend/onyx/document_index/opensearch/port_copy.py:20:from onyx.document_index.factory import build_opensearch_document_index
HEAD:backend/onyx/document_index/opensearch/port_copy.py:21:from onyx.document_index.opensearch.client import OpenSearchIndexClient
HEAD:backend/onyx/document_index/opensearch/port_copy.py:22:from onyx.document_index.opensearch.opensearch_document_index import (
HEAD:backend/onyx/document_index/opensearch/port_copy.py:23:    OpenSearchDocumentIndex,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:25:from onyx.document_index.opensearch.schema import DocumentChunkWithoutVectors
HEAD:backend/onyx/document_index/opensearch/port_copy.py:83:    future_index: OpenSearchDocumentIndex,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:178:        self._future_index = build_opensearch_document_index(future_search_settings)
HEAD:backend/onyx/document_index/opensearch/schema.py:22:from onyx.document_index.interfaces_new import TenantState
HEAD:backend/onyx/document_index/opensearch/schema.py:23:from onyx.document_index.opensearch.constants import (
HEAD:backend/onyx/document_index/opensearch/schema.py:29:from onyx.document_index.opensearch.string_filtering import (
HEAD:backend/onyx/document_index/opensearch/search.py:13:from onyx.document_index.interfaces_new import TenantState
HEAD:backend/onyx/document_index/opensearch/search.py:14:from onyx.document_index.opensearch.constants import (
HEAD:backend/onyx/document_index/opensearch/search.py:23:from onyx.document_index.opensearch.schema import (
HEAD:backend/onyx/document_index/opensearch/search.py:928:                See document_index/FILTER_SEMANTICS.md ("Time filtering").
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:23:from onyx.document_index.interfaces_new import TenantState
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:24:from onyx.document_index.vespa.internal_types import VespaChunkRequest
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:25:from onyx.document_index.vespa.shared_utils.utils import get_vespa_http_client
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:26:from onyx.document_index.vespa.shared_utils.vespa_request_builders import (
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:30:from onyx.document_index.vespa_constants import (
HEAD:backend/onyx/document_index/vespa/deletion.py:6:from onyx.document_index.vespa_constants import DOCUMENT_ID_ENDPOINT, NUM_THREADS
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:16:from onyx.document_index.chunk_content_enrichment import (
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:19:from onyx.document_index.document_index_utils import (
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:23:from onyx.document_index.vespa.internal_types import MinimalDocumentIndexingInfo
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:24:from onyx.document_index.vespa.shared_utils.utils import (
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:27:from onyx.document_index.vespa_constants import (
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:164:    title = document.get_title_for_document_index()
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:330:def batch_index_vespa_chunks(
HEAD:backend/onyx/document_index/vespa/internal_types.py:4:`onyx.document_index.interfaces` module. They survive only to support Vespa's
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:6:from onyx.document_index.interfaces_new import TenantState
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:7:from onyx.document_index.vespa.vespa_document_index import (
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:9:    VespaDocumentIndex,
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:23:    vespa_index = VespaDocumentIndex(
HEAD:backend/onyx/document_index/vespa/shared_utils/utils.py:12:from onyx.document_index.vespa_constants import VESPA_APP_CONTAINER_URL
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:5:from onyx.document_index.vespa.internal_types import VespaChunkRequest
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:6:from onyx.document_index.vespa_constants import (
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:35:from onyx.document_index.chunk_content_enrichment import cleanup_content_for_chunks
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:36:from onyx.document_index.document_index_utils import (
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:40:from onyx.document_index.interfaces_new import (
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:48:from onyx.document_index.vespa.chunk_retrieval import (
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:55:from onyx.document_index.vespa.deletion import delete_vespa_chunks
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:56:from onyx.document_index.vespa.indexing_utils import (
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:60:    batch_index_vespa_chunks,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:64:from onyx.document_index.vespa.internal_types import (
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:69:from onyx.document_index.vespa.shared_utils.utils import (
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:73:from onyx.document_index.vespa.shared_utils.vespa_request_builders import (
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:76:from onyx.document_index.vespa_constants import (
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:219:        os.getcwd(), "onyx", "document_index", "vespa", "app_config"
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:309:        os.getcwd(), "onyx", "document_index", "vespa", "app_config"
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:508:        # backend/onyx/document_index/vespa_constants.py.
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:597:class VespaDocumentIndex(DocumentIndex):
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:641:        deploy call. Calling this on a single VespaDocumentIndex deploys an
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:766:                batch_index_vespa_chunks(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:819:        # WARNING: This method can be called by document_index_metadata_sync_task,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1243:        primary: VespaDocumentIndex,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1244:        secondary: VespaDocumentIndex | None,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1260:                "Bug: secondary VespaDocumentIndex, secondary_index_name, "
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1363:    def primary(self) -> VespaDocumentIndex:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1367:    def secondary(self) -> VespaDocumentIndex | None:
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:70:        """Upsert docs, map CC pairs, return context or mark as indexed if no-op.
HEAD:backend/onyx/indexing/chunker.py:41:def get_metadata_suffix_for_document_index(
HEAD:backend/onyx/indexing/chunker.py:202:            document.get_title_for_document_index() or "",
HEAD:backend/onyx/indexing/chunker.py:216:            ) = get_metadata_suffix_for_document_index(
HEAD:backend/onyx/indexing/embedder.py:13:from onyx.document_index.chunk_content_enrichment import (
HEAD:backend/onyx/indexing/embedder.py:135:            ) or chunk.source_document.get_title_for_document_index()
HEAD:backend/onyx/indexing/embedder.py:161:            chunk.source_document.get_title_for_document_index() for chunk in chunks
HEAD:backend/onyx/indexing/embedder.py:198:            title = chunk.source_document.get_title_for_document_index()
HEAD:backend/onyx/indexing/indexing_pipeline.py:40:    upsert_document_by_connector_credential_pair,
HEAD:backend/onyx/indexing/indexing_pipeline.py:41:    upsert_documents,
HEAD:backend/onyx/indexing/indexing_pipeline.py:54:from onyx.db.tag import upsert_document_tags
HEAD:backend/onyx/indexing/indexing_pipeline.py:55:from onyx.document_index.document_index_utils import get_multipass_config
HEAD:backend/onyx/indexing/indexing_pipeline.py:56:from onyx.document_index.document_metadata import DocumentMetadata
HEAD:backend/onyx/indexing/indexing_pipeline.py:57:from onyx.document_index.interfaces_new import (
HEAD:backend/onyx/indexing/indexing_pipeline.py:89:from onyx.indexing.vector_db_insertion import write_chunks_to_vector_db_with_backoff
HEAD:backend/onyx/indexing/indexing_pipeline.py:201:def _upsert_documents_in_db(
HEAD:backend/onyx/indexing/indexing_pipeline.py:229:    upsert_documents(db_session, document_metadata_list)
HEAD:backend/onyx/indexing/indexing_pipeline.py:233:        upsert_document_tags(
HEAD:backend/onyx/indexing/indexing_pipeline.py:507:    Intended to run immediately before `_upsert_documents_in_db` so the origin
HEAD:backend/onyx/indexing/indexing_pipeline.py:580:    # for all updatable docs, upsert into the DB
HEAD:backend/onyx/indexing/indexing_pipeline.py:583:        # Queue the STAGING → CONNECTOR origin flips BEFORE the Document upsert
HEAD:backend/onyx/indexing/indexing_pipeline.py:584:        # so `upsert_documents`' commit flushes Document.file_id and the origin
HEAD:backend/onyx/indexing/indexing_pipeline.py:591:        _upsert_documents_in_db(
HEAD:backend/onyx/indexing/indexing_pipeline.py:603:        "Upserted %s changed docs out of %s total docs into the DB",
HEAD:backend/onyx/indexing/indexing_pipeline.py:608:    # for all docs, upsert the document to cc pair relationship
HEAD:backend/onyx/indexing/indexing_pipeline.py:609:    upsert_document_by_connector_credential_pair(
HEAD:backend/onyx/indexing/indexing_pipeline.py:618:    # This must happen after documents are upserted due to FK constraint.
HEAD:backend/onyx/indexing/indexing_pipeline.py:1130:    document_index_name: str,
HEAD:backend/onyx/indexing/indexing_pipeline.py:1144:            f"This occured for document index {document_index_name}"
HEAD:backend/onyx/indexing/indexing_pipeline.py:1555:            for document_index in document_indices:
HEAD:backend/onyx/indexing/indexing_pipeline.py:1564:                        document_index=document_index,
HEAD:backend/onyx/indexing/indexing_pipeline.py:1579:                    document_index_name=document_index.__class__.__name__,
HEAD:backend/onyx/indexing/models.py:190:    # onyx/document_index/opensearch/opensearch_document_index.py. BFLOAT16
HEAD:backend/onyx/indexing/port_reembed.py:48:from onyx.document_index.chunk_content_enrichment import (
HEAD:backend/onyx/indexing/port_reembed.py:52:from onyx.document_index.opensearch.schema import (
HEAD:backend/onyx/indexing/port_reembed.py:58:    get_metadata_suffix_for_document_index,
HEAD:backend/onyx/indexing/port_reembed.py:129:    semantic_suffix, _ = get_metadata_suffix_for_document_index(
HEAD:backend/onyx/indexing/port_reembed.py:204:    (`.id`, `.get_title_for_document_index()`)."""
HEAD:backend/onyx/indexing/port_reembed.py:211:        # get_title_for_document_index returns None and reproduces that; passing
HEAD:backend/onyx/indexing/port_reembed.py:327:    # Lazy import: opensearch_document_index is a heavy module and only needed on
HEAD:backend/onyx/indexing/port_reembed.py:329:    from onyx.document_index.opensearch.opensearch_document_index import (
HEAD:backend/onyx/indexing/vector_db_insertion.py:10:from onyx.document_index.interfaces_new import (
HEAD:backend/onyx/indexing/vector_db_insertion.py:32:    document_index: DocumentIndex,
HEAD:backend/onyx/indexing/vector_db_insertion.py:37:    """Tries to insert all chunks in one large batch. If that batch fails for any reason,
HEAD:backend/onyx/indexing/vector_db_insertion.py:47:            document_index.index(
HEAD:backend/onyx/indexing/vector_db_insertion.py:58:        # the bulk write doesn't ship an event for every indexing batch.
HEAD:backend/onyx/indexing/vector_db_insertion.py:63:        # finish the bulk index.)
HEAD:backend/onyx/indexing/vector_db_insertion.py:95:                document_index.index(
```
This establishes source-level index-write mechanisms.
Runtime index contents remain unverified.
## Index-Time Access Metadata
Evidence lines: 401
```text
HEAD:backend/ee/onyx/access/access.py:8:    fetch_user_groups_for_documents,
HEAD:backend/ee/onyx/access/access.py:9:    fetch_user_groups_for_user,
HEAD:backend/ee/onyx/access/access.py:11:from ee.onyx.external_permissions.sync_params import get_source_perm_sync_config
HEAD:backend/ee/onyx/access/access.py:17:from onyx.access.models import DocumentAccess
HEAD:backend/ee/onyx/access/access.py:30:) -> DocumentAccess:
HEAD:backend/ee/onyx/access/access.py:33:        return DocumentAccess.build(
HEAD:backend/ee/onyx/access/access.py:34:            user_emails=[],
HEAD:backend/ee/onyx/access/access.py:35:            user_groups=[],
HEAD:backend/ee/onyx/access/access.py:36:            external_user_emails=[],
HEAD:backend/ee/onyx/access/access.py:38:            is_public=False,
HEAD:backend/ee/onyx/access/access.py:47:) -> dict[str, DocumentAccess]:
HEAD:backend/ee/onyx/access/access.py:54:        for document_id, group_names in fetch_user_groups_for_documents(
HEAD:backend/ee/onyx/access/access.py:89:            set(document.external_user_emails)
HEAD:backend/ee/onyx/access/access.py:90:            if document.external_user_emails
HEAD:backend/ee/onyx/access/access.py:104:        is_public_anywhere = (
HEAD:backend/ee/onyx/access/access.py:105:            document.is_public
HEAD:backend/ee/onyx/access/access.py:106:            or non_ee_access.is_public
HEAD:backend/ee/onyx/access/access.py:112:        access_map[document_id] = DocumentAccess.build(
HEAD:backend/ee/onyx/access/access.py:113:            user_emails=list(non_ee_access.user_emails),
HEAD:backend/ee/onyx/access/access.py:114:            user_groups=user_group_info.get(document_id, []),
HEAD:backend/ee/onyx/access/access.py:115:            is_public=is_public_anywhere,  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/access/access.py:116:            external_user_emails=list(ext_u_emails),
HEAD:backend/ee/onyx/access/access.py:137:) -> dict[str, DocumentAccess]:
HEAD:backend/ee/onyx/access/access.py:154:) -> dict[str, DocumentAccess]:
HEAD:backend/ee/onyx/access/access.py:160:    result: dict[str, DocumentAccess] = {}
HEAD:backend/ee/onyx/access/access.py:163:            result[str(user_file.id)] = DocumentAccess.build(
HEAD:backend/ee/onyx/access/access.py:164:                user_emails=[],
HEAD:backend/ee/onyx/access/access.py:165:                user_groups=[],
HEAD:backend/ee/onyx/access/access.py:166:                is_public=True,
HEAD:backend/ee/onyx/access/access.py:167:                external_user_emails=[],
HEAD:backend/ee/onyx/access/access.py:172:        emails, is_public = collect_user_file_access(user_file)
HEAD:backend/ee/onyx/access/access.py:174:        result[str(user_file.id)] = DocumentAccess.build(
HEAD:backend/ee/onyx/access/access.py:175:            user_emails=list(emails),
HEAD:backend/ee/onyx/access/access.py:176:            user_groups=list(group_names),
HEAD:backend/ee/onyx/access/access.py:177:            is_public=is_public,
HEAD:backend/ee/onyx/access/access.py:178:            external_user_emails=[],
HEAD:backend/ee/onyx/access/access.py:193:    db_user_groups = (
HEAD:backend/ee/onyx/access/access.py:194:        [] if is_anonymous else fetch_user_groups_for_user(db_session, user.id)
HEAD:backend/ee/onyx/access/access.py:196:    prefixed_user_groups = [
HEAD:backend/ee/onyx/access/access.py:197:        prefix_user_group(db_user_group.name) for db_user_group in db_user_groups
HEAD:backend/ee/onyx/access/access.py:208:    user_acl = set(prefixed_user_groups + prefixed_external_groups)
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:7:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/light.py:7:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:8:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:24:from ee.onyx.external_permissions.sync_params import get_source_perm_sync_config
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:38:    CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:50:from onyx.db.connector import mark_cc_pair_as_permissions_synced
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:72:from onyx.db.permission_sync_attempt import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:73:    complete_doc_permission_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:74:    create_doc_permission_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:75:    mark_doc_permission_sync_attempt_failed,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:76:    mark_doc_permission_sync_attempt_in_progress,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:84:    RedisConnectorPermissionSync,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:85:    RedisConnectorPermissionSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:103:    doc_permission_sync_ctx,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:141:"""Jobs / utils for kicking off doc permissions sync tasks."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:144:def _fail_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:151:    """Helper to mark a doc permission sync attempt as failed with an error message."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:153:        mark_doc_permission_sync_attempt_failed(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:163:def _is_external_doc_permissions_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:164:    """Returns boolean indicating if external doc permissions sync is due."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:169:    # skip doc permissions sync if not active
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:196:    source_sync_period *= int(OnyxRuntime.get_doc_permission_sync_multiplier())
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:207:    name=OnyxCeleryTask.CHECK_FOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:212:def check_for_doc_permissions_sync(self: Task, *, tenant_id: str) -> bool | None:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:221:        OnyxRedisLocks.CHECK_CONNECTOR_DOC_PERMISSIONS_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:238:                if _is_external_doc_permissions_sync_due(cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:242:        # whenever doc-permission sync has any due cc_pairs to dispatch.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:244:            maybe_mark_tenant_active(tenant_id, caller="doc_permission_sync")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:248:            payload_id = try_creating_permissions_sync_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:255:                f"Permissions sync queued: cc_pair={cc_pair_id} id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:260:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:266:                validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:271:                    "Exception while validating permission sync fences"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:275:                OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:292:            if key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:297:        task_logger.info(f"check_for_doc_permissions_sync finished: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:305:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:308:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:317:def try_creating_permissions_sync_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:332:        DANSWER_REDIS_FUNCTION_LOCK_PREFIX + "try_generate_permissions_sync_tasks",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:369:        payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:378:            OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:383:            queue=OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:396:            f"Unexpected try_creating_permissions_sync_task exception: cc_pair={cc_pair_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:404:        f"try_creating_permissions_sync_task finished: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:410:    name=OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:417:def connector_permission_sync_generator_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:423:    Permission sync task that handles document permission syncing for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:431:    doc_permission_sync_ctx_dict = dict(doc_permission_sync_ctx.get())
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:432:    doc_permission_sync_ctx_dict["cc_pair_id"] = cc_pair_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:433:    doc_permission_sync_ctx_dict["request_id"] = self.request.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:434:    doc_permission_sync_ctx.set(doc_permission_sync_ctx_dict)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:437:        attempt_id = create_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:442:            f"Created doc permission sync attempt: {attempt_id} for cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:456:                f"connector_permission_sync_generator_task - timed out waiting for fence to be ready: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:459:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:463:            error_msg = f"connector_permission_sync_generator_task - fence not found: fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:464:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:470:                "connector_permission_sync_generator_task: payload invalid or not found"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:472:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:477:                "connector_permission_sync_generator_task - Waiting for fence: fence=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:486:            "connector_permission_sync_generator_task - Fence found, continuing...: fence=%s payload_id=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:493:        OnyxRedisLocks.CONNECTOR_DOC_PERMISSIONS_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:495:        timeout=CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:502:            f"Permission sync task already running, exiting...: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:505:        _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:543:                    f"validate_ccpair_permissions_sync exceptioned: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:554:                _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:560:                    _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:569:            mark_doc_permission_sync_attempt_in_progress(attempt_id, db_session)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:575:            new_payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:583:            callback = PermissionSyncCallback(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:616:        document_external_accesses = doc_sync_func(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:627:        for doc_external_access in document_external_accesses:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:630:                    f"Permission sync task timed out or stop signal detected: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:637:                new_permissions=[doc_external_access],
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:656:            complete_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:663:            f"Completed doc permission sync attempt {attempt_id}: {tasks_generated} docs, {docs_with_errors} errors"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:673:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:676:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:679:        _fail_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:697:        f"Permission sync finished: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:718:    external_access = permissions.external_access
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:733:                emails=list(external_access.external_user_emails),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:742:                    external_access=external_access,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:760:                    is_public=external_access.is_public,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:761:                    external_user_emails=(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:762:                        list(external_access.external_user_emails)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:763:                        if external_access.external_user_emails
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:767:                        list(external_access.external_user_group_ids)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:768:                        if external_access.external_user_group_ids
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:790:def validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:799:    PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN = 1024
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:804:    if queue_len > PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:811:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:814:    # validate all existing permission sync jobs
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:820:        if not key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:823:        validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:837:def validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:868:    queued_tasks: the celery queue of lightweight permission sync tasks
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:876:            f"validate_permission_sync_fence - could not parse id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:895:            "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:915:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:956:        f"validate_permission_sync_fence task check: tasks_scanned={tasks_scanned} tasks_not_in_celery={tasks_not_in_celery}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:977:        "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:988:class PermissionSyncCallback(IndexingHeartbeatInterface):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1006:        self.last_tag: str = "PermissionSyncCallback.__init__"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1023:                    "PermissionSyncCallback - task timeout exceeded: elapsed=%ss timeout=%ss cc_pair=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1047:                "PermissionSyncCallback - lock.reacquire exceptioned: lock_timeout=%s start=%s last_tag=%s last_reacquired=%s now=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1090:            "Permissions sync payload failed to validate. Schema may have been updated."
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1099:        f"Permissions sync progress: cc_pair={cc_pair_id} id={payload.id} remaining={remaining} initial={initial}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1102:    # Add telemetry for permission syncing progress
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1104:        record_type=RecordType.PERMISSION_SYNC_PROGRESS,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1116:    mark_cc_pair_as_permissions_synced(db_session, int(cc_pair_id), payload.started)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1118:        f"Permissions sync finished: cc_pair={cc_pair_id} id={payload.id} num_synced={initial}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1121:    # Add telemetry for permission syncing complete
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1123:        record_type=RecordType.PERMISSION_SYNC_COMPLETE,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:3:from ee.onyx.external_permissions.sync_params import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:26:from ee.onyx.external_permissions.sync_params import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:59:from onyx.db.permission_sync_attempt import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:594:                total_group_memberships_synced += len(external_user_group.user_emails)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:595:                seen_users.update(external_user_group.user_emails)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:17:def _delete_connector_credential_pair_user_groups_relationship__no_commit(
HEAD:backend/ee/onyx/db/document.py:15:    external_access: ExternalAccess,
HEAD:backend/ee/onyx/db/document.py:31:        for group_id in external_access.external_user_group_ids
HEAD:backend/ee/onyx/db/document.py:40:            external_user_emails=external_access.external_user_emails,
HEAD:backend/ee/onyx/db/document.py:42:            is_public=external_access.is_public,
HEAD:backend/ee/onyx/db/document.py:47:    document.external_user_emails = list(external_access.external_user_emails)
HEAD:backend/ee/onyx/db/document.py:49:    document.is_public = external_access.is_public
HEAD:backend/ee/onyx/db/document.py:55:    external_access: ExternalAccess,
HEAD:backend/ee/onyx/db/document.py:72:        for group_id in external_access.external_user_group_ids
HEAD:backend/ee/onyx/db/document.py:82:            external_user_emails=external_access.external_user_emails,
HEAD:backend/ee/onyx/db/document.py:84:            is_public=external_access.is_public,
HEAD:backend/ee/onyx/db/document.py:92:        external_access.external_user_emails != set(document.external_user_emails or [])
HEAD:backend/ee/onyx/db/document.py:94:        or external_access.is_public != document.is_public
HEAD:backend/ee/onyx/db/document.py:96:        document.external_user_emails = list(external_access.external_user_emails)
HEAD:backend/ee/onyx/db/document.py:98:        document.is_public = external_access.is_public
HEAD:backend/ee/onyx/db/document_set.py:99:        document_set.id for document_set in attaching if not document_set.is_public
HEAD:backend/ee/onyx/db/document_set.py:158:        .filter(DocumentSet.is_public == True)  # noqa
HEAD:backend/ee/onyx/db/document_set.py:172:    user_groups = (
HEAD:backend/ee/onyx/db/document_set.py:180:    for group in user_groups:
HEAD:backend/ee/onyx/db/external_perm.py:20:    user_emails: list[str]
HEAD:backend/ee/onyx/db/external_perm.py:23:    # if this is set, `user_emails` don't really matter.
HEAD:backend/ee/onyx/db/external_perm.py:106:        all_group_member_emails.update(external_group.user_emails)
HEAD:backend/ee/onyx/db/external_perm.py:126:        for user_email in external_group.user_emails:
HEAD:backend/ee/onyx/db/hierarchy.py:56:        HierarchyNode.is_public.is_(True),
HEAD:backend/ee/onyx/db/hierarchy.py:59:        access_filters.append(any_(HierarchyNode.external_user_emails) == user_email)
HEAD:backend/ee/onyx/db/persona.py:84:    original_is_public: bool,
HEAD:backend/ee/onyx/db/persona.py:91:    current is_public must be private — sharing a public agent in would capture it."""
HEAD:backend/ee/onyx/db/persona.py:95:    if has_global_permission(acting_user, Permission.MANAGE_USER_GROUPS):
HEAD:backend/ee/onyx/db/persona.py:129:        is_non_public=not original_is_public and not persona.is_public,
HEAD:backend/ee/onyx/db/persona.py:138:    is_public: bool | None = None,
HEAD:backend/ee/onyx/db/persona.py:144:    original_is_public: bool | None = None,
HEAD:backend/ee/onyx/db/persona.py:149:    Pass ``original_is_public`` if you changed is_public before calling: autoflush writes
HEAD:backend/ee/onyx/db/persona.py:156:    # would otherwise serve pre-lock is_public out of the identity map.
HEAD:backend/ee/onyx/db/persona.py:164:    if original_is_public is None:
HEAD:backend/ee/onyx/db/persona.py:165:        original_is_public = persona.is_public if persona is not None else False
HEAD:backend/ee/onyx/db/persona.py:167:    if is_public is not None or public_permission is not None:
HEAD:backend/ee/onyx/db/persona.py:170:            if is_public is not None:
HEAD:backend/ee/onyx/db/persona.py:171:                persona.is_public = is_public
HEAD:backend/ee/onyx/db/persona.py:196:            original_is_public,
HEAD:backend/ee/onyx/db/scim.py:419:    def get_user_groups(self, user_id: UUID) -> list[tuple[int, str]]:
HEAD:backend/ee/onyx/db/usage_export.py:153:    user_emails = {
HEAD:backend/ee/onyx/db/usage_export.py:164:                user_emails.get(r.requestor_user_id) if r.requestor_user_id else None
HEAD:backend/ee/onyx/db/user_group.py:158:            not persona.is_public
HEAD:backend/ee/onyx/db/user_group.py:279:def fetch_user_groups(
HEAD:backend/ee/onyx/db/user_group.py:319:def fetch_user_groups_for_user(
HEAD:backend/ee/onyx/db/user_group.py:418:def fetch_user_groups_for_documents(
HEAD:backend/ee/onyx/db/user_group.py:646:    """Adding a member hands them the group's grants, so a MANAGE_USER_GROUPS holder
HEAD:backend/ee/onyx/db/user_group.py:725:    # MANAGE_USER_GROUPS holder keeps today's unrestricted attach behavior.
HEAD:backend/ee/onyx/db/user_group.py:727:        has_permission(user, Permission.MANAGE_USER_GROUPS)
HEAD:backend/ee/onyx/db/user_group.py:766:    """Whether ``user`` would still hold global MANAGE_USER_GROUPS with ``group_id`` gone.
HEAD:backend/ee/onyx/db/user_group.py:785:    return Permission.MANAGE_USER_GROUPS.value in resolve_effective_permissions(granted)
HEAD:backend/ee/onyx/db/user_group.py:795:    That will be processed by check_for_vespa_user_groups_sync_task and trigger
HEAD:backend/onyx/access/access.py:9:from onyx.access.models import DocumentAccess
HEAD:backend/onyx/access/access.py:37:) -> DocumentAccess:
HEAD:backend/onyx/access/access.py:43:    doc_access = DocumentAccess.build(
HEAD:backend/onyx/access/access.py:44:        user_emails=info[1] if info and info[1] else [],
HEAD:backend/onyx/access/access.py:45:        user_groups=[],
HEAD:backend/onyx/access/access.py:46:        external_user_emails=[],
HEAD:backend/onyx/access/access.py:48:        is_public=info[2] if info else False,
HEAD:backend/onyx/access/access.py:57:) -> DocumentAccess:
HEAD:backend/onyx/access/access.py:64:def get_null_document_access() -> DocumentAccess:
HEAD:backend/onyx/access/access.py:65:    return DocumentAccess.build(
HEAD:backend/onyx/access/access.py:66:        user_emails=[],
HEAD:backend/onyx/access/access.py:67:        user_groups=[],
HEAD:backend/onyx/access/access.py:68:        is_public=False,
HEAD:backend/onyx/access/access.py:69:        external_user_emails=[],
HEAD:backend/onyx/access/access.py:77:) -> dict[str, DocumentAccess]:
HEAD:backend/onyx/access/access.py:83:    for document_id, user_emails, is_public in document_access_info:
HEAD:backend/onyx/access/access.py:84:        doc_access[document_id] = DocumentAccess.build(
HEAD:backend/onyx/access/access.py:85:            user_emails=[email for email in user_emails if email],
HEAD:backend/onyx/access/access.py:87:            user_groups=[],
HEAD:backend/onyx/access/access.py:88:            is_public=is_public,
HEAD:backend/onyx/access/access.py:89:            external_user_emails=[],
HEAD:backend/onyx/access/access.py:106:) -> dict[str, DocumentAccess]:
HEAD:backend/onyx/access/access.py:145:def source_should_fetch_permissions_during_indexing(source: DocumentSource) -> bool:
HEAD:backend/onyx/access/access.py:146:    _source_should_fetch_permissions_during_indexing_func = cast(
HEAD:backend/onyx/access/access.py:149:            "onyx.external_permissions.sync_params",
HEAD:backend/onyx/access/access.py:150:            "source_should_fetch_permissions_during_indexing",
HEAD:backend/onyx/access/access.py:154:    return _source_should_fetch_permissions_during_indexing_func(source)
HEAD:backend/onyx/access/access.py:160:) -> dict[str, DocumentAccess]:
HEAD:backend/onyx/access/access.py:170:) -> dict[str, DocumentAccess]:
HEAD:backend/onyx/access/access.py:177:) -> dict[str, DocumentAccess]:
HEAD:backend/onyx/access/access.py:189:) -> dict[str, DocumentAccess]:
HEAD:backend/onyx/access/access.py:190:    result: dict[str, DocumentAccess] = {}
HEAD:backend/onyx/access/access.py:192:        emails, is_public = collect_user_file_access(user_file)
HEAD:backend/onyx/access/access.py:193:        result[str(user_file.id)] = DocumentAccess.build(
HEAD:backend/onyx/access/access.py:194:            user_emails=list(emails),
HEAD:backend/onyx/access/access.py:195:            user_groups=[],
HEAD:backend/onyx/access/access.py:196:            is_public=is_public,
HEAD:backend/onyx/access/access.py:197:            external_user_emails=[],
HEAD:backend/onyx/access/access.py:206:    Returns (emails, is_public)."""
HEAD:backend/onyx/access/access.py:208:    is_public = False
HEAD:backend/onyx/access/access.py:212:        if persona.is_public:
HEAD:backend/onyx/access/access.py:213:            is_public = True
HEAD:backend/onyx/access/access.py:218:    return emails, is_public
HEAD:backend/onyx/access/access.py:304:                Persona.is_public.is_(True),
HEAD:backend/onyx/access/access.py:345:        not user_acl.isdisjoint(access.to_acl()) for access in doc_access.values()
HEAD:backend/onyx/access/models.py:18:    external_user_emails: set[str]
HEAD:backend/onyx/access/models.py:22:    is_public: bool
HEAD:backend/onyx/access/models.py:35:            f"external_user_emails={truncate_set(self.external_user_emails)}, "
HEAD:backend/onyx/access/models.py:37:            f"is_public={self.is_public})"
HEAD:backend/onyx/access/models.py:42:        return len(self.external_user_emails) + len(self.external_user_group_ids)
HEAD:backend/onyx/access/models.py:47:            external_user_emails=set(),
HEAD:backend/onyx/access/models.py:49:            is_public=True,
HEAD:backend/onyx/access/models.py:55:        A helper function that returns an *empty* set of external user-emails and group-ids, and sets `is_public` to `False`.
HEAD:backend/onyx/access/models.py:58:        This is especially helpful to use when you are performing permission-syncing, and some document's permissions aren't able
HEAD:backend/onyx/access/models.py:63:            external_user_emails=set(),
HEAD:backend/onyx/access/models.py:65:            is_public=False,
HEAD:backend/onyx/access/models.py:76:    external_access: ExternalAccess
HEAD:backend/onyx/access/models.py:82:            "external_access": {
HEAD:backend/onyx/access/models.py:83:                "external_user_emails": list(self.external_access.external_user_emails),
HEAD:backend/onyx/access/models.py:85:                    self.external_access.external_user_group_ids
HEAD:backend/onyx/access/models.py:87:                "is_public": self.external_access.is_public,
HEAD:backend/onyx/access/models.py:94:        external_access = ExternalAccess(
HEAD:backend/onyx/access/models.py:95:            external_user_emails=set(
HEAD:backend/onyx/access/models.py:96:                data["external_access"].get("external_user_emails", [])
HEAD:backend/onyx/access/models.py:99:                data["external_access"].get("external_user_group_ids", [])
HEAD:backend/onyx/access/models.py:101:            is_public=data["external_access"]["is_public"],
HEAD:backend/onyx/access/models.py:104:            external_access=external_access,
HEAD:backend/onyx/access/models.py:116:    external_access: ExternalAccess
HEAD:backend/onyx/access/models.py:124:            "external_access": {
HEAD:backend/onyx/access/models.py:125:                "external_user_emails": list(self.external_access.external_user_emails),
HEAD:backend/onyx/access/models.py:127:                    self.external_access.external_user_group_ids
HEAD:backend/onyx/access/models.py:129:                "is_public": self.external_access.is_public,
HEAD:backend/onyx/access/models.py:137:        external_access = ExternalAccess(
HEAD:backend/onyx/access/models.py:138:            external_user_emails=set(
HEAD:backend/onyx/access/models.py:139:                data["external_access"].get("external_user_emails", [])
HEAD:backend/onyx/access/models.py:142:                data["external_access"].get("external_user_group_ids", [])
HEAD:backend/onyx/access/models.py:144:            is_public=data["external_access"]["is_public"],
HEAD:backend/onyx/access/models.py:147:            external_access=external_access,
HEAD:backend/onyx/access/models.py:153:# Union type for elements that can have permissions synced
HEAD:backend/onyx/access/models.py:160:class DocumentAccess(ExternalAccess):
HEAD:backend/onyx/access/models.py:162:    user_emails: set[str | None]
HEAD:backend/onyx/access/models.py:165:    user_groups: set[str]
HEAD:backend/onyx/access/models.py:167:    external_user_emails: set[str]
HEAD:backend/onyx/access/models.py:169:    is_public: bool
HEAD:backend/onyx/access/models.py:173:            "Use `DocumentAccess.build(...)` instead of creating an instance directly."
HEAD:backend/onyx/access/models.py:176:    def to_acl(self) -> set[str]:
HEAD:backend/onyx/access/models.py:183:        for user_email in self.user_emails:
HEAD:backend/onyx/access/models.py:187:        for group_name in self.user_groups:
HEAD:backend/onyx/access/models.py:190:        for external_user_email in self.external_user_emails:
HEAD:backend/onyx/access/models.py:196:        if self.is_public:
HEAD:backend/onyx/access/models.py:204:        user_emails: list[str | None],
HEAD:backend/onyx/access/models.py:205:        user_groups: list[str],
HEAD:backend/onyx/access/models.py:206:        external_user_emails: list[str],
HEAD:backend/onyx/access/models.py:208:        is_public: bool,
HEAD:backend/onyx/access/models.py:209:    ) -> "DocumentAccess":
HEAD:backend/onyx/access/models.py:210:        """Don't prefix incoming data wth acl type, prefix on read from to_acl!"""
HEAD:backend/onyx/access/models.py:214:            obj, "user_emails", {user_email for user_email in user_emails if user_email}
HEAD:backend/onyx/access/models.py:216:        object.__setattr__(obj, "user_groups", set(user_groups))
HEAD:backend/onyx/access/models.py:219:            "external_user_emails",
HEAD:backend/onyx/access/models.py:220:            {external_email for external_email in external_user_emails},
HEAD:backend/onyx/access/models.py:227:        object.__setattr__(obj, "is_public", is_public)
HEAD:backend/onyx/access/models.py:232:default_public_access = DocumentAccess.build(
HEAD:backend/onyx/access/models.py:233:    external_user_emails=[],
HEAD:backend/onyx/access/models.py:235:    user_emails=[],
HEAD:backend/onyx/access/models.py:236:    user_groups=[],
HEAD:backend/onyx/access/models.py:237:    is_public=True,
HEAD:backend/onyx/document_index/FILTER_SEMANTICS.md:13:| **ACL** | `access_control_list` | OR within, AND with rest |
HEAD:backend/onyx/document_index/FILTER_SEMANTICS.md:159:| `access_control_list` | `access_control_list` | `weightedset<string>` | ACL entries for the requesting user |
HEAD:backend/onyx/document_index/document_metadata.py:33:    external_access: ExternalAccess | None = None
HEAD:backend/onyx/document_index/interfaces_new.py:8:from onyx.access.models import DocumentAccess
HEAD:backend/onyx/document_index/interfaces_new.py:145:    access: DocumentAccess | None = None
HEAD:backend/onyx/document_index/interfaces_new.py:187:    access_control_list: frozenset[str] = frozenset({PUBLIC_DOC_PAT})
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:7:from onyx.access.models import DocumentAccess
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:49:    ACCESS_CONTROL_LIST_FIELD_NAME,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:96:def generate_opensearch_filtered_access_control_list(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:97:    access: DocumentAccess,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:103:    access_control_list = access.to_acl()
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:104:    access_control_list.discard(PUBLIC_DOC_PAT)
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:105:    return list(access_control_list)
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:235:        public=chunk.access.is_public,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:236:        access_control_list=generate_opensearch_filtered_access_control_list(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:636:                properties_to_update[ACCESS_CONTROL_LIST_FIELD_NAME] = (
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:637:                    generate_opensearch_filtered_access_control_list(
HEAD:backend/onyx/document_index/opensearch/schema.py:48:ACCESS_CONTROL_LIST_FIELD_NAME = "access_control_list"
HEAD:backend/onyx/document_index/opensearch/schema.py:174:    access_control_list: list[str]
HEAD:backend/onyx/document_index/opensearch/schema.py:480:                # is its own field. If true, ACCESS_CONTROL_LIST_FIELD_NAME
HEAD:backend/onyx/document_index/opensearch/schema.py:490:                ACCESS_CONTROL_LIST_FIELD_NAME: {"type": "keyword"},
HEAD:backend/onyx/document_index/opensearch/schema.py:493:                # PUBLIC_FIELD_NAME and ACCESS_CONTROL_LIST_FIELD_NAME; up to
HEAD:backend/onyx/document_index/opensearch/search.py:24:    ACCESS_CONTROL_LIST_FIELD_NAME,
HEAD:backend/onyx/document_index/opensearch/search.py:221:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:288:            access_control_list=None,
HEAD:backend/onyx/document_index/opensearch/search.py:389:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:486:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:570:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:633:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:874:        access_control_list: list[str] | None,
HEAD:backend/onyx/document_index/opensearch/search.py:909:            access_control_list: Access control list for the documents to
HEAD:backend/onyx/document_index/opensearch/search.py:960:            access_control_list: list[str],
HEAD:backend/onyx/document_index/opensearch/search.py:968:                access_control_list: The access control list to restrict
HEAD:backend/onyx/document_index/opensearch/search.py:985:            if access_control_list:
HEAD:backend/onyx/document_index/opensearch/search.py:986:                if len(access_control_list) > MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY:
HEAD:backend/onyx/document_index/opensearch/search.py:988:                        f"Too many access control list entries: {len(access_control_list)}. Max allowed: {MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY}."
HEAD:backend/onyx/document_index/opensearch/search.py:995:                    "terms": {ACCESS_CONTROL_LIST_FIELD_NAME: list(access_control_list)}
HEAD:backend/onyx/document_index/opensearch/search.py:1270:        if access_control_list is not None:
HEAD:backend/onyx/document_index/opensearch/search.py:1276:            filter_clauses.append(_get_acl_visibility_filter(access_control_list))
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:159:        field access_control_list type weightedset<string> {
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:31:    ACCESS_CONTROL_LIST,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:183:    acl_fieldset_entry = f"{ACCESS_CONTROL_LIST}"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:186:        and filters.access_control_list
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:259:                if filters.access_control_list:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:260:                    document_acl = document["fields"].get(ACCESS_CONTROL_LIST)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:263:                        for user_acl_entry in filters.access_control_list
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:463:#         filters=filters or IndexFilters(access_control_list=None),
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:28:    ACCESS_CONTROL_LIST,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:218:        ACCESS_CONTROL_LIST: {acl_entry: 1 for acl_entry in chunk.access.to_acl()},
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:7:    ACCESS_CONTROL_LIST,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:51:        access_control_list where a single user may have tens of thousands
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:192:    # access_control_list weightedset<string> field.  OR-chaining thousands
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:195:    if filters.access_control_list is not None:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:199:                ACCESS_CONTROL_LIST, filters.access_control_list
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:511:        access_control_list: _AccessControl | None = None
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:534:            assign={acl_entry: 1 for acl_entry in update_request.access.to_acl()}
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:558:        access_control_list=access_update,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1040:            filters=IndexFilters(access_control_list=None, tenant_id=self._tenant_id),
HEAD:backend/onyx/document_index/vespa_constants.py:58:ACCESS_CONTROL_LIST = "access_control_list"
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:8:from onyx.access.models import DocumentAccess
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:133:        no_access = DocumentAccess.build(
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:134:            user_emails=[],
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:135:            user_groups=[],
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:136:            external_user_emails=[],
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:138:            is_public=False,
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:274:        doc_id_to_access_info: dict[str, DocumentAccess],
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:280:        no_access: DocumentAccess,
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:15:from onyx.access.models import DocumentAccess
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:150:        no_access = DocumentAccess.build(
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:151:            user_emails=[],
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:152:            user_groups=[],
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:153:            external_user_emails=[],
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:155:            is_public=False,
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:166:        user_file_id_to_access: dict[str, DocumentAccess] = get_access_for_user_files(
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:308:        user_file_id_to_access: dict[str, DocumentAccess],
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:315:        no_access: DocumentAccess,
HEAD:backend/onyx/indexing/indexing_pipeline.py:221:            external_access=doc.external_access,
HEAD:backend/onyx/indexing/models.py:7:from onyx.access.models import DocumentAccess
HEAD:backend/onyx/indexing/models.py:109:    access: "DocumentAccess"
HEAD:backend/onyx/indexing/models.py:124:        access: "DocumentAccess",
```
Document access metadata is propagated into indexing-related code.
This is important because retrieval enforcement depends on indexed ACL state
remaining synchronized with authoritative permissions.
## Index-Time Tenant Metadata
Evidence lines: 169
```text
HEAD:backend/onyx/document_index/FILTER_SEMANTICS.md:12:| **Tenant** | `tenant_id` | AND (multi-tenant only) |
HEAD:backend/onyx/document_index/FILTER_SEMANTICS.md:164:| `tenant_id` | `tenant_id` | `string` | Tenant isolation (multi-tenant) |
HEAD:backend/onyx/document_index/document_index_utils.py:82:    tenant_id: str,
HEAD:backend/onyx/document_index/document_index_utils.py:97:                        tenant_id=tenant_id,
HEAD:backend/onyx/document_index/document_index_utils.py:128:                            tenant_id=tenant_id,
HEAD:backend/onyx/document_index/document_index_utils.py:140:    tenant_id: str,
HEAD:backend/onyx/document_index/document_index_utils.py:156:        unique_identifier_string += "_" + tenant_id
HEAD:backend/onyx/document_index/document_index_utils.py:190:        tenant_id=chunk.tenant_id,
HEAD:backend/onyx/document_index/factory.py:12:from onyx.document_index.interfaces_new import DocumentIndex, TenantState
HEAD:backend/onyx/document_index/factory.py:23:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/onyx/document_index/factory.py:26:def _build_tenant_state() -> TenantState:
HEAD:backend/onyx/document_index/factory.py:27:    return TenantState(tenant_id=get_current_tenant_id(), multitenant=MULTI_TENANT)
HEAD:backend/onyx/document_index/interfaces_new.py:43:class TenantState(BaseModel):
HEAD:backend/onyx/document_index/interfaces_new.py:52:    tenant_id: str
HEAD:backend/onyx/document_index/interfaces_new.py:57:            f"TenantState(tenant_id={self.tenant_id}, multitenant={self.multitenant})"
HEAD:backend/onyx/document_index/interfaces_new.py:61:    def check_tenant_id_is_set_in_multitenant_mode(self) -> Self:
HEAD:backend/onyx/document_index/interfaces_new.py:62:        if self.multitenant and not self.tenant_id:
HEAD:backend/onyx/document_index/opensearch/client.py:35:from onyx.document_index.interfaces_new import TenantState
HEAD:backend/onyx/document_index/opensearch/client.py:907:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/opensearch/client.py:929:            tenant_state.tenant_id,
HEAD:backend/onyx/document_index/opensearch/client.py:987:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/opensearch/client.py:1029:            tenant_state.tenant_id,
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:9:from onyx.document_index.interfaces_new import TenantState
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:11:from onyx.document_index.opensearch.schema import TENANT_ID_FIELD_NAME
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:24:def reclaim_index_data(index_name: str, tenant_state: TenantState) -> ReclaimOutcome:
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:49:            "query": {"term": {TENANT_ID_FIELD_NAME: {"value": tenant_state.tenant_id}}}
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:60:            tenant_state.tenant_id,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:36:    TenantState,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:268:        tenant_id=TenantState(tenant_id=chunk.tenant_id, multitenant=MULTI_TENANT),
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:299:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:305:        self._tenant_state: TenantState = tenant_state
HEAD:backend/onyx/document_index/opensearch/schema.py:22:from onyx.document_index.interfaces_new import TenantState
HEAD:backend/onyx/document_index/opensearch/schema.py:35:from onyx.utils.tenant import get_tenant_id_short_string
HEAD:backend/onyx/document_index/opensearch/schema.py:37:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/onyx/document_index/opensearch/schema.py:61:TENANT_ID_FIELD_NAME = "tenant_id"
HEAD:backend/onyx/document_index/opensearch/schema.py:78:    tenant_state: TenantState,
HEAD:backend/onyx/document_index/opensearch/schema.py:98:        short_tenant_id: str = get_tenant_id_short_string(tenant_state.tenant_id)
HEAD:backend/onyx/document_index/opensearch/schema.py:102:        opensearch_doc_chunk_id_tenant_prefix = f"{short_tenant_id}__"
HEAD:backend/onyx/document_index/opensearch/schema.py:145:    get_current_tenant_id. Generally relying on global state is bad, in this
HEAD:backend/onyx/document_index/opensearch/schema.py:209:    tenant_id: TenantState = Field(
HEAD:backend/onyx/document_index/opensearch/schema.py:210:        default_factory=lambda: TenantState(
HEAD:backend/onyx/document_index/opensearch/schema.py:211:            tenant_id=get_current_tenant_id(), multitenant=MULTI_TENANT
HEAD:backend/onyx/document_index/opensearch/schema.py:218:            f"content length={len(self.content)}, tenant_id={self.tenant_id.tenant_id})."
HEAD:backend/onyx/document_index/opensearch/schema.py:280:    @field_serializer("tenant_id", mode="wrap")
HEAD:backend/onyx/document_index/opensearch/schema.py:283:        value: TenantState,
HEAD:backend/onyx/document_index/opensearch/schema.py:291:        tenant_id field, so we don't want to supply it in our serialized
HEAD:backend/onyx/document_index/opensearch/schema.py:298:            return value.tenant_id
HEAD:backend/onyx/document_index/opensearch/schema.py:300:    @field_validator("tenant_id", mode="before")
HEAD:backend/onyx/document_index/opensearch/schema.py:302:    def parse_tenant_id(cls, value: Any) -> TenantState:
HEAD:backend/onyx/document_index/opensearch/schema.py:304:        Generates a TenantState from OpenSearch's tenant_id if it exists, or
HEAD:backend/onyx/document_index/opensearch/schema.py:311:                    "Bug: No tenant_id was supplied but multi-tenant mode is enabled."
HEAD:backend/onyx/document_index/opensearch/schema.py:313:            return TenantState(
HEAD:backend/onyx/document_index/opensearch/schema.py:314:                tenant_id=get_current_tenant_id(), multitenant=MULTI_TENANT
HEAD:backend/onyx/document_index/opensearch/schema.py:316:        elif isinstance(value, TenantState):
HEAD:backend/onyx/document_index/opensearch/schema.py:319:                    f"Bug: An existing TenantState object was supplied to the DocumentChunk model "
HEAD:backend/onyx/document_index/opensearch/schema.py:326:                f"Bug: Expected a str for the tenant_id property from OpenSearch, got {type(value)} instead."
HEAD:backend/onyx/document_index/opensearch/schema.py:331:                    "Bug: Got a non-null str for the tenant_id property from OpenSearch but "
HEAD:backend/onyx/document_index/opensearch/schema.py:333:                    "mode we don't expect to see a tenant_id."
HEAD:backend/onyx/document_index/opensearch/schema.py:335:            return TenantState(tenant_id=value, multitenant=MULTI_TENANT)
HEAD:backend/onyx/document_index/opensearch/schema.py:354:            f"tenant_id={self.tenant_id.tenant_id})"
HEAD:backend/onyx/document_index/opensearch/schema.py:582:            schema["properties"][TENANT_ID_FIELD_NAME] = {"type": "keyword"}
HEAD:backend/onyx/document_index/opensearch/search.py:13:from onyx.document_index.interfaces_new import TenantState
HEAD:backend/onyx/document_index/opensearch/search.py:39:    TENANT_ID_FIELD_NAME,
HEAD:backend/onyx/document_index/opensearch/search.py:180:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/opensearch/search.py:261:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/opensearch/search.py:313:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/opensearch/search.py:323:        # Single-tenant indices have no tenant_id field (added only in multitenant mode);
HEAD:backend/onyx/document_index/opensearch/search.py:327:                {"term": {TENANT_ID_FIELD_NAME: {"value": tenant_state.tenant_id}}}
HEAD:backend/onyx/document_index/opensearch/search.py:343:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/opensearch/search.py:453:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/opensearch/search.py:537:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/opensearch/search.py:616:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/opensearch/search.py:872:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/opensearch/search.py:1366:                {"term": {TENANT_ID_FIELD_NAME: {"value": tenant_state.tenant_id}}}
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:11:        field tenant_id type string {
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:23:from onyx.document_index.interfaces_new import TenantState
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:56:    TENANT_ID,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:192:        tenant_id_fieldset_entry = f"{TENANT_ID}"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:193:        if field_set_list and tenant_id_fieldset_entry not in field_set_list:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:194:            field_set_list.append(tenant_id_fieldset_entry)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:210:    # enforcing tenant_id through a == condition
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:212:        if filters.tenant_id:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:213:            selection += f" and {index_name}.tenant_id=='{filters.tenant_id}'"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:268:                    if not filters.tenant_id:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:270:                    document_tenant_id = document["fields"].get(TENANT_ID)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:271:                    if document_tenant_id != filters.tenant_id:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:277:                            filters.tenant_id,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:294:    tenant_state: TenantState,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:318:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:336:            selection += f" and {index_name}.tenant_id=='{tenant_state.tenant_id}'"
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:57:    TENANT_ID,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:229:        if chunk.tenant_id:
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:230:            vespa_document_fields[TENANT_ID] = chunk.tenant_id
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:6:from onyx.document_index.interfaces_new import TenantState
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:20:    tenant_id: str,
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:25:        tenant_state=TenantState(tenant_id=tenant_id, multitenant=MULTI_TENANT),
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:31:        kg_update_requests=kg_update_requests, tenant_id=tenant_id
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:16:    TENANT_ID,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:26:def build_tenant_id_filter(tenant_id: str) -> str:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:27:    return f'({TENANT_ID} contains "{tenant_id}")'
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:187:    # TODO: add error condition if MULTI_TENANT and no tenant_id filter is set
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:188:    if filters.tenant_id and MULTI_TENANT:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:189:        filter_parts.append(build_tenant_id_filter(filters.tenant_id))
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:46:    TenantState,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:608:        tenant_state: TenantState,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:613:        self._tenant_id = tenant_state.tenant_id
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:743:                tenant_id=self._tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:800:                tenant_id=self._tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:846:                        tenant_id=self._tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1040:            filters=IndexFilters(access_control_list=None, tenant_id=self._tenant_id),
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1069:            tenant_state=TenantState(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1070:                tenant_id=self._tenant_id, multitenant=MULTI_TENANT
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1091:                        tenant_id=self._tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1112:            f'tenant_id contains "{self._tenant_id}"' if self._multitenant else "true"
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1114:        yql = f"select documentid from {self._index_name} where {where_clause} limit 0"  # noqa: S608 - Vespa YQL with internal index_name/tenant_id
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1184:        tenant_id: str,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1203:                tenant_id=tenant_id,
HEAD:backend/onyx/document_index/vespa_constants.py:46:TENANT_ID = "tenant_id"
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:56:        tenant_id: str,
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:61:        self.tenant_id = tenant_id
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:118:        tenant_id: str,
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:152:                context.updatable_docs, tenant_id, db_session
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:164:            tenant_id=tenant_id,
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:176:        tenant_id: str,
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:191:        redis_client = get_redis_client(tenant_id=tenant_id)
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:281:        tenant_id: str,
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:288:        self._tenant_id = tenant_id
HEAD:backend/onyx/indexing/adapters/document_indexing_adapter.py:310:            tenant_id=self._tenant_id,
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:82:    def __init__(self, tenant_id: str, db_session: Session):
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:83:        self.tenant_id = tenant_id
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:129:        tenant_id: str,
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:215:            tenant_id=tenant_id,
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:316:        tenant_id: str,
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:322:        self._tenant_id = tenant_id
HEAD:backend/onyx/indexing/adapters/user_file_indexing_adapter.py:344:            tenant_id=self._tenant_id,
HEAD:backend/onyx/indexing/embedder.py:82:        tenant_id: str | None = None,
HEAD:backend/onyx/indexing/embedder.py:121:        tenant_id: str | None = None,
HEAD:backend/onyx/indexing/embedder.py:156:            tenant_id=tenant_id,
HEAD:backend/onyx/indexing/embedder.py:175:                tenant_id=tenant_id,
HEAD:backend/onyx/indexing/embedder.py:212:                        tenant_id=tenant_id,
HEAD:backend/onyx/indexing/embedder.py:254:    tenant_id: str | None = None,
HEAD:backend/onyx/indexing/embedder.py:268:                chunks=chunks, tenant_id=tenant_id, request_id=request_id
HEAD:backend/onyx/indexing/embedder.py:293:                chunks=chunks_for_doc, tenant_id=tenant_id, request_id=request_id
HEAD:backend/onyx/indexing/embedder.py:300:                if tenant_id:
HEAD:backend/onyx/indexing/embedder.py:301:                    scope.set_tag("tenant_id", tenant_id)
HEAD:backend/onyx/indexing/indexing_pipeline.py:249:    tenant_id: str,
HEAD:backend/onyx/indexing/indexing_pipeline.py:281:            tenant_id=tenant_id,
HEAD:backend/onyx/indexing/indexing_pipeline.py:320:    tenant_id: str,
HEAD:backend/onyx/indexing/indexing_pipeline.py:337:        with embed_and_stream(chunks, embedder, tenant_id, req_id) as (result, store):
HEAD:backend/onyx/indexing/indexing_pipeline.py:346:            tenant_id=tenant_id,
HEAD:backend/onyx/indexing/indexing_pipeline.py:435:    tenant_id: str,
HEAD:backend/onyx/indexing/indexing_pipeline.py:452:            tenant_id=tenant_id,
HEAD:backend/onyx/indexing/indexing_pipeline.py:471:            scope.set_tag("tenant_id", tenant_id)
HEAD:backend/onyx/indexing/indexing_pipeline.py:1365:    tenant_id: str,
HEAD:backend/onyx/indexing/indexing_pipeline.py:1390:        "Starting index_doc_batch: connector_id=%s, credential_id=%s, tenant_id=%s, num_docs=%s",
HEAD:backend/onyx/indexing/indexing_pipeline.py:1393:        tenant_id,
HEAD:backend/onyx/indexing/indexing_pipeline.py:1493:        chunks, embedder, tenant_id, request_id, attempt_id=attempt_id
HEAD:backend/onyx/indexing/indexing_pipeline.py:1524:                tenant_id=tenant_id,
HEAD:backend/onyx/indexing/indexing_pipeline.py:1567:                        tenant_id=tenant_id,
HEAD:backend/onyx/indexing/indexing_pipeline.py:1655:    tenant_id: str,
HEAD:backend/onyx/indexing/indexing_pipeline.py:1722:            tenant_id=tenant_id,
HEAD:backend/onyx/indexing/models.py:108:    tenant_id: str
HEAD:backend/onyx/indexing/models.py:130:        tenant_id: str,
HEAD:backend/onyx/indexing/models.py:141:            tenant_id=tenant_id,
HEAD:backend/onyx/indexing/models.py:273:        tenant_id: str,
HEAD:backend/onyx/indexing/persistent_indexing.py:69:    tenant_id: str,
HEAD:backend/onyx/indexing/persistent_indexing.py:83:            scope.set_tag("tenant_id", tenant_id)
HEAD:backend/onyx/indexing/vector_db_insertion.py:35:    tenant_id: str,
HEAD:backend/onyx/indexing/vector_db_insertion.py:104:                scope.set_tag("tenant_id", tenant_id)
```
Tenant identifiers are explicit parts of document-index behavior.
Their presence does not by itself prove cross-tenant isolation.
## Search and Retrieval
Evidence lines: 412
```text
HEAD:backend/ee/onyx/server/query_and_chat/models.py:31:class SendSearchQueryRequest(BaseModel):
HEAD:backend/ee/onyx/server/query_and_chat/models.py:37:    hybrid_alpha: float | None = None
HEAD:backend/ee/onyx/server/query_and_chat/models.py:101:class SearchQueryResponse(BaseModel):
HEAD:backend/ee/onyx/server/query_and_chat/models.py:108:    search_queries: list[SearchQueryResponse]
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:8:multi-stage retrieval used by chat mode), see
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:31:    SearchQueryResponse,
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:32:    SendSearchQueryRequest,
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:36:from onyx.configs.app_configs import ONYX_SEARCH_UI_USES_OPENSEARCH_KEYWORD_SEARCH
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:123:    request: SendSearchQueryRequest,
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:130:    If hybrid_alpha is unset and ONYX_SEARCH_UI_USES_OPENSEARCH_KEYWORD_SEARCH
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:138:    if request.hybrid_alpha is None and ONYX_SEARCH_UI_USES_OPENSEARCH_KEYWORD_SEARCH:
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:139:        request.hybrid_alpha = 0.0
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:215:            SearchQueryResponse(
HEAD:backend/onyx/document_index/chunk_content_enrichment.py:44:        chunks: Chunks as retrieved from the document index with indexing
HEAD:backend/onyx/document_index/disabled.py:62:    def id_based_retrieval(
HEAD:backend/onyx/document_index/disabled.py:66:        batch_retrieval: bool = False,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:70:    def hybrid_retrieval(
HEAD:backend/onyx/document_index/disabled.py:73:        query_embedding: Embedding,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:77:        num_to_retrieve: int,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:81:    def keyword_retrieval(
HEAD:backend/onyx/document_index/disabled.py:85:        num_to_retrieve: int,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:90:    def semantic_retrieval(
HEAD:backend/onyx/document_index/disabled.py:92:        query_embedding: Embedding,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:94:        num_to_retrieve: int,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:98:    def random_retrieval(
HEAD:backend/onyx/document_index/disabled.py:101:        num_to_retrieve: int = 10,  # noqa: ARG002
HEAD:backend/onyx/document_index/factory.py:10:from onyx.db.opensearch_migration import get_opensearch_retrieval_state
HEAD:backend/onyx/document_index/factory.py:117:    """Gets the default document index for retrieval.
HEAD:backend/onyx/document_index/factory.py:126:    opensearch_retrieval_enabled = get_opensearch_retrieval_state(db_session)
HEAD:backend/onyx/document_index/factory.py:127:    if ONYX_DISABLE_VESPA and not opensearch_retrieval_enabled:
HEAD:backend/onyx/document_index/factory.py:129:            "Bug: ONYX_DISABLE_VESPA is set but opensearch_retrieval_enabled is not set."
HEAD:backend/onyx/document_index/factory.py:132:    if opensearch_retrieval_enabled:
HEAD:backend/onyx/document_index/interfaces_new.py:37:    "IdRetrievalCapable",
HEAD:backend/onyx/document_index/interfaces_new.py:38:    "HybridCapable",
HEAD:backend/onyx/document_index/interfaces_new.py:170:class IndexRetrievalFilters(BaseModel):
HEAD:backend/onyx/document_index/interfaces_new.py:175:    chunk content. Should be passed in for every retrieval method.
HEAD:backend/onyx/document_index/interfaces_new.py:177:    TODO(andrei): Currently unused, use this when making retrieval methods more
HEAD:backend/onyx/document_index/interfaces_new.py:327:class IdRetrievalCapable(abc.ABC):
HEAD:backend/onyx/document_index/interfaces_new.py:329:    Class must implement the ability to retrieve either:
HEAD:backend/onyx/document_index/interfaces_new.py:335:    def id_based_retrieval(
HEAD:backend/onyx/document_index/interfaces_new.py:342:        batch_retrieval: bool = False,
HEAD:backend/onyx/document_index/interfaces_new.py:343:        # TODO(andrei): Add a param for whether to retrieve hidden docs.
HEAD:backend/onyx/document_index/interfaces_new.py:355:                range to retrieve.
HEAD:backend/onyx/document_index/interfaces_new.py:363:class HybridCapable(abc.ABC):
HEAD:backend/onyx/document_index/interfaces_new.py:365:    Class must implement hybrid (keyword + vector) search functionality.
HEAD:backend/onyx/document_index/interfaces_new.py:369:    def hybrid_retrieval(
HEAD:backend/onyx/document_index/interfaces_new.py:372:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/interfaces_new.py:378:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/interfaces_new.py:380:        """Runs hybrid search and returns a list of inference chunks.
HEAD:backend/onyx/document_index/interfaces_new.py:385:            query_embedding: Vector representation of the query. Must be of the
HEAD:backend/onyx/document_index/interfaces_new.py:393:            num_to_retrieve: Number of highest matching chunks to return.
HEAD:backend/onyx/document_index/interfaces_new.py:401:    def keyword_retrieval(
HEAD:backend/onyx/document_index/interfaces_new.py:405:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/interfaces_new.py:414:            num_to_retrieve: Number of highest matching chunks to return.
HEAD:backend/onyx/document_index/interfaces_new.py:426:    def semantic_retrieval(
HEAD:backend/onyx/document_index/interfaces_new.py:428:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/interfaces_new.py:430:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/interfaces_new.py:435:            query_embedding: Vector representation of the query. Must be of the
HEAD:backend/onyx/document_index/interfaces_new.py:439:            num_to_retrieve: Number of highest matching chunks to return.
HEAD:backend/onyx/document_index/interfaces_new.py:449:    Class must implement random document retrieval.
HEAD:backend/onyx/document_index/interfaces_new.py:453:    def random_retrieval(
HEAD:backend/onyx/document_index/interfaces_new.py:457:        num_to_retrieve: int = 10,
HEAD:backend/onyx/document_index/interfaces_new.py:460:        """Retrieves random chunks matching the filters.
HEAD:backend/onyx/document_index/interfaces_new.py:465:            num_to_retrieve: Number of chunks to retrieve. Defaults to 10.
HEAD:backend/onyx/document_index/interfaces_new.py:466:            dirty: If set, retrieve chunks whose "dirty" flag matches this
HEAD:backend/onyx/document_index/interfaces_new.py:467:                argument. If None, there is no restriction on retrieved chunks
HEAD:backend/onyx/document_index/interfaces_new.py:483:    HybridCapable,
HEAD:backend/onyx/document_index/interfaces_new.py:484:    IdRetrievalCapable,
HEAD:backend/onyx/document_index/interfaces_new.py:497:    - Run hybrid search
HEAD:backend/onyx/document_index/interfaces_new.py:498:    - Retrieve document or sections of documents based on document id
HEAD:backend/onyx/document_index/interfaces_new.py:499:    - Retrieve sets of random documents
HEAD:backend/onyx/document_index/opensearch/README.md:6:an intermediate phase (seemingly built specifically to handle hybrid search queries) which can run in between as a processor.
HEAD:backend/onyx/document_index/opensearch/README.md:10:https://docs.opensearch.org/latest/query-dsl/compound/hybrid/
HEAD:backend/onyx/document_index/opensearch/README.md:12:## How Hybrid queries work
HEAD:backend/onyx/document_index/opensearch/README.md:13:Hybrid queries are basically parallel queries that each run through their own `Search` phase and do not interact in any way.
HEAD:backend/onyx/document_index/opensearch/README.md:17:When the normalization processor is applied to keyword/vector hybrid searches, documents that show up due to keyword match may
HEAD:backend/onyx/document_index/opensearch/README.md:58:work that is relevant for the hybrid search. Since the Rescore happens prior to normalization, it's not able to provide any
HEAD:backend/onyx/document_index/opensearch/client.py:89:    # The document chunk source retrieved from OpenSearch.
HEAD:backend/onyx/document_index/opensearch/client.py:93:    # score is not relevant like direct retrieval on ID.
HEAD:backend/onyx/document_index/opensearch/client.py:307:        self._client = OpenSearch(
HEAD:backend/onyx/document_index/opensearch/client.py:1563:    def search(
HEAD:backend/onyx/document_index/opensearch/client.py:1605:                result = self._client.search(
HEAD:backend/onyx/document_index/opensearch/client.py:1630:                    observe_opensearch_search(search_type, client_duration_s, time_took)
HEAD:backend/onyx/document_index/opensearch/client.py:1708:                result: dict[str, Any] = self._client.search(
HEAD:backend/onyx/document_index/opensearch/client.py:1729:                    observe_opensearch_search(search_type, client_duration_s, time_took)
HEAD:backend/onyx/document_index/opensearch/client.py:1835:        # search() applies; we still detect a server-side timeout below so a
HEAD:backend/onyx/document_index/opensearch/client.py:1838:            result = self._client.search(
HEAD:backend/onyx/document_index/opensearch/client.py:1852:            result = self._client.search(
HEAD:backend/onyx/document_index/opensearch/client.py:2070:            track_opensearch_search(search_type)
HEAD:backend/onyx/document_index/opensearch/constants.py:16:# cutoff filtering during retrieval.
HEAD:backend/onyx/document_index/opensearch/constants.py:28:# When performing hybrid search, we need to consider more candidates than the
HEAD:backend/onyx/document_index/opensearch/constants.py:29:# number of results to be returned. This is because the scoring is hybrid and
HEAD:backend/onyx/document_index/opensearch/constants.py:30:# the results are reordered due to the hybrid scoring. Higher = more candidates
HEAD:backend/onyx/document_index/opensearch/constants.py:31:# for hybrid fusion = better retrieval accuracy, but results in more computation
HEAD:backend/onyx/document_index/opensearch/constants.py:35:# good hybrid ranking for the 10 results. If we fetch 1000 candidates from each,
HEAD:backend/onyx/document_index/opensearch/constants.py:41:DEFAULT_NUM_HYBRID_SUBQUERY_CANDIDATES = int(
HEAD:backend/onyx/document_index/opensearch/constants.py:42:    os.environ.get("DEFAULT_NUM_HYBRID_SUBQUERY_CANDIDATES", 500)
HEAD:backend/onyx/document_index/opensearch/constants.py:52:EF_SEARCH = DEFAULT_NUM_HYBRID_SUBQUERY_CANDIDATES
HEAD:backend/onyx/document_index/opensearch/constants.py:71:    HYBRID = "hybrid"
HEAD:backend/onyx/document_index/opensearch/constants.py:75:    DOC_ID_RETRIEVAL = "doc_id_retrieval"
HEAD:backend/onyx/document_index/opensearch/constants.py:79:class HybridSearchSubqueryConfiguration(Enum):
HEAD:backend/onyx/document_index/opensearch/constants.py:85:# Will raise and block application start if HYBRID_SEARCH_SUBQUERY_CONFIGURATION
HEAD:backend/onyx/document_index/opensearch/constants.py:88:HYBRID_SEARCH_SUBQUERY_CONFIGURATION: HybridSearchSubqueryConfiguration = (
HEAD:backend/onyx/document_index/opensearch/constants.py:89:    HybridSearchSubqueryConfiguration(
HEAD:backend/onyx/document_index/opensearch/constants.py:90:        int(os.environ["HYBRID_SEARCH_SUBQUERY_CONFIGURATION"])
HEAD:backend/onyx/document_index/opensearch/constants.py:92:    if os.environ.get("HYBRID_SEARCH_SUBQUERY_CONFIGURATION", None) is not None
HEAD:backend/onyx/document_index/opensearch/constants.py:93:    else HybridSearchSubqueryConfiguration.CONTENT_VECTOR_TITLE_CONTENT_COMBINED_KEYWORD
HEAD:backend/onyx/document_index/opensearch/constants.py:97:class HybridSearchNormalizationPipeline(Enum):
HEAD:backend/onyx/document_index/opensearch/constants.py:100:    # NOTE: Using z-score normalization is better for hybrid search from a
HEAD:backend/onyx/document_index/opensearch/constants.py:103:    # https://opensearch.org/blog/introducing-the-z-score-normalization-technique-for-hybrid-search/
HEAD:backend/onyx/document_index/opensearch/constants.py:107:# Will raise and block application start if HYBRID_SEARCH_NORMALIZATION_PIPELINE
HEAD:backend/onyx/document_index/opensearch/constants.py:109:HYBRID_SEARCH_NORMALIZATION_PIPELINE: HybridSearchNormalizationPipeline = (
HEAD:backend/onyx/document_index/opensearch/constants.py:110:    HybridSearchNormalizationPipeline(
HEAD:backend/onyx/document_index/opensearch/constants.py:111:        int(os.environ["HYBRID_SEARCH_NORMALIZATION_PIPELINE"])
HEAD:backend/onyx/document_index/opensearch/constants.py:113:    if os.environ.get("HYBRID_SEARCH_NORMALIZATION_PIPELINE", None) is not None
HEAD:backend/onyx/document_index/opensearch/constants.py:114:    else HybridSearchNormalizationPipeline.MIN_MAX
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:133:def convert_retrieved_opensearch_chunk_to_inference_chunk_uncleaned(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:145:            relevant for searches like hybrid search. It is acceptable for this
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:147:            retrieval as a match score makes no sense in those contexts.
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:277:    This class provides document indexing, retrieval, and management operations
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:739:    def id_based_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:745:        batch_retrieval: bool = False,  # noqa: ARG002
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:746:        # TODO(andrei): Add a param for whether to retrieve hidden docs.
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:749:        TODO(andrei): Consider implementing this method to retrieve on document
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:775:            search_hits = self._client.search(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:778:                search_type=OpenSearchSearchType.DOC_ID_RETRIEVAL,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:781:                convert_retrieved_opensearch_chunk_to_inference_chunk_uncleaned(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:792:    def hybrid_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:795:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:800:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:805:            "[OpenSearchDocumentIndex] Hybrid retrieving %s chunks for index %s.",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:806:            num_to_retrieve,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:813:        query_body = DocumentQuery.get_hybrid_search_query(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:815:            query_vector=query_embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:816:            num_hits=num_to_retrieve,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:828:        search_hits: list[SearchHit[DocumentChunkWithoutVectors]] = self._client.search(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:831:            search_type=OpenSearchSearchType.HYBRID,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:837:            convert_retrieved_opensearch_chunk_to_inference_chunk_uncleaned(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:848:    def keyword_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:852:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:859:            num_to_retrieve,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:862:        query_body = DocumentQuery.get_keyword_search_query(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:864:            num_hits=num_to_retrieve,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:875:        search_hits: list[SearchHit[DocumentChunkWithoutVectors]] = self._client.search(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:882:            convert_retrieved_opensearch_chunk_to_inference_chunk_uncleaned(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:893:    def semantic_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:895:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:897:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:903:            num_to_retrieve,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:906:        query_body = DocumentQuery.get_semantic_search_query(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:907:            query_embedding=query_embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:908:            num_hits=num_to_retrieve,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:919:        search_hits: list[SearchHit[DocumentChunkWithoutVectors]] = self._client.search(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:926:            convert_retrieved_opensearch_chunk_to_inference_chunk_uncleaned(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:937:    def random_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:940:        num_to_retrieve: int = 10,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:945:            num_to_retrieve,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:951:            num_to_retrieve=num_to_retrieve,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:953:        search_hits: list[SearchHit[DocumentChunkWithoutVectors]] = self._client.search(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:959:            convert_retrieved_opensearch_chunk_to_inference_chunk_uncleaned(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1009:      - All retrieval goes to primary.
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1094:    def id_based_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1098:        batch_retrieval: bool = False,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1100:        return self._primary.id_based_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1101:            chunk_requests, filters, batch_retrieval
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1104:    def hybrid_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1107:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1111:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1113:        return self._primary.hybrid_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1115:            query_embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1119:            num_to_retrieve,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1122:    def keyword_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1126:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1129:        return self._primary.keyword_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1130:            query, filters, num_to_retrieve, include_hidden=include_hidden
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1133:    def semantic_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1135:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1137:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1139:        return self._primary.semantic_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1140:            query_embedding, filters, num_to_retrieve
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1143:    def random_retrieval(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1146:        num_to_retrieve: int = 10,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1149:        return self._primary.random_retrieval(filters, num_to_retrieve, dirty)
HEAD:backend/onyx/document_index/opensearch/schema.py:486:                # set, the user should be able to retrieve this document. This
HEAD:backend/onyx/document_index/opensearch/search.py:16:    DEFAULT_NUM_HYBRID_SUBQUERY_CANDIDATES,
HEAD:backend/onyx/document_index/opensearch/search.py:18:    HYBRID_SEARCH_NORMALIZATION_PIPELINE,
HEAD:backend/onyx/document_index/opensearch/search.py:19:    HYBRID_SEARCH_SUBQUERY_CONFIGURATION,
HEAD:backend/onyx/document_index/opensearch/search.py:20:    HybridSearchNormalizationPipeline,
HEAD:backend/onyx/document_index/opensearch/search.py:21:    HybridSearchSubqueryConfiguration,
HEAD:backend/onyx/document_index/opensearch/search.py:62:def _get_hybrid_search_normalization_weights() -> list[float]:
HEAD:backend/onyx/document_index/opensearch/search.py:64:        HYBRID_SEARCH_SUBQUERY_CONFIGURATION
HEAD:backend/onyx/document_index/opensearch/search.py:65:        is HybridSearchSubqueryConfiguration.TITLE_VECTOR_CONTENT_VECTOR_TITLE_CONTENT_COMBINED_KEYWORD
HEAD:backend/onyx/document_index/opensearch/search.py:77:        # of the sub-queries in the hybrid search.
HEAD:backend/onyx/document_index/opensearch/search.py:78:        hybrid_search_normalization_weights = [
HEAD:backend/onyx/document_index/opensearch/search.py:84:        HYBRID_SEARCH_SUBQUERY_CONFIGURATION
HEAD:backend/onyx/document_index/opensearch/search.py:85:        is HybridSearchSubqueryConfiguration.CONTENT_VECTOR_TITLE_CONTENT_COMBINED_KEYWORD
HEAD:backend/onyx/document_index/opensearch/search.py:93:        # of the sub-queries in the hybrid search.
HEAD:backend/onyx/document_index/opensearch/search.py:94:        hybrid_search_normalization_weights = [
HEAD:backend/onyx/document_index/opensearch/search.py:100:            f"Bug: Unhandled hybrid search subquery configuration: {HYBRID_SEARCH_SUBQUERY_CONFIGURATION}."
HEAD:backend/onyx/document_index/opensearch/search.py:103:    assert sum(hybrid_search_normalization_weights) == 1.0, (
HEAD:backend/onyx/document_index/opensearch/search.py:104:        "Bug: Hybrid search normalization weights do not sum to 1.0."
HEAD:backend/onyx/document_index/opensearch/search.py:107:    return hybrid_search_normalization_weights
HEAD:backend/onyx/document_index/opensearch/search.py:122:                            "weights": _get_hybrid_search_normalization_weights()
HEAD:backend/onyx/document_index/opensearch/search.py:144:                            "weights": _get_hybrid_search_normalization_weights()
HEAD:backend/onyx/document_index/opensearch/search.py:156:        HYBRID_SEARCH_NORMALIZATION_PIPELINE
HEAD:backend/onyx/document_index/opensearch/search.py:157:        is HybridSearchNormalizationPipeline.MIN_MAX
HEAD:backend/onyx/document_index/opensearch/search.py:161:        HYBRID_SEARCH_NORMALIZATION_PIPELINE is HybridSearchNormalizationPipeline.ZSCORE
HEAD:backend/onyx/document_index/opensearch/search.py:166:            f"Bug: Unhandled hybrid search normalization pipeline: {HYBRID_SEARCH_NORMALIZATION_PIPELINE}."
HEAD:backend/onyx/document_index/opensearch/search.py:200:            index_filters: Filters for the document retrieval query.
HEAD:backend/onyx/document_index/opensearch/search.py:204:                maximum size category of document chunks to retrieve.
HEAD:backend/onyx/document_index/opensearch/search.py:205:            min_chunk_index: The minimum chunk index to retrieve, inclusive. If
HEAD:backend/onyx/document_index/opensearch/search.py:207:            max_chunk_index: The maximum chunk index to retrieve, inclusive. If
HEAD:backend/onyx/document_index/opensearch/search.py:243:            # on retrieval cost as we don't need them upstream.
HEAD:backend/onyx/document_index/opensearch/search.py:251:            # retrieve IDs.
HEAD:backend/onyx/document_index/opensearch/search.py:339:    def get_hybrid_search_query(
HEAD:backend/onyx/document_index/opensearch/search.py:347:        """Returns a final hybrid search query.
HEAD:backend/onyx/document_index/opensearch/search.py:351:        hybrid search are not meaningful without that step.
HEAD:backend/onyx/document_index/opensearch/search.py:361:            index_filters: Filters for the hybrid search query.
HEAD:backend/onyx/document_index/opensearch/search.py:365:            A dictionary representing the final hybrid search query.
HEAD:backend/onyx/document_index/opensearch/search.py:367:        # WARNING: Profiling does not work with hybrid search; do not add it at
HEAD:backend/onyx/document_index/opensearch/search.py:378:        max_results_per_subquery = DEFAULT_NUM_HYBRID_SUBQUERY_CANDIDATES
HEAD:backend/onyx/document_index/opensearch/search.py:380:        hybrid_search_subqueries = DocumentQuery._get_hybrid_search_subqueries(
HEAD:backend/onyx/document_index/opensearch/search.py:383:        hybrid_search_filters = DocumentQuery._get_search_filters(
HEAD:backend/onyx/document_index/opensearch/search.py:404:        # See https://docs.opensearch.org/latest/query-dsl/compound/hybrid/
HEAD:backend/onyx/document_index/opensearch/search.py:405:        hybrid_search_query: dict[str, Any] = {
HEAD:backend/onyx/document_index/opensearch/search.py:406:            "hybrid": {
HEAD:backend/onyx/document_index/opensearch/search.py:407:                "queries": hybrid_search_subqueries,
HEAD:backend/onyx/document_index/opensearch/search.py:410:                # candidate pool for hybrid fusion.
HEAD:backend/onyx/document_index/opensearch/search.py:412:                # https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/pagination/
HEAD:backend/onyx/document_index/opensearch/search.py:413:                # https://opensearch.org/blog/navigating-pagination-in-hybrid-queries-with-the-pagination_depth-parameter/
HEAD:backend/onyx/document_index/opensearch/search.py:419:                # https://docs.opensearch.org/latest/query-dsl/compound/hybrid/
HEAD:backend/onyx/document_index/opensearch/search.py:420:                # https://opensearch.org/blog/introducing-common-filter-support-for-hybrid-search-queries
HEAD:backend/onyx/document_index/opensearch/search.py:422:                "filter": {"bool": {"filter": hybrid_search_filters}},
HEAD:backend/onyx/document_index/opensearch/search.py:426:        final_hybrid_search_body: dict[str, Any] = {
HEAD:backend/onyx/document_index/opensearch/search.py:427:            "query": hybrid_search_query,
HEAD:backend/onyx/document_index/opensearch/search.py:431:            # retrieval cost as we don't need them upstream.
HEAD:backend/onyx/document_index/opensearch/search.py:438:            final_hybrid_search_body["highlight"] = (
HEAD:backend/onyx/document_index/opensearch/search.py:445:            final_hybrid_search_body["explain"] = True
HEAD:backend/onyx/document_index/opensearch/search.py:447:        return final_hybrid_search_body
HEAD:backend/onyx/document_index/opensearch/search.py:450:    def get_keyword_search_query(
HEAD:backend/onyx/document_index/opensearch/search.py:480:        keyword_search_filters = DocumentQuery._get_search_filters(
HEAD:backend/onyx/document_index/opensearch/search.py:501:        keyword_search_query = (
HEAD:backend/onyx/document_index/opensearch/search.py:502:            DocumentQuery._get_title_content_combined_keyword_search_query(
HEAD:backend/onyx/document_index/opensearch/search.py:503:                query_text, search_filters=keyword_search_filters
HEAD:backend/onyx/document_index/opensearch/search.py:507:        final_keyword_search_query: dict[str, Any] = {
HEAD:backend/onyx/document_index/opensearch/search.py:508:            "query": keyword_search_query,
HEAD:backend/onyx/document_index/opensearch/search.py:512:            # retrieval cost as we don't need them upstream.
HEAD:backend/onyx/document_index/opensearch/search.py:519:            final_keyword_search_query["highlight"] = (
HEAD:backend/onyx/document_index/opensearch/search.py:524:            final_keyword_search_query["profile"] = True
HEAD:backend/onyx/document_index/opensearch/search.py:529:            final_keyword_search_query["explain"] = True
HEAD:backend/onyx/document_index/opensearch/search.py:531:        return final_keyword_search_query
HEAD:backend/onyx/document_index/opensearch/search.py:534:    def get_semantic_search_query(
HEAD:backend/onyx/document_index/opensearch/search.py:535:        query_embedding: list[float],
HEAD:backend/onyx/document_index/opensearch/search.py:549:            query_embedding: The vector embedding of the text to query for.
HEAD:backend/onyx/document_index/opensearch/search.py:564:        semantic_search_filters = DocumentQuery._get_search_filters(
HEAD:backend/onyx/document_index/opensearch/search.py:585:        semantic_search_query = (
HEAD:backend/onyx/document_index/opensearch/search.py:587:                query_embedding,
HEAD:backend/onyx/document_index/opensearch/search.py:589:                search_filters=semantic_search_filters,
HEAD:backend/onyx/document_index/opensearch/search.py:593:        final_semantic_search_query: dict[str, Any] = {
HEAD:backend/onyx/document_index/opensearch/search.py:594:            "query": semantic_search_query,
HEAD:backend/onyx/document_index/opensearch/search.py:598:            # retrieval cost as we don't need them upstream.
HEAD:backend/onyx/document_index/opensearch/search.py:605:            final_semantic_search_query["profile"] = True
HEAD:backend/onyx/document_index/opensearch/search.py:610:            final_semantic_search_query["explain"] = True
HEAD:backend/onyx/document_index/opensearch/search.py:612:        return final_semantic_search_query
HEAD:backend/onyx/document_index/opensearch/search.py:618:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/opensearch/search.py:625:            num_to_retrieve: Number of document chunks to retrieve.
HEAD:backend/onyx/document_index/opensearch/search.py:664:            "size": num_to_retrieve,
HEAD:backend/onyx/document_index/opensearch/search.py:667:            # retrieval cost as we don't need them upstream.
HEAD:backend/onyx/document_index/opensearch/search.py:678:    def _get_hybrid_search_subqueries(
HEAD:backend/onyx/document_index/opensearch/search.py:683:        # is hybrid. For a detailed breakdown, see where the default value is
HEAD:backend/onyx/document_index/opensearch/search.py:685:        vector_candidates: int = DEFAULT_NUM_HYBRID_SUBQUERY_CANDIDATES,
HEAD:backend/onyx/document_index/opensearch/search.py:687:        """Returns subqueries for hybrid search.
HEAD:backend/onyx/document_index/opensearch/search.py:689:        Each of these subqueries are the "hybrid" component of this search. We
HEAD:backend/onyx/document_index/opensearch/search.py:693:        the OpenSearch client. See get_hybrid_search_query.
HEAD:backend/onyx/document_index/opensearch/search.py:700:        HYBRID_SEARCH_SUBQUERY_CONFIGURATION setting.
HEAD:backend/onyx/document_index/opensearch/search.py:703:        in a single hybrid query. Source:
HEAD:backend/onyx/document_index/opensearch/search.py:704:        https://docs.opensearch.org/latest/query-dsl/compound/hybrid/
HEAD:backend/onyx/document_index/opensearch/search.py:709:        keyword, it gets a score of 0 for the keyword component of the hybrid
HEAD:backend/onyx/document_index/opensearch/search.py:719:        - minimum_should_match: Since it's hybrid search and users often provide
HEAD:backend/onyx/document_index/opensearch/search.py:734:        # Build sub-queries for hybrid search. Order must match normalization
HEAD:backend/onyx/document_index/opensearch/search.py:737:            HYBRID_SEARCH_SUBQUERY_CONFIGURATION
HEAD:backend/onyx/document_index/opensearch/search.py:738:            is HybridSearchSubqueryConfiguration.TITLE_VECTOR_CONTENT_VECTOR_TITLE_CONTENT_COMBINED_KEYWORD
HEAD:backend/onyx/document_index/opensearch/search.py:747:                DocumentQuery._get_title_content_combined_keyword_search_query(
HEAD:backend/onyx/document_index/opensearch/search.py:752:            HYBRID_SEARCH_SUBQUERY_CONFIGURATION
HEAD:backend/onyx/document_index/opensearch/search.py:753:            is HybridSearchSubqueryConfiguration.CONTENT_VECTOR_TITLE_CONTENT_COMBINED_KEYWORD
HEAD:backend/onyx/document_index/opensearch/search.py:759:                DocumentQuery._get_title_content_combined_keyword_search_query(
HEAD:backend/onyx/document_index/opensearch/search.py:765:                f"Bug: Unhandled hybrid search subquery configuration: {HYBRID_SEARCH_SUBQUERY_CONFIGURATION}"
HEAD:backend/onyx/document_index/opensearch/search.py:771:        vector_candidates: int = DEFAULT_NUM_HYBRID_SUBQUERY_CANDIDATES,
HEAD:backend/onyx/document_index/opensearch/search.py:785:        vector_candidates: int = DEFAULT_NUM_HYBRID_SUBQUERY_CANDIDATES,
HEAD:backend/onyx/document_index/opensearch/search.py:805:    def _get_title_content_combined_keyword_search_query(
HEAD:backend/onyx/document_index/opensearch/search.py:896:        retrieved. This function returns a list of such subfilters.
HEAD:backend/onyx/document_index/opensearch/search.py:910:                retrieve. If None, there is no restriction on the documents that
HEAD:backend/onyx/document_index/opensearch/search.py:911:                can be retrieved. If not None, only public documents can be
HEAD:backend/onyx/document_index/opensearch/search.py:912:                retrieved, or non-public documents where at least one acl
HEAD:backend/onyx/document_index/opensearch/search.py:915:                types will be retrieved.
HEAD:backend/onyx/document_index/opensearch/search.py:917:                list corresponding to a tag will be retrieved.
HEAD:backend/onyx/document_index/opensearch/search.py:919:                document set ID from this list will be retrieved.
HEAD:backend/onyx/document_index/opensearch/search.py:921:                in user projects will be retrieved. Additive — only applied
HEAD:backend/onyx/document_index/opensearch/search.py:924:                contains this persona ID will be retrieved. Primary — creates
HEAD:backend/onyx/document_index/opensearch/search.py:929:            min_chunk_index: The minimum chunk index to retrieve, inclusive. If
HEAD:backend/onyx/document_index/opensearch/search.py:931:            max_chunk_index: The maximum chunk index to retrieve, inclusive. If
HEAD:backend/onyx/document_index/opensearch/search.py:933:            max_chunk_size: The type of chunk to retrieve, specified by the
HEAD:backend/onyx/document_index/opensearch/search.py:937:            document_id: The document ID to retrieve. If None, no filter will be
HEAD:backend/onyx/document_index/opensearch/search.py:941:                matching EITHER criteria will be retrieved (OR logic).
HEAD:backend/onyx/document_index/opensearch/search.py:1272:            # retrieve public documents, and non-public documents where at least
HEAD:backend/onyx/document_index/opensearch/search.py:1275:            # the documents that can be retrieved.
HEAD:backend/onyx/document_index/opensearch/search.py:1286:            # retrieve documents whose source type is present in this input
HEAD:backend/onyx/document_index/opensearch/search.py:1291:            # If at least one tag is provided, the caller will only retrieve
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:229:    rank-profile hybrid_search_semantic_base_{{ dim }} inherits default, default_rank {
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:231:            query(query_embedding) tensor<float>(x[{{ dim }}])
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:281:            # Target hits for hybrid retrieval should be at least this value.
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:298:    rank-profile hybrid_search_keyword_base_{{ dim }} inherits default, default_rank {
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:300:            query(query_embedding) tensor<float>(x[{{ dim }}])
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:350:            # Target hits for hybrid retrieval should be at least this value.
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:28:    build_vespa_id_based_retrieval_yql,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:179:    # build the list of fields to retrieve
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:227:    # asks to retrieve tensor data in "short-value" format.
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:470:def parallel_visit_api_retrieval(
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:488:    # Any failures to retrieve would give a None, drop the Nones and empty lists
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:583:        num_retrieved_inference_chunks = len(inference_chunks)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:584:        num_retrieved_document_ids = len(
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:588:            "Retrieved %s inference chunks for %s documents",
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:589:            num_retrieved_inference_chunks,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:590:            num_retrieved_document_ids,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:593:        # Debug logging only, should not fail the retrieval
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:594:        logger.error("Error logging retrieval statistics: %s", e)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:600:def _get_chunks_via_batch_search(
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:614:        + build_vespa_id_based_retrieval_yql(chunk_requests[0])
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:619:        yql += " or " + build_vespa_id_based_retrieval_yql(request)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:634:def batch_search_api_retrieval(
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:640:    retrieved_chunks: list[InferenceChunkUncleaned] = []
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:646:        # Uncapped requests are retrieved using the Visit API
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:656:            retrieved_chunks.extend(
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:657:                _get_chunks_via_batch_search(
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:670:        retrieved_chunks.extend(
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:671:            _get_chunks_via_batch_search(
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:681:        retrieved_chunks.extend(
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:682:            parallel_visit_api_retrieval(
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:687:    return retrieved_chunks
HEAD:backend/onyx/document_index/vespa/internal_types.py:5:chunk-id deletion / range-retrieval plumbing, which has not been ported to the
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:278:def build_vespa_id_based_retrieval_yql(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:281:    id_based_retrieval_yql_section = (
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:286:        id_based_retrieval_yql_section += (
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:289:        id_based_retrieval_yql_section += (
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:293:    id_based_retrieval_yql_section += ")"
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:294:    return id_based_retrieval_yql_section
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:27:    HYBRID_ALPHA,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:48:from onyx.document_index.vespa.chunk_retrieval import (
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:49:    batch_search_api_retrieval,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:52:    parallel_visit_api_retrieval,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:91:from onyx.tools.tool_implementations.search.constants import KEYWORD_QUERY_HYBRID_ALPHA
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:600:    This class provides document indexing, retrieval, and management operations
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:864:    def id_based_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:868:        batch_retrieval: bool = False,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:881:        if batch_retrieval:
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:883:                batch_search_api_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:893:            parallel_visit_api_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:903:    def hybrid_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:906:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:910:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:915:        target_hits = min(max(4 * num_to_retrieve, 100), RERANK_COUNT)
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:920:            + f"(({{targetHits: {target_hits}}}nearestNeighbor(embeddings, query_embedding)) "
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:921:            + f"or ({{targetHits: {target_hits}}}nearestNeighbor(title_embedding, query_embedding)) "
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:929:            f"hybrid_search_{query_type.value}_base_{len(query_embedding)}"
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:936:        # In this interface we do not pass in hybrid alpha. Tracing the codepath
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:938:        # corresponds to an alpha of 0.2 (from KEYWORD_QUERY_HYBRID_ALPHA), and
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:939:        # SEMANTIC to 0.5 (from HYBRID_ALPHA). HYBRID_ALPHA_KEYWORD was only
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:941:        hybrid_alpha = (
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:942:            KEYWORD_QUERY_HYBRID_ALPHA
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:944:            else HYBRID_ALPHA
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:950:            "input.query(query_embedding)": str(query_embedding),
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:952:            "input.query(alpha)": hybrid_alpha,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:954:            "hits": num_to_retrieve,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:961:    def keyword_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:965:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:968:        # Ported from the legacy Vespa admin_retrieval: pure-keyword search over
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:986:            "hits": num_to_retrieve,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:993:    def semantic_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:995:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:997:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1001:    def random_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1004:        num_to_retrieve: int = 100,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1015:            "hits": num_to_retrieve,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1246:        # pair rather than threading it through every retrieval call.
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1305:    def id_based_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1309:        batch_retrieval: bool = False,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1311:        return self._primary.id_based_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1312:            chunk_requests, filters, batch_retrieval
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1315:    def hybrid_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1318:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1322:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1324:        return self._primary.hybrid_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1326:            query_embedding,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1330:            num_to_retrieve,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1333:    def keyword_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1337:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1340:        return self._primary.keyword_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1341:            query, filters, num_to_retrieve, include_hidden=include_hidden
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1344:    def semantic_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1346:        query_embedding: Embedding,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1348:        num_to_retrieve: int,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1350:        return self._primary.semantic_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1351:            query_embedding, filters, num_to_retrieve
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1354:    def random_retrieval(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1357:        num_to_retrieve: int = 10,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1360:        return self._primary.random_retrieval(filters, num_to_retrieve, dirty)
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:374:            # If we failed to get a chat session, try to retrieve the session with
HEAD:backend/onyx/server/query_and_chat/query_backend.py:34:def admin_search(
HEAD:backend/onyx/server/query_and_chat/query_backend.py:59:        matching_chunks = document_index.random_retrieval(filters=final_filters)
HEAD:backend/onyx/server/query_and_chat/query_backend.py:61:        matching_chunks = document_index.keyword_retrieval(
HEAD:backend/onyx/server/query_and_chat/query_backend.py:64:            num_to_retrieve=NUM_RETURNED_HITS,
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:327:    # Short previews of the retrieved text for the collapsed/expanded UI
```
## Retrieval-Time ACL and Tenant Filtering
Evidence lines: 141
```text
HEAD:backend/ee/onyx/access/access.py:15:from onyx.access.access import _get_acl_for_user as get_acl_for_user_without_groups
HEAD:backend/ee/onyx/access/access.py:184:def _get_acl_for_user(user: User, db_session: Session) -> set[str]:
HEAD:backend/ee/onyx/access/access.py:208:    user_acl = set(prefixed_user_groups + prefixed_external_groups)
HEAD:backend/ee/onyx/access/access.py:209:    user_acl.update(get_acl_for_user_without_groups(user, db_session))
HEAD:backend/ee/onyx/access/access.py:211:    return user_acl
HEAD:backend/onyx/access/access.py:11:from onyx.configs.constants import PUBLIC_DOC_PAT, DocumentSource, FileOrigin
HEAD:backend/onyx/access/access.py:114:def _get_acl_for_user(
HEAD:backend/onyx/access/access.py:130:        return {PUBLIC_DOC_PAT}
HEAD:backend/onyx/access/access.py:134:        PUBLIC_DOC_PAT,
HEAD:backend/onyx/access/access.py:138:def get_acl_for_user(user: User, db_session: Session | None = None) -> set[str]:
HEAD:backend/onyx/access/access.py:140:        "onyx.access.access", "_get_acl_for_user"
HEAD:backend/onyx/access/access.py:342:    user_acl = get_acl_for_user(user, db_session)
HEAD:backend/onyx/access/access.py:345:        not user_acl.isdisjoint(access.to_acl()) for access in doc_access.values()
HEAD:backend/onyx/access/models.py:8:from onyx.configs.constants import PUBLIC_DOC_PAT
HEAD:backend/onyx/access/models.py:197:            acl_set.add(PUBLIC_DOC_PAT)
HEAD:backend/onyx/db/document_access.py:19:def apply_document_access_filter(
HEAD:backend/onyx/db/document_access.py:73:    stmt = apply_document_access_filter(
HEAD:backend/onyx/document_index/FILTER_SEMANTICS.md:3:How `IndexFilters` fields combine into the final query filter. Describes the active
HEAD:backend/onyx/document_index/FILTER_SEMANTICS.md:13:| **ACL** | `access_control_list` | OR within, AND with rest |
HEAD:backend/onyx/document_index/FILTER_SEMANTICS.md:159:| `access_control_list` | `access_control_list` | `weightedset<string>` | ACL entries for the requesting user |
HEAD:backend/onyx/document_index/disabled.py:11:from onyx.context.search.models import IndexFilters, InferenceChunk
HEAD:backend/onyx/document_index/disabled.py:65:        filters: IndexFilters,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:76:        filters: IndexFilters,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:84:        filters: IndexFilters,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:93:        filters: IndexFilters,  # noqa: ARG002
HEAD:backend/onyx/document_index/disabled.py:100:        filters: IndexFilters,  # noqa: ARG002
HEAD:backend/onyx/document_index/interfaces_new.py:9:from onyx.configs.constants import PUBLIC_DOC_PAT
HEAD:backend/onyx/document_index/interfaces_new.py:11:from onyx.context.search.models import IndexFilters, InferenceChunk
HEAD:backend/onyx/document_index/interfaces_new.py:187:    access_control_list: frozenset[str] = frozenset({PUBLIC_DOC_PAT})
HEAD:backend/onyx/document_index/interfaces_new.py:339:        filters: IndexFilters,
HEAD:backend/onyx/document_index/interfaces_new.py:377:        filters: IndexFilters,
HEAD:backend/onyx/document_index/interfaces_new.py:404:        filters: IndexFilters,
HEAD:backend/onyx/document_index/interfaces_new.py:429:        filters: IndexFilters,
HEAD:backend/onyx/document_index/interfaces_new.py:456:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:11:from onyx.document_index.opensearch.schema import TENANT_ID_FIELD_NAME
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:49:            "query": {"term": {TENANT_ID_FIELD_NAME: {"value": tenant_state.tenant_id}}}
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:12:from onyx.configs.constants import PUBLIC_DOC_PAT, OnyxRedisLocks
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:19:    IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:49:    ACCESS_CONTROL_LIST_FIELD_NAME,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:96:def generate_opensearch_filtered_access_control_list(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:99:    """Generates an access control list with PUBLIC_DOC_PAT removed.
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:103:    access_control_list = access.to_acl()
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:104:    access_control_list.discard(PUBLIC_DOC_PAT)
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:105:    return list(access_control_list)
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:236:        access_control_list=generate_opensearch_filtered_access_control_list(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:636:                properties_to_update[ACCESS_CONTROL_LIST_FIELD_NAME] = (
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:637:                    generate_opensearch_filtered_access_control_list(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:742:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:799:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:851:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:896:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:939:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1097:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1110:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1125:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1136:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1145:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/schema.py:48:ACCESS_CONTROL_LIST_FIELD_NAME = "access_control_list"
HEAD:backend/onyx/document_index/opensearch/schema.py:61:TENANT_ID_FIELD_NAME = "tenant_id"
HEAD:backend/onyx/document_index/opensearch/schema.py:174:    access_control_list: list[str]
HEAD:backend/onyx/document_index/opensearch/schema.py:480:                # is its own field. If true, ACCESS_CONTROL_LIST_FIELD_NAME
HEAD:backend/onyx/document_index/opensearch/schema.py:490:                ACCESS_CONTROL_LIST_FIELD_NAME: {"type": "keyword"},
HEAD:backend/onyx/document_index/opensearch/schema.py:493:                # PUBLIC_FIELD_NAME and ACCESS_CONTROL_LIST_FIELD_NAME; up to
HEAD:backend/onyx/document_index/opensearch/schema.py:582:            schema["properties"][TENANT_ID_FIELD_NAME] = {"type": "keyword"}
HEAD:backend/onyx/document_index/opensearch/search.py:12:from onyx.context.search.models import IndexFilters, Tag, TimeRange
HEAD:backend/onyx/document_index/opensearch/search.py:24:    ACCESS_CONTROL_LIST_FIELD_NAME,
HEAD:backend/onyx/document_index/opensearch/search.py:39:    TENANT_ID_FIELD_NAME,
HEAD:backend/onyx/document_index/opensearch/search.py:181:        index_filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/search.py:221:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:288:            access_control_list=None,
HEAD:backend/onyx/document_index/opensearch/search.py:327:                {"term": {TENANT_ID_FIELD_NAME: {"value": tenant_state.tenant_id}}}
HEAD:backend/onyx/document_index/opensearch/search.py:344:        index_filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/search.py:386:            # TODO(andrei): We've done no filtering for PUBLIC_DOC_PAT up to
HEAD:backend/onyx/document_index/opensearch/search.py:389:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:454:        index_filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/search.py:483:            # TODO(andrei): We've done no filtering for PUBLIC_DOC_PAT up to
HEAD:backend/onyx/document_index/opensearch/search.py:486:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:538:        index_filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/search.py:567:            # TODO(andrei): We've done no filtering for PUBLIC_DOC_PAT up to
HEAD:backend/onyx/document_index/opensearch/search.py:570:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:617:        index_filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/search.py:633:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:874:        access_control_list: list[str] | None,
HEAD:backend/onyx/document_index/opensearch/search.py:909:            access_control_list: Access control list for the documents to
HEAD:backend/onyx/document_index/opensearch/search.py:960:            access_control_list: list[str],
HEAD:backend/onyx/document_index/opensearch/search.py:968:                access_control_list: The access control list to restrict
HEAD:backend/onyx/document_index/opensearch/search.py:985:            if access_control_list:
HEAD:backend/onyx/document_index/opensearch/search.py:986:                if len(access_control_list) > MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY:
HEAD:backend/onyx/document_index/opensearch/search.py:988:                        f"Too many access control list entries: {len(access_control_list)}. Max allowed: {MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY}."
HEAD:backend/onyx/document_index/opensearch/search.py:995:                    "terms": {ACCESS_CONTROL_LIST_FIELD_NAME: list(access_control_list)}
HEAD:backend/onyx/document_index/opensearch/search.py:1270:        if access_control_list is not None:
HEAD:backend/onyx/document_index/opensearch/search.py:1276:            filter_clauses.append(_get_acl_visibility_filter(access_control_list))
HEAD:backend/onyx/document_index/opensearch/search.py:1366:                {"term": {TENANT_ID_FIELD_NAME: {"value": tenant_state.tenant_id}}}
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:159:        field access_control_list type weightedset<string> {
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:22:from onyx.context.search.models import IndexFilters, InferenceChunkUncleaned
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:31:    ACCESS_CONTROL_LIST,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:170:    filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:183:    acl_fieldset_entry = f"{ACCESS_CONTROL_LIST}"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:186:        and filters.access_control_list
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:213:            selection += f" and {index_name}.tenant_id=='{filters.tenant_id}'"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:259:                if filters.access_control_list:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:260:                    document_acl = document["fields"].get(ACCESS_CONTROL_LIST)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:262:                        user_acl_entry in document_acl
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:263:                        for user_acl_entry in filters.access_control_list
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:271:                    if document_tenant_id != filters.tenant_id:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:457:#     filters: IndexFilters | None = None,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:463:#         filters=filters or IndexFilters(access_control_list=None),
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:473:    filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:603:    filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:637:    filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:28:    ACCESS_CONTROL_LIST,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:218:        ACCESS_CONTROL_LIST: {acl_entry: 1 for acl_entry in chunk.access.to_acl()},
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:4:from onyx.context.search.models import IndexFilters
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:7:    ACCESS_CONTROL_LIST,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:26:def build_tenant_id_filter(tenant_id: str) -> str:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:31:    filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:51:        access_control_list where a single user may have tens of thousands
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:187:    # TODO: add error condition if MULTI_TENANT and no tenant_id filter is set
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:189:        filter_parts.append(build_tenant_id_filter(filters.tenant_id))
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:192:    # access_control_list weightedset<string> field.  OR-chaining thousands
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:195:    if filters.access_control_list is not None:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:199:                ACCESS_CONTROL_LIST, filters.access_control_list
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:33:from onyx.context.search.models import IndexFilters, InferenceChunk
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:511:        access_control_list: _AccessControl | None = None
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:558:        access_control_list=access_update,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:867:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:909:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:964:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:996:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1003:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1040:            filters=IndexFilters(access_control_list=None, tenant_id=self._tenant_id),
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1308:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1321:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1336:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1347:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1356:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa_constants.py:58:ACCESS_CONTROL_LIST = "access_control_list"
HEAD:backend/onyx/server/query_and_chat/query_backend.py:7:from onyx.context.search.models import IndexFilters, SearchDoc
HEAD:backend/onyx/server/query_and_chat/query_backend.py:43:    user_acl_filters = build_access_filters_for_user(user, db_session)
HEAD:backend/onyx/server/query_and_chat/query_backend.py:45:    final_filters = IndexFilters(
HEAD:backend/onyx/server/query_and_chat/query_backend.py:51:        access_control_list=user_acl_filters,
```
Static source contains retrieval-time access and tenant filtering mechanisms.
These mechanisms are later high-priority targets for bounded cross-user and
cross-tenant security verification.
## OpenSearch Filter Evidence
Evidence lines: 476
```text
HEAD:backend/onyx/document_index/opensearch/README.md:6:an intermediate phase (seemingly built specifically to handle hybrid search queries) which can run in between as a processor.
HEAD:backend/onyx/document_index/opensearch/README.md:37:query which filters on recently updated documents) is added, it would not be able to introduce any new documents
HEAD:backend/onyx/document_index/opensearch/README.md:39:and vector would make the docs which only came because of time filter very low scoring. This can however make some of the lower
HEAD:backend/onyx/document_index/opensearch/README.md:42:- There is no way to sort by this field, only a filter, so there's no way to guarantee the best docs even irrespective of the
HEAD:backend/onyx/document_index/opensearch/README.md:53:filtering. The impact of time decay and boost should not be so big that we would need orders of magnitude more results back
HEAD:backend/onyx/document_index/opensearch/client.py:96:    # terms wrapped in tags (e.g. "something <hi>keyword</hi> other thing").
HEAD:backend/onyx/document_index/opensearch/client.py:163:# OpenSearch applies when disk usage crosses the flood-stage watermark.
HEAD:backend/onyx/document_index/opensearch/client.py:170:def is_cluster_block_error(e: Exception) -> bool:
HEAD:backend/onyx/document_index/opensearch/client.py:178:    read_only_allow_delete applied at the disk flood-stage watermark). The
HEAD:backend/onyx/document_index/opensearch/client.py:268:        use_ssl: bool = OPENSEARCH_USE_SSL,
HEAD:backend/onyx/document_index/opensearch/client.py:269:        verify_certs: bool = OPENSEARCH_VERIFY_CERTS,
HEAD:backend/onyx/document_index/opensearch/client.py:273:        ssl_show_warn: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:372:    def put_cluster_settings(self, settings: dict[str, Any]) -> bool:
HEAD:backend/onyx/document_index/opensearch/client.py:470:        primary: bool | None = None,
HEAD:backend/onyx/document_index/opensearch/client.py:518:    def ping(self) -> bool:
HEAD:backend/onyx/document_index/opensearch/client.py:579:        use_ssl: bool = OPENSEARCH_USE_SSL,
HEAD:backend/onyx/document_index/opensearch/client.py:580:        verify_certs: bool = OPENSEARCH_VERIFY_CERTS,
HEAD:backend/onyx/document_index/opensearch/client.py:584:        ssl_show_warn: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:586:        emit_metrics: bool = True,
HEAD:backend/onyx/document_index/opensearch/client.py:644:    def delete_index(self) -> bool:
HEAD:backend/onyx/document_index/opensearch/client.py:668:    def index_exists(self) -> bool:
HEAD:backend/onyx/document_index/opensearch/client.py:710:    def validate_index(self, expected_mappings: dict[str, Any]) -> bool:
HEAD:backend/onyx/document_index/opensearch/client.py:823:        include_defaults: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:824:        flat_settings: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:825:        pretty: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:826:        human: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:908:        update_if_exists: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:929:            tenant_state.tenant_id,
HEAD:backend/onyx/document_index/opensearch/client.py:988:        update_if_exists: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:989:        use_create_only: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:1029:            tenant_state.tenant_id,
HEAD:backend/onyx/document_index/opensearch/client.py:1121:    def delete_document(self, document_chunk_id: str) -> bool:
HEAD:backend/onyx/document_index/opensearch/client.py:1177:        refresh: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:1260:        ignore_missing: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:1339:        ignore_missing: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:1340:        surface_document_missing: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:1543:        found_result: bool = result.get("found", False)
HEAD:backend/onyx/document_index/opensearch/client.py:1808:        Filters to regular chunks (max_chunk_size == DEFAULT_MAX_CHUNK_SIZE),
HEAD:backend/onyx/document_index/opensearch/client.py:1942:                "bool": {
HEAD:backend/onyx/document_index/opensearch/client.py:1943:                    "filter": [
HEAD:backend/onyx/document_index/opensearch/client.py:1944:                        {"terms": {DOCUMENT_ID_FIELD_NAME: doc_ids}},
HEAD:backend/onyx/document_index/opensearch/client.py:1947:                        {"term": {MAX_CHUNK_SIZE_FIELD_NAME: DEFAULT_MAX_CHUNK_SIZE}},
HEAD:backend/onyx/document_index/opensearch/client.py:1961:    def _is_pit_expired(error: NotFoundError) -> bool:
HEAD:backend/onyx/document_index/opensearch/client.py:1984:    ) -> tuple[list[Any], int | None, bool | None, dict[str, Any], dict[str, Any]]:
HEAD:backend/onyx/document_index/opensearch/client.py:2001:        timed_out: bool | None = result.get("timed_out")
HEAD:backend/onyx/document_index/opensearch/client.py:2017:        timed_out: bool | None,
HEAD:backend/onyx/document_index/opensearch/client.py:2022:        raise_on_timeout: bool = False,
HEAD:backend/onyx/document_index/opensearch/client.py:2080:) -> bool:
HEAD:backend/onyx/document_index/opensearch/constants.py:16:# cutoff filtering during retrieval.
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:11:from onyx.document_index.opensearch.schema import TENANT_ID_FIELD_NAME
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:49:            "query": {"term": {TENANT_ID_FIELD_NAME: {"value": tenant_state.tenant_id}}}
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:60:            tenant_state.tenant_id,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:19:    IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:49:    ACCESS_CONTROL_LIST_FIELD_NAME,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:82:# Batch size for the orphan sweep's delete-by-query terms filter — well under the
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:83:# OpenSearch terms cap (65536) so a large mid-port purge can't build an oversized query.
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:96:def generate_opensearch_filtered_access_control_list(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:103:    access_control_list = access.to_acl()
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:104:    access_control_list.discard(PUBLIC_DOC_PAT)
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:105:    return list(access_control_list)
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:149:            with match terms wrapped in tags (e.g. "something <hi>keyword</hi>
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:202:    filtered_blurb = remove_invalid_unicode_chars(chunk.blurb)
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:204:    filtered_title = remove_invalid_unicode_chars(_title) if _title else None
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:205:    filtered_content = remove_invalid_unicode_chars(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:208:    filtered_semantic_identifier = remove_invalid_unicode_chars(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:211:    filtered_metadata_suffix = remove_invalid_unicode_chars(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:215:    filtered_metadata_list = (
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:226:        title=filtered_title,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:228:        content=filtered_content,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:231:        metadata_list=filtered_metadata_list,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:232:        metadata_suffix=filtered_metadata_suffix,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:236:        access_control_list=generate_opensearch_filtered_access_control_list(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:240:        semantic_identifier=filtered_semantic_identifier,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:246:        blurb=filtered_blurb,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:268:        tenant_id=TenantState(tenant_id=chunk.tenant_id, multitenant=MULTI_TENANT),
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:269:        # Store ancestor hierarchy node IDs for hierarchy-based filtering.
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:325:                    "the flood-stage watermark). Error: %s",
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:577:        unmarked). Dedups and batches the ids under the OpenSearch terms cap so a large
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:578:        mid-port purge can't build an oversized terms query. Returns chunks deleted.
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:596:        surface_document_missing: bool = False,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:636:                properties_to_update[ACCESS_CONTROL_LIST_FIELD_NAME] = (
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:637:                    generate_opensearch_filtered_access_control_list(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:742:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:745:        batch_retrieval: bool = False,  # noqa: ARG002
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:763:                # NOTE: Index filters includes metadata tags which were filtered
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:765:                # ideal to do filtering here as well, in practice we never did
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:769:                index_filters=filters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:799:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:818:            # NOTE: Index filters includes metadata tags which were filtered
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:820:            # ideal to do filtering here as well, in practice we never did
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:824:            index_filters=filters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:851:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:853:        include_hidden: bool = False,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:866:            # NOTE: Index filters includes metadata tags which were filtered
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:868:            # ideal to do filtering here as well, in practice we never did
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:872:            index_filters=filters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:896:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:910:            # NOTE: Index filters includes metadata tags which were filtered
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:912:            # ideal to do filtering here as well, in practice we never did
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:916:            index_filters=filters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:939:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:941:        dirty: bool | None = None,  # noqa: ARG002
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:950:            index_filters=filters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:971:        self, chunks: list[DocumentChunk], use_create_only: bool = False
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1021:        primary_backfill_in_progress: bool = False,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1097:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1098:        batch_retrieval: bool = False,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1101:            chunk_requests, filters, batch_retrieval
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1110:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1118:            filters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1125:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1127:        include_hidden: bool = False,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1130:            query, filters, num_to_retrieve, include_hidden=include_hidden
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1136:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1140:            query_embedding, filters, num_to_retrieve
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1145:        filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1147:        dirty: bool | None = None,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:1149:        return self._primary.random_retrieval(filters, num_to_retrieve, dirty)
HEAD:backend/onyx/document_index/opensearch/port_copy.py:90:    should_abort: Callable[[], bool] | None = None,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:91:) -> tuple[int, bool]:
HEAD:backend/onyx/document_index/opensearch/port_copy.py:202:        should_abort: Callable[[], bool] | None = None,
HEAD:backend/onyx/document_index/opensearch/port_copy.py:203:    ) -> tuple[int, bool]:
HEAD:backend/onyx/document_index/opensearch/schema.py:29:from onyx.document_index.opensearch.string_filtering import (
HEAD:backend/onyx/document_index/opensearch/schema.py:32:    filter_and_validate_document_id,
HEAD:backend/onyx/document_index/opensearch/schema.py:35:from onyx.utils.tenant import get_tenant_id_short_string
HEAD:backend/onyx/document_index/opensearch/schema.py:37:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/onyx/document_index/opensearch/schema.py:48:ACCESS_CONTROL_LIST_FIELD_NAME = "access_control_list"
HEAD:backend/onyx/document_index/opensearch/schema.py:61:TENANT_ID_FIELD_NAME = "tenant_id"
HEAD:backend/onyx/document_index/opensearch/schema.py:68:# Hierarchy filtering - list of ancestor hierarchy node IDs
HEAD:backend/onyx/document_index/opensearch/schema.py:98:        short_tenant_id: str = get_tenant_id_short_string(tenant_state.tenant_id)
HEAD:backend/onyx/document_index/opensearch/schema.py:102:        opensearch_doc_chunk_id_tenant_prefix = f"{short_tenant_id}__"
HEAD:backend/onyx/document_index/opensearch/schema.py:109:        sanitized_document_id: str = filter_and_validate_document_id(
HEAD:backend/onyx/document_index/opensearch/schema.py:122:        # Subtract 1 because filter_and_validate_document_id compares on >= on
HEAD:backend/onyx/document_index/opensearch/schema.py:133:    opensearch_doc_chunk_id = filter_and_validate_document_id(opensearch_doc_chunk_id)
HEAD:backend/onyx/document_index/opensearch/schema.py:145:    get_current_tenant_id. Generally relying on global state is bad, in this
HEAD:backend/onyx/document_index/opensearch/schema.py:173:    public: bool
HEAD:backend/onyx/document_index/opensearch/schema.py:174:    access_control_list: list[str]
HEAD:backend/onyx/document_index/opensearch/schema.py:176:    hidden: bool = False
HEAD:backend/onyx/document_index/opensearch/schema.py:180:    written_by_port: bool | None = None
HEAD:backend/onyx/document_index/opensearch/schema.py:204:    # List of ancestor hierarchy node IDs for hierarchy-based filtering.
HEAD:backend/onyx/document_index/opensearch/schema.py:206:    # hierarchy-filtered searches).
HEAD:backend/onyx/document_index/opensearch/schema.py:209:    tenant_id: TenantState = Field(
HEAD:backend/onyx/document_index/opensearch/schema.py:211:            tenant_id=get_current_tenant_id(), multitenant=MULTI_TENANT
HEAD:backend/onyx/document_index/opensearch/schema.py:218:            f"content length={len(self.content)}, tenant_id={self.tenant_id.tenant_id})."
HEAD:backend/onyx/document_index/opensearch/schema.py:280:    @field_serializer("tenant_id", mode="wrap")
HEAD:backend/onyx/document_index/opensearch/schema.py:291:        tenant_id field, so we don't want to supply it in our serialized
HEAD:backend/onyx/document_index/opensearch/schema.py:298:            return value.tenant_id
HEAD:backend/onyx/document_index/opensearch/schema.py:300:    @field_validator("tenant_id", mode="before")
HEAD:backend/onyx/document_index/opensearch/schema.py:302:    def parse_tenant_id(cls, value: Any) -> TenantState:
HEAD:backend/onyx/document_index/opensearch/schema.py:304:        Generates a TenantState from OpenSearch's tenant_id if it exists, or
HEAD:backend/onyx/document_index/opensearch/schema.py:311:                    "Bug: No tenant_id was supplied but multi-tenant mode is enabled."
HEAD:backend/onyx/document_index/opensearch/schema.py:314:                tenant_id=get_current_tenant_id(), multitenant=MULTI_TENANT
HEAD:backend/onyx/document_index/opensearch/schema.py:326:                f"Bug: Expected a str for the tenant_id property from OpenSearch, got {type(value)} instead."
HEAD:backend/onyx/document_index/opensearch/schema.py:331:                    "Bug: Got a non-null str for the tenant_id property from OpenSearch but "
HEAD:backend/onyx/document_index/opensearch/schema.py:333:                    "mode we don't expect to see a tenant_id."
HEAD:backend/onyx/document_index/opensearch/schema.py:335:            return TenantState(tenant_id=value, multitenant=MULTI_TENANT)
HEAD:backend/onyx/document_index/opensearch/schema.py:354:            f"tenant_id={self.tenant_id.tenant_id})"
HEAD:backend/onyx/document_index/opensearch/schema.py:375:    def get_document_schema(vector_dimension: int, multitenant: bool) -> dict[str, Any]:
HEAD:backend/onyx/document_index/opensearch/schema.py:387:            filtering, etc.
HEAD:backend/onyx/document_index/opensearch/schema.py:407:                determined by OpenSearch documentation.
HEAD:backend/onyx/document_index/opensearch/schema.py:479:                # control list but is such a broad and critical filter that it
HEAD:backend/onyx/document_index/opensearch/schema.py:480:                # is its own field. If true, ACCESS_CONTROL_LIST_FIELD_NAME
HEAD:backend/onyx/document_index/opensearch/schema.py:482:                PUBLIC_FIELD_NAME: {"type": "boolean"},
HEAD:backend/onyx/document_index/opensearch/schema.py:490:                ACCESS_CONTROL_LIST_FIELD_NAME: {"type": "keyword"},
HEAD:backend/onyx/document_index/opensearch/schema.py:492:                # Should clobber all other access search filters, namely
HEAD:backend/onyx/document_index/opensearch/schema.py:493:                # PUBLIC_FIELD_NAME and ACCESS_CONTROL_LIST_FIELD_NAME; up to
HEAD:backend/onyx/document_index/opensearch/schema.py:495:                HIDDEN_FIELD_NAME: {"type": "boolean"},
HEAD:backend/onyx/document_index/opensearch/schema.py:496:                # Marks port-written chunks; filtered by the orphan sweep's delete-by-query.
HEAD:backend/onyx/document_index/opensearch/schema.py:497:                WRITTEN_BY_PORT_FIELD_NAME: {"type": "boolean"},
HEAD:backend/onyx/document_index/opensearch/schema.py:572:                # Hierarchy filtering - list of ancestor hierarchy node IDs.
HEAD:backend/onyx/document_index/opensearch/schema.py:574:                # OpenSearch's terms query with value_type: "bitmap" can
HEAD:backend/onyx/document_index/opensearch/schema.py:582:            schema["properties"][TENANT_ID_FIELD_NAME] = {"type": "keyword"}
HEAD:backend/onyx/document_index/opensearch/search.py:12:from onyx.context.search.models import IndexFilters, Tag, TimeRange
HEAD:backend/onyx/document_index/opensearch/search.py:24:    ACCESS_CONTROL_LIST_FIELD_NAME,
HEAD:backend/onyx/document_index/opensearch/search.py:39:    TENANT_ID_FIELD_NAME,
HEAD:backend/onyx/document_index/opensearch/search.py:47:# See https://docs.opensearch.org/latest/query-dsl/term/terms/.
HEAD:backend/onyx/document_index/opensearch/search.py:48:MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY = 65_536
HEAD:backend/onyx/document_index/opensearch/search.py:52:TermsQuery: TypeAlias = dict[str, dict[str, list[_T]]]
HEAD:backend/onyx/document_index/opensearch/search.py:53:TermQuery: TypeAlias = dict[str, dict[str, dict[str, _T]]]
HEAD:backend/onyx/document_index/opensearch/search.py:181:        index_filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/search.py:182:        include_hidden: bool,
HEAD:backend/onyx/document_index/opensearch/search.py:186:        get_full_document: bool = True,
HEAD:backend/onyx/document_index/opensearch/search.py:200:            index_filters: Filters for the document retrieval query.
HEAD:backend/onyx/document_index/opensearch/search.py:218:        filter_clauses = DocumentQuery._get_search_filters(
HEAD:backend/onyx/document_index/opensearch/search.py:221:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:222:            source_types=index_filters.source_type or [],
HEAD:backend/onyx/document_index/opensearch/search.py:223:            tags=index_filters.tags or [],
HEAD:backend/onyx/document_index/opensearch/search.py:224:            document_sets=index_filters.document_set or [],
HEAD:backend/onyx/document_index/opensearch/search.py:225:            project_id_filter=index_filters.project_id_filter,
HEAD:backend/onyx/document_index/opensearch/search.py:226:            persona_id_filter=index_filters.persona_id_filter,
HEAD:backend/onyx/document_index/opensearch/search.py:227:            created_at_range=index_filters.created_at_range,
HEAD:backend/onyx/document_index/opensearch/search.py:228:            updated_at_range=index_filters.updated_at_range,
HEAD:backend/onyx/document_index/opensearch/search.py:233:            attached_document_ids=index_filters.attached_document_ids,
HEAD:backend/onyx/document_index/opensearch/search.py:234:            hierarchy_node_ids=index_filters.hierarchy_node_ids,
HEAD:backend/onyx/document_index/opensearch/search.py:237:            "query": {"bool": {"filter": filter_clauses}},
HEAD:backend/onyx/document_index/opensearch/search.py:284:        filter_clauses = DocumentQuery._get_search_filters(
HEAD:backend/onyx/document_index/opensearch/search.py:288:            access_control_list=None,
HEAD:backend/onyx/document_index/opensearch/search.py:292:            project_id_filter=None,
HEAD:backend/onyx/document_index/opensearch/search.py:293:            persona_id_filter=None,
HEAD:backend/onyx/document_index/opensearch/search.py:302:            "query": {"bool": {"filter": filter_clauses}},
HEAD:backend/onyx/document_index/opensearch/search.py:319:        filter_clauses: list[dict[str, Any]] = [
HEAD:backend/onyx/document_index/opensearch/search.py:320:            {"terms": {DOCUMENT_ID_FIELD_NAME: list(document_ids)}},
HEAD:backend/onyx/document_index/opensearch/search.py:321:            {"term": {WRITTEN_BY_PORT_FIELD_NAME: {"value": True}}},
HEAD:backend/onyx/document_index/opensearch/search.py:323:        # Single-tenant indices have no tenant_id field (added only in multitenant mode);
HEAD:backend/onyx/document_index/opensearch/search.py:324:        # a term on the unmapped field would match zero docs. Mirror _get_search_filters.
HEAD:backend/onyx/document_index/opensearch/search.py:326:            filter_clauses.append(
HEAD:backend/onyx/document_index/opensearch/search.py:327:                {"term": {TENANT_ID_FIELD_NAME: {"value": tenant_state.tenant_id}}}
HEAD:backend/onyx/document_index/opensearch/search.py:330:            "query": {"bool": {"filter": filter_clauses}},
HEAD:backend/onyx/document_index/opensearch/search.py:344:        index_filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/search.py:345:        include_hidden: bool,
HEAD:backend/onyx/document_index/opensearch/search.py:361:            index_filters: Filters for the hybrid search query.
HEAD:backend/onyx/document_index/opensearch/search.py:383:        hybrid_search_filters = DocumentQuery._get_search_filters(
HEAD:backend/onyx/document_index/opensearch/search.py:386:            # TODO(andrei): We've done no filtering for PUBLIC_DOC_PAT up to
HEAD:backend/onyx/document_index/opensearch/search.py:388:            # redundant filters in queries that may affect performance.
HEAD:backend/onyx/document_index/opensearch/search.py:389:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:390:            source_types=index_filters.source_type or [],
HEAD:backend/onyx/document_index/opensearch/search.py:391:            tags=index_filters.tags or [],
HEAD:backend/onyx/document_index/opensearch/search.py:392:            document_sets=index_filters.document_set or [],
HEAD:backend/onyx/document_index/opensearch/search.py:393:            project_id_filter=index_filters.project_id_filter,
HEAD:backend/onyx/document_index/opensearch/search.py:394:            persona_id_filter=index_filters.persona_id_filter,
HEAD:backend/onyx/document_index/opensearch/search.py:395:            created_at_range=index_filters.created_at_range,
HEAD:backend/onyx/document_index/opensearch/search.py:396:            updated_at_range=index_filters.updated_at_range,
HEAD:backend/onyx/document_index/opensearch/search.py:399:            attached_document_ids=index_filters.attached_document_ids,
HEAD:backend/onyx/document_index/opensearch/search.py:400:            hierarchy_node_ids=index_filters.hierarchy_node_ids,
HEAD:backend/onyx/document_index/opensearch/search.py:401:            forced_document_sets=index_filters.forced_document_set,
HEAD:backend/onyx/document_index/opensearch/search.py:420:                # https://opensearch.org/blog/introducing-common-filter-support-for-hybrid-search-queries
HEAD:backend/onyx/document_index/opensearch/search.py:421:                # Does AND for each filter in the list.
HEAD:backend/onyx/document_index/opensearch/search.py:422:                "filter": {"bool": {"filter": hybrid_search_filters}},
HEAD:backend/onyx/document_index/opensearch/search.py:454:        index_filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/search.py:455:        include_hidden: bool,
HEAD:backend/onyx/document_index/opensearch/search.py:468:            index_filters: Filters for the keyword search query.
HEAD:backend/onyx/document_index/opensearch/search.py:480:        keyword_search_filters = DocumentQuery._get_search_filters(
HEAD:backend/onyx/document_index/opensearch/search.py:483:            # TODO(andrei): We've done no filtering for PUBLIC_DOC_PAT up to
HEAD:backend/onyx/document_index/opensearch/search.py:485:            # redundant filters in queries that may affect performance.
HEAD:backend/onyx/document_index/opensearch/search.py:486:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:487:            source_types=index_filters.source_type or [],
HEAD:backend/onyx/document_index/opensearch/search.py:488:            tags=index_filters.tags or [],
HEAD:backend/onyx/document_index/opensearch/search.py:489:            document_sets=index_filters.document_set or [],
HEAD:backend/onyx/document_index/opensearch/search.py:490:            project_id_filter=index_filters.project_id_filter,
HEAD:backend/onyx/document_index/opensearch/search.py:491:            persona_id_filter=index_filters.persona_id_filter,
HEAD:backend/onyx/document_index/opensearch/search.py:492:            created_at_range=index_filters.created_at_range,
HEAD:backend/onyx/document_index/opensearch/search.py:493:            updated_at_range=index_filters.updated_at_range,
HEAD:backend/onyx/document_index/opensearch/search.py:496:            attached_document_ids=index_filters.attached_document_ids,
HEAD:backend/onyx/document_index/opensearch/search.py:497:            hierarchy_node_ids=index_filters.hierarchy_node_ids,
HEAD:backend/onyx/document_index/opensearch/search.py:498:            forced_document_sets=index_filters.forced_document_set,
HEAD:backend/onyx/document_index/opensearch/search.py:503:                query_text, search_filters=keyword_search_filters
HEAD:backend/onyx/document_index/opensearch/search.py:538:        index_filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/search.py:539:        include_hidden: bool,
HEAD:backend/onyx/document_index/opensearch/search.py:552:            index_filters: Filters for the semantic search query.
HEAD:backend/onyx/document_index/opensearch/search.py:564:        semantic_search_filters = DocumentQuery._get_search_filters(
HEAD:backend/onyx/document_index/opensearch/search.py:567:            # TODO(andrei): We've done no filtering for PUBLIC_DOC_PAT up to
HEAD:backend/onyx/document_index/opensearch/search.py:569:            # redundant filters in queries that may affect performance.
HEAD:backend/onyx/document_index/opensearch/search.py:570:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:571:            source_types=index_filters.source_type or [],
HEAD:backend/onyx/document_index/opensearch/search.py:572:            tags=index_filters.tags or [],
HEAD:backend/onyx/document_index/opensearch/search.py:573:            document_sets=index_filters.document_set or [],
HEAD:backend/onyx/document_index/opensearch/search.py:574:            project_id_filter=index_filters.project_id_filter,
HEAD:backend/onyx/document_index/opensearch/search.py:575:            persona_id_filter=index_filters.persona_id_filter,
HEAD:backend/onyx/document_index/opensearch/search.py:576:            created_at_range=index_filters.created_at_range,
HEAD:backend/onyx/document_index/opensearch/search.py:577:            updated_at_range=index_filters.updated_at_range,
HEAD:backend/onyx/document_index/opensearch/search.py:580:            attached_document_ids=index_filters.attached_document_ids,
HEAD:backend/onyx/document_index/opensearch/search.py:581:            hierarchy_node_ids=index_filters.hierarchy_node_ids,
HEAD:backend/onyx/document_index/opensearch/search.py:582:            forced_document_sets=index_filters.forced_document_set,
HEAD:backend/onyx/document_index/opensearch/search.py:589:                search_filters=semantic_search_filters,
HEAD:backend/onyx/document_index/opensearch/search.py:617:        index_filters: IndexFilters,
HEAD:backend/onyx/document_index/opensearch/search.py:624:            index_filters: Filters for the random search query.
HEAD:backend/onyx/document_index/opensearch/search.py:630:        search_filters = DocumentQuery._get_search_filters(
HEAD:backend/onyx/document_index/opensearch/search.py:633:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:634:            source_types=index_filters.source_type or [],
HEAD:backend/onyx/document_index/opensearch/search.py:635:            tags=index_filters.tags or [],
HEAD:backend/onyx/document_index/opensearch/search.py:636:            document_sets=index_filters.document_set or [],
HEAD:backend/onyx/document_index/opensearch/search.py:637:            project_id_filter=index_filters.project_id_filter,
HEAD:backend/onyx/document_index/opensearch/search.py:638:            persona_id_filter=index_filters.persona_id_filter,
HEAD:backend/onyx/document_index/opensearch/search.py:639:            created_at_range=index_filters.created_at_range,
HEAD:backend/onyx/document_index/opensearch/search.py:640:            updated_at_range=index_filters.updated_at_range,
HEAD:backend/onyx/document_index/opensearch/search.py:643:            attached_document_ids=index_filters.attached_document_ids,
HEAD:backend/onyx/document_index/opensearch/search.py:644:            hierarchy_node_ids=index_filters.hierarchy_node_ids,
HEAD:backend/onyx/document_index/opensearch/search.py:645:            forced_document_sets=index_filters.forced_document_set,
HEAD:backend/onyx/document_index/opensearch/search.py:650:                    "query": {"bool": {"filter": search_filters}},
HEAD:backend/onyx/document_index/opensearch/search.py:720:          semantic queries, there is often a lot of terms, and very low number
HEAD:backend/onyx/document_index/opensearch/search.py:722:        - fuzziness AUTO: Typo tolerance (0/1/2 edit distance by term length).
HEAD:backend/onyx/document_index/opensearch/search.py:786:        search_filters: list[dict[str, Any]] | None = None,
HEAD:backend/onyx/document_index/opensearch/search.py:797:        if search_filters is not None:
HEAD:backend/onyx/document_index/opensearch/search.py:798:            query["knn"][CONTENT_VECTOR_FIELD_NAME]["filter"] = {
HEAD:backend/onyx/document_index/opensearch/search.py:799:                "bool": {"filter": search_filters}
HEAD:backend/onyx/document_index/opensearch/search.py:807:        search_filters: list[dict[str, Any]] | None = None,
HEAD:backend/onyx/document_index/opensearch/search.py:810:            "bool": {
HEAD:backend/onyx/document_index/opensearch/search.py:835:                        # of the query's terms. More matches result in higher
HEAD:backend/onyx/document_index/opensearch/search.py:859:                # in the document. This defaults to 1, unless a filter or must
HEAD:backend/onyx/document_index/opensearch/search.py:865:        if search_filters is not None:
HEAD:backend/onyx/document_index/opensearch/search.py:866:            query["bool"]["filter"] = search_filters
HEAD:backend/onyx/document_index/opensearch/search.py:871:    def _get_search_filters(
HEAD:backend/onyx/document_index/opensearch/search.py:873:        include_hidden: bool,
HEAD:backend/onyx/document_index/opensearch/search.py:874:        access_control_list: list[str] | None,
HEAD:backend/onyx/document_index/opensearch/search.py:878:        project_id_filter: int | None,
HEAD:backend/onyx/document_index/opensearch/search.py:879:        persona_id_filter: int | None,
HEAD:backend/onyx/document_index/opensearch/search.py:886:        # Assistant knowledge filters
HEAD:backend/onyx/document_index/opensearch/search.py:892:        """Returns filters to be passed into the "filter" key of a search query.
HEAD:backend/onyx/document_index/opensearch/search.py:894:        The "filter" key applies a logical AND operator to its elements, so
HEAD:backend/onyx/document_index/opensearch/search.py:895:        every subfilter must evaluate to true in order for the document to be
HEAD:backend/onyx/document_index/opensearch/search.py:896:        retrieved. This function returns a list of such subfilters.
HEAD:backend/onyx/document_index/opensearch/search.py:897:        See https://docs.opensearch.org/latest/query-dsl/compound/bool/.
HEAD:backend/onyx/document_index/opensearch/search.py:899:        TODO(ENG-3874): The terms queries returned by this function can be made
HEAD:backend/onyx/document_index/opensearch/search.py:903:        TODO(ENG-3875): This function can take even better advantage of filter
HEAD:backend/onyx/document_index/opensearch/search.py:904:        caching by grouping "static" filters together into one sub-clause.
HEAD:backend/onyx/document_index/opensearch/search.py:909:            access_control_list: Access control list for the documents to
HEAD:backend/onyx/document_index/opensearch/search.py:920:            project_id_filter: If not None, only documents with this project ID
HEAD:backend/onyx/document_index/opensearch/search.py:923:            persona_id_filter: If not None, only documents whose personas array
HEAD:backend/onyx/document_index/opensearch/search.py:928:                See document_index/FILTER_SEMANTICS.md ("Time filtering").
HEAD:backend/onyx/document_index/opensearch/search.py:934:                maximum number of tokens it can hold. If None, no filter will be
HEAD:backend/onyx/document_index/opensearch/search.py:937:            document_id: The document ID to retrieve. If None, no filter will be
HEAD:backend/onyx/document_index/opensearch/search.py:955:            A list of filters to be passed into the "filter" key of a search
HEAD:backend/onyx/document_index/opensearch/search.py:959:        def _get_acl_visibility_filter(
HEAD:backend/onyx/document_index/opensearch/search.py:960:            access_control_list: list[str],
HEAD:backend/onyx/document_index/opensearch/search.py:961:        ) -> dict[str, dict[str, list[TermQuery[bool] | TermsQuery[str]] | int]]:
HEAD:backend/onyx/document_index/opensearch/search.py:962:            """Returns a filter for the access control list.
HEAD:backend/onyx/document_index/opensearch/search.py:964:            Since this returns an isolated bool should clause, it can be cached
HEAD:backend/onyx/document_index/opensearch/search.py:965:            in OpenSearch independently of other clauses in _get_search_filters.
HEAD:backend/onyx/document_index/opensearch/search.py:968:                access_control_list: The access control list to restrict
HEAD:backend/onyx/document_index/opensearch/search.py:973:                    than MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY.
HEAD:backend/onyx/document_index/opensearch/search.py:976:                A filter for the access control list.
HEAD:backend/onyx/document_index/opensearch/search.py:979:            acl_visibility_filter: dict[str, dict[str, Any]] = {
HEAD:backend/onyx/document_index/opensearch/search.py:980:                "bool": {
HEAD:backend/onyx/document_index/opensearch/search.py:981:                    "should": [{"term": {PUBLIC_FIELD_NAME: {"value": True}}}],
HEAD:backend/onyx/document_index/opensearch/search.py:985:            if access_control_list:
HEAD:backend/onyx/document_index/opensearch/search.py:986:                if len(access_control_list) > MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY:
HEAD:backend/onyx/document_index/opensearch/search.py:988:                        f"Too many access control list entries: {len(access_control_list)}. Max allowed: {MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY}."
HEAD:backend/onyx/document_index/opensearch/search.py:990:                # Use terms instead of a list of term within a should clause
HEAD:backend/onyx/document_index/opensearch/search.py:991:                # because Lucene will optimize the filtering for large sets of
HEAD:backend/onyx/document_index/opensearch/search.py:992:                # terms. Small sets of terms are not expected to perform any
HEAD:backend/onyx/document_index/opensearch/search.py:993:                # differently than individual term clauses.
HEAD:backend/onyx/document_index/opensearch/search.py:994:                acl_subclause: TermsQuery[str] = {
HEAD:backend/onyx/document_index/opensearch/search.py:995:                    "terms": {ACCESS_CONTROL_LIST_FIELD_NAME: list(access_control_list)}
HEAD:backend/onyx/document_index/opensearch/search.py:997:                acl_visibility_filter["bool"]["should"].append(
HEAD:backend/onyx/document_index/opensearch/search.py:1000:            return acl_visibility_filter
HEAD:backend/onyx/document_index/opensearch/search.py:1002:        def _get_source_type_filter(
HEAD:backend/onyx/document_index/opensearch/search.py:1004:        ) -> TermsQuery[str]:
HEAD:backend/onyx/document_index/opensearch/search.py:1005:            """Returns a filter for the source types.
HEAD:backend/onyx/document_index/opensearch/search.py:1007:            Since this returns an isolated terms clause, it can be cached in
HEAD:backend/onyx/document_index/opensearch/search.py:1008:            OpenSearch independently of other clauses in _get_search_filters.
HEAD:backend/onyx/document_index/opensearch/search.py:1015:                    MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY.
HEAD:backend/onyx/document_index/opensearch/search.py:1019:                A filter for the source types.
HEAD:backend/onyx/document_index/opensearch/search.py:1023:                    "source_types cannot be empty if trying to create a source type filter."
HEAD:backend/onyx/document_index/opensearch/search.py:1025:            if len(source_types) > MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY:
HEAD:backend/onyx/document_index/opensearch/search.py:1027:                    f"Too many source types: {len(source_types)}. Max allowed: {MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY}."
HEAD:backend/onyx/document_index/opensearch/search.py:1029:            # Use terms instead of a list of term within a should clause because
HEAD:backend/onyx/document_index/opensearch/search.py:1030:            # Lucene will optimize the filtering for large sets of terms. Small
HEAD:backend/onyx/document_index/opensearch/search.py:1031:            # sets of terms are not expected to perform any differently than
HEAD:backend/onyx/document_index/opensearch/search.py:1032:            # individual term clauses.
HEAD:backend/onyx/document_index/opensearch/search.py:1034:                "terms": {
HEAD:backend/onyx/document_index/opensearch/search.py:1041:        def _get_tag_filter(tags: list[Tag]) -> TermsQuery[str]:
HEAD:backend/onyx/document_index/opensearch/search.py:1042:            """Returns a filter for the tags.
HEAD:backend/onyx/document_index/opensearch/search.py:1044:            Since this returns an isolated terms clause, it can be cached in
HEAD:backend/onyx/document_index/opensearch/search.py:1045:            OpenSearch independently of other clauses in _get_search_filters.
HEAD:backend/onyx/document_index/opensearch/search.py:1052:                    MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY.
HEAD:backend/onyx/document_index/opensearch/search.py:1056:                A filter for the tags.
HEAD:backend/onyx/document_index/opensearch/search.py:1060:                    "tags cannot be empty if trying to create a tag filter."
HEAD:backend/onyx/document_index/opensearch/search.py:1062:            if len(tags) > MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY:
HEAD:backend/onyx/document_index/opensearch/search.py:1064:                    f"Too many tags: {len(tags)}. Max allowed: {MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY}."
HEAD:backend/onyx/document_index/opensearch/search.py:1072:            # Use terms instead of a list of term within a should clause because
HEAD:backend/onyx/document_index/opensearch/search.py:1073:            # Lucene will optimize the filtering for large sets of terms. Small
HEAD:backend/onyx/document_index/opensearch/search.py:1074:            # sets of terms are not expected to perform any differently than
HEAD:backend/onyx/document_index/opensearch/search.py:1075:            # individual term clauses.
HEAD:backend/onyx/document_index/opensearch/search.py:1076:            return {"terms": {METADATA_LIST_FIELD_NAME: tag_str_list}}
HEAD:backend/onyx/document_index/opensearch/search.py:1078:        def _get_document_set_filter(document_sets: list[str]) -> TermsQuery[str]:
HEAD:backend/onyx/document_index/opensearch/search.py:1079:            """Returns a filter for the document sets.
HEAD:backend/onyx/document_index/opensearch/search.py:1081:            Since this returns an isolated terms clause, it can be cached in
HEAD:backend/onyx/document_index/opensearch/search.py:1082:            OpenSearch independently of other clauses in _get_search_filters.
HEAD:backend/onyx/document_index/opensearch/search.py:1089:                    MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY.
HEAD:backend/onyx/document_index/opensearch/search.py:1093:                A filter for the document sets.
HEAD:backend/onyx/document_index/opensearch/search.py:1097:                    "document_sets cannot be empty if trying to create a document set filter."
HEAD:backend/onyx/document_index/opensearch/search.py:1099:            if len(document_sets) > MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY:
HEAD:backend/onyx/document_index/opensearch/search.py:1101:                    f"Too many document sets: {len(document_sets)}. Max allowed: {MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY}."
HEAD:backend/onyx/document_index/opensearch/search.py:1103:            # Use terms instead of a list of term within a should clause because
HEAD:backend/onyx/document_index/opensearch/search.py:1104:            # Lucene will optimize the filtering for large sets of terms. Small
HEAD:backend/onyx/document_index/opensearch/search.py:1105:            # sets of terms are not expected to perform any differently than
HEAD:backend/onyx/document_index/opensearch/search.py:1106:            # individual term clauses.
HEAD:backend/onyx/document_index/opensearch/search.py:1107:            return {"terms": {DOCUMENT_SETS_FIELD_NAME: list(document_sets)}}
HEAD:backend/onyx/document_index/opensearch/search.py:1109:        def _get_user_project_filter(project_id: int) -> TermQuery[int]:
HEAD:backend/onyx/document_index/opensearch/search.py:1110:            return {"term": {USER_PROJECTS_FIELD_NAME: {"value": project_id}}}
HEAD:backend/onyx/document_index/opensearch/search.py:1112:        def _get_persona_filter(persona_id: int) -> TermQuery[int]:
HEAD:backend/onyx/document_index/opensearch/search.py:1113:            return {"term": {PERSONAS_FIELD_NAME: {"value": persona_id}}}
HEAD:backend/onyx/document_index/opensearch/search.py:1119:            include_undated: bool,
HEAD:backend/onyx/document_index/opensearch/search.py:1123:            Isolated bool clause, so OpenSearch can cache it independently."""
HEAD:backend/onyx/document_index/opensearch/search.py:1134:                "bool": {"should": [], "minimum_should_match": 1}
HEAD:backend/onyx/document_index/opensearch/search.py:1136:            date_range_clause["bool"]["should"].append(
HEAD:backend/onyx/document_index/opensearch/search.py:1140:                date_range_clause["bool"]["should"].append(
HEAD:backend/onyx/document_index/opensearch/search.py:1141:                    {"bool": {"must_not": {"exists": {"field": field_name}}}}
HEAD:backend/onyx/document_index/opensearch/search.py:1145:        def _get_document_time_filter(
HEAD:backend/onyx/document_index/opensearch/search.py:1150:            filter. created_at always keeps undated documents (over-extend);
HEAD:backend/onyx/document_index/opensearch/search.py:1181:        def _get_chunk_index_filter(
HEAD:backend/onyx/document_index/opensearch/search.py:1191:        def _get_attached_document_id_filter(
HEAD:backend/onyx/document_index/opensearch/search.py:1193:        ) -> TermsQuery[str]:
HEAD:backend/onyx/document_index/opensearch/search.py:1195:            Returns a filter for documents explicitly attached to an assistant.
HEAD:backend/onyx/document_index/opensearch/search.py:1197:            Since this returns an isolated terms clause, it can be cached in
HEAD:backend/onyx/document_index/opensearch/search.py:1198:            OpenSearch independently of other clauses in _get_search_filters.
HEAD:backend/onyx/document_index/opensearch/search.py:1205:                    MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY.
HEAD:backend/onyx/document_index/opensearch/search.py:1209:                A filter for the document IDs.
HEAD:backend/onyx/document_index/opensearch/search.py:1213:                    "doc_ids cannot be empty if trying to create a document ID filter."
HEAD:backend/onyx/document_index/opensearch/search.py:1215:            if len(doc_ids) > MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY:
HEAD:backend/onyx/document_index/opensearch/search.py:1217:                    f"Too many document IDs: {len(doc_ids)}. Max allowed: {MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY}."
HEAD:backend/onyx/document_index/opensearch/search.py:1219:            # Use terms instead of a list of term within a should clause because
HEAD:backend/onyx/document_index/opensearch/search.py:1220:            # Lucene will optimize the filtering for large sets of terms. Small
HEAD:backend/onyx/document_index/opensearch/search.py:1221:            # sets of terms are not expected to perform any differently than
HEAD:backend/onyx/document_index/opensearch/search.py:1222:            # individual term clauses.
HEAD:backend/onyx/document_index/opensearch/search.py:1223:            return {"terms": {DOCUMENT_ID_FIELD_NAME: list(doc_ids)}}
HEAD:backend/onyx/document_index/opensearch/search.py:1225:        def _get_hierarchy_node_filter(
HEAD:backend/onyx/document_index/opensearch/search.py:1227:        ) -> TermsQuery[int]:
HEAD:backend/onyx/document_index/opensearch/search.py:1229:            Returns a filter for chunks whose ancestors include any of the given
HEAD:backend/onyx/document_index/opensearch/search.py:1232:            Since this returns an isolated terms clause, it can be cached in
HEAD:backend/onyx/document_index/opensearch/search.py:1233:            OpenSearch independently of other clauses in _get_search_filters.
HEAD:backend/onyx/document_index/opensearch/search.py:1240:                    MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY.
HEAD:backend/onyx/document_index/opensearch/search.py:1244:                A filter for the hierarchy node IDs.
HEAD:backend/onyx/document_index/opensearch/search.py:1248:                    "node_ids cannot be empty if trying to create a hierarchy node ID filter."
HEAD:backend/onyx/document_index/opensearch/search.py:1250:            if len(node_ids) > MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY:
HEAD:backend/onyx/document_index/opensearch/search.py:1252:                    f"Too many hierarchy node IDs: {len(node_ids)}. Max allowed: {MAX_NUM_TERMS_ALLOWED_IN_TERMS_QUERY}."
HEAD:backend/onyx/document_index/opensearch/search.py:1254:            # Use terms instead of a list of term within a should clause because
HEAD:backend/onyx/document_index/opensearch/search.py:1255:            # Lucene will optimize the filtering for large sets of terms. Small
HEAD:backend/onyx/document_index/opensearch/search.py:1256:            # sets of terms are not expected to perform any differently than
HEAD:backend/onyx/document_index/opensearch/search.py:1257:            # individual term clauses.
HEAD:backend/onyx/document_index/opensearch/search.py:1258:            return {"terms": {ANCESTOR_HIERARCHY_NODE_IDS_FIELD_NAME: list(node_ids)}}
HEAD:backend/onyx/document_index/opensearch/search.py:1265:        filter_clauses: list[dict[str, Any]] = []
HEAD:backend/onyx/document_index/opensearch/search.py:1268:            filter_clauses.append({"term": {HIDDEN_FIELD_NAME: {"value": False}}})
HEAD:backend/onyx/document_index/opensearch/search.py:1270:        if access_control_list is not None:
HEAD:backend/onyx/document_index/opensearch/search.py:1276:            filter_clauses.append(_get_acl_visibility_filter(access_control_list))
HEAD:backend/onyx/document_index/opensearch/search.py:1280:            # knowledge_filter below), so it INTERSECTS rather than widens; placed
HEAD:backend/onyx/document_index/opensearch/search.py:1282:            filter_clauses.append(_get_document_set_filter(forced_document_sets))
HEAD:backend/onyx/document_index/opensearch/search.py:1288:            filter_clauses.append(_get_source_type_filter(source_types))
HEAD:backend/onyx/document_index/opensearch/search.py:1294:            filter_clauses.append(_get_tag_filter(tags))
HEAD:backend/onyx/document_index/opensearch/search.py:1300:        # persona_id_filter is a primary trigger — a persona with user files IS
HEAD:backend/onyx/document_index/opensearch/search.py:1303:        # project_id_filter is a primary trigger — a chat inside a project is
HEAD:backend/onyx/document_index/opensearch/search.py:1304:        # scoped to that project, so project_id_filter restricts the search to
HEAD:backend/onyx/document_index/opensearch/search.py:1311:            or persona_id_filter is not None
HEAD:backend/onyx/document_index/opensearch/search.py:1312:            or project_id_filter is not None
HEAD:backend/onyx/document_index/opensearch/search.py:1316:            # Since this returns an isolated bool should clause, it can be
HEAD:backend/onyx/document_index/opensearch/search.py:1318:            # _get_search_filters.
HEAD:backend/onyx/document_index/opensearch/search.py:1319:            knowledge_filter: dict[str, Any] = {
HEAD:backend/onyx/document_index/opensearch/search.py:1320:                "bool": {"should": [], "minimum_should_match": 1}
HEAD:backend/onyx/document_index/opensearch/search.py:1323:                knowledge_filter["bool"]["should"].append(
HEAD:backend/onyx/document_index/opensearch/search.py:1324:                    _get_attached_document_id_filter(attached_document_ids)
HEAD:backend/onyx/document_index/opensearch/search.py:1327:                knowledge_filter["bool"]["should"].append(
HEAD:backend/onyx/document_index/opensearch/search.py:1328:                    _get_hierarchy_node_filter(hierarchy_node_ids)
HEAD:backend/onyx/document_index/opensearch/search.py:1331:                knowledge_filter["bool"]["should"].append(
HEAD:backend/onyx/document_index/opensearch/search.py:1332:                    _get_document_set_filter(document_sets)
HEAD:backend/onyx/document_index/opensearch/search.py:1334:            if persona_id_filter is not None:
HEAD:backend/onyx/document_index/opensearch/search.py:1335:                knowledge_filter["bool"]["should"].append(
HEAD:backend/onyx/document_index/opensearch/search.py:1336:                    _get_persona_filter(persona_id_filter)
HEAD:backend/onyx/document_index/opensearch/search.py:1338:            if project_id_filter is not None:
HEAD:backend/onyx/document_index/opensearch/search.py:1339:                knowledge_filter["bool"]["should"].append(
HEAD:backend/onyx/document_index/opensearch/search.py:1340:                    _get_user_project_filter(project_id_filter)
HEAD:backend/onyx/document_index/opensearch/search.py:1342:            filter_clauses.append(knowledge_filter)
HEAD:backend/onyx/document_index/opensearch/search.py:1345:            filter_clauses.extend(
HEAD:backend/onyx/document_index/opensearch/search.py:1346:                _get_document_time_filter(created_at_range, updated_at_range)
HEAD:backend/onyx/document_index/opensearch/search.py:1350:            filter_clauses.append(
HEAD:backend/onyx/document_index/opensearch/search.py:1351:                _get_chunk_index_filter(min_chunk_index, max_chunk_index)
HEAD:backend/onyx/document_index/opensearch/search.py:1355:            filter_clauses.append(
HEAD:backend/onyx/document_index/opensearch/search.py:1356:                {"term": {DOCUMENT_ID_FIELD_NAME: {"value": document_id}}}
HEAD:backend/onyx/document_index/opensearch/search.py:1360:            filter_clauses.append(
HEAD:backend/onyx/document_index/opensearch/search.py:1361:                {"term": {MAX_CHUNK_SIZE_FIELD_NAME: {"value": max_chunk_size}}}
HEAD:backend/onyx/document_index/opensearch/search.py:1365:            filter_clauses.append(
HEAD:backend/onyx/document_index/opensearch/search.py:1366:                {"term": {TENANT_ID_FIELD_NAME: {"value": tenant_state.tenant_id}}}
HEAD:backend/onyx/document_index/opensearch/search.py:1369:        return filter_clauses
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:7:    """Raised when a document ID is too long for OpenSearch after filtering."""
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:10:def filter_and_validate_document_id(
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:14:    Filters and validates a document ID such that it can be used as an ID in
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:29:        document_id: The document ID to filter and validate.
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:31:            filtering in bytes. Compared with >= for extra resilience, so
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:35:        DocumentIDTooLongError: If the document ID is too long after filtering.
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:36:        ValueError: If the document ID is empty after filtering.
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:39:        str: The filtered document ID.
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:41:    filtered_document_id = re.sub(r"[^A-Za-z0-9_.\-~]", "", document_id)
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:42:    if not filtered_document_id:
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:43:        raise ValueError(f"Document ID {document_id} is empty after filtering.")
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:44:    if len(filtered_document_id.encode("utf-8")) >= max_encoded_length:
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:46:            f"Document ID {document_id} is too long after filtering."
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:48:    return filtered_document_id
```
## Vespa Filter Evidence
Evidence lines: 180
```text
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:11:        field tenant_id type string {
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:13:            rank: filter
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:20:            rank: filter
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:77:            rank: filter
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:94:            rank: filter
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:128:        # Needs to have a separate Attribute list for efficient filtering
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:131:            rank:filter
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:159:        field access_control_list type weightedset<string> {
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:161:            rank: filter
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:166:            rank: filter
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:171:            rank: filter
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:176:            rank: filter
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:181:            rank: filter
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:186:            rank: filter
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:22:from onyx.context.search.models import IndexFilters, InferenceChunkUncleaned
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:27:    build_vespa_filters,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:31:    ACCESS_CONTROL_LIST,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:56:    TENANT_ID,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:170:    filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:183:    acl_fieldset_entry = f"{ACCESS_CONTROL_LIST}"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:186:        and filters.access_control_list
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:192:        tenant_id_fieldset_entry = f"{TENANT_ID}"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:193:        if field_set_list and tenant_id_fieldset_entry not in field_set_list:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:194:            field_set_list.append(tenant_id_fieldset_entry)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:201:    # build filters
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:202:    selection = f"{index_name}.document_id=='{chunk_request.document_id}'"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:205:        selection += f" and {index_name}.chunk_id>={chunk_request.min_chunk_ind or 0}"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:206:        selection += f" and {index_name}.chunk_id<={chunk_request.max_chunk_ind}"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:208:        selection += f" and {index_name}.large_chunk_reference_ids == null"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:210:    # enforcing tenant_id through a == condition
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:212:        if filters.tenant_id:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:213:            selection += f" and {index_name}.tenant_id=='{filters.tenant_id}'"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:217:    # Setting up the selection criteria in the query parameters
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:220:        # for the ACL in the selection. Instead, we have to check as a postfilter
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:221:        "selection": selection,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:234:            filtered_params = {k: v for k, v in params.items() if v is not None}
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:236:                response = http_client.get(url, params=filtered_params)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:259:                if filters.access_control_list:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:260:                    document_acl = document["fields"].get(ACCESS_CONTROL_LIST)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:262:                        user_acl_entry in document_acl
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:263:                        for user_acl_entry in filters.access_control_list
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:268:                    if not filters.tenant_id:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:270:                    document_tenant_id = document["fields"].get(TENANT_ID)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:271:                    if document_tenant_id != filters.tenant_id:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:277:                            filters.tenant_id,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:298:    """Gets all chunks in Vespa matching the filters, paginated.
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:305:        tenant_state: The tenant state to filter by.
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:334:        selection: str = f"{index_name}.large_chunk_reference_ids == null"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:336:            selection += f" and {index_name}.tenant_id=='{tenant_state.tenant_id}'"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:341:            "selection": selection,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:457:#     filters: IndexFilters | None = None,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:463:#         filters=filters or IndexFilters(access_control_list=None),
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:473:    filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:479:            (chunk_request, index_name, filters, get_large_chunks),
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:578:    filtered_hits = [hit for hit in hits if hit["fields"].get(CONTENT) is not None]
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:580:    inference_chunks = [_vespa_hit_to_inference_chunk(hit) for hit in filtered_hits]
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:603:    filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:609:    filters_str = build_vespa_filters(filters=filters, include_hidden=True)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:613:        + filters_str
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:637:    filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:660:                    filters=filters,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:674:                filters=filters,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:683:                index_name, uncapped_requests, filters, get_large_chunks
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:28:    ACCESS_CONTROL_LIST,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:57:    TENANT_ID,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:218:        ACCESS_CONTROL_LIST: {acl_entry: 1 for acl_entry in chunk.access.to_acl()},
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:229:        if chunk.tenant_id:
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:230:            vespa_document_fields[TENANT_ID] = chunk.tenant_id
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:20:    tenant_id: str,
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:25:        tenant_state=TenantState(tenant_id=tenant_id, multitenant=MULTI_TENANT),
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:31:        kg_update_requests=kg_update_requests, tenant_id=tenant_id
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:4:from onyx.context.search.models import IndexFilters
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:7:    ACCESS_CONTROL_LIST,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:16:    TENANT_ID,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:26:def build_tenant_id_filter(tenant_id: str) -> str:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:27:    return f'({TENANT_ID} contains "{tenant_id}")'
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:30:def build_vespa_filters(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:31:    filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:36:    def _build_or_filters(key: str, vals: list[str] | None) -> str:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:37:        """For string-based 'contains' filters, e.g. WSET fields or array<string> fields.
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:46:    def _build_weighted_set_filter(key: str, vals: list[str] | None) -> str:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:47:        """Build a Vespa weightedSet filter for large value lists.
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:51:        access_control_list where a single user may have tens of thousands
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:56:        filtered = [val for val in vals if val]
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:57:        if not filtered:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:59:        items = ", ".join(f'"{val}":1' for val in filtered)
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:62:    def _build_int_or_filters(key: str, vals: list[int] | None) -> str:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:63:        """For an integer field filter.
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:70:    def _build_kg_filter(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:78:        combined_filter_parts = []
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:88:            filter_parts = [
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:92:            combined_filter_parts.append(f"({' or '.join(filter_parts)})")
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:96:            filter_parts = []
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:99:                filter_parts.append(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:105:            combined_filter_parts.append(f"{' and '.join(filter_parts)}")
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:109:        return f"({' and '.join(combined_filter_parts)})"
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:111:    def _build_kg_source_filters(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:120:    def _build_kg_chunk_id_zero_only_filter(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:127:    def _build_time_filter(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:154:    def _build_user_project_filter(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:165:    def _build_persona_filter(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:181:    # Collect all top-level filter clauses, then join with " and " at the end.
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:182:    filter_parts: list[str] = []
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:185:        filter_parts.append(f"!({HIDDEN}=true)")
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:187:    # TODO: add error condition if MULTI_TENANT and no tenant_id filter is set
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:188:    if filters.tenant_id and MULTI_TENANT:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:189:        filter_parts.append(build_tenant_id_filter(filters.tenant_id))
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:191:    # ACL filters — use weightedSet for efficient matching against the
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:192:    # access_control_list weightedset<string> field.  OR-chaining thousands
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:195:    if filters.access_control_list is not None:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:197:            filter_parts,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:198:            _build_weighted_set_filter(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:199:                ACCESS_CONTROL_LIST, filters.access_control_list
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:203:    # Source type filters
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:205:        [s.value for s in filters.source_type] if filters.source_type else None
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:207:    _append(filter_parts, _build_or_filters(SOURCE_TYPE, source_strs))
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:209:    # Tag filters
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:211:    if filters.tags:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:213:            f"{tag.tag_key}{INDEX_SEPARATOR}{tag.tag_value}" for tag in filters.tags
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:215:    _append(filter_parts, _build_or_filters(METADATA_LIST, tag_attributes))
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:221:    # persona_id_filter is a primary trigger — a persona with user files IS
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:224:    # project_id_filter is additive — it widens the scope to also cover
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:230:        knowledge_scope_parts, _build_or_filters(DOCUMENT_SETS, filters.document_set)
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:232:    _append(knowledge_scope_parts, _build_persona_filter(filters.persona_id_filter))
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:234:    # project_id_filter only widens an existing scope.
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:238:            _build_user_project_filter(filters.project_id_filter),
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:242:        filter_parts.append("(" + " or ".join(knowledge_scope_parts) + ")")
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:244:        filter_parts.append(knowledge_scope_parts[0])
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:248:    updated_at_range = filters.updated_at_range
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:250:        filter_parts,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:251:        _build_time_filter(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:257:    # # Knowledge Graph Filters
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:258:    # _append(filter_parts, _build_kg_filter(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:259:    #     kg_entities=filters.kg_entities,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:260:    #     kg_relationships=filters.kg_relationships,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:261:    #     kg_terms=filters.kg_terms,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:264:    # _append(filter_parts, _build_kg_source_filters(filters.kg_sources))
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:266:    # _append(filter_parts, _build_kg_chunk_id_zero_only_filter(
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:267:    #     filters.kg_chunk_id_zero_only or False
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:270:    filter_str = " and ".join(filter_parts)
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:272:    if filter_str and not remove_trailing_and:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:273:        filter_str += " and "
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:275:    return filter_str
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:33:from onyx.context.search.models import IndexFilters, InferenceChunk
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:74:    build_vespa_filters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:511:        access_control_list: _AccessControl | None = None
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:558:        access_control_list=access_update,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:613:        self._tenant_id = tenant_state.tenant_id
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:743:                tenant_id=self._tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:800:                tenant_id=self._tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:846:                        tenant_id=self._tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:867:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:886:                    filters=filters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:896:                filters=filters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:909:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:912:        vespa_where_clauses = build_vespa_filters(filters)
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:964:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:973:        vespa_where_clauses = build_vespa_filters(
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:974:            filters, include_hidden=include_hidden
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:996:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1003:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1007:        vespa_where_clauses = build_vespa_filters(filters, remove_trailing_and=True)
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1040:            filters=IndexFilters(access_control_list=None, tenant_id=self._tenant_id),
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1070:                tenant_id=self._tenant_id, multitenant=MULTI_TENANT
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1091:                        tenant_id=self._tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1108:        Includes large chunks. There is no way to filter these out using the
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1112:            f'tenant_id contains "{self._tenant_id}"' if self._multitenant else "true"
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1114:        yql = f"select documentid from {self._index_name} where {where_clause} limit 0"  # noqa: S608 - Vespa YQL with internal index_name/tenant_id
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1184:        tenant_id: str,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1203:                tenant_id=tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1308:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1312:            chunk_requests, filters, batch_retrieval
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1321:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1329:            filters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1336:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1341:            query, filters, num_to_retrieve, include_hidden=include_hidden
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1347:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1351:            query_embedding, filters, num_to_retrieve
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1356:        filters: IndexFilters,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1360:        return self._primary.random_retrieval(filters, num_to_retrieve, dirty)
```
Onyx contains multiple index-backend implementations. Their security behavior
must be evaluated independently when active.
## Reranking
Evidence lines: 126
```text
HEAD:backend/model_server/legacy/README.md:3:We stopped using rerankers because the state of the art rerankers are not significantly better than the biencoders and much worse than LLMs which are also capable of acting on a small set of documents for filtering, reranking, etc.
HEAD:backend/model_server/legacy/reranker.py:11:# from shared_configs.model_server_models import RerankRequest
HEAD:backend/model_server/legacy/reranker.py:12:# from shared_configs.model_server_models import RerankResponse
HEAD:backend/model_server/legacy/reranker.py:15:#     from sentence_transformers import CrossEncoder
HEAD:backend/model_server/legacy/reranker.py:21:# _RERANK_MODEL: Optional["CrossEncoder"] = None
HEAD:backend/model_server/legacy/reranker.py:24:# def get_local_reranking_model(
HEAD:backend/model_server/legacy/reranker.py:26:# ) -> "CrossEncoder":
HEAD:backend/model_server/legacy/reranker.py:27:#     global _RERANK_MODEL
HEAD:backend/model_server/legacy/reranker.py:28:#     from sentence_transformers import CrossEncoder
HEAD:backend/model_server/legacy/reranker.py:30:#     if _RERANK_MODEL is None:
HEAD:backend/model_server/legacy/reranker.py:32:#         model = CrossEncoder(model_name)
HEAD:backend/model_server/legacy/reranker.py:33:#         _RERANK_MODEL = model
HEAD:backend/model_server/legacy/reranker.py:34:#     return _RERANK_MODEL
HEAD:backend/model_server/legacy/reranker.py:38:# async def local_rerank(query: str, docs: list[str], model_name: str) -> list[float]:
HEAD:backend/model_server/legacy/reranker.py:39:#     cross_encoder = get_local_reranking_model(model_name)
HEAD:backend/model_server/legacy/reranker.py:40:#     # Run CPU-bound reranking in a thread pool
HEAD:backend/model_server/legacy/reranker.py:43:#         lambda: cross_encoder.predict([(query, doc) for doc in docs]).tolist(),
HEAD:backend/model_server/legacy/reranker.py:47:# @router.post("/cross-encoder-scores")
HEAD:backend/model_server/legacy/reranker.py:48:# async def process_rerank_request(rerank_request: RerankRequest) -> RerankResponse:
HEAD:backend/model_server/legacy/reranker.py:49:#     """Cross encoders can be purely black box from the app perspective"""
HEAD:backend/model_server/legacy/reranker.py:51:#     if rerank_request.provider_type is not None:
HEAD:backend/model_server/legacy/reranker.py:53:#             f"Model server reranking endpoint should only be used for local models. "
HEAD:backend/model_server/legacy/reranker.py:54:#             f"API provider '{rerank_request.provider_type}' should make direct API calls instead."
HEAD:backend/model_server/legacy/reranker.py:58:#         raise RuntimeError("Indexing model server should not call reranking endpoint")
HEAD:backend/model_server/legacy/reranker.py:60:#     if not rerank_request.documents or not rerank_request.query:
HEAD:backend/model_server/legacy/reranker.py:62:#             status_code=400, detail="Missing documents or query for reranking"
HEAD:backend/model_server/legacy/reranker.py:64:#     if not all(rerank_request.documents):
HEAD:backend/model_server/legacy/reranker.py:65:#         raise ValueError("Empty documents cannot be reranked.")
HEAD:backend/model_server/legacy/reranker.py:68:#         # At this point, provider_type is None, so handle local reranking
HEAD:backend/model_server/legacy/reranker.py:69:#         sim_scores = await local_rerank(
HEAD:backend/model_server/legacy/reranker.py:70:#             query=rerank_request.query,
HEAD:backend/model_server/legacy/reranker.py:71:#             docs=rerank_request.documents,
HEAD:backend/model_server/legacy/reranker.py:72:#             model_name=rerank_request.model_name,
HEAD:backend/model_server/legacy/reranker.py:74:#         return RerankResponse(scores=sim_scores)
HEAD:backend/model_server/legacy/reranker.py:77:#         logger.exception(f"Error during reranking process:\n{str(e)}")
HEAD:backend/model_server/legacy/reranker.py:79:#             status_code=500, detail="Failed to run Cross-Encoder reranking"
HEAD:backend/onyx/configs/agent_configs.py:4:AGENT_DEFAULT_RERANKING_HITS = 10
HEAD:backend/onyx/configs/agent_configs.py:31:# Reranking agent configs
HEAD:backend/onyx/configs/agent_configs.py:32:AGENT_RERANKING_MAX_QUERY_RETRIEVAL_RESULTS = int(
HEAD:backend/onyx/configs/agent_configs.py:33:    os.environ.get("AGENT_RERANKING_MAX_QUERY_RETRIEVAL_RESULTS")
HEAD:backend/onyx/configs/agent_configs.py:34:    or AGENT_DEFAULT_RERANKING_HITS
HEAD:backend/onyx/configs/app_configs.py:1633:# Should match the rerank-count value set in
HEAD:backend/onyx/configs/app_configs.py:1635:RERANK_COUNT = int(os.environ.get("RERANK_COUNT") or 1000)
HEAD:backend/onyx/configs/kg_configs.py:93:_KG_NORMALIZATION_RERANK_UNIGRAM_WEIGHT: float = max(
HEAD:backend/onyx/configs/kg_configs.py:95:    min(1, float(os.environ.get("KG_NORMALIZATION_RERANK_UNIGRAM_WEIGHT", "0.25"))),
HEAD:backend/onyx/configs/kg_configs.py:97:_KG_NORMALIZATION_RERANK_BIGRAM_WEIGHT: float = max(
HEAD:backend/onyx/configs/kg_configs.py:99:    min(1, float(os.environ.get("KG_NORMALIZATION_RERANK_BIGRAM_WEIGHT", "0.25"))),
HEAD:backend/onyx/configs/kg_configs.py:101:_KG_NORMALIZATION_RERANK_TRIGRAM_WEIGHT: float = max(
HEAD:backend/onyx/configs/kg_configs.py:103:    min(1, float(os.environ.get("KG_NORMALIZATION_RERANK_TRIGRAM_WEIGHT", "0.5"))),
HEAD:backend/onyx/configs/kg_configs.py:105:_KG_NORMALIZATION_RERANK_NGRAM_SUMS: float = (
HEAD:backend/onyx/configs/kg_configs.py:106:    _KG_NORMALIZATION_RERANK_UNIGRAM_WEIGHT
HEAD:backend/onyx/configs/kg_configs.py:107:    + _KG_NORMALIZATION_RERANK_BIGRAM_WEIGHT
HEAD:backend/onyx/configs/kg_configs.py:108:    + _KG_NORMALIZATION_RERANK_TRIGRAM_WEIGHT
HEAD:backend/onyx/configs/kg_configs.py:111:KG_NORMALIZATION_RERANK_NGRAM_WEIGHTS: tuple[float, float, float] = (
HEAD:backend/onyx/configs/kg_configs.py:112:    _KG_NORMALIZATION_RERANK_UNIGRAM_WEIGHT / _KG_NORMALIZATION_RERANK_NGRAM_SUMS,
HEAD:backend/onyx/configs/kg_configs.py:113:    _KG_NORMALIZATION_RERANK_BIGRAM_WEIGHT / _KG_NORMALIZATION_RERANK_NGRAM_SUMS,
HEAD:backend/onyx/configs/kg_configs.py:114:    _KG_NORMALIZATION_RERANK_TRIGRAM_WEIGHT / _KG_NORMALIZATION_RERANK_NGRAM_SUMS,
HEAD:backend/onyx/configs/kg_configs.py:118:KG_NORMALIZATION_RERANK_LEVENSHTEIN_WEIGHT: float = max(
HEAD:backend/onyx/configs/kg_configs.py:120:    min(1, float(os.environ.get("KG_NORMALIZATION_RERANK_LEVENSHTEIN_WEIGHT", "0.25"))),
HEAD:backend/onyx/configs/kg_configs.py:124:KG_NORMALIZATION_RERANK_THRESHOLD: float = float(
HEAD:backend/onyx/configs/kg_configs.py:125:    os.environ.get("KG_NORMALIZATION_RERANK_THRESHOLD", "0.3")
HEAD:backend/onyx/configs/model_configs.py:7:# Embedding/Reranking Model Configs
HEAD:backend/onyx/configs/model_configs.py:31:# These are only used if reranking is turned off, to normalize the direct retrieval scores for display
HEAD:backend/onyx/document_index/opensearch/constants.py:38:# as the final 10 (worse than just a miss at the reranking step).
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:282:            rerank-count: 1000
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:351:            rerank-count: 1000
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:23:    RERANK_COUNT,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:913:        # Avoid over-fetching a very large candidate set for global-phase reranking.
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:915:        target_hits = min(max(4 * num_to_retrieve, 100), RERANK_COUNT)
HEAD:backend/onyx/kg/clustering/normalizations.py:11:    KG_NORMALIZATION_RERANK_LEVENSHTEIN_WEIGHT,
HEAD:backend/onyx/kg/clustering/normalizations.py:12:    KG_NORMALIZATION_RERANK_NGRAM_WEIGHTS,
HEAD:backend/onyx/kg/clustering/normalizations.py:13:    KG_NORMALIZATION_RERANK_THRESHOLD,
HEAD:backend/onyx/kg/clustering/normalizations.py:150:    # step 2: do a weighted ngram analysis and damerau levenshtein distance to rerank
HEAD:backend/onyx/kg/clustering/normalizations.py:166:        W_n1, W_n2, W_n3 = KG_NORMALIZATION_RERANK_NGRAM_WEIGHTS
HEAD:backend/onyx/kg/clustering/normalizations.py:175:        W_leven = KG_NORMALIZATION_RERANK_LEVENSHTEIN_WEIGHT
HEAD:backend/onyx/kg/clustering/normalizations.py:183:            filter(lambda x: x[2] > KG_NORMALIZATION_RERANK_THRESHOLD, candidates),
HEAD:backend/onyx/natural_language_processing/constants.py:2:Constants for natural language processing, including embedding and reranking models.
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:75:from shared_configs.enums import EmbeddingProvider, EmbedTextType, RerankerProvider
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:82:    RerankRequest,
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:83:    RerankResponse,
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:688:# API-based reranking functions (moved from model server)
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:689:async def cohere_rerank_api(
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:694:        response = await cohere_client.rerank(
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:700:                "Cohere rerank request rejected due to billing cap. Falling back to retrieval ordering until billing resets."
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:703:                "Cohere billing limit reached for reranking"
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:711:async def cohere_rerank_aws(
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:750:async def litellm_rerank(
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1216:class RerankingModel:
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1220:        provider_type: RerankerProvider | None,
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1236:            self.rerank_server_endpoint: str | None = (
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1237:                model_server_url + "/encoder/cross-encoder-scores"
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1241:            self.rerank_server_endpoint = None
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1243:    async def _make_direct_rerank_call(
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1253:        if self.provider_type == RerankerProvider.COHERE:
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1254:            return await cohere_rerank_api(
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1257:        elif self.provider_type == RerankerProvider.BEDROCK:
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1261:            return await cohere_rerank_aws(
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1269:        elif self.provider_type == RerankerProvider.LITELLM:
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1271:                raise ValueError("API URL is required for LiteLLM reranking.")
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1272:            return await litellm_rerank(
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1276:            raise ValueError(f"Unsupported reranking provider: {self.provider_type}")
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1280:            flow=LLMFlow.RERANK,
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1294:                        self._make_direct_rerank_call(query, passages)
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1300:                if self.rerank_server_endpoint is None:
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1302:                        "Rerank server endpoint is not configured for local models"
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1305:                rerank_request = RerankRequest(
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1315:                    self.rerank_server_endpoint,
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1316:                    json=rerank_request.model_dump(),
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1321:                return RerankResponse(**response.json()).scores
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1433:def warm_up_cross_encoder(
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1434:    rerank_model_name: str,
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1440:    logger.debug("Warming up reranking model: %s", rerank_model_name)
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1442:    reranking_model = RerankingModel(
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1443:        model_name=rerank_model_name,
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1451:            reranking_model.predict(WARM_UP_STRINGS[0], WARM_UP_STRINGS[1:])
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1452:            logger.debug("Warm-up complete for reranking model: %s", rerank_model_name)
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1455:                "Warm-up request failed for reranking model %s: %s",
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1456:                rerank_model_name,
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1463:            "Started non-blocking warm-up for reranking model: %s", rerank_model_name
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1466:        retry_rerank = warm_up_retry(reranking_model.predict)
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1467:        retry_rerank(WARM_UP_STRINGS[0], WARM_UP_STRINGS[1:])
HEAD:backend/onyx/server/features/search/api.py:66:    expansion, hybrid retrieval, reranking and section merging — and returns the
HEAD:backend/onyx/server/manage/llm/api.py:2089:            # this drops embeddings/rerankers that slip past the name check.
HEAD:backend/onyx/tracing/flows.py:59:    # Embeddings / rerank / intent (cross-process to model_server)
HEAD:backend/onyx/tracing/flows.py:62:    RERANK = "rerank"
HEAD:backend/onyx/tracing/llm_utils.py:70:    Use this for image generation, voice (TTS/STT), embeddings/rerank crossing
```
Reranking occurs after retrieval in candidate RAG paths.
Later verification must ensure unauthorized documents cannot survive into
reranking or context simply because an earlier filter was bypassed or stale.
## Retrieved Document to AI Context Assembly
Evidence lines: 600
```text
HEAD:backend/ee/onyx/server/query_and_chat/models.py:92:    search_docs: list[SearchDocWithContent]
HEAD:backend/ee/onyx/server/query_and_chat/models.py:95:    # This a list of document ids that are in the search_docs list
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:149:                search_docs=[],
HEAD:backend/ee/onyx/server/query_and_chat/streaming_models.py:18:    type: Literal["search_docs"] = "search_docs"
HEAD:backend/ee/onyx/server/query_and_chat/streaming_models.py:19:    search_docs: list[SearchDocWithContent]
HEAD:backend/onyx/chat/README.md:6:> Note: it is assumed the reader is familiar with the Onyx product and features such as Projects, User files, Citations, etc.
HEAD:backend/onyx/chat/README.md:16:- If the user has just called a search related tool, then a section about citations is included
HEAD:backend/onyx/chat/README.md:41:access. Note that the project documents are assumed to be quite useful and that they should 1. never be dropped from context, 2. is not just a needle in
HEAD:backend/onyx/chat/README.md:54:Here are some documents provided for context, they may not all be relevant:
HEAD:backend/onyx/chat/README.md:73:tool is used, a citation reminder is always added. Otherwise, by default there is no reminder. If the user configures reminders, those are added to the
HEAD:backend/onyx/chat/README.md:124:those files. The LLM is much better at referencing documents close to the end of the context window so keeping it there for ease of access.
HEAD:backend/onyx/chat/README.md:151:the built-in reminders are around citations and what tools it should call in certain situations.
HEAD:backend/onyx/chat/README.md:153:The document json includes a field for the LLM to cite (it's a single number) to make citations reliable and avoid weird artifacts. It's called "document" so
HEAD:backend/onyx/chat/README.md:154:that the LLM does not create weird artifacts in reasoning like "I should reference citation_id: 5 for...". It is also strategically placed so that it is easy to
HEAD:backend/onyx/chat/README.md:210:So it will accumulate answer tokens, reasoning tokens, tool calls, citation info, etc. This is used at the end of the flow once
HEAD:backend/onyx/chat/chat_state.py:10:from onyx.chat.citation_processor import CitationMapping
HEAD:backend/onyx/chat/chat_state.py:53:        # Store citation mapping for building citation_docs_info during partial saves
HEAD:backend/onyx/chat/chat_state.py:54:        self.citation_to_doc: CitationMapping = {}
HEAD:backend/onyx/chat/chat_state.py:63:        self._all_search_docs: dict[SearchDocKey, SearchDoc] = {}
HEAD:backend/onyx/chat/chat_state.py:64:        # Track which citation numbers were actually emitted during streaming
HEAD:backend/onyx/chat/chat_state.py:65:        self._emitted_citations: set[int] = set()
HEAD:backend/onyx/chat/chat_state.py:92:    def set_citation_mapping(self, citation_to_doc: CitationMapping) -> None:
HEAD:backend/onyx/chat/chat_state.py:93:        """Set the citation mapping from citation processor."""
HEAD:backend/onyx/chat/chat_state.py:95:            self.citation_to_doc = citation_to_doc
HEAD:backend/onyx/chat/chat_state.py:117:    def get_citation_to_doc(self) -> CitationMapping:
HEAD:backend/onyx/chat/chat_state.py:118:        """Thread-safe getter for citation_to_doc (returns a copy)."""
HEAD:backend/onyx/chat/chat_state.py:120:            return self.citation_to_doc.copy()
HEAD:backend/onyx/chat/chat_state.py:154:    def add_search_docs(
HEAD:backend/onyx/chat/chat_state.py:155:        self, search_docs: list[SearchDoc], use_simple_key: bool = True
HEAD:backend/onyx/chat/chat_state.py:160:            search_docs: List of SearchDoc objects to add
HEAD:backend/onyx/chat/chat_state.py:165:            for doc in search_docs:
HEAD:backend/onyx/chat/chat_state.py:167:                if key not in self._all_search_docs:
HEAD:backend/onyx/chat/chat_state.py:168:                    self._all_search_docs[key] = doc
HEAD:backend/onyx/chat/chat_state.py:170:    def get_all_search_docs(self) -> dict[SearchDocKey, SearchDoc]:
HEAD:backend/onyx/chat/chat_state.py:173:            return self._all_search_docs.copy()
HEAD:backend/onyx/chat/chat_state.py:175:    def add_emitted_citation(self, citation_num: int) -> None:
HEAD:backend/onyx/chat/chat_state.py:176:        """Add a citation number that was actually emitted during streaming."""
HEAD:backend/onyx/chat/chat_state.py:178:            self._emitted_citations.add(citation_num)
HEAD:backend/onyx/chat/chat_state.py:180:    def get_emitted_citations(self) -> set[int]:
HEAD:backend/onyx/chat/chat_state.py:181:        """Thread-safe getter for emitted citations (returns a copy)."""
HEAD:backend/onyx/chat/chat_state.py:183:            return self._emitted_citations.copy()
HEAD:backend/onyx/chat/chat_utils.py:67:from onyx.server.query_and_chat.streaming_models import CitationInfo
HEAD:backend/onyx/chat/chat_utils.py:304:def reorganize_citations(
HEAD:backend/onyx/chat/chat_utils.py:305:    answer: str, citations: list[CitationInfo]
HEAD:backend/onyx/chat/chat_utils.py:306:) -> tuple[str, list[CitationInfo]]:
HEAD:backend/onyx/chat/chat_utils.py:307:    """For a complete, citation-aware response, we want to reorganize the citations so that
HEAD:backend/onyx/chat/chat_utils.py:314:    all_citation_matches = re.findall(pattern, answer)
HEAD:backend/onyx/chat/chat_utils.py:316:    new_citation_info: dict[int, CitationInfo] = {}
HEAD:backend/onyx/chat/chat_utils.py:317:    for citation_match in all_citation_matches:
HEAD:backend/onyx/chat/chat_utils.py:319:            citation_num = int(citation_match[0])
HEAD:backend/onyx/chat/chat_utils.py:320:            if citation_num in new_citation_info:
HEAD:backend/onyx/chat/chat_utils.py:323:            matching_citation = next(
HEAD:backend/onyx/chat/chat_utils.py:324:                iter([c for c in citations if c.citation_number == int(citation_num)]),
HEAD:backend/onyx/chat/chat_utils.py:327:            if matching_citation is None:
HEAD:backend/onyx/chat/chat_utils.py:330:            new_citation_info[citation_num] = CitationInfo(
HEAD:backend/onyx/chat/chat_utils.py:331:                citation_number=len(new_citation_info) + 1,
HEAD:backend/onyx/chat/chat_utils.py:332:                document_id=matching_citation.document_id,
HEAD:backend/onyx/chat/chat_utils.py:337:    # Function to replace citations with their new number
HEAD:backend/onyx/chat/chat_utils.py:341:            citation_num = int(link_text)
HEAD:backend/onyx/chat/chat_utils.py:342:            if citation_num in new_citation_info:
HEAD:backend/onyx/chat/chat_utils.py:343:                link_text = new_citation_info[citation_num].citation_number
HEAD:backend/onyx/chat/chat_utils.py:353:    # if any citations weren't parsable, just add them back to be safe
HEAD:backend/onyx/chat/chat_utils.py:354:    for citation in citations:
HEAD:backend/onyx/chat/chat_utils.py:355:        if citation.citation_number not in new_citation_info:
HEAD:backend/onyx/chat/chat_utils.py:356:            new_citation_info[citation.citation_number] = citation
HEAD:backend/onyx/chat/chat_utils.py:358:    return new_answer, list(new_citation_info.values())
HEAD:backend/onyx/chat/chat_utils.py:361:def build_citation_map_from_infos(
HEAD:backend/onyx/chat/chat_utils.py:362:    citations_list: list[CitationInfo], db_docs: list[DbSearchDoc]
HEAD:backend/onyx/chat/chat_utils.py:364:    """Translate a list of streaming CitationInfo objects into a mapping of
HEAD:backend/onyx/chat/chat_utils.py:365:    citation number -> saved search doc DB id.
HEAD:backend/onyx/chat/chat_utils.py:375:    citation_to_saved_doc_id_map: dict[int, int] = {}
HEAD:backend/onyx/chat/chat_utils.py:376:    for citation in citations_list:
HEAD:backend/onyx/chat/chat_utils.py:377:        if citation.citation_number not in citation_to_saved_doc_id_map:
HEAD:backend/onyx/chat/chat_utils.py:378:            saved_id = doc_id_to_saved_doc_id_map.get(citation.document_id)
HEAD:backend/onyx/chat/chat_utils.py:380:                citation_to_saved_doc_id_map[citation.citation_number] = saved_id
HEAD:backend/onyx/chat/chat_utils.py:382:    return citation_to_saved_doc_id_map
HEAD:backend/onyx/chat/chat_utils.py:385:def build_citation_map_from_numbers(
HEAD:backend/onyx/chat/chat_utils.py:388:    """Translate parsed citation numbers (e.g., from [[n]]) into a mapping of
HEAD:backend/onyx/chat/chat_utils.py:389:    citation number -> saved search doc DB id by positional index.
HEAD:backend/onyx/chat/chat_utils.py:391:    citation_to_saved_doc_id_map: dict[int, int] = {}
HEAD:backend/onyx/chat/chat_utils.py:395:            citation_to_saved_doc_id_map[num] = db_docs[idx].id
HEAD:backend/onyx/chat/chat_utils.py:397:    return citation_to_saved_doc_id_map
HEAD:backend/onyx/chat/chat_utils.py:1026:def build_python_chat_files_from_search_docs(
HEAD:backend/onyx/chat/chat_utils.py:1027:    search_docs: list[SearchDoc],
HEAD:backend/onyx/chat/chat_utils.py:1033:    if not search_docs:
HEAD:backend/onyx/chat/chat_utils.py:1040:    for doc in search_docs:
HEAD:backend/onyx/chat/citation_processor.py:2:Dynamic Citation Processor for LLM Responses
HEAD:backend/onyx/chat/citation_processor.py:4:This module provides a citation processor that can:
HEAD:backend/onyx/chat/citation_processor.py:5:- Accept citation number to SearchDoc mappings dynamically
HEAD:backend/onyx/chat/citation_processor.py:6:- Process token streams from LLMs to extract citations
HEAD:backend/onyx/chat/citation_processor.py:7:- Handle citations in three modes: REMOVE, KEEP_MARKERS, or HYPERLINK
HEAD:backend/onyx/chat/citation_processor.py:8:- Emit CitationInfo objects for detected citations (in HYPERLINK mode)
HEAD:backend/onyx/chat/citation_processor.py:9:- Track all seen citations regardless of mode
HEAD:backend/onyx/chat/citation_processor.py:10:- Maintain a list of cited documents in order of first citation
HEAD:backend/onyx/chat/citation_processor.py:21:from onyx.server.query_and_chat.streaming_models import CitationInfo
HEAD:backend/onyx/chat/citation_processor.py:27:class CitationMode(Enum):
HEAD:backend/onyx/chat/citation_processor.py:28:    """Defines how citations should be handled in the output.
HEAD:backend/onyx/chat/citation_processor.py:30:    REMOVE: Citations are completely removed from output text.
HEAD:backend/onyx/chat/citation_processor.py:31:            No CitationInfo objects are emitted.
HEAD:backend/onyx/chat/citation_processor.py:32:            Use case: When you need to remove citations from the output if they are not shared with the user
HEAD:backend/onyx/chat/citation_processor.py:35:    KEEP_MARKERS: Original citation markers like [1], [2] are preserved unchanged.
HEAD:backend/onyx/chat/citation_processor.py:36:                  No CitationInfo objects are emitted.
HEAD:backend/onyx/chat/citation_processor.py:37:                  Use case: When you need to track citations in research agent and later process
HEAD:backend/onyx/chat/citation_processor.py:38:                  them with collapse_citations() to renumber.
HEAD:backend/onyx/chat/citation_processor.py:40:    HYPERLINK: Citations are replaced with markdown links like [[1]](url).
HEAD:backend/onyx/chat/citation_processor.py:41:               CitationInfo objects are emitted for UI tracking.
HEAD:backend/onyx/chat/citation_processor.py:50:CitationMapping: TypeAlias = dict[int, SearchDoc]
HEAD:backend/onyx/chat/citation_processor.py:65:# Main Citation Processor with Dynamic Mapping
HEAD:backend/onyx/chat/citation_processor.py:69:class DynamicCitationProcessor:
HEAD:backend/onyx/chat/citation_processor.py:71:    A citation processor that accepts dynamic citation mappings.
HEAD:backend/onyx/chat/citation_processor.py:73:    This processor is designed for multi-turn conversations where the citation
HEAD:backend/onyx/chat/citation_processor.py:75:    tokens from an LLM, detects citations (e.g., [1], [2,3], [[4]]), and handles
HEAD:backend/onyx/chat/citation_processor.py:76:    them according to the configured CitationMode:
HEAD:backend/onyx/chat/citation_processor.py:78:    CitationMode.HYPERLINK (default):
HEAD:backend/onyx/chat/citation_processor.py:79:        1. Replaces citation markers with formatted markdown links (e.g., [[1]](url))
HEAD:backend/onyx/chat/citation_processor.py:80:        2. Emits CitationInfo objects for tracking
HEAD:backend/onyx/chat/citation_processor.py:84:    CitationMode.KEEP_MARKERS:
HEAD:backend/onyx/chat/citation_processor.py:85:        1. Preserves original citation markers like [1], [2] unchanged
HEAD:backend/onyx/chat/citation_processor.py:86:        2. Does NOT emit CitationInfo objects
HEAD:backend/onyx/chat/citation_processor.py:87:        3. Still tracks all seen citations via get_seen_citations()
HEAD:backend/onyx/chat/citation_processor.py:88:        Use case: When citations need later processing (e.g., renumbering).
HEAD:backend/onyx/chat/citation_processor.py:90:    CitationMode.REMOVE:
HEAD:backend/onyx/chat/citation_processor.py:91:        1. Removes citation markers entirely from the output text
HEAD:backend/onyx/chat/citation_processor.py:92:        2. Does NOT emit CitationInfo objects
HEAD:backend/onyx/chat/citation_processor.py:93:        3. Still tracks all seen citations via get_seen_citations()
HEAD:backend/onyx/chat/citation_processor.py:97:        - Accepts citation number → SearchDoc mapping via update_citation_mapping()
HEAD:backend/onyx/chat/citation_processor.py:98:        - Configurable citation mode at initialization
HEAD:backend/onyx/chat/citation_processor.py:99:        - Always tracks seen citations regardless of mode
HEAD:backend/onyx/chat/citation_processor.py:100:        - Holds back tokens that might be partial citations
HEAD:backend/onyx/chat/citation_processor.py:101:        - Maintains list of cited SearchDocs in order of first citation
HEAD:backend/onyx/chat/citation_processor.py:103:        - Skips citation processing inside code blocks
HEAD:backend/onyx/chat/citation_processor.py:106:        processor = DynamicCitationProcessor()
HEAD:backend/onyx/chat/citation_processor.py:108:        # Set up citation mapping
HEAD:backend/onyx/chat/citation_processor.py:109:        processor.update_citation_mapping({1: search_doc1, 2: search_doc2})
HEAD:backend/onyx/chat/citation_processor.py:116:                elif isinstance(result, CitationInfo):
HEAD:backend/onyx/chat/citation_processor.py:117:                    handle_citation(result)  # Track citation
HEAD:backend/onyx/chat/citation_processor.py:123:        processor = DynamicCitationProcessor(citation_mode=CitationMode.KEEP_MARKERS)
HEAD:backend/onyx/chat/citation_processor.py:124:        processor.update_citation_mapping({1: search_doc1, 2: search_doc2})
HEAD:backend/onyx/chat/citation_processor.py:129:                # Only strings are yielded, no CitationInfo objects
HEAD:backend/onyx/chat/citation_processor.py:132:        # Get all seen citations after processing
HEAD:backend/onyx/chat/citation_processor.py:133:        seen_citations = processor.get_seen_citations()  # {1: search_doc1, ...}
HEAD:backend/onyx/chat/citation_processor.py:136:        processor = DynamicCitationProcessor(citation_mode=CitationMode.REMOVE)
HEAD:backend/onyx/chat/citation_processor.py:137:        processor.update_citation_mapping({1: search_doc1, 2: search_doc2})
HEAD:backend/onyx/chat/citation_processor.py:139:        # Process tokens - citations are removed but tracked
HEAD:backend/onyx/chat/citation_processor.py:142:                print(result)  # Text without any citation markers
HEAD:backend/onyx/chat/citation_processor.py:144:        # Citations are still tracked
HEAD:backend/onyx/chat/citation_processor.py:145:        seen_citations = processor.get_seen_citations()
HEAD:backend/onyx/chat/citation_processor.py:150:        citation_mode: CitationMode = CitationMode.HYPERLINK,
HEAD:backend/onyx/chat/citation_processor.py:154:        Initialize the citation processor.
HEAD:backend/onyx/chat/citation_processor.py:157:            citation_mode: How to handle citations in the output. One of:
HEAD:backend/onyx/chat/citation_processor.py:158:                - CitationMode.HYPERLINK (default): Replace [1] with [[1]](url)
HEAD:backend/onyx/chat/citation_processor.py:159:                  and emit CitationInfo objects.
HEAD:backend/onyx/chat/citation_processor.py:160:                - CitationMode.KEEP_MARKERS: Keep original [1] markers unchanged,
HEAD:backend/onyx/chat/citation_processor.py:161:                  no CitationInfo objects emitted.
HEAD:backend/onyx/chat/citation_processor.py:162:                - CitationMode.REMOVE: Remove citations entirely from output,
HEAD:backend/onyx/chat/citation_processor.py:163:                  no CitationInfo objects emitted.
HEAD:backend/onyx/chat/citation_processor.py:164:                All modes track seen citations via get_seen_citations().
HEAD:backend/onyx/chat/citation_processor.py:170:        # Citation mapping from citation number to SearchDoc
HEAD:backend/onyx/chat/citation_processor.py:171:        self.citation_to_doc: CitationMapping = {}
HEAD:backend/onyx/chat/citation_processor.py:172:        self.seen_citations: CitationMapping = {}  # citation num -> SearchDoc
HEAD:backend/onyx/chat/citation_processor.py:176:        self.curr_segment = ""  # tokens held for citation processing
HEAD:backend/onyx/chat/citation_processor.py:179:        self.citation_mode = citation_mode
HEAD:backend/onyx/chat/citation_processor.py:181:        # Citation tracking
HEAD:backend/onyx/chat/citation_processor.py:184:        ] = []  # SearchDocs in citation order
HEAD:backend/onyx/chat/citation_processor.py:189:        self.non_citation_count = 0
HEAD:backend/onyx/chat/citation_processor.py:191:        # Citation patterns
HEAD:backend/onyx/chat/citation_processor.py:192:        # Matches potential incomplete citations: '[', '[[', '[1', '[[1', '[1,', '[1, ', etc.
HEAD:backend/onyx/chat/citation_processor.py:202:        # linear. This must mirror `citation_pattern` below, which already requires
HEAD:backend/onyx/chat/citation_processor.py:203:        # commas between numbers, so no real (closeable) citation is missed.
HEAD:backend/onyx/chat/citation_processor.py:204:        self.possible_citation_pattern = re.compile(
HEAD:backend/onyx/chat/citation_processor.py:208:        # Matches complete citations:
HEAD:backend/onyx/chat/citation_processor.py:211:        self.citation_pattern = re.compile(
HEAD:backend/onyx/chat/citation_processor.py:215:    def update_citation_mapping(
HEAD:backend/onyx/chat/citation_processor.py:217:        citation_mapping: CitationMapping,
HEAD:backend/onyx/chat/citation_processor.py:221:        Update the citation number to SearchDoc mapping.
HEAD:backend/onyx/chat/citation_processor.py:227:            citation_mapping: Dictionary mapping citation numbers (1, 2, 3, ...) to SearchDoc objects
HEAD:backend/onyx/chat/citation_processor.py:230:                The default behavior is useful when OpenURL may have the same citation number as a
HEAD:backend/onyx/chat/citation_processor.py:231:                Web Search result - in those cases, we keep the web search citation and snippet etc.
HEAD:backend/onyx/chat/citation_processor.py:235:            self.citation_to_doc.update(citation_mapping)
HEAD:backend/onyx/chat/citation_processor.py:238:            # Reason for this is that OpenURL may have the same citation number as a Web Search result
HEAD:backend/onyx/chat/citation_processor.py:239:            # For those, we should just keep the web search citation and snippet etc.
HEAD:backend/onyx/chat/citation_processor.py:240:            duplicate_keys = set(citation_mapping.keys()) & set(
HEAD:backend/onyx/chat/citation_processor.py:241:                self.citation_to_doc.keys()
HEAD:backend/onyx/chat/citation_processor.py:244:                k: v for k, v in citation_mapping.items() if k not in duplicate_keys
HEAD:backend/onyx/chat/citation_processor.py:246:            self.citation_to_doc.update(non_duplicate_mapping)
HEAD:backend/onyx/chat/citation_processor.py:250:    ) -> Generator[str | CitationInfo, None, None]:
HEAD:backend/onyx/chat/citation_processor.py:255:        1. Accumulates tokens until a complete citation or non-citation is found
HEAD:backend/onyx/chat/citation_processor.py:256:        2. Holds back potential partial citations (e.g., "[", "[1")
HEAD:backend/onyx/chat/citation_processor.py:258:        4. Handles code blocks (avoids processing citations inside code)
HEAD:backend/onyx/chat/citation_processor.py:260:        6. Always tracks seen citations in self.seen_citations
HEAD:backend/onyx/chat/citation_processor.py:262:        Behavior depends on the `citation_mode` setting from __init__:
HEAD:backend/onyx/chat/citation_processor.py:263:        - HYPERLINK: Citations are replaced with [[n]](url) format and CitationInfo
HEAD:backend/onyx/chat/citation_processor.py:264:          objects are yielded before each formatted citation
HEAD:backend/onyx/chat/citation_processor.py:265:        - KEEP_MARKERS: Original citation markers like [1] are preserved unchanged,
HEAD:backend/onyx/chat/citation_processor.py:266:          no CitationInfo objects are yielded
HEAD:backend/onyx/chat/citation_processor.py:267:        - REMOVE: Citations are removed entirely from output,
HEAD:backend/onyx/chat/citation_processor.py:268:          no CitationInfo objects are yielded
HEAD:backend/onyx/chat/citation_processor.py:275:            str: Text chunks to display. Citation format depends on citation_mode.
HEAD:backend/onyx/chat/citation_processor.py:276:            CitationInfo: Citation metadata (only when citation_mode=HYPERLINK)
HEAD:backend/onyx/chat/citation_processor.py:326:        # Look for citations in current segment
HEAD:backend/onyx/chat/citation_processor.py:327:        citation_matches = list(self.citation_pattern.finditer(self.curr_segment))
HEAD:backend/onyx/chat/citation_processor.py:328:        possible_citation_found = bool(
HEAD:backend/onyx/chat/citation_processor.py:329:            re.search(self.possible_citation_pattern, self.curr_segment)
HEAD:backend/onyx/chat/citation_processor.py:333:        if citation_matches and not in_code_block(self.llm_out):
HEAD:backend/onyx/chat/citation_processor.py:335:            for match in citation_matches:
HEAD:backend/onyx/chat/citation_processor.py:338:                # Get text before/between citations
HEAD:backend/onyx/chat/citation_processor.py:340:                self.non_citation_count += len(intermatch_str)
HEAD:backend/onyx/chat/citation_processor.py:343:                # Check if there is already a space before this citation
HEAD:backend/onyx/chat/citation_processor.py:347:                    # No text between citations (consecutive citations)
HEAD:backend/onyx/chat/citation_processor.py:348:                    # If match_idx > 0, we've already processed a citation, so don't add space
HEAD:backend/onyx/chat/citation_processor.py:350:                        # Consecutive citations - don't add space between them
HEAD:backend/onyx/chat/citation_processor.py:353:                        # Citation at start of segment - check if previous output has space
HEAD:backend/onyx/chat/citation_processor.py:362:                # Reset recent citations if no citations found for a while
HEAD:backend/onyx/chat/citation_processor.py:363:                if self.non_citation_count > 5:
HEAD:backend/onyx/chat/citation_processor.py:366:                # Process the citation (returns formatted citation text and CitationInfo objects)
HEAD:backend/onyx/chat/citation_processor.py:367:                # Always tracks seen citations regardless of citation_mode
HEAD:backend/onyx/chat/citation_processor.py:368:                citation_text, citation_info_list = self._process_citation(
HEAD:backend/onyx/chat/citation_processor.py:372:                if self.citation_mode == CitationMode.HYPERLINK:
HEAD:backend/onyx/chat/citation_processor.py:373:                    # HYPERLINK mode: Replace citations with markdown links [[n]](url)
HEAD:backend/onyx/chat/citation_processor.py:374:                    # Yield text before citation FIRST (preserve order)
HEAD:backend/onyx/chat/citation_processor.py:377:                    # Yield CitationInfo objects BEFORE the citation text
HEAD:backend/onyx/chat/citation_processor.py:378:                    # This allows the frontend to receive citation metadata before the token
HEAD:backend/onyx/chat/citation_processor.py:380:                    for citation in citation_info_list:
HEAD:backend/onyx/chat/citation_processor.py:381:                        yield citation
HEAD:backend/onyx/chat/citation_processor.py:382:                    # Then yield the formatted citation text
HEAD:backend/onyx/chat/citation_processor.py:383:                    if citation_text:
HEAD:backend/onyx/chat/citation_processor.py:384:                        yield citation_text
HEAD:backend/onyx/chat/citation_processor.py:386:                elif self.citation_mode == CitationMode.KEEP_MARKERS:
HEAD:backend/onyx/chat/citation_processor.py:387:                    # KEEP_MARKERS mode: Preserve original citation markers unchanged
HEAD:backend/onyx/chat/citation_processor.py:388:                    # Yield text before citation
HEAD:backend/onyx/chat/citation_processor.py:391:                    # Yield the original citation marker as-is
HEAD:backend/onyx/chat/citation_processor.py:394:                else:  # CitationMode.REMOVE
HEAD:backend/onyx/chat/citation_processor.py:395:                    # REMOVE mode: Remove citations entirely from output
HEAD:backend/onyx/chat/citation_processor.py:396:                    # This strips citation markers like [1], [2], 【1】 from the output text
HEAD:backend/onyx/chat/citation_processor.py:397:                    # When removing citations, we need to handle spacing to avoid issues like:
HEAD:backend/onyx/chat/citation_processor.py:413:                self.non_citation_count = 0
HEAD:backend/onyx/chat/citation_processor.py:415:            # Leftover text could be part of next citation
HEAD:backend/onyx/chat/citation_processor.py:417:            self.non_citation_count = len(self.curr_segment)
HEAD:backend/onyx/chat/citation_processor.py:419:        # Hold onto the current segment if potential citations found, otherwise stream it
HEAD:backend/onyx/chat/citation_processor.py:420:        if not possible_citation_found:
HEAD:backend/onyx/chat/citation_processor.py:422:            self.non_citation_count += len(self.curr_segment)
HEAD:backend/onyx/chat/citation_processor.py:428:    def _process_citation(
HEAD:backend/onyx/chat/citation_processor.py:430:    ) -> tuple[str, list[CitationInfo]]:
HEAD:backend/onyx/chat/citation_processor.py:432:        Process a single citation match and return formatted citation text and citation info objects.
HEAD:backend/onyx/chat/citation_processor.py:438:        1. Extracts citation numbers from the match
HEAD:backend/onyx/chat/citation_processor.py:440:        3. Tracks seen citations in self.seen_citations (regardless of citation_mode)
HEAD:backend/onyx/chat/citation_processor.py:442:        When citation_mode is HYPERLINK:
HEAD:backend/onyx/chat/citation_processor.py:443:        4. Creates formatted citation text as [[n]](url)
HEAD:backend/onyx/chat/citation_processor.py:444:        5. Creates CitationInfo objects for new citations
HEAD:backend/onyx/chat/citation_processor.py:447:        When citation_mode is REMOVE or KEEP_MARKERS:
HEAD:backend/onyx/chat/citation_processor.py:451:            match: Regex match object containing the citation pattern
HEAD:backend/onyx/chat/citation_processor.py:452:            has_leading_space: Whether the text immediately before this citation
HEAD:backend/onyx/chat/citation_processor.py:457:            Tuple of (formatted_citation_text, citation_info_list):
HEAD:backend/onyx/chat/citation_processor.py:458:            - formatted_citation_text: Markdown-formatted citation text like
HEAD:backend/onyx/chat/citation_processor.py:460:            - citation_info_list: List of CitationInfo objects for newly cited
HEAD:backend/onyx/chat/citation_processor.py:463:        citation_str: str = match.group()  # e.g., '[1]', '[1, 2, 3]', '[[1]]', '【1】'
HEAD:backend/onyx/chat/citation_processor.py:468:        citation_info_list: list[CitationInfo] = []
HEAD:backend/onyx/chat/citation_processor.py:469:        formatted_citation_parts: list[str] = []
HEAD:backend/onyx/chat/citation_processor.py:471:        # Extract citation numbers - regex ensures matched brackets, so we can simply slice
HEAD:backend/onyx/chat/citation_processor.py:472:        citation_content = citation_str[2:-2] if formatted else citation_str[1:-1]
HEAD:backend/onyx/chat/citation_processor.py:474:        for num_str in citation_content.split(","):
HEAD:backend/onyx/chat/citation_processor.py:482:                # Invalid citation, skip it
HEAD:backend/onyx/chat/citation_processor.py:483:                logger.warning("Invalid citation number format: %s", num_str)
HEAD:backend/onyx/chat/citation_processor.py:486:            # Check if we have a mapping for this citation number
HEAD:backend/onyx/chat/citation_processor.py:487:            if num not in self.citation_to_doc:
HEAD:backend/onyx/chat/citation_processor.py:489:                    "Citation number %s not found in mapping. Available: %s",
HEAD:backend/onyx/chat/citation_processor.py:491:                    list(self.citation_to_doc.keys()),
HEAD:backend/onyx/chat/citation_processor.py:496:            search_doc = self.citation_to_doc[num]
HEAD:backend/onyx/chat/citation_processor.py:500:            # Always track seen citations regardless of citation_mode setting
HEAD:backend/onyx/chat/citation_processor.py:501:            self.seen_citations[num] = search_doc
HEAD:backend/onyx/chat/citation_processor.py:503:            # Only generate formatted citations and CitationInfo in HYPERLINK mode
HEAD:backend/onyx/chat/citation_processor.py:504:            if self.citation_mode != CitationMode.HYPERLINK:
HEAD:backend/onyx/chat/citation_processor.py:507:            # Format the citation text as [[n]](link)
HEAD:backend/onyx/chat/citation_processor.py:508:            formatted_citation_parts.append(f"[[{num}]]({link})")
HEAD:backend/onyx/chat/citation_processor.py:510:            # Skip creating CitationInfo for citations of the same work if cited recently (deduplication)
HEAD:backend/onyx/chat/citation_processor.py:515:            # Track cited documents and create CitationInfo only for new citations
HEAD:backend/onyx/chat/citation_processor.py:519:                citation_info_list.append(
HEAD:backend/onyx/chat/citation_processor.py:520:                    CitationInfo(
HEAD:backend/onyx/chat/citation_processor.py:521:                        citation_number=num,
HEAD:backend/onyx/chat/citation_processor.py:526:        # Join all citation parts with spaces
HEAD:backend/onyx/chat/citation_processor.py:527:        formatted_citation_text = " ".join(formatted_citation_parts)
HEAD:backend/onyx/chat/citation_processor.py:530:        if formatted_citation_text and not has_leading_space:
HEAD:backend/onyx/chat/citation_processor.py:531:            formatted_citation_text = " " + formatted_citation_text
HEAD:backend/onyx/chat/citation_processor.py:533:        return formatted_citation_text, citation_info_list
HEAD:backend/onyx/chat/citation_processor.py:539:        Note: This list is only populated when `citation_mode=HYPERLINK`.
HEAD:backend/onyx/chat/citation_processor.py:541:        Use get_seen_citations() instead if you need to track citations without
HEAD:backend/onyx/chat/citation_processor.py:542:        emitting CitationInfo objects.
HEAD:backend/onyx/chat/citation_processor.py:546:            Empty list if citation_mode is not HYPERLINK.
HEAD:backend/onyx/chat/citation_processor.py:554:        Note: This list is only populated when `citation_mode=HYPERLINK`.
HEAD:backend/onyx/chat/citation_processor.py:556:        Use get_seen_citations() instead if you need to track citations without
HEAD:backend/onyx/chat/citation_processor.py:557:        emitting CitationInfo objects.
HEAD:backend/onyx/chat/citation_processor.py:561:            Empty list if citation_mode is not HYPERLINK.
HEAD:backend/onyx/chat/citation_processor.py:565:    def get_seen_citations(self) -> CitationMapping:
HEAD:backend/onyx/chat/citation_processor.py:567:        Get all seen citations as a mapping from citation number to SearchDoc.
HEAD:backend/onyx/chat/citation_processor.py:569:        This returns all citations that have been encountered during processing,
HEAD:backend/onyx/chat/citation_processor.py:570:        regardless of the `citation_mode` setting. Citations are tracked
HEAD:backend/onyx/chat/citation_processor.py:572:        know which citations appeared in the text without emitting CitationInfo objects.
HEAD:backend/onyx/chat/citation_processor.py:575:        get_cited_documents() will be empty in those cases, but get_seen_citations()
HEAD:backend/onyx/chat/citation_processor.py:576:        will still contain all the citations that were found.
HEAD:backend/onyx/chat/citation_processor.py:579:            Dictionary mapping citation numbers (int) to SearchDoc objects.
HEAD:backend/onyx/chat/citation_processor.py:580:            The dictionary is keyed by the citation number as it appeared in
HEAD:backend/onyx/chat/citation_processor.py:583:        return self.seen_citations
HEAD:backend/onyx/chat/citation_processor.py:590:        Note: This count is only updated when `citation_mode=HYPERLINK`.
HEAD:backend/onyx/chat/citation_processor.py:592:        Use len(get_seen_citations()) instead if you need to count citations
HEAD:backend/onyx/chat/citation_processor.py:593:        without emitting CitationInfo objects.
HEAD:backend/onyx/chat/citation_processor.py:596:            Number of unique documents cited. 0 if citation_mode is not HYPERLINK.
HEAD:backend/onyx/chat/citation_processor.py:600:    def reset_recent_citations(self) -> None:
HEAD:backend/onyx/chat/citation_processor.py:602:        Reset the recent citations tracker.
HEAD:backend/onyx/chat/citation_processor.py:605:        CitationInfo objects for the same document when it's cited multiple times
HEAD:backend/onyx/chat/citation_processor.py:608:        This is primarily useful when `citation_mode=HYPERLINK` to allow
HEAD:backend/onyx/chat/citation_processor.py:609:        previously cited documents to emit CitationInfo objects again. Has no
HEAD:backend/onyx/chat/citation_processor.py:612:        The recent citation tracker is also automatically cleared when more than
HEAD:backend/onyx/chat/citation_processor.py:613:        5 non-citation characters are processed between citations.
HEAD:backend/onyx/chat/citation_processor.py:617:    def get_next_citation_number(self) -> int:
HEAD:backend/onyx/chat/citation_processor.py:619:        Get the next available citation number for adding new documents to the mapping.
HEAD:backend/onyx/chat/citation_processor.py:621:        This method returns the next citation number that should be used when adding
HEAD:backend/onyx/chat/citation_processor.py:622:        new documents via update_citation_mapping(). Useful when dynamically adding
HEAD:backend/onyx/chat/citation_processor.py:623:        citations during processing (e.g., from tool results like web search).
HEAD:backend/onyx/chat/citation_processor.py:625:        If no citations exist yet in the mapping, returns 1.
HEAD:backend/onyx/chat/citation_processor.py:626:        Otherwise, returns max(existing_citation_numbers) + 1.
HEAD:backend/onyx/chat/citation_processor.py:629:            The next available citation number (1-indexed integer).
HEAD:backend/onyx/chat/citation_processor.py:632:            # After adding citations 1, 2, 3
HEAD:backend/onyx/chat/citation_processor.py:633:            processor.get_next_citation_number()  # Returns 4
HEAD:backend/onyx/chat/citation_processor.py:635:            # With non-sequential citations 1, 5, 10
HEAD:backend/onyx/chat/citation_processor.py:636:            processor.get_next_citation_number()  # Returns 11
HEAD:backend/onyx/chat/citation_processor.py:638:        if not self.citation_to_doc:
HEAD:backend/onyx/chat/citation_processor.py:640:        return max(self.citation_to_doc.keys()) + 1
HEAD:backend/onyx/chat/citation_utils.py:3:from onyx.chat.citation_processor import CitationMapping, DynamicCitationProcessor
HEAD:backend/onyx/chat/citation_utils.py:9:def update_citation_processor_from_tool_response(
HEAD:backend/onyx/chat/citation_utils.py:11:    citation_processor: DynamicCitationProcessor,
HEAD:backend/onyx/chat/citation_utils.py:13:    """Update citation processor if this was a citeable tool with a SearchDocsResponse.
HEAD:backend/onyx/chat/citation_utils.py:16:    then creates a mapping from citation numbers to SearchDoc objects and updates the
HEAD:backend/onyx/chat/citation_utils.py:17:    citation processor.
HEAD:backend/onyx/chat/citation_utils.py:21:        citation_processor: The DynamicCitationProcessor to update
HEAD:backend/onyx/chat/citation_utils.py:27:    # Update citation processor if this was a search tool
HEAD:backend/onyx/chat/citation_utils.py:33:            # Create mapping from citation number to SearchDoc
HEAD:backend/onyx/chat/citation_utils.py:34:            citation_to_doc: CitationMapping = {}
HEAD:backend/onyx/chat/citation_utils.py:36:                citation_num,
HEAD:backend/onyx/chat/citation_utils.py:38:            ) in search_response.citation_mapping.items():
HEAD:backend/onyx/chat/citation_utils.py:43:                        for doc in search_response.search_docs
HEAD:backend/onyx/chat/citation_utils.py:49:                    citation_to_doc[citation_num] = matching_doc
HEAD:backend/onyx/chat/citation_utils.py:51:            # Update the citation processor
HEAD:backend/onyx/chat/citation_utils.py:52:            citation_processor.update_citation_mapping(citation_to_doc)
HEAD:backend/onyx/chat/citation_utils.py:55:def extract_citation_order_from_text(text: str) -> list[int]:
HEAD:backend/onyx/chat/citation_utils.py:56:    """Extract citation numbers from text in order of first appearance.
HEAD:backend/onyx/chat/citation_utils.py:58:    Parses citation patterns like [1], [1, 2], [[1]], 【1】 etc. and returns
HEAD:backend/onyx/chat/citation_utils.py:59:    the citation numbers in the order they first appear in the text.
HEAD:backend/onyx/chat/citation_utils.py:62:        text: The text containing citations
HEAD:backend/onyx/chat/citation_utils.py:65:        List of citation numbers in order of first appearance (no duplicates)
HEAD:backend/onyx/chat/citation_utils.py:67:    # Same pattern used in collapse_citations and DynamicCitationProcessor
HEAD:backend/onyx/chat/citation_utils.py:70:    citation_pattern = re.compile(
HEAD:backend/onyx/chat/citation_utils.py:76:    for match in citation_pattern.finditer(text):
HEAD:backend/onyx/chat/citation_utils.py:99:def collapse_citations(
HEAD:backend/onyx/chat/citation_utils.py:101:    existing_citation_mapping: CitationMapping,
HEAD:backend/onyx/chat/citation_utils.py:102:    new_citation_mapping: CitationMapping,
HEAD:backend/onyx/chat/citation_utils.py:103:) -> tuple[str, CitationMapping]:
HEAD:backend/onyx/chat/citation_utils.py:104:    """Collapse the citations in the text to use the smallest possible numbers.
HEAD:backend/onyx/chat/citation_utils.py:106:    This function takes citations in the text (like [25], [30], etc.) and replaces them
HEAD:backend/onyx/chat/citation_utils.py:108:    integer after the existing citation mapping. If a citation refers to a document
HEAD:backend/onyx/chat/citation_utils.py:109:    that already exists in the existing citation mapping (matched by document_id),
HEAD:backend/onyx/chat/citation_utils.py:110:    it uses the existing citation number instead of assigning a new one.
HEAD:backend/onyx/chat/citation_utils.py:113:        answer_text: The text containing citations to collapse (e.g., "See [25] and [30]")
HEAD:backend/onyx/chat/citation_utils.py:114:        existing_citation_mapping: Citations already processed/displayed. These mappings
HEAD:backend/onyx/chat/citation_utils.py:116:        new_citation_mapping: Citations from the current text that need to be collapsed.
HEAD:backend/onyx/chat/citation_utils.py:117:            The keys are the citation numbers as they appear in answer_text.
HEAD:backend/onyx/chat/citation_utils.py:121:        - updated_text: The text with citations replaced with collapsed numbers
HEAD:backend/onyx/chat/citation_utils.py:122:        - combined_mapping: All values from existing_citation_mapping plus the new
HEAD:backend/onyx/chat/citation_utils.py:125:    # Build a reverse lookup: document_id -> existing citation number
HEAD:backend/onyx/chat/citation_utils.py:126:    doc_id_to_existing_citation: dict[str, int] = {
HEAD:backend/onyx/chat/citation_utils.py:127:        doc.document_id: citation_num
HEAD:backend/onyx/chat/citation_utils.py:128:        for citation_num, doc in existing_citation_mapping.items()
HEAD:backend/onyx/chat/citation_utils.py:131:    # Determine the next available citation number
HEAD:backend/onyx/chat/citation_utils.py:132:    if existing_citation_mapping:
HEAD:backend/onyx/chat/citation_utils.py:133:        next_citation_num = max(existing_citation_mapping.keys()) + 1
HEAD:backend/onyx/chat/citation_utils.py:135:        next_citation_num = 1
HEAD:backend/onyx/chat/citation_utils.py:137:    # Build the mapping from old citation numbers (in new_citation_mapping) to new numbers
HEAD:backend/onyx/chat/citation_utils.py:139:    additional_mappings: CitationMapping = {}
HEAD:backend/onyx/chat/citation_utils.py:141:    for old_num, search_doc in new_citation_mapping.items():
HEAD:backend/onyx/chat/citation_utils.py:144:        # Check if this document already exists in existing citations
HEAD:backend/onyx/chat/citation_utils.py:145:        if doc_id in doc_id_to_existing_citation:
HEAD:backend/onyx/chat/citation_utils.py:146:            # Use the existing citation number
HEAD:backend/onyx/chat/citation_utils.py:147:            old_to_new[old_num] = doc_id_to_existing_citation[doc_id]
HEAD:backend/onyx/chat/citation_utils.py:154:                    mapped_old in new_citation_mapping
HEAD:backend/onyx/chat/citation_utils.py:155:                    and new_citation_mapping[mapped_old].document_id == doc_id
HEAD:backend/onyx/chat/citation_utils.py:164:                old_to_new[old_num] = next_citation_num
HEAD:backend/onyx/chat/citation_utils.py:165:                additional_mappings[next_citation_num] = search_doc
HEAD:backend/onyx/chat/citation_utils.py:166:                next_citation_num += 1
HEAD:backend/onyx/chat/citation_utils.py:168:    # Pattern to match citations like [25], [1, 2, 3], [[25]], etc.
HEAD:backend/onyx/chat/citation_utils.py:170:    citation_pattern = re.compile(
HEAD:backend/onyx/chat/citation_utils.py:174:    def replace_citation(match: re.Match) -> str:
HEAD:backend/onyx/chat/citation_utils.py:175:        """Replace citation numbers in a match with their new collapsed values."""
HEAD:backend/onyx/chat/citation_utils.py:176:        citation_str = match.group()
HEAD:backend/onyx/chat/citation_utils.py:179:        if citation_str.startswith(("[[", "【【", "［［")):
HEAD:backend/onyx/chat/citation_utils.py:180:            open_bracket = citation_str[:2]
HEAD:backend/onyx/chat/citation_utils.py:181:            close_bracket = citation_str[-2:]
HEAD:backend/onyx/chat/citation_utils.py:182:            content = citation_str[2:-2]
HEAD:backend/onyx/chat/citation_utils.py:184:            open_bracket = citation_str[0]
HEAD:backend/onyx/chat/citation_utils.py:185:            close_bracket = citation_str[-1]
HEAD:backend/onyx/chat/citation_utils.py:186:            content = citation_str[1:-1]
HEAD:backend/onyx/chat/citation_utils.py:188:        # Parse and replace citation numbers
HEAD:backend/onyx/chat/citation_utils.py:205:        # Reconstruct the citation with original bracket style
HEAD:backend/onyx/chat/citation_utils.py:209:    # Replace all citations in the text
HEAD:backend/onyx/chat/citation_utils.py:210:    updated_text = citation_pattern.sub(replace_citation, answer_text)
HEAD:backend/onyx/chat/citation_utils.py:213:    combined_mapping: CitationMapping = dict(existing_citation_mapping)
HEAD:backend/onyx/chat/compression.py:329:    # Build system prompt
HEAD:backend/onyx/chat/llm_loop.py:9:    build_python_chat_files_from_search_docs,
HEAD:backend/onyx/chat/llm_loop.py:12:from onyx.chat.citation_processor import (
HEAD:backend/onyx/chat/llm_loop.py:13:    CitationMapping,
HEAD:backend/onyx/chat/llm_loop.py:14:    CitationMode,
HEAD:backend/onyx/chat/llm_loop.py:15:    DynamicCitationProcessor,
HEAD:backend/onyx/chat/llm_loop.py:17:from onyx.chat.citation_utils import update_citation_processor_from_tool_response
HEAD:backend/onyx/chat/llm_loop.py:34:    build_system_prompt,
HEAD:backend/onyx/chat/llm_loop.py:131:    "IMAGE_RECITATION",
HEAD:backend/onyx/chat/llm_loop.py:137:    "RECITATION",
HEAD:backend/onyx/chat/llm_loop.py:316:def _build_context_file_citation_mapping(
HEAD:backend/onyx/chat/llm_loop.py:318:    starting_citation_num: int = 1,
HEAD:backend/onyx/chat/llm_loop.py:319:) -> CitationMapping:
HEAD:backend/onyx/chat/llm_loop.py:320:    """Build citation mapping for context files.
HEAD:backend/onyx/chat/llm_loop.py:323:    Citation numbers start from the provided starting number.
HEAD:backend/onyx/chat/llm_loop.py:327:        starting_citation_num: Starting citation number (default: 1)
HEAD:backend/onyx/chat/llm_loop.py:330:        Dictionary mapping citation numbers to SearchDoc objects
HEAD:backend/onyx/chat/llm_loop.py:332:    citation_mapping: CitationMapping = {}
HEAD:backend/onyx/chat/llm_loop.py:334:    for idx, file_meta in enumerate(file_metadata, start=starting_citation_num):
HEAD:backend/onyx/chat/llm_loop.py:348:        citation_mapping[idx] = search_doc
HEAD:backend/onyx/chat/llm_loop.py:350:    return citation_mapping
HEAD:backend/onyx/chat/llm_loop.py:707:    message_content = f"Here are some documents provided for context, they may not all be relevant:\n{documents_json}"
HEAD:backend/onyx/chat/llm_loop.py:724:    include_citation_reminder: bool,
HEAD:backend/onyx/chat/llm_loop.py:739:        include_citation_reminder=include_citation_reminder,
HEAD:backend/onyx/chat/llm_loop.py:761:    include_citations: bool = True,
HEAD:backend/onyx/chat/llm_loop.py:788:        # Initialize citation processor for handling citations dynamically
HEAD:backend/onyx/chat/llm_loop.py:789:        # When include_citations is True, use HYPERLINK mode to format citations as [[1]](url)
HEAD:backend/onyx/chat/llm_loop.py:790:        # When include_citations is False, use REMOVE mode to strip citations from output
HEAD:backend/onyx/chat/llm_loop.py:791:        citation_processor = DynamicCitationProcessor(
HEAD:backend/onyx/chat/llm_loop.py:792:            citation_mode=(
HEAD:backend/onyx/chat/llm_loop.py:793:                CitationMode.HYPERLINK if include_citations else CitationMode.REMOVE
HEAD:backend/onyx/chat/llm_loop.py:797:        # Add project file citation mappings if project files are present
HEAD:backend/onyx/chat/llm_loop.py:798:        project_citation_mapping: CitationMapping = {}
HEAD:backend/onyx/chat/llm_loop.py:800:            project_citation_mapping = _build_context_file_citation_mapping(
HEAD:backend/onyx/chat/llm_loop.py:803:            citation_processor.update_citation_mapping(project_citation_mapping)
HEAD:backend/onyx/chat/llm_loop.py:827:            list(project_citation_mapping.values())
HEAD:backend/onyx/chat/llm_loop.py:828:            if project_citation_mapping
HEAD:backend/onyx/chat/llm_loop.py:832:        # One future workaround is to include the images as separate user messages with citation information and process those.
HEAD:backend/onyx/chat/llm_loop.py:843:        citation_mapping: dict[int, str] = {}  # Maps citation_num -> document_id/URL
HEAD:backend/onyx/chat/llm_loop.py:938:                    system_prompt_str = build_system_prompt(
HEAD:backend/onyx/chat/llm_loop.py:1008:                include_citation_reminder=should_cite_documents
HEAD:backend/onyx/chat/llm_loop.py:1063:                citation_processor=citation_processor,
HEAD:backend/onyx/chat/llm_loop.py:1090:            # Save citation mapping after each LLM step for incremental state updates
HEAD:backend/onyx/chat/llm_loop.py:1091:            state_container.set_citation_mapping(citation_processor.citation_to_doc)
HEAD:backend/onyx/chat/llm_loop.py:1121:            # Quick note for why citation_mapping and citation_processors are both needed:
HEAD:backend/onyx/chat/llm_loop.py:1124:            # 3. The citation_processor operates on SearchDoc objects and can't provide a complete reverse URL lookup for
HEAD:backend/onyx/chat/llm_loop.py:1125:            # in-flight citations
HEAD:backend/onyx/chat/llm_loop.py:1134:                citation_mapping=citation_mapping,
HEAD:backend/onyx/chat/llm_loop.py:1135:                next_citation_num=citation_processor.get_next_citation_number(),
HEAD:backend/onyx/chat/llm_loop.py:1143:            citation_mapping = parallel_tool_call_results.updated_citation_mapping
HEAD:backend/onyx/chat/llm_loop.py:1188:                # Extract search_docs if this is a search tool response
HEAD:backend/onyx/chat/llm_loop.py:1189:                search_docs = None
HEAD:backend/onyx/chat/llm_loop.py:1192:                    search_docs = tool_response.rich_response.search_docs
HEAD:backend/onyx/chat/llm_loop.py:1196:                    if search_docs:
HEAD:backend/onyx/chat/llm_loop.py:1197:                        state_container.add_search_docs(search_docs)
HEAD:backend/onyx/chat/llm_loop.py:1200:                        gathered_documents.extend(search_docs)
HEAD:backend/onyx/chat/llm_loop.py:1202:                        gathered_documents = search_docs
HEAD:backend/onyx/chat/llm_loop.py:1206:                    if search_docs and tool_call.tool_name == WebSearchTool.NAME:
HEAD:backend/onyx/chat/llm_loop.py:1212:                    if search_docs:
HEAD:backend/onyx/chat/llm_loop.py:1213:                        staged = build_python_chat_files_from_search_docs(
HEAD:backend/onyx/chat/llm_loop.py:1214:                            search_docs=search_docs,
HEAD:backend/onyx/chat/llm_loop.py:1312:                    search_docs=displayed_docs or search_docs,
HEAD:backend/onyx/chat/llm_loop.py:1320:                # Update citation processor if this was a search tool
HEAD:backend/onyx/chat/llm_loop.py:1321:                update_citation_processor_from_tool_response(
HEAD:backend/onyx/chat/llm_loop.py:1322:                    tool_response, citation_processor
HEAD:backend/onyx/chat/llm_step.py:10:from onyx.chat.citation_processor import DynamicCitationProcessor
HEAD:backend/onyx/chat/llm_step.py:58:    CitationInfo,
HEAD:backend/onyx/chat/llm_step.py:1081:    citation_processor: DynamicCitationProcessor | None,
HEAD:backend/onyx/chat/llm_step.py:1100:    answer content, tool calls, and citations. It yields Packet objects for
HEAD:backend/onyx/chat/llm_step.py:1111:        citation_processor: Optional processor for extracting and formatting citations
HEAD:backend/onyx/chat/llm_step.py:1112:            from the response. If provided, processes tokens to identify citations.
HEAD:backend/onyx/chat/llm_step.py:1134:            - CitationInfo for extracted citations
HEAD:backend/onyx/chat/llm_step.py:1202:        def _emit_citation_results(
HEAD:backend/onyx/chat/llm_step.py:1203:            results: Generator[str | CitationInfo, None, None],
HEAD:backend/onyx/chat/llm_step.py:1205:            """Yield packets for citation processor results (str or CitationInfo)."""
HEAD:backend/onyx/chat/llm_step.py:1217:                elif isinstance(result, CitationInfo):
HEAD:backend/onyx/chat/llm_step.py:1223:                        state_container.add_emitted_citation(result.citation_number)
HEAD:backend/onyx/chat/llm_step.py:1293:            if citation_processor:
HEAD:backend/onyx/chat/llm_step.py:1294:                yield from _emit_citation_results(
HEAD:backend/onyx/chat/llm_step.py:1295:                    citation_processor.process_token(content_chunk)
HEAD:backend/onyx/chat/llm_step.py:1446:        # Flush any remaining content from citation processor
HEAD:backend/onyx/chat/llm_step.py:1448:        # Note that this doesn't need to handle any sub-turns as those docs will not have citations
HEAD:backend/onyx/chat/llm_step.py:1450:        if citation_processor:
HEAD:backend/onyx/chat/llm_step.py:1451:            yield from _emit_citation_results(citation_processor.process_token(None))
HEAD:backend/onyx/chat/llm_step.py:1453:        # Empty-answer recovery: the model emitted text but content/citation
HEAD:backend/onyx/chat/llm_step.py:1455:        # like "[123456789012345]" that the citation processor strips). Surface the
HEAD:backend/onyx/chat/llm_step.py:1470:                "Answer empty after content/citation processing; recovering raw "
HEAD:backend/onyx/chat/llm_step.py:1583:    citation_processor: DynamicCitationProcessor | None,
HEAD:backend/onyx/chat/llm_step.py:1608:        citation_processor=citation_processor,
HEAD:backend/onyx/chat/models.py:15:    CitationInfo,
HEAD:backend/onyx/chat/models.py:62:    search_docs: list[SearchDoc] | None = None
HEAD:backend/onyx/chat/models.py:71:    answer_citationless: str
HEAD:backend/onyx/chat/models.py:77:    citation_info: list[CitationInfo]
HEAD:backend/onyx/chat/models.py:88:    answer_citationless: str
HEAD:backend/onyx/chat/models.py:92:    # Documents & citations
HEAD:backend/onyx/chat/models.py:94:    citation_info: list[CitationInfo]
HEAD:backend/onyx/chat/models.py:185:    """Metadata for a context-injected file to enable citation support."""
HEAD:backend/onyx/chat/process_message.py:136:    CitationInfo,
HEAD:backend/onyx/chat/process_message.py:1174:            accumulated state (tool calls, answer tokens, citations) after the stream
HEAD:backend/onyx/chat/process_message.py:1185:        answer tokens, tool output, citations — followed by a terminal ``Packet``
HEAD:backend/onyx/chat/process_message.py:1413:                    include_citations=setup.new_msg_req.include_citations,
HEAD:backend/onyx/chat/process_message.py:1680:            provided, accumulated state (tool calls, citations, answer tokens) is
HEAD:backend/onyx/chat/process_message.py:1684:        Generator yielding ``Packet`` objects — answer tokens, tool output, citations —
HEAD:backend/onyx/chat/process_message.py:1993:    citation_to_doc = state_container.get_citation_to_doc()
HEAD:backend/onyx/chat/process_message.py:1996:    all_search_docs = state_container.get_all_search_docs()
HEAD:backend/onyx/chat/process_message.py:1997:    emitted_citations = state_container.get_emitted_citations()
HEAD:backend/onyx/chat/process_message.py:2040:            citation_to_doc=citation_to_doc,
HEAD:backend/onyx/chat/process_message.py:2042:            all_search_docs=all_search_docs,
HEAD:backend/onyx/chat/process_message.py:2046:            emitted_citations=emitted_citations,
HEAD:backend/onyx/chat/process_message.py:2100:_CITATION_LINK_START_PATTERN = re.compile(r"\s*\[\[\d+\]\]\(")
HEAD:backend/onyx/chat/process_message.py:2125:def remove_answer_citations(answer: str) -> str:
HEAD:backend/onyx/chat/process_message.py:2129:    while match := _CITATION_LINK_START_PATTERN.search(answer, cursor):
HEAD:backend/onyx/chat/process_message.py:2147:    citations: list[CitationInfo] = []
HEAD:backend/onyx/chat/process_message.py:2165:            elif isinstance(packet.obj, CitationInfo):
HEAD:backend/onyx/chat/process_message.py:2166:                # CitationInfo contains citation information
HEAD:backend/onyx/chat/process_message.py:2167:                citations.append(packet.obj)
HEAD:backend/onyx/chat/process_message.py:2185:        answer_citationless=remove_answer_citations(answer),
HEAD:backend/onyx/chat/process_message.py:2186:        citation_info=citations,
HEAD:backend/onyx/chat/process_message.py:2203:    including answer, reasoning, citations, and tool calls.
HEAD:backend/onyx/chat/process_message.py:2213:    citations: list[CitationInfo] = []
HEAD:backend/onyx/chat/process_message.py:2230:            elif isinstance(packet.obj, CitationInfo):
HEAD:backend/onyx/chat/process_message.py:2231:                citations.append(packet.obj)
HEAD:backend/onyx/chat/process_message.py:2255:            search_docs=tc.search_docs,
HEAD:backend/onyx/chat/process_message.py:2264:        answer_citationless=remove_answer_citations(final_answer),
HEAD:backend/onyx/chat/process_message.py:2268:        citation_info=citations,
HEAD:backend/onyx/chat/prompt_utils.py:12:    CITATION_REMINDER,
HEAD:backend/onyx/chat/prompt_utils.py:15:    LAST_CYCLE_CITATION_REMINDER,
HEAD:backend/onyx/chat/prompt_utils.py:16:    REQUIRE_CITATION_GUIDANCE,
HEAD:backend/onyx/chat/prompt_utils.py:90:    fake_system_prompt = build_system_prompt(
HEAD:backend/onyx/chat/prompt_utils.py:132:    include_citation_reminder: bool,
HEAD:backend/onyx/chat/prompt_utils.py:138:        reminder += "\n\n" + LAST_CYCLE_CITATION_REMINDER
HEAD:backend/onyx/chat/prompt_utils.py:139:    if include_citation_reminder:
HEAD:backend/onyx/chat/prompt_utils.py:140:        reminder += "\n\n" + CITATION_REMINDER
HEAD:backend/onyx/chat/prompt_utils.py:160:        append_citation_if_missing=False,
HEAD:backend/onyx/chat/prompt_utils.py:176:    """Deep research builds its own system prompts, so the reply-language line that
HEAD:backend/onyx/chat/prompt_utils.py:177:    build_system_prompt adds for chat is appended to the user-facing ones here."""
HEAD:backend/onyx/chat/prompt_utils.py:250:def build_system_prompt(
HEAD:backend/onyx/chat/prompt_utils.py:261:    system_prompt, should_append_citation_guidance = apply_prompt_placeholders(
HEAD:backend/onyx/chat/prompt_utils.py:267:        append_citation_if_missing=True,
HEAD:backend/onyx/chat/prompt_utils.py:276:    # Append citation guidance after company context if placeholder was not present
HEAD:backend/onyx/chat/prompt_utils.py:277:    # This maintains backward compatibility and ensures citations are always enforced when needed
HEAD:backend/onyx/chat/prompt_utils.py:278:    if should_append_citation_guidance:
HEAD:backend/onyx/chat/prompt_utils.py:279:        system_prompt += REQUIRE_CITATION_GUIDANCE
HEAD:backend/onyx/chat/save_chat.py:11:    add_search_docs_to_chat_message,
HEAD:backend/onyx/chat/save_chat.py:12:    add_search_docs_to_tool_call,
HEAD:backend/onyx/chat/save_chat.py:162:            add_search_docs_to_tool_call(
HEAD:backend/onyx/chat/save_chat.py:173:    citation_to_doc: dict[int, SearchDoc],
HEAD:backend/onyx/chat/save_chat.py:174:    all_search_docs: dict[SearchDocKey, SearchDoc],
HEAD:backend/onyx/chat/save_chat.py:178:    emitted_citations: set[int] | None = None,
HEAD:backend/onyx/chat/save_chat.py:188:    2. Creates DB SearchDoc entries from pre-deduplicated all_search_docs
HEAD:backend/onyx/chat/save_chat.py:190:    4. Builds citation mapping from citation_to_doc
HEAD:backend/onyx/chat/save_chat.py:193:    7. Builds the citations mapping for the ChatMessage
HEAD:backend/onyx/chat/save_chat.py:198:        tool_calls: List of tool call information to create ToolCall entries (may include search_docs)
HEAD:backend/onyx/chat/save_chat.py:199:        citation_to_doc: Mapping from citation number to SearchDoc for building citations
HEAD:backend/onyx/chat/save_chat.py:200:        all_search_docs: Pre-deduplicated search docs from ChatStateContainer
HEAD:backend/onyx/chat/save_chat.py:204:        emitted_citations: Set of citation numbers that were actually emitted during streaming.
HEAD:backend/onyx/chat/save_chat.py:205:            If provided, only citations in this set will be saved; others are filtered out.
HEAD:backend/onyx/chat/save_chat.py:223:        citation_to_doc = {}
HEAD:backend/onyx/chat/save_chat.py:224:        all_search_docs = {}
HEAD:backend/onyx/chat/save_chat.py:225:        emitted_citations = set()
HEAD:backend/onyx/chat/save_chat.py:244:    # 2. Create DB SearchDoc entries from pre-deduplicated all_search_docs
HEAD:backend/onyx/chat/save_chat.py:246:    for key, search_doc_py in all_search_docs.items():
HEAD:backend/onyx/chat/save_chat.py:257:        if tool_call_info.search_docs:
HEAD:backend/onyx/chat/save_chat.py:259:            for search_doc_py in tool_call_info.search_docs:
HEAD:backend/onyx/chat/save_chat.py:264:                    # Displayed doc not in all_search_docs - create it
HEAD:backend/onyx/chat/save_chat.py:265:                    # This can happen if displayed_docs contains docs not in search_docs
HEAD:backend/onyx/chat/save_chat.py:280:    # 4. Build a citation mapping from the citation number to the saved DB SearchDoc ID
HEAD:backend/onyx/chat/save_chat.py:281:    # Only include citations that were actually emitted during streaming
HEAD:backend/onyx/chat/save_chat.py:282:    citation_number_to_search_doc_id: dict[int, int] = {}
HEAD:backend/onyx/chat/save_chat.py:284:    for citation_num, search_doc_py in citation_to_doc.items():
HEAD:backend/onyx/chat/save_chat.py:285:        # Skip citations that weren't actually emitted (if emitted_citations is provided)
HEAD:backend/onyx/chat/save_chat.py:286:        if emitted_citations is not None and citation_num not in emitted_citations:
HEAD:backend/onyx/chat/save_chat.py:296:            # Citation doc not found in tool call search_docs
HEAD:backend/onyx/chat/save_chat.py:298:            # Unexpected case: Other citation-only docs (indicates a potential issue upstream)
HEAD:backend/onyx/chat/save_chat.py:303:                    "Project file citation %s not in tool calls, creating it",
HEAD:backend/onyx/chat/save_chat.py:308:                    "Citation doc %s not found in tool call search_docs, creating it",
HEAD:backend/onyx/chat/save_chat.py:328:        # Build mapping from citation number to search doc ID
HEAD:backend/onyx/chat/save_chat.py:329:        citation_number_to_search_doc_id[citation_num] = db_search_doc_id
HEAD:backend/onyx/chat/save_chat.py:331:    # 5. Link all unique SearchDocs (from both tool calls and citations) to ChatMessage
HEAD:backend/onyx/chat/save_chat.py:334:        add_search_docs_to_chat_message(
HEAD:backend/onyx/chat/save_chat.py:349:    # 7. Build citations mapping - use the mapping we already built in step 4
HEAD:backend/onyx/chat/save_chat.py:350:    assistant_message.citations = (
HEAD:backend/onyx/chat/save_chat.py:351:        citation_number_to_search_doc_id if citation_number_to_search_doc_id else None
HEAD:backend/onyx/configs/agent_configs.py:57:AGENT_MAX_ANSWER_CONTEXT_DOCS = int(
HEAD:backend/onyx/configs/agent_configs.py:58:    os.environ.get("AGENT_MAX_ANSWER_CONTEXT_DOCS")
HEAD:backend/onyx/configs/kg_configs.py:3:KG_RESEARCH_NUM_RETRIEVED_DOCS: int = int(
HEAD:backend/onyx/configs/kg_configs.py:4:    os.environ.get("KG_RESEARCH_NUM_RETRIEVED_DOCS", "25")
HEAD:backend/onyx/connectors/blob/connector.py:222:            # This is important for correct citation links
HEAD:backend/onyx/connectors/braintrust/connector.py:305:    def _prompt_to_document(
HEAD:backend/onyx/connectors/braintrust/connector.py:559:                    yield self._prompt_to_document(prompt, ref.project_name or "")
HEAD:backend/onyx/connectors/file/connector.py:191:    # `build_python_chat_files_from_search_docs`, which has no tabular
HEAD:backend/onyx/connectors/file/connector.py:197:    # tabular check to `build_python_chat_files_from_search_docs` (keyed
HEAD:backend/onyx/context/search/models.py:344:        search_docs = [
HEAD:backend/onyx/context/search/models.py:372:        return search_docs  # ty: ignore[invalid-return-type]
HEAD:backend/onyx/context/search/models.py:384:    def from_saved_search_docs(
HEAD:backend/onyx/context/search/models.py:385:        cls, saved_search_docs: list["SavedSearchDoc"]
```
This is a major AI-product security boundary.
Retrieved content changes from stored application data into model-visible
context at this point.
## LLM Handoff Candidates
Evidence lines: 550
```text
HEAD:backend/ee/onyx/server/query_and_chat/models.py:34:    num_docs_fed_to_llm_selection: int | None = None
HEAD:backend/ee/onyx/server/query_and_chat/models.py:93:    # Reasoning tokens output by the LLM for the document selection
HEAD:backend/ee/onyx/server/query_and_chat/models.py:96:    llm_selected_doc_ids: list[str] | None = None
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:4:directly with optional LLM query expansion and document selection.  Supports
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:23:from ee.onyx.secondary_llm_flows.search_flow_classification import (
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:41:from onyx.llm.factory import get_default_llm
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:42:from onyx.server.usage_limits import check_llm_cost_limit_for_provider
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:63:    LLM call. A failed classification falls back to ``is_search_flow: false``
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:72:    llm = get_default_llm()
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:74:    check_llm_cost_limit_for_provider(
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:77:        llm_provider_api_key=llm.config.api_key,
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:81:        is_search_flow = classify_is_search_flow(query=query, llm=llm)
HEAD:backend/ee/onyx/server/query_and_chat/streaming_models.py:29:class LLMSelectedDocsPacket(BaseModel):
HEAD:backend/ee/onyx/server/query_and_chat/streaming_models.py:32:    type: Literal["llm_selected_docs"] = "llm_selected_docs"
HEAD:backend/ee/onyx/server/query_and_chat/streaming_models.py:33:    # None if LLM selection failed, empty list if no docs selected, list of IDs otherwise
HEAD:backend/ee/onyx/server/query_and_chat/streaming_models.py:34:    llm_selected_doc_ids: list[str] | None
HEAD:backend/onyx/chat/COMPRESSION.md:3:Compresses long chat histories by summarizing older messages while keeping recent ones verbatim.
HEAD:backend/onyx/chat/COMPRESSION.md:10:- `last_summarized_message_id` → pointer to an older message up the chain (the cutoff). Messages after this are kept verbatim.
HEAD:backend/onyx/chat/COMPRESSION.md:12:**Why store summary as a separate message?** If we embedded the summary in the `last_summarized_message_id` message itself, that message would contain context from messages that came after it—context that doesn't exist in other branches. By creating the summary as a new message attached to the branch tip, it only applies to the specific branch where compression occurred. It's only back-pointed to by the
HEAD:backend/onyx/chat/COMPRESSION.md:13:branch which it applies to. All of this is necessary because we keep the last few messages verbatim and also to support branching logic.
HEAD:backend/onyx/chat/COMPRESSION.md:16:Subsequent compressions incorporate the existing summary text + new messages, preventing information loss in very long conversations.
HEAD:backend/onyx/chat/COMPRESSION.md:18:### Cutoff Marker Prompt Strategy
HEAD:backend/onyx/chat/COMPRESSION.md:19:The LLM receives older messages, a cutoff marker, then recent messages. It summarizes only content before the marker while using recent context to inform what's important.
HEAD:backend/onyx/chat/COMPRESSION.md:24:- `max_context_tokens` — LLM's total context window
HEAD:backend/onyx/chat/COMPRESSION.md:25:- `reserved_tokens` — space for system prompt, tools, files, etc.
HEAD:backend/onyx/chat/COMPRESSION.md:31:- `RECENT_MESSAGES_RATIO` (default 0.2) — portion of chat history to keep verbatim when compressing
HEAD:backend/onyx/chat/COMPRESSION.md:37:3. Split messages: older (summarize) / recent (keep 25%)
HEAD:backend/onyx/chat/COMPRESSION.md:38:4. Generate summary via LLM
HEAD:backend/onyx/chat/COMPRESSION.md:47:| `get_messages_to_summarize` | Split messages at token budget boundary |
HEAD:backend/onyx/chat/README.md:8:## System Prompt
HEAD:backend/onyx/chat/README.md:10:The system prompt is a default prompt that comes packaged with the system. Users can edit the default prompt and it will be persisted in the database.
HEAD:backend/onyx/chat/README.md:12:Some parts of the system prompt are dynamically updated / inserted:
HEAD:backend/onyx/chat/README.md:18:## Custom Agent Prompt
HEAD:backend/onyx/chat/README.md:20:The custom agent is inserted as a user message above the most recent user message, it is dynamically moved in the history as the user sends more messages.
HEAD:backend/onyx/chat/README.md:21:If the user has opted to completely replace the System Prompt, then this Custom Agent prompt replaces the system prompt and does not move along the history.
HEAD:backend/onyx/chat/README.md:25:On upload, Files are processed for tokens, if too many tokens to fit in the context, it’s considered a failed inclusion. This is done using the LLM tokenizer.
HEAD:backend/onyx/chat/README.md:27:- In many cases, there is not a known tokenizer for each LLM so there is a default tokenizer used as a catchall.
HEAD:backend/onyx/chat/README.md:32:Image files are attached to User Messages also as point in time inclusions.
HEAD:backend/onyx/chat/README.md:40:If a Project contains few enough files that it all fits in the model context, we keep it close enough in the history to ensure it is easy for the LLM to
HEAD:backend/onyx/chat/README.md:42:a haystack type search with a strong keyword to make the LLM attend to it.
HEAD:backend/onyx/chat/README.md:49:Documents from search or uploaded Project files are represented as a json so that the LLM can easily understand it. It is represented with a prefix string to
HEAD:backend/onyx/chat/README.md:50:make the context clearer to the LLM. Note that for search results (whether web or internal, it will just be the json) and it will be a Tool Call type of
HEAD:backend/onyx/chat/README.md:63:Documents are represented with the `document` key so that the LLM can easily cite them with a single number. The tool returns have to be richer to be able to
HEAD:backend/onyx/chat/README.md:64:translate this into links and other UI elements. What the LLM sees is far simpler to reduce noise/hallucinations.
HEAD:backend/onyx/chat/README.md:68:Search tools also give URLs to the LLM so that open_url (a separate tool) can be called on them.
HEAD:backend/onyx/chat/README.md:72:To ensure the LLM follows certain specific instructions, instructions are added at the very end of the chat context as a user message. If a search related
HEAD:backend/onyx/chat/README.md:84:> Note: in the Internal Search flow with query expansion, the Tool Call which was actually run differs from what the LLM provided as arguments.
HEAD:backend/onyx/chat/README.md:85:> What the LLM sees in the history (to be most informative for future calls) is the full set of expanded queries.
HEAD:backend/onyx/chat/README.md:88:Instead of dropping the Tool Call response, we might summarize it using an LLM so that it is just 1-2 sentences and captures the main points. That said,
HEAD:backend/onyx/chat/README.md:113:- Project files move along the chain as new messages are sent
HEAD:backend/onyx/chat/README.md:114:- Custom Agent prompt comes before project files which come before user uploaded files in each turn
HEAD:backend/onyx/chat/README.md:124:those files. The LLM is much better at referencing documents close to the end of the context window so keeping it there for ease of access.
HEAD:backend/onyx/chat/README.md:130:Reminder are absolutely necessary to ensure 1-2 specific instructions get followed with a very high probability. It is less detailed than the system prompt
HEAD:backend/onyx/chat/README.md:135:Custom Agent instructions being placed in the system prompt is poorly followed. It also degrades performance of the system especially when the instructions
HEAD:backend/onyx/chat/README.md:136:are orthogonal (or even possibly contradictory) to the system prompt. For weaker models, it causes strange artifacts in tool calls and final responses
HEAD:backend/onyx/chat/README.md:140:Different LLMs vary in this but some now have a section that cannot be set via the API layer called the "System Prompt" (OpenAI terminology) which contains
HEAD:backend/onyx/chat/README.md:141:information like the model cutoff date, identity, and some other basic non-changing information. The System prompt described above is in that convention called
HEAD:backend/onyx/chat/README.md:142:the "Developer Prompt". It seems the distribution of the System Prompt, by which I mean the style of wording and terms used can also affect the behavior. This
HEAD:backend/onyx/chat/README.md:143:is different between different models and not necessarily scientific so the system prompt is built from an exploration across different models. It currently
HEAD:backend/onyx/chat/README.md:146:LLMs are able to handle changes in topic best at message boundaries. There are special tokens under the hood for this. We also use this property to slice up
HEAD:backend/onyx/chat/README.md:149:Reminder messages are placed at the end of the prompt because all model fine tuning approaches cause the LLMs to attend very strongly to the tokens at the very
HEAD:backend/onyx/chat/README.md:150:back of the context closest to generation. This is the only way to get the LLMs to not miss critical information and for the product to be reliable. Specifically
HEAD:backend/onyx/chat/README.md:153:The document json includes a field for the LLM to cite (it's a single number) to make citations reliable and avoid weird artifacts. It's called "document" so
HEAD:backend/onyx/chat/README.md:154:that the LLM does not create weird artifacts in reasoning like "I should reference citation_id: 5 for...". It is also strategically placed so that it is easy to
HEAD:backend/onyx/chat/README.md:155:reference. It is followed by a couple short sections like the metadata and title before the long content section. It seems LLMs are still better at local
HEAD:backend/onyx/chat/README.md:158:In a similar concept, LLM instructions in the system prompt are structured specifically so that there are coherent sections for the LLM to attend to. This is
HEAD:backend/onyx/chat/README.md:160:need to call additional tools, you are encouraged to do this", having this in the Tool section of the System prompt makes all the LLMs follow it well but if it's
HEAD:backend/onyx/chat/README.md:161:even just a paragraph away like near the beginning of the prompt, it is often ignored. The difference is as drastic as a 30% follow rate to a 90% follow
HEAD:backend/onyx/chat/README.md:166:- How messages, files, images are stored can be found in backend/onyx/db/models.py, there is also a README.md under that directory that may be helpful.
HEAD:backend/onyx/chat/README.md:170:# Overview of LLM flow architecture
HEAD:backend/onyx/chat/README.md:174:Step/Cycle: 1 single LLM inference given some context and some tools
HEAD:backend/onyx/chat/README.md:179:messages in the session and sets up all the necessary items to run the chat loop and state containers. The major things it does
HEAD:backend/onyx/chat/README.md:185:- Prepares all of the tools for the LLM
HEAD:backend/onyx/chat/README.md:192:means the top level is isolated from the LLM flow and can yield packets as soon as they are produced. If a
HEAD:backend/onyx/chat/README.md:195:workers themselves via self-completion if the drain loop exits early).
HEAD:backend/onyx/chat/README.md:208:The state container is used to accumulate state during the LLM flow. Similar to the emitter, it should not be used for logic,
HEAD:backend/onyx/chat/README.md:221:reaching the normal completion path.
HEAD:backend/onyx/chat/README.md:223:## 2. LLM Loop (run_llm_loop function)
HEAD:backend/onyx/chat/README.md:228:- Translate and truncate the context for the LLM inference
HEAD:backend/onyx/chat/README.md:229:- Add context modifiers like reminders, updates to the system prompts, etc.
HEAD:backend/onyx/chat/README.md:233:## 3. LLM Step (run_llm_step function)
HEAD:backend/onyx/chat/README.md:235:This function is a single inference of the LLM. It's a wrapper around the LLM stream function which handles packet translations
HEAD:backend/onyx/chat/README.md:238:tool calls and returns that to the LLM Loop to execute.
HEAD:backend/onyx/chat/README.md:244:  comes from the same LLM inference (same backend LLM step), they are 2 turns to the frontend because that's how it's rendered.
HEAD:backend/onyx/chat/README.md:247:  1. **ChatMessage** — The database model. Should be converted into ChatMessageSimple early and never passed deep into the flow.
HEAD:backend/onyx/chat/README.md:248:  2. **ChatMessageSimple** — The canonical data model used throughout the codebase. This is the rich, full-featured representation
HEAD:backend/onyx/chat/README.md:250:  3. **LanguageModelInput** — The LLM-facing representation. Intentionally minimal so the LLM interface layer stays clean and
HEAD:backend/onyx/chat/chat_processing_checker.py:14:    """Generate the cache key for a chat session processing fence.
HEAD:backend/onyx/chat/chat_state.py:13:    ChatMessageSimple,
HEAD:backend/onyx/chat/chat_state.py:22:from onyx.llm.interfaces import LLM, LLMUserIdentity
HEAD:backend/onyx/chat/chat_state.py:23:from onyx.llm.models import ReasoningEffort
HEAD:backend/onyx/chat/chat_state.py:35:    """Container for accumulating state during LLM loop execution.
HEAD:backend/onyx/chat/chat_state.py:61:        # Note: LLM cost tracking is now handled in multi_llm.py
HEAD:backend/onyx/chat/chat_state.py:201:    (``persona``, ``reserved_messages``) are detached after ``build_chat_turn``
HEAD:backend/onyx/chat/chat_state.py:218:    user_identity: LLMUserIdentity
HEAD:backend/onyx/chat/chat_state.py:219:    llms: list[LLM]  # length 1 for single-model, N for multi-model
HEAD:backend/onyx/chat/chat_state.py:220:    model_display_names: list[str]  # parallel to llms
HEAD:backend/onyx/chat/chat_state.py:221:    simple_chat_history: list[ChatMessageSimple]
HEAD:backend/onyx/chat/chat_state.py:223:    reserved_messages: list[ChatMessage]  # length 1 for single, N for multi
HEAD:backend/onyx/chat/chat_state.py:235:    custom_agent_prompt: str | None
HEAD:backend/onyx/chat/chat_utils.py:19:    ChatMessageSimple,
HEAD:backend/onyx/chat/chat_utils.py:33:    get_chat_messages_by_session,
HEAD:backend/onyx/chat/chat_utils.py:61:from onyx.prompts.chat_prompts import (
HEAD:backend/onyx/chat/chat_utils.py:62:    ADDITIONAL_CONTEXT_PROMPT,
HEAD:backend/onyx/chat/chat_utils.py:65:from onyx.prompts.tool_prompts import TOOL_CALL_FAILURE_PROMPT
HEAD:backend/onyx/chat/chat_utils.py:74:IMAGE_GENERATION_TOOL_NAME = "generate_image"
HEAD:backend/onyx/chat/chat_utils.py:78:    """Result of building a file's LLM context representation."""
HEAD:backend/onyx/chat/chat_utils.py:80:    message: ChatMessageSimple
HEAD:backend/onyx/chat/chat_utils.py:107:    """Build the LLM context representation for a single file.
HEAD:backend/onyx/chat/chat_utils.py:109:    Centralises how files should appear in the LLM prompt
HEAD:backend/onyx/chat/chat_utils.py:118:        message = ChatMessageSimple(
HEAD:backend/onyx/chat/chat_utils.py:132:        message = ChatMessageSimple(
HEAD:backend/onyx/chat/chat_utils.py:140:        message = ChatMessageSimple(
HEAD:backend/onyx/chat/chat_utils.py:249:    """Build the linear chain of messages without including the root message"""
HEAD:backend/onyx/chat/chat_utils.py:250:    mainline_messages: list[ChatMessage] = []
HEAD:backend/onyx/chat/chat_utils.py:252:    all_chat_messages = get_chat_messages_by_session(
HEAD:backend/onyx/chat/chat_utils.py:261:    if not all_chat_messages:
HEAD:backend/onyx/chat/chat_utils.py:266:        root_message = all_chat_messages[0]
HEAD:backend/onyx/chat/chat_utils.py:289:            and mainline_messages
HEAD:backend/onyx/chat/chat_utils.py:291:            # Note that 2 user messages in a row is fine since this is often used for
HEAD:backend/onyx/chat/chat_utils.py:292:            # adding custom prompts and reminders
HEAD:backend/onyx/chat/chat_utils.py:294:                "Invalid message chain, cannot have two assistant messages in a row"
HEAD:backend/onyx/chat/chat_utils.py:297:            mainline_messages.append(current_message)
HEAD:backend/onyx/chat/chat_utils.py:301:    return mainline_messages
HEAD:backend/onyx/chat/chat_utils.py:497:    ``content_text`` (used for LLM context injection) and ``token_count``
HEAD:backend/onyx/chat/chat_utils.py:530:            # Only invoked on cache miss; bytes-read happens here, not upfront.
HEAD:backend/onyx/chat/chat_utils.py:540:        # file store id (covers code-interpreter-generated files, etc.).
HEAD:backend/onyx/chat/chat_utils.py:558:        # Chat messages keep file references in their JSONB `files` column, but
HEAD:backend/onyx/chat/chat_utils.py:561:        # lazily (on first `.content` access, often mid-LLM-flow), a raised
HEAD:backend/onyx/chat/chat_utils.py:599:    chat_messages: list[ChatMessage],
HEAD:backend/onyx/chat/chat_utils.py:607:    for chat_message in chat_messages:
HEAD:backend/onyx/chat/chat_utils.py:629:) -> list[ChatMessageSimple]:
HEAD:backend/onyx/chat/chat_utils.py:630:    """Convert ChatMessage history to ChatMessageSimple format with no tool calls or files included.
HEAD:backend/onyx/chat/chat_utils.py:635:        max_individual_message_tokens: If set, messages exceeding this number of tokens are dropped.
HEAD:backend/onyx/chat/chat_utils.py:636:            If None, no messages are dropped based on individual token count.
HEAD:backend/onyx/chat/chat_utils.py:641:        List of ChatMessageSimple objects
HEAD:backend/onyx/chat/chat_utils.py:647:    # Convert only the core USER/ASSISTANT messages; omit files and tool calls.
HEAD:backend/onyx/chat/chat_utils.py:648:    converted: list[ChatMessageSimple] = []
HEAD:backend/onyx/chat/chat_utils.py:666:            ChatMessageSimple(
HEAD:backend/onyx/chat/chat_utils.py:678:    trimmed_reversed: list[ChatMessageSimple] = []
HEAD:backend/onyx/chat/chat_utils.py:691:    generated_images: list[dict] | None,
HEAD:backend/onyx/chat/chat_utils.py:697:    if generated_images:
HEAD:backend/onyx/chat/chat_utils.py:698:        llm_image_context: list[dict[str, str]] = []
HEAD:backend/onyx/chat/chat_utils.py:699:        for image in generated_images:
HEAD:backend/onyx/chat/chat_utils.py:701:            revised_prompt = image.get("revised_prompt")
HEAD:backend/onyx/chat/chat_utils.py:705:            llm_image_context.append(
HEAD:backend/onyx/chat/chat_utils.py:708:                    "revised_prompt": (
HEAD:backend/onyx/chat/chat_utils.py:709:                        revised_prompt if isinstance(revised_prompt, str) else ""
HEAD:backend/onyx/chat/chat_utils.py:714:        if llm_image_context:
HEAD:backend/onyx/chat/chat_utils.py:715:            return json.dumps(llm_image_context)
HEAD:backend/onyx/chat/chat_utils.py:731:    """Convert ChatMessage history to ChatMessageSimple format.
HEAD:backend/onyx/chat/chat_utils.py:733:    For user messages: includes attached files (images attached to message, text files as separate messages)
HEAD:backend/onyx/chat/chat_utils.py:734:    For assistant messages with tool calls: creates ONE ASSISTANT message with tool_calls array,
HEAD:backend/onyx/chat/chat_utils.py:735:        followed by N TOOL_CALL_RESPONSE messages (OpenAI parallel tool calling format)
HEAD:backend/onyx/chat/chat_utils.py:736:    For assistant messages without tool calls: creates a simple ASSISTANT message
HEAD:backend/onyx/chat/chat_utils.py:744:    simple_messages: list[ChatMessageSimple] = []
HEAD:backend/onyx/chat/chat_utils.py:771:                            # Text files (DOC, PLAIN_TEXT, TABULAR) are added as separate messages
HEAD:backend/onyx/chat/chat_utils.py:774:            # Add text files as separate messages before the user message.
HEAD:backend/onyx/chat/chat_utils.py:790:                simple_messages.append(ctx.message)
HEAD:backend/onyx/chat/chat_utils.py:806:                    simple_messages.append(
HEAD:backend/onyx/chat/chat_utils.py:807:                        ChatMessageSimple(
HEAD:backend/onyx/chat/chat_utils.py:808:                            message=ADDITIONAL_CONTEXT_PROMPT.format(
HEAD:backend/onyx/chat/chat_utils.py:817:            simple_messages.append(
HEAD:backend/onyx/chat/chat_utils.py:818:                ChatMessageSimple(
HEAD:backend/onyx/chat/chat_utils.py:831:            # 3. Followed by N TOOL_CALL_RESPONSE messages (one per tool call)
HEAD:backend/onyx/chat/chat_utils.py:865:                    simple_messages.append(
HEAD:backend/onyx/chat/chat_utils.py:866:                        ChatMessageSimple(
HEAD:backend/onyx/chat/chat_utils.py:875:                    # Add TOOL_CALL_RESPONSE messages for each tool call in this turn
HEAD:backend/onyx/chat/chat_utils.py:883:                                generated_images=tool_call.generated_images,
HEAD:backend/onyx/chat/chat_utils.py:887:                        simple_messages.append(
HEAD:backend/onyx/chat/chat_utils.py:888:                            ChatMessageSimple(
HEAD:backend/onyx/chat/chat_utils.py:898:            simple_messages.append(
HEAD:backend/onyx/chat/chat_utils.py:899:                ChatMessageSimple(
HEAD:backend/onyx/chat/chat_utils.py:912:        simple_messages=simple_messages,
HEAD:backend/onyx/chat/chat_utils.py:917:def get_custom_agent_prompt(persona: Persona, chat_session: ChatSession) -> str | None:
HEAD:backend/onyx/chat/chat_utils.py:918:    """Get the custom agent prompt from persona or project instructions. If it's replacing the base system prompt,
HEAD:backend/onyx/chat/chat_utils.py:919:    it does not count as a custom agent prompt (logic exists later also to drop it in this case).
HEAD:backend/onyx/chat/chat_utils.py:921:    Chat Sessions in Projects that are using a custom agent will retain the custom agent prompt.
HEAD:backend/onyx/chat/chat_utils.py:922:    Priority: persona.system_prompt (if not default Agent) > chat_session.project.instructions
HEAD:backend/onyx/chat/chat_utils.py:924:    # NOTE: Logic elsewhere allows saving empty strings for potentially other purposes but for constructing the prompts
HEAD:backend/onyx/chat/chat_utils.py:925:    # we never want to return an empty string for a prompt so it's translated into an explicit None.
HEAD:backend/onyx/chat/chat_utils.py:932:        The prompt to use for the custom Agent part of the prompt.
HEAD:backend/onyx/chat/chat_utils.py:934:    # If using a custom Agent, always respect its prompt, even if in a Project, and even if it's an empty custom prompt.
HEAD:backend/onyx/chat/chat_utils.py:937:        if persona.replace_base_system_prompt:
HEAD:backend/onyx/chat/chat_utils.py:939:        return persona.system_prompt or None
HEAD:backend/onyx/chat/chat_utils.py:966:def create_tool_call_failure_messages(
HEAD:backend/onyx/chat/chat_utils.py:968:) -> list[ChatMessageSimple]:
HEAD:backend/onyx/chat/chat_utils.py:969:    """Create ChatMessageSimple objects for failed tool calls.
HEAD:backend/onyx/chat/chat_utils.py:971:    Creates messages using OpenAI parallel tool calling format:
HEAD:backend/onyx/chat/chat_utils.py:980:        List containing ChatMessageSimple objects: one assistant message with all tool calls
HEAD:backend/onyx/chat/chat_utils.py:1002:    assistant_msg = ChatMessageSimple(
HEAD:backend/onyx/chat/chat_utils.py:1010:    messages: list[ChatMessageSimple] = [assistant_msg]
HEAD:backend/onyx/chat/chat_utils.py:1014:        failure_response_msg = ChatMessageSimple(
HEAD:backend/onyx/chat/chat_utils.py:1015:            message=TOOL_CALL_FAILURE_PROMPT,
HEAD:backend/onyx/chat/chat_utils.py:1021:        messages.append(failure_response_msg)
HEAD:backend/onyx/chat/chat_utils.py:1023:    return messages
HEAD:backend/onyx/chat/citation_processor.py:2:Dynamic Citation Processor for LLM Responses
HEAD:backend/onyx/chat/citation_processor.py:6:- Process token streams from LLMs to extract citations
HEAD:backend/onyx/chat/citation_processor.py:20:from onyx.prompts.constants import TRIPLE_BACKTICK
HEAD:backend/onyx/chat/citation_processor.py:58:def in_code_block(llm_text: str) -> bool:
HEAD:backend/onyx/chat/citation_processor.py:60:    count = llm_text.count(TRIPLE_BACKTICK)
HEAD:backend/onyx/chat/citation_processor.py:75:    tokens from an LLM, detects citations (e.g., [1], [2,3], [[4]]), and handles
HEAD:backend/onyx/chat/citation_processor.py:111:        # Process tokens from LLM
HEAD:backend/onyx/chat/citation_processor.py:112:        for token in llm_stream:
HEAD:backend/onyx/chat/citation_processor.py:126:        # Process tokens from LLM
HEAD:backend/onyx/chat/citation_processor.py:127:        for token in llm_stream:
HEAD:backend/onyx/chat/citation_processor.py:140:        for token in llm_stream:
HEAD:backend/onyx/chat/citation_processor.py:175:        self.llm_out = ""  # entire output so far
HEAD:backend/onyx/chat/citation_processor.py:252:        Process a token from the LLM stream.
HEAD:backend/onyx/chat/citation_processor.py:271:            token: The next token from the LLM stream, or None to signal end of stream.
HEAD:backend/onyx/chat/citation_processor.py:308:        self.llm_out += token
HEAD:backend/onyx/chat/citation_processor.py:319:                    if piece_that_comes_after == "\n" and in_code_block(self.llm_out):
HEAD:backend/onyx/chat/citation_processor.py:333:        if citation_matches and not in_code_block(self.llm_out):
HEAD:backend/onyx/chat/citation_processor.py:354:                        segment_start_idx = len(self.llm_out) - len(self.curr_segment)
HEAD:backend/onyx/chat/citation_processor.py:356:                            has_leading_space = self.llm_out[
HEAD:backend/onyx/chat/citation_processor.py:503:            # Only generate formatted citations and CitationInfo in HYPERLINK mode
HEAD:backend/onyx/chat/compression.py:4:This module handles compressing long chat histories by summarizing older messages
HEAD:backend/onyx/chat/compression.py:5:while keeping recent messages verbatim.
HEAD:backend/onyx/chat/compression.py:21:from onyx.llm.interfaces import LLM
HEAD:backend/onyx/chat/compression.py:22:from onyx.llm.models import (
HEAD:backend/onyx/chat/compression.py:24:    ChatCompletionMessage,
HEAD:backend/onyx/chat/compression.py:29:from onyx.prompts.compression_prompts import (
HEAD:backend/onyx/chat/compression.py:30:    PROGRESSIVE_SUMMARY_SYSTEM_PROMPT_BLOCK,
HEAD:backend/onyx/chat/compression.py:33:    SUMMARIZATION_PROMPT,
HEAD:backend/onyx/chat/compression.py:36:from onyx.tracing.flows import LLMFlow
HEAD:backend/onyx/chat/compression.py:38:from onyx.tracing.llm_utils import llm_generation_span, record_llm_response
HEAD:backend/onyx/chat/compression.py:43:# Ratio of available context to allocate for recent messages after compression
HEAD:backend/onyx/chat/compression.py:44:RECENT_MESSAGES_RATIO = 0.2
HEAD:backend/onyx/chat/compression.py:51:    messages_summarized: int
HEAD:backend/onyx/chat/compression.py:63:    """Messages split for summarization."""
HEAD:backend/onyx/chat/compression.py:65:    older_messages: list[ChatMessage]
HEAD:backend/onyx/chat/compression.py:66:    recent_messages: list[ChatMessage]
HEAD:backend/onyx/chat/compression.py:72:    tool-call argument tokens (which are replayed alongside the messages).
HEAD:backend/onyx/chat/compression.py:75:        chat_history: Branch-aware list of messages
HEAD:backend/onyx/chat/compression.py:97:        max_input_tokens: The maximum input tokens for the LLM
HEAD:backend/onyx/chat/compression.py:99:        reserved_tokens: Tokens reserved for system prompt, tools, files, etc.
HEAD:backend/onyx/chat/compression.py:112:    # Calculate token budget for recent messages as a percentage of current history
HEAD:backend/onyx/chat/compression.py:113:    # This ensures we always have messages to summarize when compression triggers
HEAD:backend/onyx/chat/compression.py:114:    tokens_for_recent = int(current_history_tokens * RECENT_MESSAGES_RATIO)
HEAD:backend/onyx/chat/compression.py:134:        chat_history: Branch-aware list of messages
HEAD:backend/onyx/chat/compression.py:184:def get_messages_to_summarize(
HEAD:backend/onyx/chat/compression.py:190:    Split messages into those to summarize and those to keep verbatim.
HEAD:backend/onyx/chat/compression.py:193:        chat_history: Branch-aware list of messages
HEAD:backend/onyx/chat/compression.py:195:        tokens_for_recent: Token budget for recent messages to keep
HEAD:backend/onyx/chat/compression.py:198:        SummaryContent with older_messages to summarize and recent_messages to keep
HEAD:backend/onyx/chat/compression.py:200:    # Filter to messages after the existing summary's cutoff using timestamp
HEAD:backend/onyx/chat/compression.py:204:        messages = [
HEAD:backend/onyx/chat/compression.py:208:        messages = list(chat_history)
HEAD:backend/onyx/chat/compression.py:210:    # Filter out empty messages
HEAD:backend/onyx/chat/compression.py:211:    messages = [m for m in messages if m.message]
HEAD:backend/onyx/chat/compression.py:213:    if not messages:
HEAD:backend/onyx/chat/compression.py:214:        return SummaryContent(older_messages=[], recent_messages=[])
HEAD:backend/onyx/chat/compression.py:216:    # Work backwards from most recent, keeping messages until we exceed budget
HEAD:backend/onyx/chat/compression.py:217:    recent_messages: list[ChatMessage] = []
HEAD:backend/onyx/chat/compression.py:220:    for msg in reversed(messages):
HEAD:backend/onyx/chat/compression.py:224:        if tokens_used + msg_tokens > tokens_for_recent and recent_messages:
HEAD:backend/onyx/chat/compression.py:226:        recent_messages.insert(0, msg)
HEAD:backend/onyx/chat/compression.py:230:    # non-user messages from recent_messages to older_messages
HEAD:backend/onyx/chat/compression.py:231:    while recent_messages and recent_messages[0].message_type != MessageType.USER:
HEAD:backend/onyx/chat/compression.py:232:        recent_messages.pop(0)
HEAD:backend/onyx/chat/compression.py:234:    if not recent_messages:
HEAD:backend/onyx/chat/compression.py:238:        # compression entirely (older_messages empty → caller no-ops).
HEAD:backend/onyx/chat/compression.py:242:                for i in range(len(messages) - 1, -1, -1)
HEAD:backend/onyx/chat/compression.py:243:                if messages[i].message_type == MessageType.USER
HEAD:backend/onyx/chat/compression.py:248:            return SummaryContent(older_messages=[], recent_messages=messages)
HEAD:backend/onyx/chat/compression.py:249:        recent_messages = messages[last_user_idx:]
HEAD:backend/onyx/chat/compression.py:252:    recent_ids = {m.id for m in recent_messages}
HEAD:backend/onyx/chat/compression.py:253:    older_messages = [m for m in messages if m.id not in recent_ids]
HEAD:backend/onyx/chat/compression.py:256:        older_messages=older_messages, recent_messages=recent_messages
HEAD:backend/onyx/chat/compression.py:260:def _build_llm_messages_for_summarization(
HEAD:backend/onyx/chat/compression.py:261:    messages: list[ChatMessage],
HEAD:backend/onyx/chat/compression.py:264:    """Convert ChatMessage objects to LLM message format for summarization.
HEAD:backend/onyx/chat/compression.py:266:    This is intentionally different from translate_history_to_llm_format in llm_step.py:
HEAD:backend/onyx/chat/compression.py:268:    - Skips TOOL_CALL_RESPONSE messages entirely (tool usage captured in assistant message)
HEAD:backend/onyx/chat/compression.py:270:    - No caching or LLMConfig-specific behavior needed
HEAD:backend/onyx/chat/compression.py:274:    for msg in messages:
HEAD:backend/onyx/chat/compression.py:275:        # Skip empty messages
HEAD:backend/onyx/chat/compression.py:279:        # Handle assistant messages with tool calls compactly
HEAD:backend/onyx/chat/compression.py:292:        # Skip tool call response messages - tool calls are captured above via assistant messages
HEAD:backend/onyx/chat/compression.py:296:        # Handle user messages
HEAD:backend/onyx/chat/compression.py:303:def generate_summary(
HEAD:backend/onyx/chat/compression.py:304:    older_messages: list[ChatMessage],
HEAD:backend/onyx/chat/compression.py:305:    recent_messages: list[ChatMessage],
HEAD:backend/onyx/chat/compression.py:306:    llm: LLM,
HEAD:backend/onyx/chat/compression.py:311:    Generate a summary using cutoff marker approach.
HEAD:backend/onyx/chat/compression.py:313:    The cutoff marker tells the LLM to summarize only older messages,
HEAD:backend/onyx/chat/compression.py:314:    while using recent messages as context to inform what's important.
HEAD:backend/onyx/chat/compression.py:316:    Messages are sent as separate UserMessage/AssistantMessage objects rather
HEAD:backend/onyx/chat/compression.py:320:        older_messages: Messages to compress into summary (before cutoff)
HEAD:backend/onyx/chat/compression.py:321:        recent_messages: Messages kept verbatim (after cutoff, for context only)
HEAD:backend/onyx/chat/compression.py:322:        llm: LLM to use for summarization
HEAD:backend/onyx/chat/compression.py:329:    # Build system prompt
HEAD:backend/onyx/chat/compression.py:330:    system_content = SUMMARIZATION_PROMPT
HEAD:backend/onyx/chat/compression.py:332:        # Progressive summarization: append existing summary to system prompt
HEAD:backend/onyx/chat/compression.py:333:        system_content += PROGRESSIVE_SUMMARY_SYSTEM_PROMPT_BLOCK.format(
HEAD:backend/onyx/chat/compression.py:340:    # Convert messages to LLM format (using compression-specific conversion)
HEAD:backend/onyx/chat/compression.py:341:    older_llm_messages = _build_llm_messages_for_summarization(
HEAD:backend/onyx/chat/compression.py:342:        older_messages, tool_id_to_name
HEAD:backend/onyx/chat/compression.py:344:    recent_llm_messages = _build_llm_messages_for_summarization(
HEAD:backend/onyx/chat/compression.py:345:        recent_messages, tool_id_to_name
HEAD:backend/onyx/chat/compression.py:348:    # Build message list with separate messages
HEAD:backend/onyx/chat/compression.py:349:    input_messages: list[ChatCompletionMessage] = [
HEAD:backend/onyx/chat/compression.py:353:    # Add older messages (to be summarized)
HEAD:backend/onyx/chat/compression.py:354:    input_messages.extend(older_llm_messages)
HEAD:backend/onyx/chat/compression.py:357:    input_messages.append(UserMessage(content=SUMMARIZATION_CUTOFF_MARKER))
HEAD:backend/onyx/chat/compression.py:359:    # Add recent messages (for context only)
HEAD:backend/onyx/chat/compression.py:360:    input_messages.extend(recent_llm_messages)
HEAD:backend/onyx/chat/compression.py:363:    input_messages.append(UserMessage(content=final_reminder))
HEAD:backend/onyx/chat/compression.py:365:    with llm_generation_span(
HEAD:backend/onyx/chat/compression.py:366:        llm=llm,
HEAD:backend/onyx/chat/compression.py:367:        flow=LLMFlow.CHAT_HISTORY_SUMMARIZATION,
HEAD:backend/onyx/chat/compression.py:368:        input_messages=input_messages,
HEAD:backend/onyx/chat/compression.py:370:        response = llm.invoke(input_messages)
HEAD:backend/onyx/chat/compression.py:371:        record_llm_response(span_generation, response)
HEAD:backend/onyx/chat/compression.py:375:        raise ValueError("LLM returned empty summary")
HEAD:backend/onyx/chat/compression.py:381:    llm: LLM,
HEAD:backend/onyx/chat/compression.py:391:    messages (to summarize) and recent messages (kept verbatim within the
HEAD:backend/onyx/chat/compression.py:392:    token budget), generates a summary of the older part, and persists the
HEAD:backend/onyx/chat/compression.py:396:    at most one existing summary for this branch. If present, only messages
HEAD:backend/onyx/chat/compression.py:398:    existing summary text is passed into the LLM so the new summary
HEAD:backend/onyx/chat/compression.py:402:    tool name map), the LLM call runs with no session held, and a fresh
HEAD:backend/onyx/chat/compression.py:406:    ``prefetch_top_two_level_tool_calls=True``); ``_build_llm_messages_for_summarization``
HEAD:backend/onyx/chat/compression.py:413:        chat_history: Branch-aware list of messages
HEAD:backend/onyx/chat/compression.py:414:        llm: LLM to use for summarization
HEAD:backend/onyx/chat/compression.py:421:        return CompressionResult(summary_created=False, messages_summarized=0)
HEAD:backend/onyx/chat/compression.py:438:            # Read phase: existing summary + tool name map. Closed before LLM call.
HEAD:backend/onyx/chat/compression.py:449:            summary_content = get_messages_to_summarize(
HEAD:backend/onyx/chat/compression.py:455:            if not summary_content.older_messages:
HEAD:backend/onyx/chat/compression.py:456:                logger.debug("No messages to summarize, skipping compression")
HEAD:backend/onyx/chat/compression.py:457:                return CompressionResult(summary_created=False, messages_summarized=0)
HEAD:backend/onyx/chat/compression.py:459:            # LLM call runs with no DB connection held.
HEAD:backend/onyx/chat/compression.py:460:            summary_text = generate_summary(
HEAD:backend/onyx/chat/compression.py:461:                older_messages=summary_content.older_messages,
HEAD:backend/onyx/chat/compression.py:462:                recent_messages=summary_content.recent_messages,
HEAD:backend/onyx/chat/compression.py:463:                llm=llm,
HEAD:backend/onyx/chat/compression.py:471:                "Generated summary (%s tokens): %s...",
HEAD:backend/onyx/chat/compression.py:484:                    last_summarized_message_id=summary_content.older_messages[-1].id,
HEAD:backend/onyx/chat/compression.py:490:                "Compressed %s messages into summary (session_id=%s, summary_tokens=%s)",
HEAD:backend/onyx/chat/compression.py:491:                len(summary_content.older_messages),
HEAD:backend/onyx/chat/compression.py:498:                messages_summarized=len(summary_content.older_messages),
HEAD:backend/onyx/chat/compression.py:507:                messages_summarized=0,
HEAD:backend/onyx/chat/emitter.py:9:    """Routes packets from LLM/tool execution to the ``_run_models`` drain loop.
HEAD:backend/onyx/chat/incognito.py:45:from onyx.llm.constants import LlmProviderNames
HEAD:backend/onyx/chat/incognito.py:46:from onyx.llm.interfaces import LlmRequestPolicy
HEAD:backend/onyx/chat/incognito.py:47:from onyx.llm.well_known_providers.constants import BIFROST_PROVIDER_NAME
HEAD:backend/onyx/chat/incognito.py:95:# LiteLLM proxy per-request redaction: content stripped from its logs while
HEAD:backend/onyx/chat/incognito.py:97:LITELLM_PROXY_REDACTION_HEADER = "x-litellm-enable-message-redaction"
HEAD:backend/onyx/chat/incognito.py:135:def sweep_incognito_generated_files(db_session: Session) -> None:
HEAD:backend/onyx/chat/incognito.py:136:    """Retry deletion of tool-generated blobs a teardown pass failed to remove.
HEAD:backend/onyx/chat/incognito.py:158:            delete_incognito_generated_files(session_id, db_session)
HEAD:backend/onyx/chat/incognito.py:164:def incognito_llm_extra_headers(
HEAD:backend/onyx/chat/incognito.py:168:    """Headers an LLM request must carry under this recording mode.
HEAD:backend/onyx/chat/incognito.py:174:    Pass the result as ``get_llm``'s ``policy_headers`` so it outranks request,
HEAD:backend/onyx/chat/incognito.py:182:    if provider == LlmProviderNames.PORTKEY.value:
HEAD:backend/onyx/chat/incognito.py:184:    if provider == LlmProviderNames.LITELLM_PROXY.value:
HEAD:backend/onyx/chat/incognito.py:185:        return {LITELLM_PROXY_REDACTION_HEADER: "true"}
HEAD:backend/onyx/chat/incognito.py:189:def incognito_llm_extra_body(
HEAD:backend/onyx/chat/incognito.py:200:    # OpenAI Responses API stores by default for 30 days, and Chat Completions
HEAD:backend/onyx/chat/incognito.py:201:    # accepts the same param. Azure's stored-completions opt-in stays off.
HEAD:backend/onyx/chat/incognito.py:203:        LlmProviderNames.OPENAI.value,
HEAD:backend/onyx/chat/incognito.py:204:        LlmProviderNames.AZURE.value,
HEAD:backend/onyx/chat/incognito.py:208:    if provider == LlmProviderNames.OPENROUTER.value:
HEAD:backend/onyx/chat/incognito.py:213:def incognito_llm_request_policy(
HEAD:backend/onyx/chat/incognito.py:216:) -> LlmRequestPolicy:
HEAD:backend/onyx/chat/incognito.py:223:    return LlmRequestPolicy(
HEAD:backend/onyx/chat/incognito.py:224:        headers=incognito_llm_extra_headers(mode, provider),
HEAD:backend/onyx/chat/incognito.py:225:        model_kwargs=incognito_llm_extra_body(mode, provider),
HEAD:backend/onyx/chat/incognito.py:243:def delete_incognito_generated_files(
HEAD:backend/onyx/chat/incognito.py:257:            logger.warning("Failed to delete incognito generated file %s", file_id)
HEAD:backend/onyx/chat/incognito_context.py:21:from onyx.chat.models import ChatMessageSimple
HEAD:backend/onyx/chat/incognito_context.py:34:# Raw-storage caps. Token budgeting trims context further at prompt build.
HEAD:backend/onyx/chat/incognito_context.py:36:_MAX_CONTEXT_MESSAGES = 200
HEAD:backend/onyx/chat/incognito_context.py:43:_MESSAGES_ADAPTER: TypeAdapter[list[ChatMessageSimple]] = TypeAdapter(
HEAD:backend/onyx/chat/incognito_context.py:44:    list[ChatMessageSimple]
HEAD:backend/onyx/chat/incognito_context.py:47:# Stored value grammar: ``<version>:<messages json>``. Lua and Python agree
HEAD:backend/onyx/chat/incognito_context.py:75:    messages: list[ChatMessageSimple]
HEAD:backend/onyx/chat/incognito_context.py:109:    """The session's context, messages oldest first.
HEAD:backend/onyx/chat/incognito_context.py:111:    Empty messages mean nothing was written, the session was torn down, the
HEAD:backend/onyx/chat/incognito_context.py:117:        return IncognitoContext(version=0, messages=[])
HEAD:backend/onyx/chat/incognito_context.py:124:        return IncognitoContext(version=0, messages=[])
HEAD:backend/onyx/chat/incognito_context.py:126:        messages = _MESSAGES_ADAPTER.validate_json(body)
HEAD:backend/onyx/chat/incognito_context.py:133:        return IncognitoContext(version=version, messages=[])
HEAD:backend/onyx/chat/incognito_context.py:134:    return IncognitoContext(version=version, messages=messages)
HEAD:backend/onyx/chat/incognito_context.py:145:    attachments only live within their own turn. Oldest messages fall off
HEAD:backend/onyx/chat/incognito_context.py:150:        for message in context.messages[-_MAX_CONTEXT_MESSAGES:]
HEAD:backend/onyx/chat/incognito_context.py:152:    body = _MESSAGES_ADAPTER.dump_json(trimmed)
HEAD:backend/onyx/chat/incognito_context.py:155:        body = _MESSAGES_ADAPTER.dump_json(trimmed)
HEAD:backend/onyx/chat/incognito_context.py:171:def append_incognito_message(chat_session_id: UUID, message: ChatMessageSimple) -> None:
HEAD:backend/onyx/chat/incognito_context.py:181:        context.messages.append(message)
HEAD:backend/onyx/chat/llm_loop.py:10:    create_tool_call_failure_messages,
HEAD:backend/onyx/chat/llm_loop.py:19:from onyx.chat.llm_step import (
HEAD:backend/onyx/chat/llm_loop.py:22:    run_llm_step,
HEAD:backend/onyx/chat/llm_loop.py:25:    ChatMessageSimple,
HEAD:backend/onyx/chat/llm_loop.py:29:    LlmStepResult,
HEAD:backend/onyx/chat/llm_loop.py:32:from onyx.chat.prompt_utils import (
HEAD:backend/onyx/chat/llm_loop.py:34:    build_system_prompt,
HEAD:backend/onyx/chat/llm_loop.py:35:    get_default_base_system_prompt,
HEAD:backend/onyx/chat/llm_loop.py:36:    process_prompt_template,
HEAD:backend/onyx/chat/llm_loop.py:40:from onyx.configs.chat_configs import MAX_LLM_CYCLES
HEAD:backend/onyx/chat/llm_loop.py:47:from onyx.llm.constants import LlmProviderNames
HEAD:backend/onyx/chat/llm_loop.py:48:from onyx.llm.exceptions import ClassifiedLLMError
HEAD:backend/onyx/chat/llm_loop.py:49:from onyx.llm.interfaces import LLM, LLMUserIdentity, ToolChoiceOptions
HEAD:backend/onyx/chat/llm_loop.py:50:from onyx.llm.model_capabilities import is_true_openai_model
HEAD:backend/onyx/chat/llm_loop.py:51:from onyx.llm.models import ReasoningEffort
HEAD:backend/onyx/chat/llm_loop.py:52:from onyx.llm.utils import model_supports_image_input
HEAD:backend/onyx/chat/llm_loop.py:53:from onyx.prompts.chat_prompts import (
HEAD:backend/onyx/chat/llm_loop.py:58:from onyx.prompts.prompt_utils import substitute_user_placeholders
HEAD:backend/onyx/chat/llm_loop.py:98:class EmptyLLMResponseError(ClassifiedLLMError):
HEAD:backend/onyx/chat/llm_loop.py:99:    """Raised when the streamed LLM response completes without a usable answer."""
HEAD:backend/onyx/chat/llm_loop.py:108:        error_code: str = "EMPTY_LLM_RESPONSE",
HEAD:backend/onyx/chat/llm_loop.py:123:# LiteLLM maps these native policy blocks to content_filter, but gateways may
HEAD:backend/onyx/chat/llm_loop.py:148:def _build_empty_llm_response_error(
HEAD:backend/onyx/chat/llm_loop.py:149:    llm: LLM,
HEAD:backend/onyx/chat/llm_loop.py:150:    llm_step_result: LlmStepResult,
HEAD:backend/onyx/chat/llm_loop.py:152:) -> EmptyLLMResponseError:
HEAD:backend/onyx/chat/llm_loop.py:153:    provider = llm.config.model_provider
HEAD:backend/onyx/chat/llm_loop.py:154:    model = llm.config.model_name
HEAD:backend/onyx/chat/llm_loop.py:155:    finish_reason = llm_step_result.finish_reason
HEAD:backend/onyx/chat/llm_loop.py:162:            " (e.g. Claude Opus 4.8)" if provider == LlmProviderNames.ANTHROPIC else ""
HEAD:backend/onyx/chat/llm_loop.py:164:        return EmptyLLMResponseError(
HEAD:backend/onyx/chat/llm_loop.py:183:        not llm_step_result.reasoning
HEAD:backend/onyx/chat/llm_loop.py:184:        and provider == LlmProviderNames.OPENAI
HEAD:backend/onyx/chat/llm_loop.py:187:        return EmptyLLMResponseError(
HEAD:backend/onyx/chat/llm_loop.py:202:    return EmptyLLMResponseError(
HEAD:backend/onyx/chat/llm_loop.py:216:    llm_step_result: LlmStepResult,
HEAD:backend/onyx/chat/llm_loop.py:221:) -> tuple[LlmStepResult, bool]:
HEAD:backend/onyx/chat/llm_loop.py:224:    This is a last resort fallback for low quality LLMs or those that don't have
HEAD:backend/onyx/chat/llm_loop.py:229:        llm_step_result: The result from the LLM step
HEAD:backend/onyx/chat/llm_loop.py:236:        Tuple of (possibly updated LlmStepResult, whether fallback was attempted this call)
HEAD:backend/onyx/chat/llm_loop.py:239:        return llm_step_result, False
HEAD:backend/onyx/chat/llm_loop.py:242:        not llm_step_result.tool_calls or len(llm_step_result.tool_calls) == 0
HEAD:backend/onyx/chat/llm_loop.py:245:        llm_step_result.reasoning and not llm_step_result.answer and no_tool_calls
HEAD:backend/onyx/chat/llm_loop.py:248:        _looks_like_xml_tool_call_payload(llm_step_result.answer)
HEAD:backend/onyx/chat/llm_loop.py:249:        or _looks_like_xml_tool_call_payload(llm_step_result.raw_answer)
HEAD:backend/onyx/chat/llm_loop.py:250:        or _looks_like_xml_tool_call_payload(llm_step_result.reasoning)
HEAD:backend/onyx/chat/llm_loop.py:259:        return llm_step_result, False
HEAD:backend/onyx/chat/llm_loop.py:264:    if llm_step_result.answer:
HEAD:backend/onyx/chat/llm_loop.py:266:            response_text=llm_step_result.answer,
HEAD:backend/onyx/chat/llm_loop.py:272:        and llm_step_result.raw_answer
HEAD:backend/onyx/chat/llm_loop.py:273:        and llm_step_result.raw_answer != llm_step_result.answer
HEAD:backend/onyx/chat/llm_loop.py:276:            response_text=llm_step_result.raw_answer,
HEAD:backend/onyx/chat/llm_loop.py:280:    if not extracted_tool_calls and llm_step_result.reasoning:
HEAD:backend/onyx/chat/llm_loop.py:282:            response_text=llm_step_result.reasoning,
HEAD:backend/onyx/chat/llm_loop.py:292:            LlmStepResult(
HEAD:backend/onyx/chat/llm_loop.py:293:                reasoning=llm_step_result.reasoning,
HEAD:backend/onyx/chat/llm_loop.py:294:                answer=llm_step_result.answer,
HEAD:backend/onyx/chat/llm_loop.py:296:                raw_answer=llm_step_result.raw_answer,
HEAD:backend/onyx/chat/llm_loop.py:297:                finish_reason=llm_step_result.finish_reason,
HEAD:backend/onyx/chat/llm_loop.py:302:    return llm_step_result, True
HEAD:backend/onyx/chat/llm_loop.py:312:# Override via the MAX_LLM_CYCLES env var when running with tool-heavy MCPs
HEAD:backend/onyx/chat/llm_loop.py:356:) -> list[ChatMessageSimple]:
HEAD:backend/onyx/chat/llm_loop.py:357:    """Build messages for context-injected / tool-backed files.
HEAD:backend/onyx/chat/llm_loop.py:359:    Returns up to two messages:
HEAD:backend/onyx/chat/llm_loop.py:361:    2. A lightweight metadata message for files the LLM should access via the
HEAD:backend/onyx/chat/llm_loop.py:367:    messages: list[ChatMessageSimple] = []
HEAD:backend/onyx/chat/llm_loop.py:369:        messages.append(
HEAD:backend/onyx/chat/llm_loop.py:373:        messages.append(
HEAD:backend/onyx/chat/llm_loop.py:378:    return messages
HEAD:backend/onyx/chat/llm_loop.py:382:    msg: ChatMessageSimple,
HEAD:backend/onyx/chat/llm_loop.py:405:    system_prompt: ChatMessageSimple | None,
HEAD:backend/onyx/chat/llm_loop.py:406:    custom_agent_prompt: ChatMessageSimple | None,
HEAD:backend/onyx/chat/llm_loop.py:407:    simple_chat_history: list[ChatMessageSimple],
HEAD:backend/onyx/chat/llm_loop.py:408:    reminder_message: ChatMessageSimple | None,
HEAD:backend/onyx/chat/llm_loop.py:411:    last_n_user_messages: int | None = None,
HEAD:backend/onyx/chat/llm_loop.py:415:) -> list[ChatMessageSimple]:
HEAD:backend/onyx/chat/llm_loop.py:416:    if last_n_user_messages is not None:
HEAD:backend/onyx/chat/llm_loop.py:417:        if last_n_user_messages <= 0:
HEAD:backend/onyx/chat/llm_loop.py:419:                "filtering chat history by last N user messages must be a value greater than 0"
HEAD:backend/onyx/chat/llm_loop.py:428:    # Build the project / file-metadata messages up front so we can use their
HEAD:backend/onyx/chat/llm_loop.py:430:    project_messages = _build_project_message(context_files, token_counter)
HEAD:backend/onyx/chat/llm_loop.py:431:    project_messages_tokens = sum(m.token_count for m in project_messages)
HEAD:backend/onyx/chat/llm_loop.py:434:    history_token_budget -= system_prompt.token_count if system_prompt else 0
HEAD:backend/onyx/chat/llm_loop.py:436:        custom_agent_prompt.token_count if custom_agent_prompt else 0
HEAD:backend/onyx/chat/llm_loop.py:438:    history_token_budget -= project_messages_tokens
HEAD:backend/onyx/chat/llm_loop.py:444:    if system_prompt:
HEAD:backend/onyx/chat/llm_loop.py:445:        system_prompt.should_cache = True
HEAD:backend/onyx/chat/llm_loop.py:449:        result = [system_prompt] if system_prompt else []
HEAD:backend/onyx/chat/llm_loop.py:450:        if custom_agent_prompt:
HEAD:backend/onyx/chat/llm_loop.py:451:            result.append(custom_agent_prompt)
HEAD:backend/onyx/chat/llm_loop.py:452:        result.extend(project_messages)
HEAD:backend/onyx/chat/llm_loop.py:457:    # If last_n_user_messages is set, filter history to only include the last n user messages
HEAD:backend/onyx/chat/llm_loop.py:458:    if last_n_user_messages is not None:
HEAD:backend/onyx/chat/llm_loop.py:469:        # If we have more than n user messages, keep only the last n
HEAD:backend/onyx/chat/llm_loop.py:470:        if len(user_msg_indices) > last_n_user_messages:
HEAD:backend/onyx/chat/llm_loop.py:472:            # For example, if last_n_user_messages=2, we want the 2nd-to-last user message
HEAD:backend/onyx/chat/llm_loop.py:473:            nth_user_msg_index = user_msg_indices[-(last_n_user_messages)]
HEAD:backend/onyx/chat/llm_loop.py:491:    # 3. Messages after the last user message (tool calls, responses, etc.)
HEAD:backend/onyx/chat/llm_loop.py:494:    messages_after_last_user = simple_chat_history[last_user_msg_index + 1 :]
HEAD:backend/onyx/chat/llm_loop.py:499:        _replay_token_count(msg) for msg in messages_after_last_user
HEAD:backend/onyx/chat/llm_loop.py:502:    # Check if we can fit at least the last user message and messages after it
HEAD:backend/onyx/chat/llm_loop.py:506:            f"Not enough tokens to include the last user message and subsequent messages. "
HEAD:backend/onyx/chat/llm_loop.py:514:    # Track dropped file messages so we can provide their metadata to the
HEAD:backend/onyx/chat/llm_loop.py:516:    truncated_history_before: list[ChatMessageSimple] = []
HEAD:backend/onyx/chat/llm_loop.py:530:    # Collect file_ids from ALL dropped messages (those not in
HEAD:backend/onyx/chat/llm_loop.py:532:    # recent messages, so the dropped ones are at the start of the original
HEAD:backend/onyx/chat/llm_loop.py:542:    # from messages removed by summary truncation (before convert_chat_history
HEAD:backend/onyx/chat/llm_loop.py:543:    # ran), so no ChatMessageSimple was ever tagged with their file_id.
HEAD:backend/onyx/chat/llm_loop.py:552:    # Build a forgotten-files metadata message if any file messages were
HEAD:backend/onyx/chat/llm_loop.py:555:    forgotten_files_message: ChatMessageSimple | None = None
HEAD:backend/onyx/chat/llm_loop.py:571:            # fit we may need to drop more history messages.
HEAD:backend/onyx/chat/llm_loop.py:591:    # [forgotten_files], [last_user_message], [messages_after_last_user], [reminder]
HEAD:backend/onyx/chat/llm_loop.py:592:    result = [system_prompt] if system_prompt else []
HEAD:backend/onyx/chat/llm_loop.py:597:    # 2. Add custom agent prompt (inserted before last user message)
HEAD:backend/onyx/chat/llm_loop.py:598:    if custom_agent_prompt:
HEAD:backend/onyx/chat/llm_loop.py:599:        result.append(custom_agent_prompt)
HEAD:backend/onyx/chat/llm_loop.py:601:    # 3. Add context files / file-metadata messages (inserted before last user message)
HEAD:backend/onyx/chat/llm_loop.py:602:    result.extend(project_messages)
HEAD:backend/onyx/chat/llm_loop.py:611:    # 6. Add messages after last user message (tool calls, responses, etc.)
HEAD:backend/onyx/chat/llm_loop.py:612:    result.extend(messages_after_last_user)
HEAD:backend/onyx/chat/llm_loop.py:622:    messages: list[ChatMessageSimple],
HEAD:backend/onyx/chat/llm_loop.py:623:) -> list[ChatMessageSimple]:
HEAD:backend/onyx/chat/llm_loop.py:624:    """Drop tool response messages whose tool_call_id is not in prior assistant tool calls.
HEAD:backend/onyx/chat/llm_loop.py:631:    sanitized: list[ChatMessageSimple] = []
HEAD:backend/onyx/chat/llm_loop.py:633:    for msg in messages:
HEAD:backend/onyx/chat/llm_loop.py:658:) -> ChatMessageSimple:
HEAD:backend/onyx/chat/llm_loop.py:662:    disabled, so the LLM must use ``read_file`` to inspect them.
HEAD:backend/onyx/chat/llm_loop.py:675:    return ChatMessageSimple(
HEAD:backend/onyx/chat/llm_loop.py:685:) -> ChatMessageSimple:
HEAD:backend/onyx/chat/llm_loop.py:686:    """Convert context files to a ChatMessageSimple message.
HEAD:backend/onyx/chat/llm_loop.py:710:    return ChatMessageSimple(
HEAD:backend/onyx/chat/llm_loop.py:723:    persona_task_prompt: str | None,
HEAD:backend/onyx/chat/llm_loop.py:738:        reminder_text=persona_task_prompt,
HEAD:backend/onyx/chat/llm_loop.py:745:def run_llm_loop(
HEAD:backend/onyx/chat/llm_loop.py:748:    simple_chat_history: list[ChatMessageSimple],
HEAD:backend/onyx/chat/llm_loop.py:750:    custom_agent_prompt: str | None,
HEAD:backend/onyx/chat/llm_loop.py:754:    llm: LLM,
HEAD:backend/onyx/chat/llm_loop.py:757:    user_identity: LLMUserIdentity | None = None,
HEAD:backend/onyx/chat/llm_loop.py:763:    inject_memories_in_prompt: bool = True,
HEAD:backend/onyx/chat/llm_loop.py:766:        "run_llm_loop",
HEAD:backend/onyx/chat/llm_loop.py:773:        # Fix some LiteLLM issues,
HEAD:backend/onyx/chat/llm_loop.py:774:        from onyx.llm.litellm_singleton.config import (
HEAD:backend/onyx/chat/llm_loop.py:775:            initialize_litellm,
HEAD:backend/onyx/chat/llm_loop.py:776:        )  # Here for lazy load LiteLLM
HEAD:backend/onyx/chat/llm_loop.py:778:        initialize_litellm()
HEAD:backend/onyx/chat/llm_loop.py:805:        llm_step_result = LlmStepResult(
HEAD:backend/onyx/chat/llm_loop.py:813:        token_budget = resolve_chat_token_budget(llm)
HEAD:backend/onyx/chat/llm_loop.py:816:        # short text markers (translate_history_to_llm_format) — budget them
HEAD:backend/onyx/chat/llm_loop.py:822:            llm.config.model_name, llm.config.model_provider, llm.config.deployment_name
HEAD:backend/onyx/chat/llm_loop.py:832:        # One future workaround is to include the images as separate user messages with citation information and process those.
HEAD:backend/onyx/chat/llm_loop.py:841:        code_interpreter_file_generated: bool = False
HEAD:backend/onyx/chat/llm_loop.py:847:        with get_session_with_current_tenant() as prompt_db_session:
HEAD:backend/onyx/chat/llm_loop.py:848:            default_base_system_prompt: str = get_default_base_system_prompt(
HEAD:backend/onyx/chat/llm_loop.py:849:                prompt_db_session
HEAD:backend/onyx/chat/llm_loop.py:851:        system_prompt = None
HEAD:backend/onyx/chat/llm_loop.py:852:        custom_agent_prompt_msg = None
HEAD:backend/onyx/chat/llm_loop.py:855:        # agent's prompts against the current user's directory profile (+
HEAD:backend/onyx/chat/llm_loop.py:864:        custom_agent_prompt = (
HEAD:backend/onyx/chat/llm_loop.py:865:            substitute_user_placeholders(custom_agent_prompt, placeholder_values)
HEAD:backend/onyx/chat/llm_loop.py:866:            if custom_agent_prompt
HEAD:backend/onyx/chat/llm_loop.py:867:            else custom_agent_prompt
```
No provider was contacted.
This evidence only identifies source-level candidate model handoff paths.
## Permission Synchronization
Evidence lines: 223
```text
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:72:from onyx.db.permission_sync_attempt import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:73:    complete_doc_permission_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:74:    create_doc_permission_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:75:    mark_doc_permission_sync_attempt_failed,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:76:    mark_doc_permission_sync_attempt_in_progress,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:103:    doc_permission_sync_ctx,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:144:def _fail_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:153:        mark_doc_permission_sync_attempt_failed(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:163:def _is_external_doc_permissions_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:196:    source_sync_period *= int(OnyxRuntime.get_doc_permission_sync_multiplier())
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:207:    name=OnyxCeleryTask.CHECK_FOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:212:def check_for_doc_permissions_sync(self: Task, *, tenant_id: str) -> bool | None:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:221:        OnyxRedisLocks.CHECK_CONNECTOR_DOC_PERMISSIONS_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:238:                if _is_external_doc_permissions_sync_due(cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:244:            maybe_mark_tenant_active(tenant_id, caller="doc_permission_sync")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:260:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:266:                validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:275:                OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:297:        task_logger.info(f"check_for_doc_permissions_sync finished: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:305:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:308:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:362:                    sync_type=SyncType.EXTERNAL_PERMISSIONS,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:378:            OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:383:            queue=OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:410:    name=OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:417:def connector_permission_sync_generator_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:423:    Permission sync task that handles document permission syncing for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:431:    doc_permission_sync_ctx_dict = dict(doc_permission_sync_ctx.get())
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:432:    doc_permission_sync_ctx_dict["cc_pair_id"] = cc_pair_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:433:    doc_permission_sync_ctx_dict["request_id"] = self.request.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:434:    doc_permission_sync_ctx.set(doc_permission_sync_ctx_dict)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:437:        attempt_id = create_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:456:                f"connector_permission_sync_generator_task - timed out waiting for fence to be ready: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:459:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:463:            error_msg = f"connector_permission_sync_generator_task - fence not found: fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:464:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:470:                "connector_permission_sync_generator_task: payload invalid or not found"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:472:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:477:                "connector_permission_sync_generator_task - Waiting for fence: fence=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:486:            "connector_permission_sync_generator_task - Fence found, continuing...: fence=%s payload_id=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:493:        OnyxRedisLocks.CONNECTOR_DOC_PERMISSIONS_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:505:        _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:554:                _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:560:                    _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:569:            mark_doc_permission_sync_attempt_in_progress(attempt_id, db_session)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:616:        document_external_accesses = doc_sync_func(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:627:        for doc_external_access in document_external_accesses:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:637:                new_permissions=[doc_external_access],
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:656:            complete_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:679:        _fail_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:718:    external_access = permissions.external_access
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:733:                emails=list(external_access.external_user_emails),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:742:                    external_access=external_access,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:760:                    is_public=external_access.is_public,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:762:                        list(external_access.external_user_emails)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:763:                        if external_access.external_user_emails
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:767:                        list(external_access.external_user_group_ids)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:768:                        if external_access.external_user_group_ids
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:790:def validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:799:    PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN = 1024
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:802:        OnyxCeleryQueues.DOC_PERMISSIONS_UPSERT, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:804:    if queue_len > PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:808:        OnyxCeleryQueues.DOC_PERMISSIONS_UPSERT, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:811:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:823:        validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:837:def validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:876:            f"validate_permission_sync_fence - could not parse id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:895:            "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:915:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:956:        f"validate_permission_sync_fence task check: tasks_scanned={tasks_scanned} tasks_not_in_celery={tasks_not_in_celery}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:977:        "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1104:        record_type=RecordType.PERMISSION_SYNC_PROGRESS,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1123:        record_type=RecordType.PERMISSION_SYNC_COMPLETE,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1131:        sync_type=SyncType.EXTERNAL_PERMISSIONS,
HEAD:backend/ee/onyx/db/document.py:15:    external_access: ExternalAccess,
HEAD:backend/ee/onyx/db/document.py:31:        for group_id in external_access.external_user_group_ids
HEAD:backend/ee/onyx/db/document.py:40:            external_user_emails=external_access.external_user_emails,
HEAD:backend/ee/onyx/db/document.py:42:            is_public=external_access.is_public,
HEAD:backend/ee/onyx/db/document.py:47:    document.external_user_emails = list(external_access.external_user_emails)
HEAD:backend/ee/onyx/db/document.py:49:    document.is_public = external_access.is_public
HEAD:backend/ee/onyx/db/document.py:55:    external_access: ExternalAccess,
HEAD:backend/ee/onyx/db/document.py:72:        for group_id in external_access.external_user_group_ids
HEAD:backend/ee/onyx/db/document.py:82:            external_user_emails=external_access.external_user_emails,
HEAD:backend/ee/onyx/db/document.py:84:            is_public=external_access.is_public,
HEAD:backend/ee/onyx/db/document.py:90:    # If the document exists, we need to check if the external access has changed
HEAD:backend/ee/onyx/db/document.py:92:        external_access.external_user_emails != set(document.external_user_emails or [])
HEAD:backend/ee/onyx/db/document.py:94:        or external_access.is_public != document.is_public
HEAD:backend/ee/onyx/db/document.py:96:        document.external_user_emails = list(external_access.external_user_emails)
HEAD:backend/ee/onyx/db/document.py:98:        document.is_public = external_access.is_public
HEAD:backend/ee/onyx/external_permissions/box/access.py:48:    def from_external_access(
HEAD:backend/ee/onyx/external_permissions/box/access.py:49:        cls, external_access: ExternalAccess | None
HEAD:backend/ee/onyx/external_permissions/box/access.py:51:        if external_access is None:
HEAD:backend/ee/onyx/external_permissions/box/access.py:54:            user_emails=external_access.external_user_emails,
HEAD:backend/ee/onyx/external_permissions/box/access.py:55:            group_ids=external_access.external_user_group_ids,
HEAD:backend/ee/onyx/external_permissions/box/access.py:56:            is_public=external_access.is_public,
HEAD:backend/ee/onyx/external_permissions/box/access.py:66:    def to_external_access(self) -> ExternalAccess:
HEAD:backend/ee/onyx/external_permissions/box/access.py:171:    access = BoxAccessContext.from_external_access(inherited_access)
HEAD:backend/ee/onyx/external_permissions/box/access.py:181:    ).to_external_access()
HEAD:backend/ee/onyx/external_permissions/box/access.py:217:        BoxAccessContext.from_external_access(folder_access), file.owned_by
HEAD:backend/ee/onyx/external_permissions/box/access.py:223:    ).to_external_access()
HEAD:backend/ee/onyx/external_permissions/box/access.py:231:    access = BoxAccessContext.from_external_access(folder_access)
HEAD:backend/ee/onyx/external_permissions/box/access.py:234:    ).to_external_access()
HEAD:backend/ee/onyx/external_permissions/confluence/page_access.py:86:def _resolve_external_access(
HEAD:backend/ee/onyx/external_permissions/confluence/page_access.py:154:    add_prefix: True for the indexing path (Document.external_access) so
HEAD:backend/ee/onyx/external_permissions/confluence/page_access.py:159:    return _resolve_external_access(
HEAD:backend/ee/onyx/external_permissions/confluence/page_access.py:194:    return _resolve_external_access(
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:80:        # Don't fail the whole sync over an anonymous-permissions hiccup.
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:13:    get_external_access_permission,
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:42:    Sync GitHub documents with external access permissions.
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:116:                new_external_access = get_external_access_permission(
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:126:                # Yield updated external access for each document
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:133:                        external_access=new_external_access,
HEAD:backend/ee/onyx/external_permissions/github/utils.py:310:def get_external_access_permission(
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:73:                if slim_doc.external_access:
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:75:                        external_access=slim_doc.external_access,
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:80:            if slim_doc.external_access is None:
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:86:                external_access=slim_doc.external_access,
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:102:def get_external_access_for_raw_gdrive_file(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:120:                When invoked from doc_sync (permission sync), use the default (False)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:282:def get_external_access_for_folder(
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:405:                if slim_doc.external_access:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:407:                        external_access=slim_doc.external_access,
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:412:            if slim_doc.external_access is None:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:418:                external_access=slim_doc.external_access,
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:472:def _build_external_access_from_holder_map(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:497:            "static Onyx ACLs; unsupported_holder_counts=%s all_holder_counts=%s",
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:666:    external_access = _build_external_access_from_holder_map(
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:671:    if add_prefix and external_access and external_access.external_user_group_ids:
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:674:            for g in external_access.external_user_group_ids
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:677:            external_user_emails=external_access.external_user_emails,
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:679:            is_public=external_access.is_public,
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:682:    return external_access
HEAD:backend/ee/onyx/external_permissions/microsoft_utils/entra_groups.py:65:    failed id lookup yields the literal ``None`` suffix. Persisted ACLs already
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:376:def _get_external_access_from_securable_object(
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:436:        "get_external_access_from_sharepoint",
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:468:def get_external_access_from_sharepoint(
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:517:    return _get_external_access_from_securable_object(
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:526:def get_hierarchy_node_external_access_from_sharepoint(
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:548:    return _get_external_access_from_securable_object(
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:205:            external_access = doc_metadata.external_access
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:206:            if external_access is None:
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:218:                    external_access = override_access
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:221:                external_access=external_access,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:214:    """Mock doc sync function for testing - returns empty list since permissions are fetched during indexing"""
HEAD:backend/ee/onyx/external_permissions/sync_params.py:221:            doc_sync_frequency=DEFAULT_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:226:            group_sync_frequency=GOOGLE_DRIVE_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:233:            doc_sync_frequency=CONFLUENCE_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:238:            group_sync_frequency=CONFLUENCE_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:245:            doc_sync_frequency=JIRA_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:250:            group_sync_frequency=JIRA_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:257:            doc_sync_frequency=CANVAS_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:262:            group_sync_frequency=CANVAS_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:269:            doc_sync_frequency=BOX_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:274:            group_sync_frequency=BOX_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:283:            doc_sync_frequency=SLACK_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:290:            doc_sync_frequency=DEFAULT_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:297:            doc_sync_frequency=GITHUB_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:302:            group_sync_frequency=GITHUB_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:314:            doc_sync_frequency=DEFAULT_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:323:            doc_sync_frequency=TEAMS_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:330:            doc_sync_frequency=SHAREPOINT_PERMISSION_DOC_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/sync_params.py:335:            group_sync_frequency=SHAREPOINT_PERMISSION_GROUP_SYNC_FREQUENCY,
HEAD:backend/ee/onyx/external_permissions/utils.py:45:        `external_access` set to "private")
HEAD:backend/ee/onyx/external_permissions/utils.py:77:                if doc.external_access:
HEAD:backend/ee/onyx/external_permissions/utils.py:79:                        external_access=doc.external_access,
HEAD:backend/ee/onyx/external_permissions/utils.py:84:            if not doc.external_access:
HEAD:backend/ee/onyx/external_permissions/utils.py:93:                external_access=doc.external_access,
HEAD:backend/ee/onyx/external_permissions/utils.py:115:            external_access=ExternalAccess.empty(),
HEAD:backend/onyx/access/access.py:114:def _get_acl_for_user(
HEAD:backend/onyx/access/access.py:118:    """Returns a list of ACL entries that the user has access to. This is meant to be
HEAD:backend/onyx/access/access.py:120:    user should have access to a document if at least one entry in the document's ACL
HEAD:backend/onyx/access/access.py:125:    Addresses the user was renamed away from match too. Indexed ACLs keep
HEAD:backend/onyx/access/access.py:138:def get_acl_for_user(user: User, db_session: Session | None = None) -> set[str]:
HEAD:backend/onyx/access/access.py:139:    versioned_acl_for_user_fn = fetch_versioned_implementation(
HEAD:backend/onyx/access/access.py:140:        "onyx.access.access", "_get_acl_for_user"
HEAD:backend/onyx/access/access.py:142:    return versioned_acl_for_user_fn(user, db_session)
HEAD:backend/onyx/access/access.py:234:    - `Document` whose ACL grants access (covers connector-ingested files).
HEAD:backend/onyx/access/access.py:317:    """Mirror retrieval-time ACL: grant access if any `Document` referencing
HEAD:backend/onyx/access/access.py:318:    `file_id` has an ACL the user satisfies.
HEAD:backend/onyx/access/access.py:326:       ACL, so any one representative document answers the question.
HEAD:backend/onyx/access/access.py:342:    user_acl = get_acl_for_user(user, db_session)
HEAD:backend/onyx/access/access.py:345:        not user_acl.isdisjoint(access.to_acl()) for access in doc_access.values()
HEAD:backend/onyx/access/access.py:355:    because ACLs are scoped to the cc_pair: the same connector paired with
HEAD:backend/onyx/access/access.py:356:    different credentials can have different ACLs, and a user with access
HEAD:backend/onyx/access/models.py:1:from dataclasses import dataclass
HEAD:backend/onyx/access/models.py:11:@dataclass(frozen=True)
HEAD:backend/onyx/access/models.py:58:        This is especially helpful to use when you are performing permission-syncing, and some document's permissions aren't able
HEAD:backend/onyx/access/models.py:69:@dataclass(frozen=True)
HEAD:backend/onyx/access/models.py:73:    together. It's used for syncing document permissions to Vespa.
HEAD:backend/onyx/access/models.py:76:    external_access: ExternalAccess
HEAD:backend/onyx/access/models.py:82:            "external_access": {
HEAD:backend/onyx/access/models.py:83:                "external_user_emails": list(self.external_access.external_user_emails),
HEAD:backend/onyx/access/models.py:85:                    self.external_access.external_user_group_ids
HEAD:backend/onyx/access/models.py:87:                "is_public": self.external_access.is_public,
HEAD:backend/onyx/access/models.py:94:        external_access = ExternalAccess(
HEAD:backend/onyx/access/models.py:96:                data["external_access"].get("external_user_emails", [])
HEAD:backend/onyx/access/models.py:99:                data["external_access"].get("external_user_group_ids", [])
HEAD:backend/onyx/access/models.py:101:            is_public=data["external_access"]["is_public"],
HEAD:backend/onyx/access/models.py:104:            external_access=external_access,
HEAD:backend/onyx/access/models.py:109:@dataclass(frozen=True)
HEAD:backend/onyx/access/models.py:113:    Used for syncing hierarchy node permissions (e.g., folder permissions).
HEAD:backend/onyx/access/models.py:116:    external_access: ExternalAccess
HEAD:backend/onyx/access/models.py:124:            "external_access": {
HEAD:backend/onyx/access/models.py:125:                "external_user_emails": list(self.external_access.external_user_emails),
HEAD:backend/onyx/access/models.py:127:                    self.external_access.external_user_group_ids
HEAD:backend/onyx/access/models.py:129:                "is_public": self.external_access.is_public,
HEAD:backend/onyx/access/models.py:137:        external_access = ExternalAccess(
HEAD:backend/onyx/access/models.py:139:                data["external_access"].get("external_user_emails", [])
HEAD:backend/onyx/access/models.py:142:                data["external_access"].get("external_user_group_ids", [])
HEAD:backend/onyx/access/models.py:144:            is_public=data["external_access"]["is_public"],
HEAD:backend/onyx/access/models.py:147:            external_access=external_access,
HEAD:backend/onyx/access/models.py:159:@dataclass(frozen=True, init=False)
HEAD:backend/onyx/access/models.py:176:    def to_acl(self) -> set[str]:
HEAD:backend/onyx/access/models.py:177:        """Converts the access state to a set of formatted ACL strings.
HEAD:backend/onyx/access/models.py:179:        NOTE: When querying for documents, the supplied ACL filter strings must
HEAD:backend/onyx/access/models.py:182:        acl_set: set[str] = set()
HEAD:backend/onyx/access/models.py:185:                acl_set.add(prefix_user_email(user_email))
HEAD:backend/onyx/access/models.py:188:            acl_set.add(prefix_user_group(group_name))
HEAD:backend/onyx/access/models.py:191:            acl_set.add(prefix_user_email(external_user_email))
HEAD:backend/onyx/access/models.py:194:            acl_set.add(prefix_external_group(external_group_id))
HEAD:backend/onyx/access/models.py:197:            acl_set.add(PUBLIC_DOC_PAT)
HEAD:backend/onyx/access/models.py:199:        return acl_set
HEAD:backend/onyx/access/models.py:210:        """Don't prefix incoming data wth acl type, prefix on read from to_acl!"""
```
Permission synchronization is security critical because stale ACL state can
create a gap between source-system authorization and retrieval-time
authorization.
## Current RAG Flow Model
```text
Stage | Static evidence status
------|-----------------------
Connector document acquisition | OBSERVED
User-file/upload ingestion | OBSERVED
Indexing orchestration | OBSERVED
Document processing/chunking | OBSERVED
Embedding generation | OBSERVED
Document/chunk index writes | OBSERVED
Index-time access metadata | OBSERVED
Index-time tenant metadata | OBSERVED
Search/retrieval | OBSERVED
Retrieval-time ACL/tenant filtering | OBSERVED
Reranking | OBSERVED
Retrieved-document context assembly | OBSERVED
LLM handoff candidates | OBSERVED
Permission synchronization | OBSERVED
Actual runtime data flow | NOT RUNTIME VERIFIED
Correct tenant isolation | NOT PROVEN
Correct ACL enforcement | NOT PROVEN
Prompt-injection resistance | NOT PROVEN
```
## Evidence-Backed Provisional Data Flow
The pinned source supports a provisional model in which:
1. documents enter through connectors and/or user-file upload mechanisms;
2. background/indexing orchestration processes source content;
3. documents are transformed into chunks;
4. embedding/model infrastructure generates vector representations where
   configured;
5. document/chunk data is written to an index backend;
6. tenant and access-control metadata accompany indexed content;
7. query/search logic retrieves candidate content;
8. tenant and ACL filters participate in retrieval;
9. candidate results may be reranked;
10. selected retrieved content is assembled into model-visible context;
11. that context can be handed to LLM/chat orchestration.
## Critical Security Boundaries
### Source -> internal document
Untrusted external content enters the trusted application pipeline.
### Document -> chunk
Security metadata must survive transformation.
### Chunk -> index
Tenant and ACL metadata must remain bound to the indexed representation.
### User query -> retrieval
The caller's effective identity and tenant must become retrieval filters.
### Retrieval -> reranking
Unauthorized candidates must not reach later stages.
### Retrieved content -> model context
Documents become instructions/data visible to an LLM, creating the primary
retrieval prompt-injection boundary.
## High-Value Future Tests
Later phases must verify:
- cross-tenant retrieval isolation;
- cross-user ACL isolation;
- stale-permission behavior after source permission changes;
- access revocation propagation;
- deleted-document persistence;
- user-file ownership isolation;
- connector scope isolation;
- index metadata tampering resilience;
- filter consistency across index backends;
- retrieval prompt injection;
- indirect prompt injection through indexed documents;
- poisoned or conflicting documents;
- malicious metadata;
- reranker manipulation;
- citation/source confusion;
- unauthorized context reaching the LLM.
No vulnerability claim is made by Action 6.6.
## Interpretation Boundary
This action demonstrates static mechanisms and candidate flow only.
It does not prove:
- actual runtime ordering;
- actual document contents;
- exact active index backend;
- correct ACL synchronization;
- correct tenant isolation;
- complete deletion;
- correct revocation;
- retrieval correctness;
- absence of prompt injection;
- absence of data leakage.
## Safety Record
During Action 6.6:
- Onyx application execution: NO
- Docker execution: NO
- connectors contacted: NO
- files uploaded: NO
- model server invoked: NO
- embeddings generated: NO
- index writes executed: NO
- search queries executed: NO
- LLM/provider invocation: NO
- credentials used: NO
- production/customer data: NO
- vulnerability testing: NO
- Onyx source modification: NO
## Result
Action 6.6 document and RAG data-flow trace: **PASS**.
