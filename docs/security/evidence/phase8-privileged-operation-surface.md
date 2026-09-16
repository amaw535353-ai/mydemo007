# Phase 8 Action 8.8 - Privileged and Administrative Operation Surface

## Interpretation boundary

This is a keyword- and source-evidence-based shortlist for later vertical-authorization testing. It does not prove that a route is externally exposed or incorrectly protected.

Privileged-route candidates: **200**

| Method | Local route | Function | Privilege signals | Visible dependencies | File:line |
|---|---|---|---|---|---|
| POST | /manage/admin/cc-pair/{cc_pair_id}/sync-groups | sync_cc_pair_groups | admin, connector, credential, group, permission, user | Depends, require_permission | backend/ee/onyx/server/documents/cc_pair.py:135 |
| PUT | /manage/admin/cc-pair/{cc_pair_id}/status | update_cc_pair_status | admin, connector, credential, permission, user | Depends, require_permission | backend/onyx/server/documents/cc_pair.py:470 |
| GET | /manage/admin/cc-pair/{cc_pair_id} | get_cc_pair_full_info | admin, connector, credential, group, permission, user | Depends, require_permission | backend/onyx/server/documents/cc_pair.py:338 |
| PUT | /manage/admin/credential/private-key/{credential_id} | update_credential_private_key | admin, credential, permission | Depends, File, Form, require_permission | backend/onyx/server/documents/credential.py:329 |
| POST | /manage/admin/cc-pair/{cc_pair_id}/sync-permissions | sync_cc_pair | admin, connector, credential, permission, user | Depends, require_permission | backend/ee/onyx/server/documents/cc_pair.py:56 |
| POST | /manage/admin/cc-pair/{cc_pair_id}/prune | prune_cc_pair | admin, connector, credential, permission, user | Depends, require_permission | backend/onyx/server/documents/cc_pair.py:685 |
| POST | /manage/admin/connector/{connector_id}/files/update | update_connector_files | admin, connector, permission | Depends, File, Form, require_permission | backend/onyx/server/documents/connector.py:559 |
| POST | /manage/credential/private-key | create_credential_with_private_key | credential, permission | Depends, File, Form, require_permission | backend/onyx/server/documents/credential.py:197 |
| PUT | /manage/admin/cc-pair/{cc_pair_id}/name | update_cc_pair_name | admin, connector, credential, permission, user | Depends, require_permission | backend/onyx/server/documents/cc_pair.py:577 |
| PUT | /manage/admin/cc-pair/{cc_pair_id}/property | update_cc_pair_property | admin, connector, credential, permission, user | Depends, require_permission | backend/onyx/server/documents/cc_pair.py:611 |
| GET | /manage/admin/connector/google-drive/check-auth/{credential_id} | check_drive_tokens | admin, connector, credential, permission, user | Depends, require_permission | backend/onyx/server/documents/connector.py:222 |
| POST | /manage/admin/connector/indexing-status | get_connector_indexing_status | admin, connector, credential, group, permission, user | Depends, require_permission | backend/onyx/server/documents/connector.py:966 |
| DELETE | /manage/admin/document-set/{document_set_id} | delete_document_set | admin, group, permission, user | Depends, require_permission | backend/onyx/server/features/document_set/api.py:182 |
| POST | /manage/admin/deletion-attempt | create_deletion_attempt_for_connector_id | admin, connector, credential, group, permission, user | Depends, require_permission | backend/onyx/server/manage/administrative.py:150 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/sync-groups | get_cc_pair_latest_group_sync | admin, connector, credential, group, permission, user | Depends, require_permission | backend/ee/onyx/server/documents/cc_pair.py:112 |
| PATCH | /manage/admin/user-group/{user_group_id}/document-sets | update_group_document_sets | admin, group, permission, user | Depends, require_permission | backend/ee/onyx/server/user_group/api.py:527 |
| POST | /manage/admin/connector-with-mock-credential | create_connector_with_mock_credential | admin, connector, credential, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:1499 |
| PUT | /manage/connector/{connector_id}/credential/{credential_id} | associate_credential_to_connector | connector, credential, permission | Depends, require_permission | backend/onyx/server/documents/cc_pair.py:797 |
| POST | /manage/admin/credential/{credential_id}/capability-check | trigger_capability_check | admin, credential, permission, user | Depends, require_permission | backend/onyx/server/documents/credential_capabilities.py:134 |
| DELETE | /admin/token-rate-limits/user-group/{group_id}/rate-limit/{rate_limit_id} | delete_group_token_limit_settings | admin, group, permission, settings, user | Depends, require_permission | backend/ee/onyx/server/token_rate_limits/api.py:261 |
| POST | /manage/admin/connector/run-once | connector_run_once | admin, connector, credential, permission, user | Depends, require_permission | backend/onyx/server/documents/connector.py:1664 |
| DELETE | /manage/admin/credential/{credential_id} | delete_credential_by_id_admin | admin, credential, permission | Depends, require_permission | backend/onyx/server/documents/credential.py:103 |
| PUT | /admin/token-rate-limits/user-group/{group_id}/rate-limit/{rate_limit_id} | update_group_token_limit_settings | admin, group, permission, settings, user | Depends, require_permission | backend/ee/onyx/server/token_rate_limits/api.py:237 |
| PATCH | /manage/admin/document-set | patch_document_set | admin, group, permission | Depends, require_permission | backend/onyx/server/features/document_set/api.py:114 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/sync-permissions | get_cc_pair_latest_sync | admin, connector, credential, permission, user | Depends, require_permission | backend/ee/onyx/server/documents/cc_pair.py:33 |
| POST | /connector/confluence/callback | confluence_oauth_callback | connector, credential, permission | Depends, require_permission | backend/ee/onyx/server/oauth/confluence_cloud.py:146 |
| DELETE | /manage/admin/connector/{connector_id} | delete_connector_by_id | admin, connector, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:1639 |
| PUT | /manage/admin/credential/{credential_id} | update_credential_data | admin, credential, permission | Depends, require_permission | backend/onyx/server/documents/credential.py:302 |
| GET | /manage/admin/credential/{credential_id}/capability-report | get_capability_report | admin, credential, permission, user | Depends, require_permission | backend/onyx/server/documents/credential_capabilities.py:263 |
| POST | /admin/token-rate-limits/user-group/{group_id} | create_group_token_limit_settings | admin, group, permission, settings, user | Depends, require_permission | backend/ee/onyx/server/token_rate_limits/api.py:158 |
| PATCH | /manage/admin/connector/{connector_id} | update_connector_from_model | admin, connector, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:1588 |
| DELETE | /admin/api-key/{api_key_id} | delete_api_key | admin, api_key, permission | Depends, require_permission | backend/onyx/server/api_key/api.py:117 |
| PUT | /manage/admin/connector/google-drive/service-account-credential | upsert_service_account_credential | admin, connector, credential, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:183 |
| PUT | /manage/admin/connector/gmail/service-account-credential | upsert_gmail_service_account_credential | admin, connector, credential, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:203 |
| GET | /manage/admin/connector/status | get_connector_status | admin, connector, credential, group, permission, user | Depends, require_permission | backend/onyx/server/documents/connector.py:904 |
| GET | /connector/oauth/callback/{source} | oauth_callback | connector, credential, permission | Depends, require_permission | backend/onyx/server/documents/standard_oauth.py:242 |
| PATCH | /admin/api-key/{api_key_id} | update_existing_api_key | admin, api_key, permission | Depends, require_permission | backend/onyx/server/api_key/api.py:94 |
| DELETE | /manage/connector/{connector_id}/credential/{credential_id} | dissociate_credential_from_connector | connector, credential, permission, user | Depends, require_permission | backend/onyx/server/documents/cc_pair.py:925 |
| GET | /manage/admin/connector/{connector_id}/files | list_connector_files | admin, connector, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:442 |
| POST | /manage/admin/connector | create_connector_from_model | admin, connector, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:1458 |
| PUT | /manage/admin/credential/swap | swap_credentials_for_connector | admin, connector, credential, permission | Depends, require_permission | backend/onyx/server/documents/credential.py:123 |
| POST | /connector/confluence/finalize | confluence_oauth_finalize | connector, credential, permission, user | Depends, require_permission | backend/ee/onyx/server/oauth/confluence_cloud.py:323 |
| GET | /admin/token-rate-limits/user-group/{group_id} | get_group_token_limit_settings | admin, group, permission, settings, user | Depends, require_permission | backend/ee/onyx/server/token_rate_limits/api.py:138 |
| POST | /onyx-api/ingestion | upsert_ingestion_doc | connector, credential, permission, settings, user | Depends, require_permission | backend/onyx/server/onyx_api/ingestion.py:102 |
| POST | /connector/google-drive/callback | handle_google_drive_oauth_callback | connector, credential, permission | Depends, require_permission | backend/ee/onyx/server/oauth/google_drive.py:111 |
| POST | /connector/slack/callback | handle_slack_oauth_callback | connector, credential, permission | Depends, require_permission | backend/ee/onyx/server/oauth/slack.py:100 |
| GET | /manage/connector/gmail/callback | gmail_callback | connector, credential, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:1788 |
| GET | /manage/connector/google-drive/callback | google_drive_callback | connector, credential, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:1818 |
| DELETE | /manage/credential/{credential_id} | delete_credential_by_id | credential, permission, user | Depends, require_permission | backend/onyx/server/documents/credential.py:423 |
| DELETE | /manage/credential/force/{credential_id} | force_delete_credential_by_id | credential, permission, user | Depends, require_permission | backend/onyx/server/documents/credential.py:448 |
| POST | /manage/admin/document-set | create_document_set | admin, permission | Depends, require_permission | backend/onyx/server/features/document_set/api.py:48 |
| DELETE | /admin/token-rate-limits/rate-limit/{token_rate_limit_id} | delete_token_limit_settings | admin, permission, settings | Depends, require_permission | backend/ee/onyx/server/token_rate_limits/api.py:101 |
| POST | /admin/search | admin_search | admin, permission, settings, user | Depends, require_permission | backend/onyx/server/query_and_chat/query_backend.py:34 |
| DELETE | /manage/admin/user-group/{user_group_id} | delete_user_group | admin, group, permission, user | Depends, require_permission | backend/ee/onyx/server/user_group/api.py:419 |
| GET | /manage/admin/connector/failed-indexing-status | get_currently_failed_indexing_status | admin, connector, credential, permission, user | Depends, Query, require_permission | backend/onyx/server/documents/connector.py:816 |
| GET | /manage/connector/gmail/authorize/{credential_id} | gmail_auth | connector, credential, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:1746 |
| GET | /manage/connector/google-drive/authorize/{credential_id} | google_drive_auth | connector, credential, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:1767 |
| PATCH | /manage/credential/{credential_id} | update_credential_from_model | credential, permission | Depends, require_permission | backend/onyx/server/documents/credential.py:379 |
| GET | /manage/admin/credential/capability-reports | list_capability_reports_for_source | admin, connector, credential, permission, user | Depends, require_permission | backend/onyx/server/documents/credential_capabilities.py:308 |
| PUT | /federated/{id} | update_federated_connector_endpoint | connector, credential, permission | Depends, require_permission | backend/onyx/server/federated/api.py:568 |
| PUT | /admin/token-rate-limits/rate-limit/{token_rate_limit_id} | update_token_limit_settings | admin, permission, settings | Depends, require_permission | backend/ee/onyx/server/token_rate_limits/api.py:82 |
| POST | /admin/api-key/{api_key_id}/regenerate | regenerate_existing_api_key | admin, api_key, permission | Depends, require_permission | backend/onyx/server/api_key/api.py:75 |
| DELETE | /user/projects/file/{file_id} | delete_user_file | permission, user | Depends, require_permission | backend/onyx/server/features/projects/api.py:518 |
| DELETE | /scim/v2/Groups/{group_id} | delete_group | group, permission, user | Depends | backend/ee/onyx/server/scim/api.py:1556 |
| PATCH | /manage/admin/user-group/{user_group_id}/incognito | patch_user_group_incognito | admin, group, permission, user | Depends, require_permission | backend/ee/onyx/server/user_group/api.py:348 |
| PATCH | /manage/admin/user-group/{user_group_id} | patch_user_group | admin, group, permission, user | Depends, require_permission | backend/ee/onyx/server/user_group/api.py:373 |
| PATCH | /manage/admin/user-group/{user_group_id}/agents | update_group_agents | admin, group, permission, user | Depends, require_permission | backend/ee/onyx/server/user_group/api.py:457 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/external-group-sync-attempts | get_cc_pair_external_group_sync_attempts | admin, group, permission | Depends, Query, require_permission | backend/onyx/server/documents/cc_pair.py:285 |
| POST | /user-library/upload | upload_files | connector, credential, permission, user | Depends, File, Form, require_permission | backend/onyx/server/features/build/user_library/api.py:180 |
| POST | /user-library/upload-zip | upload_zip | connector, credential, permission, user | Depends, File, Form, require_permission | backend/onyx/server/features/build/user_library/api.py:284 |
| GET | /manage/admin/document-set/{document_set_id} | get_document_set | admin, group, permission, user | Depends, require_permission | backend/onyx/server/features/document_set/api.py:231 |
| GET | /connector/confluence/accessible-resources | confluence_oauth_accessible_resources | connector, credential, permission, user | Depends, require_permission | backend/ee/onyx/server/oauth/confluence_cloud.py:259 |
| GET | /manage/admin/similar-credentials/{source_type} | get_cc_source_full_info | admin, credential, permission, user | Depends, require_permission | backend/onyx/server/documents/credential.py:80 |
| DELETE | /user-library/files/{document_id} | delete_file | permission, user | Depends, require_permission | backend/onyx/server/features/build/user_library/api.py:483 |
| PUT | /admin/tool/custom/{tool_id} | update_custom_tool | admin, permission, settings | Depends, require_permission | backend/onyx/server/features/tool/api.py:176 |
| POST | /federated/ | create_federated_connector | connector, credential, permission | Depends, require_permission | backend/onyx/server/federated/api.py:69 |
| PUT | /scim/v2/Groups/{group_id} | replace_group | group, permission, user | Depends | backend/ee/onyx/server/scim/api.py:1396 |
| PATCH | /scim/v2/Groups/{group_id} | patch_group | group, permission, user | Depends | backend/ee/onyx/server/scim/api.py:1463 |
| PATCH | /admin/sso/provider/{provider_id} | update_sso_provider_endpoint | admin, credential, permission | Depends, require_permission | backend/onyx/server/manage/sso/api.py:197 |
| POST | /admin/enterprise-settings/scim/token | create_scim_token | admin, permission, settings | Depends, require_permission | backend/ee/onyx/server/enterprise_settings/api.py:378 |
| POST | /chat/send-chat-message | handle_send_chat_message | permission | Depends, require_permission | backend/onyx/server/query_and_chat/chat_backend.py:799 |
| PUT | /manage/admin/user-group/{user_group_id}/permissions | set_user_group_permissions | admin, group, permission, user | Depends, require_permission | backend/ee/onyx/server/user_group/api.py:222 |
| PUT | /manage/admin/user-group/{user_group_id}/manager | set_group_manager | admin, group, permission, user | Depends, require_permission | backend/ee/onyx/server/user_group/api.py:614 |
| GET | /manage/admin/connector | get_connectors_by_credential | admin, connector, credential, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:783 |
| POST | /manage/admin/indexing/targeted-reindex | submit_targeted_reindex | admin, permission | Depends, require_permission | backend/onyx/server/documents/targeted_reindex.py:78 |
| GET | /apps/{external_app_id}/oauth/start | start_external_app_oauth | credential, permission | Depends, require_permission | backend/onyx/server/features/build/external_apps/oauth.py:85 |
| POST | /sessions/{session_id}/subagents/{subagent_session_id}/send-message | send_subagent_message | permission | Depends, require_permission | backend/onyx/server/features/build/session/messages.py:221 |
| DELETE | /mcp/user-credentials/{server_id} | delete_user_credentials | credential, permission, user | Depends, require_permission | backend/onyx/server/features/mcp/api.py:1099 |
| DELETE | /admin/mcp/server/{server_id} | delete_mcp_server_admin | admin, permission | Depends, require_permission | backend/onyx/server/features/mcp/api.py:2652 |
| DELETE | /admin/oauth-config/{oauth_config_id} | delete_oauth_config_endpoint | admin, permission | Depends, require_permission | backend/onyx/server/features/oauth_config/api.py:174 |
| DELETE | /user/projects/{project_id}/files/{file_id} | unlink_user_file_from_project | permission, user | Depends, require_permission | backend/onyx/server/features/projects/api.py:280 |
| DELETE | /admin/tool/custom/{tool_id} | delete_custom_tool | admin, permission | Depends, require_permission | backend/onyx/server/features/tool/api.py:211 |
| DELETE | /admin/llm/provider/{provider_id} | delete_llm_provider | admin, permission | Depends, Query, require_permission | backend/onyx/server/manage/llm/api.py:733 |
| DELETE | /manage/admin/delete-user | delete_user | admin, permission, user | Depends, require_permission | backend/onyx/server/manage/users.py:809 |
| GET | /admin/token-rate-limits/user-groups | get_all_group_token_limit_settings | admin, group, permission, settings, user | Depends, require_permission | backend/ee/onyx/server/token_rate_limits/api.py:120 |
| PATCH | /admin/persona/{persona_id}/undelete | undelete_persona | admin, permission | Depends, require_permission | backend/onyx/server/features/persona/api.py:312 |
| PUT | /scim/v2/Users/{user_id} | replace_user | admin, group, user | Depends | backend/ee/onyx/server/scim/api.py:917 |
| PATCH | /scim/v2/Users/{user_id} | patch_user | admin, group, user | Depends | backend/ee/onyx/server/scim/api.py:1006 |
| POST | /admin/token-rate-limits/users | create_user_token_limit_settings | admin, permission, settings, user | Depends, require_permission | backend/ee/onyx/server/token_rate_limits/api.py:293 |
| POST | /manage/admin/user-group/{user_group_id}/add-users | add_users | admin, group, permission, user | Depends, require_permission | backend/ee/onyx/server/user_group/api.py:396 |
| POST | /admin/api-key/ | create_api_key | admin, api_key, permission | Depends, require_permission | backend/onyx/server/api_key/api.py:53 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/index-attempts | get_cc_pair_index_attempts | admin, permission | Depends, Query, require_permission | backend/onyx/server/documents/cc_pair.py:118 |
| GET | /manage/admin/index-attempt/{index_attempt_id}/stage-metrics | get_index_attempt_stage_metrics | admin, permission | Depends, require_permission | backend/onyx/server/documents/cc_pair.py:160 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/permission-sync-attempts | get_cc_pair_permission_sync_attempts | admin, permission | Depends, Query, require_permission | backend/onyx/server/documents/cc_pair.py:235 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/last_pruned | get_cc_pair_last_pruned | admin, permission | Depends, require_permission | backend/onyx/server/documents/cc_pair.py:667 |
| GET | /manage/admin/credential | list_credentials_admin | admin, credential, permission, user | Depends, require_permission | backend/onyx/server/documents/credential.py:59 |
| GET | /manage/credential/{credential_id} | get_credential_by_id | credential, permission, user | Depends, require_permission | backend/onyx/server/documents/credential.py:279 |
| GET | /manage/admin/indexing/targeted-reindex/{job_id} | get_targeted_reindex_status | admin, permission | Depends, require_permission | backend/onyx/server/documents/targeted_reindex.py:172 |
| PATCH | /admin/mcp/server/{server_id} | update_mcp_server_simple | admin, permission | Depends, require_permission | backend/onyx/server/features/mcp/api.py:2558 |
| PUT | /admin/oauth-config/{oauth_config_id} | update_oauth_config_endpoint | admin, permission | Depends, require_permission | backend/onyx/server/features/oauth_config/api.py:138 |
| DELETE | /oauth-config/{oauth_config_id}/token | revoke_oauth_token | permission, user | Depends, require_permission | backend/onyx/server/features/oauth_config/api.py:298 |
| GET | /federated/{id}/authorize | get_authorize_url | connector, credential, permission | Depends, require_permission | backend/onyx/server/federated/api.py:328 |
| GET | /federated/{id} | get_federated_connector_detail | connector, credential, permission | Depends, require_permission | backend/onyx/server/federated/api.py:522 |
| DELETE | /federated/{id}/oauth | disconnect_oauth_token | permission | Depends, require_permission | backend/onyx/server/federated/api.py:618 |
| DELETE | /admin/web-search/search-providers/{provider_id} | delete_search_provider | admin, permission | Depends, require_permission | backend/onyx/server/manage/web_search/api.py:157 |
| DELETE | /admin/web-search/content-providers/{provider_id} | delete_content_provider | admin, permission | Depends, require_permission | backend/onyx/server/manage/web_search/api.py:337 |
| GET | /onyx-api/connector-docs/{cc_pair_id} | get_docs_by_connector_credential_pair | connector, credential, permission, user | Depends, require_permission | backend/onyx/server/onyx_api/ingestion.py:59 |
| DELETE | /onyx-api/ingestion/{document_id} | delete_ingestion_doc | permission | Depends, require_permission | backend/onyx/server/onyx_api/ingestion.py:238 |
| DELETE | /user/pats/{token_id} | delete_token | permission, user | Depends, require_permission | backend/onyx/server/pat/api.py:95 |
| POST | /chat/end-incognito-session/{session_id} | end_incognito_session | permission | Depends, require_permission | backend/onyx/server/query_and_chat/chat_backend.py:730 |
| GET | /admin/api-key/{api_key_id} | get_api_key | admin, api_key, permission | Depends, require_permission | backend/onyx/server/api_key/api.py:39 |
| POST | /user/projects/{project_id}/files/{file_id} | link_user_file_to_project | permission, user | Depends, require_permission | backend/onyx/server/features/projects/api.py:325 |
| POST | /search/ | search | group, permission, settings, user | Depends, require_permission | backend/onyx/server/features/search/api.py:57 |
| DELETE | /manage/admin/discord-bot/service-api-key | delete_service_api_key_endpoint | admin, api_key, permission | Depends, require_permission | backend/onyx/server/manage/discord_bot/api.py:134 |
| POST | /admin/tracing/providers/{provider_type}/adopt-env | adopt_env_tracing_provider | admin, credential, permission | Depends, require_permission | backend/onyx/server/manage/tracing/api.py:179 |
| GET | /chat/max-selected-document-tokens | get_max_document_tokens | permission | Depends, require_permission | backend/onyx/server/query_and_chat/chat_backend.py:1040 |
| POST | /admin/hooks/{hook_id}/activate | activate_hook | admin, permission | Depends, require_permission | backend/ee/onyx/server/features/hooks/api.py:363 |
| POST | /tenants/seats/update | update_seats | admin, permission | Depends, require_permission | backend/ee/onyx/server/tenants/billing_api.py:156 |
| GET | /manage/admin/user-group/{user_group_id} | get_user_group | admin, group, permission, user | Depends, require_permission | backend/ee/onyx/server/user_group/api.py:137 |
| GET | /manage/admin/user-group/{user_group_id}/permissions | get_user_group_permissions | admin, group, permission, user | Depends, require_permission | backend/ee/onyx/server/user_group/api.py:202 |
| GET | /persona/{persona_id} | get_persona | admin, group, permission, user | Depends | backend/onyx/server/features/persona/api.py:696 |
| POST | /admin/usage/reset | reset_usage | admin, group, permission, user | Depends, require_permission | backend/onyx/server/features/usage/api.py:401 |
| POST | /federated/callback | handle_oauth_callback_generic | connector, credential, permission | Depends, require_permission | backend/onyx/server/federated/api.py:377 |
| DELETE | /chat/delete-chat-session/{session_id} | delete_chat_session_by_id | permission | Depends, require_permission | backend/onyx/server/query_and_chat/chat_backend.py:681 |
| GET | /chat/chat-session/{session_id}/resume-stream | resume_chat_stream | permission | Depends, Query, require_permission | backend/onyx/server/query_and_chat/chat_backend.py:1292 |
| POST | /prepare-authorization-request | prepare_authorization_request | permission | Depends, require_permission | backend/ee/onyx/server/oauth/api.py:24 |
| POST | /manage/admin/connector/file/upload | upload_files_api | admin, connector, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:433 |
| DELETE | /apps/{external_app_id}/credentials | disconnect_user_from_external_app | credential, permission, user | Depends, require_permission | backend/onyx/server/features/build/external_apps/api.py:403 |
| POST | /sessions/{session_id}/snapshot | create_session_snapshot | permission | Depends, require_permission | backend/onyx/server/features/build/session/api.py:436 |
| POST | /sessions/{session_id}/opencode-history-snapshot | create_session_opencode_history_snapshot | permission | Depends, require_permission | backend/onyx/server/features/build/session/api.py:471 |
| DELETE | /sessions/{session_id}/files/{path:path} | delete_file_endpoint | permission | Depends, require_permission | backend/onyx/server/features/build/session/api.py:819 |
| DELETE | /admin/hooks/{hook_id} | delete_hook | admin, permission | Depends, require_permission | backend/ee/onyx/server/features/hooks/api.py:352 |
| DELETE | /manage/admin/standard-answer/{standard_answer_id} | delete_standard_answer | admin, permission | Depends, require_permission | backend/ee/onyx/server/manage/standard_answer.py:87 |
| DELETE | /manage/admin/standard-answer/category/{standard_answer_category_id} | delete_standard_answer_category | admin, permission | Depends, require_permission | backend/ee/onyx/server/manage/standard_answer.py:151 |
| DELETE | /apps/{external_app_id} | delete_external_app_admin | admin, permission | Depends, require_permission | backend/onyx/server/features/build/external_apps/api.py:340 |
| DELETE | /admin/input_prompt/{input_prompt_id} | delete_public_input_prompt | admin, permission | Depends, require_permission | backend/onyx/server/features/input_prompt/api.py:125 |
| PATCH | /admin/persona/{persona_id}/listed | patch_persona_visibility | admin, permission | Depends, require_permission | backend/onyx/server/features/persona/api.py:167 |
| PATCH | /admin/persona/{persona_id}/featured | patch_persona_featured_status | admin, permission | Depends, require_permission | backend/onyx/server/features/persona/api.py:204 |
| DELETE | /admin/persona/label/{label_id} | delete_label | admin, permission | Depends, require_permission | backend/onyx/server/features/persona/api.py:444 |
| GET | /user/projects/session/{chat_session_id}/token-count | get_chat_session_project_token_count | permission, user | Depends, require_permission | backend/onyx/server/features/projects/api.py:671 |
| POST | /manage/admin/doc-boosts | document_boost_update | admin, permission | Depends, require_permission | backend/onyx/server/manage/administrative.py:88 |
| POST | /manage/admin/doc-hidden | document_hidden_update | admin, permission | Depends, require_permission | backend/onyx/server/manage/administrative.py:103 |
| DELETE | /manage/admin/discord-bot/guilds/{config_id} | delete_guild_request | admin, permission | Depends, require_permission | backend/onyx/server/manage/discord_bot/api.py:221 |
| GET | /admin/image-generation/config/{image_provider_id}/credentials | get_config_credentials | admin, credential, permission | Depends, require_permission | backend/onyx/server/manage/image_generation/api.py:381 |
| DELETE | /admin/image-generation/config/{image_provider_id} | delete_config | admin, permission | Depends, require_permission | backend/onyx/server/manage/image_generation/api.py:499 |
| DELETE | /admin/image-generation/config/{image_provider_id}/default | unset_config_as_default | admin, permission | Depends, require_permission | backend/onyx/server/manage/image_generation/api.py:544 |
| GET | /admin/llm/provider/{provider_id} | get_llm_provider | admin, credential, permission | Depends, require_permission | backend/onyx/server/manage/llm/api.py:572 |
| PUT | /admin/llm/provider | put_llm_provider | admin, credential, permission | Depends, Query, require_permission | backend/onyx/server/manage/llm/api.py:590 |
| DELETE | /manage/admin/slack-app/channel/{slack_channel_config_id} | delete_slack_channel_config | admin, permission | Depends, require_permission | backend/onyx/server/manage/slack_bot.py:216 |
| DELETE | /manage/admin/slack-app/bots/{slack_bot_id} | delete_bot | admin, permission | Depends, require_permission | backend/onyx/server/manage/slack_bot.py:307 |
| GET | /manage/users/accepted | list_accepted_users | admin, group, permission, user | Depends, Query, require_permission | backend/onyx/server/manage/users.py:259 |
| PUT | /manage/admin/users | bulk_invite_users | admin, permission, user | Body, Depends, require_permission | backend/onyx/server/manage/users.py:554 |
| PATCH | /manage/admin/remove-invited-user | remove_invited_user | admin, permission, user | Depends, require_permission | backend/onyx/server/manage/users.py:734 |
| DELETE | /admin/voice/providers/{provider_id} | delete_voice_provider_endpoint | admin, permission | Depends, require_permission | backend/onyx/server/manage/voice/api.py:261 |
| PUT | /chat/rename-chat-session | rename_chat_session | permission | Depends, require_permission | backend/onyx/server/query_and_chat/chat_backend.py:550 |
| PATCH | /chat/chat-session/{session_id} | patch_chat_session | permission | Depends, require_permission | backend/onyx/server/query_and_chat/chat_backend.py:621 |
| GET | /admin/token-rate-limits/users | get_user_token_limit_settings | admin, permission, settings, user | Depends, require_permission | backend/ee/onyx/server/token_rate_limits/api.py:282 |
| POST | /manage/credential | create_credential_from_model | credential, permission | Depends, require_permission | backend/onyx/server/documents/credential.py:169 |
| POST | /search-settings/set-new-search-settings | set_new_search_settings | connector, credential, permission, settings | Depends, require_permission | backend/onyx/server/manage/search_settings.py:97 |
| PATCH | /admin/hooks/{hook_id} | update_hook | admin, permission | Depends, require_permission | backend/ee/onyx/server/features/hooks/api.py:277 |
| POST | /search/send-search-message | handle_send_search_message | permission | Depends, require_permission | backend/ee/onyx/server/query_and_chat/search_backend.py:122 |
| POST | /admin/usage-report | generate_report | admin, permission | Depends, require_permission | backend/ee/onyx/server/reporting/usage_export_api.py:37 |
| POST | /admin/token-rate-limits/global | create_global_token_limit_settings | admin, permission, settings | Depends, require_permission | backend/ee/onyx/server/token_rate_limits/api.py:63 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/get-docs-sync-status | get_docs_sync_status | admin, permission | Depends, require_permission | backend/onyx/server/documents/cc_pair.py:741 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/errors | get_cc_pair_indexing_errors | admin, permission | Depends, Query, require_permission | backend/onyx/server/documents/cc_pair.py:754 |
| GET | /document/document-size-info | get_document_info | permission, settings, user | Depends, Query, require_permission | backend/onyx/server/documents/document.py:26 |
| GET | /document/chunk-info | get_chunk_info | permission, settings, user | Depends, Query, require_permission | backend/onyx/server/documents/document.py:70 |
| POST | /approvals/{approval_id}/session-grant | submit_session_grant | permission | Depends, require_permission | backend/onyx/server/features/build/approvals/api.py:202 |
| PATCH | /apps/{external_app_id} | update_external_app_admin | admin, permission | Depends, require_permission | backend/onyx/server/features/build/external_apps/api.py:204 |
| POST | /apps/{external_app_id}/credentials | upsert_user_credentials | credential, permission, user | Depends, require_permission | backend/onyx/server/features/build/external_apps/api.py:372 |
| POST | /apps/connect/{request_id}/decision | resolve_connect_app_request | permission | Depends, require_permission | backend/onyx/server/features/build/external_apps/api.py:437 |
| POST | /apps/oauth/callback | handle_external_app_oauth_callback | credential, permission, user | Depends, require_permission | backend/onyx/server/features/build/external_apps/oauth.py:135 |
| POST | /sessions/{session_id}/restore | restore_session | permission | Depends, require_permission | backend/onyx/server/features/build/session/api.py:357 |
| POST | /sessions/{session_id}/upload | upload_file_endpoint | permission | Depends, File, require_permission | backend/onyx/server/features/build/session/api.py:768 |
| POST | /skills/custom/{skill_id}/files | upload_current_user_skill_files | permission, user | Depends, File, require_permission | backend/onyx/server/features/skill/api.py:599 |
| GET | /federated/{id}/entities | get_entities | connector, credential, permission | Depends, require_permission | backend/onyx/server/federated/api.py:114 |
| GET | /federated/{id}/credentials/schema | get_credentials_schema | connector, credential, permission | Depends, require_permission | backend/onyx/server/federated/api.py:156 |
| HEAD | /federated/{id}/entities/validate | validate_entities | connector, credential, permission | Depends, require_permission | backend/onyx/server/federated/api.py:284 |
| DELETE | /federated/{id} | delete_federated_connector_endpoint | connector, permission | Depends, require_permission | backend/onyx/server/federated/api.py:600 |
| PATCH | /manage/admin/discord-bot/guilds/{config_id} | update_guild_request | admin, permission | Depends, require_permission | backend/onyx/server/manage/discord_bot/api.py:198 |
| PATCH | /manage/admin/discord-bot/guilds/{guild_config_id}/channels/{channel_config_id} | update_channel_request | admin, permission | Depends, require_permission | backend/onyx/server/manage/discord_bot/api.py:270 |
| PUT | /admin/image-generation/config/{image_provider_id} | update_config | admin, permission | Depends, require_permission | backend/onyx/server/manage/image_generation/api.py:401 |
| GET | /admin/chat-sessions | admin_get_chat_sessions | admin, permission, user | Depends, require_permission | backend/ee/onyx/server/query_history/api.py:159 |
| POST | /manage/admin/user-group | create_user_group | admin, group, permission, user | Depends, require_permission | backend/ee/onyx/server/user_group/api.py:269 |
| POST | /manage/connector-request | submit_connector_request | connector, permission | Depends, require_permission | backend/onyx/server/documents/connector.py:1905 |
| PATCH | /admin/mcp/server/{server_id}/status | update_mcp_server_status | admin, permission | Depends, require_permission | backend/onyx/server/features/mcp/api.py:2239 |
| GET | /user/projects/session/{chat_session_id}/files | get_chat_session_project_files | permission, user | Depends, require_permission | backend/onyx/server/features/projects/api.py:699 |
| GET | /chat/get-chat-session/{session_id} | get_chat_session | permission | Depends, require_permission | backend/onyx/server/query_and_chat/chat_backend.py:354 |
| GET | /chat/file/{file_id:path} | fetch_chat_file | permission, user | Depends, Query, require_permission | backend/onyx/server/query_and_chat/chat_backend.py:1147 |
| POST | /admin/billing/seats/update | update_seats | admin, permission | Depends, require_permission | backend/ee/onyx/server/billing/api.py:358 |

# Result

**PRIVILEGED-OPERATION TEST SURFACE IDENTIFIED**
