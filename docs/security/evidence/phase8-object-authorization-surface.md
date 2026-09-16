# Phase 8 Action 8.7 - Object Authorization / BOLA / IDOR Surface

## Classification

These endpoints contain object-reference indicators suitable for later ownership and object-level authorization testing.

Their presence does not indicate broken authorization.

Object-reference candidates: **200**

| Method | Local route | Path parameters | ID-like function args | Function | File:line |
|---|---|---|---|---|---|
| PUT | /manage/admin/cc-pair/{cc_pair_id}/status | cc_pair_id | cc_pair_id | update_cc_pair_status | backend/onyx/server/documents/cc_pair.py:470 |
| PUT | /manage/admin/credential/private-key/{credential_id} | credential_id | credential_id, field_key, type_definition_key | update_credential_private_key | backend/onyx/server/documents/credential.py:329 |
| PUT | /manage/admin/cc-pair/{cc_pair_id}/name | cc_pair_id | cc_pair_id | update_cc_pair_name | backend/onyx/server/documents/cc_pair.py:577 |
| PUT | /manage/admin/cc-pair/{cc_pair_id}/property | cc_pair_id | cc_pair_id | update_cc_pair_property | backend/onyx/server/documents/cc_pair.py:611 |
| DELETE | /manage/admin/document-set/{document_set_id} | document_set_id | document_set_id, tenant_id | delete_document_set | backend/onyx/server/features/document_set/api.py:182 |
| PATCH | /manage/admin/user-group/{user_group_id}/document-sets | user_group_id | tenant_id, user_group_id | update_group_document_sets | backend/ee/onyx/server/user_group/api.py:527 |
| PUT | /manage/connector/{connector_id}/credential/{credential_id} | connector_id, credential_id | connector_id, credential_id, tenant_id | associate_credential_to_connector | backend/onyx/server/documents/cc_pair.py:797 |
| DELETE | /admin/token-rate-limits/user-group/{group_id}/rate-limit/{rate_limit_id} | group_id, rate_limit_id | group_id, rate_limit_id | delete_group_token_limit_settings | backend/ee/onyx/server/token_rate_limits/api.py:261 |
| DELETE | /manage/admin/credential/{credential_id} | credential_id | credential_id | delete_credential_by_id_admin | backend/onyx/server/documents/credential.py:103 |
| PUT | /admin/token-rate-limits/user-group/{group_id}/rate-limit/{rate_limit_id} | group_id, rate_limit_id | group_id, rate_limit_id | update_group_token_limit_settings | backend/ee/onyx/server/token_rate_limits/api.py:237 |
| PATCH | /manage/admin/document-set | none | tenant_id | patch_document_set | backend/onyx/server/features/document_set/api.py:114 |
| DELETE | /manage/admin/connector/{connector_id} | connector_id | connector_id | delete_connector_by_id | backend/onyx/server/documents/connector.py:1639 |
| PUT | /manage/admin/credential/{credential_id} | credential_id | credential_id | update_credential_data | backend/onyx/server/documents/credential.py:302 |
| PATCH | /manage/admin/connector/{connector_id} | connector_id | connector_id | update_connector_from_model | backend/onyx/server/documents/connector.py:1588 |
| DELETE | /admin/api-key/{api_key_id} | api_key_id | api_key_id | delete_api_key | backend/onyx/server/api_key/api.py:117 |
| PATCH | /admin/api-key/{api_key_id} | api_key_id | api_key_id | update_existing_api_key | backend/onyx/server/api_key/api.py:94 |
| DELETE | /manage/connector/{connector_id}/credential/{credential_id} | connector_id, credential_id | connector_id, credential_id | dissociate_credential_from_connector | backend/onyx/server/documents/cc_pair.py:925 |
| DELETE | /manage/credential/{credential_id} | credential_id | credential_id | delete_credential_by_id | backend/onyx/server/documents/credential.py:423 |
| DELETE | /manage/credential/force/{credential_id} | credential_id | credential_id | force_delete_credential_by_id | backend/onyx/server/documents/credential.py:448 |
| DELETE | /admin/token-rate-limits/rate-limit/{token_rate_limit_id} | token_rate_limit_id | token_rate_limit_id | delete_token_limit_settings | backend/ee/onyx/server/token_rate_limits/api.py:101 |
| DELETE | /manage/admin/user-group/{user_group_id} | user_group_id | user_group_id | delete_user_group | backend/ee/onyx/server/user_group/api.py:419 |
| PATCH | /manage/credential/{credential_id} | credential_id | credential_id | update_credential_from_model | backend/onyx/server/documents/credential.py:379 |
| PUT | /federated/{id} | id | id | update_federated_connector_endpoint | backend/onyx/server/federated/api.py:568 |
| PUT | /admin/token-rate-limits/rate-limit/{token_rate_limit_id} | token_rate_limit_id | token_rate_limit_id | update_token_limit_settings | backend/ee/onyx/server/token_rate_limits/api.py:82 |
| DELETE | /user/projects/file/{file_id} | file_id | file_id | delete_user_file | backend/onyx/server/features/projects/api.py:518 |
| DELETE | /scim/v2/Groups/{group_id} | group_id | group_id | delete_group | backend/ee/onyx/server/scim/api.py:1556 |
| PATCH | /manage/admin/user-group/{user_group_id}/incognito | user_group_id | user_group_id | patch_user_group_incognito | backend/ee/onyx/server/user_group/api.py:348 |
| PATCH | /manage/admin/user-group/{user_group_id} | user_group_id | user_group_id | patch_user_group | backend/ee/onyx/server/user_group/api.py:373 |
| PATCH | /manage/admin/user-group/{user_group_id}/agents | user_group_id | user_group_id | update_group_agents | backend/ee/onyx/server/user_group/api.py:457 |
| DELETE | /user-library/files/{document_id} | document_id | document_id | delete_file | backend/onyx/server/features/build/user_library/api.py:483 |
| PUT | /admin/tool/custom/{tool_id} | tool_id | tool_id | update_custom_tool | backend/onyx/server/features/tool/api.py:176 |
| PUT | /scim/v2/Groups/{group_id} | group_id | group_id | replace_group | backend/ee/onyx/server/scim/api.py:1396 |
| PATCH | /scim/v2/Groups/{group_id} | group_id | group_id | patch_group | backend/ee/onyx/server/scim/api.py:1463 |
| PATCH | /admin/sso/provider/{provider_id} | provider_id | provider_id | update_sso_provider_endpoint | backend/onyx/server/manage/sso/api.py:197 |
| PUT | /manage/admin/user-group/{user_group_id}/permissions | user_group_id | user_group_id | set_user_group_permissions | backend/ee/onyx/server/user_group/api.py:222 |
| PUT | /manage/admin/user-group/{user_group_id}/manager | user_group_id | user_group_id | set_group_manager | backend/ee/onyx/server/user_group/api.py:614 |
| DELETE | /mcp/user-credentials/{server_id} | server_id | server_id | delete_user_credentials | backend/onyx/server/features/mcp/api.py:1099 |
| DELETE | /admin/mcp/server/{server_id} | server_id | server_id | delete_mcp_server_admin | backend/onyx/server/features/mcp/api.py:2652 |
| DELETE | /admin/oauth-config/{oauth_config_id} | oauth_config_id | oauth_config_id | delete_oauth_config_endpoint | backend/onyx/server/features/oauth_config/api.py:174 |
| DELETE | /user/projects/{project_id}/files/{file_id} | file_id, project_id | file_id, project_id | unlink_user_file_from_project | backend/onyx/server/features/projects/api.py:280 |
| DELETE | /admin/tool/custom/{tool_id} | tool_id | tool_id | delete_custom_tool | backend/onyx/server/features/tool/api.py:211 |
| DELETE | /admin/llm/provider/{provider_id} | provider_id | provider_id | delete_llm_provider | backend/onyx/server/manage/llm/api.py:733 |
| PATCH | /admin/persona/{persona_id}/undelete | persona_id | persona_id | undelete_persona | backend/onyx/server/features/persona/api.py:312 |
| PUT | /scim/v2/Users/{user_id} | user_id | user_id | replace_user | backend/ee/onyx/server/scim/api.py:917 |
| PATCH | /scim/v2/Users/{user_id} | user_id | user_id | patch_user | backend/ee/onyx/server/scim/api.py:1006 |
| PATCH | /admin/mcp/server/{server_id} | server_id | server_id | update_mcp_server_simple | backend/onyx/server/features/mcp/api.py:2558 |
| PUT | /admin/oauth-config/{oauth_config_id} | oauth_config_id | oauth_config_id | update_oauth_config_endpoint | backend/onyx/server/features/oauth_config/api.py:138 |
| DELETE | /oauth-config/{oauth_config_id}/token | oauth_config_id | oauth_config_id | revoke_oauth_token | backend/onyx/server/features/oauth_config/api.py:298 |
| DELETE | /federated/{id}/oauth | id | id | disconnect_oauth_token | backend/onyx/server/federated/api.py:618 |
| DELETE | /admin/web-search/search-providers/{provider_id} | provider_id | provider_id | delete_search_provider | backend/onyx/server/manage/web_search/api.py:157 |
| DELETE | /admin/web-search/content-providers/{provider_id} | provider_id | provider_id | delete_content_provider | backend/onyx/server/manage/web_search/api.py:337 |
| DELETE | /onyx-api/ingestion/{document_id} | document_id | document_id | delete_ingestion_doc | backend/onyx/server/onyx_api/ingestion.py:238 |
| DELETE | /user/pats/{token_id} | token_id | token_id | delete_token | backend/onyx/server/pat/api.py:95 |
| DELETE | /chat/delete-chat-session/{session_id} | session_id | session_id | delete_chat_session_by_id | backend/onyx/server/query_and_chat/chat_backend.py:681 |
| DELETE | /apps/{external_app_id}/credentials | external_app_id | external_app_id | disconnect_user_from_external_app | backend/onyx/server/features/build/external_apps/api.py:403 |
| DELETE | /sessions/{session_id}/files/{path:path} | path, session_id | session_id | delete_file_endpoint | backend/onyx/server/features/build/session/api.py:819 |
| DELETE | /admin/hooks/{hook_id} | hook_id | hook_id | delete_hook | backend/ee/onyx/server/features/hooks/api.py:352 |
| DELETE | /manage/admin/standard-answer/{standard_answer_id} | standard_answer_id | standard_answer_id | delete_standard_answer | backend/ee/onyx/server/manage/standard_answer.py:87 |
| DELETE | /manage/admin/standard-answer/category/{standard_answer_category_id} | standard_answer_category_id | standard_answer_category_id | delete_standard_answer_category | backend/ee/onyx/server/manage/standard_answer.py:151 |
| DELETE | /apps/{external_app_id} | external_app_id | external_app_id | delete_external_app_admin | backend/onyx/server/features/build/external_apps/api.py:340 |
| DELETE | /admin/input_prompt/{input_prompt_id} | input_prompt_id | input_prompt_id | delete_public_input_prompt | backend/onyx/server/features/input_prompt/api.py:125 |
| PATCH | /admin/persona/{persona_id}/listed | persona_id | persona_id | patch_persona_visibility | backend/onyx/server/features/persona/api.py:167 |
| PATCH | /admin/persona/{persona_id}/featured | persona_id | persona_id | patch_persona_featured_status | backend/onyx/server/features/persona/api.py:204 |
| DELETE | /admin/persona/label/{label_id} | label_id | label_id | delete_label | backend/onyx/server/features/persona/api.py:444 |
| DELETE | /manage/admin/discord-bot/guilds/{config_id} | config_id | config_id | delete_guild_request | backend/onyx/server/manage/discord_bot/api.py:221 |
| DELETE | /admin/image-generation/config/{image_provider_id} | image_provider_id | image_provider_id | delete_config | backend/onyx/server/manage/image_generation/api.py:499 |
| DELETE | /admin/image-generation/config/{image_provider_id}/default | image_provider_id | image_provider_id | unset_config_as_default | backend/onyx/server/manage/image_generation/api.py:544 |
| DELETE | /manage/admin/slack-app/channel/{slack_channel_config_id} | slack_channel_config_id | slack_channel_config_id | delete_slack_channel_config | backend/onyx/server/manage/slack_bot.py:216 |
| DELETE | /manage/admin/slack-app/bots/{slack_bot_id} | slack_bot_id | slack_bot_id | delete_bot | backend/onyx/server/manage/slack_bot.py:307 |
| DELETE | /admin/voice/providers/{provider_id} | provider_id | provider_id | delete_voice_provider_endpoint | backend/onyx/server/manage/voice/api.py:261 |
| PATCH | /chat/chat-session/{session_id} | session_id | session_id | patch_chat_session | backend/onyx/server/query_and_chat/chat_backend.py:621 |
| PATCH | /admin/hooks/{hook_id} | hook_id | hook_id | update_hook | backend/ee/onyx/server/features/hooks/api.py:277 |
| PATCH | /apps/{external_app_id} | external_app_id | external_app_id | update_external_app_admin | backend/onyx/server/features/build/external_apps/api.py:204 |
| DELETE | /federated/{id} | id | id | delete_federated_connector_endpoint | backend/onyx/server/federated/api.py:600 |
| PATCH | /manage/admin/discord-bot/guilds/{config_id} | config_id | config_id | update_guild_request | backend/onyx/server/manage/discord_bot/api.py:198 |
| PATCH | /manage/admin/discord-bot/guilds/{guild_config_id}/channels/{channel_config_id} | channel_config_id, guild_config_id | channel_config_id, guild_config_id | update_channel_request | backend/onyx/server/manage/discord_bot/api.py:270 |
| PUT | /admin/image-generation/config/{image_provider_id} | image_provider_id | image_provider_id | update_config | backend/onyx/server/manage/image_generation/api.py:401 |
| PATCH | /admin/mcp/server/{server_id}/status | server_id | server_id | update_mcp_server_status | backend/onyx/server/features/mcp/api.py:2239 |
| DELETE | /scheduled-tasks/{task_id} | task_id | task_id | delete_task | backend/onyx/server/features/build/scheduled_tasks/api.py:522 |
| DELETE | /sessions/{session_id} | session_id | session_id | delete_session | backend/onyx/server/features/build/session/api.py:321 |
| DELETE | /input_prompt/{input_prompt_id} | input_prompt_id | input_prompt_id | delete_input_prompt | backend/onyx/server/features/input_prompt/api.py:107 |
| DELETE | /persona/{persona_id} | persona_id | persona_id | delete_persona | backend/onyx/server/features/persona/api.py:580 |
| DELETE | /user/projects/{project_id} | project_id | project_id | delete_project | backend/onyx/server/features/projects/api.py:490 |
| DELETE | /skills/custom/{skill_id}/files | skill_id | skill_id | remove_current_user_skill_file | backend/onyx/server/features/skill/api.py:627 |
| PATCH | /skills/custom/{skill_id}/share | skill_id | skill_id | share_current_user_skill | backend/onyx/server/features/skill/api.py:786 |
| DELETE | /skills/custom/{skill_id} | skill_id | skill_id | delete_current_user_skill | backend/onyx/server/features/skill/api.py:938 |
| PUT | /skills/custom/{skill_id}/bundle | skill_id | skill_id | replace_current_user_skill_bundle | backend/onyx/server/features/skill/api.py:554 |
| PATCH | /manage/admin/standard-answer/{standard_answer_id} | standard_answer_id | standard_answer_id | patch_standard_answer | backend/ee/onyx/server/manage/standard_answer.py:60 |
| PATCH | /manage/admin/standard-answer/category/{standard_answer_category_id} | standard_answer_category_id | standard_answer_category_id | patch_standard_answer_category | backend/ee/onyx/server/manage/standard_answer.py:126 |
| PUT | /sessions/{session_id}/name | session_id | session_id | update_session_name | backend/onyx/server/features/build/session/api.py:282 |
| PATCH | /input_prompt/{input_prompt_id} | input_prompt_id | input_prompt_id | patch_input_prompt | backend/onyx/server/features/input_prompt/api.py:83 |
| PATCH | /persona/{persona_id} | persona_id | persona_id | update_persona | backend/onyx/server/features/persona/api.py:374 |
| PATCH | /admin/persona/label/{label_id} | label_id | label_id | patch_persona_label | backend/onyx/server/features/persona/api.py:430 |
| PATCH | /user/projects/{project_id} | project_id | project_id | update_project | backend/onyx/server/features/projects/api.py:462 |
| PUT | /search-settings/upsert-unstructured-api-key | none | unstructured_api_key | upsert_unstructured_api_key | backend/onyx/server/manage/search_settings.py:714 |
| PATCH | /manage/admin/slack-app/channel/{slack_channel_config_id} | slack_channel_config_id | slack_channel_config_id | patch_slack_channel_config | backend/onyx/server/manage/slack_bot.py:154 |
| PATCH | /manage/admin/slack-app/bots/{slack_bot_id} | slack_bot_id | slack_bot_id | patch_bot | backend/onyx/server/manage/slack_bot.py:285 |
| PATCH | /user/assistant-list/update/{assistant_id} | assistant_id | assistant_id | update_user_assistant_visibility_api | backend/onyx/server/manage/users.py:1400 |
| PATCH | /user/assistant/{assistant_id}/preferences | assistant_id | assistant_id | update_assistant_preferences_for_user_api | backend/onyx/server/manage/users.py:1439 |
| DELETE | /scim/v2/Users/{user_id} | user_id | user_id | delete_user | backend/ee/onyx/server/scim/api.py:1156 |
| DELETE | /persona/{persona_id}/share/me | persona_id | persona_id | leave_persona_shares | backend/onyx/server/features/persona/api.py:563 |
| PATCH | /scheduled-tasks/{task_id} | task_id | task_id | patch_task | backend/onyx/server/features/build/scheduled_tasks/api.py:469 |
| PATCH | /sessions/{session_id}/public | session_id | session_id | set_session_public | backend/onyx/server/features/build/session/api.py:302 |
| PATCH | /persona/{persona_id}/public | persona_id | persona_id | patch_user_persona_public_status | backend/onyx/server/features/persona/api.py:182 |
| PATCH | /persona/{persona_id}/share | persona_id | persona_id | share_persona | backend/onyx/server/features/persona/api.py:486 |
| PUT | /skills/{skill_id}/enabled | skill_id | skill_id | set_skill_enabled_for_current_user | backend/onyx/server/features/skill/api.py:190 |
| PATCH | /skills/custom/{skill_id} | skill_id | skill_id | patch_current_user_skill | backend/onyx/server/features/skill/api.py:655 |
| DELETE | /chat/remove-chat-message-feedback | none | chat_message_id | remove_chat_feedback | backend/onyx/server/query_and_chat/chat_backend.py:1021 |
| POST | /manage/admin/cc-pair/{cc_pair_id}/sync-groups | cc_pair_id | cc_pair_id | sync_cc_pair_groups | backend/ee/onyx/server/documents/cc_pair.py:135 |
| GET | /manage/admin/cc-pair/{cc_pair_id} | cc_pair_id | cc_pair_id | get_cc_pair_full_info | backend/onyx/server/documents/cc_pair.py:338 |
| POST | /manage/admin/cc-pair/{cc_pair_id}/sync-permissions | cc_pair_id | cc_pair_id | sync_cc_pair | backend/ee/onyx/server/documents/cc_pair.py:56 |
| POST | /manage/admin/cc-pair/{cc_pair_id}/prune | cc_pair_id | cc_pair_id | prune_cc_pair | backend/onyx/server/documents/cc_pair.py:685 |
| POST | /manage/admin/connector/{connector_id}/files/update | connector_id | connector_id | update_connector_files | backend/onyx/server/documents/connector.py:559 |
| POST | /manage/credential/private-key | none | field_key, type_definition_key | create_credential_with_private_key | backend/onyx/server/documents/credential.py:197 |
| GET | /manage/admin/connector/google-drive/check-auth/{credential_id} | credential_id | credential_id | check_drive_tokens | backend/onyx/server/documents/connector.py:222 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/sync-groups | cc_pair_id | cc_pair_id | get_cc_pair_latest_group_sync | backend/ee/onyx/server/documents/cc_pair.py:112 |
| POST | /manage/admin/credential/{credential_id}/capability-check | credential_id | credential_id | trigger_capability_check | backend/onyx/server/documents/credential_capabilities.py:134 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/sync-permissions | cc_pair_id | cc_pair_id | get_cc_pair_latest_sync | backend/ee/onyx/server/documents/cc_pair.py:33 |
| POST | /connector/confluence/callback | none | tenant_id | confluence_oauth_callback | backend/ee/onyx/server/oauth/confluence_cloud.py:146 |
| GET | /manage/admin/credential/{credential_id}/capability-report | credential_id | connector_id, credential_id | get_capability_report | backend/onyx/server/documents/credential_capabilities.py:263 |
| POST | /admin/token-rate-limits/user-group/{group_id} | group_id | group_id | create_group_token_limit_settings | backend/ee/onyx/server/token_rate_limits/api.py:158 |
| GET | /connector/oauth/callback/{source} | source | none | oauth_callback | backend/onyx/server/documents/standard_oauth.py:242 |
| GET | /manage/admin/connector/{connector_id}/files | connector_id | connector_id | list_connector_files | backend/onyx/server/documents/connector.py:442 |
| POST | /connector/confluence/finalize | none | cloud_id, credential_id, tenant_id | confluence_oauth_finalize | backend/ee/onyx/server/oauth/confluence_cloud.py:323 |
| GET | /admin/token-rate-limits/user-group/{group_id} | group_id | group_id | get_group_token_limit_settings | backend/ee/onyx/server/token_rate_limits/api.py:138 |
| POST | /connector/google-drive/callback | none | tenant_id | handle_google_drive_oauth_callback | backend/ee/onyx/server/oauth/google_drive.py:111 |
| POST | /connector/slack/callback | none | tenant_id | handle_slack_oauth_callback | backend/ee/onyx/server/oauth/slack.py:100 |
| POST | /manage/admin/document-set | none | tenant_id | create_document_set | backend/onyx/server/features/document_set/api.py:48 |
| GET | /manage/connector/gmail/authorize/{credential_id} | credential_id | credential_id | gmail_auth | backend/onyx/server/documents/connector.py:1746 |
| GET | /manage/connector/google-drive/authorize/{credential_id} | credential_id | credential_id | google_drive_auth | backend/onyx/server/documents/connector.py:1767 |
| POST | /admin/api-key/{api_key_id}/regenerate | api_key_id | api_key_id | regenerate_existing_api_key | backend/onyx/server/api_key/api.py:75 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/external-group-sync-attempts | cc_pair_id | cc_pair_id | get_cc_pair_external_group_sync_attempts | backend/onyx/server/documents/cc_pair.py:285 |
| GET | /manage/admin/document-set/{document_set_id} | document_set_id | document_set_id | get_document_set | backend/onyx/server/features/document_set/api.py:231 |
| GET | /connector/confluence/accessible-resources | none | credential_id, tenant_id | confluence_oauth_accessible_resources | backend/ee/onyx/server/oauth/confluence_cloud.py:259 |
| GET | /manage/admin/similar-credentials/{source_type} | source_type | none | get_cc_source_full_info | backend/onyx/server/documents/credential.py:80 |
| GET | /apps/{external_app_id}/oauth/start | external_app_id | external_app_id | start_external_app_oauth | backend/onyx/server/features/build/external_apps/oauth.py:85 |
| POST | /sessions/{session_id}/subagents/{subagent_session_id}/send-message | session_id, subagent_session_id | session_id, subagent_session_id | send_subagent_message | backend/onyx/server/features/build/session/messages.py:221 |
| POST | /manage/admin/user-group/{user_group_id}/add-users | user_group_id | user_group_id | add_users | backend/ee/onyx/server/user_group/api.py:396 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/index-attempts | cc_pair_id | cc_pair_id | get_cc_pair_index_attempts | backend/onyx/server/documents/cc_pair.py:118 |
| GET | /manage/admin/index-attempt/{index_attempt_id}/stage-metrics | index_attempt_id | index_attempt_id | get_index_attempt_stage_metrics | backend/onyx/server/documents/cc_pair.py:160 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/permission-sync-attempts | cc_pair_id | cc_pair_id | get_cc_pair_permission_sync_attempts | backend/onyx/server/documents/cc_pair.py:235 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/last_pruned | cc_pair_id | cc_pair_id | get_cc_pair_last_pruned | backend/onyx/server/documents/cc_pair.py:667 |
| GET | /manage/credential/{credential_id} | credential_id | credential_id | get_credential_by_id | backend/onyx/server/documents/credential.py:279 |
| GET | /manage/admin/indexing/targeted-reindex/{job_id} | job_id | job_id | get_targeted_reindex_status | backend/onyx/server/documents/targeted_reindex.py:172 |
| GET | /federated/{id}/authorize | id | id | get_authorize_url | backend/onyx/server/federated/api.py:328 |
| GET | /federated/{id} | id | id | get_federated_connector_detail | backend/onyx/server/federated/api.py:522 |
| GET | /onyx-api/connector-docs/{cc_pair_id} | cc_pair_id | cc_pair_id | get_docs_by_connector_credential_pair | backend/onyx/server/onyx_api/ingestion.py:59 |
| POST | /chat/end-incognito-session/{session_id} | session_id | session_id | end_incognito_session | backend/onyx/server/query_and_chat/chat_backend.py:730 |
| GET | /admin/api-key/{api_key_id} | api_key_id | api_key_id | get_api_key | backend/onyx/server/api_key/api.py:39 |
| POST | /user/projects/{project_id}/files/{file_id} | file_id, project_id | file_id, project_id | link_user_file_to_project | backend/onyx/server/features/projects/api.py:325 |
| GET | /chat/max-selected-document-tokens | none | persona_id | get_max_document_tokens | backend/onyx/server/query_and_chat/chat_backend.py:1040 |
| POST | /admin/hooks/{hook_id}/activate | hook_id | hook_id | activate_hook | backend/ee/onyx/server/features/hooks/api.py:363 |
| GET | /manage/admin/user-group/{user_group_id} | user_group_id | user_group_id | get_user_group | backend/ee/onyx/server/user_group/api.py:137 |
| GET | /manage/admin/user-group/{user_group_id}/permissions | user_group_id | user_group_id | get_user_group_permissions | backend/ee/onyx/server/user_group/api.py:202 |
| GET | /persona/{persona_id} | persona_id | persona_id | get_persona | backend/onyx/server/features/persona/api.py:696 |
| GET | /chat/chat-session/{session_id}/resume-stream | session_id | session_id | resume_chat_stream | backend/onyx/server/query_and_chat/chat_backend.py:1292 |
| POST | /prepare-authorization-request | none | tenant_id | prepare_authorization_request | backend/ee/onyx/server/oauth/api.py:24 |
| POST | /sessions/{session_id}/snapshot | session_id | session_id | create_session_snapshot | backend/onyx/server/features/build/session/api.py:436 |
| POST | /sessions/{session_id}/opencode-history-snapshot | session_id | session_id | create_session_opencode_history_snapshot | backend/onyx/server/features/build/session/api.py:471 |
| GET | /user/projects/session/{chat_session_id}/token-count | chat_session_id | chat_session_id | get_chat_session_project_token_count | backend/onyx/server/features/projects/api.py:671 |
| GET | /admin/image-generation/config/{image_provider_id}/credentials | image_provider_id | image_provider_id | get_config_credentials | backend/onyx/server/manage/image_generation/api.py:381 |
| GET | /admin/llm/provider/{provider_id} | provider_id | provider_id | get_llm_provider | backend/onyx/server/manage/llm/api.py:572 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/get-docs-sync-status | cc_pair_id | cc_pair_id | get_docs_sync_status | backend/onyx/server/documents/cc_pair.py:741 |
| GET | /manage/admin/cc-pair/{cc_pair_id}/errors | cc_pair_id | cc_pair_id | get_cc_pair_indexing_errors | backend/onyx/server/documents/cc_pair.py:754 |
| GET | /document/document-size-info | none | document_id | get_document_info | backend/onyx/server/documents/document.py:26 |
| GET | /document/chunk-info | none | chunk_id, document_id | get_chunk_info | backend/onyx/server/documents/document.py:70 |
| POST | /approvals/{approval_id}/session-grant | approval_id | approval_id | submit_session_grant | backend/onyx/server/features/build/approvals/api.py:202 |
| POST | /apps/{external_app_id}/credentials | external_app_id | external_app_id | upsert_user_credentials | backend/onyx/server/features/build/external_apps/api.py:372 |
| POST | /apps/connect/{request_id}/decision | request_id | request_id | resolve_connect_app_request | backend/onyx/server/features/build/external_apps/api.py:437 |
| POST | /sessions/{session_id}/restore | session_id | session_id | restore_session | backend/onyx/server/features/build/session/api.py:357 |
| POST | /sessions/{session_id}/upload | session_id | session_id | upload_file_endpoint | backend/onyx/server/features/build/session/api.py:768 |
| POST | /skills/custom/{skill_id}/files | skill_id | skill_id | upload_current_user_skill_files | backend/onyx/server/features/skill/api.py:599 |
| GET | /federated/{id}/entities | id | id | get_entities | backend/onyx/server/federated/api.py:114 |
| GET | /federated/{id}/credentials/schema | id | id | get_credentials_schema | backend/onyx/server/federated/api.py:156 |
| GET | /admin/chat-sessions | none | user_id | admin_get_chat_sessions | backend/ee/onyx/server/query_history/api.py:159 |
| GET | /user/projects/session/{chat_session_id}/files | chat_session_id | chat_session_id | get_chat_session_project_files | backend/onyx/server/features/projects/api.py:699 |
| GET | /chat/get-chat-session/{session_id} | session_id | session_id | get_chat_session | backend/onyx/server/query_and_chat/chat_backend.py:354 |
| GET | /chat/file/{file_id:path} | file_id | file_id | fetch_chat_file | backend/onyx/server/query_and_chat/chat_backend.py:1147 |
| GET | /admin/chat-session-history/{chat_session_id} | chat_session_id | chat_session_id | get_chat_session_admin | backend/ee/onyx/server/query_history/api.py:248 |
| GET | /manage/connector/{connector_id} | connector_id | connector_id | get_connector_by_id | backend/onyx/server/documents/connector.py:1876 |
| GET | /sessions/{session_id}/turns/{turn_id}/events | session_id, turn_id | session_id, turn_id | get_interactive_turn_events | backend/onyx/server/features/build/interactive_turns/api.py:129 |
| GET | /sessions/{session_id}/scheduled-run-events | session_id | session_id | get_session_scheduled_run_events | backend/onyx/server/features/build/session/api.py:923 |
| GET | /admin/mcp/servers/{server_id} | server_id | server_id | get_mcp_server_detail | backend/onyx/server/features/mcp/api.py:2172 |
| GET | /admin/oauth-config/{oauth_config_id} | oauth_config_id | oauth_config_id | get_oauth_config_endpoint | backend/onyx/server/features/oauth_config/api.py:119 |
| POST | /admin/web-search/search-providers/{provider_id}/activate | provider_id | provider_id | activate_search_provider | backend/onyx/server/manage/web_search/api.py:167 |
| POST | /admin/web-search/search-providers/{provider_id}/deactivate | provider_id | provider_id | deactivate_search_provider | backend/onyx/server/manage/web_search/api.py:189 |
| POST | /admin/web-search/content-providers/{provider_id}/activate | provider_id | provider_id | activate_content_provider | backend/onyx/server/manage/web_search/api.py:347 |
| POST | /admin/web-search/content-providers/{provider_id}/deactivate | provider_id | provider_id | deactivate_content_provider | backend/onyx/server/manage/web_search/api.py:384 |
| POST | /user/projects/{project_id}/move_chat_session | project_id | project_id | move_chat_session | backend/onyx/server/features/projects/api.py:632 |
| GET | /user/projects/{project_id}/token-count | project_id | project_id | get_project_total_token_count | backend/onyx/server/features/projects/api.py:737 |
| POST | /chat/stop-chat-session/{chat_session_id} | chat_session_id | chat_session_id | stop_chat_session | backend/onyx/server/query_and_chat/chat_backend.py:1372 |
| GET | /sessions/{session_id} | session_id | session_id | get_session_details | backend/onyx/server/features/build/session/api.py:165 |
| POST | /user/projects/file/upload | none | incognito_session_id, project_id | upload_user_files | backend/onyx/server/features/projects/api.py:175 |
| GET | /manage/admin/indexing/failed-documents | none | cc_pair_id | get_failed_documents | backend/onyx/server/manage/administrative.py:233 |
| POST | /admin/hooks/{hook_id}/validate | hook_id | hook_id | validate_hook | backend/ee/onyx/server/features/hooks/api.py:405 |
| POST | /admin/hooks/{hook_id}/deactivate | hook_id | hook_id | deactivate_hook | backend/ee/onyx/server/features/hooks/api.py:433 |
| POST | /admin/image-generation/config/{image_provider_id}/default | image_provider_id | image_provider_id | set_config_as_default | backend/onyx/server/manage/image_generation/api.py:531 |
| GET | /llm/persona/{persona_id}/providers | persona_id | persona_id | list_llm_providers_for_persona | backend/onyx/server/manage/llm/api.py:1053 |
| POST | /admin/sso/provider/{provider_id}/enabled | provider_id | provider_id | set_sso_provider_enabled_endpoint | backend/onyx/server/manage/sso/api.py:237 |
| POST | /admin/voice/providers/{provider_id}/activate-stt | provider_id | provider_id | activate_stt_provider_endpoint | backend/onyx/server/manage/voice/api.py:273 |

## Later testing model

For each selected object route, establish a positive control with the owner, then repeat with a different synthetic user and, where applicable, a different synthetic tenant.

# Result

**OBJECT-AUTHORIZATION TEST SURFACE IDENTIFIED**
