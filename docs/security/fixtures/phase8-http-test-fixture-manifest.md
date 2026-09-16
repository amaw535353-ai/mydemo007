# Phase 8 Action 8.9 - HTTP Security Test Fixture Manifest

## Status

**PREPARED - NOT EXECUTED**

## Runtime limitation

The current Debian host does not yet provide an approved live Onyx runtime. Therefore these fixtures are request templates for later execution, not test results.

## Synthetic identities

- Alice - Tenant Alpha - ordinary user
- Bob - Tenant Alpha - ordinary user
- Carol - Tenant Beta - ordinary user
- Alpha Admin - Tenant Alpha - privileged test identity
- Anonymous - no authenticated identity

Request fixtures prepared: **80**

| Fixture | Method | Local route | Function | Recommended verification | Source |
|---|---|---|---|---|---|
| R8-001 | PUT | /manage/admin/cc-pair/{cc_pair_id}/status | update_cc_pair_status | owner-update + non-owner-update | backend/onyx/server/documents/cc_pair.py:470 |
| R8-002 | PUT | /manage/admin/credential/private-key/{credential_id} | update_credential_private_key | owner-update + non-owner-update | backend/onyx/server/documents/credential.py:329 |
| R8-003 | PUT | /manage/admin/cc-pair/{cc_pair_id}/name | update_cc_pair_name | owner-update + non-owner-update | backend/onyx/server/documents/cc_pair.py:577 |
| R8-004 | PUT | /manage/admin/cc-pair/{cc_pair_id}/property | update_cc_pair_property | owner-update + non-owner-update | backend/onyx/server/documents/cc_pair.py:611 |
| R8-005 | DELETE | /manage/admin/document-set/{document_set_id} | delete_document_set | owner-delete + non-owner-delete | backend/onyx/server/features/document_set/api.py:182 |
| R8-006 | PATCH | /manage/admin/user-group/{user_group_id}/document-sets | update_group_document_sets | owner-update + non-owner-update | backend/ee/onyx/server/user_group/api.py:527 |
| R8-007 | PUT | /manage/connector/{connector_id}/credential/{credential_id} | associate_credential_to_connector | owner-update + non-owner-update | backend/onyx/server/documents/cc_pair.py:797 |
| R8-008 | DELETE | /admin/token-rate-limits/user-group/{group_id}/rate-limit/{rate_limit_id} | delete_group_token_limit_settings | owner-delete + non-owner-delete | backend/ee/onyx/server/token_rate_limits/api.py:261 |
| R8-009 | DELETE | /manage/admin/credential/{credential_id} | delete_credential_by_id_admin | owner-delete + non-owner-delete | backend/onyx/server/documents/credential.py:103 |
| R8-010 | PUT | /admin/token-rate-limits/user-group/{group_id}/rate-limit/{rate_limit_id} | update_group_token_limit_settings | owner-update + non-owner-update | backend/ee/onyx/server/token_rate_limits/api.py:237 |
| R8-011 | PATCH | /manage/admin/document-set | patch_document_set | owner-update + non-owner-update | backend/onyx/server/features/document_set/api.py:114 |
| R8-012 | DELETE | /manage/admin/connector/{connector_id} | delete_connector_by_id | owner-delete + non-owner-delete | backend/onyx/server/documents/connector.py:1639 |
| R8-013 | PUT | /manage/admin/credential/{credential_id} | update_credential_data | owner-update + non-owner-update | backend/onyx/server/documents/credential.py:302 |
| R8-014 | PATCH | /manage/admin/connector/{connector_id} | update_connector_from_model | owner-update + non-owner-update | backend/onyx/server/documents/connector.py:1588 |
| R8-015 | DELETE | /admin/api-key/{api_key_id} | delete_api_key | owner-delete + non-owner-delete | backend/onyx/server/api_key/api.py:117 |
| R8-016 | PATCH | /admin/api-key/{api_key_id} | update_existing_api_key | owner-update + non-owner-update | backend/onyx/server/api_key/api.py:94 |
| R8-017 | DELETE | /manage/connector/{connector_id}/credential/{credential_id} | dissociate_credential_from_connector | owner-delete + non-owner-delete | backend/onyx/server/documents/cc_pair.py:925 |
| R8-018 | DELETE | /manage/credential/{credential_id} | delete_credential_by_id | owner-delete + non-owner-delete | backend/onyx/server/documents/credential.py:423 |
| R8-019 | DELETE | /manage/credential/force/{credential_id} | force_delete_credential_by_id | owner-delete + non-owner-delete | backend/onyx/server/documents/credential.py:448 |
| R8-020 | DELETE | /admin/token-rate-limits/rate-limit/{token_rate_limit_id} | delete_token_limit_settings | owner-delete + non-owner-delete | backend/ee/onyx/server/token_rate_limits/api.py:101 |
| R8-021 | DELETE | /manage/admin/user-group/{user_group_id} | delete_user_group | owner-delete + non-owner-delete | backend/ee/onyx/server/user_group/api.py:419 |
| R8-022 | PATCH | /manage/credential/{credential_id} | update_credential_from_model | owner-update + non-owner-update | backend/onyx/server/documents/credential.py:379 |
| R8-023 | PUT | /federated/{id} | update_federated_connector_endpoint | owner-update + non-owner-update | backend/onyx/server/federated/api.py:568 |
| R8-024 | PUT | /admin/token-rate-limits/rate-limit/{token_rate_limit_id} | update_token_limit_settings | owner-update + non-owner-update | backend/ee/onyx/server/token_rate_limits/api.py:82 |
| R8-025 | DELETE | /user/projects/file/{file_id} | delete_user_file | owner-delete + non-owner-delete | backend/onyx/server/features/projects/api.py:518 |
| R8-026 | DELETE | /scim/v2/Groups/{group_id} | delete_group | owner-delete + non-owner-delete | backend/ee/onyx/server/scim/api.py:1556 |
| R8-027 | PATCH | /manage/admin/user-group/{user_group_id}/incognito | patch_user_group_incognito | owner-update + non-owner-update | backend/ee/onyx/server/user_group/api.py:348 |
| R8-028 | PATCH | /manage/admin/user-group/{user_group_id} | patch_user_group | owner-update + non-owner-update | backend/ee/onyx/server/user_group/api.py:373 |
| R8-029 | PATCH | /manage/admin/user-group/{user_group_id}/agents | update_group_agents | owner-update + non-owner-update | backend/ee/onyx/server/user_group/api.py:457 |
| R8-030 | DELETE | /user-library/files/{document_id} | delete_file | owner-delete + non-owner-delete | backend/onyx/server/features/build/user_library/api.py:483 |
| R8-031 | PUT | /admin/tool/custom/{tool_id} | update_custom_tool | owner-update + non-owner-update | backend/onyx/server/features/tool/api.py:176 |
| R8-032 | PUT | /scim/v2/Groups/{group_id} | replace_group | owner-update + non-owner-update | backend/ee/onyx/server/scim/api.py:1396 |
| R8-033 | PATCH | /scim/v2/Groups/{group_id} | patch_group | owner-update + non-owner-update | backend/ee/onyx/server/scim/api.py:1463 |
| R8-034 | PATCH | /admin/sso/provider/{provider_id} | update_sso_provider_endpoint | owner-update + non-owner-update | backend/onyx/server/manage/sso/api.py:197 |
| R8-035 | PUT | /manage/admin/user-group/{user_group_id}/permissions | set_user_group_permissions | owner-update + non-owner-update | backend/ee/onyx/server/user_group/api.py:222 |
| R8-036 | PUT | /manage/admin/user-group/{user_group_id}/manager | set_group_manager | owner-update + non-owner-update | backend/ee/onyx/server/user_group/api.py:614 |
| R8-037 | DELETE | /mcp/user-credentials/{server_id} | delete_user_credentials | owner-delete + non-owner-delete | backend/onyx/server/features/mcp/api.py:1099 |
| R8-038 | DELETE | /admin/mcp/server/{server_id} | delete_mcp_server_admin | owner-delete + non-owner-delete | backend/onyx/server/features/mcp/api.py:2652 |
| R8-039 | DELETE | /admin/oauth-config/{oauth_config_id} | delete_oauth_config_endpoint | owner-delete + non-owner-delete | backend/onyx/server/features/oauth_config/api.py:174 |
| R8-040 | DELETE | /user/projects/{project_id}/files/{file_id} | unlink_user_file_from_project | owner-delete + non-owner-delete | backend/onyx/server/features/projects/api.py:280 |
| R8-041 | DELETE | /admin/tool/custom/{tool_id} | delete_custom_tool | owner-delete + non-owner-delete | backend/onyx/server/features/tool/api.py:211 |
| R8-042 | DELETE | /admin/llm/provider/{provider_id} | delete_llm_provider | owner-delete + non-owner-delete | backend/onyx/server/manage/llm/api.py:733 |
| R8-043 | PATCH | /admin/persona/{persona_id}/undelete | undelete_persona | owner-update + non-owner-update | backend/onyx/server/features/persona/api.py:312 |
| R8-044 | PUT | /scim/v2/Users/{user_id} | replace_user | owner-update + non-owner-update | backend/ee/onyx/server/scim/api.py:917 |
| R8-045 | PATCH | /scim/v2/Users/{user_id} | patch_user | owner-update + non-owner-update | backend/ee/onyx/server/scim/api.py:1006 |
| R8-046 | PATCH | /admin/mcp/server/{server_id} | update_mcp_server_simple | owner-update + non-owner-update | backend/onyx/server/features/mcp/api.py:2558 |
| R8-047 | PUT | /admin/oauth-config/{oauth_config_id} | update_oauth_config_endpoint | owner-update + non-owner-update | backend/onyx/server/features/oauth_config/api.py:138 |
| R8-048 | DELETE | /oauth-config/{oauth_config_id}/token | revoke_oauth_token | owner-delete + non-owner-delete | backend/onyx/server/features/oauth_config/api.py:298 |
| R8-049 | DELETE | /federated/{id}/oauth | disconnect_oauth_token | owner-delete + non-owner-delete | backend/onyx/server/federated/api.py:618 |
| R8-050 | DELETE | /admin/web-search/search-providers/{provider_id} | delete_search_provider | owner-delete + non-owner-delete | backend/onyx/server/manage/web_search/api.py:157 |
| R8-051 | DELETE | /admin/web-search/content-providers/{provider_id} | delete_content_provider | owner-delete + non-owner-delete | backend/onyx/server/manage/web_search/api.py:337 |
| R8-052 | DELETE | /onyx-api/ingestion/{document_id} | delete_ingestion_doc | owner-delete + non-owner-delete | backend/onyx/server/onyx_api/ingestion.py:238 |
| R8-053 | DELETE | /user/pats/{token_id} | delete_token | owner-delete + non-owner-delete | backend/onyx/server/pat/api.py:95 |
| R8-054 | DELETE | /chat/delete-chat-session/{session_id} | delete_chat_session_by_id | owner-delete + non-owner-delete | backend/onyx/server/query_and_chat/chat_backend.py:681 |
| R8-055 | DELETE | /apps/{external_app_id}/credentials | disconnect_user_from_external_app | owner-delete + non-owner-delete | backend/onyx/server/features/build/external_apps/api.py:403 |
| R8-056 | DELETE | /sessions/{session_id}/files/{path:path} | delete_file_endpoint | owner-delete + non-owner-delete | backend/onyx/server/features/build/session/api.py:819 |
| R8-057 | DELETE | /admin/hooks/{hook_id} | delete_hook | owner-delete + non-owner-delete | backend/ee/onyx/server/features/hooks/api.py:352 |
| R8-058 | DELETE | /manage/admin/standard-answer/{standard_answer_id} | delete_standard_answer | owner-delete + non-owner-delete | backend/ee/onyx/server/manage/standard_answer.py:87 |
| R8-059 | DELETE | /manage/admin/standard-answer/category/{standard_answer_category_id} | delete_standard_answer_category | owner-delete + non-owner-delete | backend/ee/onyx/server/manage/standard_answer.py:151 |
| R8-060 | DELETE | /apps/{external_app_id} | delete_external_app_admin | owner-delete + non-owner-delete | backend/onyx/server/features/build/external_apps/api.py:340 |
| R8-061 | DELETE | /admin/input_prompt/{input_prompt_id} | delete_public_input_prompt | owner-delete + non-owner-delete | backend/onyx/server/features/input_prompt/api.py:125 |
| R8-062 | PATCH | /admin/persona/{persona_id}/listed | patch_persona_visibility | owner-update + non-owner-update | backend/onyx/server/features/persona/api.py:167 |
| R8-063 | PATCH | /admin/persona/{persona_id}/featured | patch_persona_featured_status | owner-update + non-owner-update | backend/onyx/server/features/persona/api.py:204 |
| R8-064 | DELETE | /admin/persona/label/{label_id} | delete_label | owner-delete + non-owner-delete | backend/onyx/server/features/persona/api.py:444 |
| R8-065 | DELETE | /manage/admin/discord-bot/guilds/{config_id} | delete_guild_request | owner-delete + non-owner-delete | backend/onyx/server/manage/discord_bot/api.py:221 |
| R8-066 | DELETE | /admin/image-generation/config/{image_provider_id} | delete_config | owner-delete + non-owner-delete | backend/onyx/server/manage/image_generation/api.py:499 |
| R8-067 | DELETE | /admin/image-generation/config/{image_provider_id}/default | unset_config_as_default | owner-delete + non-owner-delete | backend/onyx/server/manage/image_generation/api.py:544 |
| R8-068 | DELETE | /manage/admin/slack-app/channel/{slack_channel_config_id} | delete_slack_channel_config | owner-delete + non-owner-delete | backend/onyx/server/manage/slack_bot.py:216 |
| R8-069 | DELETE | /manage/admin/slack-app/bots/{slack_bot_id} | delete_bot | owner-delete + non-owner-delete | backend/onyx/server/manage/slack_bot.py:307 |
| R8-070 | DELETE | /admin/voice/providers/{provider_id} | delete_voice_provider_endpoint | owner-delete + non-owner-delete | backend/onyx/server/manage/voice/api.py:261 |
| R8-071 | PATCH | /chat/chat-session/{session_id} | patch_chat_session | owner-update + non-owner-update | backend/onyx/server/query_and_chat/chat_backend.py:621 |
| R8-072 | PATCH | /admin/hooks/{hook_id} | update_hook | owner-update + non-owner-update | backend/ee/onyx/server/features/hooks/api.py:277 |
| R8-073 | PATCH | /apps/{external_app_id} | update_external_app_admin | owner-update + non-owner-update | backend/onyx/server/features/build/external_apps/api.py:204 |
| R8-074 | DELETE | /federated/{id} | delete_federated_connector_endpoint | owner-delete + non-owner-delete | backend/onyx/server/federated/api.py:600 |
| R8-075 | PATCH | /manage/admin/discord-bot/guilds/{config_id} | update_guild_request | owner-update + non-owner-update | backend/onyx/server/manage/discord_bot/api.py:198 |
| R8-076 | PATCH | /manage/admin/discord-bot/guilds/{guild_config_id}/channels/{channel_config_id} | update_channel_request | owner-update + non-owner-update | backend/onyx/server/manage/discord_bot/api.py:270 |
| R8-077 | PUT | /admin/image-generation/config/{image_provider_id} | update_config | owner-update + non-owner-update | backend/onyx/server/manage/image_generation/api.py:401 |
| R8-078 | PATCH | /admin/mcp/server/{server_id}/status | update_mcp_server_status | owner-update + non-owner-update | backend/onyx/server/features/mcp/api.py:2239 |
| R8-079 | DELETE | /scheduled-tasks/{task_id} | delete_task | owner-delete + non-owner-delete | backend/onyx/server/features/build/scheduled_tasks/api.py:522 |
| R8-080 | DELETE | /sessions/{session_id} | delete_session | owner-delete + non-owner-delete | backend/onyx/server/features/build/session/api.py:321 |

## Execution evidence required later

For every executed fixture record:

- exact resolved URL;
- exact synthetic actor;
- authentication state;
- object owner and tenant;
- request method;
- request parameters/body summary;
- expected ALLOW/DENY result;
- actual HTTP status;
- response evidence;
- interpretation;
- cleanup result.

# Result

**RUNTIME-READY AUTHORIZATION TEST FIXTURES PREPARED**
