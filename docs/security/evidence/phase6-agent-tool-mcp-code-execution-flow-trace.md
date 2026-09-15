# Phase 6 Action 6.8 - Agent, Tool, MCP and Code-Execution Flow Trace
## Purpose
Trace security-critical capability execution through the exact pinned Onyx
source revision.
Target model:
model decision -> tool selection -> authorization/availability -> argument
parsing -> identity/credential context -> execution -> result -> model context.
MCP and code-interpreter execution surfaces are traced separately.
This action is static source analysis only.
## Verified Baseline
- Evidence branch: `security/phase-6-onyx-baseline`
- Action 6.7 parent: `6e64beacb3162d62cf108ec9fc3b70c0730bb633`
- Onyx repository: `https://github.com/onyx-dot-app/onyx.git`
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx source clean: PASS
## Capability Source Inventory
Captured paths: 307
```text
.cursor/mcp.json
.mcp.json
backend/alembic/versions/07b98176f1de_code_interpreter_seed.py
backend/alembic/versions/2a391f840e85_add_last_refreshed_at_mcp_server.py
backend/alembic/versions/33cb72ea4d80_single_tool_call_per_message.py
backend/alembic/versions/3879338f8ba1_add_tool_table.py
backend/alembic/versions/3a9b8d7c6e5f_add_mcp_known_provider_fields.py
backend/alembic/versions/4cebcbc9b2ae_add_tab_index_to_tool_call.py
backend/alembic/versions/565c5b57a573_add_available_in_craft_to_mcp_server.py
backend/alembic/versions/57122d037335_add_python_tool_on_default.py
backend/alembic/versions/7cb492013621_code_interpreter_server_model.py
backend/alembic/versions/7ed603b64d5a_add_mcp_server_and_connection_config_.py
backend/alembic/versions/904451035c9b_store_tool_details.py
backend/alembic/versions/96a5702df6aa_mcp_tool_enabled.py
backend/alembic/versions/a01bf2971c5d_update_default_tool_descriptions.py
backend/alembic/versions/b30353be4eec_add_mcp_auth_performer.py
backend/alembic/versions/b7e9a3c1d2f4_add_is_public_to_mcp_server.py
backend/alembic/versions/d25168c2beee_tool_name_consistency.py
backend/alembic/versions/dba7f71618f5_onyx_custom_tool_flow.py
backend/alembic/versions/e2875ce6454b_rename_python_tool_llm_facing_name.py
backend/alembic/versions/e8f0d2a38171_add_status_to_mcp_server_and_make_auth_.py
backend/alembic/versions/fe958f19e42b_add_mcp_config_hash_to_sandbox_and_.py
backend/ee/onyx/db/mcp.py
backend/ee/onyx/server/manage/standard_answer.py
backend/onyx/chat/COMPRESSION.md
backend/onyx/chat/README.md
backend/onyx/chat/__init__.py
backend/onyx/chat/chat_processing_checker.py
backend/onyx/chat/chat_state.py
backend/onyx/chat/chat_utils.py
backend/onyx/chat/citation_processor.py
backend/onyx/chat/citation_utils.py
backend/onyx/chat/compression.py
backend/onyx/chat/emitter.py
backend/onyx/chat/incognito.py
backend/onyx/chat/incognito_context.py
backend/onyx/chat/llm_loop.py
backend/onyx/chat/llm_step.py
backend/onyx/chat/models.py
backend/onyx/chat/process_message.py
backend/onyx/chat/prompt_utils.py
backend/onyx/chat/save_chat.py
backend/onyx/chat/stop_signal_checker.py
backend/onyx/chat/stream_buffer.py
backend/onyx/chat/token_budget.py
backend/onyx/chat/tool_call_args_streaming.py
backend/onyx/configs/tool_configs.py
backend/onyx/db/code_interpreter.py
backend/onyx/db/mcp.py
backend/onyx/mcp_server/README.md
backend/onyx/mcp_server/api.py
backend/onyx/mcp_server/auth.py
backend/onyx/mcp_server/mcp.json.template
backend/onyx/mcp_server/resources/__init__.py
backend/onyx/mcp_server/resources/agents.py
backend/onyx/mcp_server/resources/document_sets.py
backend/onyx/mcp_server/resources/indexed_sources.py
backend/onyx/mcp_server/tools/__init__.py
backend/onyx/mcp_server/tools/search.py
backend/onyx/mcp_server/utils.py
backend/onyx/mcp_server_main.py
backend/onyx/prompts/deep_research/dr_tool_prompts.py
backend/onyx/prompts/tool_prompts.py
backend/onyx/sandbox_proxy/mcp_jsonrpc.py
backend/onyx/sandbox_proxy/resolvers/mcp_matching.py
backend/onyx/sandbox_proxy/resolvers/mcp_server.py
backend/onyx/server/features/build/sandbox/util/mcp_config.py
backend/onyx/server/features/mcp/api.py
backend/onyx/server/features/mcp/client.py
backend/onyx/server/features/mcp/client_metadata.py
backend/onyx/server/features/mcp/credentials.py
backend/onyx/server/features/mcp/models.py
backend/onyx/server/features/mcp/oauth.py
backend/onyx/server/features/mcp/oauth_flow.py
backend/onyx/server/features/mcp/ssrf.py
backend/onyx/server/features/tool/tool_visibility.py
backend/onyx/server/manage/__init__.py
backend/onyx/server/manage/administrative.py
backend/onyx/server/manage/code_interpreter/__init__.py
backend/onyx/server/manage/code_interpreter/api.py
backend/onyx/server/manage/code_interpreter/models.py
backend/onyx/server/manage/discord_bot/api.py
backend/onyx/server/manage/discord_bot/models.py
backend/onyx/server/manage/discord_bot/utils.py
backend/onyx/server/manage/embedding/api.py
backend/onyx/server/manage/embedding/models.py
backend/onyx/server/manage/get_state.py
backend/onyx/server/manage/image_generation/api.py
backend/onyx/server/manage/image_generation/models.py
backend/onyx/server/manage/invite_rate_limit.py
backend/onyx/server/manage/llm/api.py
backend/onyx/server/manage/llm/models.py
backend/onyx/server/manage/llm/provider_cache.py
backend/onyx/server/manage/llm/utils.py
backend/onyx/server/manage/models.py
backend/onyx/server/manage/oauth_test.py
backend/onyx/server/manage/opensearch_migration/api.py
backend/onyx/server/manage/opensearch_migration/models.py
backend/onyx/server/manage/search_settings.py
backend/onyx/server/manage/slack_bot.py
backend/onyx/server/manage/sso/__init__.py
backend/onyx/server/manage/sso/api.py
backend/onyx/server/manage/sso/models.py
backend/onyx/server/manage/tracing/__init__.py
backend/onyx/server/manage/tracing/api.py
backend/onyx/server/manage/tracing/models.py
backend/onyx/server/manage/users.py
backend/onyx/server/manage/validate_tokens.py
backend/onyx/server/manage/voice/__init__.py
backend/onyx/server/manage/voice/api.py
backend/onyx/server/manage/voice/models.py
backend/onyx/server/manage/voice/text_utils.py
backend/onyx/server/manage/voice/user_api.py
backend/onyx/server/manage/voice/websocket_api.py
backend/onyx/server/manage/web_search/api.py
backend/onyx/server/manage/web_search/models.py
backend/onyx/server/metrics/mcp_client.py
backend/onyx/server/metrics/mcp_common.py
backend/onyx/server/metrics/mcp_server.py
backend/onyx/tools/built_in_tools.py
backend/onyx/tools/constants.py
backend/onyx/tools/fake_tools/__init__.py
backend/onyx/tools/fake_tools/coding_agent.py
backend/onyx/tools/fake_tools/research_agent.py
backend/onyx/tools/interface.py
backend/onyx/tools/models.py
backend/onyx/tools/tool_constructor.py
backend/onyx/tools/tool_implementations/bash/__init__.py
backend/onyx/tools/tool_implementations/bash/bash_tool.py
backend/onyx/tools/tool_implementations/coding_agent/__init__.py
backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py
backend/onyx/tools/tool_implementations/custom/base_tool_types.py
backend/onyx/tools/tool_implementations/custom/custom_tool.py
backend/onyx/tools/tool_implementations/custom/openapi_parsing.py
backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py
backend/onyx/tools/tool_implementations/images/image_generation_tool.py
backend/onyx/tools/tool_implementations/images/models.py
backend/onyx/tools/tool_implementations/knowledge_graph/knowledge_graph_tool.py
backend/onyx/tools/tool_implementations/mcp/mcp_tool.py
backend/onyx/tools/tool_implementations/memory/__init__.py
backend/onyx/tools/tool_implementations/memory/memory_tool.py
backend/onyx/tools/tool_implementations/memory/models.py
backend/onyx/tools/tool_implementations/open_url/__init__.py
backend/onyx/tools/tool_implementations/open_url/firecrawl.py
backend/onyx/tools/tool_implementations/open_url/models.py
backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py
backend/onyx/tools/tool_implementations/open_url/open_url_tool.py
backend/onyx/tools/tool_implementations/open_url/snippet_matcher.py
backend/onyx/tools/tool_implementations/open_url/tavily.py
backend/onyx/tools/tool_implementations/open_url/url_normalization.py
backend/onyx/tools/tool_implementations/open_url/utils.py
backend/onyx/tools/tool_implementations/python/__init__.py
backend/onyx/tools/tool_implementations/python/code_interpreter_client.py
backend/onyx/tools/tool_implementations/python/python_tool.py
backend/onyx/tools/tool_implementations/search/constants.py
backend/onyx/tools/tool_implementations/search/search_tool.py
backend/onyx/tools/tool_implementations/search/search_utils.py
backend/onyx/tools/tool_implementations/search_like_tool_utils.py
backend/onyx/tools/tool_implementations/utils.py
backend/onyx/tools/tool_implementations/web_search/clients/brave_client.py
backend/onyx/tools/tool_implementations/web_search/clients/exa_client.py
backend/onyx/tools/tool_implementations/web_search/clients/google_pse_client.py
backend/onyx/tools/tool_implementations/web_search/clients/searxng_client.py
backend/onyx/tools/tool_implementations/web_search/clients/serper_client.py
backend/onyx/tools/tool_implementations/web_search/clients/tavily_client.py
backend/onyx/tools/tool_implementations/web_search/models.py
backend/onyx/tools/tool_implementations/web_search/providers.py
backend/onyx/tools/tool_implementations/web_search/utils.py
backend/onyx/tools/tool_implementations/web_search/web_search_tool.py
backend/onyx/tools/tool_name.py
backend/onyx/tools/tool_runner.py
backend/onyx/tools/utils.py
backend/tests/external_dependency_unit/craft/test_mcp_config_resolution.py
backend/tests/external_dependency_unit/db/test_agent_editor_tool_visibility.py
backend/tests/external_dependency_unit/mcp/test_craft_admin_api.py
backend/tests/external_dependency_unit/mcp/test_mcp_oauth_dead_grant.py
backend/tests/external_dependency_unit/sandbox_proxy/test_mcp_approval_evaluator.py
backend/tests/external_dependency_unit/sandbox_proxy/test_mcp_approval_pipeline.py
backend/tests/external_dependency_unit/sandbox_proxy/test_mcp_server_resolver.py
backend/tests/external_dependency_unit/server/features/mcp/test_mcp_access_control.py
backend/tests/external_dependency_unit/server/features/mcp/test_mcp_access_edge_cases.py
backend/tests/external_dependency_unit/server/features/mcp/test_mcp_grant_reconciliation.py
backend/tests/external_dependency_unit/server/features/mcp/test_mcp_oauth_authenticated_status.py
backend/tests/external_dependency_unit/server/features/mcp/test_mcp_persona_gate.py
backend/tests/external_dependency_unit/server/features/mcp/test_mcp_tool_sync.py
backend/tests/external_dependency_unit/server/features/mcp/test_mcp_user_group_deletion.py
backend/tests/external_dependency_unit/server/features/mcp/test_per_user_api_token_credentials.py
backend/tests/external_dependency_unit/server/features/mcp/test_shared_api_token_template_visibility.py
backend/tests/external_dependency_unit/tools/test_disabled_tool_not_constructed.py
backend/tests/external_dependency_unit/tools/test_mcp_passthrough_oauth.py
backend/tests/external_dependency_unit/tools/test_memory_tool_integration.py
backend/tests/external_dependency_unit/tools/test_oauth_tool_integration.py
backend/tests/external_dependency_unit/tools/test_python_tool_server_enabled.py
backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_api_key.py
backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_google_oauth.py
backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_no_auth.py
backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_oauth.py
backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_per_user_key.py
backend/tests/integration/mock_services/mcp_test_server/run_mock_oidc_idp.py
backend/tests/integration/tests/code_interpreter/conftest.py
backend/tests/integration/tests/code_interpreter/test_code_interpreter_api.py
backend/tests/integration/tests/image_generation/test_image_generation_tool_visibility.py
backend/tests/integration/tests/llm_workflows/test_mock_llm_tool_calls.py
backend/tests/integration/tests/llm_workflows/test_tool_policy_enforcement.py
backend/tests/integration/tests/mcp/test_craft_mcp_servers.py
backend/tests/integration/tests/mcp/test_mcp_client_no_auth_flow.py
backend/tests/integration/tests/mcp/test_mcp_server_auth.py
backend/tests/integration/tests/mcp/test_mcp_server_search.py
backend/tests/integration/tests/mcp_oauth/conftest.py
backend/tests/integration/tests/mcp_oauth/test_mcp_oauth_cimd_integration.py
backend/tests/integration/tests/migrations/test_tool_seeding.py
backend/tests/integration/tests/tools/test_force_tool_use.py
backend/tests/unit/onyx/chat/test_narration_tool_placement.py
backend/tests/unit/onyx/mcp_server/test_agent_scoped_search.py
backend/tests/unit/onyx/mcp_server/test_request_timeouts.py
backend/tests/unit/onyx/server/features/mcp/test_admin_credentials_resolver.py
backend/tests/unit/onyx/server/features/mcp/test_build_headers.py
backend/tests/unit/onyx/server/features/mcp/test_mcp_client.py
backend/tests/unit/onyx/server/features/mcp/test_mcp_known_provider_flow.py
backend/tests/unit/onyx/server/features/mcp/test_mcp_oauth_attempt_store.py
backend/tests/unit/onyx/server/features/mcp/test_mcp_oauth_callback.py
backend/tests/unit/onyx/server/features/mcp/test_mcp_oauth_client_metadata_document.py
backend/tests/unit/onyx/server/features/mcp/test_mcp_oauth_connect.py
backend/tests/unit/onyx/server/features/mcp/test_mcp_oauth_flow.py
backend/tests/unit/onyx/server/features/mcp/test_mcp_oauth_models.py
backend/tests/unit/onyx/server/features/mcp/test_mcp_oauth_provider.py
backend/tests/unit/onyx/server/features/mcp/test_mcp_oauth_refresh.py
backend/tests/unit/onyx/server/features/mcp/test_mcp_oauth_storage.py
backend/tests/unit/onyx/server/features/mcp/test_mcp_ssrf.py
backend/tests/unit/onyx/server/features/mcp/test_oauth_credentials_resolver.py
backend/tests/unit/onyx/server/features/mcp/test_per_user_listing_invariants.py
backend/tests/unit/onyx/server/features/mcp/test_shared_api_token_headers.py
backend/tests/unit/onyx/server/features/mcp/test_template_header_substitution.py
backend/tests/unit/onyx/tools/test_mcp_tool_schema.py
backend/tests/unit/onyx/tools/test_python_tool_availability.py
backend/tests/unit/onyx/tools/test_search_tool_time_filter_cache.py
backend/tests/unit/onyx/tools/test_tool_llm_names.py
backend/tests/unit/onyx/tools/test_tool_runner.py
backend/tests/unit/onyx/tools/test_tool_runner_chat_files.py
backend/tests/unit/onyx/tools/test_tool_utils.py
backend/tests/unit/onyx/tools/tool_implementations/bash/__init__.py
backend/tests/unit/onyx/tools/tool_implementations/bash/test_bash_tool.py
backend/tests/unit/onyx/tools/tool_implementations/coding_agent/__init__.py
backend/tests/unit/onyx/tools/tool_implementations/coding_agent/test_coding_agent_tool.py
backend/tests/unit/onyx/tools/tool_implementations/open_url/data/test_snippet_finding_data.json
backend/tests/unit/onyx/tools/tool_implementations/open_url/test_onyx_web_crawler.py
backend/tests/unit/onyx/tools/tool_implementations/open_url/test_onyx_web_crawler_playwright_fallback.py
backend/tests/unit/onyx/tools/tool_implementations/open_url/test_open_url_failure_messages.py
backend/tests/unit/onyx/tools/tool_implementations/open_url/test_snippet_matcher.py
backend/tests/unit/onyx/tools/tool_implementations/open_url/test_url_normalization.py
backend/tests/unit/onyx/tools/tool_implementations/python/__init__.py
backend/tests/unit/onyx/tools/tool_implementations/python/test_code_interpreter_client.py
backend/tests/unit/onyx/tools/tool_implementations/python/test_python_tool_upload_cache.py
backend/tests/unit/onyx/tools/tool_implementations/search/test_search_tool_run.py
backend/tests/unit/onyx/tools/tool_implementations/websearch/data/tartan.txt
backend/tests/unit/onyx/tools/tool_implementations/websearch/test_brave_client.py
backend/tests/unit/onyx/tools/tool_implementations/websearch/test_web_search_providers.py
backend/tests/unit/onyx/tools/tool_implementations/websearch/test_web_search_tool_run.py
backend/tests/unit/onyx/tools/tool_implementations/websearch/test_websearch_utils.py
backend/tests/unit/sandbox_proxy/test_mcp_jsonrpc.py
backend/tests/unit/server/metrics/test_mcp_metrics.py
backend/tests/unit/tools/test_memory_tool_packets.py
deployment/data/nginx/mcp.conf.inc.template
deployment/data/nginx/mcp_upstream.conf.inc.template
deployment/docker_compose/docker-compose.mcp-api-key-test.yml
deployment/docker_compose/docker-compose.mcp-oauth-test.yml
deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml
deployment/helm/charts/onyx/templates/ingress-mcp-oauth-callback.yaml
deployment/helm/charts/onyx/templates/ingress-mcp.yaml
deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml
deployment/helm/charts/onyx/templates/mcp-server-service.yaml
deployment/helm/charts/onyx/templates/mcp-server-servicemonitor.yaml
terraform-provider-onyx/docs/resources/mcp_server.md
terraform-provider-onyx/examples/resources/onyx_mcp_server/import.sh
terraform-provider-onyx/examples/resources/onyx_mcp_server/resource.tf
terraform-provider-onyx/internal/client/custom_tool_test.go
terraform-provider-onyx/internal/client/mcp_server.go
terraform-provider-onyx/internal/client/mcp_server_test.go
terraform-provider-onyx/internal/provider/custom_tool_resource.go
terraform-provider-onyx/internal/provider/custom_tool_resource_test.go
terraform-provider-onyx/internal/provider/mcp_server_resource.go
terraform-provider-onyx/internal/provider/mcp_server_resource_test.go
web/lib/opal/src/icons/mcp.tsx
web/src/app/admin/code-interpreter/page.tsx
web/src/app/admin/mcp-actions/page.tsx
web/src/app/api/chat/mcp/oauth/callback/route.ts
web/src/app/craft/v1/apps/admin/McpServerPolicyModal.tsx
web/src/app/mcp/[[...path]]/route.ts
web/src/app/mcp/oauth/callback/page.tsx
web/src/components/chat/MCPApiKeyModal.tsx
web/src/lib/tools/components/MCPLineItem.test.tsx
web/src/lib/tools/components/MCPLineItem.tsx
web/src/sections/actions/MCPActionCard.tsx
web/src/sections/actions/MCPPageContent.test.tsx
web/src/sections/actions/MCPPageContent.tsx
web/src/sections/actions/modals/AddMCPServerModal.tsx
web/src/sections/actions/modals/MCPAuthenticationModal.tsx
web/tests/e2e/admin/code-interpreter/code_interpreter.spec.ts
web/tests/e2e/admin/oauth_config/test_tool_oauth.spec.ts
web/tests/e2e/mcp/McpOAuthFlow.ts
web/tests/e2e/mcp/default-agent-mcp.spec.ts
web/tests/e2e/mcp/mcpToolInvocation.ts
web/tests/e2e/mcp/mcp_group_access.spec.ts
web/tests/e2e/mcp/mcp_oauth_flow.spec.ts
web/tests/e2e/mcp/mcp_per_user_key.spec.ts
web/tests/e2e/pages/AdminMcpServersPage.ts
web/tests/e2e/utils/mcpServer.ts
```
## Tool Definitions and Schemas
Evidence lines: 600
```text
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:25:class BoxGroupTooLargeError(Exception):
HEAD:backend/ee/onyx/server/gateway/api.py:45:from onyx.llm.model_response import ChatCompletionMessageToolCall
HEAD:backend/ee/onyx/server/gateway/api.py:55:    ToolCall,
HEAD:backend/ee/onyx/server/gateway/api.py:505:    tool_call: ToolCall | ChatCompletionMessageToolCall,
HEAD:backend/ee/onyx/server/gateway/api.py:521:    tool_calls: list[ToolCall] | list[ChatCompletionMessageToolCall] | None,
HEAD:backend/ee/onyx/server/gateway/api.py:928:        input_schema = tool.get("input_schema")
HEAD:backend/ee/onyx/server/gateway/api.py:934:                "only client tools with an input_schema are accepted.",
HEAD:backend/ee/onyx/server/gateway/api.py:972:    tool_names = {
HEAD:backend/ee/onyx/server/gateway/api.py:977:    if tool_choice.name not in tool_names:
HEAD:backend/ee/onyx/server/gateway/api.py:1056:    tool_calls: list[ToolCall] | list[ChatCompletionMessageToolCall] | None,
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:16:    ChatCompletionDeltaToolCall,
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:59:        self.tool_call_buffer: dict[int, ChatCompletionDeltaToolCall] = {}
HEAD:backend/ee/onyx/server/seeding.py:32:class CustomToolSeed(BaseModel):
HEAD:backend/onyx/auth/permission_projection.py:118:class ToolPermissions(TypedDict):
HEAD:backend/onyx/chat/chat_state.py:26:from onyx.tools.models import ChatFile, ToolCallInfo
HEAD:backend/onyx/chat/chat_state.py:48:        self.tool_calls: list[ToolCallInfo] = []
HEAD:backend/onyx/chat/chat_state.py:67:    def add_tool_call(self, tool_call: ToolCallInfo) -> None:
HEAD:backend/onyx/chat/chat_state.py:112:    def get_tool_calls(self) -> list[ToolCallInfo]:
HEAD:backend/onyx/chat/chat_utils.py:21:    ToolCallSimple,
HEAD:backend/onyx/chat/chat_utils.py:68:from onyx.tools.models import ChatFile, ToolCallKickoff
HEAD:backend/onyx/chat/chat_utils.py:74:IMAGE_GENERATION_TOOL_NAME = "generate_image"
HEAD:backend/onyx/chat/chat_utils.py:690:    tool_name: str,
HEAD:backend/onyx/chat/chat_utils.py:694:    if tool_name != IMAGE_GENERATION_TOOL_NAME:
HEAD:backend/onyx/chat/chat_utils.py:846:                    # Build ToolCallSimple list for this turn
HEAD:backend/onyx/chat/chat_utils.py:847:                    tool_calls_simple: list[ToolCallSimple] = []
HEAD:backend/onyx/chat/chat_utils.py:849:                        tool_name = tool_id_to_name_map.get(
HEAD:backend/onyx/chat/chat_utils.py:853:                            ToolCallSimple(
HEAD:backend/onyx/chat/chat_utils.py:855:                                tool_name=tool_name,
HEAD:backend/onyx/chat/chat_utils.py:877:                        tool_name = tool_id_to_name_map.get(
HEAD:backend/onyx/chat/chat_utils.py:882:                                tool_name=tool_name,
HEAD:backend/onyx/chat/chat_utils.py:967:    tool_calls: list[ToolCallKickoff], token_counter: Callable[[str], int]
HEAD:backend/onyx/chat/chat_utils.py:976:        tool_calls: List of ToolCallKickoff objects representing the failed tool calls
HEAD:backend/onyx/chat/chat_utils.py:986:    # Create ToolCallSimple for each failed tool call
HEAD:backend/onyx/chat/chat_utils.py:987:    tool_calls_simple: list[ToolCallSimple] = []
HEAD:backend/onyx/chat/chat_utils.py:991:            ToolCallSimple(
HEAD:backend/onyx/chat/chat_utils.py:993:                tool_name=tool_call.tool_name,
HEAD:backend/onyx/chat/citation_utils.py:28:    if tool_response.tool_call.tool_name in CITEABLE_TOOLS_NAMES:
HEAD:backend/onyx/chat/compression.py:282:                tool_names = [
HEAD:backend/onyx/chat/compression.py:286:                    AssistantMessage(content=f"[Used tools: {', '.join(tool_names)}]")
HEAD:backend/onyx/chat/llm_loop.py:30:    ToolCallSimple,
HEAD:backend/onyx/chat/llm_loop.py:63:    ToolCallDebug,
HEAD:backend/onyx/chat/llm_loop.py:70:    CustomToolCallSummary,
HEAD:backend/onyx/chat/llm_loop.py:74:    ToolCallInfo,
HEAD:backend/onyx/chat/llm_loop.py:75:    ToolCallKickoff,
HEAD:backend/onyx/chat/llm_loop.py:262:    extracted_tool_calls: list[ToolCallKickoff] = []
HEAD:backend/onyx/chat/llm_loop.py:267:            tool_definitions=tool_defs,
HEAD:backend/onyx/chat/llm_loop.py:277:            tool_definitions=tool_defs,
HEAD:backend/onyx/chat/llm_loop.py:283:            tool_definitions=tool_defs,
HEAD:backend/onyx/chat/llm_loop.py:1050:            tool_defs = [tool.tool_definition() for tool in final_tools]
HEAD:backend/onyx/chat/llm_loop.py:1059:                tool_definitions=tool_defs,
HEAD:backend/onyx/chat/llm_loop.py:1103:                            obj=ToolCallDebug(
HEAD:backend/onyx/chat/llm_loop.py:1105:                                tool_name=tool_call.tool_name,
HEAD:backend/onyx/chat/llm_loop.py:1162:                if tool_call.tool_name == SearchTool.NAME:
HEAD:backend/onyx/chat/llm_loop.py:1167:                    tool_call.tool_name == PythonTool.NAME
HEAD:backend/onyx/chat/llm_loop.py:1182:                tool = tools_by_name.get(tool_call.tool_name)
HEAD:backend/onyx/chat/llm_loop.py:1185:                        f"Tool '{tool_call.tool_name}' not found in tools list"
HEAD:backend/onyx/chat/llm_loop.py:1206:                    if search_docs and tool_call.tool_name == WebSearchTool.NAME:
HEAD:backend/onyx/chat/llm_loop.py:1241:                    tool_response.rich_response, CustomToolCallSummary
HEAD:backend/onyx/chat/llm_loop.py:1293:                elif isinstance(tool_response.rich_response, CustomToolCallSummary):
HEAD:backend/onyx/chat/llm_loop.py:1302:                tool_call_info = ToolCallInfo(
HEAD:backend/onyx/chat/llm_loop.py:1306:                    tool_name=tool_call.tool_name,
HEAD:backend/onyx/chat/llm_loop.py:1335:                # Build ToolCallSimple list for all tool calls in this turn
HEAD:backend/onyx/chat/llm_loop.py:1336:                tool_calls_simple: list[ToolCallSimple] = []
HEAD:backend/onyx/chat/llm_loop.py:1347:                        ToolCallSimple(
HEAD:backend/onyx/chat/llm_loop.py:1349:                            tool_name=tc.tool_name,
HEAD:backend/onyx/chat/llm_loop.py:1389:                tool.tool_name in STOPPING_TOOLS_NAMES
HEAD:backend/onyx/chat/llm_loop.py:1395:                tool.tool_name in CITEABLE_TOOLS_NAMES
HEAD:backend/onyx/chat/llm_step.py:41:    ToolCall,
HEAD:backend/onyx/chat/llm_step.py:64:from onyx.tools.models import ToolCallKickoff
HEAD:backend/onyx/chat/llm_step.py:65:from onyx.tools.tool_name import sanitize_tool_name
HEAD:backend/onyx/chat/llm_step.py:89:class _XmlToolCallContentFilter:
HEAD:backend/onyx/chat/llm_step.py:388:) -> list[ToolCallKickoff]:
HEAD:backend/onyx/chat/llm_step.py:389:    """Extract ToolCallKickoff objects from the tool call map.
HEAD:backend/onyx/chat/llm_step.py:391:    Returns a list of ToolCallKickoff objects for valid tool calls (those with both id and name).
HEAD:backend/onyx/chat/llm_step.py:401:    tool_calls: list[ToolCallKickoff] = []
HEAD:backend/onyx/chat/llm_step.py:408:                ToolCallKickoff(
HEAD:backend/onyx/chat/llm_step.py:410:                    tool_name=tool_call_data["name"],
HEAD:backend/onyx/chat/llm_step.py:427:    tool_definitions: list[dict],
HEAD:backend/onyx/chat/llm_step.py:429:) -> list[ToolCallKickoff]:
HEAD:backend/onyx/chat/llm_step.py:439:        tool_definitions: List of tool definitions to match against
HEAD:backend/onyx/chat/llm_step.py:443:        List of ToolCallKickoff objects for any matched tool calls
HEAD:backend/onyx/chat/llm_step.py:445:    if not response_text or not tool_definitions:
HEAD:backend/onyx/chat/llm_step.py:449:    tool_name_to_def: dict[str, dict] = {}
HEAD:backend/onyx/chat/llm_step.py:450:    for tool_def in tool_definitions:
HEAD:backend/onyx/chat/llm_step.py:453:            tool_name = func_def.get("name")
HEAD:backend/onyx/chat/llm_step.py:454:            if tool_name:
HEAD:backend/onyx/chat/llm_step.py:455:                tool_name_to_def[tool_name] = func_def
HEAD:backend/onyx/chat/llm_step.py:457:    if not tool_name_to_def:
HEAD:backend/onyx/chat/llm_step.py:467:        matched_tool_call = _try_match_json_to_tool(json_obj, tool_name_to_def)
HEAD:backend/onyx/chat/llm_step.py:481:                tool_name_to_def=tool_name_to_def,
HEAD:backend/onyx/chat/llm_step.py:495:            tool_name_to_def=tool_name_to_def,
HEAD:backend/onyx/chat/llm_step.py:498:    tool_calls: list[ToolCallKickoff] = []
HEAD:backend/onyx/chat/llm_step.py:499:    for tab_index, (tool_name, tool_args) in enumerate(matched_tool_calls):
HEAD:backend/onyx/chat/llm_step.py:501:            ToolCallKickoff(
HEAD:backend/onyx/chat/llm_step.py:503:                tool_name=tool_name,
HEAD:backend/onyx/chat/llm_step.py:523:    tool_name_to_def: dict[str, dict],
HEAD:backend/onyx/chat/llm_step.py:538:        tool_name = _extract_xml_attribute(invoke_attrs, "name")
HEAD:backend/onyx/chat/llm_step.py:539:        if not tool_name or tool_name not in tool_name_to_def:
HEAD:backend/onyx/chat/llm_step.py:556:        matched_tool_calls.append((tool_name, tool_args))
HEAD:backend/onyx/chat/llm_step.py:587:    """Extract and parse an arguments/parameters value from a tool-call-like object.
HEAD:backend/onyx/chat/llm_step.py:606:    tool_name_to_def: dict[str, dict],
HEAD:backend/onyx/chat/llm_step.py:611:    1. Direct tool call format: {"name": "tool_name", "arguments": {...}}
HEAD:backend/onyx/chat/llm_step.py:612:    2. Function call format: {"function": {"name": "tool_name", "arguments": {...}}}
HEAD:backend/onyx/chat/llm_step.py:613:    3. Tool name as key: {"tool_name": {...arguments...}}
HEAD:backend/onyx/chat/llm_step.py:618:        tool_name_to_def: Map of tool names to their function definitions
HEAD:backend/onyx/chat/llm_step.py:621:        Tuple of (tool_name, tool_args) if matched, None otherwise
HEAD:backend/onyx/chat/llm_step.py:624:    if "name" in json_obj and json_obj["name"] in tool_name_to_def:
HEAD:backend/onyx/chat/llm_step.py:625:        tool_name = json_obj["name"]
HEAD:backend/onyx/chat/llm_step.py:628:            return (tool_name, arguments)
HEAD:backend/onyx/chat/llm_step.py:633:        if "name" in func_obj and func_obj["name"] in tool_name_to_def:
HEAD:backend/onyx/chat/llm_step.py:634:            tool_name = func_obj["name"]
HEAD:backend/onyx/chat/llm_step.py:637:                return (tool_name, arguments)
HEAD:backend/onyx/chat/llm_step.py:639:    # Format 3: Tool name as key {"tool_name": {...arguments...}}
HEAD:backend/onyx/chat/llm_step.py:640:    for tool_name in tool_name_to_def:
HEAD:backend/onyx/chat/llm_step.py:641:        if tool_name in json_obj:
HEAD:backend/onyx/chat/llm_step.py:642:            arguments = json_obj[tool_name]
HEAD:backend/onyx/chat/llm_step.py:644:                return (tool_name, arguments)
HEAD:backend/onyx/chat/llm_step.py:647:    for tool_name, func_def in tool_name_to_def.items():
HEAD:backend/onyx/chat/llm_step.py:662:                return (tool_name, filtered_args)
HEAD:backend/onyx/chat/llm_step.py:670:    tool_name_to_def: dict[str, dict],
HEAD:backend/onyx/chat/llm_step.py:673:    extracted_args = _extract_nested_arguments_obj(previous_json_obj, tool_name_to_def)
HEAD:backend/onyx/chat/llm_step.py:679:    tool_name_to_def: dict[str, dict],
HEAD:backend/onyx/chat/llm_step.py:682:    if "name" in json_obj and json_obj["name"] in tool_name_to_def:
HEAD:backend/onyx/chat/llm_step.py:690:        if "name" in function_obj and function_obj["name"] in tool_name_to_def:
HEAD:backend/onyx/chat/llm_step.py:695:    # Format 3: {"tool_name": {...arguments...}}
HEAD:backend/onyx/chat/llm_step.py:696:    for tool_name in tool_name_to_def:
HEAD:backend/onyx/chat/llm_step.py:697:        if tool_name in json_obj and isinstance(json_obj[tool_name], dict):
HEAD:backend/onyx/chat/llm_step.py:698:            return json_obj[tool_name]
HEAD:backend/onyx/chat/llm_step.py:704:    tool_calls_list: list[ToolCall] | None = None
HEAD:backend/onyx/chat/llm_step.py:707:            ToolCall(
HEAD:backend/onyx/chat/llm_step.py:711:                    name=sanitize_tool_name(tc.tool_name),
HEAD:backend/onyx/chat/llm_step.py:763:                f"[Tool Call] name={tc.tool_name} id={tc.tool_call_id} args={json.dumps(tc.tool_arguments)}"
HEAD:backend/onyx/chat/llm_step.py:1076:    tool_definitions: list[dict],
HEAD:backend/onyx/chat/llm_step.py:1105:        tool_definitions: List of tool definitions available to the LLM.
HEAD:backend/onyx/chat/llm_step.py:1135:            - ToolCallKickoff for tool calls (extracted at the end)
HEAD:backend/onyx/chat/llm_step.py:1182:    xml_tool_call_content_filter = _XmlToolCallContentFilter()
HEAD:backend/onyx/chat/llm_step.py:1197:            Sequence[Mapping[str, Any]], tool_definitions
HEAD:backend/onyx/chat/llm_step.py:1309:            tools=tool_definitions,
HEAD:backend/onyx/chat/llm_step.py:1502:            tool_calls_list: list[ToolCall] = [
HEAD:backend/onyx/chat/llm_step.py:1503:                ToolCall(
HEAD:backend/onyx/chat/llm_step.py:1507:                        name=kickoff.tool_name,
HEAD:backend/onyx/chat/llm_step.py:1540:                f"  - {tc.tool_name}: {json.dumps(tc.tool_args, indent=4)}"
HEAD:backend/onyx/chat/llm_step.py:1560:            len(tool_definitions),
HEAD:backend/onyx/chat/llm_step.py:1578:    tool_definitions: list[dict],
HEAD:backend/onyx/chat/llm_step.py:1603:        tool_definitions=tool_definitions,
HEAD:backend/onyx/chat/models.py:19:from onyx.tools.models import SearchToolUsage, ToolCallKickoff
HEAD:backend/onyx/chat/models.py:33:class CustomToolResponse(BaseModel):
HEAD:backend/onyx/chat/models.py:35:    tool_name: str
HEAD:backend/onyx/chat/models.py:56:class ToolCallResponse(BaseModel):
HEAD:backend/onyx/chat/models.py:59:    tool_name: str
HEAD:backend/onyx/chat/models.py:90:    tool_calls: list[ToolCallResponse] = []
HEAD:backend/onyx/chat/models.py:146:class ToolCallSimple(BaseModel):
HEAD:backend/onyx/chat/models.py:154:    tool_name: str
HEAD:backend/onyx/chat/models.py:172:    tool_calls: list[ToolCallSimple] | None = None
HEAD:backend/onyx/chat/models.py:192:class FileToolMetadata(BaseModel):
HEAD:backend/onyx/chat/models.py:244:    tool_calls: list[ToolCallKickoff] | None
HEAD:backend/onyx/chat/process_message.py:66:    ToolCallResponse,
HEAD:backend/onyx/chat/process_message.py:2249:    # Convert ToolCallInfo list to ToolCallResponse list
HEAD:backend/onyx/chat/process_message.py:2251:        ToolCallResponse(
HEAD:backend/onyx/chat/process_message.py:2252:            tool_name=tc.tool_name,
HEAD:backend/onyx/chat/prompt_utils.py:25:    TOOL_DESCRIPTION_SEARCH_GUIDANCE,
HEAD:backend/onyx/chat/prompt_utils.py:283:            TOOL_DESCRIPTION_SEARCH_GUIDANCE,
HEAD:backend/onyx/chat/prompt_utils.py:309:            tool_guidance_sections.append(TOOL_DESCRIPTION_SEARCH_GUIDANCE)
HEAD:backend/onyx/chat/save_chat.py:15:from onyx.db.models import ChatMessage, ToolCall
HEAD:backend/onyx/chat/save_chat.py:20:from onyx.tools.models import ToolCallInfo
HEAD:backend/onyx/chat/save_chat.py:28:    tool_calls: list[ToolCallInfo],
HEAD:backend/onyx/chat/save_chat.py:53:    tool_calls: list[ToolCallInfo],
HEAD:backend/onyx/chat/save_chat.py:60:    Create ToolCall entries and link parent references and SearchDocs.
HEAD:backend/onyx/chat/save_chat.py:63:    1. Creating all ToolCall objects (with temporary parent references)
HEAD:backend/onyx/chat/save_chat.py:66:    4. Linking SearchDocs to ToolCalls
HEAD:backend/onyx/chat/save_chat.py:76:    # Create all ToolCall objects first (without parent_tool_call_id set)
HEAD:backend/onyx/chat/save_chat.py:78:    tool_call_objects: list[ToolCall] = []
HEAD:backend/onyx/chat/save_chat.py:79:    tool_call_info_map: dict[str, ToolCallInfo] = {}
HEAD:backend/onyx/chat/save_chat.py:101:        # Create ToolCall DB entry (parent_tool_call_id will be set after flush)
HEAD:backend/onyx/chat/save_chat.py:137:    valid_tool_calls: list[ToolCall] = []
HEAD:backend/onyx/chat/save_chat.py:158:    # Link SearchDocs only to valid ToolCalls
HEAD:backend/onyx/chat/save_chat.py:172:    tool_calls: list[ToolCallInfo],
HEAD:backend/onyx/chat/save_chat.py:192:    6. Creates ToolCall entries and links SearchDocs to them
HEAD:backend/onyx/chat/save_chat.py:198:        tool_calls: List of tool call information to create ToolCall entries (may include search_docs)
HEAD:backend/onyx/chat/save_chat.py:340:    # 6. Create ToolCall entries and link SearchDocs to them
HEAD:backend/onyx/chat/tool_call_args_streaming.py:4:from onyx.llm.model_response import ChatCompletionDeltaToolCall
HEAD:backend/onyx/chat/tool_call_args_streaming.py:6:from onyx.server.query_and_chat.streaming_models import Packet, ToolCallArgumentDelta
HEAD:backend/onyx/chat/tool_call_args_streaming.py:7:from onyx.tools.built_in_tools import TOOL_NAME_TO_CLASS
HEAD:backend/onyx/chat/tool_call_args_streaming.py:14:    tool_call_delta: ChatCompletionDeltaToolCall,
HEAD:backend/onyx/chat/tool_call_args_streaming.py:16:    """Look up the Tool subclass for a streaming tool call delta."""
HEAD:backend/onyx/chat/tool_call_args_streaming.py:17:    tool_name = tool_calls_in_progress.get(tool_call_delta.index, {}).get("name")
HEAD:backend/onyx/chat/tool_call_args_streaming.py:18:    if not tool_name:
HEAD:backend/onyx/chat/tool_call_args_streaming.py:20:    return TOOL_NAME_TO_CLASS.get(tool_name)
HEAD:backend/onyx/chat/tool_call_args_streaming.py:25:    tool_call_delta: ChatCompletionDeltaToolCall,
HEAD:backend/onyx/chat/tool_call_args_streaming.py:70:        obj=ToolCallArgumentDelta(
HEAD:backend/onyx/coding_agent/mock_tools.py:1:from onyx.deep_research.dr_mock_tools import THINK_TOOL_NAME
HEAD:backend/onyx/coding_agent/mock_tools.py:4:CODING_AGENT_TOOL_NAME = "coding_agent"
HEAD:backend/onyx/coding_agent/mock_tools.py:8:BASH_TOOL_NAME = "bash"
HEAD:backend/onyx/coding_agent/mock_tools.py:12:GENERATE_ANSWER_TOOL_NAME = "generate_answer"
HEAD:backend/onyx/coding_agent/mock_tools.py:15:CODING_AGENT_TOOL_DESCRIPTION = {
HEAD:backend/onyx/coding_agent/mock_tools.py:18:        "name": CODING_AGENT_TOOL_NAME,
HEAD:backend/onyx/coding_agent/mock_tools.py:24:        "parameters": {
HEAD:backend/onyx/coding_agent/mock_tools.py:48:BASH_TOOL_DESCRIPTION = {
HEAD:backend/onyx/coding_agent/mock_tools.py:51:        "name": BASH_TOOL_NAME,
HEAD:backend/onyx/coding_agent/mock_tools.py:59:        "parameters": {
HEAD:backend/onyx/coding_agent/mock_tools.py:73:GENERATE_ANSWER_TOOL_DESCRIPTION = {
HEAD:backend/onyx/coding_agent/mock_tools.py:76:        "name": GENERATE_ANSWER_TOOL_NAME,
HEAD:backend/onyx/coding_agent/mock_tools.py:83:        "parameters": {
HEAD:backend/onyx/coding_agent/mock_tools.py:92:CODING_AGENT_THINK_TOOL_DESCRIPTION = {
HEAD:backend/onyx/coding_agent/mock_tools.py:95:        "name": THINK_TOOL_NAME,
HEAD:backend/onyx/coding_agent/mock_tools.py:101:        "parameters": {
HEAD:backend/onyx/coding_agent/mock_tools.py:115:def get_coding_agent_tool_definitions(include_think_tool: bool) -> list[dict]:
HEAD:backend/onyx/coding_agent/mock_tools.py:117:        BASH_TOOL_DESCRIPTION,
HEAD:backend/onyx/coding_agent/mock_tools.py:118:        GENERATE_ANSWER_TOOL_DESCRIPTION,
HEAD:backend/onyx/coding_agent/mock_tools.py:121:        tools.append(CODING_AGENT_THINK_TOOL_DESCRIPTION)
HEAD:backend/onyx/coding_agent/models.py:3:from onyx.tools.models import ToolCallKickoff
HEAD:backend/onyx/coding_agent/models.py:6:class CodingAgentSpecialToolCalls(BaseModel):
HEAD:backend/onyx/coding_agent/models.py:7:    think_tool_call: ToolCallKickoff | None = None
HEAD:backend/onyx/coding_agent/models.py:8:    generate_answer_tool_call: ToolCallKickoff | None = None
HEAD:backend/onyx/configs/agent_configs.py:287:# Parameters for the Thoughtful/Deep Research flows
HEAD:backend/onyx/db/README.md:21:Tool calls are stored in the ToolCall table and can represent all of the following:
HEAD:backend/onyx/db/README.md:25:- Tool calls that are instead attached to other ToolCalls are tool calls that happen as part of an
HEAD:backend/onyx/db/chat.py:23:    ToolCall,
HEAD:backend/onyx/db/chat.py:577:    Link SearchDocs to a ToolCall by creating entries in the tool_call__search_doc junction table.
HEAD:backend/onyx/db/chat.py:584:    from onyx.db.models import ToolCall__SearchDoc
HEAD:backend/onyx/db/chat.py:587:        tool_call_search_doc = ToolCall__SearchDoc(
HEAD:backend/onyx/db/chat.py:625:                ToolCall.tool_call_children
HEAD:backend/onyx/db/models.py:817:class ToolCall__SearchDoc(Base):
HEAD:backend/onyx/db/models.py:839:class Persona__Tool(Base):
HEAD:backend/onyx/db/models.py:3402:    tool_calls: Mapped[list["ToolCall"] | None] = relationship(
HEAD:backend/onyx/db/models.py:3403:        "ToolCall",
HEAD:backend/onyx/db/models.py:3414:class ToolCall(Base):
HEAD:backend/onyx/db/models.py:3469:    parent_tool_call: Mapped["ToolCall | None"] = relationship(
HEAD:backend/onyx/db/models.py:3470:        "ToolCall",
HEAD:backend/onyx/db/models.py:3472:        remote_side="ToolCall.id",
HEAD:backend/onyx/db/models.py:3474:    tool_call_children: Mapped[list["ToolCall"]] = relationship(
HEAD:backend/onyx/db/models.py:3475:        "ToolCall",
HEAD:backend/onyx/db/models.py:3483:        secondary=ToolCall__SearchDoc.__table__,
HEAD:backend/onyx/db/models.py:3535:    tool_calls: Mapped[list["ToolCall"]] = relationship(
HEAD:backend/onyx/db/models.py:3536:        "ToolCall",
HEAD:backend/onyx/db/models.py:3537:        secondary=ToolCall__SearchDoc.__table__,
HEAD:backend/onyx/db/models.py:4015:class Tool(Base):
HEAD:backend/onyx/db/models.py:4032:    mcp_input_schema: Mapped[dict[str, Any] | None] = mapped_column(
HEAD:backend/onyx/db/tools.py:18:    ToolCall,
HEAD:backend/onyx/db/tools.py:198:def get_tool_by_name(tool_name: str, db_session: Session) -> Tool:
HEAD:backend/onyx/db/tools.py:199:    tool = db_session.scalar(select(Tool).where(Tool.name == tool_name))
HEAD:backend/onyx/db/tools.py:361:) -> ToolCall:
HEAD:backend/onyx/db/tools.py:363:    Create a ToolCall entry in the database.
HEAD:backend/onyx/db/tools.py:382:        The created ToolCall object
HEAD:backend/onyx/db/tools.py:384:    tool_call = ToolCall(
HEAD:backend/onyx/deep_research/dr_loop.py:19:    ToolCallSimple,
HEAD:backend/onyx/deep_research/dr_loop.py:31:    RESEARCH_AGENT_TOOL_NAME,
HEAD:backend/onyx/deep_research/dr_loop.py:34:    get_clarification_tool_definitions,
HEAD:backend/onyx/deep_research/dr_loop.py:71:from onyx.tools.models import ToolCallInfo, ToolCallKickoff
HEAD:backend/onyx/deep_research/dr_loop.py:165:            tool_definitions=[],
HEAD:backend/onyx/deep_research/dr_loop.py:200:            tool_name=RESEARCH_AGENT_TOOL_NAME,
HEAD:backend/onyx/deep_research/dr_loop.py:255:        allowed_tool_names = {SearchTool.NAME, WebSearchTool.NAME, OpenURLTool.NAME}
HEAD:backend/onyx/deep_research/dr_loop.py:256:        allowed_tools = [tool for tool in tools if tool.name in allowed_tool_names]
HEAD:backend/onyx/deep_research/dr_loop.py:257:        include_internal_search_tunings = SearchTool.NAME in allowed_tool_names
HEAD:backend/onyx/deep_research/dr_loop.py:301:                    tool_definitions=get_clarification_tool_definitions(),
HEAD:backend/onyx/deep_research/dr_loop.py:362:                tool_definitions=[],
HEAD:backend/onyx/deep_research/dr_loop.py:499:                research_agent_calls: list[ToolCallKickoff] = []
HEAD:backend/onyx/deep_research/dr_loop.py:537:                    tool_definitions=get_orchestrator_tools(
HEAD:backend/onyx/deep_research/dr_loop.py:635:                        think_tool_simple = ToolCallSimple(
HEAD:backend/onyx/deep_research/dr_loop.py:637:                            tool_name=think_tool_call.tool_name,
HEAD:backend/onyx/deep_research/dr_loop.py:662:                        if tool_call.tool_name != RESEARCH_AGENT_TOOL_NAME:
HEAD:backend/onyx/deep_research/dr_loop.py:664:                                "Unexpected tool call: %s", tool_call.tool_name
HEAD:backend/onyx/deep_research/dr_loop.py:738:                    tool_calls_simple: list[ToolCallSimple] = []
HEAD:backend/onyx/deep_research/dr_loop.py:743:                            ToolCallSimple(
HEAD:backend/onyx/deep_research/dr_loop.py:745:                                tool_name=current_tool_call.tool_name,
HEAD:backend/onyx/deep_research/dr_loop.py:793:                        tool_call_info = ToolCallInfo(
HEAD:backend/onyx/deep_research/dr_loop.py:799:                            tool_name=current_tool_call.tool_name,
HEAD:backend/onyx/deep_research/dr_mock_tools.py:1:GENERATE_PLAN_TOOL_NAME = "generate_plan"
HEAD:backend/onyx/deep_research/dr_mock_tools.py:4:RESEARCH_AGENT_TOOL_NAME = "research_agent"
HEAD:backend/onyx/deep_research/dr_mock_tools.py:7:GENERATE_REPORT_TOOL_NAME = "generate_report"
HEAD:backend/onyx/deep_research/dr_mock_tools.py:9:THINK_TOOL_NAME = "think_tool"
HEAD:backend/onyx/deep_research/dr_mock_tools.py:13:GENERATE_PLAN_TOOL_DESCRIPTION = {
HEAD:backend/onyx/deep_research/dr_mock_tools.py:16:        "name": GENERATE_PLAN_TOOL_NAME,
HEAD:backend/onyx/deep_research/dr_mock_tools.py:18:        "parameters": {
HEAD:backend/onyx/deep_research/dr_mock_tools.py:27:RESEARCH_AGENT_TOOL_DESCRIPTION = {
HEAD:backend/onyx/deep_research/dr_mock_tools.py:30:        "name": RESEARCH_AGENT_TOOL_NAME,
HEAD:backend/onyx/deep_research/dr_mock_tools.py:32:        "parameters": {
HEAD:backend/onyx/deep_research/dr_mock_tools.py:46:GENERATE_REPORT_TOOL_DESCRIPTION = {
HEAD:backend/onyx/deep_research/dr_mock_tools.py:49:        "name": GENERATE_REPORT_TOOL_NAME,
HEAD:backend/onyx/deep_research/dr_mock_tools.py:51:        "parameters": {
HEAD:backend/onyx/deep_research/dr_mock_tools.py:60:THINK_TOOL_DESCRIPTION = {
HEAD:backend/onyx/deep_research/dr_mock_tools.py:63:        "name": THINK_TOOL_NAME,
HEAD:backend/onyx/deep_research/dr_mock_tools.py:65:        "parameters": {
HEAD:backend/onyx/deep_research/dr_mock_tools.py:79:RESEARCH_AGENT_THINK_TOOL_DESCRIPTION = {
HEAD:backend/onyx/deep_research/dr_mock_tools.py:84:        "parameters": {
HEAD:backend/onyx/deep_research/dr_mock_tools.py:98:RESEARCH_AGENT_GENERATE_REPORT_TOOL_DESCRIPTION = {
HEAD:backend/onyx/deep_research/dr_mock_tools.py:103:        "parameters": {
HEAD:backend/onyx/deep_research/dr_mock_tools.py:116:def get_clarification_tool_definitions() -> list[dict]:
HEAD:backend/onyx/deep_research/dr_mock_tools.py:117:    return [GENERATE_PLAN_TOOL_DESCRIPTION]
HEAD:backend/onyx/deep_research/dr_mock_tools.py:122:        RESEARCH_AGENT_TOOL_DESCRIPTION,
HEAD:backend/onyx/deep_research/dr_mock_tools.py:123:        GENERATE_REPORT_TOOL_DESCRIPTION,
HEAD:backend/onyx/deep_research/dr_mock_tools.py:126:        tools.append(THINK_TOOL_DESCRIPTION)
HEAD:backend/onyx/deep_research/dr_mock_tools.py:130:def get_research_agent_additional_tool_definitions(
HEAD:backend/onyx/deep_research/dr_mock_tools.py:133:    tools = [GENERATE_REPORT_TOOL_DESCRIPTION]
HEAD:backend/onyx/deep_research/dr_mock_tools.py:135:        tools.append(RESEARCH_AGENT_THINK_TOOL_DESCRIPTION)
HEAD:backend/onyx/deep_research/models.py:4:from onyx.tools.models import ToolCallKickoff
HEAD:backend/onyx/deep_research/models.py:7:class SpecialToolCalls(BaseModel):
HEAD:backend/onyx/deep_research/models.py:8:    think_tool_call: ToolCallKickoff | None = None
HEAD:backend/onyx/deep_research/models.py:9:    generate_report_tool_call: ToolCallKickoff | None = None
HEAD:backend/onyx/deep_research/utils.py:6:from onyx.deep_research.dr_mock_tools import GENERATE_REPORT_TOOL_NAME, THINK_TOOL_NAME
HEAD:backend/onyx/deep_research/utils.py:7:from onyx.deep_research.models import SpecialToolCalls
HEAD:backend/onyx/deep_research/utils.py:8:from onyx.llm.model_response import ChatCompletionDeltaToolCall, Delta, FunctionCall
HEAD:backend/onyx/deep_research/utils.py:9:from onyx.tools.models import ToolCallKickoff
HEAD:backend/onyx/deep_research/utils.py:17:class ThinkToolProcessorState(BaseModel):
HEAD:backend/onyx/deep_research/utils.py:143:                complete_tool_call = ChatCompletionDeltaToolCall(
HEAD:backend/onyx/deep_research/utils.py:148:                        name=THINK_TOOL_NAME,
HEAD:backend/onyx/deep_research/utils.py:159:                if tool_call.function and tool_call.function.name == THINK_TOOL_NAME:
HEAD:backend/onyx/deep_research/utils.py:199:def check_special_tool_calls(tool_calls: list[ToolCallKickoff]) -> SpecialToolCalls:
HEAD:backend/onyx/deep_research/utils.py:200:    think_tool_call: ToolCallKickoff | None = None
HEAD:backend/onyx/deep_research/utils.py:201:    generate_report_tool_call: ToolCallKickoff | None = None
HEAD:backend/onyx/deep_research/utils.py:204:        if tool_call.tool_name == THINK_TOOL_NAME:
HEAD:backend/onyx/deep_research/utils.py:206:        elif tool_call.tool_name == GENERATE_REPORT_TOOL_NAME:
HEAD:backend/onyx/deep_research/utils.py:209:    return SpecialToolCalls(
HEAD:backend/onyx/document_index/opensearch/schema.py:447:                        "parameters": {"ef_construction": EF_CONSTRUCTION, "m": M},
HEAD:backend/onyx/document_index/opensearch/schema.py:459:                        "parameters": {"ef_construction": EF_CONSTRUCTION, "m": M},
HEAD:backend/onyx/document_index/opensearch/search.py:121:                        "parameters": {
HEAD:backend/onyx/document_index/opensearch/search.py:143:                        "parameters": {
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:6:class DocumentIDTooLongError(ValueError):
HEAD:backend/onyx/evals/eval.py:82:    tools_called = [tc.tool_name for tc in full.tool_calls]
HEAD:backend/onyx/evals/eval.py:84:        {"tool_name": tc.tool_name, "tool_arguments": tc.tool_arguments}
HEAD:backend/onyx/evals/models.py:14:class ToolAssertion(BaseModel):
HEAD:backend/onyx/evals/models.py:42:class EvalToolResult(BaseModel):
HEAD:backend/onyx/evals/providers/local.py:44:            for tool_name, duration_ms in result.timings.tool_execution_ms.items():
HEAD:backend/onyx/evals/providers/local.py:45:                print(f"    {tool_name}: {duration_ms:.0f}ms")
HEAD:backend/onyx/llm/model_response.py:18:class ChatCompletionMessageToolCall(BaseModel):
HEAD:backend/onyx/llm/model_response.py:24:class ChatCompletionDeltaToolCall(BaseModel):
HEAD:backend/onyx/llm/model_response.py:35:    tool_calls: List[ChatCompletionDeltaToolCall] = Field(default_factory=list)
HEAD:backend/onyx/llm/model_response.py:66:    tool_calls: List[ChatCompletionMessageToolCall] | None = None
HEAD:backend/onyx/llm/model_response.py:103:) -> list[ChatCompletionDeltaToolCall]:
HEAD:backend/onyx/llm/model_response.py:108:    parsed_tool_calls: list[ChatCompletionDeltaToolCall] = [
HEAD:backend/onyx/llm/model_response.py:109:        ChatCompletionDeltaToolCall(
HEAD:backend/onyx/llm/model_response.py:147:) -> list[ChatCompletionMessageToolCall]:
HEAD:backend/onyx/llm/model_response.py:152:    parsed_tool_calls: list[ChatCompletionMessageToolCall] = []
HEAD:backend/onyx/llm/model_response.py:159:            ChatCompletionMessageToolCall(
HEAD:backend/onyx/llm/models.py:13:class ToolChoiceOptions(str, Enum):
HEAD:backend/onyx/llm/models.py:19:class NamedToolChoice(BaseModel):
HEAD:backend/onyx/llm/models.py:201:class ToolCall(BaseModel):
HEAD:backend/onyx/llm/models.py:229:    tool_calls: list[ToolCall] | None = None
HEAD:backend/onyx/llm/models.py:233:class ToolMessage(CacheableMessage):
HEAD:backend/onyx/llm/tracing_wrap.py:23:from onyx.llm.model_response import ChatCompletionDeltaToolCall, Usage
HEAD:backend/onyx/llm/tracing_wrap.py:31:    from onyx.llm.models import ToolCall
HEAD:backend/onyx/llm/tracing_wrap.py:204:            tool_call_buffer: dict[int, ChatCompletionDeltaToolCall] = {}
HEAD:backend/onyx/llm/tracing_wrap.py:247:    buffer: dict[int, "ChatCompletionDeltaToolCall"],
HEAD:backend/onyx/llm/tracing_wrap.py:248:    delta: "ChatCompletionDeltaToolCall",
HEAD:backend/onyx/llm/tracing_wrap.py:260:    result is a dict of complete ``ChatCompletionDeltaToolCall`` objects
HEAD:backend/onyx/llm/tracing_wrap.py:261:    keyed by ``index`` that can be converted to fully-formed ``ToolCall``
HEAD:backend/onyx/llm/tracing_wrap.py:269:        buffer[delta.index] = ChatCompletionDeltaToolCall(
HEAD:backend/onyx/llm/tracing_wrap.py:302:    buffer: dict[int, "ChatCompletionDeltaToolCall"],
HEAD:backend/onyx/llm/tracing_wrap.py:303:) -> list["ToolCall"] | None:
HEAD:backend/onyx/llm/tracing_wrap.py:304:    """Convert a reassembled delta buffer into a list of complete ``ToolCall``.
HEAD:backend/onyx/llm/tracing_wrap.py:314:    from onyx.llm.models import ToolCall
HEAD:backend/onyx/llm/tracing_wrap.py:316:    finalized: list[ToolCall] = []
HEAD:backend/onyx/llm/tracing_wrap.py:322:            ToolCall(
HEAD:backend/onyx/mcp_server/README.md:143:- Test tool calls with different parameters
HEAD:backend/onyx/mcp_server/tools/search.py:35:from onyx.server.metrics.mcp_common import MCPToolCallStatus
HEAD:backend/onyx/mcp_server/tools/search.py:354:    outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/mcp_server/tools/search.py:369:            outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/mcp_server/tools/search.py:401:        outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/mcp_server/tools/search.py:441:    outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/mcp_server/tools/search.py:457:        outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/mcp_server/tools/search.py:501:    outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/mcp_server/tools/search.py:512:        outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/prompts/chat_tools.py:4:DANSWER_TOOL_NAME = "Current Search"
HEAD:backend/onyx/prompts/chat_tools.py:5:DANSWER_TOOL_DESCRIPTION = "A search tool that can find information on any topic including up to date and proprietary knowledge."
HEAD:backend/onyx/prompts/chat_tools.py:26:    "action": string, \\ The action to take. {tool_names}
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:1:from onyx.coding_agent.mock_tools import BASH_TOOL_NAME, GENERATE_ANSWER_TOOL_NAME
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:2:from onyx.deep_research.dr_mock_tools import THINK_TOOL_NAME
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:10:You operate in a read-only, network-isolated sandbox with the repository checked out at the working directory of every `{BASH_TOOL_NAME}` call. Iteratively call `{BASH_TOOL_NAME}` to inspect the codebase, then call `{GENERATE_ANSWER_TOOL_NAME}` once you have gathered enough evidence to answer the user's query comprehensively.
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:51:## {BASH_TOOL_NAME}
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:70:## {THINK_TOOL_NAME}
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:71:Use `{THINK_TOOL_NAME}` between sets of bash calls to consolidate what you've learned, identify the next question, and decide which command(s) will most efficiently answer it. Use it before calling `{GENERATE_ANSWER_TOOL_NAME}` to verify that every claim you intend to make is backed by something you read.
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:73:## {GENERATE_ANSWER_TOOL_NAME}
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:81:You operate in a read-only, network-isolated sandbox with the repository checked out at the working directory of every `{BASH_TOOL_NAME}` call. Reason between calls about what you have learned and what to inspect next. When you have enough evidence to answer the query, call `{GENERATE_ANSWER_TOOL_NAME}`.
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:100:## {BASH_TOOL_NAME}
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:103:## {GENERATE_ANSWER_TOOL_NAME}
HEAD:backend/onyx/prompts/deep_research/dr_tool_prompts.py:1:GENERATE_PLAN_TOOL_NAME = "generate_plan"
HEAD:backend/onyx/prompts/deep_research/dr_tool_prompts.py:4:GENERATE_REPORT_TOOL_NAME = "generate_report"
HEAD:backend/onyx/prompts/deep_research/dr_tool_prompts.py:7:RESEARCH_AGENT_TOOL_NAME = "research_agent"
HEAD:backend/onyx/prompts/deep_research/dr_tool_prompts.py:11:THINK_TOOL_NAME = "think_tool"
HEAD:backend/onyx/prompts/deep_research/dr_tool_prompts.py:17:WEB_SEARCH_TOOL_DESCRIPTION = """
HEAD:backend/onyx/prompts/deep_research/dr_tool_prompts.py:26:OPEN_URLS_TOOL_DESCRIPTION = f"""
HEAD:backend/onyx/prompts/deep_research/dr_tool_prompts.py:31:You should almost always use open_urls after a web_search call and sometimes after reasoning with the {THINK_TOOL_NAME} tool.
HEAD:backend/onyx/prompts/deep_research/dr_tool_prompts.py:34:OPEN_URLS_TOOL_DESCRIPTION_REASONING = """
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:2:    GENERATE_PLAN_TOOL_NAME,
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:3:    GENERATE_REPORT_TOOL_NAME,
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:4:    RESEARCH_AGENT_TOOL_NAME,
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:5:    THINK_TOOL_NAME,
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:11:CRITICAL - Never directly answer the user's query, you must only ask clarifying questions or call the `{GENERATE_PLAN_TOOL_NAME}` tool.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:13:If the user query is already very detailed or lengthy (more than 3 sentences), do not ask for clarification and instead call the `{GENERATE_PLAN_TOOL_NAME}` tool.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:63:You are an orchestrator agent for deep research. Your job is to conduct research by calling the {RESEARCH_AGENT_TOOL_NAME} tool with high level research tasks. \
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:64:This delegates the lower level research work to the {RESEARCH_AGENT_TOOL_NAME} which will provide back the results of the research.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:68:Before calling {GENERATE_REPORT_TOOL_NAME}, reason to double check that all aspects of the user's query have been well researched and that all key topics around the plan have been researched. \
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:70:In these cases, ensure that the new directions are thoroughly investigated prior to calling {GENERATE_REPORT_TOOL_NAME}.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:77:## {RESEARCH_AGENT_TOOL_NAME}
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:78:The research task provided to the {RESEARCH_AGENT_TOOL_NAME} should be reasonably high level with a clear direction for investigation. \
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:82:CRITICAL - the {RESEARCH_AGENT_TOOL_NAME} only receives the task and has no additional context about the user's query, research plan, other research agents, or message history. \
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:83:You absolutely must provide all of the context needed to complete the task in the argument to the {RESEARCH_AGENT_TOOL_NAME}.{{internal_search_research_task_guidance}}
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:85:You should call the {RESEARCH_AGENT_TOOL_NAME} MANY times before completing with the {GENERATE_REPORT_TOOL_NAME} tool.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:87:You are encouraged to call the {RESEARCH_AGENT_TOOL_NAME} in parallel if the research tasks are not dependent on each other, which is typically the case. NEVER call more than 3 {RESEARCH_AGENT_TOOL_NAME} calls in parallel.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:89:## {GENERATE_REPORT_TOOL_NAME}
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:90:You should call the {GENERATE_REPORT_TOOL_NAME} tool if any of the following conditions are met:
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:96:## {THINK_TOOL_NAME}
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:97:CRITICAL - use the {THINK_TOOL_NAME} to reason between every call to the {RESEARCH_AGENT_TOOL_NAME} and before calling {GENERATE_REPORT_TOOL_NAME}. You should treat this as chain-of-thought reasoning to think deeply on what to do next. \
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:100:NEVER use the {THINK_TOOL_NAME} in parallel with other {RESEARCH_AGENT_TOOL_NAME} or {GENERATE_REPORT_TOOL_NAME}.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:102:Before calling {GENERATE_REPORT_TOOL_NAME}, double check that all aspects of the user's query have been researched and that all key topics around the plan have been researched (unless you have gone in a different direction).
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:115:Remember to refer to the system prompt and follow how to use the tools. Call the {THINK_TOOL_NAME} between every call to the {RESEARCH_AGENT_TOOL_NAME} and before calling {GENERATE_REPORT_TOOL_NAME}. Never run more than 3 {RESEARCH_AGENT_TOOL_NAME} calls in parallel.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:147:Ignore the format styles of the intermediate {RESEARCH_AGENT_TOOL_NAME} reports, those are not end user facing and different from your task.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:155:You are an orchestrator agent for deep research. Your job is to conduct research by calling the {RESEARCH_AGENT_TOOL_NAME} tool with high level research tasks. \
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:156:This delegates the lower level research work to the {RESEARCH_AGENT_TOOL_NAME} which will provide back the results of the research.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:160:Before calling {GENERATE_REPORT_TOOL_NAME}, reason to double check that all aspects of the user's query have been well researched and that all key topics around the plan have been researched.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:161:There are cases where new discoveries from research may lead to a deviation from the original research plan. In these cases, ensure that the new directions are thoroughly investigated prior to calling {GENERATE_REPORT_TOOL_NAME}.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:170:## {RESEARCH_AGENT_TOOL_NAME}
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:171:The research task provided to the {RESEARCH_AGENT_TOOL_NAME} should be reasonably high level with a clear direction for investigation. \
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:175:CRITICAL - the {RESEARCH_AGENT_TOOL_NAME} only receives the task and has no additional context about the user's query, research plan, or message history. \
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:176:You absolutely must provide all of the context needed to complete the task in the argument to the {RESEARCH_AGENT_TOOL_NAME}.{{internal_search_research_task_guidance}}
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:178:You should call the {RESEARCH_AGENT_TOOL_NAME} MANY times before completing with the {GENERATE_REPORT_TOOL_NAME} tool.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:180:You are encouraged to call the {RESEARCH_AGENT_TOOL_NAME} in parallel if the research tasks are not dependent on each other, which is typically the case. NEVER call more than 3 {RESEARCH_AGENT_TOOL_NAME} calls in parallel.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:182:## {GENERATE_REPORT_TOOL_NAME}
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:183:You should call the {GENERATE_REPORT_TOOL_NAME} tool if any of the following conditions are met:
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:196:You are encouraged to call the {RESEARCH_AGENT_TOOL_NAME} in parallel when the research tasks are not dependent on each other, but never call more than 3 {RESEARCH_AGENT_TOOL_NAME} calls in parallel.
HEAD:backend/onyx/prompts/deep_research/research_agent.py:2:    GENERATE_REPORT_TOOL_NAME,
HEAD:backend/onyx/prompts/deep_research/research_agent.py:3:    THINK_TOOL_NAME,
HEAD:backend/onyx/prompts/deep_research/research_agent.py:11:You iteratively call the tools available to you including {{available_tools}} until you have completed your research at which point you call the {GENERATE_REPORT_TOOL_NAME} tool.
HEAD:backend/onyx/prompts/deep_research/research_agent.py:19:{{optional_internal_search_tool_description}}\
HEAD:backend/onyx/prompts/deep_research/research_agent.py:20:{{optional_web_search_tool_description}}\
HEAD:backend/onyx/prompts/deep_research/research_agent.py:21:{{optional_open_url_tool_description}}
HEAD:backend/onyx/prompts/deep_research/research_agent.py:22:## {THINK_TOOL_NAME}
HEAD:backend/onyx/prompts/deep_research/research_agent.py:24:You MUST use the {THINK_TOOL_NAME} before calling the web_search tool for all calls to web_search except for the first call. \
HEAD:backend/onyx/prompts/deep_research/research_agent.py:25:Use the {THINK_TOOL_NAME} before calling the {GENERATE_REPORT_TOOL_NAME} tool.
HEAD:backend/onyx/prompts/deep_research/research_agent.py:27:After a set of searches + reads, use the {THINK_TOOL_NAME} to analyze the results and plan the next steps.
HEAD:backend/onyx/prompts/deep_research/research_agent.py:32:## {GENERATE_REPORT_TOOL_NAME}
HEAD:backend/onyx/prompts/deep_research/research_agent.py:33:Once you have completed your research, call the `{GENERATE_REPORT_TOOL_NAME}` tool. \
HEAD:backend/onyx/prompts/deep_research/research_agent.py:75:You iteratively call the tools available to you including {{available_tools}} until you have completed your research at which point you call the {GENERATE_REPORT_TOOL_NAME} tool. Between calls, think about the results of the previous tool call and plan the next steps. \
HEAD:backend/onyx/prompts/deep_research/research_agent.py:78:Once you have completed your research, call the `{GENERATE_REPORT_TOOL_NAME}` tool.
HEAD:backend/onyx/prompts/deep_research/research_agent.py:86:{{optional_internal_search_tool_description}}\
HEAD:backend/onyx/prompts/deep_research/research_agent.py:87:{{optional_web_search_tool_description}}\
HEAD:backend/onyx/prompts/deep_research/research_agent.py:88:{{optional_open_url_tool_description}}
HEAD:backend/onyx/prompts/deep_research/research_agent.py:89:## {GENERATE_REPORT_TOOL_NAME}
HEAD:backend/onyx/prompts/deep_research/research_agent.py:90:Once you have completed your research, call the `{GENERATE_REPORT_TOOL_NAME}` tool. You should only call this tool after you have fully researched the topic.
HEAD:backend/onyx/prompts/tool_prompts.py:7:TOOL_DESCRIPTION_SEARCH_GUIDANCE = """
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:54:    tool_names: tuple[str, ...] = ()
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:85:    tool_names: list[str] = []
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:91:            name = _tool_name(message)
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:94:            tool_names.append(name)
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:98:    if tool_names:
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:100:            kind=McpRpcKind.TOOL_CALL, tool_names=tuple(tool_names)
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:130:def _tool_name(message: dict[str, Any]) -> str | None:
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:255:    counts: Counter[str] = Counter(classification.tool_names)
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:258:            action_type=tool_name,
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:259:            display_name=tool_name,
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:261:                f"Call the “{tool_name}” tool on {server.name}."
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:264:            policy=stored.get(tool_name, MCP_TOOL_DEFAULT_POLICY),
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:266:        for tool_name, count in counts.items()
HEAD:backend/onyx/server/features/build/sandbox/base.py:32:    ToolCallProgress,
HEAD:backend/onyx/server/features/build/sandbox/base.py:33:    ToolCallStart,
HEAD:backend/onyx/server/features/build/sandbox/base.py:77:    | ToolCallStart
HEAD:backend/onyx/server/features/build/sandbox/base.py:78:    | ToolCallProgress
HEAD:backend/onyx/server/features/build/sandbox/event_schema.py:18:    ToolCallProgress,
HEAD:backend/onyx/server/features/build/sandbox/event_schema.py:19:    ToolCallStart,
HEAD:backend/onyx/server/features/build/sandbox/event_schema.py:46:    "ToolCallProgress",
HEAD:backend/onyx/server/features/build/sandbox/event_schema.py:47:    "ToolCallStart",
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:50:    ToolCallProgress,
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:51:    ToolCallStart,
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:73:    | ToolCallStart
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:74:    | ToolCallProgress
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:102:# aware (idempotent ToolCallStart, terminator de-dup, gap-fill accumulators).
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:115:    # ToolCallStart is emitted only on the FIRST sighting of a callID.
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:217:# opencode's tool status values → ToolCallStatus literal.
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:848:    """Emit ToolCallStart (first sighting) and/or ToolCallProgress for a
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:871:        "toolCallId": call_id,
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:890:        yield ToolCallStart.model_validate({"sessionUpdate": "tool_call", **common})
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:895:            yield ToolCallProgress.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:899:        yield ToolCallProgress.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:121:        for tool_name in server.disabled_tools:
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:122:            permissions[f"{server.key}_{tool_name}"] = "deny"
HEAD:backend/onyx/server/features/build/session/streaming.py:63:    ToolCallProgress,
HEAD:backend/onyx/server/features/build/session/streaming.py:64:    ToolCallStart,
HEAD:backend/onyx/server/features/build/session/streaming.py:698:    if isinstance(sandbox_event, ToolCallStart):
HEAD:backend/onyx/server/features/build/session/streaming.py:703:    if isinstance(sandbox_event, ToolCallProgress):
HEAD:backend/onyx/server/features/build/session/streaming.py:710:        tool_name = (event_data.get("title") or "").lower()
HEAD:backend/onyx/server/features/build/session/streaming.py:711:        is_todo_write = tool_name in ("todowrite", "todo_write")
HEAD:backend/onyx/server/features/build/session/streaming.py:715:            tool_name == "task"
HEAD:backend/onyx/server/features/build/session/streaming.py:927:                    ToolCallStart,
HEAD:backend/onyx/server/features/build/session/streaming.py:928:                    ToolCallProgress,
HEAD:backend/onyx/server/features/build/session/streaming.py:944:            elif isinstance(sandbox_event, ToolCallStart):
HEAD:backend/onyx/server/features/build/session/streaming.py:946:            elif isinstance(sandbox_event, ToolCallProgress):
HEAD:backend/onyx/server/features/build/session/streaming.py:992:    elif isinstance(sandbox_event, ToolCallStart):
HEAD:backend/onyx/server/features/build/session/streaming.py:994:    elif isinstance(sandbox_event, ToolCallProgress):
HEAD:backend/onyx/server/features/mcp/api.py:895:    # Get callback data from query parameters (like federated OAuth does)
HEAD:backend/onyx/server/features/mcp/api.py:1127:class MCPToolDescription(BaseModel):
HEAD:backend/onyx/server/features/mcp/api.py:1134:class ServerToolsResponse(BaseModel):
HEAD:backend/onyx/server/features/mcp/api.py:1408:class ToolSnapshotSource(str, Enum):
HEAD:backend/onyx/server/features/mcp/api.py:1425:    Query Parameters:
HEAD:backend/onyx/server/features/mcp/api.py:1497:        tool_name = tool.name
HEAD:backend/onyx/server/features/mcp/api.py:1498:        if not tool_name:
HEAD:backend/onyx/server/features/mcp/api.py:1501:        processed_names.add(tool_name)
HEAD:backend/onyx/server/features/mcp/api.py:1504:        display_name = tool.title or annotations_title or tool_name
HEAD:backend/onyx/server/features/mcp/api.py:1505:        input_schema = tool.inputSchema
HEAD:backend/onyx/server/features/mcp/api.py:1507:        if existing_tool := existing_by_name.get(tool_name):
HEAD:backend/onyx/server/features/mcp/api.py:1510:            existing_tool.mcp_input_schema = input_schema
HEAD:backend/onyx/server/features/mcp/api.py:1514:            name=tool_name,
HEAD:backend/onyx/server/features/mcp/api.py:1525:        new_tool.mcp_input_schema = input_schema
HEAD:backend/onyx/server/features/mcp/api.py:1527:        existing_by_name[tool_name] = new_tool
HEAD:backend/onyx/server/features/mcp/api.py:2162:    for tool_name, db_tool in existing_by_name.items():
HEAD:backend/onyx/server/features/mcp/api.py:2163:        should_enable = tool_name in selected_tools
HEAD:backend/onyx/server/features/mcp/api.py:2345:        tool_name = tool.name
HEAD:backend/onyx/server/features/mcp/api.py:2346:        if tool.mcp_server and tool_name.startswith(f"{tool.mcp_server.name}_"):
HEAD:backend/onyx/server/features/mcp/api.py:2347:            tool_name = tool_name[len(f"{tool.mcp_server.name}_") :]
HEAD:backend/onyx/server/features/mcp/api.py:2352:                name=tool_name,
HEAD:backend/onyx/server/features/mcp/api.py:2353:                display_name=tool.display_name or tool_name,
HEAD:backend/onyx/server/features/mcp/client.py:246:def _call_mcp_tool(tool_name: str, arguments: dict[str, Any]) -> MCPClientFunction[str]:
HEAD:backend/onyx/server/features/mcp/client.py:249:        result = await session.call_tool(tool_name, arguments)
HEAD:backend/onyx/server/features/mcp/client.py:257:    tool_name: str,
HEAD:backend/onyx/server/features/mcp/client.py:265:        _call_mcp_tool(tool_name, arguments),
HEAD:backend/onyx/server/features/mcp/models.py:206:class MCPToolCreateRequest(BaseModel):
HEAD:backend/onyx/server/features/mcp/models.py:243:        None, description="Optional extra query parameters for the authorization URL"
HEAD:backend/onyx/server/features/mcp/models.py:396:                    f"parameters: {', '.join(sorted(reserved_params))}"
HEAD:backend/onyx/server/features/mcp/models.py:408:class MCPToolUpdateRequest(BaseModel):
HEAD:backend/onyx/server/features/mcp/models.py:478:class MCPToolResponse(BaseModel):
HEAD:backend/onyx/server/features/mcp/models.py:589:    additional_authorization_parameters: dict[str, Any] | None
HEAD:backend/onyx/server/features/mcp/models.py:772:class MCPToolListResponse(BaseModel):
HEAD:backend/onyx/server/features/mcp/oauth.py:17:from mcp.client.auth import OAuthClientProvider, PKCEParameters, TokenStorage
HEAD:backend/onyx/server/features/mcp/oauth.py:718:        pkce = PKCEParameters.generate()
HEAD:backend/onyx/server/features/mcp/oauth_flow.py:8:from mcp.client.auth import OAuthClientProvider, PKCEParameters
HEAD:backend/onyx/server/features/mcp/oauth_flow.py:94:            "Known-provider OAuth additional parameters cannot override: "
HEAD:backend/onyx/server/features/mcp/oauth_flow.py:119:        additional_authorization_parameters=mcp_server.oauth_additional_auth_params,
HEAD:backend/onyx/server/features/mcp/oauth_flow.py:240:    pkce = PKCEParameters.generate()
HEAD:backend/onyx/server/features/oauth_config/api.py:246:    Accepts code and state as query parameters (standard OAuth flow).
HEAD:backend/onyx/server/features/persona/models.py:497:class ImageGenerationToolStatus(BaseModel):
HEAD:backend/onyx/server/features/tool/api.py:49:def _validate_tool_definition(definition: dict[str, Any]) -> None:
HEAD:backend/onyx/server/features/tool/api.py:156:    _validate_tool_definition(tool_data.definition)
HEAD:backend/onyx/server/features/tool/api.py:186:        _validate_tool_definition(tool_data.definition)
HEAD:backend/onyx/server/features/tool/api.py:229:class ToolStatusUpdateRequest(BaseModel):
HEAD:backend/onyx/server/features/tool/api.py:234:class ToolStatusUpdateResponse(BaseModel):
HEAD:backend/onyx/server/features/tool/api.py:288:class ValidateToolRequest(BaseModel):
HEAD:backend/onyx/server/features/tool/api.py:292:class ValidateToolResponse(BaseModel):
HEAD:backend/onyx/server/features/tool/api.py:301:    _validate_tool_definition(tool_data.definition)
HEAD:backend/onyx/server/features/tool/models.py:27:class ToolSnapshot(BaseModel):
HEAD:backend/onyx/server/features/tool/models.py:86:class CustomToolCreate(BaseModel):
HEAD:backend/onyx/server/features/tool/models.py:95:class CustomToolUpdate(BaseModel):
HEAD:backend/onyx/server/features/tool/tool_visibility.py:8:# Tool class name constant for OktaProfileTool (not in main constants.py as it's hidden)
HEAD:backend/onyx/server/features/tool/tool_visibility.py:12:class ToolVisibilitySettings(BaseModel):
HEAD:backend/onyx/server/features/web_search/models.py:7:class WebSearchToolRequest(BaseModel):
HEAD:backend/onyx/server/features/web_search/models.py:38:class WebSearchToolResponse(BaseModel):
HEAD:backend/onyx/server/features/web_search/models.py:50:class OpenUrlsToolRequest(BaseModel):
HEAD:backend/onyx/server/features/web_search/models.py:66:class OpenUrlsToolResponse(BaseModel):
HEAD:backend/onyx/server/gateway/models.py:593:class AnthropicToolUseBlock(_WireModel):
HEAD:backend/onyx/server/metrics/mcp_client.py:5:from onyx.server.metrics.mcp_common import MCPToolCallStatus
HEAD:backend/onyx/server/metrics/mcp_client.py:13:    ["server_name", "tool_name", "status"],
HEAD:backend/onyx/server/metrics/mcp_client.py:18:    ["server_name", "tool_name"],
HEAD:backend/onyx/server/metrics/mcp_client.py:25:    tool_name: str,
HEAD:backend/onyx/server/metrics/mcp_client.py:27:    status: MCPToolCallStatus,
HEAD:backend/onyx/server/metrics/mcp_client.py:32:            tool_name=tool_name,
HEAD:backend/onyx/server/metrics/mcp_client.py:36:            tool_name=tool_name,
HEAD:backend/onyx/server/metrics/mcp_common.py:4:class MCPToolCallStatus(str, Enum):
HEAD:backend/onyx/server/metrics/mcp_server.py:6:from onyx.server.metrics.mcp_common import MCPToolCallStatus
HEAD:backend/onyx/server/metrics/mcp_server.py:18:class MCPServerToolName(str, Enum):
HEAD:backend/onyx/server/metrics/mcp_server.py:66:    status: MCPToolCallStatus,
HEAD:backend/onyx/server/query_and_chat/session_loading.py:188:    tool_name: str,
HEAD:backend/onyx/server/query_and_chat/session_loading.py:203:            obj=CustomToolStart(tool_name=tool_name, tool_id=tool_id),
HEAD:backend/onyx/server/query_and_chat/session_loading.py:211:                obj=CustomToolArgs(tool_name=tool_name, tool_args=tool_args),
HEAD:backend/onyx/server/query_and_chat/session_loading.py:219:                tool_name=tool_name,
HEAD:backend/onyx/server/query_and_chat/session_loading.py:743:                        # Try to parse as structured CustomToolCallSummary JSON
HEAD:backend/onyx/server/query_and_chat/session_loading.py:752:                            if isinstance(parsed, dict) and "tool_name" in parsed:
HEAD:backend/onyx/server/query_and_chat/session_loading.py:783:                                tool_name=tool.display_name or tool.name,
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:151:class ToolCallDebug(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:155:    tool_name: str
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:163:class SearchToolStart(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:171:class SearchToolQueriesDelta(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:181:class SearchToolFilterDelta(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:192:class SearchToolDocumentsDelta(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:226:class ImageGenerationToolStart(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:232:class ImageGenerationToolHeartbeat(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:255:class PythonToolStart(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:260:class PythonToolDelta(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:269:class CustomToolStart(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:272:    tool_name: str
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:276:class CustomToolArgs(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:279:    tool_name: str
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:283:class CustomToolErrorInfo(BaseModel):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:290:class CustomToolDelta(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:293:    tool_name: str
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:303:class ToolCallArgumentDelta(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:334:class MemoryToolStart(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:338:class MemoryToolDelta(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:347:class MemoryToolNoAccess(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:417:class BashToolStart(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:422:class BashToolDelta(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:471:    ToolCallDebug,
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:472:    ToolCallArgumentDelta,
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:432:browser ships with first-class React introspection. Works on any React app — Next.js, Remix, Vite+React, CRA, TanStack Start, React Native Web, etc. The `react …` commands require the React DevTools hook to be installed at launch via `--enable react-devtools`:
HEAD:backend/onyx/tools/built_in_tools.py:75:def _build_tool_name_to_class() -> dict[str, Type[BUILT_IN_TOOL_TYPES]]:
HEAD:backend/onyx/tools/built_in_tools.py:80:TOOL_NAME_TO_CLASS: dict[str, Type[BUILT_IN_TOOL_TYPES]] = _build_tool_name_to_class()
HEAD:backend/onyx/tools/constants.py:4:SEARCH_TOOL_NAME = "run_search"
HEAD:backend/onyx/tools/constants.py:5:INTERNET_SEARCH_TOOL_NAME = "run_internet_search"
HEAD:backend/onyx/tools/constants.py:6:IMAGE_GENERATION_TOOL_NAME = "run_image_generation"
HEAD:backend/onyx/tools/constants.py:7:PYTHON_TOOL_NAME = "run_python"
HEAD:backend/onyx/tools/constants.py:8:OPEN_URL_TOOL_NAME = "open_url"
HEAD:backend/onyx/tools/constants.py:21:FILE_READER_TOOL_NAME = "read_file"
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:9:from onyx.chat.models import ChatMessageSimple, ToolCallSimple
```
Tool schemas define the capability contract presented to the model.
A model knowing about a tool does not itself prove that the caller is
authorized to use it.
## Tool Availability / Registry
Evidence lines: 276
```text
HEAD:backend/ee/onyx/db/user_group.py:239:            selectinload(Persona.tools),
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:126:    for tool in body.get("tools") or []:
HEAD:backend/ee/onyx/server/seeding.py:182:                    tool_ids=persona.tool_ids,
HEAD:backend/onyx/chat/chat_utils.py:689:def _build_tool_call_response_history_message(
HEAD:backend/onyx/chat/chat_utils.py:846:                    # Build ToolCallSimple list for this turn
HEAD:backend/onyx/chat/chat_utils.py:881:                            _build_tool_call_response_history_message(
HEAD:backend/onyx/chat/compression.py:20:from onyx.db.tools import get_tools
HEAD:backend/onyx/chat/compression.py:404:    be detached, but callers must have eager-loaded the ``tool_calls``
HEAD:backend/onyx/chat/compression.py:444:                all_tools = get_tools(read_session)
HEAD:backend/onyx/chat/llm_loop.py:357:    """Build messages for context-injected / tool-backed files.
HEAD:backend/onyx/chat/llm_loop.py:659:    """Build a lightweight metadata-only message listing files available via FileReaderTool.
HEAD:backend/onyx/chat/llm_loop.py:1023:            tool_token_budget = compute_all_tool_tokens(final_tools, token_counter)
HEAD:backend/onyx/chat/llm_loop.py:1171:                        parsed = json.loads(tool_response.llm_facing_response)
HEAD:backend/onyx/chat/llm_loop.py:1177:                tools_by_name = {tool.name: tool for tool in final_tools}
HEAD:backend/onyx/chat/llm_loop.py:1182:                tool = tools_by_name.get(tool_call.tool_name)
HEAD:backend/onyx/chat/llm_loop.py:1335:                # Build ToolCallSimple list for all tool calls in this turn
HEAD:backend/onyx/chat/llm_step.py:448:    # Build a map of tool names to their definitions
HEAD:backend/onyx/chat/llm_step.py:725:def _build_structured_tool_response_message(msg: ChatMessageSimple) -> ToolMessage:
HEAD:backend/onyx/chat/llm_step.py:753:        return _build_structured_tool_response_message(msg)
HEAD:backend/onyx/chat/process_message.py:95:from onyx.db.tools import get_tools
HEAD:backend/onyx/chat/process_message.py:223:    """Convert ChatLoadedFile objects to ChatFile for tool usage (e.g., PythonTool).
HEAD:backend/onyx/chat/process_message.py:226:    ``loaded_file.content`` only when a tool actually accesses it. Previously
HEAD:backend/onyx/chat/process_message.py:259:def _load_context_user_files_for_tools(
HEAD:backend/onyx/chat/process_message.py:428:            overflow_tool_metadata = [_build_tool_metadata(uf) for uf in user_files]
HEAD:backend/onyx/chat/process_message.py:431:                _build_tool_metadata(uf)
HEAD:backend/onyx/chat/process_message.py:471:            tool_metadata.append(_build_tool_metadata(uf))
HEAD:backend/onyx/chat/process_message.py:514:def _build_tool_metadata(user_file: UserFile) -> FileToolMetadata:
HEAD:backend/onyx/chat/process_message.py:515:    """Build lightweight FileToolMetadata from a UserFile record.
HEAD:backend/onyx/chat/process_message.py:917:    all_tools = get_tools(db_session)
HEAD:backend/onyx/chat/process_message.py:942:    # Convert loaded files to ChatFile format for tools like PythonTool
HEAD:backend/onyx/chat/process_message.py:945:        _load_context_user_files_for_tools(
HEAD:backend/onyx/chat/process_message.py:1363:                allowed_tool_ids=setup.new_msg_req.allowed_tool_ids,
HEAD:backend/onyx/chat/save_chat.py:129:    # Build mapping of tool calls (tool_call_id string -> DB id int)
HEAD:backend/onyx/chat/save_chat.py:189:    3. Builds tool_call -> search_doc mapping for displayed docs
HEAD:backend/onyx/chat/save_chat.py:254:    # 3. Build tool_call -> search_doc mapping (for displayed docs in each tool call)
HEAD:backend/onyx/db/chat.py:54:                selectinload(Persona.tools),
HEAD:backend/onyx/db/chat.py:622:        # Load tool_calls and their direct children (one level deep)
HEAD:backend/onyx/db/chat.py:624:            selectinload(ChatMessage.tool_calls).selectinload(
HEAD:backend/onyx/db/enums.py:205:    FETCHING_TOOLS = "FETCHING_TOOLS"  # Auth complete, fetching tools
HEAD:backend/onyx/db/llm.py:629:def fetch_existing_tools(db_session: Session, tool_ids: list[int]) -> list[ToolModel]:
HEAD:backend/onyx/db/llm.py:631:        db_session.scalars(select(ToolModel).where(ToolModel.id.in_(tool_ids))).all()
HEAD:backend/onyx/db/mcp.py:88:    # Get the persona and its tools
HEAD:backend/onyx/db/mcp.py:327:def get_all_mcp_tools_for_server(server_id: int, db_session: Session) -> list[Tool]:
HEAD:backend/onyx/db/mcp.py:328:    """Get all MCP tools for a server"""
HEAD:backend/onyx/db/mcp.py:334:def get_mcp_tools_for_servers(server_ids: list[int], db_session: Session) -> list[Tool]:
HEAD:backend/onyx/db/models.py:4410:    disabled_tool_ids: Mapped[list[int]] = mapped_column(
HEAD:backend/onyx/db/oauth_config.py:186:def get_tools_by_oauth_config(oauth_config_id: int, db_session: Session) -> list[Tool]:
HEAD:backend/onyx/db/oauth_config.py:187:    """Get all tools that use a specific OAuth configuration"""
HEAD:backend/onyx/db/persona.py:70:    eager_load_for_tools: bool = False,
HEAD:backend/onyx/db/persona.py:73:    if eager_load_for_tools:
HEAD:backend/onyx/db/persona.py:75:            selectinload(Persona.tools),
HEAD:backend/onyx/db/persona.py:196:def get_tool_ids_on_editable_personas(user: User, db_session: Session) -> set[int]:
HEAD:backend/onyx/db/persona.py:197:    """Tools on agents this user may edit. The editor rebuilds an agent's tool_ids
HEAD:backend/onyx/db/persona.py:657:            tool_ids=create_persona_request.tool_ids,
HEAD:backend/onyx/db/persona.py:1046:        selectinload(Persona.tools),
HEAD:backend/onyx/db/persona.py:1098:        selectinload(Persona.tools),
HEAD:backend/onyx/db/persona.py:1210:        selectinload(Persona.tools),
HEAD:backend/onyx/db/persona.py:1294:        selectinload(Persona.tools),
HEAD:backend/onyx/db/persona.py:1567:    tool_ids: list[int] | None = None,
HEAD:backend/onyx/db/persona.py:1621:    # Fetch and attach tools by IDs
HEAD:backend/onyx/db/persona.py:1623:    if tool_ids is not None:
HEAD:backend/onyx/db/persona.py:1624:        tools = db_session.query(Tool).filter(Tool.id.in_(tool_ids)).all()
HEAD:backend/onyx/db/persona.py:1625:        if not tools and tool_ids:
HEAD:backend/onyx/db/persona.py:1633:            existing_tool_ids = (
HEAD:backend/onyx/db/persona.py:1642:                    tool.id in existing_tool_ids
HEAD:backend/onyx/db/persona.py:2086:        .options(selectinload(Persona.tools))
HEAD:backend/onyx/db/persona.py:2099:        .options(selectinload(Persona.tools))
HEAD:backend/onyx/db/persona.py:2110:    tool_ids: list[int] | None = None,
HEAD:backend/onyx/db/persona.py:2118:        tool_ids: List of tool IDs to enable (if None, tools are not updated)
HEAD:backend/onyx/db/persona.py:2138:    if tool_ids is not None:
HEAD:backend/onyx/db/persona.py:2143:        for tool_id in tool_ids:
HEAD:backend/onyx/db/slack_channel_config.py:73:        tool_ids=[search_tool.id],
HEAD:backend/onyx/db/tools.py:33:def get_tools(
HEAD:backend/onyx/db/tools.py:69:def get_tools_by_mcp_server_id(
HEAD:backend/onyx/db/tools.py:84:def get_tools_by_ids(tool_ids: list[int], db_session: Session) -> list[Tool]:
HEAD:backend/onyx/db/tools.py:85:    if not tool_ids:
HEAD:backend/onyx/db/tools.py:87:    stmt = select(Tool).where(Tool.id.in_(tool_ids))
HEAD:backend/onyx/db/tools.py:189:def get_tool_ids_connected_to_groups(
HEAD:backend/onyx/db/tools.py:319:    from onyx.tools.built_in_tools import BUILT_IN_TOOL_MAP
HEAD:backend/onyx/db/tools.py:324:            for in_code_tool_id, tool_cls in BUILT_IN_TOOL_MAP.items()
HEAD:backend/onyx/db/user_preferences.py:362:        config.disabled_tool_ids = new_assistant_preference.disabled_tool_ids
HEAD:backend/onyx/db/user_preferences.py:368:            disabled_tool_ids=new_assistant_preference.disabled_tool_ids,
HEAD:backend/onyx/deep_research/dr_loop.py:35:    get_orchestrator_tools,
HEAD:backend/onyx/deep_research/dr_loop.py:537:                    tool_definitions=get_orchestrator_tools(
HEAD:backend/onyx/deep_research/dr_loop.py:737:                    # Build ONE ASSISTANT message with all tool calls (OpenAI parallel format)
HEAD:backend/onyx/deep_research/dr_mock_tools.py:120:def get_orchestrator_tools(include_think_tool: bool) -> list[dict]:
HEAD:backend/onyx/evals/eval.py:148:def _get_answer_with_tools(
HEAD:backend/onyx/evals/eval.py:175:            forced_tool_ids: list[int] = []
HEAD:backend/onyx/evals/eval.py:176:            input_force_tools = eval_input.get("force_tools", [])
HEAD:backend/onyx/evals/eval.py:179:                from onyx.tools.built_in_tools import BUILT_IN_TOOL_MAP
HEAD:backend/onyx/evals/eval.py:182:                    if tool_type in BUILT_IN_TOOL_MAP:
HEAD:backend/onyx/evals/eval.py:184:                            db_session, BUILT_IN_TOOL_MAP[tool_type]
HEAD:backend/onyx/evals/eval.py:186:                        if tool_id not in forced_tool_ids:
HEAD:backend/onyx/evals/eval.py:187:                            forced_tool_ids.append(tool_id)
HEAD:backend/onyx/evals/eval.py:189:            # Build tool assertions from per-input config
HEAD:backend/onyx/evals/eval.py:191:            input_expected_tools = eval_input.get("expected_tools", [])
HEAD:backend/onyx/evals/eval.py:195:                    require_all=eval_input.get("require_all_tools", False),
HEAD:backend/onyx/evals/eval.py:222:            forced_tool_id = forced_tool_ids[0] if forced_tool_ids else None
HEAD:backend/onyx/evals/eval.py:226:                allowed_tool_ids=full_configuration.allowed_tool_ids,
HEAD:backend/onyx/evals/eval.py:268:def _get_multi_turn_answer_with_tools(
HEAD:backend/onyx/evals/eval.py:298:            expected_tools=msg_data.get("expected_tools", []),
HEAD:backend/onyx/evals/eval.py:299:            require_all_tools=msg_data.get("require_all_tools", False),
HEAD:backend/onyx/evals/eval.py:303:            force_tools=msg_data.get("force_tools", []),
HEAD:backend/onyx/evals/eval.py:343:                forced_tool_ids: list[int] = []
HEAD:backend/onyx/evals/eval.py:346:                    from onyx.tools.built_in_tools import BUILT_IN_TOOL_MAP
HEAD:backend/onyx/evals/eval.py:349:                        if tool_type in BUILT_IN_TOOL_MAP:
HEAD:backend/onyx/evals/eval.py:351:                                db_session, BUILT_IN_TOOL_MAP[tool_type]
HEAD:backend/onyx/evals/eval.py:353:                            if tool_id not in forced_tool_ids:
HEAD:backend/onyx/evals/eval.py:354:                                forced_tool_ids.append(tool_id)
HEAD:backend/onyx/evals/eval.py:356:                # Build tool assertions for this turn
HEAD:backend/onyx/evals/eval.py:380:                forced_tool_id = forced_tool_ids[0] if forced_tool_ids else None
HEAD:backend/onyx/evals/eval.py:386:                    allowed_tool_ids=full_configuration.allowed_tool_ids,
HEAD:backend/onyx/evals/eval.py:460:        task=lambda eval_input: _get_answer_with_tools(eval_input, configuration),
HEAD:backend/onyx/evals/eval.py:464:        multi_turn_task=lambda eval_input: _get_multi_turn_answer_with_tools(
HEAD:backend/onyx/evals/models.py:11:from onyx.tools.built_in_tools import BUILT_IN_TOOL_MAP
HEAD:backend/onyx/evals/models.py:82:    allowed_tool_ids: list[int]
HEAD:backend/onyx/evals/models.py:86:    builtin_tool_types: list[str] = list(BUILT_IN_TOOL_MAP.keys())
HEAD:backend/onyx/evals/models.py:104:            allowed_tool_ids=[
HEAD:backend/onyx/evals/models.py:105:                get_builtin_tool(db_session, BUILT_IN_TOOL_MAP[tool]).id
HEAD:backend/onyx/evals/providers/braintrust.py:135:                            "force_tools": item.get("force_tools", []),
HEAD:backend/onyx/evals/providers/braintrust.py:136:                            "expected_tools": item.get("expected_tools", []),
HEAD:backend/onyx/evals/providers/braintrust.py:137:                            "require_all_tools": item.get("require_all_tools", False),
HEAD:backend/onyx/evals/providers/local.py:144:        # Build input with tool and model config
HEAD:backend/onyx/evals/providers/local.py:148:            "force_tools": item.get("force_tools", []),
HEAD:backend/onyx/evals/providers/local.py:149:            "expected_tools": item.get("expected_tools", []),
HEAD:backend/onyx/evals/providers/local.py:150:            "require_all_tools": item.get("require_all_tools", False),
HEAD:backend/onyx/llm/tracing_wrap.py:121:        bound.arguments.get(_TOOLS_PARAM_NAME),
HEAD:backend/onyx/mcp_server/tools/search.py:100:    """Build the standard MCP error response envelope used by every tool."""
HEAD:backend/onyx/mcp_server/tools/search.py:456:        payload = WebSearchToolResponse.model_validate_json(response.content)
HEAD:backend/onyx/mcp_server/tools/search.py:511:        payload = OpenUrlsToolResponse.model_validate_json(response.content)
HEAD:backend/onyx/onyxbot/slack/handlers/handle_regular_answer.py:356:            allowed_tool_ids=None,
HEAD:backend/onyx/prompts/deep_research/research_agent.py:11:You iteratively call the tools available to you including {{available_tools}} until you have completed your research at which point you call the {GENERATE_REPORT_TOOL_NAME} tool.
HEAD:backend/onyx/prompts/deep_research/research_agent.py:75:You iteratively call the tools available to you including {{available_tools}} until you have completed your research at which point you call the {GENERATE_REPORT_TOOL_NAME} tool. Between calls, think about the results of the previous tool call and plan the next steps. \
HEAD:backend/onyx/server/features/build/configs.py:23:_disabled_tools_str = os.environ.get("OPENCODE_DISABLED_TOOLS", "question")
HEAD:backend/onyx/server/features/build/packets.py:83:    ``/build/apps/connect/{request_id}/decision`` to answer the agent's tool call.
HEAD:backend/onyx/server/features/build/sandbox/README.md:112:  `get_opencode_disabled_tools()` in `../utils.py`
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:163:from onyx.server.features.build.utils import get_opencode_disabled_tools
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:896:                disabled_tools=get_opencode_disabled_tools(),
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1109:            disabled_tools=get_opencode_disabled_tools(),
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1135:                disabled_tools=get_opencode_disabled_tools(),
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1565:                    disabled_tools=get_opencode_disabled_tools(),
HEAD:backend/onyx/server/features/build/sandbox/image/opencode-plugins/connect-app.ts:19:async function loadToolFactory(): Promise<typeof ToolFactory> {
HEAD:backend/onyx/server/features/build/sandbox/image/opencode-plugins/connect-app.ts:31:  const tool = await loadToolFactory();
HEAD:backend/onyx/server/features/build/sandbox/image/opencode-plugins/webapp.ts:20:async function loadToolFactory(): Promise<typeof ToolFactory> {
HEAD:backend/onyx/server/features/build/sandbox/image/opencode-plugins/webapp.ts:169:  const tool = await loadToolFactory();
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:152:from onyx.server.features.build.utils import get_opencode_disabled_tools
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1112:                    disabled_tools=get_opencode_disabled_tools(),
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1403:        disabled_tools = get_opencode_disabled_tools()
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1903:        disabled_tools = get_opencode_disabled_tools()
HEAD:backend/onyx/server/features/build/sandbox/models.py:39:    runtime hash so a hot reload fires when the server set or tools change."""
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:249:    """Build the ``content`` array expected by the consumer for a tool call.
HEAD:backend/onyx/server/features/build/sandbox/util/agent_instructions.py:141:    # Build disabled tools section
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:15:    get_mcp_tools_for_servers,
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:64:    for tool in get_mcp_tools_for_servers([s.id for s in servers], db_session):
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:211:        "permission": _build_permissions(disabled_tools, dev_mode),
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:246:        "permission": _build_permissions(disabled_tools, dev_mode, mcp_servers),
HEAD:backend/onyx/server/features/build/session/manager.py:109:from onyx.server.features.build.utils import get_opencode_disabled_tools
HEAD:backend/onyx/server/features/build/session/manager.py:291:                disabled_tools=get_opencode_disabled_tools(),
HEAD:backend/onyx/server/features/build/utils.py:189:def get_opencode_disabled_tools() -> list[str]:
HEAD:backend/onyx/server/features/default_assistant/api.py:41:    tool_ids = [tool.id for tool in persona.tools]
HEAD:backend/onyx/server/features/default_assistant/api.py:44:        tool_ids=tool_ids,
HEAD:backend/onyx/server/features/default_assistant/api.py:59:        update_request: Request with optional tool_ids and system_prompt
HEAD:backend/onyx/server/features/default_assistant/api.py:77:            tool_ids=update_request.tool_ids,
HEAD:backend/onyx/server/features/default_assistant/api.py:83:        tool_ids = [tool.id for tool in updated_persona.tools]
HEAD:backend/onyx/server/features/default_assistant/api.py:85:            tool_ids=tool_ids,
HEAD:backend/onyx/server/features/default_assistant/models.py:9:    tool_ids: list[int] = Field(
HEAD:backend/onyx/server/features/default_assistant/models.py:24:    tool_ids: list[int] | None = Field(
HEAD:backend/onyx/server/features/mcp/api.py:54:    get_all_mcp_tools_for_server,
HEAD:backend/onyx/server/features/mcp/api.py:75:    get_tools_by_mcp_server_id,
HEAD:backend/onyx/server/features/mcp/api.py:1397:@admin_router.get("/server/{server_id}/tools")
HEAD:backend/onyx/server/features/mcp/api.py:1398:def admin_list_mcp_tools_by_id(
HEAD:backend/onyx/server/features/mcp/api.py:1405:    return _list_mcp_tools_by_id(server_id, db, True, user)
HEAD:backend/onyx/server/features/mcp/api.py:1413:@admin_router.get("/server/{server_id}/tools/snapshots")
HEAD:backend/onyx/server/features/mcp/api.py:1414:def get_mcp_server_tools_snapshots(
HEAD:backend/onyx/server/features/mcp/api.py:1423:    Get tools for an MCP server as ToolSnapshot objects.
HEAD:backend/onyx/server/features/mcp/api.py:1430:    from onyx.db.tools import get_tools_by_mcp_server_id
HEAD:backend/onyx/server/features/mcp/api.py:1442:            _list_mcp_tools_by_id(server_id, db, True, user)
HEAD:backend/onyx/server/features/mcp/api.py:1470:    mcp_tools = get_tools_by_mcp_server_id(server_id, db, order_by_id=True)
HEAD:backend/onyx/server/features/mcp/api.py:1480:@router.get("/server/{server_id}/tools")
HEAD:backend/onyx/server/features/mcp/api.py:1481:def user_list_mcp_tools_by_id(
HEAD:backend/onyx/server/features/mcp/api.py:1486:    return _list_mcp_tools_by_id(server_id, db, False, user)
HEAD:backend/onyx/server/features/mcp/api.py:1546:    for db_tool in get_tools_by_mcp_server_id(mcp_server_id, db, order_by_id=True):
HEAD:backend/onyx/server/features/mcp/api.py:1565:def _list_mcp_tools_by_id(
HEAD:backend/onyx/server/features/mcp/api.py:2158:    existing_tools = get_tools_by_mcp_server_id(mcp_server.id, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:2203:@admin_router.get("/tools")
HEAD:backend/onyx/server/features/mcp/api.py:2204:def get_all_mcp_tools(
HEAD:backend/onyx/server/features/mcp/api.py:2210:    """Get all tools associated with MCP servers, including both enabled and disabled tools"""
HEAD:backend/onyx/server/features/mcp/api.py:2319:@admin_router.get("/server/{server_id}/db-tools")
HEAD:backend/onyx/server/features/mcp/api.py:2320:def get_mcp_server_db_tools(
HEAD:backend/onyx/server/features/mcp/api.py:2327:    """Get existing database tools created for an MCP server"""
HEAD:backend/onyx/server/features/mcp/api.py:2328:    logger.info("Getting database tools for MCP server: %s", server_id)
HEAD:backend/onyx/server/features/mcp/api.py:2338:    # Get all tools associated with this MCP server
HEAD:backend/onyx/server/features/mcp/api.py:2339:    mcp_tools = get_tools_by_mcp_server_id(server_id, db)
HEAD:backend/onyx/server/features/mcp/api.py:2611:        known = {t.name for t in get_all_mcp_tools_for_server(server_id, db_session)}
HEAD:backend/onyx/server/features/mcp/api.py:2675:        tools_to_delete = get_tools_by_mcp_server_id(server_id, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:2689:        remaining_tools = get_tools_by_mcp_server_id(server_id, db_session)
HEAD:backend/onyx/server/features/oauth_config/api.py:18:    get_tools_by_oauth_config,
HEAD:backend/onyx/server/features/oauth_config/api.py:48:    tools = get_tools_by_oauth_config(oauth_config.id, db_session)
HEAD:backend/onyx/server/features/oauth_config/api.py:75:    tools = get_tools_by_oauth_config(oauth_config.id, db_session)
HEAD:backend/onyx/server/features/persona/models.py:172:    tool_ids: list[int]
HEAD:backend/onyx/server/features/search/api.py:33:from onyx.db.tools import get_tools
HEAD:backend/onyx/server/features/search/api.py:151:    all_tools = get_tools(db_session)
HEAD:backend/onyx/server/features/tool/api.py:16:from onyx.db.persona import get_tool_ids_on_editable_personas
HEAD:backend/onyx/server/features/tool/api.py:23:    get_tool_ids_connected_to_groups,
HEAD:backend/onyx/server/features/tool/api.py:24:    get_tools,
HEAD:backend/onyx/server/features/tool/api.py:25:    get_tools_by_ids,
HEAD:backend/onyx/server/features/tool/api.py:230:    tool_ids: list[int]
HEAD:backend/onyx/server/features/tool/api.py:236:    tool_ids: list[int]
HEAD:backend/onyx/server/features/tool/api.py:252:    if not update_data.tool_ids:
HEAD:backend/onyx/server/features/tool/api.py:255:    tools = get_tools_by_ids(update_data.tool_ids, db_session)
HEAD:backend/onyx/server/features/tool/api.py:256:    tools_by_id = {tool.id: tool for tool in tools}
HEAD:backend/onyx/server/features/tool/api.py:261:    for tool_id in update_data.tool_ids:
HEAD:backend/onyx/server/features/tool/api.py:262:        tool = tools_by_id.get(tool_id)
HEAD:backend/onyx/server/features/tool/api.py:284:        tool_ids=updated_tools,
HEAD:backend/onyx/server/features/tool/api.py:309:def _connected_tool_ids(user: User, db_session: Session) -> set[int]:
HEAD:backend/onyx/server/features/tool/api.py:311:    edit, since the editor rebuilds tool_ids from this and drops whatever it never saw."""
HEAD:backend/onyx/server/features/tool/api.py:315:    return get_tool_ids_connected_to_groups(
HEAD:backend/onyx/server/features/tool/api.py:317:    ) | get_tool_ids_on_editable_personas(user, db_session)
HEAD:backend/onyx/server/features/tool/api.py:320:def _may_view_tool(tool: Tool, user: User, connected_tool_ids: set[int]) -> bool:
HEAD:backend/onyx/server/features/tool/api.py:325:    return can_manage_tool(user, tool) or tool.id in connected_tool_ids
HEAD:backend/onyx/server/features/tool/api.py:333:    tools = get_tools(db_session, only_openapi=True)
HEAD:backend/onyx/server/features/tool/api.py:334:    connected_tool_ids = _connected_tool_ids(user, db_session)
HEAD:backend/onyx/server/features/tool/api.py:340:        if not _may_view_tool(tool, user, connected_tool_ids):
HEAD:backend/onyx/server/features/tool/api.py:363:    if not _may_view_tool(tool, user, _connected_tool_ids(user, db_session)):
HEAD:backend/onyx/server/features/tool/api.py:376:    tools = get_tools(db_session, only_enabled=True, only_connected_mcp=True)
HEAD:backend/onyx/server/kg/api.py:113:    # Get the search and knowledge graph tools
HEAD:backend/onyx/server/kg/api.py:151:        tool_ids=[search_tool.id, kg_tool.id],
HEAD:backend/onyx/server/manage/models.py:91:    disabled_tool_ids: list[int]
HEAD:backend/onyx/server/manage/users.py:1432:            disabled_tool_ids=config.disabled_tool_ids
HEAD:backend/onyx/server/query_and_chat/models.py:115:    allowed_tool_ids: list[int] | None = None
HEAD:backend/onyx/server/query_and_chat/session_loading.py:691:                            memory_data = json.loads(tool_call.tool_call_response)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:716:                                response_data = json.loads(tool_call.tool_call_response)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:751:                            parsed = json.loads(tool_call.tool_call_response)
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:61:Configure the MCP client to launch `browser` with `["mcp"]`. The server defaults to MCP protocol 2025-11-25 and accepts older supported client protocol versions during initialization. The default tools profile is `core`, which keeps MCP context small for everyday browser automation. Use `--tools all` for the full typed CLI parity surface, or combine profiles with commas, such as `--tools core,network,react`. Profiles are `core`, `network`, `state`, `debug`, `tabs`, `react`, `mobile`, and `all`; the `debug` profile includes plugin registry and command.run tools. Each tool accepts typed arguments plus `extraArgs` for advanced CLI flags and exact CLI parity. Tool discovery is paginated and includes read-only/open-world annotations so modern MCP clients can load the large typed surface incrementally. Use the tool `session` argument or `AGENT_BROWSER_SESSION` to isolate browser sessions.
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1215:Tool calls use the same config files and environment variables as the CLI. Each tool accepts typed arguments plus `extraArgs` for advanced CLI flags and exact CLI parity. Tool discovery is paginated and includes read-only/open-world annotations so modern MCP clients can load the large typed surface incrementally. Use the `session` tool argument or `AGENT_BROWSER_SESSION` to isolate browser state.
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1423:Load the output JSON file in any of these tools:
HEAD:backend/onyx/tools/built_in_tools.py:35:BUILT_IN_TOOL_MAP: dict[str, Type[BUILT_IN_TOOL_TYPES]] = {
HEAD:backend/onyx/tools/built_in_tools.py:55:def get_built_in_tool_ids() -> list[str]:
HEAD:backend/onyx/tools/built_in_tools.py:56:    return list(BUILT_IN_TOOL_MAP.keys())
HEAD:backend/onyx/tools/built_in_tools.py:60:    return BUILT_IN_TOOL_MAP[in_code_tool_id]
HEAD:backend/onyx/tools/built_in_tools.py:75:def _build_tool_name_to_class() -> dict[str, Type[BUILT_IN_TOOL_TYPES]]:
HEAD:backend/onyx/tools/built_in_tools.py:76:    """Build a mapping from LLM-facing tool name to tool class."""
HEAD:backend/onyx/tools/built_in_tools.py:77:    return {_tool_llm_name(cls): cls for cls in BUILT_IN_TOOL_MAP.values()}
HEAD:backend/onyx/tools/built_in_tools.py:80:TOOL_NAME_TO_CLASS: dict[str, Type[BUILT_IN_TOOL_TYPES]] = _build_tool_name_to_class()
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:455:                    # Build ONE assistant message with all bash tool calls
HEAD:backend/onyx/tools/fake_tools/research_agent.py:290:                tools_by_name = {tool.name: tool for tool in current_tools}
HEAD:backend/onyx/tools/fake_tools/research_agent.py:317:                    available_tools=tools_description,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:514:                    # Build ONE ASSISTANT message with all tool calls (OpenAI parallel format)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:549:                        tool = tools_by_name.get(tc.tool_name)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:770:        persona = get_default_behavior_persona(db_session, eager_load_for_tools=True)
HEAD:backend/onyx/tools/tool_constructor.py:16:    get_all_mcp_tools_for_server,
HEAD:backend/onyx/tools/tool_constructor.py:39:    build_custom_tools_from_openapi_schema_and_headers,
HEAD:backend/onyx/tools/tool_constructor.py:126:    allowed_tool_ids: list[int] | None,
HEAD:backend/onyx/tools/tool_constructor.py:134:    if allowed_tool_ids is None:
HEAD:backend/onyx/tools/tool_constructor.py:138:        and tool.id not in allowed_tool_ids
HEAD:backend/onyx/tools/tool_constructor.py:152:    allowed_tool_ids: list[int] | None = None,
HEAD:backend/onyx/tools/tool_constructor.py:161:    (e.g. via ``eager_load_persona=True`` or ``eager_load_for_tools=True``)
HEAD:backend/onyx/tools/tool_constructor.py:173:            allowed_tool_ids=allowed_tool_ids,
HEAD:backend/onyx/tools/tool_constructor.py:187:    allowed_tool_ids: list[int] | None = None,
HEAD:backend/onyx/tools/tool_constructor.py:211:    def _build_search_tool(tool_id: int, config: SearchToolConfig) -> SearchTool:
HEAD:backend/onyx/tools/tool_constructor.py:235:        persona.tools, allowed_tool_ids
HEAD:backend/onyx/tools/tool_constructor.py:243:        # by any request that sends no allowed_tool_ids whitelist.
HEAD:backend/onyx/tools/tool_constructor.py:247:        # If allowed_tool_ids is specified, skip tools not in the allowed list
HEAD:backend/onyx/tools/tool_constructor.py:248:        if allowed_tool_ids is not None and db_tool_model.id not in allowed_tool_ids:
HEAD:backend/onyx/tools/tool_constructor.py:279:                    _build_search_tool(db_tool_model.id, search_tool_config)
HEAD:backend/onyx/tools/tool_constructor.py:432:                build_custom_tools_from_openapi_schema_and_headers(
HEAD:backend/onyx/tools/tool_constructor.py:468:            # Get all saved tools for this MCP server
HEAD:backend/onyx/tools/tool_constructor.py:469:            saved_tools = get_all_mcp_tools_for_server(mcp_server.id, db_session)
HEAD:backend/onyx/tools/tool_constructor.py:520:            _build_search_tool(search_tool_db_model.id, search_tool_config)
HEAD:backend/onyx/tools/tool_constructor.py:524:    # bypassing persona tool associations and allowed_tool_ids filtering
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:277:def build_custom_tools_from_openapi_schema_and_headers(
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:285:    """Build CustomTool instances from an OpenAPI schema.
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:388:    tools = build_custom_tools_from_openapi_schema_and_headers(
HEAD:backend/onyx/tools/tool_runner.py:302:    tools_by_name = {tool.name: tool for tool in tools}
HEAD:backend/onyx/tools/tool_runner.py:307:        if tool_call.tool_name not in tools_by_name:
HEAD:backend/onyx/tools/tool_runner.py:345:        tool = tools_by_name[tool_call.tool_name]
```
Tool availability is a distinct security decision from LLM tool selection.
## Tool / Agent Authorization
Evidence lines: 262
```text
HEAD:backend/ee/onyx/db/user_group.py:239:            selectinload(Persona.tools),
HEAD:backend/ee/onyx/server/seeding.py:97:                    user_id=tool.user_id,
HEAD:backend/ee/onyx/server/seeding.py:182:                    tool_ids=persona.tool_ids,
HEAD:backend/onyx/auth/permission_projection.py:118:class ToolPermissions(TypedDict):
HEAD:backend/onyx/auth/permission_projection.py:125:TOOL_ACTIONS: frozenset[str] = frozenset(ToolPermissions.__annotations__)
HEAD:backend/onyx/auth/permission_projection.py:128:def tool_permissions(*, can_manage: bool) -> dict[str, bool]:
HEAD:backend/onyx/auth/permission_projection.py:133:    result: ToolPermissions = {
HEAD:backend/onyx/chat/README.md:16:- If the user has just called a search related tool, then a section about citations is included
HEAD:backend/onyx/chat/README.md:73:tool is used, a citation reminder is always added. Otherwise, by default there is no reminder. If the user configures reminders, those are added to the
HEAD:backend/onyx/chat/README.md:74:final message. If a search related tool just ran and the user has reminders, both appear in a single message.
HEAD:backend/onyx/chat/README.md:106:S, U1, TC, TR, A1, CA, U2, A2  -- user sends another message, triggers tool call -> S, U1, TC, TR, A1, U2, A2, CA, U3, TC, TR, R, A3
HEAD:backend/onyx/chat/chat_state.py:204:    (e.g. ``setup.persona.tools[i].some_lazy_field``) or SQLAlchemy will raise
HEAD:backend/onyx/chat/chat_utils.py:110:    — the ID that FileReaderTool accepts (``UserFile.id`` for user files).
HEAD:backend/onyx/chat/chat_utils.py:647:    # Convert only the core USER/ASSISTANT messages; omit files and tool calls.
HEAD:backend/onyx/chat/chat_utils.py:778:                # Use user_file_id as the FileReaderTool accepts that.
HEAD:backend/onyx/chat/chat_utils.py:780:                tool_id = fd.get("user_file_id") or text_file.file_id
HEAD:backend/onyx/chat/compression.py:235:        # The verbatim tail had no USER message (e.g. a tool-heavy turn).
HEAD:backend/onyx/chat/llm_loop.py:49:from onyx.llm.interfaces import LLM, LLMUserIdentity, ToolChoiceOptions
HEAD:backend/onyx/chat/llm_loop.py:71:    CustomToolUserFileSnapshot,
HEAD:backend/onyx/chat/llm_loop.py:478:    # The history may contain tool calls and responses after the last user message
HEAD:backend/onyx/chat/llm_loop.py:491:    # 3. Messages after the last user message (tool calls, responses, etc.)
HEAD:backend/onyx/chat/llm_loop.py:611:    # 6. Add messages after last user message (tool calls, responses, etc.)
HEAD:backend/onyx/chat/llm_loop.py:1243:                    tool_response.rich_response.tool_result, CustomToolUserFileSnapshot
HEAD:backend/onyx/chat/llm_step.py:291:        message_history, (SystemMessage, UserMessage, AssistantMessage, ToolMessage)
HEAD:backend/onyx/chat/llm_step.py:744:    ) -> ToolMessage | UserMessage:
HEAD:backend/onyx/chat/llm_step.py:778:    def format_tool_response_message(self, msg: ChatMessageSimple) -> UserMessage:
HEAD:backend/onyx/chat/llm_step.py:866:    # Some providers flatten tool history into plain assistant/user text, so this split
HEAD:backend/onyx/chat/llm_step.py:1256:            # about which tool to call, not an actual answer to the user.
HEAD:backend/onyx/chat/process_message.py:175:    project/user files (``user_file`` IDs) so the tool can pick the right
HEAD:backend/onyx/chat/process_message.py:259:def _load_context_user_files_for_tools(
HEAD:backend/onyx/chat/process_message.py:428:            overflow_tool_metadata = [_build_tool_metadata(uf) for uf in user_files]
HEAD:backend/onyx/chat/process_message.py:514:def _build_tool_metadata(user_file: UserFile) -> FileToolMetadata:
HEAD:backend/onyx/chat/process_message.py:515:    """Build lightweight FileToolMetadata from a UserFile record.
HEAD:backend/onyx/chat/process_message.py:521:        tool_file_id=str(user_file.id),
HEAD:backend/onyx/chat/process_message.py:910:    # Also grant access to persona-attached user files for FileReaderTool
HEAD:backend/onyx/chat/process_message.py:945:        _load_context_user_files_for_tools(
HEAD:backend/onyx/chat/process_message.py:985:        tool.in_code_tool_id == FILE_READER_TOOL_ID for tool in persona.tools
HEAD:backend/onyx/chat/process_message.py:1170:        setup: Fully constructed turn context — LLMs, persona, history, tool config.
HEAD:backend/onyx/chat/process_message.py:1363:                allowed_tool_ids=setup.new_msg_req.allowed_tool_ids,
HEAD:backend/onyx/configs/app_configs.py:79:# are disabled but core chat, tools, user file uploads, and Projects still work.
HEAD:backend/onyx/db/chat.py:54:                selectinload(Persona.tools),
HEAD:backend/onyx/db/connector_credential_pair.py:439:def verify_user_has_access_to_cc_pair(
HEAD:backend/onyx/db/mcp.py:85:    """Servers already on a persona's tools. No attach ACL — chat users of the
HEAD:backend/onyx/db/mcp.py:88:    # Get the persona and its tools
HEAD:backend/onyx/db/mcp.py:93:    # Collect unique MCP server IDs from the persona's tools
HEAD:backend/onyx/db/mcp.py:95:    for tool in persona.tools:
HEAD:backend/onyx/db/mcp.py:148:    """Whether the user may add this server's tools to an agent."""
HEAD:backend/onyx/db/models.py:479:    # Custom tools created by this user
HEAD:backend/onyx/db/models.py:480:    custom_tools: Mapped[list["Tool"]] = relationship("Tool", back_populates="user")
HEAD:backend/onyx/db/models.py:839:class Persona__Tool(Base):
HEAD:backend/onyx/db/models.py:843:    For example, a persona may have the image generation tool attached to it, even though
HEAD:backend/onyx/db/models.py:848:    __tablename__ = "persona__tool"
HEAD:backend/onyx/db/models.py:3425:    # If this is not None, it's a top level tool call from the user message
HEAD:backend/onyx/db/models.py:4038:    # user who created / owns the tool. Will be None for built-in tools.
HEAD:backend/onyx/db/models.py:4054:    user: Mapped[User | None] = relationship("User", back_populates="custom_tools")
HEAD:backend/onyx/db/models.py:4061:        secondary=Persona__Tool.__table__,
HEAD:backend/onyx/db/models.py:4254:        secondary=Persona__Tool.__table__,
HEAD:backend/onyx/db/models.py:5870:    # When True, any user may add this server's tools to their agents.
HEAD:backend/onyx/db/oauth_config.py:7:from onyx.db.models import OAuthConfig, OAuthUserToken, Tool
HEAD:backend/onyx/db/persona.py:32:    Persona__Tool,
HEAD:backend/onyx/db/persona.py:75:            selectinload(Persona.tools),
HEAD:backend/onyx/db/persona.py:196:def get_tool_ids_on_editable_personas(user: User, db_session: Session) -> set[int]:
HEAD:backend/onyx/db/persona.py:197:    """Tools on agents this user may edit. The editor rebuilds an agent's tool_ids
HEAD:backend/onyx/db/persona.py:202:    # deleted agents keep their tool rows, and MANAGE_AGENTS skips _add_user_filters
HEAD:backend/onyx/db/persona.py:208:            select(Persona__Tool.tool_id).where(
HEAD:backend/onyx/db/persona.py:209:                Persona__Tool.persona_id.in_(editable_persona_ids)
HEAD:backend/onyx/db/persona.py:390:    if has_permission(user, Permission.MANAGE_AGENTS) is not PermissionAuthority.SCOPED:
HEAD:backend/onyx/db/persona.py:450:    if has_permission(user, Permission.MANAGE_AGENTS) is not PermissionAuthority.SCOPED:
HEAD:backend/onyx/db/persona.py:577:        if has_permission(user, Permission.MANAGE_AGENTS) is PermissionAuthority.SCOPED
HEAD:backend/onyx/db/persona.py:580:    is_manage_agents_admin = has_global_permission(user, Permission.MANAGE_AGENTS)
HEAD:backend/onyx/db/persona.py:584:        has_permission(user, Permission.ADD_AGENTS) is not PermissionAuthority.NONE
HEAD:backend/onyx/db/persona.py:637:                    "Only users with agent management permissions can make a featured persona"
HEAD:backend/onyx/db/persona.py:657:            tool_ids=create_persona_request.tool_ids,
HEAD:backend/onyx/db/persona.py:1046:        selectinload(Persona.tools),
HEAD:backend/onyx/db/persona.py:1098:        selectinload(Persona.tools),
HEAD:backend/onyx/db/persona.py:1210:        selectinload(Persona.tools),
HEAD:backend/onyx/db/persona.py:1294:        selectinload(Persona.tools),
HEAD:backend/onyx/db/persona.py:1634:                {tool.id for tool in existing_persona.tools}
HEAD:backend/onyx/db/persona.py:1766:        validate_persona_tools(tools, db_session)
HEAD:backend/onyx/db/persona.py:1824:            existing_persona.tools = tools or []
HEAD:backend/onyx/db/persona.py:1944:def validate_persona_tools(tools: list[Tool], db_session: Session) -> None:
HEAD:backend/onyx/db/persona.py:2083:def persona_has_search_tool(persona_id: int, db_session: Session) -> bool:
HEAD:backend/onyx/db/persona.py:2086:        .options(selectinload(Persona.tools))
HEAD:backend/onyx/db/persona.py:2092:    return any(tool.in_code_tool_id == "run_search" for tool in persona.tools)
HEAD:backend/onyx/db/persona.py:2099:        .options(selectinload(Persona.tools))
HEAD:backend/onyx/db/persona.py:2140:        persona.tools = []
HEAD:backend/onyx/db/persona.py:2155:            persona.tools.append(tool)
HEAD:backend/onyx/db/tools.py:15:    Persona__Tool,
HEAD:backend/onyx/db/tools.py:98:def can_manage_own_tool(user: User, tool: Tool) -> bool:
HEAD:backend/onyx/db/tools.py:107:        return tool.user_id is not None and tool.user_id == user.id
HEAD:backend/onyx/db/tools.py:123:def can_manage_tool(user: User, tool: Tool) -> bool:
HEAD:backend/onyx/db/tools.py:128:        return can_manage_mcp_server(user, tool.mcp_server)
HEAD:backend/onyx/db/tools.py:129:    return can_manage_own_tool(user, tool)
HEAD:backend/onyx/db/tools.py:149:            select(Tool.user_id).where(Tool.oauth_config_id == oauth_config_id)
HEAD:backend/onyx/db/tools.py:161:        .join(Persona__Tool, Persona__Tool.tool_id == Tool.id)
HEAD:backend/onyx/db/tools.py:162:        .join(Persona, Persona.id == Persona__Tool.persona_id)
HEAD:backend/onyx/db/tools.py:259:        tool.user_id = user_id
HEAD:backend/onyx/db/user_preferences.py:351:    """Update the disabled tools for a specific assistant for a specific user."""
HEAD:backend/onyx/deep_research/dr_loop.py:255:        allowed_tool_names = {SearchTool.NAME, WebSearchTool.NAME, OpenURLTool.NAME}
HEAD:backend/onyx/deep_research/dr_loop.py:256:        allowed_tools = [tool for tool in tools if tool.name in allowed_tool_names]
HEAD:backend/onyx/deep_research/dr_loop.py:257:        include_internal_search_tunings = SearchTool.NAME in allowed_tool_names
HEAD:backend/onyx/deep_research/dr_loop.py:718:                        tools=allowed_tools,
HEAD:backend/onyx/evals/eval.py:226:                allowed_tool_ids=full_configuration.allowed_tool_ids,
HEAD:backend/onyx/evals/eval.py:386:                    allowed_tool_ids=full_configuration.allowed_tool_ids,
HEAD:backend/onyx/evals/models.py:82:    allowed_tool_ids: list[int]
HEAD:backend/onyx/evals/models.py:104:            allowed_tool_ids=[
HEAD:backend/onyx/federated_connectors/federated_retrieval.py:235:                "Skipping Slack federated connector in user OAuth path - handled by SearchTool"
HEAD:backend/onyx/llm/models.py:240:ChatCompletionMessage = SystemMessage | UserMessage | AssistantMessage | ToolMessage
HEAD:backend/onyx/llm/multi_llm.py:308:            # Convert tool response to user message with text content
HEAD:backend/onyx/llm/multi_llm.py:313:            # tool result to avoid consecutive user messages (Bedrock requires
HEAD:backend/onyx/llm/multi_llm.py:322:                result.append({"role": "user", "content": tool_result_text})
HEAD:backend/onyx/llm/multi_llm.py:330:def _fix_tool_user_message_ordering(
HEAD:backend/onyx/llm/multi_llm.py:333:    """Insert a synthetic assistant message between tool and user messages.
HEAD:backend/onyx/llm/multi_llm.py:336:    a user message cannot immediately follow a tool message. This function
HEAD:backend/onyx/llm/multi_llm.py:346:        if prev_role == "tool" and curr_role == "user":
HEAD:backend/onyx/llm/multi_llm.py:932:            optional_kwargs["allowed_openai_params"] = ["tool_choice"]
HEAD:backend/onyx/llm/multi_llm.py:1026:                messages = _fix_tool_user_message_ordering(messages)
HEAD:backend/onyx/mcp_server/tools/search.py:283:    Use this tool for information that is not public knowledge and specific to the user,
HEAD:backend/onyx/onyxbot/slack/handlers/handle_regular_answer.py:344:                for tool in persona.tools
HEAD:backend/onyx/onyxbot/slack/handlers/handle_regular_answer.py:356:            allowed_tool_ids=None,
HEAD:backend/onyx/prompts/chat_prompts.py:16:Whenever there is any ambiguity around the user's query (or more information would be helpful), you use available tools (if any) to get more context.
HEAD:backend/onyx/prompts/chat_tools.py:12:You can use tools to look up information that may be helpful in answering the user's \
HEAD:backend/onyx/prompts/chat_tools.py:42:# For the case where the user has not configured any tools to call, but still using the tool-flow
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:10:You operate in a read-only, network-isolated sandbox with the repository checked out at the working directory of every `{BASH_TOOL_NAME}` call. Iteratively call `{BASH_TOOL_NAME}` to inspect the codebase, then call `{GENERATE_ANSWER_TOOL_NAME}` once you have gathered enough evidence to answer the user's query comprehensively.
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:109:You are an expert code investigator. You produce the final answer to the user's query using only the bash output and reasoning in the conversation history. You no longer have tools.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:11:CRITICAL - Never directly answer the user's query, you must only ask clarifying questions or call the `{GENERATE_PLAN_TOOL_NAME}` tool.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:13:If the user query is already very detailed or lengthy (more than 3 sentences), do not ask for clarification and instead call the `{GENERATE_PLAN_TOOL_NAME}` tool.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:68:Before calling {GENERATE_REPORT_TOOL_NAME}, reason to double check that all aspects of the user's query have been well researched and that all key topics around the plan have been researched. \
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:82:CRITICAL - the {RESEARCH_AGENT_TOOL_NAME} only receives the task and has no additional context about the user's query, research plan, other research agents, or message history. \
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:102:Before calling {GENERATE_REPORT_TOOL_NAME}, double check that all aspects of the user's query have been researched and that all key topics around the plan have been researched (unless you have gone in a different direction).
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:147:Ignore the format styles of the intermediate {RESEARCH_AGENT_TOOL_NAME} reports, those are not end user facing and different from your task.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:160:Before calling {GENERATE_REPORT_TOOL_NAME}, reason to double check that all aspects of the user's query have been well researched and that all key topics around the plan have been researched.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:175:CRITICAL - the {RESEARCH_AGENT_TOOL_NAME} only receives the task and has no additional context about the user's query, research plan, or message history. \
HEAD:backend/onyx/prompts/prompt_utils.py:316:            raise ValueError("Last message must be user input OR a tool result")
HEAD:backend/onyx/prompts/tool_prompts.py:8:For questions that can be answered from existing knowledge, answer the user directly without using any tools. \
HEAD:backend/onyx/prompts/tool_prompts.py:13:When using any search type tool, do not make any assumptions and stay as faithful to the user's query as possible. \
HEAD:backend/onyx/prompts/tool_prompts.py:15:When searching for information, if the initial results cannot fully answer the user's query, try again with different tools or arguments. \
HEAD:backend/onyx/prompts/tool_prompts.py:48:Use the `open_url` tool to read the content of one or more URLs. Use this tool to access the contents of the most promising web pages from your web searches or user specified URLs. \
HEAD:backend/onyx/prompts/tool_prompts.py:51:You should almost always use open_url after a web_search call. Use this tool when a user asks about a specific provided URL.
HEAD:backend/onyx/prompts/tool_prompts.py:73:File IDs come from `[attached image — file_id: <id>]` tags on user-attached images or from prior `generate_image` tool results — never invent one. \
HEAD:backend/onyx/prompts/tool_prompts.py:79:Use the `add_memory` tool for facts shared by the user that should be remembered for future conversations. \
HEAD:backend/onyx/server/documents/connector.py:81:    verify_user_has_access_to_cc_pair,
HEAD:backend/onyx/server/documents/connector.py:408:    has_requested_access = verify_user_has_access_to_cc_pair(
HEAD:backend/onyx/server/features/build/AGENTS.template.md:53:Some org apps aren't set up for this user yet, so you can't call them until they're connected. When the task needs one, call the `connect_app` tool with its numeric external app ID from the list below; once connected, it works like any other app. Never ask for or handle credentials yourself.
HEAD:backend/onyx/server/features/build/packets.py:79:    """The agent's ``connect_app`` tool is asking the user to connect an org app.
HEAD:backend/onyx/server/features/build/sandbox/README.md:105:- **Tool permissions**: File operations, bash commands, web access
HEAD:backend/onyx/server/features/build/sandbox/README.md:106:- **Disabled tools**: Resolved deployment-wide (not per-user) via the
HEAD:backend/onyx/server/features/build/sandbox/README.md:300:### Adding New Tools/Permissions
HEAD:backend/onyx/server/features/build/sandbox/README.md:302:Update `util/opencode_config.py` to add/remove tool permissions in the `permission` section.
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:203:# Surfaces the no-op `connect_app` tool; always on. Its "ask" permission is what
HEAD:backend/onyx/server/features/build/sandbox/image/opencode-plugins/connect-app.ts:1:// A no-op `connect_app` tool the agent calls to ask the user to connect an org
HEAD:backend/onyx/server/features/build/sandbox/image/templates/outputs/web/AGENTS.md:522:5. **Accessible** - Use `ChartTooltip` with `ChartTooltipContent` for proper styling
HEAD:backend/onyx/server/features/build/sandbox/image/templates/outputs/web/bun.lock:878:    "radix-ui": ["radix-ui@1.4.3", "", { "dependencies": { "@radix-ui/primitive": "1.1.3", "@radix-ui/react-accessible-icon": "1.1.7", "@radix-ui/react-accordion": "1.2.12", "@radix-ui/react-alert-dialog": "1.1.15", "@radix-ui/react-arrow": "1.1.7", "@radix-ui/react-aspect-ratio": "1.1.7", "@radix-ui/react-avatar": "1.1.10", "@radix-ui/react-checkbox": "1.3.3", "@radix-ui/react-collapsible": "1.1.12", "@radix-ui/react-collection": "1.1.7", "@radix-ui/react-compose-refs": "1.1.2", "@radix-ui/react-context": "1.1.2", "@radix-ui/react-context-menu": "2.2.16", "@radix-ui/react-dialog": "1.1.15", "@radix-ui/react-direction": "1.1.1", "@radix-ui/react-dismissable-layer": "1.1.11", "@radix-ui/react-dropdown-menu": "2.1.16", "@radix-ui/react-focus-guards": "1.1.3", "@radix-ui/react-focus-scope": "1.1.7", "@radix-ui/react-form": "0.1.8", "@radix-ui/react-hover-card": "1.1.15", "@radix-ui/react-label": "2.1.7", "@radix-ui/react-menu": "2.1.16", "@radix-ui/react-menubar": "1.1.16", "@radix-ui/react-navigation-menu": "1.2.14", "@radix-ui/react-one-time-password-field": "0.1.8", "@radix-ui/react-password-toggle-field": "0.1.3", "@radix-ui/react-popover": "1.1.15", "@radix-ui/react-popper": "1.2.8", "@radix-ui/react-portal": "1.1.9", "@radix-ui/react-presence": "1.1.5", "@radix-ui/react-primitive": "2.1.3", "@radix-ui/react-progress": "1.1.7", "@radix-ui/react-radio-group": "1.3.8", "@radix-ui/react-roving-focus": "1.1.11", "@radix-ui/react-scroll-area": "1.2.10", "@radix-ui/react-select": "2.2.6", "@radix-ui/react-separator": "1.1.7", "@radix-ui/react-slider": "1.3.6", "@radix-ui/react-slot": "1.2.3", "@radix-ui/react-switch": "1.2.6", "@radix-ui/react-tabs": "1.1.13", "@radix-ui/react-toast": "1.2.15", "@radix-ui/react-toggle": "1.1.10", "@radix-ui/react-toggle-group": "1.1.11", "@radix-ui/react-toolbar": "1.1.11", "@radix-ui/react-tooltip": "1.2.8", "@radix-ui/react-use-callback-ref": "1.1.1", "@radix-ui/react-use-controllable-state": "1.2.2", "@radix-ui/react-use-effect-event": "0.0.2", "@radix-ui/react-use-escape-keydown": "1.1.1", "@radix-ui/react-use-is-hydrated": "0.1.0", "@radix-ui/react-use-layout-effect": "1.1.1", "@radix-ui/react-use-size": "1.1.1", "@radix-ui/react-visually-hidden": "1.2.3" }, "peerDependencies": { "@types/react": "*", "@types/react-dom": "*", "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc", "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc" } }, "sha512-aWizCQiyeAenIdUbqEpXgRA1ya65P13NKn/W8rWkcN0OPkRDxdBVLWnIEDsS2RpwCK2nobI7oMUSmexzTDyAmA=="],
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:178:# Surfaces the no-op `connect_app` tool; always on. Its "ask" permission is what
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:65:# opencode permission category emitted by the no-op ``connect_app`` tool
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:116:            permissions[tool] = "deny"
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:122:            permissions[f"{server.key}_{tool_name}"] = "deny"
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:211:        "permission": _build_permissions(disabled_tools, dev_mode),
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:246:        "permission": _build_permissions(disabled_tools, dev_mode, mcp_servers),
HEAD:backend/onyx/server/features/default_assistant/api.py:40:    # Extract DB tool IDs from the persona's tools
HEAD:backend/onyx/server/features/default_assistant/api.py:41:    tool_ids = [tool.id for tool in persona.tools]
HEAD:backend/onyx/server/features/default_assistant/api.py:83:        tool_ids = [tool.id for tool in updated_persona.tools]
HEAD:backend/onyx/server/features/mcp/api.py:20:from onyx.auth.permission_projection import mcp_server_permissions, tool_permissions
HEAD:backend/onyx/server/features/mcp/api.py:67:from onyx.db.models import MCPConnectionConfig, Tool, User
HEAD:backend/onyx/server/features/mcp/api.py:979:    # OAuth connect unblocks tool discovery for this user's craft session;
HEAD:backend/onyx/server/features/mcp/api.py:1114:    # Disconnecting revokes tool discovery for this user; reload their craft
HEAD:backend/onyx/server/features/mcp/api.py:1405:    return _list_mcp_tools_by_id(server_id, db, True, user)
HEAD:backend/onyx/server/features/mcp/api.py:1442:            _list_mcp_tools_by_id(server_id, db, True, user)
HEAD:backend/onyx/server/features/mcp/api.py:1474:            permissions=tool_permissions(can_manage=can_manage_tool(user, tool)),
HEAD:backend/onyx/server/features/mcp/api.py:1481:def user_list_mcp_tools_by_id(
HEAD:backend/onyx/server/features/mcp/api.py:1486:    return _list_mcp_tools_by_id(server_id, db, False, user)
HEAD:backend/onyx/server/features/mcp/api.py:2150:    Updates to the db model of a tool all happen when the user Lists Tools.
HEAD:backend/onyx/server/features/mcp/api.py:2151:    This ensures that the the tools added to the db match what the user sees in the UI,
HEAD:backend/onyx/server/features/mcp/models.py:294:            "If True, any user may add this server's tools to their agents. "
HEAD:backend/onyx/server/features/mcp/models.py:428:            "If True, any user may add this server's tools to their agents. "
HEAD:backend/onyx/server/features/mcp/models.py:460:            "If True, any user may add this server's tools to their agents. "
HEAD:backend/onyx/server/features/mcp/oauth.py:3:Used by chat tool calls (`MCPTool.run`), the admin/user MCP API routes, and the
HEAD:backend/onyx/server/features/oauth_config/api.py:76:    if tools and all(tool.user_id == user.id for tool in tools):
HEAD:backend/onyx/server/features/persona/api.py:244:    if has_permission(user, Permission.READ_AGENTS) is PermissionAuthority.SCOPED:
HEAD:backend/onyx/server/features/persona/api.py:753:            holds_add_agents=has_permission(user, Permission.ADD_AGENTS)
HEAD:backend/onyx/server/features/persona/api.py:755:            is_manage_agents_admin=has_global_permission(
HEAD:backend/onyx/server/features/persona/models.py:171:    # e.g. ID of SearchTool or ImageGenerationTool or <USER_DEFINED_TOOL>
HEAD:backend/onyx/server/features/persona/models.py:283:                for tool in persona.tools
HEAD:backend/onyx/server/features/persona/models.py:375:                for tool in persona.tools
HEAD:backend/onyx/server/features/persona/models.py:458:                for tool in persona.tools
HEAD:backend/onyx/server/features/tool/api.py:7:from onyx.auth.permission_projection import tool_permissions
HEAD:backend/onyx/server/features/tool/api.py:14:from onyx.db.models import Tool, User
HEAD:backend/onyx/server/features/tool/api.py:16:from onyx.db.persona import get_tool_ids_on_editable_personas
HEAD:backend/onyx/server/features/tool/api.py:101:def _get_manageable_custom_tool(tool_id: int, db_session: Session, user: User) -> Tool:
HEAD:backend/onyx/server/features/tool/api.py:113:    if not can_manage_tool(user, tool):
HEAD:backend/onyx/server/features/tool/api.py:158:    _assert_can_link_oauth_config(tool_data.oauth_config_id, db_session, user)
HEAD:backend/onyx/server/features/tool/api.py:184:    existing_tool = _get_manageable_custom_tool(tool_id, db_session, user)
HEAD:backend/onyx/server/features/tool/api.py:202:        user_id=existing_tool.user_id,
HEAD:backend/onyx/server/features/tool/api.py:218:    _ = _get_manageable_custom_tool(tool_id, db_session, user)
HEAD:backend/onyx/server/features/tool/api.py:264:            if not can_manage_tool(user, tool):
HEAD:backend/onyx/server/features/tool/api.py:309:def _connected_tool_ids(user: User, db_session: Session) -> set[int]:
HEAD:backend/onyx/server/features/tool/api.py:310:    """Tools viewable without managing them — including those on agents the user can
HEAD:backend/onyx/server/features/tool/api.py:317:    ) | get_tool_ids_on_editable_personas(user, db_session)
HEAD:backend/onyx/server/features/tool/api.py:320:def _may_view_tool(tool: Tool, user: User, connected_tool_ids: set[int]) -> bool:
HEAD:backend/onyx/server/features/tool/api.py:325:    return can_manage_tool(user, tool) or tool.id in connected_tool_ids
HEAD:backend/onyx/server/features/tool/api.py:334:    connected_tool_ids = _connected_tool_ids(user, db_session)
HEAD:backend/onyx/server/features/tool/api.py:340:        if not _may_view_tool(tool, user, connected_tool_ids):
HEAD:backend/onyx/server/features/tool/api.py:346:                permissions=tool_permissions(can_manage=can_manage_tool(user, tool)),
HEAD:backend/onyx/server/features/tool/api.py:363:    if not _may_view_tool(tool, user, _connected_tool_ids(user, db_session)):
HEAD:backend/onyx/server/features/tool/api.py:378:    # Attach catalog: omit MCP tools the user cannot put on a persona.
HEAD:backend/onyx/server/features/tool/models.py:52:        cls, tool: Tool, *, permissions: dict[str, bool] | None = None
HEAD:backend/onyx/server/features/tool/models.py:68:            user_id=str(tool.user_id) if tool.user_id else None,
HEAD:backend/onyx/server/manage/llm/api.py:1658:    # Strip /v1 suffix that users may copy from OpenAI-compatible tool configs;
HEAD:backend/onyx/server/manage/models.py:125:    # controls which tools are enabled for the user for a specific assistant
HEAD:backend/onyx/server/manage/models.py:248:                enable_memory_tool=user.enable_memory_tool,
HEAD:backend/onyx/server/manage/users.py:1330:        else user.enable_memory_tool
HEAD:backend/onyx/server/onyx_api/ingestion.py:14:    verify_user_has_access_to_cc_pair,
HEAD:backend/onyx/server/onyx_api/ingestion.py:67:    if not verify_user_has_access_to_cc_pair(cc_pair_id, db_session, user):
HEAD:backend/onyx/server/onyx_api/ingestion.py:130:    if not verify_user_has_access_to_cc_pair(target_cc_pair_id, db_session, user):
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:198:        num_tools=len(persona.tools),
HEAD:backend/onyx/server/query_and_chat/models.py:115:    allowed_tool_ids: list[int] | None = None
HEAD:backend/onyx/server/query_and_chat/models.py:124:    # Headers to forward to MCP tool calls (e.g., user JWT token, user ID)
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:289:# The allowed streamed packets for a custom tool
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:4:allowed-tools: Bash(browser:*)
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1352:browser profiler start --categories "devtools.timeline,v8.execute,blink.user_timing"
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:2060:  Tell the user exactly this: "Open DevTools → Network, click any authenticated request, right-click → Copy → Copy as cURL, paste the whole thing into a file, and give me the path."
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:2076:`--init-script <path>` and `--enable <feature>` register scripts that run before any page JS. That's exactly why they work, and it's also why you should only pass scripts you wrote or have reviewed. The built-in `--enable react-devtools` is a vendored MIT-licensed hook from facebook/react and is safe; custom `--init-script` files are the user's responsibility.
HEAD:backend/onyx/skills/models.py:25:    allowed_tools: str | None = Field(default=None, alias="allowed-tools")
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:192:    """Run a final, no-tool LLM step that produces the user-facing answer."""
HEAD:backend/onyx/tools/fake_tools/research_agent.py:770:        persona = get_default_behavior_persona(db_session, eager_load_for_tools=True)
HEAD:backend/onyx/tools/interface.py:48:        """Should be the name of the tool displayed to the user"""
HEAD:backend/onyx/tools/interface.py:87:        # For example when calling the internal search tool, the original user query is passed along too (but not by the LLM)
HEAD:backend/onyx/tools/models.py:57:class CustomToolUserFileSnapshot(BaseModel):
HEAD:backend/onyx/tools/tool_constructor.py:125:    persona_tools: Sequence[ToolDBModel],
HEAD:backend/onyx/tools/tool_constructor.py:126:    allowed_tool_ids: list[int] | None,
HEAD:backend/onyx/tools/tool_constructor.py:134:    if allowed_tool_ids is None:
HEAD:backend/onyx/tools/tool_constructor.py:138:        and tool.id not in allowed_tool_ids
HEAD:backend/onyx/tools/tool_constructor.py:139:        for tool in persona_tools
HEAD:backend/onyx/tools/tool_constructor.py:152:    allowed_tool_ids: list[int] | None = None,
HEAD:backend/onyx/tools/tool_constructor.py:159:    Callers must supply a persona with ``tools``, ``document_sets``,
HEAD:backend/onyx/tools/tool_constructor.py:161:    (e.g. via ``eager_load_persona=True`` or ``eager_load_for_tools=True``)
HEAD:backend/onyx/tools/tool_constructor.py:173:            allowed_tool_ids=allowed_tool_ids,
HEAD:backend/onyx/tools/tool_constructor.py:187:    allowed_tool_ids: list[int] | None = None,
HEAD:backend/onyx/tools/tool_constructor.py:193:    persona_tool_names = [t.name for t in persona.tools]
HEAD:backend/onyx/tools/tool_constructor.py:198:        persona_tool_names,
HEAD:backend/onyx/tools/tool_constructor.py:235:        persona.tools, allowed_tool_ids
HEAD:backend/onyx/tools/tool_constructor.py:239:    for db_tool_model in persona.tools:
HEAD:backend/onyx/tools/tool_constructor.py:241:        # tool is not necessarily a usable one (see Persona__Tool). Only the tool
HEAD:backend/onyx/tools/tool_constructor.py:243:        # by any request that sends no allowed_tool_ids whitelist.
HEAD:backend/onyx/tools/tool_constructor.py:247:        # If allowed_tool_ids is specified, skip tools not in the allowed list
HEAD:backend/onyx/tools/tool_constructor.py:248:        if allowed_tool_ids is not None and db_tool_model.id not in allowed_tool_ids:
HEAD:backend/onyx/tools/tool_constructor.py:404:                        "Anonymous user cannot use OAuth tool %s", db_tool_model.id
HEAD:backend/onyx/tools/tool_constructor.py:424:                        "Anonymous user cannot use passthrough auth tool %s",
HEAD:backend/onyx/tools/tool_constructor.py:428:                oauth_token_for_tool = user_oauth_token
HEAD:backend/onyx/tools/tool_constructor.py:448:                    user_oauth_token=oauth_token_for_tool,
HEAD:backend/onyx/tools/tool_constructor.py:523:    # Always inject MemoryTool when the user has the memory tool enabled,
HEAD:backend/onyx/tools/tool_constructor.py:524:    # bypassing persona tool associations and allowed_tool_ids filtering
HEAD:backend/onyx/tools/tool_constructor.py:525:    if user.enable_memory_tool:
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:29:    CustomToolUserFileSnapshot,
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:222:            tool_result = CustomToolUserFileSnapshot(file_ids=file_ids)
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:229:            tool_result = CustomToolUserFileSnapshot(file_ids=file_ids)
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:129:                                " user-attached images or from prior generate_image tool responses."
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:2:Memory Tool for storing user-specific information.
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:4:This tool allows the LLM to save memories about the user for future conversations.
HEAD:backend/onyx/tools/tool_name.py:4:# OpenAI imposes the same constraint on function names. User-supplied Tool.name
HEAD:backend/onyx/tools/tool_runner.py:274:        user_memory_context: User memory context, if available (passed through to `SearchTool`).
HEAD:backend/onyx/tools/tool_runner.py:275:        user_info: User information string, if available (passed through to `SearchTool`).
```
Static authorization-related mechanisms were captured where present.
Their completeness and correctness are not proven by this action.
## LLM Tool-Call Production and Parsing
Evidence lines: 650
```text
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:330:                tool_calls=None,
HEAD:backend/ee/onyx/server/gateway/api.py:45:from onyx.llm.model_response import ChatCompletionMessageToolCall
HEAD:backend/ee/onyx/server/gateway/api.py:50:    NamedToolChoice,
HEAD:backend/ee/onyx/server/gateway/api.py:56:    ToolChoice,
HEAD:backend/ee/onyx/server/gateway/api.py:57:    ToolChoiceOptions,
HEAD:backend/ee/onyx/server/gateway/api.py:62:from onyx.llm.tracing_wrap import _finalize_tool_calls
HEAD:backend/ee/onyx/server/gateway/api.py:212:            and not message.tool_calls
HEAD:backend/ee/onyx/server/gateway/api.py:267:def _parse_tool_choice(raw: Any) -> ToolChoice | None:
HEAD:backend/ee/onyx/server/gateway/api.py:272:            return ToolChoiceOptions(raw)
HEAD:backend/ee/onyx/server/gateway/api.py:276:                f"Unsupported tool_choice {raw!r}; expected one of "
HEAD:backend/ee/onyx/server/gateway/api.py:277:                f"{', '.join(option.value for option in ToolChoiceOptions)}.",
HEAD:backend/ee/onyx/server/gateway/api.py:285:            return NamedToolChoice(name=name)
HEAD:backend/ee/onyx/server/gateway/api.py:286:        raise OnyxError(OnyxErrorCode.INVALID_INPUT, "tool_choice names no function.")
HEAD:backend/ee/onyx/server/gateway/api.py:289:        f"Unsupported tool_choice {raw!r}.",
HEAD:backend/ee/onyx/server/gateway/api.py:310:    tool_choice: ToolChoice | None,
HEAD:backend/ee/onyx/server/gateway/api.py:341:                tool_choice=tool_choice,
HEAD:backend/ee/onyx/server/gateway/api.py:374:    tool_choice = _parse_tool_choice(request.tool_choice)
HEAD:backend/ee/onyx/server/gateway/api.py:375:    _require_named_tool(tool_choice, request.tools)
HEAD:backend/ee/onyx/server/gateway/api.py:387:                "tool_choice": tool_choice,
HEAD:backend/ee/onyx/server/gateway/api.py:408:                tool_choice=tool_choice,
HEAD:backend/ee/onyx/server/gateway/api.py:504:def _function_call_item(
HEAD:backend/ee/onyx/server/gateway/api.py:505:    tool_call: ToolCall | ChatCompletionMessageToolCall,
HEAD:backend/ee/onyx/server/gateway/api.py:507:    # A nameless tool call has no valid function_call representation.
HEAD:backend/ee/onyx/server/gateway/api.py:508:    name = tool_call.function.name
HEAD:backend/ee/onyx/server/gateway/api.py:513:        call_id=tool_call.id,
HEAD:backend/ee/onyx/server/gateway/api.py:515:        arguments=tool_call.function.arguments or "",
HEAD:backend/ee/onyx/server/gateway/api.py:521:    tool_calls: list[ToolCall] | list[ChatCompletionMessageToolCall] | None,
HEAD:backend/ee/onyx/server/gateway/api.py:535:        for item in (_function_call_item(tc) for tc in tool_calls or [])
HEAD:backend/ee/onyx/server/gateway/api.py:546:    tool_choice: ToolChoice | None,
HEAD:backend/ee/onyx/server/gateway/api.py:637:                tool_choice=tool_choice,
HEAD:backend/ee/onyx/server/gateway/api.py:686:                        _function_call_item(tool_call)
HEAD:backend/ee/onyx/server/gateway/api.py:687:                        for tool_call in _finalize_tool_calls(state.tool_call_buffer)
HEAD:backend/ee/onyx/server/gateway/api.py:748:    tool_choice = _parse_tool_choice(request.tool_choice)
HEAD:backend/ee/onyx/server/gateway/api.py:749:    _require_named_tool(tool_choice, tools)
HEAD:backend/ee/onyx/server/gateway/api.py:765:                "tool_choice": tool_choice,
HEAD:backend/ee/onyx/server/gateway/api.py:787:                tool_choice=tool_choice,
HEAD:backend/ee/onyx/server/gateway/api.py:821:            response.choice.message.tool_calls,
HEAD:backend/ee/onyx/server/gateway/api.py:943:def _anthropic_tool_choice(raw: dict[str, Any] | None) -> ToolChoice | None:
HEAD:backend/ee/onyx/server/gateway/api.py:948:        return ToolChoiceOptions.AUTO
HEAD:backend/ee/onyx/server/gateway/api.py:950:        return ToolChoiceOptions.REQUIRED
HEAD:backend/ee/onyx/server/gateway/api.py:952:        return ToolChoiceOptions.NONE
HEAD:backend/ee/onyx/server/gateway/api.py:956:            return NamedToolChoice(name=name)
HEAD:backend/ee/onyx/server/gateway/api.py:957:        raise OnyxError(OnyxErrorCode.INVALID_INPUT, "tool_choice names no function.")
HEAD:backend/ee/onyx/server/gateway/api.py:960:        f"Unsupported tool_choice type {choice_type!r}; expected one of "
HEAD:backend/ee/onyx/server/gateway/api.py:966:    tool_choice: ToolChoice | None, tools: list[dict[str, Any]] | None
HEAD:backend/ee/onyx/server/gateway/api.py:968:    """A named tool_choice referencing an absent tool would fail opaquely
HEAD:backend/ee/onyx/server/gateway/api.py:970:    if not isinstance(tool_choice, NamedToolChoice):
HEAD:backend/ee/onyx/server/gateway/api.py:977:    if tool_choice.name not in tool_names:
HEAD:backend/ee/onyx/server/gateway/api.py:980:            f"tool_choice names unknown tool {tool_choice.name!r}.",
HEAD:backend/ee/onyx/server/gateway/api.py:1014:    "tool_calls": "tool_use",
HEAD:backend/ee/onyx/server/gateway/api.py:1056:    tool_calls: list[ToolCall] | list[ChatCompletionMessageToolCall] | None,
HEAD:backend/ee/onyx/server/gateway/api.py:1059:    for tool_call in tool_calls or []:
HEAD:backend/ee/onyx/server/gateway/api.py:1060:        name = tool_call.function.name
HEAD:backend/ee/onyx/server/gateway/api.py:1063:        arguments = tool_call.function.arguments
HEAD:backend/ee/onyx/server/gateway/api.py:1071:            AnthropicToolUseBlock.create(id=tool_call.id, name=name, input=parsed_input)
HEAD:backend/ee/onyx/server/gateway/api.py:1081:    tool_choice: ToolChoice | None,
HEAD:backend/ee/onyx/server/gateway/api.py:1208:                tool_choice=tool_choice,
HEAD:backend/ee/onyx/server/gateway/api.py:1243:                finalized_tool_calls = _finalize_tool_calls(state.tool_call_buffer)
HEAD:backend/ee/onyx/server/gateway/api.py:1244:                tool_blocks = _anthropic_tool_use_blocks(finalized_tool_calls)
HEAD:backend/ee/onyx/server/gateway/api.py:1245:                named_tool_calls = [
HEAD:backend/ee/onyx/server/gateway/api.py:1246:                    tc for tc in finalized_tool_calls or [] if tc.function.name
HEAD:backend/ee/onyx/server/gateway/api.py:1248:                for tool_index, (tool_block, tool_call) in enumerate(
HEAD:backend/ee/onyx/server/gateway/api.py:1249:                    zip(tool_blocks, named_tool_calls, strict=True), start=next_index
HEAD:backend/ee/onyx/server/gateway/api.py:1263:                                partial_json=tool_call.function.arguments or "{}"
HEAD:backend/ee/onyx/server/gateway/api.py:1299:    tool_choice = _anthropic_tool_choice(request.tool_choice)
HEAD:backend/ee/onyx/server/gateway/api.py:1300:    _require_named_tool(tool_choice, tools)
HEAD:backend/ee/onyx/server/gateway/api.py:1315:                "tool_choice": tool_choice,
HEAD:backend/ee/onyx/server/gateway/api.py:1336:                tool_choice=tool_choice,
HEAD:backend/ee/onyx/server/gateway/api.py:1370:        tool_blocks = _anthropic_tool_use_blocks(response.choice.message.tool_calls)
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:375:                tool_calls=None,
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:16:    ChatCompletionDeltaToolCall,
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:21:from onyx.llm.tracing_wrap import _finalize_tool_calls, _merge_tool_call_delta
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:59:        self.tool_call_buffer: dict[int, ChatCompletionDeltaToolCall] = {}
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:72:        for delta_tc in chunk.choice.delta.tool_calls:
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:73:            _merge_tool_call_delta(self.tool_call_buffer, delta_tc)
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:140:                    tool_calls=_finalize_tool_calls(state.tool_call_buffer),
HEAD:backend/onyx/chat/chat_state.py:48:        self.tool_calls: list[ToolCallInfo] = []
HEAD:backend/onyx/chat/chat_state.py:67:    def add_tool_call(self, tool_call: ToolCallInfo) -> None:
HEAD:backend/onyx/chat/chat_state.py:70:            self.tool_calls.append(tool_call)
HEAD:backend/onyx/chat/chat_state.py:112:    def get_tool_calls(self) -> list[ToolCallInfo]:
HEAD:backend/onyx/chat/chat_state.py:113:        """Thread-safe getter for tool_calls (returns a copy)."""
HEAD:backend/onyx/chat/chat_state.py:115:            return self.tool_calls.copy()
HEAD:backend/onyx/chat/chat_utils.py:63:    TOOL_CALL_RESPONSE_CROSS_MESSAGE,
HEAD:backend/onyx/chat/chat_utils.py:65:from onyx.prompts.tool_prompts import TOOL_CALL_FAILURE_PROMPT
HEAD:backend/onyx/chat/chat_utils.py:244:    prefetch_top_two_level_tool_calls: bool = True,
HEAD:backend/onyx/chat/chat_utils.py:257:        prefetch_top_two_level_tool_calls=prefetch_top_two_level_tool_calls,
HEAD:backend/onyx/chat/chat_utils.py:689:def _build_tool_call_response_history_message(
HEAD:backend/onyx/chat/chat_utils.py:692:    tool_call_response: str | None,
HEAD:backend/onyx/chat/chat_utils.py:695:        return TOOL_CALL_RESPONSE_CROSS_MESSAGE
HEAD:backend/onyx/chat/chat_utils.py:717:    if tool_call_response:
HEAD:backend/onyx/chat/chat_utils.py:718:        return tool_call_response
HEAD:backend/onyx/chat/chat_utils.py:720:    return TOOL_CALL_RESPONSE_CROSS_MESSAGE
HEAD:backend/onyx/chat/chat_utils.py:734:    For assistant messages with tool calls: creates ONE ASSISTANT message with tool_calls array,
HEAD:backend/onyx/chat/chat_utils.py:735:        followed by N TOOL_CALL_RESPONSE messages (OpenAI parallel tool calling format)
HEAD:backend/onyx/chat/chat_utils.py:830:            # 2. For each turn: ONE ASSISTANT message with tool_calls array
HEAD:backend/onyx/chat/chat_utils.py:831:            # 3. Followed by N TOOL_CALL_RESPONSE messages (one per tool call)
HEAD:backend/onyx/chat/chat_utils.py:832:            if chat_message.tool_calls:
HEAD:backend/onyx/chat/chat_utils.py:834:                tool_calls_by_turn: dict[int, list] = {}
HEAD:backend/onyx/chat/chat_utils.py:835:                for tool_call in chat_message.tool_calls:
HEAD:backend/onyx/chat/chat_utils.py:836:                    if tool_call.turn_number not in tool_calls_by_turn:
HEAD:backend/onyx/chat/chat_utils.py:837:                        tool_calls_by_turn[tool_call.turn_number] = []
HEAD:backend/onyx/chat/chat_utils.py:838:                    tool_calls_by_turn[tool_call.turn_number].append(tool_call)
HEAD:backend/onyx/chat/chat_utils.py:841:                for turn_number in sorted(tool_calls_by_turn.keys()):
HEAD:backend/onyx/chat/chat_utils.py:842:                    turn_tool_calls = tool_calls_by_turn[turn_number]
HEAD:backend/onyx/chat/chat_utils.py:844:                    turn_tool_calls.sort(key=lambda tc: tc.tool_id)
HEAD:backend/onyx/chat/chat_utils.py:847:                    tool_calls_simple: list[ToolCallSimple] = []
HEAD:backend/onyx/chat/chat_utils.py:848:                    for tool_call in turn_tool_calls:
HEAD:backend/onyx/chat/chat_utils.py:850:                            tool_call.tool_id, "unknown"
HEAD:backend/onyx/chat/chat_utils.py:852:                        tool_calls_simple.append(
HEAD:backend/onyx/chat/chat_utils.py:854:                                tool_call_id=tool_call.tool_call_id,
HEAD:backend/onyx/chat/chat_utils.py:856:                                tool_arguments=tool_call.tool_call_arguments or {},
HEAD:backend/onyx/chat/chat_utils.py:857:                                token_count=tool_call.tool_call_tokens,
HEAD:backend/onyx/chat/chat_utils.py:862:                    total_tool_call_tokens = sum(
HEAD:backend/onyx/chat/chat_utils.py:863:                        tc.token_count for tc in tool_calls_simple
HEAD:backend/onyx/chat/chat_utils.py:868:                            token_count=total_tool_call_tokens,
HEAD:backend/onyx/chat/chat_utils.py:870:                            tool_calls=tool_calls_simple,
HEAD:backend/onyx/chat/chat_utils.py:875:                    # Add TOOL_CALL_RESPONSE messages for each tool call in this turn
HEAD:backend/onyx/chat/chat_utils.py:876:                    for tool_call in turn_tool_calls:
HEAD:backend/onyx/chat/chat_utils.py:878:                            tool_call.tool_id, "unknown"
HEAD:backend/onyx/chat/chat_utils.py:881:                            _build_tool_call_response_history_message(
HEAD:backend/onyx/chat/chat_utils.py:883:                                generated_images=tool_call.generated_images,
HEAD:backend/onyx/chat/chat_utils.py:884:                                tool_call_response=tool_call.tool_call_response,
HEAD:backend/onyx/chat/chat_utils.py:891:                                message_type=MessageType.TOOL_CALL_RESPONSE,
HEAD:backend/onyx/chat/chat_utils.py:892:                                tool_call_id=tool_call.tool_call_id,
HEAD:backend/onyx/chat/chat_utils.py:966:def create_tool_call_failure_messages(
HEAD:backend/onyx/chat/chat_utils.py:967:    tool_calls: list[ToolCallKickoff], token_counter: Callable[[str], int]
HEAD:backend/onyx/chat/chat_utils.py:972:    1. An ASSISTANT message with tool_calls field containing all failed tool calls
HEAD:backend/onyx/chat/chat_utils.py:973:    2. A TOOL_CALL_RESPONSE failure message for each tool call
HEAD:backend/onyx/chat/chat_utils.py:976:        tool_calls: List of ToolCallKickoff objects representing the failed tool calls
HEAD:backend/onyx/chat/chat_utils.py:983:    if not tool_calls:
HEAD:backend/onyx/chat/chat_utils.py:987:    tool_calls_simple: list[ToolCallSimple] = []
HEAD:backend/onyx/chat/chat_utils.py:988:    for tool_call in tool_calls:
HEAD:backend/onyx/chat/chat_utils.py:989:        tool_call_token_count = token_counter(tool_call.to_msg_str())
HEAD:backend/onyx/chat/chat_utils.py:990:        tool_calls_simple.append(
HEAD:backend/onyx/chat/chat_utils.py:992:                tool_call_id=tool_call.tool_call_id,
HEAD:backend/onyx/chat/chat_utils.py:993:                tool_name=tool_call.tool_name,
HEAD:backend/onyx/chat/chat_utils.py:994:                tool_arguments=tool_call.tool_args,
HEAD:backend/onyx/chat/chat_utils.py:995:                token_count=tool_call_token_count,
HEAD:backend/onyx/chat/chat_utils.py:999:    total_token_count = sum(tc.token_count for tc in tool_calls_simple)
HEAD:backend/onyx/chat/chat_utils.py:1001:    # Create ONE ASSISTANT message with all tool_calls (OpenAI format)
HEAD:backend/onyx/chat/chat_utils.py:1006:        tool_calls=tool_calls_simple,
HEAD:backend/onyx/chat/chat_utils.py:1012:    # Create a TOOL_CALL_RESPONSE failure message for each tool call
HEAD:backend/onyx/chat/chat_utils.py:1013:    for tool_call in tool_calls:
HEAD:backend/onyx/chat/chat_utils.py:1015:            message=TOOL_CALL_FAILURE_PROMPT,
HEAD:backend/onyx/chat/chat_utils.py:1017:            message_type=MessageType.TOOL_CALL_RESPONSE,
HEAD:backend/onyx/chat/chat_utils.py:1018:            tool_call_id=tool_call.tool_call_id,
HEAD:backend/onyx/chat/citation_utils.py:20:        tool_response: The response from the tool execution (must have tool_call set)
HEAD:backend/onyx/chat/citation_utils.py:23:    # Early return if tool_call is not set
HEAD:backend/onyx/chat/citation_utils.py:24:    if tool_response.tool_call is None:
HEAD:backend/onyx/chat/citation_utils.py:28:    if tool_response.tool_call.tool_name in CITEABLE_TOOLS_NAMES:
HEAD:backend/onyx/chat/compression.py:83:        for tool_call in m.tool_calls or []:
HEAD:backend/onyx/chat/compression.py:84:            total += tool_call.tool_call_tokens or 0
HEAD:backend/onyx/chat/compression.py:268:    - Skips TOOL_CALL_RESPONSE messages entirely (tool usage captured in assistant message)
HEAD:backend/onyx/chat/compression.py:281:            if msg.tool_calls:
HEAD:backend/onyx/chat/compression.py:283:                    tool_id_to_name.get(tc.tool_id, "unknown") for tc in msg.tool_calls
HEAD:backend/onyx/chat/compression.py:293:        if msg.message_type == MessageType.TOOL_CALL_RESPONSE:
HEAD:backend/onyx/chat/compression.py:404:    be detached, but callers must have eager-loaded the ``tool_calls``
HEAD:backend/onyx/chat/compression.py:406:    ``prefetch_top_two_level_tool_calls=True``); ``_build_llm_messages_for_summarization``
HEAD:backend/onyx/chat/compression.py:407:    walks ``msg.tool_calls`` and would raise ``DetachedInstanceError`` if
HEAD:backend/onyx/chat/llm_loop.py:10:    create_tool_call_failure_messages,
HEAD:backend/onyx/chat/llm_loop.py:20:    _looks_like_xml_tool_call_payload,
HEAD:backend/onyx/chat/llm_loop.py:21:    extract_tool_calls_from_response_text,
HEAD:backend/onyx/chat/llm_loop.py:49:from onyx.llm.interfaces import LLM, LLMUserIdentity, ToolChoiceOptions
HEAD:backend/onyx/chat/llm_loop.py:85:from onyx.tools.tool_runner import run_tool_calls
HEAD:backend/onyx/chat/llm_loop.py:106:        tool_choice: ToolChoiceOptions,
HEAD:backend/onyx/chat/llm_loop.py:119:        self.tool_choice = tool_choice
HEAD:backend/onyx/chat/llm_loop.py:151:    tool_choice: ToolChoiceOptions,
HEAD:backend/onyx/chat/llm_loop.py:167:            tool_choice=tool_choice,
HEAD:backend/onyx/chat/llm_loop.py:190:            tool_choice=tool_choice,
HEAD:backend/onyx/chat/llm_loop.py:205:        tool_choice=tool_choice,
HEAD:backend/onyx/chat/llm_loop.py:217:    tool_choice: ToolChoiceOptions,
HEAD:backend/onyx/chat/llm_loop.py:230:        tool_choice: The tool choice option used for this step
HEAD:backend/onyx/chat/llm_loop.py:241:    no_tool_calls = (
HEAD:backend/onyx/chat/llm_loop.py:242:        not llm_step_result.tool_calls or len(llm_step_result.tool_calls) == 0
HEAD:backend/onyx/chat/llm_loop.py:245:        llm_step_result.reasoning and not llm_step_result.answer and no_tool_calls
HEAD:backend/onyx/chat/llm_loop.py:247:    xml_tool_call_text_detected = no_tool_calls and (
HEAD:backend/onyx/chat/llm_loop.py:248:        _looks_like_xml_tool_call_payload(llm_step_result.answer)
HEAD:backend/onyx/chat/llm_loop.py:249:        or _looks_like_xml_tool_call_payload(llm_step_result.raw_answer)
HEAD:backend/onyx/chat/llm_loop.py:250:        or _looks_like_xml_tool_call_payload(llm_step_result.reasoning)
HEAD:backend/onyx/chat/llm_loop.py:253:        (tool_choice == ToolChoiceOptions.REQUIRED and no_tool_calls)
HEAD:backend/onyx/chat/llm_loop.py:255:        or xml_tool_call_text_detected
HEAD:backend/onyx/chat/llm_loop.py:262:    extracted_tool_calls: list[ToolCallKickoff] = []
HEAD:backend/onyx/chat/llm_loop.py:265:        extracted_tool_calls = extract_tool_calls_from_response_text(
HEAD:backend/onyx/chat/llm_loop.py:271:        not extracted_tool_calls
HEAD:backend/onyx/chat/llm_loop.py:275:        extracted_tool_calls = extract_tool_calls_from_response_text(
HEAD:backend/onyx/chat/llm_loop.py:280:    if not extracted_tool_calls and llm_step_result.reasoning:
HEAD:backend/onyx/chat/llm_loop.py:281:        extracted_tool_calls = extract_tool_calls_from_response_text(
HEAD:backend/onyx/chat/llm_loop.py:286:    if extracted_tool_calls:
HEAD:backend/onyx/chat/llm_loop.py:289:            len(extracted_tool_calls),
HEAD:backend/onyx/chat/llm_loop.py:295:                tool_calls=extracted_tool_calls,
HEAD:backend/onyx/chat/llm_loop.py:618:    return _drop_orphaned_tool_call_responses(result)
HEAD:backend/onyx/chat/llm_loop.py:621:def _drop_orphaned_tool_call_responses(
HEAD:backend/onyx/chat/llm_loop.py:624:    """Drop tool response messages whose tool_call_id is not in prior assistant tool calls.
HEAD:backend/onyx/chat/llm_loop.py:627:    leaves a later TOOL_CALL_RESPONSE message in context. Some providers (e.g. Ollama)
HEAD:backend/onyx/chat/llm_loop.py:630:    known_tool_call_ids: set[str] = set()
HEAD:backend/onyx/chat/llm_loop.py:634:        if msg.message_type == MessageType.ASSISTANT and msg.tool_calls:
HEAD:backend/onyx/chat/llm_loop.py:635:            for tool_call in msg.tool_calls:
HEAD:backend/onyx/chat/llm_loop.py:636:                known_tool_call_ids.add(tool_call.tool_call_id)
HEAD:backend/onyx/chat/llm_loop.py:640:        if msg.message_type == MessageType.TOOL_CALL_RESPONSE:
HEAD:backend/onyx/chat/llm_loop.py:641:            if msg.tool_call_id and msg.tool_call_id in known_tool_call_ids:
HEAD:backend/onyx/chat/llm_loop.py:645:                    "Dropping orphaned tool response with tool_call_id=%s while constructing message history",
HEAD:backend/onyx/chat/llm_loop.py:646:                    msg.tool_call_id,
HEAD:backend/onyx/chat/llm_loop.py:808:            tool_calls=None,
HEAD:backend/onyx/chat/llm_loop.py:824:        tool_choice: ToolChoiceOptions = ToolChoiceOptions.AUTO
HEAD:backend/onyx/chat/llm_loop.py:889:                tool_choice = ToolChoiceOptions.REQUIRED
HEAD:backend/onyx/chat/llm_loop.py:893:                tool_choice = ToolChoiceOptions.NONE
HEAD:backend/onyx/chat/llm_loop.py:896:                tool_choice = ToolChoiceOptions.AUTO
HEAD:backend/onyx/chat/llm_loop.py:1060:                tool_choice=tool_choice,
HEAD:backend/onyx/chat/llm_loop.py:1081:                tool_choice=tool_choice,
HEAD:backend/onyx/chat/llm_loop.py:1096:            tool_calls = llm_step_result.tool_calls or []
HEAD:backend/onyx/chat/llm_loop.py:1098:            if INTEGRATION_TESTS_MODE and tool_calls:
HEAD:backend/onyx/chat/llm_loop.py:1099:                for tool_call in tool_calls:
HEAD:backend/onyx/chat/llm_loop.py:1102:                            placement=tool_call.placement,
HEAD:backend/onyx/chat/llm_loop.py:1104:                                tool_call_id=tool_call.tool_call_id,
HEAD:backend/onyx/chat/llm_loop.py:1105:                                tool_name=tool_call.tool_name,
HEAD:backend/onyx/chat/llm_loop.py:1106:                                tool_args=tool_call.tool_args,
HEAD:backend/onyx/chat/llm_loop.py:1111:            if len(tool_calls) > 1:
HEAD:backend/onyx/chat/llm_loop.py:1115:                            turn_index=tool_calls[0].placement.turn_index
HEAD:backend/onyx/chat/llm_loop.py:1117:                        obj=TopLevelBranching(num_parallel_branches=len(tool_calls)),
HEAD:backend/onyx/chat/llm_loop.py:1128:            parallel_tool_call_results = run_tool_calls(
HEAD:backend/onyx/chat/llm_loop.py:1129:                tool_calls=tool_calls,
HEAD:backend/onyx/chat/llm_loop.py:1142:            tool_responses = parallel_tool_call_results.tool_responses
HEAD:backend/onyx/chat/llm_loop.py:1143:            citation_mapping = parallel_tool_call_results.updated_citation_mapping
HEAD:backend/onyx/chat/llm_loop.py:1146:            if tool_calls and not tool_responses:
HEAD:backend/onyx/chat/llm_loop.py:1147:                failure_messages = create_tool_call_failure_messages(
HEAD:backend/onyx/chat/llm_loop.py:1148:                    tool_calls, token_counter
HEAD:backend/onyx/chat/llm_loop.py:1154:                # Extract tool_call from the response (set by run_tool_calls)
HEAD:backend/onyx/chat/llm_loop.py:1155:                if tool_response.tool_call is None:
HEAD:backend/onyx/chat/llm_loop.py:1156:                    raise ValueError("Tool response missing tool_call reference")
HEAD:backend/onyx/chat/llm_loop.py:1158:                tool_call = tool_response.tool_call
HEAD:backend/onyx/chat/llm_loop.py:1159:                tab_index = tool_call.placement.tab_index
HEAD:backend/onyx/chat/llm_loop.py:1162:                if tool_call.tool_name == SearchTool.NAME:
HEAD:backend/onyx/chat/llm_loop.py:1167:                    tool_call.tool_name == PythonTool.NAME
HEAD:backend/onyx/chat/llm_loop.py:1182:                tool = tools_by_name.get(tool_call.tool_name)
HEAD:backend/onyx/chat/llm_loop.py:1185:                        f"Tool '{tool_call.tool_name}' not found in tools list"
HEAD:backend/onyx/chat/llm_loop.py:1206:                    if search_docs and tool_call.tool_name == WebSearchTool.NAME:
HEAD:backend/onyx/chat/llm_loop.py:1302:                tool_call_info = ToolCallInfo(
HEAD:backend/onyx/chat/llm_loop.py:1303:                    parent_tool_call_id=None,  # Top-level tool calls are attached to the chat message
HEAD:backend/onyx/chat/llm_loop.py:1306:                    tool_name=tool_call.tool_name,
HEAD:backend/onyx/chat/llm_loop.py:1307:                    tool_call_id=tool_call.tool_call_id,
HEAD:backend/onyx/chat/llm_loop.py:1310:                    tool_call_arguments=tool_call.tool_args,
HEAD:backend/onyx/chat/llm_loop.py:1311:                    tool_call_response=saved_response,
HEAD:backend/onyx/chat/llm_loop.py:1318:                state_container.add_tool_call(tool_call_info)
HEAD:backend/onyx/chat/llm_loop.py:1327:            # 1. ONE ASSISTANT message with tool_calls array
HEAD:backend/onyx/chat/llm_loop.py:1328:            # 2. N TOOL_CALL_RESPONSE messages (one per tool call)
HEAD:backend/onyx/chat/llm_loop.py:1330:                # Filter to only responses with valid tool_call references
HEAD:backend/onyx/chat/llm_loop.py:1332:                    tr for tr in tool_responses if tr.tool_call is not None
HEAD:backend/onyx/chat/llm_loop.py:1336:                tool_calls_simple: list[ToolCallSimple] = []
HEAD:backend/onyx/chat/llm_loop.py:1338:                    tc = tool_response.tool_call
HEAD:backend/onyx/chat/llm_loop.py:1343:                    tool_call_message = tc.to_msg_str()
HEAD:backend/onyx/chat/llm_loop.py:1344:                    tool_call_token_count = token_counter(tool_call_message)
HEAD:backend/onyx/chat/llm_loop.py:1346:                    tool_calls_simple.append(
HEAD:backend/onyx/chat/llm_loop.py:1348:                            tool_call_id=tc.tool_call_id,
HEAD:backend/onyx/chat/llm_loop.py:1351:                            token_count=tool_call_token_count,
HEAD:backend/onyx/chat/llm_loop.py:1356:                total_tool_call_tokens = sum(tc.token_count for tc in tool_calls_simple)
HEAD:backend/onyx/chat/llm_loop.py:1359:                    token_count=total_tool_call_tokens,
HEAD:backend/onyx/chat/llm_loop.py:1361:                    tool_calls=tool_calls_simple,
HEAD:backend/onyx/chat/llm_loop.py:1366:                # Add TOOL_CALL_RESPONSE messages for each tool call
HEAD:backend/onyx/chat/llm_loop.py:1368:                    tc = tool_response.tool_call
HEAD:backend/onyx/chat/llm_loop.py:1377:                        message_type=MessageType.TOOL_CALL_RESPONSE,
HEAD:backend/onyx/chat/llm_loop.py:1378:                        tool_call_id=tc.tool_call_id,
HEAD:backend/onyx/chat/llm_loop.py:1384:            if not llm_step_result.tool_calls or len(llm_step_result.tool_calls) == 0:
HEAD:backend/onyx/chat/llm_loop.py:1390:                for tool in llm_step_result.tool_calls
HEAD:backend/onyx/chat/llm_loop.py:1394:            if llm_step_result.tool_calls and any(
HEAD:backend/onyx/chat/llm_loop.py:1396:                for tool in llm_step_result.tool_calls
HEAD:backend/onyx/chat/llm_loop.py:1401:        if not llm_step_result.answer and not llm_step_result.tool_calls:
HEAD:backend/onyx/chat/llm_loop.py:1405:                tool_choice=tool_choice,
HEAD:backend/onyx/chat/llm_step.py:14:from onyx.chat.tool_call_args_streaming import maybe_emit_argument_delta
HEAD:backend/onyx/chat/llm_step.py:29:    ToolChoiceOptions,
HEAD:backend/onyx/chat/llm_step.py:85:_FUNCTION_CALLS_OPEN_MARKER = "<function_calls"
HEAD:backend/onyx/chat/llm_step.py:86:_FUNCTION_CALLS_CLOSE_MARKER = "</function_calls>"
HEAD:backend/onyx/chat/llm_step.py:94:        self._inside_function_calls_block = False
HEAD:backend/onyx/chat/llm_step.py:106:            if self._inside_function_calls_block:
HEAD:backend/onyx/chat/llm_step.py:107:                end_idx = pending_lower.find(_FUNCTION_CALLS_CLOSE_MARKER)
HEAD:backend/onyx/chat/llm_step.py:112:                # Drop the whole function_calls block.
HEAD:backend/onyx/chat/llm_step.py:114:                    end_idx + len(_FUNCTION_CALLS_CLOSE_MARKER) :
HEAD:backend/onyx/chat/llm_step.py:116:                self._inside_function_calls_block = False
HEAD:backend/onyx/chat/llm_step.py:119:            start_idx = _find_function_calls_open_marker(pending_lower)
HEAD:backend/onyx/chat/llm_step.py:121:                # Keep only a possible prefix of "<function_calls" in the buffer so
HEAD:backend/onyx/chat/llm_step.py:135:            self._inside_function_calls_block = True
HEAD:backend/onyx/chat/llm_step.py:140:        if self._inside_function_calls_block:
HEAD:backend/onyx/chat/llm_step.py:143:            self._inside_function_calls_block = False
HEAD:backend/onyx/chat/llm_step.py:152:    """Return longest suffix of text that matches prefix of "<function_calls"."""
HEAD:backend/onyx/chat/llm_step.py:153:    max_len = min(len(text), len(_FUNCTION_CALLS_OPEN_MARKER) - 1)
HEAD:backend/onyx/chat/llm_step.py:155:    marker_lower = _FUNCTION_CALLS_OPEN_MARKER
HEAD:backend/onyx/chat/llm_step.py:164:def _is_valid_function_calls_open_follower(char: str | None) -> bool:
HEAD:backend/onyx/chat/llm_step.py:168:def _find_function_calls_open_marker(text_lower: str) -> int:
HEAD:backend/onyx/chat/llm_step.py:169:    """Find '<function_calls' with a valid tag boundary follower."""
HEAD:backend/onyx/chat/llm_step.py:172:        idx = text_lower.find(_FUNCTION_CALLS_OPEN_MARKER, search_from)
HEAD:backend/onyx/chat/llm_step.py:176:        follower_pos = idx + len(_FUNCTION_CALLS_OPEN_MARKER)
HEAD:backend/onyx/chat/llm_step.py:178:        if _is_valid_function_calls_open_follower(follower):
HEAD:backend/onyx/chat/llm_step.py:184:def _looks_like_xml_tool_call_payload(text: str | None) -> bool:
HEAD:backend/onyx/chat/llm_step.py:188:    (e.g. <function_calls><invoke name="get_time"></invoke></function_calls>) are
HEAD:backend/onyx/chat/llm_step.py:189:    valid tool calls that _extract_xml_tool_calls_from_response_text can parse, so
HEAD:backend/onyx/chat/llm_step.py:196:    return "<function_calls" in lowered and "<invoke" in lowered
HEAD:backend/onyx/chat/llm_step.py:322:            if msg.tool_calls:
HEAD:backend/onyx/chat/llm_step.py:324:                for tool_call in msg.tool_calls:
HEAD:backend/onyx/chat/llm_step.py:325:                    tool_call_dict: dict[str, Any] = {
HEAD:backend/onyx/chat/llm_step.py:326:                        "id": tool_call.id,
HEAD:backend/onyx/chat/llm_step.py:327:                        "type": tool_call.type,
HEAD:backend/onyx/chat/llm_step.py:329:                            "name": tool_call.function.name,
HEAD:backend/onyx/chat/llm_step.py:330:                            "arguments": tool_call.function.arguments,
HEAD:backend/onyx/chat/llm_step.py:333:                    tool_call_json = json.dumps(tool_call_dict, indent=4)
HEAD:backend/onyx/chat/llm_step.py:334:                    formatted_lines.append(tool_call_json)
HEAD:backend/onyx/chat/llm_step.py:339:            formatted_lines.append(f"Tool call ID: {msg.tool_call_id}")
HEAD:backend/onyx/chat/llm_step.py:355:def _update_tool_call_with_delta(
HEAD:backend/onyx/chat/llm_step.py:356:    tool_calls_in_progress: dict[int, dict[str, Any]],
HEAD:backend/onyx/chat/llm_step.py:357:    tool_call_delta: Any,
HEAD:backend/onyx/chat/llm_step.py:359:    index = tool_call_delta.index
HEAD:backend/onyx/chat/llm_step.py:361:    if index not in tool_calls_in_progress:
HEAD:backend/onyx/chat/llm_step.py:362:        tool_calls_in_progress[index] = {
HEAD:backend/onyx/chat/llm_step.py:369:    if tool_call_delta.id:
HEAD:backend/onyx/chat/llm_step.py:370:        tool_calls_in_progress[index]["id"] = tool_call_delta.id
HEAD:backend/onyx/chat/llm_step.py:372:    if tool_call_delta.function:
HEAD:backend/onyx/chat/llm_step.py:373:        if tool_call_delta.function.name:
HEAD:backend/onyx/chat/llm_step.py:374:            tool_calls_in_progress[index]["name"] = tool_call_delta.function.name
HEAD:backend/onyx/chat/llm_step.py:376:        if tool_call_delta.function.arguments:
HEAD:backend/onyx/chat/llm_step.py:377:            tool_calls_in_progress[index]["arguments"] += (
HEAD:backend/onyx/chat/llm_step.py:378:                tool_call_delta.function.arguments
HEAD:backend/onyx/chat/llm_step.py:382:def _extract_tool_call_kickoffs(
HEAD:backend/onyx/chat/llm_step.py:383:    id_to_tool_call_map: dict[int, dict[str, Any]],
HEAD:backend/onyx/chat/llm_step.py:395:        id_to_tool_call_map: Map of tool call index to tool call data
HEAD:backend/onyx/chat/llm_step.py:401:    tool_calls: list[ToolCallKickoff] = []
HEAD:backend/onyx/chat/llm_step.py:403:    for tool_call_data in id_to_tool_call_map.values():
HEAD:backend/onyx/chat/llm_step.py:404:        if tool_call_data.get("id") and tool_call_data.get("name"):
HEAD:backend/onyx/chat/llm_step.py:405:            tool_args = _parse_tool_args_to_dict(tool_call_data.get("arguments"))
HEAD:backend/onyx/chat/llm_step.py:407:            tool_calls.append(
HEAD:backend/onyx/chat/llm_step.py:409:                    tool_call_id=tool_call_data["id"],
HEAD:backend/onyx/chat/llm_step.py:410:                    tool_name=tool_call_data["name"],
HEAD:backend/onyx/chat/llm_step.py:422:    return tool_calls
HEAD:backend/onyx/chat/llm_step.py:425:def extract_tool_calls_from_response_text(
HEAD:backend/onyx/chat/llm_step.py:460:    matched_tool_calls: list[tuple[str, dict[str, Any]]] = []
HEAD:backend/onyx/chat/llm_step.py:464:    prev_tool_call: tuple[str, dict[str, Any]] | None = None
HEAD:backend/onyx/chat/llm_step.py:467:        matched_tool_call = _try_match_json_to_tool(json_obj, tool_name_to_def)
HEAD:backend/onyx/chat/llm_step.py:468:        if not matched_tool_call:
HEAD:backend/onyx/chat/llm_step.py:476:            and prev_tool_call is not None
HEAD:backend/onyx/chat/llm_step.py:477:            and matched_tool_call == prev_tool_call
HEAD:backend/onyx/chat/llm_step.py:486:        matched_tool_calls.append(matched_tool_call)
HEAD:backend/onyx/chat/llm_step.py:488:        prev_tool_call = matched_tool_call
HEAD:backend/onyx/chat/llm_step.py:492:    if not matched_tool_calls:
HEAD:backend/onyx/chat/llm_step.py:493:        matched_tool_calls = _extract_xml_tool_calls_from_response_text(
HEAD:backend/onyx/chat/llm_step.py:498:    tool_calls: list[ToolCallKickoff] = []
HEAD:backend/onyx/chat/llm_step.py:499:    for tab_index, (tool_name, tool_args) in enumerate(matched_tool_calls):
HEAD:backend/onyx/chat/llm_step.py:500:        tool_calls.append(
HEAD:backend/onyx/chat/llm_step.py:502:                tool_call_id=f"extracted_{uuid.uuid4().hex[:8]}",
HEAD:backend/onyx/chat/llm_step.py:515:        len(tool_calls),
HEAD:backend/onyx/chat/llm_step.py:518:    return tool_calls
HEAD:backend/onyx/chat/llm_step.py:521:def _extract_xml_tool_calls_from_response_text(
HEAD:backend/onyx/chat/llm_step.py:528:    <function_calls>
HEAD:backend/onyx/chat/llm_step.py:532:    </function_calls>
HEAD:backend/onyx/chat/llm_step.py:534:    matched_tool_calls: list[tuple[str, dict[str, Any]]] = []
HEAD:backend/onyx/chat/llm_step.py:556:        matched_tool_calls.append((tool_name, tool_args))
HEAD:backend/onyx/chat/llm_step.py:558:    return matched_tool_calls
HEAD:backend/onyx/chat/llm_step.py:704:    tool_calls_list: list[ToolCall] | None = None
HEAD:backend/onyx/chat/llm_step.py:705:    if msg.tool_calls:
HEAD:backend/onyx/chat/llm_step.py:706:        tool_calls_list = [
HEAD:backend/onyx/chat/llm_step.py:708:                id=tc.tool_call_id,
HEAD:backend/onyx/chat/llm_step.py:715:            for tc in msg.tool_calls
HEAD:backend/onyx/chat/llm_step.py:721:        tool_calls=tool_calls_list,
HEAD:backend/onyx/chat/llm_step.py:726:    if not msg.tool_call_id:
HEAD:backend/onyx/chat/llm_step.py:728:            f"Tool call response message encountered but tool_call_id is not available. Message: {msg}"
HEAD:backend/onyx/chat/llm_step.py:734:        tool_call_id=msg.tool_call_id,
HEAD:backend/onyx/chat/llm_step.py:758:        if not msg.tool_calls:
HEAD:backend/onyx/chat/llm_step.py:761:        tool_call_lines = [
HEAD:backend/onyx/chat/llm_step.py:763:                f"[Tool Call] name={tc.tool_name} id={tc.tool_call_id} args={json.dumps(tc.tool_arguments)}"
HEAD:backend/onyx/chat/llm_step.py:765:            for tc in msg.tool_calls
HEAD:backend/onyx/chat/llm_step.py:768:            "\n".join([msg.message, *tool_call_lines])
HEAD:backend/onyx/chat/llm_step.py:770:            else "\n".join(tool_call_lines)
HEAD:backend/onyx/chat/llm_step.py:775:            tool_calls=None,
HEAD:backend/onyx/chat/llm_step.py:779:        if not msg.tool_call_id:
HEAD:backend/onyx/chat/llm_step.py:781:                f"Tool call response message encountered but tool_call_id is not available. Message: {msg}"
HEAD:backend/onyx/chat/llm_step.py:786:            content=f"[Tool Result] id={msg.tool_call_id}\n{msg.message}",
HEAD:backend/onyx/chat/llm_step.py:917:            MessageType.TOOL_CALL_RESPONSE,
HEAD:backend/onyx/chat/llm_step.py:1013:        elif msg.message_type == MessageType.TOOL_CALL_RESPONSE:
HEAD:backend/onyx/chat/llm_step.py:1071:    return bool(delta.content or delta.reasoning_content or delta.tool_calls)
HEAD:backend/onyx/chat/llm_step.py:1077:    tool_choice: ToolChoiceOptions,
HEAD:backend/onyx/chat/llm_step.py:1106:        tool_choice: Tool choice configuration (e.g., "auto", "required", "none").
HEAD:backend/onyx/chat/llm_step.py:1125:            when tool_choice is REQUIRED.
HEAD:backend/onyx/chat/llm_step.py:1170:    id_to_tool_call_map: dict[int, dict[str, Any]] = {}
HEAD:backend/onyx/chat/llm_step.py:1182:    xml_tool_call_content_filter = _XmlToolCallContentFilter()
HEAD:backend/onyx/chat/llm_step.py:1255:            # When tool_choice is REQUIRED, content before tool calls is reasoning/thinking
HEAD:backend/onyx/chat/llm_step.py:1258:            if is_deep_research and tool_choice == ToolChoiceOptions.REQUIRED:
HEAD:backend/onyx/chat/llm_step.py:1310:            tool_choice=tool_choice,
HEAD:backend/onyx/chat/llm_step.py:1341:                and not delta.tool_calls
HEAD:backend/onyx/chat/llm_step.py:1393:                filtered_content = xml_tool_call_content_filter.process(delta.content)
HEAD:backend/onyx/chat/llm_step.py:1397:            if delta.tool_calls:
HEAD:backend/onyx/chat/llm_step.py:1400:                for tool_call_delta in delta.tool_calls:
HEAD:backend/onyx/chat/llm_step.py:1402:                    _update_tool_call_with_delta(id_to_tool_call_map, tool_call_delta)
HEAD:backend/onyx/chat/llm_step.py:1404:                        tool_calls_in_progress=id_to_tool_call_map,
HEAD:backend/onyx/chat/llm_step.py:1405:                        tool_call_delta=tool_call_delta,
HEAD:backend/onyx/chat/llm_step.py:1410:        # Flush any tail text buffered while checking for split "<function_calls" markers.
HEAD:backend/onyx/chat/llm_step.py:1411:        filtered_content_tail = xml_tool_call_content_filter.flush()
HEAD:backend/onyx/chat/llm_step.py:1427:            if flush_delta and flush_delta.tool_calls:
HEAD:backend/onyx/chat/llm_step.py:1428:                for tool_call_delta in flush_delta.tool_calls:
HEAD:backend/onyx/chat/llm_step.py:1429:                    _update_tool_call_with_delta(id_to_tool_call_map, tool_call_delta)
HEAD:backend/onyx/chat/llm_step.py:1435:        tool_calls = _extract_tool_call_kickoffs(
HEAD:backend/onyx/chat/llm_step.py:1436:            id_to_tool_call_map=id_to_tool_call_map,
HEAD:backend/onyx/chat/llm_step.py:1463:            tool_choice != ToolChoiceOptions.REQUIRED
HEAD:backend/onyx/chat/llm_step.py:1464:            and not tool_calls
HEAD:backend/onyx/chat/llm_step.py:1467:            and not _looks_like_xml_tool_call_payload(accumulated_raw_answer)
HEAD:backend/onyx/chat/llm_step.py:1501:        if tool_calls:
HEAD:backend/onyx/chat/llm_step.py:1502:            tool_calls_list: list[ToolCall] = [
HEAD:backend/onyx/chat/llm_step.py:1504:                    id=kickoff.tool_call_id,
HEAD:backend/onyx/chat/llm_step.py:1511:                for kickoff in tool_calls
HEAD:backend/onyx/chat/llm_step.py:1517:                tool_calls=tool_calls_list,
HEAD:backend/onyx/chat/llm_step.py:1524:                tool_calls=None,
HEAD:backend/onyx/chat/llm_step.py:1538:        if tool_calls:
HEAD:backend/onyx/chat/llm_step.py:1539:            tool_calls_str = "\n".join(
HEAD:backend/onyx/chat/llm_step.py:1541:                for tc in tool_calls
HEAD:backend/onyx/chat/llm_step.py:1543:            logger.debug("Tool calls:\n%s", tool_calls_str)
HEAD:backend/onyx/chat/llm_step.py:1553:            "tool_choice=%s, tools_sent=%s",
HEAD:backend/onyx/chat/llm_step.py:1559:            tool_choice,
HEAD:backend/onyx/chat/llm_step.py:1567:            tool_calls=tool_calls if tool_calls else None,
HEAD:backend/onyx/chat/llm_step.py:1579:    tool_choice: ToolChoiceOptions,
HEAD:backend/onyx/chat/llm_step.py:1604:        tool_choice=tool_choice,
HEAD:backend/onyx/chat/models.py:27:        None  # e.g., "RATE_LIMIT", "AUTH_ERROR", "TOOL_CALL_FAILED"
HEAD:backend/onyx/chat/models.py:90:    tool_calls: list[ToolCallResponse] = []
HEAD:backend/onyx/chat/models.py:153:    tool_call_id: str
HEAD:backend/onyx/chat/models.py:169:    # Only for TOOL_CALL_RESPONSE type messages
HEAD:backend/onyx/chat/models.py:170:    tool_call_id: str | None = None
HEAD:backend/onyx/chat/models.py:172:    tool_calls: list[ToolCallSimple] | None = None
HEAD:backend/onyx/chat/models.py:244:    tool_calls: list[ToolCallKickoff] | None
HEAD:backend/onyx/chat/models.py:249:    # "length", "tool_calls", "content_filter"). Lets downstream classification
HEAD:backend/onyx/chat/process_message.py:1143:        details["tool_choice"] = error.tool_choice.value
HEAD:backend/onyx/chat/process_message.py:1821:            "(provider=%s, model=%s, tool_choice=%s, finish_reason=%s)",
HEAD:backend/onyx/chat/process_message.py:1824:            e.tool_choice,
HEAD:backend/onyx/chat/process_message.py:1835:                "tool_choice": e.tool_choice.value,
HEAD:backend/onyx/chat/process_message.py:1994:    tool_calls = state_container.get_tool_calls()
HEAD:backend/onyx/chat/process_message.py:2041:            tool_calls=tool_calls,
HEAD:backend/onyx/chat/process_message.py:2250:    tool_call_responses = [
HEAD:backend/onyx/chat/process_message.py:2253:            tool_arguments=tc.tool_call_arguments,
HEAD:backend/onyx/chat/process_message.py:2254:            tool_result=tc.tool_call_response,
HEAD:backend/onyx/chat/process_message.py:2259:        for tc in state_container.get_tool_calls()
HEAD:backend/onyx/chat/process_message.py:2266:        tool_calls=tool_call_responses,
HEAD:backend/onyx/chat/save_chat.py:12:    add_search_docs_to_tool_call,
HEAD:backend/onyx/chat/save_chat.py:16:from onyx.db.tools import create_tool_call_no_commit
HEAD:backend/onyx/chat/save_chat.py:28:    tool_calls: list[ToolCallInfo],
HEAD:backend/onyx/chat/save_chat.py:33:    for tool_call_info in tool_calls:
HEAD:backend/onyx/chat/save_chat.py:34:        if not tool_call_info.generated_files:
HEAD:backend/onyx/chat/save_chat.py:36:        for gen_file in tool_call_info.generated_files:
HEAD:backend/onyx/chat/save_chat.py:52:def _create_and_link_tool_calls(
HEAD:backend/onyx/chat/save_chat.py:53:    tool_calls: list[ToolCallInfo],
HEAD:backend/onyx/chat/save_chat.py:57:    tool_call_to_search_doc_ids: dict[str, list[int]],
HEAD:backend/onyx/chat/save_chat.py:70:        tool_calls: List of tool call information to create
HEAD:backend/onyx/chat/save_chat.py:74:        tool_call_to_search_doc_ids: Mapping from tool_call_id to list of search_doc IDs
HEAD:backend/onyx/chat/save_chat.py:76:    # Create all ToolCall objects first (without parent_tool_call_id set)
HEAD:backend/onyx/chat/save_chat.py:78:    tool_call_objects: list[ToolCall] = []
HEAD:backend/onyx/chat/save_chat.py:79:    tool_call_info_map: dict[str, ToolCallInfo] = {}
HEAD:backend/onyx/chat/save_chat.py:81:    for tool_call_info in tool_calls:
HEAD:backend/onyx/chat/save_chat.py:82:        tool_call_info_map[tool_call_info.tool_call_id] = tool_call_info
HEAD:backend/onyx/chat/save_chat.py:84:        # Calculate tool_call_tokens from arguments
HEAD:backend/onyx/chat/save_chat.py:86:            arguments_json_str = json.dumps(tool_call_info.tool_call_arguments)
HEAD:backend/onyx/chat/save_chat.py:87:            tool_call_tokens = len(default_tokenizer.encode(arguments_json_str))
HEAD:backend/onyx/chat/save_chat.py:91:                tool_call_info.tool_call_id,
HEAD:backend/onyx/chat/save_chat.py:94:            arguments_json_str = json.dumps(tool_call_info.tool_call_arguments)
HEAD:backend/onyx/chat/save_chat.py:95:            tool_call_tokens = len(arguments_json_str)
HEAD:backend/onyx/chat/save_chat.py:98:            assistant_message.id if tool_call_info.parent_tool_call_id is None else None
HEAD:backend/onyx/chat/save_chat.py:101:        # Create ToolCall DB entry (parent_tool_call_id will be set after flush)
HEAD:backend/onyx/chat/save_chat.py:103:        tool_call = create_tool_call_no_commit(
HEAD:backend/onyx/chat/save_chat.py:106:            turn_number=tool_call_info.turn_index,
HEAD:backend/onyx/chat/save_chat.py:107:            tool_id=tool_call_info.tool_id,
HEAD:backend/onyx/chat/save_chat.py:108:            tool_call_id=tool_call_info.tool_call_id,
HEAD:backend/onyx/chat/save_chat.py:109:            tool_call_arguments=tool_call_info.tool_call_arguments,
HEAD:backend/onyx/chat/save_chat.py:110:            tool_call_response=tool_call_info.tool_call_response,
HEAD:backend/onyx/chat/save_chat.py:111:            tool_call_tokens=tool_call_tokens,
HEAD:backend/onyx/chat/save_chat.py:113:            parent_tool_call_id=None,  # Will be updated after flush
HEAD:backend/onyx/chat/save_chat.py:114:            reasoning_tokens=tool_call_info.reasoning_tokens,
HEAD:backend/onyx/chat/save_chat.py:116:                [img.model_dump() for img in tool_call_info.generated_images]
HEAD:backend/onyx/chat/save_chat.py:117:                if tool_call_info.generated_images
HEAD:backend/onyx/chat/save_chat.py:120:            tab_index=tool_call_info.tab_index,
HEAD:backend/onyx/chat/save_chat.py:127:        tool_call_objects.append(tool_call)
HEAD:backend/onyx/chat/save_chat.py:129:    # Build mapping of tool calls (tool_call_id string -> DB id int)
HEAD:backend/onyx/chat/save_chat.py:130:    tool_call_map: dict[str, int] = {}
HEAD:backend/onyx/chat/save_chat.py:131:    for tool_call_obj in tool_call_objects:
HEAD:backend/onyx/chat/save_chat.py:132:        tool_call_map[tool_call_obj.tool_call_id] = tool_call_obj.id
HEAD:backend/onyx/chat/save_chat.py:134:    # Update parent_tool_call_id for all tool calls
HEAD:backend/onyx/chat/save_chat.py:137:    valid_tool_calls: list[ToolCall] = []
HEAD:backend/onyx/chat/save_chat.py:138:    for tool_call_obj in tool_call_objects:
HEAD:backend/onyx/chat/save_chat.py:139:        tool_call_info = tool_call_info_map[tool_call_obj.tool_call_id]
HEAD:backend/onyx/chat/save_chat.py:140:        if tool_call_info.parent_tool_call_id is not None:
HEAD:backend/onyx/chat/save_chat.py:141:            parent_id = tool_call_map.get(tool_call_info.parent_tool_call_id)
HEAD:backend/onyx/chat/save_chat.py:143:                tool_call_obj.parent_tool_call_id = parent_id
HEAD:backend/onyx/chat/save_chat.py:144:                valid_tool_calls.append(tool_call_obj)
HEAD:backend/onyx/chat/save_chat.py:149:                    tool_call_obj.tool_call_id,
HEAD:backend/onyx/chat/save_chat.py:150:                    tool_call_info.parent_tool_call_id,
HEAD:backend/onyx/chat/save_chat.py:153:                db_session.delete(tool_call_obj)
HEAD:backend/onyx/chat/save_chat.py:156:            valid_tool_calls.append(tool_call_obj)
HEAD:backend/onyx/chat/save_chat.py:159:    for tool_call_obj in valid_tool_calls:
HEAD:backend/onyx/chat/save_chat.py:160:        search_doc_ids = tool_call_to_search_doc_ids.get(tool_call_obj.tool_call_id, [])
HEAD:backend/onyx/chat/save_chat.py:162:            add_search_docs_to_tool_call(
HEAD:backend/onyx/chat/save_chat.py:163:                tool_call_id=tool_call_obj.id,
HEAD:backend/onyx/chat/save_chat.py:172:    tool_calls: list[ToolCallInfo],
HEAD:backend/onyx/chat/save_chat.py:189:    3. Builds tool_call -> search_doc mapping for displayed docs
HEAD:backend/onyx/chat/save_chat.py:198:        tool_calls: List of tool call information to create ToolCall entries (may include search_docs)
HEAD:backend/onyx/chat/save_chat.py:222:        tool_calls = []
HEAD:backend/onyx/chat/save_chat.py:254:    # 3. Build tool_call -> search_doc mapping (for displayed docs in each tool call)
HEAD:backend/onyx/chat/save_chat.py:255:    tool_call_to_search_doc_ids: dict[str, list[int]] = {}
HEAD:backend/onyx/chat/save_chat.py:256:    for tool_call_info in tool_calls:
HEAD:backend/onyx/chat/save_chat.py:257:        if tool_call_info.search_docs:
HEAD:backend/onyx/chat/save_chat.py:259:            for search_doc_py in tool_call_info.search_docs:
HEAD:backend/onyx/chat/save_chat.py:273:            tool_call_to_search_doc_ids[tool_call_info.tool_call_id] = list(
HEAD:backend/onyx/chat/save_chat.py:292:        # Get the search doc ID (should already exist from processing tool_calls)
HEAD:backend/onyx/chat/save_chat.py:341:    _create_and_link_tool_calls(
HEAD:backend/onyx/chat/save_chat.py:342:        tool_calls=tool_calls,
HEAD:backend/onyx/chat/save_chat.py:346:        tool_call_to_search_doc_ids=tool_call_to_search_doc_ids,
HEAD:backend/onyx/chat/save_chat.py:359:            tool_calls, sanitized_message_text
HEAD:backend/onyx/chat/tool_call_args_streaming.py:4:from onyx.llm.model_response import ChatCompletionDeltaToolCall
HEAD:backend/onyx/chat/tool_call_args_streaming.py:13:    tool_calls_in_progress: Mapping[int, Mapping[str, Any]],
HEAD:backend/onyx/chat/tool_call_args_streaming.py:14:    tool_call_delta: ChatCompletionDeltaToolCall,
HEAD:backend/onyx/chat/tool_call_args_streaming.py:17:    tool_name = tool_calls_in_progress.get(tool_call_delta.index, {}).get("name")
HEAD:backend/onyx/chat/tool_call_args_streaming.py:24:    tool_calls_in_progress: Mapping[int, Mapping[str, Any]],
HEAD:backend/onyx/chat/tool_call_args_streaming.py:25:    tool_call_delta: ChatCompletionDeltaToolCall,
HEAD:backend/onyx/chat/tool_call_args_streaming.py:41:    tool_cls = _get_tool_class(tool_calls_in_progress, tool_call_delta)
HEAD:backend/onyx/chat/tool_call_args_streaming.py:45:    fn = tool_call_delta.function
HEAD:backend/onyx/chat/tool_call_args_streaming.py:50:    idx = tool_call_delta.index
HEAD:backend/onyx/chat/tool_call_args_streaming.py:67:    tc_data = tool_calls_in_progress[tool_call_delta.index]
HEAD:backend/onyx/llm/interfaces.py:11:    ToolChoice,
HEAD:backend/onyx/llm/interfaces.py:12:    ToolChoiceOptions,  # noqa: F401  # re-exported: onyx.chat imports it from here
HEAD:backend/onyx/llm/interfaces.py:94:        tool_choice: ToolChoice | None = None,
HEAD:backend/onyx/llm/interfaces.py:108:        tool_choice: ToolChoice | None = None,
HEAD:backend/onyx/llm/litellm_singleton/config.py:29:            "ollama_chat/gpt-oss:120b-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:30:            "ollama_chat/gpt-oss:120b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:31:            "ollama_chat/gpt-oss:20b-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:32:            "ollama_chat/gpt-oss:20b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:33:            "ollama/gpt-oss:120b-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:34:            "ollama/gpt-oss:120b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:35:            "ollama/gpt-oss:20b-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:36:            "ollama/gpt-oss:20b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:38:            "ollama_chat/deepseek-r1:latest": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:39:            "ollama_chat/deepseek-r1:1.5b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:40:            "ollama_chat/deepseek-r1:7b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:41:            "ollama_chat/deepseek-r1:8b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:42:            "ollama_chat/deepseek-r1:14b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:43:            "ollama_chat/deepseek-r1:32b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:44:            "ollama_chat/deepseek-r1:70b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:45:            "ollama_chat/deepseek-r1:671b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:46:            "ollama_chat/deepseek-v3.1:latest": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:47:            "ollama_chat/deepseek-v3.1:671b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:48:            "ollama_chat/deepseek-v3.1:671b-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:49:            "ollama/deepseek-r1:latest": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:50:            "ollama/deepseek-r1:1.5b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:51:            "ollama/deepseek-r1:7b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:52:            "ollama/deepseek-r1:8b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:53:            "ollama/deepseek-r1:14b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:54:            "ollama/deepseek-r1:32b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:55:            "ollama/deepseek-r1:70b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:56:            "ollama/deepseek-r1:671b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:57:            "ollama/deepseek-v3.1:latest": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:58:            "ollama/deepseek-v3.1:671b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:59:            "ollama/deepseek-v3.1:671b-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:61:            "ollama_chat/gemma3:latest": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:62:            "ollama_chat/gemma3:270m": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:63:            "ollama_chat/gemma3:1b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:64:            "ollama_chat/gemma3:4b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:65:            "ollama_chat/gemma3:12b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:66:            "ollama_chat/gemma3:27b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:67:            "ollama/gemma3:latest": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:68:            "ollama/gemma3:270m": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:69:            "ollama/gemma3:1b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:70:            "ollama/gemma3:4b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:71:            "ollama/gemma3:12b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:72:            "ollama/gemma3:27b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:74:            "ollama_chat/qwen3-coder:latest": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:75:            "ollama_chat/qwen3-coder:30b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:76:            "ollama_chat/qwen3-coder:480b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:77:            "ollama_chat/qwen3-coder:480b-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:78:            "ollama_chat/qwen3-vl:latest": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:79:            "ollama_chat/qwen3-vl:2b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:80:            "ollama_chat/qwen3-vl:4b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:81:            "ollama_chat/qwen3-vl:8b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:82:            "ollama_chat/qwen3-vl:30b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:83:            "ollama_chat/qwen3-vl:32b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:84:            "ollama_chat/qwen3-vl:235b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:85:            "ollama_chat/qwen3-vl:235b-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:87:                "supports_function_calling": True
HEAD:backend/onyx/llm/litellm_singleton/config.py:89:            "ollama/qwen3-coder:latest": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:90:            "ollama/qwen3-coder:30b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:91:            "ollama/qwen3-coder:480b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:92:            "ollama/qwen3-coder:480b-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:93:            "ollama/qwen3-vl:latest": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:94:            "ollama/qwen3-vl:2b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:95:            "ollama/qwen3-vl:4b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:96:            "ollama/qwen3-vl:8b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:97:            "ollama/qwen3-vl:30b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:98:            "ollama/qwen3-vl:32b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:99:            "ollama/qwen3-vl:235b": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:100:            "ollama/qwen3-vl:235b-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:101:            "ollama/qwen3-vl:235b-instruct-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:103:            "ollama_chat/kimi-k2:1t": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:104:            "ollama_chat/kimi-k2:1t-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:105:            "ollama/kimi-k2:1t": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:106:            "ollama/kimi-k2:1t-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:108:            "ollama_chat/glm-4.6:cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:109:            "ollama_chat/glm-4.6": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:110:            "ollama/glm-4.6": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/config.py:111:            "ollama/glm-4.6-cloud": {"supports_function_calling": True},
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:26:   - Also turns empty function_call_arguments.delta events into no-op chunks;
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:127:                    "tool_calls": [{
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:148:            tool_calls = chunk["message"].get("tool_calls")
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:149:            if tool_calls is not None:
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:150:                for tool_call in tool_calls:
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:151:                    function_args = tool_call.get("function").get("arguments")
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:153:                        is_function_call_complete = self._is_function_call_complete(
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:156:                        if is_function_call_complete:
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:157:                            tool_call["id"] = str(uuid.uuid4())
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:210:                tool_calls=tool_calls,
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:215:                # calls are present, override done_reason to "tool_calls" so
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:217:                if tool_calls:
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:218:                    finish_reason = "tool_calls"
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:323:        if event_type == "response.function_call_arguments.delta" and not (
HEAD:backend/onyx/llm/model_response.py:18:class ChatCompletionMessageToolCall(BaseModel):
HEAD:backend/onyx/llm/model_response.py:24:class ChatCompletionDeltaToolCall(BaseModel):
HEAD:backend/onyx/llm/model_response.py:35:    tool_calls: List[ChatCompletionDeltaToolCall] = Field(default_factory=list)
HEAD:backend/onyx/llm/model_response.py:66:    tool_calls: List[ChatCompletionMessageToolCall] | None = None
HEAD:backend/onyx/llm/model_response.py:89:def _parse_function_call(
HEAD:backend/onyx/llm/model_response.py:101:def _parse_delta_tool_calls(
HEAD:backend/onyx/llm/model_response.py:102:    tool_calls: list[dict[str, Any]] | None,
HEAD:backend/onyx/llm/model_response.py:103:) -> list[ChatCompletionDeltaToolCall]:
HEAD:backend/onyx/llm/model_response.py:105:    if not tool_calls:
HEAD:backend/onyx/llm/model_response.py:108:    parsed_tool_calls: list[ChatCompletionDeltaToolCall] = [
HEAD:backend/onyx/llm/model_response.py:109:        ChatCompletionDeltaToolCall(
HEAD:backend/onyx/llm/model_response.py:110:            id=tool_call.get("id"),
HEAD:backend/onyx/llm/model_response.py:111:            index=tool_call.get("index", 0),
HEAD:backend/onyx/llm/model_response.py:112:            type=tool_call.get("type", "function"),
HEAD:backend/onyx/llm/model_response.py:113:            function=_parse_function_call(tool_call.get("function")),
HEAD:backend/onyx/llm/model_response.py:115:        for tool_call in tool_calls
HEAD:backend/onyx/llm/model_response.py:117:    return parsed_tool_calls
HEAD:backend/onyx/llm/model_response.py:145:def _parse_message_tool_calls(
HEAD:backend/onyx/llm/model_response.py:146:    tool_calls: list[dict[str, Any]] | None,
HEAD:backend/onyx/llm/model_response.py:147:) -> list[ChatCompletionMessageToolCall]:
HEAD:backend/onyx/llm/model_response.py:149:    if not tool_calls:
HEAD:backend/onyx/llm/model_response.py:152:    parsed_tool_calls: list[ChatCompletionMessageToolCall] = []
HEAD:backend/onyx/llm/model_response.py:153:    for tool_call in tool_calls:
HEAD:backend/onyx/llm/model_response.py:154:        function_call = _parse_function_call(tool_call.get("function"))
HEAD:backend/onyx/llm/model_response.py:155:        if not function_call:
HEAD:backend/onyx/llm/model_response.py:158:        parsed_tool_calls.append(
HEAD:backend/onyx/llm/model_response.py:159:            ChatCompletionMessageToolCall(
HEAD:backend/onyx/llm/model_response.py:160:                id=tool_call.get("id", ""),
HEAD:backend/onyx/llm/model_response.py:161:                type=tool_call.get("type", "function"),
HEAD:backend/onyx/llm/model_response.py:162:                function=function_call,
HEAD:backend/onyx/llm/model_response.py:165:    return parsed_tool_calls
HEAD:backend/onyx/llm/model_response.py:225:        tool_calls=_parse_delta_tool_calls(delta_data.get("tool_calls")),
HEAD:backend/onyx/llm/model_response.py:254:    parsed_tool_calls = _parse_message_tool_calls(message_data.get("tool_calls"))
HEAD:backend/onyx/llm/model_response.py:259:        tool_calls=parsed_tool_calls if parsed_tool_calls else None,
HEAD:backend/onyx/llm/models.py:13:class ToolChoiceOptions(str, Enum):
HEAD:backend/onyx/llm/models.py:19:class NamedToolChoice(BaseModel):
HEAD:backend/onyx/llm/models.py:25:ToolChoice = ToolChoiceOptions | NamedToolChoice
HEAD:backend/onyx/llm/models.py:229:    tool_calls: list[ToolCall] | None = None
HEAD:backend/onyx/llm/models.py:236:    tool_call_id: str
HEAD:backend/onyx/llm/multi_llm.py:42:    ToolChoice,
```
This establishes a source-level boundary where model-controlled output can
be interpreted as a request for an application capability.
## Tool Argument Parsing and Validation
Evidence lines: 596
```text
HEAD:backend/ee/onyx/configs/app_configs.py:144:SUPER_USERS = json.loads(os.environ.get("SUPER_USERS", "[]"))
HEAD:backend/ee/onyx/db/license.py:252:        return LicenseMetadata.model_validate_json(cached_str)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:79:            doc_metadata = DocMetadata.model_validate_json(json.dumps(doc.doc_metadata))
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:34:        payload = json.loads(raw_text)
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:184:        user_model = User.model_validate(raw_user_dict)
HEAD:backend/ee/onyx/server/billing/api.py:320:                return BillingInformationResponse.model_validate_json(cached)
HEAD:backend/ee/onyx/server/billing/api.py:325:                    return SubscriptionStatusResponse.model_validate_json(cached)
HEAD:backend/ee/onyx/server/billing/billing_cache.py:59:    envelope = json.loads(raw)
HEAD:backend/ee/onyx/server/enterprise_settings/models.py:19:    def model_validate(cls, *args: Any, **kwargs: Any) -> "NavigationItem":
HEAD:backend/ee/onyx/server/enterprise_settings/models.py:20:        instance = super().model_validate(*args, **kwargs)
HEAD:backend/ee/onyx/server/features/hooks/api.py:209:            input_schema=spec.input_schema,
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:198:        parsed = json.loads(body)
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:443:                    event = json.loads(raw_data)
HEAD:backend/ee/onyx/server/gateway/api.py:515:        arguments=tool_call.function.arguments or "",
HEAD:backend/ee/onyx/server/gateway/api.py:928:        input_schema = tool.get("input_schema")
HEAD:backend/ee/onyx/server/gateway/api.py:929:        if not name or input_schema is None:
HEAD:backend/ee/onyx/server/gateway/api.py:934:                "only client tools with an input_schema are accepted.",
HEAD:backend/ee/onyx/server/gateway/api.py:936:        function: dict[str, Any] = {"name": name, "parameters": input_schema}
HEAD:backend/ee/onyx/server/gateway/api.py:1063:        arguments = tool_call.function.arguments
HEAD:backend/ee/onyx/server/gateway/api.py:1065:            parsed_input = json.loads(arguments) if arguments else {}
HEAD:backend/ee/onyx/server/gateway/api.py:1067:            raise ValueError("Upstream tool arguments are not valid JSON") from e
HEAD:backend/ee/onyx/server/gateway/api.py:1069:            raise ValueError("Upstream tool arguments must be a JSON object")
HEAD:backend/ee/onyx/server/gateway/api.py:1263:                                partial_json=tool_call.function.arguments or "{}"
HEAD:backend/ee/onyx/server/gateway/api.py:1374:            "The upstream LLM returned invalid tool arguments.",
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:239:        parsed = json.loads(body)
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:509:                    event = json.loads(raw_data)
HEAD:backend/ee/onyx/server/log_export/storage.py:100:    manifest = LogExportManifest.model_validate_json(
HEAD:backend/ee/onyx/server/log_export/storage.py:104:        LogExportReceipt.model_validate_json(file_store.read_file(file_id).read())
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:137:        session = ConfluenceCloudOAuth.OAuthSession.model_validate_json(session_json)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:210:            token_response = ConfluenceCloudOAuth.TokenResponse.model_validate_json(
HEAD:backend/ee/onyx/server/oauth/google_drive.py:106:        session = GoogleDriveOAuth.OAuthSession.model_validate_json(session_json)
HEAD:backend/ee/onyx/server/oauth/slack.py:95:        session = SlackOAuth.OAuthSession.model_validate_json(session_json)
HEAD:backend/ee/onyx/server/query_history/models.py:258:        metadata = QueryHistoryFileMetadata.model_validate(dict(file.file_metadata))
HEAD:backend/ee/onyx/server/scim/patch.py:102:        return model.model_validate(data)
HEAD:backend/ee/onyx/server/scim/providers/base.py:193:            entries = json.loads(stored_json)
HEAD:backend/ee/onyx/server/scim/schema_definitions.py:19:USER_RESOURCE_TYPE = ScimResourceType.model_validate(
HEAD:backend/ee/onyx/server/scim/schema_definitions.py:32:GROUP_RESOURCE_TYPE = ScimResourceType.model_validate(
HEAD:backend/ee/onyx/server/seeding.py:74:    seed_config = SeedConfiguration.model_validate_json(seed_config_str)
HEAD:backend/ee/onyx/server/seeding.py:89:                    openapi_schema = json.loads(file_content)
HEAD:backend/ee/onyx/server/tenants/proxy.py:408:            return BillingInformationResponse.model_validate_json(cached)
HEAD:backend/ee/onyx/server/tenants/tier_management.py:73:        parsed = json.loads(value)
HEAD:backend/ee/onyx/utils/license.py:203:        decoded = json.loads(base64.b64decode(license_data))
HEAD:backend/ee/onyx/utils/posthog_client.py:134:        cookie_data = json.loads(decoded_cookie)
HEAD:backend/onyx/auth/login_claims_capture.py:211:            parsed = json.loads(raw)
HEAD:backend/onyx/auth/mobile_sso/code_store.py:66:        record = json.loads(raw)
HEAD:backend/onyx/auth/session_tokens.py:109:            previous = SessionTokenValue.model_validate_json(previous_raw_value)
HEAD:backend/onyx/auth/session_tokens.py:153:        value = SessionTokenValue.model_validate_json(raw_value)
HEAD:backend/onyx/background/celery/celery_k8s_probe.py:46:    args = parser.parse_args()
HEAD:backend/onyx/background/celery/celery_redis.py:86:    Uses a bytes-substring pre-filter to skip the json.loads call for entries
HEAD:backend/onyx/background/celery/celery_redis.py:99:        task = json.loads(v_bytes)
HEAD:backend/onyx/background/celery/celery_redis.py:148:            task_dict: dict[str, Any] = json.loads(task.decode("utf-8"))
HEAD:backend/onyx/background/celery/celery_redis.py:170:            task_dict: dict[str, Any] = json.loads(task.decode("utf-8"))
HEAD:backend/onyx/background/celery/tasks/evals/tasks.py:38:        configuration = EvalConfigurationOptions.model_validate(configuration_dict)
HEAD:backend/onyx/background/indexing/checkpointing_utils.py:65:    return ConnectorCheckpoint.model_validate_json(checkpoint_data)
HEAD:backend/onyx/chat/README.md:81:string saying it is no longer available. Tool Call details like the search query and other arguments are kept in the history as this is information
HEAD:backend/onyx/chat/README.md:84:> Note: in the Internal Search flow with query expansion, the Tool Call which was actually run differs from what the LLM provided as arguments.
HEAD:backend/onyx/chat/chat_utils.py:856:                                tool_arguments=tool_call.tool_call_arguments or {},
HEAD:backend/onyx/chat/chat_utils.py:994:                tool_arguments=tool_call.tool_args,
HEAD:backend/onyx/chat/llm_loop.py:1106:                                tool_args=tool_call.tool_args,
HEAD:backend/onyx/chat/llm_loop.py:1171:                        parsed = json.loads(tool_response.llm_facing_response)
HEAD:backend/onyx/chat/llm_loop.py:1310:                    tool_call_arguments=tool_call.tool_args,
HEAD:backend/onyx/chat/llm_loop.py:1350:                            tool_arguments=tc.tool_args,
HEAD:backend/onyx/chat/llm_step.py:14:from onyx.chat.tool_call_args_streaming import maybe_emit_argument_delta
HEAD:backend/onyx/chat/llm_step.py:72:from onyx.utils.postgres_sanitization import sanitize_string
HEAD:backend/onyx/chat/llm_step.py:220:        return json.loads(stripped)
HEAD:backend/onyx/chat/llm_step.py:225:def _parse_tool_args_to_dict(raw_args: Any) -> dict[str, Any]:
HEAD:backend/onyx/chat/llm_step.py:226:    """Parse tool arguments into a dict.
HEAD:backend/onyx/chat/llm_step.py:229:    - raw_args == '{"queries":[...]}' -> dict via json.loads
HEAD:backend/onyx/chat/llm_step.py:232:    - raw_args == '"{\\"queries\\":[...]}"' -> json.loads -> str -> json.loads -> dict
HEAD:backend/onyx/chat/llm_step.py:246:            k: _try_parse_json_string(sanitize_string(v) if isinstance(v, str) else v)
HEAD:backend/onyx/chat/llm_step.py:254:    raw_args = sanitize_string(raw_args)
HEAD:backend/onyx/chat/llm_step.py:257:        parsed1: Any = json.loads(raw_args)
HEAD:backend/onyx/chat/llm_step.py:267:            parsed2: Any = json.loads(parsed1)
HEAD:backend/onyx/chat/llm_step.py:330:                            "arguments": tool_call.function.arguments,
HEAD:backend/onyx/chat/llm_step.py:376:        if tool_call_delta.function.arguments:
HEAD:backend/onyx/chat/llm_step.py:377:            tool_calls_in_progress[index]["arguments"] += (
HEAD:backend/onyx/chat/llm_step.py:378:                tool_call_delta.function.arguments
HEAD:backend/onyx/chat/llm_step.py:405:            tool_args = _parse_tool_args_to_dict(tool_call_data.get("arguments"))
HEAD:backend/onyx/chat/llm_step.py:411:                    tool_args=tool_args,
HEAD:backend/onyx/chat/llm_step.py:472:        # its nested arguments object. If both resolve to the same tool call,
HEAD:backend/onyx/chat/llm_step.py:499:    for tab_index, (tool_name, tool_args) in enumerate(matched_tool_calls):
HEAD:backend/onyx/chat/llm_step.py:504:                tool_args=tool_args,
HEAD:backend/onyx/chat/llm_step.py:542:        tool_args: dict[str, Any] = {}
HEAD:backend/onyx/chat/llm_step.py:551:            tool_args[parameter_name] = _parse_xml_parameter_value(
HEAD:backend/onyx/chat/llm_step.py:556:        matched_tool_calls.append((tool_name, tool_args))
HEAD:backend/onyx/chat/llm_step.py:570:    return sanitize_string(unescape(attr_match.group(2).strip()))
HEAD:backend/onyx/chat/llm_step.py:575:    value = sanitize_string(unescape(raw_value).strip())
HEAD:backend/onyx/chat/llm_step.py:581:        return json.loads(value)
HEAD:backend/onyx/chat/llm_step.py:586:def _resolve_tool_arguments(obj: dict[str, Any]) -> dict[str, Any] | None:
HEAD:backend/onyx/chat/llm_step.py:587:    """Extract and parse an arguments/parameters value from a tool-call-like object.
HEAD:backend/onyx/chat/llm_step.py:594:        arguments = sanitize_string(arguments)
HEAD:backend/onyx/chat/llm_step.py:596:            arguments = json.loads(arguments)
HEAD:backend/onyx/chat/llm_step.py:611:    1. Direct tool call format: {"name": "tool_name", "arguments": {...}}
HEAD:backend/onyx/chat/llm_step.py:612:    2. Function call format: {"function": {"name": "tool_name", "arguments": {...}}}
HEAD:backend/onyx/chat/llm_step.py:613:    3. Tool name as key: {"tool_name": {...arguments...}}
HEAD:backend/onyx/chat/llm_step.py:614:    4. Arguments matching a tool's parameter schema
HEAD:backend/onyx/chat/llm_step.py:621:        Tuple of (tool_name, tool_args) if matched, None otherwise
HEAD:backend/onyx/chat/llm_step.py:623:    # Format 1: Direct tool call format {"name": "...", "arguments": {...}}
HEAD:backend/onyx/chat/llm_step.py:626:        arguments = _resolve_tool_arguments(json_obj)
HEAD:backend/onyx/chat/llm_step.py:628:            return (tool_name, arguments)
HEAD:backend/onyx/chat/llm_step.py:635:            arguments = _resolve_tool_arguments(func_obj)
HEAD:backend/onyx/chat/llm_step.py:637:                return (tool_name, arguments)
HEAD:backend/onyx/chat/llm_step.py:639:    # Format 3: Tool name as key {"tool_name": {...arguments...}}
HEAD:backend/onyx/chat/llm_step.py:642:            arguments = json_obj[tool_name]
HEAD:backend/onyx/chat/llm_step.py:644:                return (tool_name, arguments)
HEAD:backend/onyx/chat/llm_step.py:662:                return (tool_name, filtered_args)
HEAD:backend/onyx/chat/llm_step.py:673:    extracted_args = _extract_nested_arguments_obj(previous_json_obj, tool_name_to_def)
HEAD:backend/onyx/chat/llm_step.py:695:    # Format 3: {"tool_name": {...arguments...}}
HEAD:backend/onyx/chat/llm_step.py:712:                    arguments=json.dumps(tc.tool_arguments),
HEAD:backend/onyx/chat/llm_step.py:763:                f"[Tool Call] name={tc.tool_name} id={tc.tool_call_id} args={json.dumps(tc.tool_arguments)}"
HEAD:backend/onyx/chat/llm_step.py:1508:                        arguments=json.dumps(kickoff.tool_args),
HEAD:backend/onyx/chat/llm_step.py:1540:                f"  - {tc.tool_name}: {json.dumps(tc.tool_args, indent=4)}"
HEAD:backend/onyx/chat/models.py:60:    tool_arguments: dict[str, Any]
HEAD:backend/onyx/chat/models.py:150:    Each tool call has an ID, name, arguments, and token count for tracking.
HEAD:backend/onyx/chat/models.py:155:    tool_arguments: dict[str, Any]
HEAD:backend/onyx/chat/process_message.py:2253:            tool_arguments=tc.tool_call_arguments,
HEAD:backend/onyx/chat/save_chat.py:22:from onyx.utils.postgres_sanitization import sanitize_string
HEAD:backend/onyx/chat/save_chat.py:84:        # Calculate tool_call_tokens from arguments
HEAD:backend/onyx/chat/save_chat.py:86:            arguments_json_str = json.dumps(tool_call_info.tool_call_arguments)
HEAD:backend/onyx/chat/save_chat.py:87:            tool_call_tokens = len(default_tokenizer.encode(arguments_json_str))
HEAD:backend/onyx/chat/save_chat.py:90:                "Failed to tokenize tool call arguments for %s: %s. Using length as (over) estimate.",
HEAD:backend/onyx/chat/save_chat.py:94:            arguments_json_str = json.dumps(tool_call_info.tool_call_arguments)
HEAD:backend/onyx/chat/save_chat.py:95:            tool_call_tokens = len(arguments_json_str)
HEAD:backend/onyx/chat/save_chat.py:109:            tool_call_arguments=tool_call_info.tool_call_arguments,
HEAD:backend/onyx/chat/save_chat.py:210:        sanitize_string(message_text) if message_text else message_text
HEAD:backend/onyx/chat/save_chat.py:217:            sanitize_string(reasoning_tokens) if reasoning_tokens else reasoning_tokens
HEAD:backend/onyx/chat/stream_buffer.py:216:        meta = StreamBufferMeta.model_validate_json(
HEAD:backend/onyx/configs/app_configs.py:292:        parsed = json.loads(raw)
HEAD:backend/onyx/configs/app_configs.py:1296:        json.loads(_RAW_CONFLUENCE_CONNECTOR_USER_PROFILES_OVERRIDE)
HEAD:backend/onyx/configs/app_configs.py:1785:CUSTOM_ANSWER_VALIDITY_CONDITIONS = json.loads(
HEAD:backend/onyx/configs/app_configs.py:1824:        dict[str, str], json.loads(_LITELLM_CUSTOM_ERROR_MESSAGE_MAPPINGS)
HEAD:backend/onyx/configs/model_configs.py:97:        LITELLM_EXTRA_HEADERS = json.loads(_LITELLM_EXTRA_HEADERS_RAW)
HEAD:backend/onyx/configs/model_configs.py:112:        LITELLM_PASS_THROUGH_HEADERS = json.loads(_LITELLM_PASS_THROUGH_HEADERS_RAW)
HEAD:backend/onyx/configs/model_configs.py:129:        LITELLM_EXTRA_BODY = json.loads(_LITELLM_EXTRA_BODY_RAW)
HEAD:backend/onyx/configs/tool_configs.py:15:        CUSTOM_TOOL_PASS_THROUGH_HEADERS = json.loads(
HEAD:backend/onyx/connectors/bitbucket/connector.py:273:        return BitbucketConnectorCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/box/connector.py:826:        return BoxConnectorCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/braintrust/connector.py:604:        return BraintrustCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/canvas/connector.py:921:        return CanvasConnectorCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/confluence/connector.py:963:        return ConfluenceCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:247:            credential_json: dict[str, Any] = json.loads(credential_str)
HEAD:backend/onyx/connectors/confluence/utils.py:322:        token_response = TokenResponse.model_validate_json(response.text)
HEAD:backend/onyx/connectors/drupal_wiki/connector.py:436:            space_response = DrupalWikiSpaceResponse.model_validate(resp_json)
HEAD:backend/onyx/connectors/drupal_wiki/connector.py:496:                page_response = DrupalWikiPageResponse.model_validate(resp_json)
HEAD:backend/onyx/connectors/drupal_wiki/connector.py:534:        return DrupalWikiPage.model_validate(response.json())
HEAD:backend/onyx/connectors/drupal_wiki/connector.py:784:        return DrupalWikiCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/file/connector.py:327:                loaded_metadata = json.loads(metadata_bytes)
HEAD:backend/onyx/connectors/freshdesk/connector.py:267:            tickets = json.loads(response.content)
HEAD:backend/onyx/connectors/github/connector.py:1469:        return GithubConnectorCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/gmail/connector.py:670:        return GmailCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/gong/connector.py:461:        return GongConnectorCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/google_drive/connector.py:2300:        return GoogleDriveCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/google_drive/connector.py:2309:    refried_credential_string = json.dumps(json.loads(raw_credential_string))
HEAD:backend/onyx/connectors/google_drive/models.py:196:            {k: StageCompletion.model_validate(val) for k, val in v.items()}
HEAD:backend/onyx/connectors/google_drive/section_extraction.py:112:    doc = json.loads(buffer)
HEAD:backend/onyx/connectors/google_utils/google_auth.py:35:    oauth_creds_sanitized_json: dict[str, Any] = json.loads(oauth_creds_json_str)
HEAD:backend/onyx/connectors/google_utils/google_auth.py:52:    creds_json = json.loads(token_json_str)
HEAD:backend/onyx/connectors/google_utils/google_auth.py:99:        credentials_dict = json.loads(credentials_dict_str)
HEAD:backend/onyx/connectors/google_utils/google_auth.py:149:        service_account_key = json.loads(service_account_key_json_str)
HEAD:backend/onyx/connectors/google_utils/google_kv.py:51:        return json.loads(raw)
HEAD:backend/onyx/connectors/guru/connector.py:82:            cards = json.loads(response.text)
HEAD:backend/onyx/connectors/imap/connector.py:246:        return ImapCheckpoint.model_validate_json(json_data=checkpoint_json)
HEAD:backend/onyx/connectors/imap/models.py:68:        return cls.model_validate(
HEAD:backend/onyx/connectors/jira/connector.py:186:                error_text = _format_error_text(json.loads(raw_text))
HEAD:backend/onyx/connectors/jira/connector.py:1094:        return JiraConnectorCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/loopio/connector.py:79:            response_data = json.loads(response.text)
HEAD:backend/onyx/connectors/lumapps/connector.py:187:        return LumAppsCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/mock_connector/connector.py:138:        return MockConnectorCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/salesforce/auth.py:109:    return SalesforceTokenResponse.model_validate(response.json())
HEAD:backend/onyx/connectors/salesforce/connector.py:336:            config_json = json.loads(custom_query_config)
HEAD:backend/onyx/connectors/salesforce/connector.py:938:                # json.loads(parent_object.data)
HEAD:backend/onyx/connectors/salesforce/connector.py:1364:    #     return SalesforceCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/salesforce/models.py:152:        return SalesforceLegacyCredentials.model_validate(credentials)
HEAD:backend/onyx/connectors/salesforce/models.py:154:        return SalesforceOAuthCredentials.model_validate(credentials)
HEAD:backend/onyx/connectors/salesforce/sqlite_functions.py:691:            data = json.loads(result[0][0])
HEAD:backend/onyx/connectors/salesforce/sqlite_functions.py:706:                        account_data = json.loads(cursor.fetchone()[0])
HEAD:backend/onyx/connectors/sharepoint/connector.py:2685:        return SharepointConnectorCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/slab/connector.py:97:    results = json.loads(run_graphql_request(graphql_query, bot_token))
HEAD:backend/onyx/connectors/slab/connector.py:119:    results = json.loads(run_graphql_request(graphql_query, bot_token))
HEAD:backend/onyx/connectors/slab/connector.py:136:    results = json.loads(run_graphql_request(graphql_query, bot_token))
HEAD:backend/onyx/connectors/slab/connector.py:178:        results = json.loads(run_graphql_request(graphql_query, bot_token))
HEAD:backend/onyx/connectors/slab/connector.py:242:            contents = json.loads(post["content"])
HEAD:backend/onyx/connectors/slack/connector.py:1554:        return SlackCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/slack/source_operations.py:489:        page = page_model.model_validate(response.data)
HEAD:backend/onyx/connectors/slack/source_operations.py:497:    return model.model_validate(response.data)
HEAD:backend/onyx/connectors/slack/source_operations.py:577:        return SlackSourceOperationsConfig.model_validate(
HEAD:backend/onyx/connectors/teams/connector.py:206:        return TeamsCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/zendesk/connector.py:659:        return ZendeskConnectorCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/zoom/client.py:168:        token = ZoomAccessToken.model_validate(response.json())
HEAD:backend/onyx/connectors/zoom/client.py:252:        return ZoomTranscript.model_validate(response.json())
HEAD:backend/onyx/connectors/zoom/client.py:261:        return ZoomPastMeetingDetails.model_validate(response.json())
HEAD:backend/onyx/connectors/zoom/client.py:293:        return [ZoomSessionOccurrence.model_validate(o) for o in occurrences]
HEAD:backend/onyx/connectors/zoom/client.py:304:        return ZoomWebinarDetails.model_validate(response.json())
HEAD:backend/onyx/connectors/zoom/client.py:320:        return [ZoomSessionOccurrence.model_validate(o) for o in occurrences]
HEAD:backend/onyx/connectors/zoom/client.py:337:            users=[ZoomUser.model_validate(m) for m in body.get("members", [])],
HEAD:backend/onyx/connectors/zoom/client.py:352:            users=[ZoomUser.model_validate(u) for u in body.get("users", [])],
HEAD:backend/onyx/connectors/zoom/connector.py:74:        return ZoomConnectorCheckpoint.model_validate_json(checkpoint_json)
HEAD:backend/onyx/connectors/zoom/recordings/discovery.py:160:            _AllowlistCursor.model_validate(cursor) if cursor else _AllowlistCursor()
HEAD:backend/onyx/connectors/zoom/recordings/discovery.py:419:            _UserRecordingsCursor.model_validate(cursor)
HEAD:backend/onyx/context/search/federated/slack_search.py:86:            cached_data = cast(dict[str, ChannelMetadata], json.loads(cached_str))
HEAD:backend/onyx/context/search/federated/slack_search_utils.py:212:            data = json.loads(response_clean)
HEAD:backend/onyx/db/admin_banner.py:31:    return AdminBanner.model_validate(raw)
HEAD:backend/onyx/db/chat.py:33:from onyx.utils.postgres_sanitization import sanitize_string
HEAD:backend/onyx/db/chat.py:870:        document_id=sanitize_string(server_search_doc.document_id),
HEAD:backend/onyx/db/chat.py:872:        semantic_id=sanitize_string(server_search_doc.semantic_identifier),
HEAD:backend/onyx/db/chat.py:874:            sanitize_string(server_search_doc.link)
HEAD:backend/onyx/db/chat.py:878:        blurb=sanitize_string(server_search_doc.blurb),
HEAD:backend/onyx/db/chat.py:885:            sanitize_string(server_search_doc.relevance_explanation)
HEAD:backend/onyx/db/chat.py:891:            sanitize_string(h) for h in server_search_doc.match_highlights
HEAD:backend/onyx/db/chat.py:895:            [sanitize_string(o) for o in server_search_doc.primary_owners]
HEAD:backend/onyx/db/chat.py:900:            [sanitize_string(o) for o in server_search_doc.secondary_owners]
HEAD:backend/onyx/db/engine/shard_registry.py:118:        raw = json.loads(ONYX_DB_SHARDS_JSON)
HEAD:backend/onyx/db/engine/shard_routing.py:59:        raw = json.loads(ONYX_DB_SHARD_OVERRIDES_JSON)
HEAD:backend/onyx/db/kg_config.py:21:        return KGConfigSettings.model_validate(stored_config or {})
HEAD:backend/onyx/db/models.py:3450:    tool_call_arguments: Mapped[dict[str, JSON_ro]] = mapped_column(postgresql.JSONB())
HEAD:backend/onyx/db/models.py:4032:    mcp_input_schema: Mapped[dict[str, Any] | None] = mapped_column(
HEAD:backend/onyx/db/opensearch_migration.py:267:        json_loaded_continuation_token_map = json.loads(
HEAD:backend/onyx/db/pydantic_type.py:24:            return json.loads(value.model_dump_json())
HEAD:backend/onyx/db/pydantic_type.py:33:            return self.pydantic_model.model_validate(value)
HEAD:backend/onyx/db/pydantic_type.py:52:            return [json.loads(item.model_dump_json()) for item in value]
HEAD:backend/onyx/db/pydantic_type.py:61:            return [self.pydantic_model.model_validate(item) for item in value]
HEAD:backend/onyx/db/rotate_encryption_key.py:123:                value: Any = json.loads(decrypted_str) if is_json else decrypted_str
HEAD:backend/onyx/db/security_settings.py:20:    return SecuritySettingsOverrides.model_validate(row, from_attributes=True)
HEAD:backend/onyx/db/sso_provider.py:139:        return _CONFIG_MODEL_BY_TYPE[provider_type].model_validate(config).model_dump()
HEAD:backend/onyx/db/sso_provider.py:323:        raw_settings = json.loads(settings_path.read_text(encoding="utf-8"))
HEAD:backend/onyx/db/tools.py:25:from onyx.utils.postgres_sanitization import sanitize_json_like, sanitize_string
HEAD:backend/onyx/db/tools.py:351:    tool_call_arguments: dict[str, Any],
HEAD:backend/onyx/db/tools.py:371:        tool_call_arguments: The tool call arguments
HEAD:backend/onyx/db/tools.py:373:        tool_call_tokens: The number of tokens in the tool call arguments
HEAD:backend/onyx/db/tools.py:393:            sanitize_string(reasoning_tokens) if reasoning_tokens else reasoning_tokens
HEAD:backend/onyx/db/tools.py:395:        tool_call_arguments=sanitize_json_like(tool_call_arguments),
HEAD:backend/onyx/deep_research/dr_loop.py:629:                        span.span_data.input = str(think_tool_call.tool_args)
HEAD:backend/onyx/deep_research/dr_loop.py:638:                            tool_arguments=think_tool_call.tool_args,
HEAD:backend/onyx/deep_research/dr_loop.py:746:                                tool_arguments=current_tool_call.tool_args,
HEAD:backend/onyx/deep_research/dr_loop.py:804:                            tool_call_arguments=current_tool_call.tool_args,
HEAD:backend/onyx/deep_research/utils.py:11:# JSON prefixes to detect in think_tool arguments
HEAD:backend/onyx/deep_research/utils.py:23:    full_arguments: str = ""  # Full accumulated arguments for final tool call
HEAD:backend/onyx/deep_research/utils.py:36:    When we extract content from JSON by string manipulation (without json.loads),
HEAD:backend/onyx/deep_research/utils.py:124:    - Tool call arguments are converted to reasoning_content (JSON wrapper stripped)
HEAD:backend/onyx/deep_research/utils.py:171:                # Accumulate arguments for the think tool
HEAD:backend/onyx/deep_research/utils.py:176:                    and tool_call.function.arguments
HEAD:backend/onyx/deep_research/utils.py:178:                    # Track full arguments for final tool call
HEAD:backend/onyx/deep_research/utils.py:179:                    state.full_arguments += tool_call.function.arguments
HEAD:backend/onyx/deep_research/utils.py:181:                    state.accumulated_args += tool_call.function.arguments
HEAD:backend/onyx/document_index/opensearch/client.py:1560:        return DocumentChunk.model_validate(document_chunk_source)
HEAD:backend/onyx/document_index/opensearch/client.py:1647:                document_chunk=DocumentChunkWithoutVectors.model_validate(
HEAD:backend/onyx/document_index/opensearch/client.py:1874:            chunks.append(DocumentChunkWithoutVectors.model_validate(source))
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:163:            {int(k): v for k, v in json.loads(chunk.source_links).items()}
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:111:    metadata = json.loads(fields[METADATA]) if METADATA in fields else {}
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:132:        json.loads(source_links) if isinstance(source_links, str) else source_links
HEAD:backend/onyx/evals/eval.py:84:        {"tool_name": tc.tool_name, "tool_arguments": tc.tool_arguments}
HEAD:backend/onyx/evals/eval_cli.py:240:    args = parser.parse_args()
HEAD:backend/onyx/evals/one_off/create_braintrust_dataset.py:199:    args = parser.parse_args()
HEAD:backend/onyx/external_apps/matching/graphql_parsing.py:33:        payload = json.loads(body)
HEAD:backend/onyx/federated_connectors/oauth_utils.py:122:    session_dict = json.loads(session_data)
HEAD:backend/onyx/file_processing/extract_file_text.py:176:        return json.loads("{" + json_str + "}")
HEAD:backend/onyx/file_store/document_batch_storage.py:21:    rather than fail the whole batch on `model_validate`."""
HEAD:backend/onyx/file_store/document_batch_storage.py:101:        doc_dicts = json.loads(data)
HEAD:backend/onyx/file_store/document_batch_storage.py:112:                Document.model_validate(self._normalize_doc_dict(doc_dict))
HEAD:backend/onyx/file_store/gcs_file_store.py:86:                    info = json.loads(self._service_account_key_json)
HEAD:backend/onyx/hooks/models.py:74:    input_schema: dict[str, Any]
HEAD:backend/onyx/hooks/points/base.py:32:    input_schema and output_schema are derived from them automatically.
HEAD:backend/onyx/hooks/points/base.py:47:    input_schema: ClassVar[dict[str, Any]]
HEAD:backend/onyx/hooks/points/base.py:56:        input_schema and output_schema are derived automatically from the models.
HEAD:backend/onyx/hooks/points/base.py:70:        cls.input_schema = cls.payload_model.model_json_schema()
HEAD:backend/onyx/image_gen/providers/vertex_img_gen.py:149:            service_account_info = json.loads(self._vertex_credentials)
HEAD:backend/onyx/image_gen/providers/vertex_img_gen.py:274:        vertex_json = json.loads(vertex_credentials)
HEAD:backend/onyx/key_value_store/store.py:58:                    return json.loads(cached.decode("utf-8"))
HEAD:backend/onyx/kg/utils/extraction_utils.py:546:        parsed_result = json.loads(cleaned_response)
HEAD:backend/onyx/kg/vespa/vespa_interactions.py:59:            fields["metadata"] = json.loads(fields["metadata"])
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:151:                    function_args = tool_call.get("function").get("arguments")
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:321:        # Gateways may open tool-call streams with an empty arguments delta;
HEAD:backend/onyx/llm/multi_llm.py:292:                    f"[Tool Call] name={name} id={tc_id} args={args}"
HEAD:backend/onyx/llm/prompt_cache/cache_manager.py:122:            metadata = CacheMetadata.model_validate(metadata_dict)
HEAD:backend/onyx/llm/prompt_cache/utils.py:74:        return cls.model_validate_json(json.dumps(mutated))
HEAD:backend/onyx/llm/prompt_cache/utils.py:76:        return cls.model_validate(mutated)
HEAD:backend/onyx/llm/tracing_wrap.py:121:        bound.arguments.get(_TOOLS_PARAM_NAME),
HEAD:backend/onyx/llm/tracing_wrap.py:142:        prompt, tools = _extract_prompt_and_tools(sig, self, args, kwargs)
HEAD:backend/onyx/llm/tracing_wrap.py:198:        prompt, tools = _extract_prompt_and_tools(sig, self, args, kwargs)
HEAD:backend/onyx/llm/well_known_providers/auto_update_service.py:67:            return LLMRecommendations.model_validate(data)
HEAD:backend/onyx/llm/well_known_providers/llm_provider_options.py:75:    return LLMRecommendations.model_validate(json_config)
HEAD:backend/onyx/mcp_server/tools/search.py:399:        payload = SearchResponse.model_validate_json(response.content)
HEAD:backend/onyx/mcp_server/tools/search.py:456:        payload = WebSearchToolResponse.model_validate_json(response.content)
HEAD:backend/onyx/mcp_server/tools/search.py:511:        payload = OpenUrlsToolResponse.model_validate_json(response.content)
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:442:        service_account_info = json.loads(self.api_key)
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:741:        response_body = json.loads(await response["body"].read())
HEAD:backend/onyx/oauth/authorization_attempt.py:93:            attempt = self._attempt_type.model_validate_json(stored)
HEAD:backend/onyx/onyxbot/discord/api_client.py:178:                response_obj = ChatFullResponse.model_validate(data)
HEAD:backend/onyx/onyxbot/slack/handlers/handle_buttons.py:215:    value_dict = json.loads(req.payload["actions"][0]["value"])
HEAD:backend/onyx/onyxbot/slack/utils.py:53:    return lambda user_id: SlackUserInfoResponse.model_validate(
HEAD:backend/onyx/prompts/tool_prompts.py:15:When searching for information, if the initial results cannot fully answer the user's query, try again with different tools or arguments. \
HEAD:backend/onyx/prompts/tool_prompts.py:85:LLM attempted to call a tool but failed. Most likely the tool name or arguments were misspelled.
HEAD:backend/onyx/redis/redis_connector_delete.py:74:        payload = RedisConnectorDeletePayload.model_validate_json(fence_str)
HEAD:backend/onyx/redis/redis_connector_doc_perm_sync.py:117:        payload = RedisConnectorPermissionSyncPayload.model_validate_json(
HEAD:backend/onyx/redis/redis_connector_ext_group_sync.py:97:        payload = RedisConnectorExternalGroupSyncPayload.model_validate_json(fence_str)
HEAD:backend/onyx/redis/redis_connector_prune.py:121:        payload = RedisConnectorPrunePayload.model_validate_json(fence_str)
HEAD:backend/onyx/redis/redis_pool.py:540:        return json.loads(token_data_str)
HEAD:backend/onyx/redis/redis_pool.py:653:        return json.loads(token_data_str)
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:112:        payload = json.loads(body)
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:282:            decoded = json.loads(body.decode("utf-8"))
HEAD:backend/onyx/server/documents/connector.py:258:                json.loads(metadata_bytes)
HEAD:backend/onyx/server/documents/connector.py:591:        file_ids_list = json.loads(file_ids_to_remove)
HEAD:backend/onyx/server/documents/connector.py:616:            loaded_metadata = json.loads(metadata_bytes)
HEAD:backend/onyx/server/documents/connector.py:647:                loaded_metadata = json.loads(metadata_bytes)
HEAD:backend/onyx/server/documents/credential.py:213:        credential_data = json.loads(credential_json)
HEAD:backend/onyx/server/documents/credential.py:340:        credential_data = json.loads(credential_json)
HEAD:backend/onyx/server/documents/credential_capabilities.py:85:                CredentialCapabilityReport.model_validate(row.report)
HEAD:backend/onyx/server/documents/standard_oauth.py:65:    _validate_additional_kwargs(connector_cls, additional_kwargs_dict)
HEAD:backend/onyx/server/documents/standard_oauth.py:69:def _validate_additional_kwargs(
HEAD:backend/onyx/server/documents/standard_oauth.py:255:    _validate_additional_kwargs(connector_cls, attempt.payload.additional_kwargs)
HEAD:backend/onyx/server/features/build/approvals/api.py:140:        items=[ApprovalView.model_validate(row) for row in pending_rows]
HEAD:backend/onyx/server/features/build/approvals/api.py:160:            ApprovalView.model_validate(current), body.decision, approval_id
HEAD:backend/onyx/server/features/build/approvals/api.py:183:            ApprovalView.model_validate(winner), body.decision, approval_id
HEAD:backend/onyx/server/features/build/approvals/api.py:198:    return ApprovalView.model_validate(decided)
HEAD:backend/onyx/server/features/build/approvals/api.py:334:    return ApprovalView.model_validate(decided_current)
HEAD:backend/onyx/server/features/build/connect_app.py:77:        return ConnectAppRequest.model_validate_json(value)
HEAD:backend/onyx/server/features/build/connect_app.py:98:        return ConnectAppPending.model_validate_json(raw)
HEAD:backend/onyx/server/features/build/external_apps/oauth.py:157:    record = _OAuthStateRecord.model_validate_json(record_bytes.decode("utf-8"))
HEAD:backend/onyx/server/features/build/interactive_turns/api.py:68:            payload = json.loads(raw_data)
HEAD:backend/onyx/server/features/build/interactive_turns/state.py:307:        payload = json.loads(_decode(raw))
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1689:        return OutputsManifestResponse.model_validate_json(result.stdout_text)
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py:169:        payload = FilesystemListRequest.model_validate_json(body)
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py:204:        payload = OutputsManifestRequest.model_validate_json(body)
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py:278:        payload = SnapshotCreateRequest.model_validate_json(body)
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:2024:                detail = json.loads(e.body).get("detail", "")
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/sidecar_client.py:164:        listing = FilesystemListResponse.model_validate_json(resp.content)
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/sidecar_client.py:204:        return OutputsManifestResponse.model_validate_json(resp.content)
HEAD:backend/onyx/server/features/build/sandbox/opencode/event_bus.py:423:        parsed = json.loads(payload)
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:415:        yield AgentThoughtChunk.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:423:        yield AgentMessageChunk.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:815:            yield emit_class.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:890:        yield ToolCallStart.model_validate({"sessionUpdate": "tool_call", **common})
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:895:            yield ToolCallProgress.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:899:        yield ToolCallProgress.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:925:            yield PromptResponse.model_validate({"stopReason": "cancelled"})
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:933:        yield Error.model_validate({"code": TURN_ERROR_CODE_SESSION, "message": msg})
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:949:    yield PromptResponse.model_validate({"stopReason": stop_reason})
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1399:                yield Error.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1407:                yield Error.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1458:                yield Error.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1467:                yield Error.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1482:                    yield PromptResponse.model_validate({"stopReason": "cancelled"})
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1487:                yield Error.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1508:                yield Error.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1554:                    yield PromptResponse.model_validate({"stopReason": "cancelled"})
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1571:                    yield Error.model_validate(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1592:                    yield Error.model_validate(
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:112:    data["editor_payload"] = model_cls.model_validate(raw)
HEAD:backend/onyx/server/features/mcp/api.py:687:            existing_client = OAuthClientInformationFull.model_validate(
HEAD:backend/onyx/server/features/mcp/api.py:813:        client_info = OAuthClientInformationFull.model_validate(client_info_raw)
HEAD:backend/onyx/server/features/mcp/api.py:959:    client_info = OAuthClientInformationFull.model_validate(client_info_raw)
HEAD:backend/onyx/server/features/mcp/api.py:1251:                OAuthClientInformationFull.model_validate(client_info_raw)
HEAD:backend/onyx/server/features/mcp/api.py:1505:        input_schema = tool.inputSchema
HEAD:backend/onyx/server/features/mcp/api.py:1510:            existing_tool.mcp_input_schema = input_schema
HEAD:backend/onyx/server/features/mcp/api.py:1525:        new_tool.mcp_input_schema = input_schema
HEAD:backend/onyx/server/features/mcp/api.py:1759:                client_info = OAuthClientInformationFull.model_validate(client_info_raw)
HEAD:backend/onyx/server/features/mcp/client.py:246:def _call_mcp_tool(tool_name: str, arguments: dict[str, Any]) -> MCPClientFunction[str]:
HEAD:backend/onyx/server/features/mcp/client.py:249:        result = await session.call_tool(tool_name, arguments)
HEAD:backend/onyx/server/features/mcp/client.py:265:        _call_mcp_tool(tool_name, arguments),
HEAD:backend/onyx/server/features/mcp/oauth.py:141:        payload = json.loads(body)
HEAD:backend/onyx/server/features/mcp/oauth.py:164:        return OAuthToken.model_validate_json(body)
HEAD:backend/onyx/server/features/mcp/oauth.py:169:            return OAuthToken.model_validate(payload)
HEAD:backend/onyx/server/features/mcp/oauth.py:337:                            OAuthMetadata.model_validate(metadata_raw)
HEAD:backend/onyx/server/features/mcp/oauth.py:341:                return OAuthToken.model_validate(tokens_raw)
HEAD:backend/onyx/server/features/mcp/oauth.py:397:                        OAuthClientInformationFull.model_validate(
HEAD:backend/onyx/server/features/mcp/oauth.py:532:                return OAuthClientInformationFull.model_validate(client_info_raw)
HEAD:backend/onyx/server/features/mcp/oauth.py:543:                        return OAuthClientInformationFull.model_validate(
HEAD:backend/onyx/server/features/mcp/oauth.py:567:                            OAuthClientInformationFull.model_validate(
HEAD:backend/onyx/server/features/notifications/api.py:174:        NotificationResponse.model_validate(notif)
HEAD:backend/onyx/server/features/projects/api.py:203:                parsed = json.loads(temp_id_map)
HEAD:backend/onyx/server/features/search/api.py:49:from onyx.tools.models import ChatMinimalTextMessage, SearchToolOverrideKwargs
HEAD:backend/onyx/server/features/search/api.py:182:        override_kwargs=SearchToolOverrideKwargs(
HEAD:backend/onyx/server/features/search/api.py:200:    entries = json.loads(llm_facing_text)["results"] if llm_facing_text else []
HEAD:backend/onyx/server/features/usage/api.py:327:            UsageExportRecord.model_validate(row.model_dump(exclude={"email"}))
HEAD:backend/onyx/server/features/usage/api.py:374:            SystemUsageRecord.model_validate(row.model_dump())
HEAD:backend/onyx/server/federated/api.py:304:                entities_dict = json.loads(query_params["entities"])
HEAD:backend/onyx/server/manage/discord_bot/api.py:163:    return [DiscordGuildConfigResponse.model_validate(c) for c in configs]
HEAD:backend/onyx/server/manage/discord_bot/api.py:194:    return DiscordGuildConfigResponse.model_validate(config)
HEAD:backend/onyx/server/manage/discord_bot/api.py:217:    return DiscordGuildConfigResponse.model_validate(config)
HEAD:backend/onyx/server/manage/discord_bot/api.py:263:    return [DiscordChannelConfigResponse.model_validate(c) for c in configs]
HEAD:backend/onyx/server/manage/discord_bot/api.py:295:    return DiscordChannelConfigResponse.model_validate(config)
HEAD:backend/onyx/server/manage/llm/api.py:1476:            ollama_model_details = OllamaModelDetails.model_validate(show_response_json)
HEAD:backend/onyx/server/manage/llm/api.py:1589:            model_details = OpenRouterModelDetails.model_validate(item)
HEAD:backend/onyx/server/manage/llm/api.py:1793:            model_details = LitellmModelDetails.model_validate(model)
HEAD:backend/onyx/server/manage/llm/provider_cache.py:112:            response=LLMProviderResponse[LLMProviderDescriptor].model_validate_json(
HEAD:backend/onyx/server/manage/voice/user_api.py:127:        parsed = json.loads(raw[json_start:])
HEAD:backend/onyx/server/manage/voice/websocket_api.py:408:        data = json.loads(text)
HEAD:backend/onyx/server/manage/voice/websocket_api.py:692:                data = json.loads(message["text"])
HEAD:backend/onyx/server/manage/voice/websocket_api.py:956:                    data = json.loads(message["text"])
HEAD:backend/onyx/server/manage/voice/websocket_api.py:1080:                data = json.loads(message["text"])
HEAD:backend/onyx/server/manage/voice/websocket_api.py:1234:                        data = json.loads(message["text"])
HEAD:backend/onyx/server/metrics/indexing_pipeline.py:286:            msg = json.loads(raw)
HEAD:backend/onyx/server/pat/api.py:59:    return [TokenResponse.model_validate(pat) for pat in pats]
HEAD:backend/onyx/server/pat/api.py:89:        **TokenResponse.model_validate(pat).model_dump(),
HEAD:backend/onyx/server/query_and_chat/session_loading.py:30:    CustomToolArgs,
HEAD:backend/onyx/server/query_and_chat/session_loading.py:195:    tool_args: dict[str, Any] | None = None,
HEAD:backend/onyx/server/query_and_chat/session_loading.py:207:    if tool_args:
HEAD:backend/onyx/server/query_and_chat/session_loading.py:211:                obj=CustomToolArgs(tool_name=tool_name, tool_args=tool_args),
HEAD:backend/onyx/server/query_and_chat/session_loading.py:255:        data = json.loads(summary_json)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:596:                            list[str], tool_call.tool_call_arguments.get("queries", [])
HEAD:backend/onyx/server/query_and_chat/session_loading.py:618:                        # Get URLs from tool_call_arguments
HEAD:backend/onyx/server/query_and_chat/session_loading.py:620:                            list[str], tool_call.tool_call_arguments.get("urls", [])
HEAD:backend/onyx/server/query_and_chat/session_loading.py:656:                            tool_call.tool_call_arguments.get(RESEARCH_AGENT_TASK_KEY)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:671:                            tool_call.tool_call_arguments.get(CODING_AGENT_QUERY_KEY)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:676:                            tool_call.tool_call_arguments.get(CODING_AGENT_REPO_KEY)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:691:                            memory_data = json.loads(tool_call.tool_call_response)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:709:                            tool_call.tool_call_arguments.get("code", ""),
HEAD:backend/onyx/server/query_and_chat/session_loading.py:716:                                response_data = json.loads(tool_call.tool_call_response)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:751:                            parsed = json.loads(tool_call.tool_call_response)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:778:                            for k, v in (tool_call.tool_call_arguments or {}).items()
HEAD:backend/onyx/server/query_and_chat/session_loading.py:790:                                tool_args=custom_args if custom_args else None,
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:35:    CUSTOM_TOOL_ARGS = "custom_tool_args"
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:156:    tool_args: dict[str, Any]
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:276:class CustomToolArgs(BaseObj):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:277:    type: Literal["custom_tool_args"] = StreamingType.CUSTOM_TOOL_ARGS.value
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:280:    tool_args: dict[str, Any]
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:458:    CustomToolArgs,
HEAD:backend/onyx/server/saml_multi.py:113:        return SAMLProviderConfig.model_validate(raw)
HEAD:backend/onyx/server/security/api.py:44:        payload_dict = json.loads(raw) if raw else {}
HEAD:backend/onyx/server/security/api.py:52:        overrides = SecuritySettingsOverrides.model_validate(payload_dict)
HEAD:backend/onyx/server/security/store.py:212:    return SecuritySettingsOverrides.model_validate(merged)
HEAD:backend/onyx/server/settings/api.py:234:        [NotificationResponse.model_validate(product_notif[0])] if product_notif else []
HEAD:backend/onyx/server/settings/api.py:273:        notifications.append(NotificationResponse.model_validate(reindex_notif))
HEAD:backend/onyx/server/settings/store.py:56:            Settings.model_validate(stored_settings) if stored_settings else Settings()
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:61:Configure the MCP client to launch `browser` with `["mcp"]`. The server defaults to MCP protocol 2025-11-25 and accepts older supported client protocol versions during initialization. The default tools profile is `core`, which keeps MCP context small for everyday browser automation. Use `--tools all` for the full typed CLI parity surface, or combine profiles with commas, such as `--tools core,network,react`. Profiles are `core`, `network`, `state`, `debug`, `tabs`, `react`, `mobile`, and `all`; the `debug` profile includes plugin registry and command.run tools. Each tool accepts typed arguments plus `extraArgs` for advanced CLI flags and exact CLI parity. Tool discovery is paginated and includes read-only/open-world annotations so modern MCP clients can load the large typed surface incrementally. Use the tool `session` argument or `AGENT_BROWSER_SESSION` to isolate browser sessions.
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1215:Tool calls use the same config files and environment variables as the CLI. Each tool accepts typed arguments plus `extraArgs` for advanced CLI flags and exact CLI parity. Tool discovery is paginated and includes read-only/open-world annotations so modern MCP clients can load the large typed surface incrementally. Use the `session` tool argument or `AGENT_BROWSER_SESSION` to isolate browser state.
HEAD:backend/onyx/skills/builtin/gmail/gmail_api.py:68:    return json.loads(raw) if raw.strip() else {}
HEAD:backend/onyx/skills/builtin/gmail/gmail_api.py:385:        body = json.loads(a.json_body)
HEAD:backend/onyx/skills/builtin/gmail/gmail_api.py:398:    a = _build_parser().parse_args(argv[1:])
HEAD:backend/onyx/skills/builtin/google-calendar/gcal_api.py:57:    return json.loads(raw) if raw.strip() else {}
HEAD:backend/onyx/skills/builtin/google-calendar/gcal_api.py:194:        body = json.loads(a.json_body)
HEAD:backend/onyx/skills/builtin/google-calendar/gcal_api.py:202:    a = _build_parser().parse_args(argv[1:])
HEAD:backend/onyx/skills/builtin/google-drive/gdrive_api.py:118:    return json.loads(raw) if raw.strip() else {}
HEAD:backend/onyx/skills/builtin/google-drive/gdrive_api.py:146:    return json.loads(raw) if raw.strip() else {}
HEAD:backend/onyx/skills/builtin/google-drive/gdrive_api.py:222:    return json.loads(raw) if raw.strip() else {}
HEAD:backend/onyx/skills/builtin/google-drive/gdrive_api.py:591:            requests = json.loads(raw_requests)
HEAD:backend/onyx/skills/builtin/google-drive/gdrive_api.py:621:            parsed_body = json.loads(a.json_body)
HEAD:backend/onyx/skills/builtin/google-drive/gdrive_api.py:631:    a = _build_parser().parse_args(argv[1:])
HEAD:backend/onyx/skills/builtin/google-drive/gsheets_api.py:63:    return json.loads(raw) if raw.strip() else {}
HEAD:backend/onyx/skills/builtin/google-drive/gsheets_api.py:76:    return json.loads(raw)
HEAD:backend/onyx/skills/builtin/google-drive/gsheets_api.py:236:    a = _build_parser().parse_args(argv[1:])
HEAD:backend/onyx/skills/builtin/google-drive/gslides_api.py:69:    return json.loads(raw) if raw.strip() else {}
HEAD:backend/onyx/skills/builtin/google-drive/gslides_api.py:118:    return json.loads(raw)
HEAD:backend/onyx/skills/builtin/google-drive/gslides_api.py:281:    a = _build_parser().parse_args(argv[1:])
HEAD:backend/onyx/skills/builtin/hubspot/hubspot_api.py:61:    return json.loads(raw) if raw else {}
HEAD:backend/onyx/skills/builtin/hubspot/hubspot_api.py:241:        parsed = json.loads(a.body)
HEAD:backend/onyx/skills/builtin/hubspot/hubspot_api.py:250:    a = _build_parser().parse_args(argv[1:])
HEAD:backend/onyx/skills/builtin/hubspot/hubspot_api.py:259:            parsed = json.loads(detail)
HEAD:backend/onyx/skills/builtin/linear/linear_api.py:57:        return json.loads(resp.read().decode("utf-8"))
HEAD:backend/onyx/skills/builtin/linear/linear_api.py:110:    """Map parsed args onto an IssueCreateInput dict, including only the keys
HEAD:backend/onyx/skills/builtin/linear/linear_api.py:291:        parsed = json.loads(a.variables)
HEAD:backend/onyx/skills/builtin/linear/linear_api.py:302:    a = _build_parser().parse_args(argv[1:])
HEAD:backend/onyx/skills/builtin/notion/notion_api.py:56:        return json.loads(raw) if raw else {}
HEAD:backend/onyx/skills/builtin/notion/notion_api.py:316:    a = _build_parser().parse_args(argv[1:])
HEAD:backend/onyx/skills/builtin/notion/notion_api.py:322:            message = json.loads(detail).get("message", detail)
HEAD:backend/onyx/skills/builtin/pptx/scripts/icon.js:228:function parseArgs(argv) {
HEAD:backend/onyx/skills/builtin/pptx/scripts/icon.js:260:  const opts = parseArgs(process.argv.slice(2));
HEAD:backend/onyx/skills/builtin/pptx/scripts/lint.py:864:    args = parser.parse_args()
HEAD:backend/onyx/skills/builtin/pptx/scripts/office/pack.py:148:    args = parser.parse_args()
HEAD:backend/onyx/skills/builtin/pptx/scripts/office/pack.py:154:        validate=args.validate,
HEAD:backend/onyx/skills/builtin/pptx/scripts/office/unpack.py:120:    args = parser.parse_args()
HEAD:backend/onyx/skills/builtin/pptx/scripts/office/validate.py:56:    args = parser.parse_args()
HEAD:backend/onyx/skills/builtin/pptx/scripts/thumbnail.py:58:    args = parser.parse_args()
HEAD:backend/onyx/skills/builtin/slack/slack_api.py:71:        return json.loads(resp.read().decode("utf-8"))
HEAD:backend/onyx/skills/builtin/slack/slack_api.py:163:        parsed = json.loads(json_args)
HEAD:backend/onyx/skills/builtin/slack/slack_api.py:261:    a = _build_parser().parse_args(argv[1:])
HEAD:backend/onyx/skills/metadata.py:109:        metadata = SkillMetadata.model_validate(frontmatter)
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:50:    BashToolOverrideKwargs,
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:151:    cmd = tool_call.tool_args.get(BASH_TOOL_CMD_KEY)
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:169:        override_kwargs=BashToolOverrideKwargs(),
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:282:        span.span_data.input = str(coding_agent_call.tool_args)
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:284:            query = coding_agent_call.tool_args[CODING_AGENT_QUERY_KEY]
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:285:            repo = coding_agent_call.tool_args[CODING_AGENT_REPO_KEY]
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:422:                                    tool_arguments=think_tool_call.tool_args,
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:463:                                tool_arguments=tc.tool_args,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:236:        span.span_data.input = str(research_agent_call.tool_args)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:256:            research_topic = research_agent_call.tool_args[RESEARCH_AGENT_TASK_KEY]
HEAD:backend/onyx/tools/fake_tools/research_agent.py:440:                        think_span.span_data.input = str(think_tool_call.tool_args)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:446:                            tool_arguments=think_tool_call.tool_args,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:526:                                    tool_arguments=tc.tool_args,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:591:                            tool_call_arguments=tc.tool_args,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:658:    research_agent_call: ToolCallKickoff = args[0]  # First arg
HEAD:backend/onyx/tools/fake_tools/research_agent.py:659:    research_task = research_agent_call.tool_args.get(
HEAD:backend/onyx/tools/fake_tools/research_agent.py:803:                tool_args={RESEARCH_AGENT_TASK_KEY: RESEARCH_PROMPT},
HEAD:backend/onyx/tools/interface.py:86:        # Specific tool override arguments that are not provided by the LLM
HEAD:backend/onyx/tools/models.py:28:TOOL_CALL_MSG_ARGUMENTS = "arguments"
HEAD:backend/onyx/tools/models.py:71:    tool_args: dict[str, Any]
HEAD:backend/onyx/tools/models.py:79:                TOOL_CALL_MSG_ARGUMENTS: self.tool_args,
HEAD:backend/onyx/tools/models.py:160:class WebSearchToolOverrideKwargs(BaseModel):
HEAD:backend/onyx/tools/models.py:165:class OpenURLToolOverrideKwargs(BaseModel):
HEAD:backend/onyx/tools/models.py:174:class SearchToolOverrideKwargs(BaseModel):
HEAD:backend/onyx/tools/models.py:234:class PythonToolOverrideKwargs(BaseModel):
HEAD:backend/onyx/tools/models.py:276:    tool_call_arguments: dict[str, Any]
HEAD:backend/onyx/tools/tool_constructor.py:489:                    tool_definition=saved_tool.mcp_input_schema or {},
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:33:class BashToolOverrideKwargs(BaseModel):
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:45:class BashTool(Tool[BashToolOverrideKwargs]):
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:132:        override_kwargs: BashToolOverrideKwargs,  # noqa: ARG002
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:26:class CodingAgentToolOverrideKwargs(BaseModel):
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:30:class CodingAgentTool(Tool[CodingAgentToolOverrideKwargs]):
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:123:        override_kwargs: CodingAgentToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:159:            tool_args={
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:16:    CustomToolArgs,
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:164:                        f"Please provide it in the tool call arguments."
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:178:        tool_args = {**path_params, **query_params}
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:179:        if tool_args:
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:183:                    obj=CustomToolArgs(
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:185:                        tool_args=tool_args,
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:315:        openapi_schema = json.loads(schema_str)
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:36:class FileReaderToolOverrideKwargs:
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:40:class FileReaderTool(Tool[FileReaderToolOverrideKwargs]):
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:150:        override_kwargs: FileReaderToolOverrideKwargs,  # noqa: ARG002
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:35:class MemoryToolOverrideKwargs(BaseModel):
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:46:class MemoryTool(Tool[MemoryToolOverrideKwargs]):
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:110:        override_kwargs: MemoryToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:35:from onyx.tools.models import OpenURLToolOverrideKwargs, ToolCallException, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:412:class OpenURLTool(Tool[OpenURLToolOverrideKwargs]):
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:531:        override_kwargs: OpenURLToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_implementations/python/code_interpreter_client.py:402:                        yield model_cls(**json.loads(data))
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:35:    PythonToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:214:class PythonTool(Tool[PythonToolOverrideKwargs]):
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:352:        override_kwargs: PythonToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:112:    SearchToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:270:class SearchTool(Tool[SearchToolOverrideKwargs]):
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:667:        override_kwargs: SearchToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:23:    WebSearchToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:85:class WebSearchTool(Tool[WebSearchToolOverrideKwargs]):
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:203:        override_kwargs: WebSearchToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_runner.py:19:    OpenURLToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_runner.py:21:    PythonToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_runner.py:22:    SearchToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_runner.py:27:    WebSearchToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_runner.py:31:    CodingAgentToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_runner.py:35:    MemoryToolOverrideKwargs,
HEAD:backend/onyx/tools/tool_runner.py:92:                values = call.tool_args.get(merge_field, [])
HEAD:backend/onyx/tools/tool_runner.py:100:            merged_args = calls[0].tool_args.copy()
HEAD:backend/onyx/tools/tool_runner.py:106:                tool_args=merged_args,
HEAD:backend/onyx/tools/tool_runner.py:139:        span_fn.span_data.input = str(tool_call.tool_args)
HEAD:backend/onyx/tools/tool_runner.py:144:                **tool_call.tool_args,
HEAD:backend/onyx/tools/tool_runner.py:163:                        "tool_args": tool_call.tool_args,
HEAD:backend/onyx/tools/tool_runner.py:184:                        "tool_args": tool_call.tool_args,
HEAD:backend/onyx/tools/tool_runner.py:211:                        "tool_args": tool_call.tool_args,
HEAD:backend/onyx/tools/tool_runner.py:273:            for `SearchTool` override kwargs).
HEAD:backend/onyx/tools/tool_runner.py:340:    # Prepare all tool calls with their override_kwargs
HEAD:backend/onyx/tools/tool_runner.py:351:            SearchToolOverrideKwargs
HEAD:backend/onyx/tools/tool_runner.py:352:            | WebSearchToolOverrideKwargs
HEAD:backend/onyx/tools/tool_runner.py:353:            | OpenURLToolOverrideKwargs
HEAD:backend/onyx/tools/tool_runner.py:354:            | PythonToolOverrideKwargs
HEAD:backend/onyx/tools/tool_runner.py:355:            | MemoryToolOverrideKwargs
HEAD:backend/onyx/tools/tool_runner.py:356:            | CodingAgentToolOverrideKwargs
HEAD:backend/onyx/tools/tool_runner.py:373:            override_kwargs = SearchToolOverrideKwargs(
HEAD:backend/onyx/tools/tool_runner.py:386:            override_kwargs = WebSearchToolOverrideKwargs(
HEAD:backend/onyx/tools/tool_runner.py:393:            override_kwargs = OpenURLToolOverrideKwargs(
HEAD:backend/onyx/tools/tool_runner.py:401:            override_kwargs = PythonToolOverrideKwargs(
HEAD:backend/onyx/tools/tool_runner.py:405:            override_kwargs = CodingAgentToolOverrideKwargs()
HEAD:backend/onyx/tools/tool_runner.py:407:            override_kwargs = MemoryToolOverrideKwargs(
HEAD:backend/onyx/tools/tool_runner.py:423:        tool_run_params.append((tool, tool_call, override_kwargs))
HEAD:backend/onyx/tools/tool_runner.py:427:        (_safe_run_single_tool, (tool, tool_call, override_kwargs))
HEAD:backend/onyx/tools/tool_runner.py:428:        for tool, tool_call, override_kwargs in tool_run_params
HEAD:backend/onyx/utils/external_endpoint.py:240:            validated_model = response_type.model_validate(outcome.response_payload)
HEAD:backend/onyx/utils/long_term_log.py:122:                results.append(json.loads(file.read_text()))
HEAD:backend/onyx/utils/postgres_sanitization.py:13:def sanitize_string(value: str) -> str:
HEAD:backend/onyx/utils/postgres_sanitization.py:24:            "sanitize_string: all characters were removed from a non-empty string"
HEAD:backend/onyx/utils/postgres_sanitization.py:32:        return sanitize_string(value)
HEAD:backend/onyx/utils/postgres_sanitization.py:43:            cleaned_key = sanitize_string(key) if isinstance(key, str) else key
HEAD:backend/onyx/utils/postgres_sanitization.py:54:                sanitize_string(expert.display_name)
HEAD:backend/onyx/utils/postgres_sanitization.py:59:                sanitize_string(expert.first_name)
HEAD:backend/onyx/utils/postgres_sanitization.py:64:                sanitize_string(expert.middle_initial)
HEAD:backend/onyx/utils/postgres_sanitization.py:69:                sanitize_string(expert.last_name)
HEAD:backend/onyx/utils/postgres_sanitization.py:74:                sanitize_string(expert.email) if expert.email is not None else None
HEAD:backend/onyx/utils/postgres_sanitization.py:83:            sanitize_string(email) for email in external_access.external_user_emails
HEAD:backend/onyx/utils/postgres_sanitization.py:86:            sanitize_string(group_id)
HEAD:backend/onyx/utils/postgres_sanitization.py:96:    cleaned_doc.id = sanitize_string(cleaned_doc.id)
HEAD:backend/onyx/utils/postgres_sanitization.py:97:    cleaned_doc.semantic_identifier = sanitize_string(cleaned_doc.semantic_identifier)
HEAD:backend/onyx/utils/postgres_sanitization.py:99:        cleaned_doc.title = sanitize_string(cleaned_doc.title)
HEAD:backend/onyx/utils/postgres_sanitization.py:101:        cleaned_doc.parent_hierarchy_raw_node_id = sanitize_string(
HEAD:backend/onyx/utils/postgres_sanitization.py:106:        sanitize_string(key): (
HEAD:backend/onyx/utils/postgres_sanitization.py:107:            [sanitize_string(item) for item in value]
HEAD:backend/onyx/utils/postgres_sanitization.py:109:            else sanitize_string(value)
HEAD:backend/onyx/utils/postgres_sanitization.py:133:            section.link = sanitize_string(section.link)
HEAD:backend/onyx/utils/postgres_sanitization.py:135:            section.text = sanitize_string(section.text)
HEAD:backend/onyx/utils/postgres_sanitization.py:137:            section.image_file_id = sanitize_string(section.image_file_id)
HEAD:backend/onyx/utils/postgres_sanitization.py:149:    cleaned_node.raw_node_id = sanitize_string(cleaned_node.raw_node_id)
HEAD:backend/onyx/utils/postgres_sanitization.py:150:    cleaned_node.display_name = sanitize_string(cleaned_node.display_name)
HEAD:backend/onyx/utils/postgres_sanitization.py:152:        cleaned_node.raw_parent_id = sanitize_string(cleaned_node.raw_parent_id)
HEAD:backend/onyx/utils/postgres_sanitization.py:154:        cleaned_node.link = sanitize_string(cleaned_node.link)
HEAD:backend/onyx/utils/sensitive.py:100:                self._decrypted_value = json.loads(decrypted_str)
HEAD:backend/onyx/utils/supervisord_watchdog.py:109:    args = parser.parse_args()
HEAD:backend/onyx/utils/text_processing.py:164:                            parsed = json.loads(candidate)
HEAD:backend/onyx/utils/text_processing.py:197:            result = json.loads(json_match.group(1))
HEAD:backend/onyx/utils/text_processing.py:205:        result = json.loads(content)
HEAD:backend/onyx/utils/text_processing.py:215:            result = json.loads(json_match.group(0))
HEAD:backend/onyx/utils/url.py:450:            url, validated_ip, hostname, port, headers, timeout, **kwargs
HEAD:backend/onyx/utils/url.py:456:        url, validated_ip, original_hostname, port, headers, timeout, **kwargs
HEAD:backend/onyx/voice/providers/elevenlabs.py:207:                        parsed_data = json.loads(msg.data)
HEAD:backend/onyx/voice/providers/elevenlabs.py:529:                    data = json.loads(msg.data)
HEAD:backend/onyx/voice/providers/openai.py:152:                    data = json.loads(msg.data)
```
Tool arguments are model-influenced input and therefore untrusted until
validated.
## Tool Execution Dispatch
Evidence lines: 32
```text
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:7:For the Search API that runs the full SearchTool.run() pipeline (the same
HEAD:backend/onyx/chat/llm_loop.py:85:from onyx.tools.tool_runner import run_tool_calls
HEAD:backend/onyx/chat/llm_loop.py:1128:            parallel_tool_call_results = run_tool_calls(
HEAD:backend/onyx/chat/llm_loop.py:1154:                # Extract tool_call from the response (set by run_tool_calls)
HEAD:backend/onyx/chat/process_message.py:269:    file into RAM for chats that never invoke the Python tool.
HEAD:backend/onyx/chat/process_message.py:1708:                    # to SearchTool.run() so that all invocations of the SearchTool
HEAD:backend/onyx/db/tools.py:194:    rows = db_session.execute(_connected_to_groups_stmt(Tool.id, group_ids)).all()
HEAD:backend/onyx/llm/tracing_wrap.py:144:            self, flow=LLMFlow.UNTAGGED_INVOKE, input_messages=prompt, tools=tools
HEAD:backend/onyx/prompts/tool_prompts.py:56:Use the `run_python` tool to execute Python code in an isolated sandbox. The tool will respond with the output of the execution or time out after 60.0 seconds.
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:155:    * ``tools/call`` → an ``AllMatchedActions`` over the invoked tool(s), each
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:237:    """One MatchedAction per invoked tool; a single DENY when unclassifiable."""
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:254:    # request that invokes the same tool several times.
HEAD:backend/onyx/server/features/build/sandbox/image/opencode-plugins/turn-budget.ts:63:    "tool.execute.after": async (_input, output) => {
HEAD:backend/onyx/server/features/mcp/oauth.py:3:Used by chat tool calls (`MCPTool.run`), the admin/user MCP API routes, and the
HEAD:backend/onyx/server/features/search/api.py:3:Runs the full SearchTool.run() pipeline — the same multi-stage search that
HEAD:backend/onyx/server/features/search/api.py:180:    tool_response = search_tool.run(
HEAD:backend/onyx/server/query_and_chat/placement.py:15:        sub_turn_index: Nesting level for tools that invoke other tools. ``None`` for
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:167:    response = bash_tool.run(
HEAD:backend/onyx/tools/fake_tools/research_agent.py:75:from onyx.tools.tool_runner import run_tool_calls
HEAD:backend/onyx/tools/fake_tools/research_agent.py:471:                    parallel_tool_call_results = run_tool_calls(
HEAD:backend/onyx/tools/models.py:117:class ToolRunnerResponse(BaseModel):
HEAD:backend/onyx/tools/models.py:123:    def validate_tool_runner_response(self) -> "ToolRunnerResponse":
HEAD:backend/onyx/tools/tool_implementations/knowledge_graph/knowledge_graph_tool.py:81:        raise NotImplementedError("KnowledgeGraphTool.run is not implemented.")
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:150:        """Execute the MCP tool by calling the MCP server"""
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:290:            logger.error("Failed to execute MCP tool '%s': %s", self._name, e)
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:534:        """Execute the open URL tool to fetch content from the specified URLs.
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:206:        """Execute the web search tool with multiple queries in parallel"""
HEAD:backend/onyx/tools/tool_runner.py:123:    """Execute a single tool and return its response.
HEAD:backend/onyx/tools/tool_runner.py:141:            tool_response = tool.run(
HEAD:backend/onyx/tools/tool_runner.py:232:def run_tool_calls(
HEAD:backend/onyx/tools/tool_runner.py:261:    Tools are executed in parallel (threadpool). For tools that generate citations,
HEAD:backend/onyx/tools/tool_runner.py:270:        tool_calls: List of tool calls to execute.
```
Execution dispatch is the transition from probabilistic model output into a
deterministic side effect.
This is one of the highest-risk boundaries in an agentic application.
## Tool Result to Model Context
Evidence lines: 299
```text
HEAD:backend/ee/onyx/server/gateway/api.py:867:    """LiteLLM's Anthropic adapter handles text/image/tool_use/tool_result block
HEAD:backend/ee/onyx/server/gateway/api.py:869:    content on system/tool messages is collapsed because our SystemMessage/
HEAD:backend/ee/onyx/server/gateway/api.py:870:    ToolMessage content is str-only."""
HEAD:backend/ee/onyx/server/gateway/api.py:880:            if not isinstance(block, dict) or block.get("type") != "tool_result":
HEAD:backend/ee/onyx/server/gateway/api.py:882:            tool_result_content = block.get("content")
HEAD:backend/ee/onyx/server/gateway/api.py:883:            if not isinstance(tool_result_content, list):
HEAD:backend/ee/onyx/server/gateway/api.py:887:                for part in tool_result_content
HEAD:backend/ee/onyx/server/gateway/api.py:891:                    "Multimodal tool_result content is not supported by the "
HEAD:backend/ee/onyx/server/gateway/api.py:1254:                            content_block=AnthropicToolUseBlock.create(
HEAD:backend/ee/onyx/server/gateway/api.py:1267:                    emit(AnthropicContentBlockStopEvent.create(index=tool_index))
HEAD:backend/ee/onyx/server/gateway/api.py:1376:    content.extend(tool_blocks)
HEAD:backend/onyx/chat/README.md:50:make the context clearer to the LLM. Note that for search results (whether web or internal, it will just be the json) and it will be a Tool Call type of
HEAD:backend/onyx/chat/README.md:230:- Run tool calls and gather results
HEAD:backend/onyx/chat/chat_utils.py:157:    return FileContextResult(message=message, tool_metadata=metadata)
HEAD:backend/onyx/chat/chat_utils.py:867:                            message="",  # No text content when making tool calls
HEAD:backend/onyx/chat/chat_utils.py:880:                        tool_response_message = (
HEAD:backend/onyx/chat/chat_utils.py:889:                                message=tool_response_message,
HEAD:backend/onyx/chat/chat_utils.py:890:                                token_count=token_counter(tool_response_message),
HEAD:backend/onyx/chat/chat_utils.py:1003:        message="",  # No text content when making tool calls
HEAD:backend/onyx/chat/citation_processor.py:623:        citations during processing (e.g., from tool results like web search).
HEAD:backend/onyx/chat/citation_utils.py:6:from onyx.tools.models import ToolResponse
HEAD:backend/onyx/chat/citation_utils.py:9:def update_citation_processor_from_tool_response(
HEAD:backend/onyx/chat/citation_utils.py:10:    tool_response: ToolResponse,
HEAD:backend/onyx/chat/citation_utils.py:20:        tool_response: The response from the tool execution (must have tool_call set)
HEAD:backend/onyx/chat/citation_utils.py:24:    if tool_response.tool_call is None:
HEAD:backend/onyx/chat/citation_utils.py:28:    if tool_response.tool_call.tool_name in CITEABLE_TOOLS_NAMES:
HEAD:backend/onyx/chat/citation_utils.py:30:        if isinstance(tool_response.rich_response, SearchDocsResponse):
HEAD:backend/onyx/chat/citation_utils.py:31:            search_response = tool_response.rich_response
HEAD:backend/onyx/chat/compression.py:286:                    AssistantMessage(content=f"[Used tools: {', '.join(tool_names)}]")
HEAD:backend/onyx/chat/llm_loop.py:17:from onyx.chat.citation_utils import update_citation_processor_from_tool_response
HEAD:backend/onyx/chat/llm_loop.py:72:    MemoryToolResponseSnapshot,
HEAD:backend/onyx/chat/llm_loop.py:76:    ToolResponse,
HEAD:backend/onyx/chat/llm_loop.py:79:from onyx.tools.tool_implementations.memory.models import MemoryToolResponse
HEAD:backend/onyx/chat/llm_loop.py:242:        not llm_step_result.tool_calls or len(llm_step_result.tool_calls) == 0
HEAD:backend/onyx/chat/llm_loop.py:245:        llm_step_result.reasoning and not llm_step_result.answer and no_tool_calls
HEAD:backend/onyx/chat/llm_loop.py:248:        _looks_like_xml_tool_call_payload(llm_step_result.answer)
HEAD:backend/onyx/chat/llm_loop.py:249:        or _looks_like_xml_tool_call_payload(llm_step_result.raw_answer)
HEAD:backend/onyx/chat/llm_loop.py:250:        or _looks_like_xml_tool_call_payload(llm_step_result.reasoning)
HEAD:backend/onyx/chat/llm_loop.py:280:    if not extracted_tool_calls and llm_step_result.reasoning:
HEAD:backend/onyx/chat/llm_loop.py:618:    return _drop_orphaned_tool_call_responses(result)
HEAD:backend/onyx/chat/llm_loop.py:1079:            llm_step_result, attempted = _try_fallback_tool_extraction(
HEAD:backend/onyx/chat/llm_loop.py:1095:            tool_responses: list[ToolResponse] = []
HEAD:backend/onyx/chat/llm_loop.py:1096:            tool_calls = llm_step_result.tool_calls or []
HEAD:backend/onyx/chat/llm_loop.py:1128:            parallel_tool_call_results = run_tool_calls(
HEAD:backend/onyx/chat/llm_loop.py:1142:            tool_responses = parallel_tool_call_results.tool_responses
HEAD:backend/onyx/chat/llm_loop.py:1143:            citation_mapping = parallel_tool_call_results.updated_citation_mapping
HEAD:backend/onyx/chat/llm_loop.py:1146:            if tool_calls and not tool_responses:
HEAD:backend/onyx/chat/llm_loop.py:1153:            for tool_response in tool_responses:
HEAD:backend/onyx/chat/llm_loop.py:1155:                if tool_response.tool_call is None:
HEAD:backend/onyx/chat/llm_loop.py:1158:                tool_call = tool_response.tool_call
HEAD:backend/onyx/chat/llm_loop.py:1171:                        parsed = json.loads(tool_response.llm_facing_response)
HEAD:backend/onyx/chat/llm_loop.py:1179:                # Add the results to the chat history. Even though tools may run in parallel,
HEAD:backend/onyx/chat/llm_loop.py:1191:                if isinstance(tool_response.rich_response, SearchDocsResponse):
HEAD:backend/onyx/chat/llm_loop.py:1192:                    search_docs = tool_response.rich_response.search_docs
HEAD:backend/onyx/chat/llm_loop.py:1193:                    displayed_docs = tool_response.rich_response.displayed_docs
HEAD:backend/onyx/chat/llm_loop.py:1205:                    # only do this if the web search tool yielded results
HEAD:backend/onyx/chat/llm_loop.py:1227:                    tool_response.rich_response, FinalImageGenerationResponse
HEAD:backend/onyx/chat/llm_loop.py:1229:                    generated_images = tool_response.rich_response.generated_images
HEAD:backend/onyx/chat/llm_loop.py:1233:                if isinstance(tool_response.rich_response, PythonToolRichResponse):
HEAD:backend/onyx/chat/llm_loop.py:1235:                        tool_response.rich_response.generated_files or None
HEAD:backend/onyx/chat/llm_loop.py:1241:                    tool_response.rich_response, CustomToolCallSummary
HEAD:backend/onyx/chat/llm_loop.py:1243:                    tool_response.rich_response.tool_result, CustomToolUserFileSnapshot
HEAD:backend/onyx/chat/llm_loop.py:1246:                        tool_response.rich_response.tool_result.file_ids or None
HEAD:backend/onyx/chat/llm_loop.py:1250:                memory_snapshot: MemoryToolResponseSnapshot | None = None
HEAD:backend/onyx/chat/llm_loop.py:1252:                if isinstance(tool_response.rich_response, MemoryToolResponse):
HEAD:backend/onyx/chat/llm_loop.py:1264:                            if tool_response.rich_response.index_to_replace is not None:
HEAD:backend/onyx/chat/llm_loop.py:1267:                                    index=tool_response.rich_response.index_to_replace,
HEAD:backend/onyx/chat/llm_loop.py:1268:                                    new_text=tool_response.rich_response.memory_text,
HEAD:backend/onyx/chat/llm_loop.py:1273:                                    memory_text=tool_response.rich_response.memory_text,
HEAD:backend/onyx/chat/llm_loop.py:1277:                            if tool_response.rich_response.index_to_replace is not None
HEAD:backend/onyx/chat/llm_loop.py:1280:                        memory_snapshot = MemoryToolResponseSnapshot(
HEAD:backend/onyx/chat/llm_loop.py:1281:                            memory_text=tool_response.rich_response.memory_text,
HEAD:backend/onyx/chat/llm_loop.py:1284:                            index=tool_response.rich_response.index_to_replace,
HEAD:backend/onyx/chat/llm_loop.py:1290:                    tool_response.llm_facing_response = incognito_memory_refusal
HEAD:backend/onyx/chat/llm_loop.py:1293:                elif isinstance(tool_response.rich_response, CustomToolCallSummary):
HEAD:backend/onyx/chat/llm_loop.py:1295:                        tool_response.rich_response.model_dump()
HEAD:backend/onyx/chat/llm_loop.py:1297:                elif isinstance(tool_response.rich_response, str):
HEAD:backend/onyx/chat/llm_loop.py:1298:                    saved_response = tool_response.rich_response
HEAD:backend/onyx/chat/llm_loop.py:1300:                    saved_response = tool_response.llm_facing_response
HEAD:backend/onyx/chat/llm_loop.py:1309:                    reasoning_tokens=llm_step_result.reasoning,  # All tool calls from this loop share the same reasoning
HEAD:backend/onyx/chat/llm_loop.py:1321:                update_citation_processor_from_tool_response(
HEAD:backend/onyx/chat/llm_loop.py:1322:                    tool_response, citation_processor
HEAD:backend/onyx/chat/llm_loop.py:1329:            if tool_responses:
HEAD:backend/onyx/chat/llm_loop.py:1331:                valid_tool_responses = [
HEAD:backend/onyx/chat/llm_loop.py:1332:                    tr for tr in tool_responses if tr.tool_call is not None
HEAD:backend/onyx/chat/llm_loop.py:1337:                for tool_response in valid_tool_responses:
HEAD:backend/onyx/chat/llm_loop.py:1338:                    tc = tool_response.tool_call
HEAD:backend/onyx/chat/llm_loop.py:1358:                    message="",  # No text content when making tool calls
HEAD:backend/onyx/chat/llm_loop.py:1367:                for tool_response in valid_tool_responses:
HEAD:backend/onyx/chat/llm_loop.py:1368:                    tc = tool_response.tool_call
HEAD:backend/onyx/chat/llm_loop.py:1371:                    tool_response_message = tool_response.llm_facing_response
HEAD:backend/onyx/chat/llm_loop.py:1372:                    tool_response_token_count = token_counter(tool_response_message)
HEAD:backend/onyx/chat/llm_loop.py:1374:                    tool_response_msg = ChatMessageSimple(
HEAD:backend/onyx/chat/llm_loop.py:1375:                        message=tool_response_message,
HEAD:backend/onyx/chat/llm_loop.py:1376:                        token_count=tool_response_token_count,
HEAD:backend/onyx/chat/llm_loop.py:1381:                    simple_chat_history.append(tool_response_msg)
HEAD:backend/onyx/chat/llm_loop.py:1384:            if not llm_step_result.tool_calls or len(llm_step_result.tool_calls) == 0:
HEAD:backend/onyx/chat/llm_loop.py:1390:                for tool in llm_step_result.tool_calls
HEAD:backend/onyx/chat/llm_loop.py:1394:            if llm_step_result.tool_calls and any(
HEAD:backend/onyx/chat/llm_loop.py:1396:                for tool in llm_step_result.tool_calls
HEAD:backend/onyx/chat/llm_loop.py:1401:        if not llm_step_result.answer and not llm_step_result.tool_calls:
HEAD:backend/onyx/chat/llm_step.py:42:    ToolMessage,
HEAD:backend/onyx/chat/llm_step.py:291:        message_history, (SystemMessage, UserMessage, AssistantMessage, ToolMessage)
HEAD:backend/onyx/chat/llm_step.py:336:        elif isinstance(msg, ToolMessage):
HEAD:backend/onyx/chat/llm_step.py:725:def _build_structured_tool_response_message(msg: ChatMessageSimple) -> ToolMessage:
HEAD:backend/onyx/chat/llm_step.py:731:    return ToolMessage(
HEAD:backend/onyx/chat/llm_step.py:732:        role="tool",
HEAD:backend/onyx/chat/llm_step.py:742:    def format_tool_response_message(
HEAD:backend/onyx/chat/llm_step.py:744:    ) -> ToolMessage | UserMessage:
HEAD:backend/onyx/chat/llm_step.py:752:    def format_tool_response_message(self, msg: ChatMessageSimple) -> ToolMessage:
HEAD:backend/onyx/chat/llm_step.py:753:        return _build_structured_tool_response_message(msg)
HEAD:backend/onyx/chat/llm_step.py:778:    def format_tool_response_message(self, msg: ChatMessageSimple) -> UserMessage:
HEAD:backend/onyx/chat/llm_step.py:786:            content=f"[Tool Result] id={msg.tool_call_id}\n{msg.message}",
HEAD:backend/onyx/chat/llm_step.py:1014:            messages.append(history_message_formatter.format_tool_response_message(msg))
HEAD:backend/onyx/chat/llm_step.py:1071:    return bool(delta.content or delta.reasoning_content or delta.tool_calls)
HEAD:backend/onyx/chat/llm_step.py:1100:    answer content, tool calls, and citations. It yields Packet objects for
HEAD:backend/onyx/chat/llm_step.py:1124:        is_deep_research: If True, treat content before tool calls as reasoning
HEAD:backend/onyx/chat/llm_step.py:1182:    xml_tool_call_content_filter = _XmlToolCallContentFilter()
HEAD:backend/onyx/chat/llm_step.py:1255:            # When tool_choice is REQUIRED, content before tool calls is reasoning/thinking
HEAD:backend/onyx/chat/llm_step.py:1345:                    "LLM packet is empty (no content, reasoning, or tool calls). "
HEAD:backend/onyx/chat/llm_step.py:1393:                filtered_content = xml_tool_call_content_filter.process(delta.content)
HEAD:backend/onyx/chat/llm_step.py:1411:        filtered_content_tail = xml_tool_call_content_filter.flush()
HEAD:backend/onyx/chat/models.py:20:from onyx.tools.tool_implementations.custom.base_tool_types import ToolResultType
HEAD:backend/onyx/chat/models.py:33:class CustomToolResponse(BaseModel):
HEAD:backend/onyx/chat/models.py:34:    response: ToolResultType
HEAD:backend/onyx/chat/models.py:61:    tool_result: str
HEAD:backend/onyx/chat/process_message.py:226:    ``loaded_file.content`` only when a tool actually accesses it. Previously
HEAD:backend/onyx/chat/process_message.py:230:    receive zero-byte content for empty files, which PythonTool handles fine
HEAD:backend/onyx/chat/process_message.py:1023:        chat_history_result.all_injected_file_metadata if has_file_reader_tool else {}
HEAD:backend/onyx/chat/process_message.py:2254:            tool_result=tc.tool_call_response,
HEAD:backend/onyx/llm/models.py:233:class ToolMessage(CacheableMessage):
HEAD:backend/onyx/llm/models.py:240:ChatCompletionMessage = SystemMessage | UserMessage | AssistantMessage | ToolMessage
HEAD:backend/onyx/llm/multi_llm.py:272:    toolUse/toolResult content blocks. When no tools are provided for the
HEAD:backend/onyx/llm/multi_llm.py:297:                [existing_content] + tool_call_lines
HEAD:backend/onyx/llm/multi_llm.py:311:            tool_result_text = f"[Tool Result] id={tool_call_id}\n{content}"
HEAD:backend/onyx/llm/multi_llm.py:313:            # tool result to avoid consecutive user messages (Bedrock requires
HEAD:backend/onyx/llm/multi_llm.py:318:                and "[Tool Result]" in result[-1].get("content", "")
HEAD:backend/onyx/llm/multi_llm.py:320:                result[-1]["content"] += "\n\n" + tool_result_text
HEAD:backend/onyx/llm/multi_llm.py:322:                result.append({"role": "user", "content": tool_result_text})
HEAD:backend/onyx/llm/multi_llm.py:1003:            # contain toolUse/toolResult content blocks. When no tools are
HEAD:backend/onyx/llm/tracing_wrap.py:170:    Accumulates content, final usage, and tool-call deltas across yielded
HEAD:backend/onyx/llm/tracing_wrap.py:260:    result is a dict of complete ``ChatCompletionDeltaToolCall`` objects
HEAD:backend/onyx/tools/constants.py:3:# Tool names as referenced by tool results / tool calls
HEAD:backend/onyx/tools/constants.py:20:# Tool names as referenced by tool results / tool calls (read_file)
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:18:from onyx.coding_agent.models import CodingAgentCallResult, CodingAgentSpecialToolCalls
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:22:    THINK_TOOL_RESPONSE_MESSAGE,
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:23:    THINK_TOOL_RESPONSE_TOKEN_COUNT,
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:397:                    tool_calls = llm_step_result.tool_calls or []
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:431:                                message=THINK_TOOL_RESPONSE_MESSAGE,
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:432:                                token_count=THINK_TOOL_RESPONSE_TOKEN_COUNT,
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:477:                        tool_response = _run_bash_call(bash_tool, tc)
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:480:                                message=tool_response,
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:481:                                token_count=token_counter(tool_response),
HEAD:backend/onyx/tools/fake_tools/research_agent.py:15:    update_citation_processor_from_tool_response,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:20:from onyx.chat.models import ChatMessageSimple, LlmStepResult, ToolCallSimple
HEAD:backend/onyx/tools/fake_tools/research_agent.py:27:    THINK_TOOL_RESPONSE_MESSAGE,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:28:    THINK_TOOL_RESPONSE_TOKEN_COUNT,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:70:from onyx.tools.models import ToolCallInfo, ToolCallKickoff, ToolResponse
HEAD:backend/onyx/tools/fake_tools/research_agent.py:396:                tool_responses: list[ToolResponse] = []
HEAD:backend/onyx/tools/fake_tools/research_agent.py:397:                tool_calls = llm_step_result.tool_calls or []
HEAD:backend/onyx/tools/fake_tools/research_agent.py:458:                        think_tool_response_msg = ChatMessageSimple(
HEAD:backend/onyx/tools/fake_tools/research_agent.py:459:                            message=THINK_TOOL_RESPONSE_MESSAGE,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:460:                            token_count=THINK_TOOL_RESPONSE_TOKEN_COUNT,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:465:                        msg_history.append(think_tool_response_msg)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:466:                        think_span.span_data.output = THINK_TOOL_RESPONSE_MESSAGE
HEAD:backend/onyx/tools/fake_tools/research_agent.py:471:                    parallel_tool_call_results = run_tool_calls(
HEAD:backend/onyx/tools/fake_tools/research_agent.py:493:                    tool_responses = parallel_tool_call_results.tool_responses
HEAD:backend/onyx/tools/fake_tools/research_agent.py:495:                        parallel_tool_call_results.updated_citation_mapping
HEAD:backend/onyx/tools/fake_tools/research_agent.py:498:                    if tool_calls and not tool_responses:
HEAD:backend/onyx/tools/fake_tools/research_agent.py:510:                    valid_tool_responses = [
HEAD:backend/onyx/tools/fake_tools/research_agent.py:511:                        tr for tr in tool_responses if tr.tool_call is not None
HEAD:backend/onyx/tools/fake_tools/research_agent.py:515:                    if valid_tool_responses:
HEAD:backend/onyx/tools/fake_tools/research_agent.py:517:                        for tool_response in valid_tool_responses:
HEAD:backend/onyx/tools/fake_tools/research_agent.py:518:                            tc = tool_response.tool_call
HEAD:backend/onyx/tools/fake_tools/research_agent.py:544:                    for tool_response in valid_tool_responses:
HEAD:backend/onyx/tools/fake_tools/research_agent.py:545:                        tc = tool_response.tool_call
HEAD:backend/onyx/tools/fake_tools/research_agent.py:557:                        if isinstance(tool_response.rich_response, SearchDocsResponse):
HEAD:backend/onyx/tools/fake_tools/research_agent.py:558:                            search_docs = tool_response.rich_response.search_docs
HEAD:backend/onyx/tools/fake_tools/research_agent.py:559:                            displayed_docs = tool_response.rich_response.displayed_docs
HEAD:backend/onyx/tools/fake_tools/research_agent.py:566:                            # only do this if the web search tool yielded results
HEAD:backend/onyx/tools/fake_tools/research_agent.py:572:                        update_citation_processor_from_tool_response(
HEAD:backend/onyx/tools/fake_tools/research_agent.py:573:                            tool_response=tool_response,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:592:                            tool_call_response=tool_response.llm_facing_response,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:598:                        tool_response_message = tool_response.llm_facing_response
HEAD:backend/onyx/tools/fake_tools/research_agent.py:599:                        tool_response_token_count = token_counter(tool_response_message)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:601:                        tool_response_msg = ChatMessageSimple(
HEAD:backend/onyx/tools/fake_tools/research_agent.py:602:                            message=tool_response_message,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:603:                            token_count=tool_response_token_count,
HEAD:backend/onyx/tools/fake_tools/research_agent.py:608:                        msg_history.append(tool_response_msg)
HEAD:backend/onyx/tools/interface.py:10:from onyx.tools.models import ToolResponse
HEAD:backend/onyx/tools/interface.py:90:    ) -> ToolResponse:
HEAD:backend/onyx/tools/models.py:25:from onyx.tools.tool_implementations.memory.models import MemoryToolResponse
HEAD:backend/onyx/tools/models.py:64:    tool_result: Any  # The response data
HEAD:backend/onyx/tools/models.py:84:class ToolResponse(BaseModel):
HEAD:backend/onyx/tools/models.py:93:        | MemoryToolResponse
HEAD:backend/onyx/tools/models.py:96:        # This comes from custom tools, tool result needs to be saved
HEAD:backend/onyx/tools/models.py:113:    tool_responses: list[ToolResponse]
HEAD:backend/onyx/tools/models.py:119:    tool_response: ToolResponse | None = None
HEAD:backend/onyx/tools/models.py:124:        fields = ["tool_response", "tool_message_content", "tool_run_kickoff"]
HEAD:backend/onyx/tools/models.py:133:                "Exactly one of 'tool_response', 'tool_message_content', or 'tool_run_kickoff' must be provided"
HEAD:backend/onyx/tools/models.py:139:class ToolCallFinalResult(ToolCallKickoff):
HEAD:backend/onyx/tools/models.py:140:    tool_result: Any = (
HEAD:backend/onyx/tools/models.py:258:class MemoryToolResponseSnapshot(BaseModel):
HEAD:backend/onyx/tools/models.py:291:class BaseCiteableToolResult(BaseModel):
HEAD:backend/onyx/tools/models.py:292:    """Base class for tool results that can be cited."""
HEAD:backend/onyx/tools/models.py:299:class LlmInternalSearchResult(BaseCiteableToolResult):
HEAD:backend/onyx/tools/models.py:308:class LlmWebSearchResult(BaseCiteableToolResult):
HEAD:backend/onyx/tools/models.py:317:class LlmOpenUrlResult(BaseCiteableToolResult):
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:21:from onyx.tools.models import ToolCallException, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:134:    ) -> ToolResponse:
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:193:            return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:225:        return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:19:from onyx.tools.models import ToolCallException, ToolCallKickoff, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:125:    ) -> ToolResponse:
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:183:            return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:188:        return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/custom/base_tool_types.py:2:ToolResultType = dict | list | str | int | float | bool
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:32:    ToolResponse,
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:46:CUSTOM_TOOL_RESPONSE_ID = "custom_tool_response"
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:154:    ) -> ToolResponse:
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:213:        tool_result: Any
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:222:            tool_result = CustomToolUserFileSnapshot(file_ids=file_ids)
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:229:            tool_result = CustomToolUserFileSnapshot(file_ids=file_ids)
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:234:                tool_result = response.json()
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:236:                data = tool_result
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:241:                tool_result = response.text
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:243:                data = tool_result
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:264:        llm_facing_response = json.dumps(tool_result)
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:266:        return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:270:                tool_result=tool_result,
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:22:from onyx.tools.models import ToolCallException, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:152:    ) -> ToolResponse:
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:255:        return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:37:from onyx.tools.models import ToolCallException, ToolExecutionException, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:309:    ) -> ToolResponse:
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:429:        return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/knowledge_graph/knowledge_graph_tool.py:9:from onyx.tools.models import ToolResponse
HEAD:backend/onyx/tools/tool_implementations/knowledge_graph/knowledge_graph_tool.py:80:    ) -> ToolResponse:
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:30:from onyx.tools.models import CustomToolCallSummary, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:53:#     tool_result: Any
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:149:    ) -> ToolResponse:
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:211:                return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:215:                        tool_result=error_result,
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:250:            tool_result = call_mcp_tool(
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:261:            # Format the tool result for response
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:262:            tool_result_dict = {"tool_result": tool_result}
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:263:            llm_facing_response = json.dumps(tool_result_dict)
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:272:                        data=tool_result_dict,
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:277:            response = ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:281:                    tool_result=tool_result_dict,
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:305:                error_result = {"error": f"Tool execution failed: {str(e)}"}
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:321:            return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:325:                    tool_result=error_result,
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:25:from onyx.tools.models import ChatMinimalTextMessage, ToolCallException, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:26:from onyx.tools.tool_implementations.memory.models import MemoryToolResponse
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:112:    ) -> ToolResponse:
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:156:        return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:157:            rich_response=MemoryToolResponse(
HEAD:backend/onyx/tools/tool_implementations/memory/models.py:4:class MemoryToolResponse(BaseModel):
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:35:from onyx.tools.models import OpenURLToolOverrideKwargs, ToolCallException, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:533:    ) -> ToolResponse:
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:543:                ToolResponse containing the fetched content and citation mapping.
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:589:                    return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:615:                    return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:687:                    return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:717:            return ToolResponse(rich_response=None, llm_facing_response=failure_msg)
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:745:        return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:38:    ToolResponse,
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:354:    ) -> ToolResponse:
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:364:            ToolResponse with execution results
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:549:                return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:586:                return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:32:We construct a response string back to the LLM as the result of the tool call. We also pass relevant richer objects back
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:114:    ToolResponse,
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:669:    ) -> ToolResponse:
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:1053:            logger.info("Search tool - no results found, returning empty response")
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:1058:            return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:1222:        return ToolResponse(
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:22:    ToolResponse,
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:205:    ) -> ToolResponse:
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:353:        return ToolResponse(
HEAD:backend/onyx/tools/tool_runner.py:26:    ToolResponse,
HEAD:backend/onyx/tools/tool_runner.py:122:) -> ToolResponse:
HEAD:backend/onyx/tools/tool_runner.py:136:    tool_response: ToolResponse | None = None
HEAD:backend/onyx/tools/tool_runner.py:141:            tool_response = tool.run(
HEAD:backend/onyx/tools/tool_runner.py:146:            span_fn.span_data.output = tool_response.llm_facing_response
HEAD:backend/onyx/tools/tool_runner.py:151:            tool_response = ToolResponse(
HEAD:backend/onyx/tools/tool_runner.py:174:            tool_response = ToolResponse(
HEAD:backend/onyx/tools/tool_runner.py:201:            tool_response = ToolResponse(
HEAD:backend/onyx/tools/tool_runner.py:228:    tool_response.tool_call = tool_call
HEAD:backend/onyx/tools/tool_runner.py:229:    return tool_response
HEAD:backend/onyx/tools/tool_runner.py:248:    # A map of url -> summary for passing web results to open url tool
HEAD:backend/onyx/tools/tool_runner.py:286:        - `tool_responses`: `ToolResponse` objects for successfully dispatched tool calls
HEAD:backend/onyx/tools/tool_runner.py:298:            tool_responses=[],
HEAD:backend/onyx/tools/tool_runner.py:316:                tool_responses=[],
HEAD:backend/onyx/tools/tool_runner.py:431:    tool_run_results: list[ToolResponse | None] = run_functions_tuples_in_parallel(
HEAD:backend/onyx/tools/tool_runner.py:439:    for result in tool_run_results:
HEAD:backend/onyx/tools/tool_runner.py:449:    tool_responses = [result for result in tool_run_results if result is not None]
HEAD:backend/onyx/tools/tool_runner.py:451:        tool_responses=tool_responses,
```
Tool results can themselves contain untrusted external content and may
influence subsequent model decisions.
## Multi-Step Agent / Loop Controls
Evidence lines: 466
```text
HEAD:backend/ee/onyx/db/external_perm.py:77:    # external API calls (e.g. Google Drive folder iteration). Without this,
HEAD:backend/ee/onyx/db/usage_export.py:131:        # Update initial_time for the next iteration
HEAD:backend/ee/onyx/external_permissions/box/access.py:27:_MAX_PAGINATION_ITERATIONS = 10_000
HEAD:backend/ee/onyx/external_permissions/box/access.py:156:    for _ in range(_MAX_PAGINATION_ITERATIONS):
HEAD:backend/ee/onyx/server/gateway/api.py:277:                f"{', '.join(option.value for option in ToolChoiceOptions)}.",
HEAD:backend/ee/onyx/server/gateway/api.py:535:        for item in (_function_call_item(tc) for tc in tool_calls or [])
HEAD:backend/ee/onyx/server/gateway/api.py:687:                        for tool_call in _finalize_tool_calls(state.tool_call_buffer)
HEAD:backend/ee/onyx/server/gateway/api.py:692:                for tool_index, call_item in enumerate(
HEAD:backend/ee/onyx/server/gateway/api.py:887:                for part in tool_result_content
HEAD:backend/ee/onyx/server/gateway/api.py:926:    for tool in raw_tools:
HEAD:backend/ee/onyx/server/gateway/api.py:974:        for tool in tools or []
HEAD:backend/ee/onyx/server/gateway/api.py:1011:_ANTHROPIC_STOP_REASONS = {
HEAD:backend/ee/onyx/server/gateway/api.py:1019:def _anthropic_stop_reason(finish_reason: str | None, has_tool_use: bool) -> str:
HEAD:backend/ee/onyx/server/gateway/api.py:1020:    mapped = _ANTHROPIC_STOP_REASONS.get(finish_reason or "", "end_turn")
HEAD:backend/ee/onyx/server/gateway/api.py:1059:    for tool_call in tool_calls or []:
HEAD:backend/ee/onyx/server/gateway/api.py:1101:                stop_reason=None,
HEAD:backend/ee/onyx/server/gateway/api.py:1246:                    tc for tc in finalized_tool_calls or [] if tc.function.name
HEAD:backend/ee/onyx/server/gateway/api.py:1248:                for tool_index, (tool_block, tool_call) in enumerate(
HEAD:backend/ee/onyx/server/gateway/api.py:1271:                            stop_reason=_anthropic_stop_reason(
HEAD:backend/ee/onyx/server/gateway/api.py:1381:        stop_reason=_anthropic_stop_reason(
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:126:    for tool in body.get("tools") or []:
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:72:        for delta_tc in chunk.choice.delta.tool_calls:
HEAD:backend/ee/onyx/server/log_export/api.py:287:        # runs if the generator is closed before its first iteration. Double
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:7:For the Search API that runs the full SearchTool.run() pipeline (the same
HEAD:backend/ee/onyx/server/seeding.py:81:        for tool in tools:
HEAD:backend/ee/onyx/server/seeding.py:103:                    "Definition file not found for tool %s: %s",
HEAD:backend/ee/onyx/server/seeding.py:109:                    "Invalid JSON in definition file for tool %s: %s", tool.name, str(e)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:267:    Handles each step independently to ensure maximum cleanup even if some steps fail.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:589:                # "No heartbeat received" failure. Checked every loop iteration
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:322:    # Persist plaintext for fast FileReaderTool loads (no DB session needed)
HEAD:backend/onyx/background/indexing/run_docfetching.py:245:    iteration of the docfetching loop body".
HEAD:backend/onyx/background/indexing/run_docfetching.py:258:            except StopIteration:
HEAD:backend/onyx/background/indexing/run_docfetching.py:262:                # terminal error iteration isn't lost from the metric.
HEAD:backend/onyx/chat/COMPRESSION.md:25:- `reserved_tokens` — space for system prompt, tools, files, etc.
HEAD:backend/onyx/chat/README.md:3:This document reviews some design decisions around the main agent-loop powering Onyx's chat flow.
HEAD:backend/onyx/chat/README.md:50:make the context clearer to the LLM. Note that for search results (whether web or internal, it will just be the json) and it will be a Tool Call type of
HEAD:backend/onyx/chat/README.md:98:TC -> Agent Message for a tool call
HEAD:backend/onyx/chat/README.md:136:are orthogonal (or even possibly contradictory) to the system prompt. For weaker models, it causes strange artifacts in tool calls and final responses
HEAD:backend/onyx/chat/README.md:218:partial state for every model, yields an `OverallStop(stop_reason="user_cancelled")` packet, and returns.
HEAD:backend/onyx/chat/README.md:238:tool calls and returns that to the LLM Loop to execute.
HEAD:backend/onyx/chat/README.md:243:  concept of a turn. The turn_index for the frontend is which block does this packet belong to. So while a reasoning + tool call
HEAD:backend/onyx/chat/chat_state.py:62:        # Search doc collection - maps dedup key to SearchDoc for all docs from tool calls
HEAD:backend/onyx/chat/chat_state.py:113:        """Thread-safe getter for tool_calls (returns a copy)."""
HEAD:backend/onyx/chat/chat_state.py:187:    """Separated file IDs for the FileReaderTool so it knows which loader to use."""
HEAD:backend/onyx/chat/chat_utils.py:734:    For assistant messages with tool calls: creates ONE ASSISTANT message with tool_calls array,
HEAD:backend/onyx/chat/chat_utils.py:736:    For assistant messages without tool calls: creates a simple ASSISTANT message
HEAD:backend/onyx/chat/chat_utils.py:830:            # 2. For each turn: ONE ASSISTANT message with tool_calls array
HEAD:backend/onyx/chat/chat_utils.py:835:                for tool_call in chat_message.tool_calls:
HEAD:backend/onyx/chat/chat_utils.py:841:                for turn_number in sorted(tool_calls_by_turn.keys()):
HEAD:backend/onyx/chat/chat_utils.py:848:                    for tool_call in turn_tool_calls:
HEAD:backend/onyx/chat/chat_utils.py:863:                        tc.token_count for tc in tool_calls_simple
HEAD:backend/onyx/chat/chat_utils.py:875:                    # Add TOOL_CALL_RESPONSE messages for each tool call in this turn
HEAD:backend/onyx/chat/chat_utils.py:876:                    for tool_call in turn_tool_calls:
HEAD:backend/onyx/chat/chat_utils.py:969:    """Create ChatMessageSimple objects for failed tool calls.
HEAD:backend/onyx/chat/chat_utils.py:973:    2. A TOOL_CALL_RESPONSE failure message for each tool call
HEAD:backend/onyx/chat/chat_utils.py:981:        followed by a failure response for each tool call
HEAD:backend/onyx/chat/chat_utils.py:986:    # Create ToolCallSimple for each failed tool call
HEAD:backend/onyx/chat/chat_utils.py:988:    for tool_call in tool_calls:
HEAD:backend/onyx/chat/chat_utils.py:999:    total_token_count = sum(tc.token_count for tc in tool_calls_simple)
HEAD:backend/onyx/chat/chat_utils.py:1012:    # Create a TOOL_CALL_RESPONSE failure message for each tool call
HEAD:backend/onyx/chat/chat_utils.py:1013:    for tool_call in tool_calls:
HEAD:backend/onyx/chat/compression.py:83:        for tool_call in m.tool_calls or []:
HEAD:backend/onyx/chat/compression.py:99:        reserved_tokens: Tokens reserved for system prompt, tools, files, etc.
HEAD:backend/onyx/chat/compression.py:283:                    tool_id_to_name.get(tc.tool_id, "unknown") for tc in msg.tool_calls
HEAD:backend/onyx/chat/compression.py:446:                    tool.id: tool.name for tool in all_tools
HEAD:backend/onyx/chat/emitter.py:9:    """Routes packets from LLM/tool execution to the ``_run_models`` drain loop.
HEAD:backend/onyx/chat/incognito.py:233:    type survive for the file-reader tool and teardown. The content-derived
HEAD:backend/onyx/chat/llm_loop.py:357:    """Build messages for context-injected / tool-backed files.
HEAD:backend/onyx/chat/llm_loop.py:553:    # dropped AND we have metadata for them (meaning the FileReaderTool is
HEAD:backend/onyx/chat/llm_loop.py:635:            for tool_call in msg.tool_calls:
HEAD:backend/onyx/chat/llm_loop.py:839:        has_open_url_tool: bool = any(isinstance(tool, OpenURLTool) for tool in tools)
HEAD:backend/onyx/chat/llm_loop.py:886:                final_tools = [tool for tool in tools if tool.id == forced_tool_id]
HEAD:backend/onyx/chat/llm_loop.py:1050:            tool_defs = [tool.tool_definition() for tool in final_tools]
HEAD:backend/onyx/chat/llm_loop.py:1077:            # Fallback extraction for LLMs that don't support tool calling natively or are lower quality
HEAD:backend/onyx/chat/llm_loop.py:1099:                for tool_call in tool_calls:
HEAD:backend/onyx/chat/llm_loop.py:1153:            for tool_response in tool_responses:
HEAD:backend/onyx/chat/llm_loop.py:1177:                tools_by_name = {tool.name: tool for tool in final_tools}
HEAD:backend/onyx/chat/llm_loop.py:1309:                    reasoning_tokens=llm_step_result.reasoning,  # All tool calls from this loop share the same reasoning
HEAD:backend/onyx/chat/llm_loop.py:1332:                    tr for tr in tool_responses if tr.tool_call is not None
HEAD:backend/onyx/chat/llm_loop.py:1335:                # Build ToolCallSimple list for all tool calls in this turn
HEAD:backend/onyx/chat/llm_loop.py:1337:                for tool_response in valid_tool_responses:
HEAD:backend/onyx/chat/llm_loop.py:1356:                total_tool_call_tokens = sum(tc.token_count for tc in tool_calls_simple)
HEAD:backend/onyx/chat/llm_loop.py:1366:                # Add TOOL_CALL_RESPONSE messages for each tool call
HEAD:backend/onyx/chat/llm_loop.py:1367:                for tool_response in valid_tool_responses:
HEAD:backend/onyx/chat/llm_loop.py:1390:                for tool in llm_step_result.tool_calls
HEAD:backend/onyx/chat/llm_loop.py:1396:                for tool in llm_step_result.tool_calls
HEAD:backend/onyx/chat/llm_step.py:281:    """Format message history for logging, with special handling for tool calls.
HEAD:backend/onyx/chat/llm_step.py:324:                for tool_call in msg.tool_calls:
HEAD:backend/onyx/chat/llm_step.py:391:    Returns a list of ToolCallKickoff objects for valid tool calls (those with both id and name).
HEAD:backend/onyx/chat/llm_step.py:396:        turn_index: The turn index for this set of tool calls
HEAD:backend/onyx/chat/llm_step.py:397:        tab_index: If provided, use this tab_index for all tool calls (otherwise auto-increment)
HEAD:backend/onyx/chat/llm_step.py:398:        sub_turn_index: The sub-turn index for nested tool calls
HEAD:backend/onyx/chat/llm_step.py:403:    for tool_call_data in id_to_tool_call_map.values():
HEAD:backend/onyx/chat/llm_step.py:432:    This is a fallback mechanism for when the LLM was expected to return tool calls
HEAD:backend/onyx/chat/llm_step.py:433:    but didn't use the proper tool call format. It searches for tool calls embedded
HEAD:backend/onyx/chat/llm_step.py:438:        response_text: The LLM's text response to search for tool calls
HEAD:backend/onyx/chat/llm_step.py:440:        placement: Placement information for the tool calls
HEAD:backend/onyx/chat/llm_step.py:443:        List of ToolCallKickoff objects for any matched tool calls
HEAD:backend/onyx/chat/llm_step.py:450:    for tool_def in tool_definitions:
HEAD:backend/onyx/chat/llm_step.py:499:    for tab_index, (tool_name, tool_args) in enumerate(matched_tool_calls):
HEAD:backend/onyx/chat/llm_step.py:640:    for tool_name in tool_name_to_def:
HEAD:backend/onyx/chat/llm_step.py:647:    for tool_name, func_def in tool_name_to_def.items():
HEAD:backend/onyx/chat/llm_step.py:696:    for tool_name in tool_name_to_def:
HEAD:backend/onyx/chat/llm_step.py:715:            for tc in msg.tool_calls
HEAD:backend/onyx/chat/llm_step.py:765:            for tc in msg.tool_calls
HEAD:backend/onyx/chat/llm_step.py:1135:            - ToolCallKickoff for tool calls (extracted at the end)
HEAD:backend/onyx/chat/llm_step.py:1274:            # Normal flow for AUTO or NONE tool choice
HEAD:backend/onyx/chat/llm_step.py:1400:                for tool_call_delta in delta.tool_calls:
HEAD:backend/onyx/chat/llm_step.py:1428:                for tool_call_delta in flush_delta.tool_calls:
HEAD:backend/onyx/chat/llm_step.py:1457:        # misleading EmptyLLMResponseError downstream. Skipped for REQUIRED tool
HEAD:backend/onyx/chat/llm_step.py:1459:        # Also skipped when the raw output is XML tool-call markup: run_llm_loop's
HEAD:backend/onyx/chat/llm_step.py:1511:                for kickoff in tool_calls
HEAD:backend/onyx/chat/llm_step.py:1541:                for tc in tool_calls
HEAD:backend/onyx/chat/llm_step.py:1624:        except StopIteration as e:
HEAD:backend/onyx/chat/models.py:169:    # Only for TOOL_CALL_RESPONSE type messages
HEAD:backend/onyx/chat/models.py:171:    # For ASSISTANT messages with tool calls (OpenAI parallel tool calling format)
HEAD:backend/onyx/chat/models.py:193:    """Lightweight metadata for exposing files to the FileReaderTool.
HEAD:backend/onyx/chat/models.py:226:    # Lightweight metadata for files exposed via FileReaderTool
HEAD:backend/onyx/chat/models.py:246:    # Used for fallback tool-call extraction when providers emit calls as text.
HEAD:backend/onyx/chat/process_message.py:223:    """Convert ChatLoadedFile objects to ChatFile for tool usage (e.g., PythonTool).
HEAD:backend/onyx/chat/process_message.py:230:    receive zero-byte content for empty files, which PythonTool handles fine
HEAD:backend/onyx/chat/process_message.py:269:    file into RAM for chats that never invoke the Python tool.
HEAD:backend/onyx/chat/process_message.py:814:    # Collect file IDs for the file reader tool *before* summary truncation so
HEAD:backend/onyx/chat/process_message.py:854:    # This prompt may come from the Agent or Project. Fetched here (before run_llm_loop)
HEAD:backend/onyx/chat/process_message.py:910:    # Also grant access to persona-attached user files for FileReaderTool
HEAD:backend/onyx/chat/process_message.py:918:    tool_id_to_name_map = {tool.id: tool.name for tool in all_tools}
HEAD:backend/onyx/chat/process_message.py:921:        (tool.id for tool in all_tools if tool.in_code_tool_id == SEARCH_TOOL_ID), None
HEAD:backend/onyx/chat/process_message.py:936:    if forced_tool_id in {tool.id for tool in all_tools if not tool.enabled}:
HEAD:backend/onyx/chat/process_message.py:942:    # Convert loaded files to ChatFile format for tools like PythonTool
HEAD:backend/onyx/chat/process_message.py:947:            {chat_file.filename for chat_file in chat_files_for_tools},
HEAD:backend/onyx/chat/process_message.py:983:    # and is easy to parse for the agent loop.
HEAD:backend/onyx/chat/process_message.py:985:        tool.in_code_tool_id == FILE_READER_TOOL_ID for tool in persona.tools
HEAD:backend/onyx/chat/process_message.py:1187:        ``OverallStop(stop_reason="user_cancelled")`` if the connection drops).
HEAD:backend/onyx/chat/process_message.py:1367:                tool for tool_list in thread_tool_dict.values() for tool in tool_list
HEAD:backend/onyx/chat/process_message.py:1371:                tool.id for tool in model_tools
HEAD:backend/onyx/chat/process_message.py:1525:                                    type="stop", stop_reason="user_cancelled"
HEAD:backend/onyx/chat/process_message.py:1673:        custom_tool_additional_headers: Extra headers for custom tool HTTP calls.
HEAD:backend/onyx/chat/process_message.py:1674:        mcp_headers: Extra headers for MCP tool calls.
HEAD:backend/onyx/chat/process_message.py:1745:                    except StopIteration as build_done:
HEAD:backend/onyx/chat/process_message.py:1771:            # Set for the whole turn so a blob any tool saves carries the
HEAD:backend/onyx/chat/process_message.py:1946:        custom_tool_additional_headers: Extra headers for custom tool HTTP calls.
HEAD:backend/onyx/chat/process_message.py:1947:        mcp_headers: Extra headers for MCP tool calls.
HEAD:backend/onyx/chat/process_message.py:2259:        for tc in state_container.get_tool_calls()
HEAD:backend/onyx/chat/prompt_utils.py:297:        has_web_search = any(isinstance(tool, WebSearchTool) for tool in tools)
HEAD:backend/onyx/chat/prompt_utils.py:298:        has_internal_search = any(isinstance(tool, SearchTool) for tool in tools)
HEAD:backend/onyx/chat/prompt_utils.py:299:        has_open_urls = any(isinstance(tool, OpenURLTool) for tool in tools)
HEAD:backend/onyx/chat/prompt_utils.py:300:        has_python = any(isinstance(tool, PythonTool) for tool in tools)
HEAD:backend/onyx/chat/prompt_utils.py:302:            isinstance(tool, ImageGenerationTool) for tool in tools
HEAD:backend/onyx/chat/prompt_utils.py:304:        has_memory = any(isinstance(tool, MemoryTool) for tool in tools)
HEAD:backend/onyx/chat/prompt_utils.py:319:                    (t for t in tools if isinstance(t, WebSearchTool)), None
HEAD:backend/onyx/chat/save_chat.py:33:    for tool_call_info in tool_calls:
HEAD:backend/onyx/chat/save_chat.py:36:        for gen_file in tool_call_info.generated_files:
HEAD:backend/onyx/chat/save_chat.py:81:    for tool_call_info in tool_calls:
HEAD:backend/onyx/chat/save_chat.py:116:                [img.model_dump() for img in tool_call_info.generated_images]
HEAD:backend/onyx/chat/save_chat.py:131:    for tool_call_obj in tool_call_objects:
HEAD:backend/onyx/chat/save_chat.py:134:    # Update parent_tool_call_id for all tool calls
HEAD:backend/onyx/chat/save_chat.py:138:    for tool_call_obj in tool_call_objects:
HEAD:backend/onyx/chat/save_chat.py:159:    for tool_call_obj in valid_tool_calls:
HEAD:backend/onyx/chat/save_chat.py:254:    # 3. Build tool_call -> search_doc mapping (for displayed docs in each tool call)
HEAD:backend/onyx/chat/save_chat.py:256:    for tool_call_info in tool_calls:
HEAD:backend/onyx/chat/save_chat.py:259:            for search_doc_py in tool_call_info.search_docs:
HEAD:backend/onyx/chat/tool_call_args_streaming.py:16:    """Look up the Tool subclass for a streaming tool call delta."""
HEAD:backend/onyx/configs/constants.py:389:    ASSISTANT = "assistant"  # AIMessage - Can include tool_calls field for parallel tool calling
HEAD:backend/onyx/connectors/box/connector.py:72:_MAX_PAGINATION_ITERATIONS = 10_000
HEAD:backend/onyx/connectors/box/connector.py:205:    for _ in range(_MAX_PAGINATION_ITERATIONS):
HEAD:backend/onyx/connectors/box/connector.py:739:            except StopIteration as e:
HEAD:backend/onyx/connectors/box/connector.py:781:                except StopIteration as e:
HEAD:backend/onyx/connectors/discord/connector.py:251:                except StopAsyncIteration:
HEAD:backend/onyx/connectors/github/connector.py:222:            # is updated during iteration over pag_list.
HEAD:backend/onyx/connectors/gong/connector.py:620:            # has_more is recomputed by the workspace iteration that follows;
HEAD:backend/onyx/connectors/gong/connector.py:649:        except StopIteration as e:
HEAD:backend/onyx/connectors/google_drive/connector.py:2379:    num_iterations = 0
HEAD:backend/onyx/connectors/google_drive/connector.py:2394:        num_iterations += 1
HEAD:backend/onyx/connectors/google_drive/connector.py:2395:        if num_iterations > 100_000:
HEAD:backend/onyx/connectors/google_drive/connector.py:2396:            raise RuntimeError("Too many iterations. Infinite loop?")
HEAD:backend/onyx/connectors/interfaces.py:293:        except StopIteration as e:
HEAD:backend/onyx/connectors/sharepoint/connector.py:1397:        fallback if expansion 400s on a corrupt page. Mirrors a single iteration
HEAD:backend/onyx/connectors/sharepoint/connector.py:2245:            # Outer try catches BFS-generator failures mid-iteration;
HEAD:backend/onyx/connectors/sharepoint/connector.py:2260:                    "Failed mid-iteration for drive '%s' in site '%s'",
HEAD:backend/onyx/connectors/slack/connector.py:1594:    except StopIteration as e:
HEAD:backend/onyx/db/engine/tenant_utils.py:49:    acquires locks sequentially, one schema per iteration.
HEAD:backend/onyx/db/llm.py:367:    # Build a lookup of existing model configurations by name (single iteration)
HEAD:backend/onyx/db/mcp.py:95:    for tool in persona.tools:
HEAD:backend/onyx/db/mcp.py:159:    after this server changes (enabled/disabled for craft, tools toggled, URL
HEAD:backend/onyx/db/models.py:843:    For example, a persona may have the image generation tool attached to it, even though
HEAD:backend/onyx/db/models.py:3437:    # Index order of tool calls from the LLM for parallel tool calls
HEAD:backend/onyx/db/models.py:3446:    # Preceeding reasoning tokens for this tool call, not included in the history
HEAD:backend/onyx/db/models.py:3456:    # For image generation tool - stores GeneratedImage objects for replay
HEAD:backend/onyx/db/models.py:4022:    # ID of the tool in the codebase, only applies for in-code tools.
HEAD:backend/onyx/db/models.py:4027:    # OpenAPI scheme for the tool. Only applies to tools defined via the UI.
HEAD:backend/onyx/db/models.py:4038:    # user who created / owns the tool. Will be None for built-in tools.
HEAD:backend/onyx/db/models.py:4044:    # MCP server this tool is associated with (null for non-MCP tools)
HEAD:backend/onyx/db/models.py:4048:    # OAuth configuration for this tool (null for tools without OAuth)
HEAD:backend/onyx/db/oauth_config.py:107:    Sets oauth_config_id to NULL for associated tools due to SET NULL foreign key.
HEAD:backend/onyx/db/persona.py:1634:                {tool.id for tool in existing_persona.tools}
HEAD:backend/onyx/db/persona.py:1639:            for tool in tools:
HEAD:backend/onyx/db/persona.py:1948:    for tool in tools:
HEAD:backend/onyx/db/persona.py:2092:    return any(tool.in_code_tool_id == "run_search" for tool in persona.tools)
HEAD:backend/onyx/db/persona.py:2143:        for tool_id in tool_ids:
HEAD:backend/onyx/db/tools.py:124:    """The gate for every per-tool action (edit, delete, toggle, OAuth config). An MCP tool
HEAD:backend/onyx/db/tools.py:195:    return {tool_id for (tool_id,) in rows}
HEAD:backend/onyx/db/tools.py:324:            for in_code_tool_id, tool_cls in BUILT_IN_TOOL_MAP.items()
HEAD:backend/onyx/db/tools.py:368:        turn_number: The turn number for this tool call
HEAD:backend/onyx/db/tools.py:375:        parent_tool_call_id: Optional parent tool call ID (for nested tool calls)
HEAD:backend/onyx/db/tools.py:378:        tab_index: Index order of tool calls from the LLM for parallel tool calls
HEAD:backend/onyx/deep_research/dr_loop.py:241:        # Track processing start time for tool duration calculation
HEAD:backend/onyx/deep_research/dr_loop.py:256:        allowed_tools = [tool for tool in tools if tool.name in allowed_tool_names]
HEAD:backend/onyx/deep_research/dr_loop.py:396:                except StopIteration as e:
HEAD:backend/onyx/deep_research/dr_loop.py:556:                    # Even for the reasoning tool, this should be plenty
HEAD:backend/onyx/deep_research/dr_loop.py:661:                    for tool_call in tool_calls:
HEAD:backend/onyx/deep_research/dr_loop.py:716:                            tool_call.tool_call_id for tool_call in tool_calls
HEAD:backend/onyx/deep_research/dr_loop.py:739:                    for current_tool_call in research_agent_calls:
HEAD:backend/onyx/deep_research/dr_loop.py:752:                        tc.token_count for tc in tool_calls_simple
HEAD:backend/onyx/deep_research/utils.py:18:    """State for tracking think tool processing across streaming deltas."""
HEAD:backend/onyx/deep_research/utils.py:23:    full_arguments: str = ""  # Full accumulated arguments for final tool call
HEAD:backend/onyx/deep_research/utils.py:155:        # Check for think tool in tool_calls
HEAD:backend/onyx/deep_research/utils.py:157:            for tool_call in delta.tool_calls:
HEAD:backend/onyx/deep_research/utils.py:171:                # Accumulate arguments for the think tool
HEAD:backend/onyx/deep_research/utils.py:178:                    # Track full arguments for final tool call
HEAD:backend/onyx/deep_research/utils.py:203:    for tool_call in tool_calls:
HEAD:backend/onyx/evals/README.md:117:For testing realistic multi-turn conversations where each turn may require different tools, use the `messages` array format instead of a single `message`:
HEAD:backend/onyx/evals/eval.py:82:    tools_called = [tc.tool_name for tc in full.tool_calls]
HEAD:backend/onyx/evals/eval.py:85:        for tc in full.tool_calls
HEAD:backend/onyx/evals/eval.py:181:                for tool_type in input_force_tools:
HEAD:backend/onyx/evals/eval.py:348:                    for tool_type in msg.force_tools:
HEAD:backend/onyx/evals/models.py:106:                for tool in self.builtin_tool_types
HEAD:backend/onyx/evals/providers/local.py:44:            for tool_name, duration_ms in result.timings.tool_execution_ms.items():
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/tabular_section_chunker.py:180:    except StopIteration:
HEAD:backend/onyx/indexing/chunking/tabular_section_chunker/tabular_section_chunker.py:316:            except StopIteration:
HEAD:backend/onyx/indexing/models.py:56:    # multiple iterations of metadata representation for backwards compatibility
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:150:                for tool_call in tool_calls:
HEAD:backend/onyx/llm/litellm_singleton/monkey_patches.py:214:                # Mirror upstream's fix for BerriAI/litellm#18922: when tool
HEAD:backend/onyx/llm/model_response.py:115:        for tool_call in tool_calls
HEAD:backend/onyx/llm/model_response.py:153:    for tool_call in tool_calls:
HEAD:backend/onyx/llm/multi_llm.py:286:            for tc in tool_calls:
HEAD:backend/onyx/llm/multi_llm.py:744:        # ("Tool choice must be auto"). The chat loop's fallback tool-call
HEAD:backend/onyx/llm/multi_llm.py:875:                    # use), so skip thinking for a NamedToolChoice.
HEAD:backend/onyx/llm/multi_llm.py:1004:            # provided for this request but the history contains tool
HEAD:backend/onyx/llm/tracing_wrap.py:213:                        for delta_tc in chunk.choice.delta.tool_calls:
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:19:        "This can be used to discover filters for the `search_indexed_documents` tool."
HEAD:backend/onyx/onyxbot/slack/handlers/handle_regular_answer.py:344:                for tool in persona.tools
HEAD:backend/onyx/onyxbot/slack/listener.py:321:            # Already acquired in a previous loop iteration?
HEAD:backend/onyx/prompts/chat_tools.py:42:# For the case where the user has not configured any tools to call, but still using the tool-flow
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:30:- *Control flow* — how iteration / scheduling / triggers work
HEAD:backend/onyx/prompts/deep_research/dr_tool_prompts.py:16:# Hard for the open_url tool to be called for a ton of search results all at once so limit to 3
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:13:If the user query is already very detailed or lengthy (more than 3 sentences), do not ask for clarification and instead call the `{GENERATE_PLAN_TOOL_NAME}` tool.
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:63:You are an orchestrator agent for deep research. Your job is to conduct research by calling the {RESEARCH_AGENT_TOOL_NAME} tool with high level research tasks. \
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:155:You are an orchestrator agent for deep research. Your job is to conduct research by calling the {RESEARCH_AGENT_TOOL_NAME} tool with high level research tasks. \
HEAD:backend/onyx/prompts/tool_prompts.py:2:# If there are any tools, this section is included, the sections below are for the available tools
HEAD:backend/onyx/prompts/tool_prompts.py:8:For questions that can be answered from existing knowledge, answer the user directly without using any tools. \
HEAD:backend/onyx/prompts/tool_prompts.py:9:If you suspect your knowledge is outdated or for topics where things are rapidly changing, use search tools to get more context. \
HEAD:backend/onyx/prompts/tool_prompts.py:15:When searching for information, if the initial results cannot fully answer the user's query, try again with different tools or arguments. \
HEAD:backend/onyx/sandbox_proxy/errors.py:110:    code for tooling to match on, and human-readable `message` prose the agent
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:266:        for tool_name, count in counts.items()
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:102:        # Ungated requests only get credentials for protocol plumbing. A tool
HEAD:backend/onyx/secondary_llm_flows/document_filter.py:59:    except StopIteration:
HEAD:backend/onyx/server/features/build/AGENTS.template.md:53:Some org apps aren't set up for this user yet, so you can't call them until they're connected. When the task needs one, call the `connect_app` tool with its numeric external app ID from the list below; once connected, it works like any other app. Never ask for or handle credentials yourself.
HEAD:backend/onyx/server/features/build/configs.py:25:    t.strip() for t in _disabled_tools_str.split(",") if t.strip()
HEAD:backend/onyx/server/features/build/interactive_turns/executor.py:457:                                sandbox_event, "stop_reason", None
HEAD:backend/onyx/server/features/build/packets.py:71:    """A child opencode session was created for a parent task tool call."""
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:2106:            except StopIteration:
HEAD:backend/onyx/server/features/build/sandbox/docker/internal/exec_helpers.py:250:    Generator returns the process exit code via ``StopIteration.value``. The
HEAD:backend/onyx/server/features/build/sandbox/image/opencode-plugins/connect-app.ts:20:  for (const path of SDK_TOOL_PATHS) {
HEAD:backend/onyx/server/features/build/sandbox/image/opencode-plugins/webapp.ts:21:  for (const path of SDK_TOOL_PATHS) {
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:565:        missing the expected container) as an opaque ``StopIteration``; this
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/scripts/bench-sandbox-spinup.sh:115:# Run $REPS iterations, print min / median / max to stdout.
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/sidecar_client.py:73:            except StopIteration:
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:249:    """Build the ``content`` array expected by the consumer for a tool call.
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:251:    Returns ``None`` for tools that don't need content synthesis (bash,
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:290:    field. Opencode gives plain strings for most tools. Wrap consistently.
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:699:            for event in _emit_tool_events(part, state):
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:837:    ``field_meta`` (aliased ``_meta``) already carries ``toolName`` for tool
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:936:    stop_reason = "end_turn"
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:944:        stop_reason = finish
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:947:        stop_reason = "end_turn"
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:949:    yield PromptResponse.model_validate({"stopReason": stop_reason})
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:64:    for tool in get_mcp_tools_for_servers([s.id for s in servers], db_session):
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:115:        for tool in disabled_tools:
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:121:        for tool_name in server.disabled_tools:
HEAD:backend/onyx/server/features/build/scheduled_tasks/executor.py:269:    # because the agent loop can be long-running and we don't want a
HEAD:backend/onyx/server/features/build/scheduled_tasks/executor.py:397:        # agent loop. __enter__/__exit__ used directly (rather than a
HEAD:backend/onyx/server/features/build/scheduled_tasks/executor.py:473:                            sandbox_event, "stop_reason", None
HEAD:backend/onyx/server/features/default_assistant/api.py:41:    tool_ids = [tool.id for tool in persona.tools]
HEAD:backend/onyx/server/features/default_assistant/api.py:83:        tool_ids = [tool.id for tool in updated_persona.tools]
HEAD:backend/onyx/server/features/mcp/api.py:1423:    Get tools for an MCP server as ToolSnapshot objects.
HEAD:backend/onyx/server/features/mcp/api.py:1476:        for tool in mcp_tools
HEAD:backend/onyx/server/features/mcp/api.py:1496:    for tool in discovered_tools:
HEAD:backend/onyx/server/features/mcp/api.py:1535:    """Make the stored tools for the server match the discovered tools.
HEAD:backend/onyx/server/features/mcp/api.py:1546:    for db_tool in get_tools_by_mcp_server_id(mcp_server_id, db, order_by_id=True):
HEAD:backend/onyx/server/features/mcp/api.py:1558:    for name, db_tool in existing_by_name.items():
HEAD:backend/onyx/server/features/mcp/api.py:1645:    for tool in discovered_tools:
HEAD:backend/onyx/server/features/mcp/api.py:2149:    """Toggle enabled state for MCP tools that exist for the server.
HEAD:backend/onyx/server/features/mcp/api.py:2159:    existing_by_name = {tool.name: tool for tool in existing_tools}
HEAD:backend/onyx/server/features/mcp/api.py:2162:    for tool_name, db_tool in existing_by_name.items():
HEAD:backend/onyx/server/features/mcp/api.py:2235:    return [ToolSnapshot.from_model(tool) for tool in mcp_tools]
HEAD:backend/onyx/server/features/mcp/api.py:2343:    for tool in mcp_tools:
HEAD:backend/onyx/server/features/mcp/api.py:2611:        known = {t.name for t in get_all_mcp_tools_for_server(server_id, db_session)}
HEAD:backend/onyx/server/features/mcp/api.py:2623:            for tool, policy in request.tool_policies.items()
HEAD:backend/onyx/server/features/mcp/api.py:2682:        for tool in tools_to_delete:
HEAD:backend/onyx/server/features/mcp/api.py:2697:            for tool in remaining_tools:
HEAD:backend/onyx/server/features/mcp/client.py:90:# a new session for each tool call.
HEAD:backend/onyx/server/features/mcp/client.py:227:    for content_block in call_tool_result.content:
HEAD:backend/onyx/server/features/mcp/client.py:243:    return "\n\n".join(p for p in parts if p) or str(call_tool_result.structuredContent)
HEAD:backend/onyx/server/features/mcp/client.py:310:    Synchronous wrapper for discovering MCP tools.
HEAD:backend/onyx/server/features/mcp/models.py:747:    """Response for creating multiple MCP tools"""
HEAD:backend/onyx/server/features/mcp/models.py:765:    """Response for updating multiple MCP tools"""
HEAD:backend/onyx/server/features/oauth_config/api.py:76:    if tools and all(tool.user_id == user.id for tool in tools):
HEAD:backend/onyx/server/features/persona/models.py:213:    # Counts for knowledge sources (used to determine if search tool should be enabled)
HEAD:backend/onyx/server/features/persona/models.py:283:                for tool in persona.tools
HEAD:backend/onyx/server/features/persona/models.py:375:                for tool in persona.tools
HEAD:backend/onyx/server/features/persona/models.py:458:                for tool in persona.tools
HEAD:backend/onyx/server/features/search/api.py:153:        (tool.id for tool in all_tools if tool.in_code_tool_id == SEARCH_TOOL_ID),
HEAD:backend/onyx/server/features/tool/api.py:58:        for header in tool_data.custom_headers:
HEAD:backend/onyx/server/features/tool/api.py:256:    tools_by_id = {tool.id: tool for tool in tools}
HEAD:backend/onyx/server/features/tool/api.py:261:    for tool_id in update_data.tool_ids:
HEAD:backend/onyx/server/features/tool/api.py:321:    """Read gate for the management surfaces: can_manage_tool covers admin, creator and MCP
HEAD:backend/onyx/server/features/tool/api.py:337:    for tool in tools:
HEAD:backend/onyx/server/features/tool/api.py:384:    for tool in tools:
HEAD:backend/onyx/server/features/tool/models.py:54:        # Get visibility config for this tool
HEAD:backend/onyx/server/features/tool/tool_visibility.py:8:# Tool class name constant for OktaProfileTool (not in main constants.py as it's hidden)
HEAD:backend/onyx/server/features/tool/tool_visibility.py:13:    """Configuration for tool visibility across different UI contexts."""
HEAD:backend/onyx/server/features/tool/tool_visibility.py:23:# Centralized configuration for tool visibility across different contexts
HEAD:backend/onyx/server/features/tool/tool_visibility.py:24:# This allows for easy extension with new tools that need custom visibility rules
HEAD:backend/onyx/server/features/tool/tool_visibility.py:87:    """Get visibility configuration for a tool, or None if not configured."""
HEAD:backend/onyx/server/gateway/models.py:127:                tc.model_dump() for tc in response.choice.message.tool_calls
HEAD:backend/onyx/server/gateway/models.py:186:                tc.model_dump(exclude_none=True) for tc in chunk.choice.delta.tool_calls
HEAD:backend/onyx/server/gateway/models.py:672:    stop_reason: str | None
HEAD:backend/onyx/server/gateway/models.py:683:        stop_reason: str | None,
HEAD:backend/onyx/server/gateway/models.py:694:            stop_reason=stop_reason,
HEAD:backend/onyx/server/gateway/models.py:795:    stop_reason: str | None
HEAD:backend/onyx/server/gateway/models.py:799:    def create(cls, *, stop_reason: str | None) -> "AnthropicMessageDeltaPayload":
HEAD:backend/onyx/server/gateway/models.py:800:        return cls(stop_reason=stop_reason, stop_sequence=None)
HEAD:backend/onyx/server/manage/image_generation/models.py:155:    """Contains all info needed for image generation tool."""
HEAD:backend/onyx/server/manage/voice/user_api.py:210:    except StopAsyncIteration:
HEAD:backend/onyx/server/query_and_chat/placement.py:15:        sub_turn_index: Nesting level for tools that invoke other tools. ``None`` for
HEAD:backend/onyx/server/query_and_chat/placement.py:16:            top-level packets; an integer for tool-within-tool output.
HEAD:backend/onyx/server/query_and_chat/session_loading.py:284:    """Create packets for research agent tool calls.
HEAD:backend/onyx/server/query_and_chat/session_loading.py:336:    """Recreate the packet stream for a saved coding-agent tool call.
HEAD:backend/onyx/server/query_and_chat/session_loading.py:546:        for tool_call in chat_message.tool_calls:
HEAD:backend/onyx/server/query_and_chat/session_loading.py:554:        for turn_num in sorted(tool_calls_by_turn.keys()):
HEAD:backend/onyx/server/query_and_chat/session_loading.py:561:                    for tool_call in tool_calls_in_turn
HEAD:backend/onyx/server/query_and_chat/session_loading.py:583:            for tool_call in tool_calls_in_turn:
HEAD:backend/onyx/server/query_and_chat/session_loading.py:600:                            for doc in tool_call.search_docs
HEAD:backend/onyx/server/query_and_chat/session_loading.py:616:                            for doc in tool_call.search_docs
HEAD:backend/onyx/server/query_and_chat/session_loading.py:635:                                for img in tool_call.generated_images
HEAD:backend/onyx/server/query_and_chat/session_loading.py:778:                            for k, v in (tool_call.tool_call_arguments or {}).items()
HEAD:backend/onyx/server/query_and_chat/session_loading.py:815:        max_tool_turn = max(tc.turn_number for tc in chat_message.tool_calls)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:876:            max_tool_turn = max(tc.turn_number for tc in chat_message.tool_calls)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:887:    stop_reason: str | None = None
HEAD:backend/onyx/server/query_and_chat/session_loading.py:890:            stop_reason = "user_cancelled"
HEAD:backend/onyx/server/query_and_chat/session_loading.py:896:            obj=OverallStop(stop_reason=stop_reason),
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:79:    stop_reason: str | None = None
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:289:# The allowed streamed packets for a custom tool
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:13:> **Onyx Craft:** for basic reads of static pages, prefer the `webfetch` tool — it returns clean markdown, is faster, and is cheaper. Reach for `browser` only when the page needs JavaScript/SPA rendering, interaction (clicks, forms, login), multi-step navigation, or visual inspection.
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:53:For tools that support Model Context Protocol servers, start the stdio server:
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:61:Configure the MCP client to launch `browser` with `["mcp"]`. The server defaults to MCP protocol 2025-11-25 and accepts older supported client protocol versions during initialization. The default tools profile is `core`, which keeps MCP context small for everyday browser automation. Use `--tools all` for the full typed CLI parity surface, or combine profiles with commas, such as `--tools core,network,react`. Profiles are `core`, `network`, `state`, `debug`, `tabs`, `react`, `mobile`, and `all`; the `debug` profile includes plugin registry and command.run tools. Each tool accepts typed arguments plus `extraArgs` for advanced CLI flags and exact CLI parity. Tool discovery is paginated and includes read-only/open-world annotations so modern MCP clients can load the large typed surface incrementally. Use the tool `session` argument or `AGENT_BROWSER_SESSION` to isolate browser sessions.
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1187:The default tools profile is `core`, which keeps MCP context small for everyday browser automation. Use `--tools all` for the full typed CLI parity surface, or combine profiles with commas, such as `--tools core,network,react`.
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1215:Tool calls use the same config files and environment variables as the CLI. Each tool accepts typed arguments plus `extraArgs` for advanced CLI flags and exact CLI parity. Tool discovery is paginated and includes read-only/open-world annotations so modern MCP clients can load the large typed surface incrementally. Use the `session` tool argument or `AGENT_BROWSER_SESSION` to isolate browser state.
HEAD:backend/onyx/skills/builtin/image-generation/SKILL.md:128:- For edits, repeat the invariants every iteration (`change only X; keep Y unchanged`).
HEAD:backend/onyx/tools/built_in_tools.py:77:    return {_tool_llm_name(cls): cls for cls in BUILT_IN_TOOL_MAP.values()}
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:238:            except StopIteration as e:
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:255:    for tool_call in tool_calls:
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:390:                        except StopIteration as e:
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:446:                        tc for tc in tool_calls if tc.tool_name == BASH_TOOL_NAME
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:451:                            [tc.tool_name for tc in tool_calls],
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:469:                        token_count=sum(tcs.token_count for tcs in tool_calls_simple),
HEAD:backend/onyx/tools/fake_tools/research_agent.py:187:            except StopIteration as e:
HEAD:backend/onyx/tools/fake_tools/research_agent.py:290:                tools_by_name = {tool.name: tool for tool in current_tools}
HEAD:backend/onyx/tools/fake_tools/research_agent.py:296:                    if any(isinstance(tool, SearchTool) for tool in current_tools)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:301:                    if any(isinstance(tool, WebSearchTool) for tool in current_tools)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:305:                    isinstance(tool, OpenURLTool) for tool in current_tools
HEAD:backend/onyx/tools/fake_tools/research_agent.py:360:                # think_tool calls to reasoning content (same as dr_loop.py)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:370:                    tool_definitions=[tool.tool_definition() for tool in current_tools]
HEAD:backend/onyx/tools/fake_tools/research_agent.py:407:                        tc for tc in tool_calls if tc.tool_name == first_tool_type
HEAD:backend/onyx/tools/fake_tools/research_agent.py:487:                                for tool_call in state_container.get_tool_calls()
HEAD:backend/onyx/tools/fake_tools/research_agent.py:489:                                for search_doc in tool_call.search_docs
HEAD:backend/onyx/tools/fake_tools/research_agent.py:511:                        tr for tr in tool_responses if tr.tool_call is not None
HEAD:backend/onyx/tools/fake_tools/research_agent.py:517:                        for tool_response in valid_tool_responses:
HEAD:backend/onyx/tools/fake_tools/research_agent.py:532:                            tc.token_count for tc in tool_calls_simple
HEAD:backend/onyx/tools/fake_tools/research_agent.py:544:                    for tool_response in valid_tool_responses:
HEAD:backend/onyx/tools/fake_tools/research_agent.py:705:        for research_agent_call, parent_tool_call_id in zip(
HEAD:backend/onyx/tools/fake_tools/research_agent.py:791:            for tool_list in tool_dict.values()
HEAD:backend/onyx/tools/fake_tools/research_agent.py:792:            for tool in tool_list
HEAD:backend/onyx/tools/fake_tools/research_agent.py:798:        logger.info("Tools: %s", [t.name for t in tools])
HEAD:backend/onyx/tools/interface.py:59:            db_session: Database session for tools that need DB access
HEAD:backend/onyx/tools/interface.py:73:        Emit the start packet for this tool. Each tool implementation should
HEAD:backend/onyx/tools/interface.py:77:            turn_index: The turn index for this tool execution
HEAD:backend/onyx/tools/interface.py:78:            tab_index: The tab index for parallel tool calls
HEAD:backend/onyx/tools/interface.py:87:        # For example when calling the internal search tool, the original user query is passed along too (but not by the LLM)
HEAD:backend/onyx/tools/models.py:32:    """Exception raised for errors during tool calls."""
HEAD:backend/onyx/tools/models.py:43:    """Exception raise for errors during tool execution."""
HEAD:backend/onyx/tools/models.py:184:    # Used for tool calls after the first one but in the same chat turn. The reason for this is that if the initial pass through
HEAD:backend/onyx/tools/models.py:235:    """Override kwargs for the Python/Code Interpreter tool."""
HEAD:backend/onyx/tools/models.py:292:    """Base class for tool results that can be cited."""
HEAD:backend/onyx/tools/tool_constructor.py:58:    tool_name_counts = Counter(tool.name for tool in tools)
HEAD:backend/onyx/tools/tool_constructor.py:59:    for tool in tools:
HEAD:backend/onyx/tools/tool_constructor.py:139:        for tool in persona_tools
HEAD:backend/onyx/tools/tool_constructor.py:193:    persona_tool_names = [t.name for t in persona.tools]
HEAD:backend/onyx/tools/tool_constructor.py:239:    for db_tool_model in persona.tools:
HEAD:backend/onyx/tools/tool_constructor.py:258:                    "Failed checking availability for tool %s", tool_cls.__name__
HEAD:backend/onyx/tools/tool_constructor.py:415:                            "No valid OAuth token found for tool %s with OAuth config %s",
HEAD:backend/onyx/tools/tool_constructor.py:481:            for saved_tool in saved_tools:
HEAD:backend/onyx/tools/tool_constructor.py:482:                # Create MCPTool instance for this specific tool
HEAD:backend/onyx/tools/tool_constructor.py:513:        # Get the database tool model for SearchTool
HEAD:backend/onyx/tools/tool_constructor.py:540:    for tool_list in tool_dict.values():
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:125:        """Emit start packet for this tool. Code will be emitted in run() method."""
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:31:    """Top-level Tool wrapper around the coding-agent loop.
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:34:    runs the inner agent loop (downloads repo, opens a code-interpreter
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:49:# override_kwargs is not supported for custom tools
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:239:                    "Failed to parse response as JSON for tool '%s'", self._name
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:403:            tool.tool_definition() for tool in tools
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:37:    """No override kwargs needed for the file reader tool."""
HEAD:backend/onyx/tools/tool_implementations/knowledge_graph/knowledge_graph_tool.py:19:    _DESCRIPTION = "Search the knowledge graph for information. Never call this tool."
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:48:# TODO: for now we're fitting MCP tool responses into the CustomToolCallSummary class
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:49:# In the future we may want custom handling for MCP tool responses
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:61:    # properties for zero-arg tools, so seed `properties: {}` ourselves.
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:191:                    "Authentication required for MCP tool '%s' but no credentials found",
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:299:                    f"Authentication failed for the {self._name} tool from {self.mcp_server.name}. "
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:435:            tool_id: Unique identifier for this tool instance.
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:537:            placement: The placement info (turn_index and tab_index) for this tool call.
HEAD:backend/onyx/tools/tool_implementations/open_url/url_normalization.py:1:"""URL normalization for OpenURL tool.
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:233:        # the same file on every tool call iteration within the same agent session.
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:238:        # iterations, typically a few minutes), so stale-ID eviction is not needed.
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:289:        """Emit start packet for this tool. Code will be emitted in run() method."""
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:359:            placement: The placement info (turn_index and tab_index) for this tool call.
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:521:                # _uploaded_file_cache reuses their file_ids across iterations. They are
HEAD:backend/onyx/tools/tool_implementations/search/constants.py:1:"""Constants for search tool implementations."""
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:563:    """For explicit tool calling"""
HEAD:backend/onyx/tools/tool_implementations/web_search/models.py:12:# This is the cap for both when the tool is running a single search and when running multiple queries in parallel
HEAD:backend/onyx/tools/tool_runner.py:52:# 10 minute timeout for tool execution to prevent indefinite hangs
HEAD:backend/onyx/tools/tool_runner.py:64:    """Merge multiple tool calls for SearchTool, WebSearchTool, or OpenURLTool into a single call.
HEAD:backend/onyx/tools/tool_runner.py:66:    For SearchTool (internal_search) and WebSearchTool (web_search), if there are
HEAD:backend/onyx/tools/tool_runner.py:68:    For OpenURLTool (open_url), multiple calls have their urls merged.
HEAD:backend/onyx/tools/tool_runner.py:81:    for tool_call in tool_calls:
HEAD:backend/onyx/tools/tool_runner.py:85:    for tool_name, calls in tool_calls_by_name.items():
HEAD:backend/onyx/tools/tool_runner.py:150:            logger.error("Tool call error for %s: %s", tool.name, e)
HEAD:backend/onyx/tools/tool_runner.py:235:    # The stuff below is needed for the different individual built-in tools
HEAD:backend/onyx/tools/tool_runner.py:244:    # Skip query expansion for repeat search tool calls
HEAD:backend/onyx/tools/tool_runner.py:248:    # A map of url -> summary for passing web results to open url tool
HEAD:backend/onyx/tools/tool_runner.py:256:    Before execution, tool calls for `SearchTool`, `WebSearchTool`, and `OpenURLTool`
HEAD:backend/onyx/tools/tool_runner.py:261:    Tools are executed in parallel (threadpool). For tools that generate citations,
HEAD:backend/onyx/tools/tool_runner.py:273:            for `SearchTool` override kwargs).
HEAD:backend/onyx/tools/tool_runner.py:281:        skip_search_query_expansion: Whether to skip query expansion for `SearchTool`
HEAD:backend/onyx/tools/tool_runner.py:286:        - `tool_responses`: `ToolResponse` objects for successfully dispatched tool calls
HEAD:backend/onyx/tools/tool_runner.py:291:    # Merge tool calls for SearchTool, WebSearchTool, and OpenURLTool
HEAD:backend/onyx/tools/tool_runner.py:302:    tools_by_name = {tool.name: tool for tool in tools}
HEAD:backend/onyx/tools/tool_runner.py:306:    for tool_call in merged_tool_calls:
HEAD:backend/onyx/tools/tool_runner.py:324:    # Prepare minimal history for SearchTool (computed once, shared by all)
HEAD:backend/onyx/tools/tool_runner.py:335:    # Convert citation_mapping for OpenURLTool (computed once, shared by all)
HEAD:backend/onyx/tools/tool_runner.py:344:    for tool_call in filtered_tool_calls:
HEAD:backend/onyx/tools/tool_runner.py:381:            # Increment citation number for next search tool to avoid conflicts
HEAD:backend/onyx/tools/tool_runner.py:389:            # Increment citation number for next search tool to avoid conflicts
HEAD:backend/onyx/tools/tool_runner.py:428:        for tool, tool_call, override_kwargs in tool_run_params
HEAD:backend/onyx/tools/tool_runner.py:433:        allow_failures=True,  # Continue even if some tools fail
HEAD:backend/onyx/tools/tool_runner.py:439:    for result in tool_run_results:
HEAD:backend/onyx/tools/tool_runner.py:449:    tool_responses = [result for result in tool_run_results if result is not None]
HEAD:backend/onyx/tools/utils.py:36:    return sum(compute_tool_tokens(tool, token_counter) for tool in tools)
HEAD:backend/onyx/tools/utils.py:44:        for tool_definition in tool_definitions
HEAD:backend/onyx/tools/utils.py:71:    names = [tool.name for tool in tools[:-1]]
HEAD:backend/onyx/tracing/llm_utils.py:133:            output_dict["tool_calls"] = [tc.model_dump() for tc in message.tool_calls]
HEAD:backend/onyx/tracing/llm_utils.py:154:    This function is useful for streaming where content, reasoning, tool_calls,
HEAD:backend/onyx/tracing/llm_utils.py:168:                output_dict["tool_calls"] = [tc.model_dump() for tc in tool_calls]
HEAD:backend/onyx/tracing/llm_utils.py:173:                output_dict["tool_calls"] = [tc.model_dump() for tc in tool_calls]
HEAD:backend/onyx/utils/sensitive.py:159:        """Prevent iteration over the value."""
HEAD:backend/onyx/utils/threadpool_concurrency.py:68:        # Return a snapshot of keys to avoid potential modification during iteration
HEAD:backend/onyx/utils/threadpool_concurrency.py:208:        # Return a snapshot to avoid modification during iteration
```
Bounded iteration, stop conditions and error handling are relevant to abuse,
availability and economic-security analysis.
## MCP Configuration and Access Model
Evidence lines: 650
```text
HEAD:backend/ee/onyx/db/mcp.py:5:from onyx.db.models import MCPServer__User, MCPServer__UserGroup
HEAD:backend/ee/onyx/db/mcp.py:9:def make_mcp_server_private(
HEAD:backend/ee/onyx/db/mcp.py:10:    server_id: int,
HEAD:backend/ee/onyx/db/mcp.py:17:        db_session.query(MCPServer__User).filter(
HEAD:backend/ee/onyx/db/mcp.py:18:            MCPServer__User.mcp_server_id == server_id
HEAD:backend/ee/onyx/db/mcp.py:21:            db_session.add(MCPServer__User(mcp_server_id=server_id, user_id=user_id))
HEAD:backend/ee/onyx/db/mcp.py:25:        db_session.query(MCPServer__UserGroup).filter(
HEAD:backend/ee/onyx/db/mcp.py:26:            MCPServer__UserGroup.mcp_server_id == server_id
HEAD:backend/ee/onyx/db/mcp.py:30:                MCPServer__UserGroup(mcp_server_id=server_id, user_group_id=group_id)
HEAD:backend/ee/onyx/db/user_group.py:46:    MCPServer__UserGroup,
HEAD:backend/ee/onyx/db/user_group.py:131:def _cleanup_mcp_server__user_group_relationships__no_commit(
HEAD:backend/ee/onyx/db/user_group.py:135:    db_session.query(MCPServer__UserGroup).filter(
HEAD:backend/ee/onyx/db/user_group.py:136:        MCPServer__UserGroup.user_group_id == user_group_id
HEAD:backend/ee/onyx/db/user_group.py:1053:    _cleanup_mcp_server__user_group_relationships__no_commit(
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:120:    if "mcp_servers" in body:
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:121:        # mcp_servers instructs Anthropic's own servers to connect to
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:125:            "mcp_servers is not supported by the Onyx gateway.",
HEAD:backend/onyx/auth/permission_projection.py:142:class MCPServerPermissions(TypedDict):
HEAD:backend/onyx/auth/permission_projection.py:149:MCP_SERVER_ACTIONS: frozenset[str] = frozenset(MCPServerPermissions.__annotations__)
HEAD:backend/onyx/auth/permission_projection.py:152:def mcp_server_permissions(*, can_manage: bool) -> dict[str, bool]:
HEAD:backend/onyx/auth/permission_projection.py:153:    """MCP server affordance map. Every action — edit, delete, authenticate (connect), and
HEAD:backend/onyx/auth/permission_projection.py:157:    result: MCPServerPermissions = {
HEAD:backend/onyx/chat/emitter.py:47:    (e.g. the Search API, MCP server).
HEAD:backend/onyx/configs/app_configs.py:42:# Certain services need to make HTTP requests to the API server, such as the MCP server and Discord bot
HEAD:backend/onyx/configs/app_configs.py:45:# This override allows self-hosting the MCP server with Onyx Cloud backend.
HEAD:backend/onyx/configs/app_configs.py:754:# intermediary idle timeouts (PgBouncer `server_idle_timeout` 600s, AWS
HEAD:backend/onyx/configs/app_configs.py:1218:# MCP_SERVER_ALLOW_PRIVATE_NETWORK, MCP_SERVER_ALLOW_LOOPBACK) are no longer read
HEAD:backend/onyx/configs/app_configs.py:1234:# an internal MCP server can opt in. Loopback/unspecified/link-local (incl.
HEAD:backend/onyx/configs/app_configs.py:1236:MCP_SERVER_ALLOW_PRIVATE_NETWORK = (
HEAD:backend/onyx/configs/app_configs.py:1237:    os.environ.get("MCP_SERVER_ALLOW_PRIVATE_NETWORK", "false").lower() == "true"
HEAD:backend/onyx/configs/app_configs.py:1242:# blocked even under MCP_SERVER_ALLOW_PRIVATE_NETWORK unless explicitly opted in.
HEAD:backend/onyx/configs/app_configs.py:1244:# local mock MCP servers; cloud-metadata/link-local stay blocked regardless.
HEAD:backend/onyx/configs/app_configs.py:1245:MCP_SERVER_ALLOW_LOOPBACK = (
HEAD:backend/onyx/configs/app_configs.py:1246:    os.environ.get("MCP_SERVER_ALLOW_LOOPBACK", "false").lower() == "true"
HEAD:backend/onyx/configs/app_configs.py:1919:# MCP Server Configs
HEAD:backend/onyx/configs/app_configs.py:1921:MCP_SERVER_ENABLED = os.environ.get("MCP_SERVER_ENABLED", "").lower() == "true"
HEAD:backend/onyx/configs/app_configs.py:1922:_MCP_SERVER_API_REQUEST_TIMEOUT_RAW = int(
HEAD:backend/onyx/configs/app_configs.py:1923:    os.environ.get("MCP_SERVER_API_REQUEST_TIMEOUT_SECONDS") or 300
HEAD:backend/onyx/configs/app_configs.py:1925:MCP_SERVER_API_REQUEST_TIMEOUT_SECONDS: int = (
HEAD:backend/onyx/configs/app_configs.py:1926:    _MCP_SERVER_API_REQUEST_TIMEOUT_RAW
HEAD:backend/onyx/configs/app_configs.py:1927:    if _MCP_SERVER_API_REQUEST_TIMEOUT_RAW > 0
HEAD:backend/onyx/configs/app_configs.py:1930:MCP_SERVER_HOST = os.environ.get("MCP_SERVER_HOST", "0.0.0.0")  # noqa: S104 — server bind address; intentional default for containerized deployment
HEAD:backend/onyx/configs/app_configs.py:1931:MCP_SERVER_PORT = int(os.environ.get("MCP_SERVER_PORT") or 8090)
HEAD:backend/onyx/configs/app_configs.py:1936:MCP_SERVER_CORS_ORIGINS = [
HEAD:backend/onyx/configs/app_configs.py:1938:    for origin in os.environ.get("MCP_SERVER_CORS_ORIGINS", "").split(",")
HEAD:backend/onyx/connectors/discord/connector.py:95:    server_ids: list[int] | None,
HEAD:backend/onyx/connectors/discord/connector.py:105:        if server_ids and len(server_ids) > 0 and channel.guild.id not in server_ids:
HEAD:backend/onyx/connectors/discord/connector.py:193:    server_ids: list[int],
HEAD:backend/onyx/connectors/discord/connector.py:231:                server_ids=server_ids,
HEAD:backend/onyx/connectors/discord/connector.py:269:        server_ids: list[str] | None = None,
HEAD:backend/onyx/connectors/discord/connector.py:277:        if server_ids is None:
HEAD:backend/onyx/connectors/discord/connector.py:278:            server_ids = []
HEAD:backend/onyx/connectors/discord/connector.py:281:        self.server_ids: list[int] = (
HEAD:backend/onyx/connectors/discord/connector.py:282:            [int(server_id) for server_id in server_ids] if server_ids else []
HEAD:backend/onyx/connectors/discord/connector.py:320:            server_ids=self.server_ids,
HEAD:backend/onyx/connectors/discord/connector.py:352:    server_ids: str | None = os.environ.get("server_ids", None)
HEAD:backend/onyx/connectors/discord/connector.py:357:        server_ids=server_ids.split(",") if server_ids else [],
HEAD:backend/onyx/db/enums.py:202:class MCPServerStatus(str, PyEnum):
HEAD:backend/onyx/db/enums.py:543:    whether the target id refers to an ``external_app`` or an ``mcp_server`` row,
HEAD:backend/onyx/db/enums.py:548:    MCP_SERVER = "MCP_SERVER"
HEAD:backend/onyx/db/gated_app.py:2:policy read/write shared by every gated target (external app or MCP server).
HEAD:backend/onyx/db/gated_app.py:23:        else GatedApp.mcp_server_id
HEAD:backend/onyx/db/mcp.py:13:    MCPServerStatus,
HEAD:backend/onyx/db/mcp.py:21:    MCPServer,
HEAD:backend/onyx/db/mcp.py:22:    MCPServer__User,
HEAD:backend/onyx/db/mcp.py:23:    MCPServer__UserGroup,
HEAD:backend/onyx/db/mcp.py:36:# MCPServer operations
HEAD:backend/onyx/db/mcp.py:37:def get_all_mcp_servers(db_session: Session) -> list[MCPServer]:
HEAD:backend/onyx/db/mcp.py:38:    """Get all MCP servers"""
HEAD:backend/onyx/db/mcp.py:40:        db_session.scalars(select(MCPServer).order_by(MCPServer.created_at)).all()
HEAD:backend/onyx/db/mcp.py:44:def get_mcp_server_by_id(server_id: int, db_session: Session) -> MCPServer:
HEAD:backend/onyx/db/mcp.py:45:    """Get MCP server by ID"""
HEAD:backend/onyx/db/mcp.py:46:    server = db_session.scalar(select(MCPServer).where(MCPServer.id == server_id))
HEAD:backend/onyx/db/mcp.py:48:        raise ValueError("MCP server by specified id does not exist")
HEAD:backend/onyx/db/mcp.py:52:def get_mcp_servers_by_owner(owner_email: str, db_session: Session) -> list[MCPServer]:
HEAD:backend/onyx/db/mcp.py:53:    """Get all MCP servers owned by a specific user"""
HEAD:backend/onyx/db/mcp.py:56:            select(MCPServer).where(MCPServer.owner == owner_email)
HEAD:backend/onyx/db/mcp.py:61:def get_craft_enabled_mcp_servers(
HEAD:backend/onyx/db/mcp.py:63:) -> list[MCPServer]:
HEAD:backend/onyx/db/mcp.py:64:    """MCP servers an admin has made available to the Craft agent, filtered to
HEAD:backend/onyx/db/mcp.py:71:        select(MCPServer)
HEAD:backend/onyx/db/mcp.py:72:        .where(MCPServer.available_in_craft.is_(True))
HEAD:backend/onyx/db/mcp.py:73:        .options(selectinload(MCPServer.admin_connection_config))
HEAD:backend/onyx/db/mcp.py:76:        stmt = _add_mcp_server_access_filter(stmt, user)
HEAD:backend/onyx/db/mcp.py:80:def get_mcp_servers_for_persona(
HEAD:backend/onyx/db/mcp.py:84:) -> list[MCPServer]:
HEAD:backend/onyx/db/mcp.py:93:    # Collect unique MCP server IDs from the persona's tools
HEAD:backend/onyx/db/mcp.py:94:    mcp_server_ids = set()
HEAD:backend/onyx/db/mcp.py:96:        if tool.mcp_server_id:
HEAD:backend/onyx/db/mcp.py:97:            mcp_server_ids.add(tool.mcp_server_id)
HEAD:backend/onyx/db/mcp.py:99:    if not mcp_server_ids:
HEAD:backend/onyx/db/mcp.py:102:    # Fetch the MCP servers
HEAD:backend/onyx/db/mcp.py:103:    mcp_servers = (
HEAD:backend/onyx/db/mcp.py:104:        db_session.query(MCPServer).filter(MCPServer.id.in_(mcp_server_ids)).all()
HEAD:backend/onyx/db/mcp.py:107:    return list(mcp_servers)
HEAD:backend/onyx/db/mcp.py:110:def _add_mcp_server_access_filter(stmt: Select, user: User) -> Select:
HEAD:backend/onyx/db/mcp.py:118:    MCPServer__UG = aliased(MCPServer__UserGroup)
HEAD:backend/onyx/db/mcp.py:120:        stmt.outerjoin(MCPServer__UG, MCPServer__UG.mcp_server_id == MCPServer.id)
HEAD:backend/onyx/db/mcp.py:123:            User__UserGroup.user_group_id == MCPServer__UG.user_group_id,
HEAD:backend/onyx/db/mcp.py:125:        .outerjoin(MCPServer__User, MCPServer__User.mcp_server_id == MCPServer.id)
HEAD:backend/onyx/db/mcp.py:128:    where_clause = MCPServer.is_public == True  # noqa: E712
HEAD:backend/onyx/db/mcp.py:131:        where_clause |= MCPServer__User.user_id == user.id
HEAD:backend/onyx/db/mcp.py:133:        where_clause |= MCPServer.owner == user.email
HEAD:backend/onyx/db/mcp.py:137:def get_mcp_servers_accessible_to_user(
HEAD:backend/onyx/db/mcp.py:139:) -> list[MCPServer]:
HEAD:backend/onyx/db/mcp.py:140:    """MCP servers the user may attach to personas (public, or shared with them)."""
HEAD:backend/onyx/db/mcp.py:141:    stmt = _add_mcp_server_access_filter(
HEAD:backend/onyx/db/mcp.py:142:        select(MCPServer).order_by(MCPServer.created_at), user
HEAD:backend/onyx/db/mcp.py:147:def user_can_access_mcp_server(user: User, server_id: int, db_session: Session) -> bool:
HEAD:backend/onyx/db/mcp.py:149:    stmt = _add_mcp_server_access_filter(
HEAD:backend/onyx/db/mcp.py:150:        select(MCPServer.id).where(MCPServer.id == server_id), user
HEAD:backend/onyx/db/mcp.py:155:def affected_user_ids_for_mcp_server(
HEAD:backend/onyx/db/mcp.py:156:    server: MCPServer, db_session: Session
HEAD:backend/onyx/db/mcp.py:161:    land. Access must match what ``resolve_craft_mcp_servers`` bakes into a
HEAD:backend/onyx/db/mcp.py:163:    filter in ``_add_mcp_server_access_filter`` and therefore see every
HEAD:backend/onyx/db/mcp.py:172:            MCPServer__UserGroup,
HEAD:backend/onyx/db/mcp.py:173:            MCPServer__UserGroup.user_group_id == User__UserGroup.user_group_id,
HEAD:backend/onyx/db/mcp.py:175:        .where(MCPServer__UserGroup.mcp_server_id == server.id)
HEAD:backend/onyx/db/mcp.py:177:    direct_users = select(MCPServer__User.user_id).where(
HEAD:backend/onyx/db/mcp.py:178:        MCPServer__User.mcp_server_id == server.id
HEAD:backend/onyx/db/mcp.py:197:def make_mcp_server_private(
HEAD:backend/onyx/db/mcp.py:198:    server_id: int,  # noqa: ARG001
HEAD:backend/onyx/db/mcp.py:208:            "Onyx MIT does not support restricting MCP servers to users/groups"
HEAD:backend/onyx/db/mcp.py:212:def create_mcp_server__no_commit(
HEAD:backend/onyx/db/mcp.py:228:) -> MCPServer:
HEAD:backend/onyx/db/mcp.py:229:    """Create a new MCP server"""
HEAD:backend/onyx/db/mcp.py:230:    new_server = MCPServer(
HEAD:backend/onyx/db/mcp.py:251:def update_mcp_server__no_commit(
HEAD:backend/onyx/db/mcp.py:252:    server_id: int,
HEAD:backend/onyx/db/mcp.py:266:    status: MCPServerStatus | None = None,
HEAD:backend/onyx/db/mcp.py:270:) -> MCPServer:
HEAD:backend/onyx/db/mcp.py:271:    """Update an existing MCP server"""
HEAD:backend/onyx/db/mcp.py:272:    server = get_mcp_server_by_id(server_id, db_session)
HEAD:backend/onyx/db/mcp.py:311:def delete_mcp_server(server_id: int, db_session: Session) -> None:
HEAD:backend/onyx/db/mcp.py:312:    """Delete an MCP server and all associated tools (via CASCADE)"""
HEAD:backend/onyx/db/mcp.py:313:    server = get_mcp_server_by_id(server_id, db_session)
HEAD:backend/onyx/db/mcp.py:316:    tools_count = db_session.query(Tool).filter(Tool.mcp_server_id == server_id).count()
HEAD:backend/onyx/db/mcp.py:318:        "Deleting MCP server %s with %s associated tools", server_id, tools_count
HEAD:backend/onyx/db/mcp.py:324:    logger.info("Successfully deleted MCP server %s and its tools", server_id)
HEAD:backend/onyx/db/mcp.py:327:def get_all_mcp_tools_for_server(server_id: int, db_session: Session) -> list[Tool]:
HEAD:backend/onyx/db/mcp.py:330:        db_session.scalars(select(Tool).where(Tool.mcp_server_id == server_id)).all()
HEAD:backend/onyx/db/mcp.py:334:def get_mcp_tools_for_servers(server_ids: list[int], db_session: Session) -> list[Tool]:
HEAD:backend/onyx/db/mcp.py:335:    """All MCP tools across ``server_ids`` in a single query"""
HEAD:backend/onyx/db/mcp.py:336:    if not server_ids:
HEAD:backend/onyx/db/mcp.py:339:        db_session.scalars(select(Tool).where(Tool.mcp_server_id.in_(server_ids))).all()
HEAD:backend/onyx/db/mcp.py:343:def add_user_to_mcp_server(server_id: int, user_id: UUID, db_session: Session) -> None:
HEAD:backend/onyx/db/mcp.py:344:    """Grant a user access to an MCP server"""
HEAD:backend/onyx/db/mcp.py:345:    server = get_mcp_server_by_id(server_id, db_session)
HEAD:backend/onyx/db/mcp.py:357:def remove_user_from_mcp_server(
HEAD:backend/onyx/db/mcp.py:358:    server_id: int, user_id: UUID, db_session: Session
HEAD:backend/onyx/db/mcp.py:360:    """Remove a user's access to an MCP server"""
HEAD:backend/onyx/db/mcp.py:361:    server = get_mcp_server_by_id(server_id, db_session)
HEAD:backend/onyx/db/mcp.py:389:    server_id: int, user_email: str, db_session: Session
HEAD:backend/onyx/db/mcp.py:391:    """Get a user's connection config for a specific MCP server"""
HEAD:backend/onyx/db/mcp.py:395:                MCPConnectionConfig.mcp_server_id == server_id,
HEAD:backend/onyx/db/mcp.py:403:    server_ids: list[int], user_email: str, db_session: Session
HEAD:backend/onyx/db/mcp.py:405:    """`user_email`'s own connection configs for `server_ids`, keyed by server id.
HEAD:backend/onyx/db/mcp.py:407:    if not server_ids:
HEAD:backend/onyx/db/mcp.py:412:                MCPConnectionConfig.mcp_server_id.in_(server_ids),
HEAD:backend/onyx/db/mcp.py:417:    return {row.mcp_server_id: row for row in rows if row.mcp_server_id is not None}
HEAD:backend/onyx/db/mcp.py:421:    server_id: int, db_session: Session
HEAD:backend/onyx/db/mcp.py:423:    """Get all user connection configs for a specific MCP server"""
HEAD:backend/onyx/db/mcp.py:427:                MCPConnectionConfig.mcp_server_id == server_id
HEAD:backend/onyx/db/mcp.py:436:    mcp_server_id: int | None = None,
HEAD:backend/onyx/db/mcp.py:441:        mcp_server_id=mcp_server_id,
HEAD:backend/onyx/db/mcp.py:478:    server_id: int,
HEAD:backend/onyx/db/mcp.py:483:    """Create or update a user's connection config for an MCP server"""
HEAD:backend/onyx/db/mcp.py:484:    existing_config = get_user_connection_config(server_id, user_email, db_session)
HEAD:backend/onyx/db/mcp.py:493:            mcp_server_id=server_id,
HEAD:backend/onyx/db/mcp.py:507:    server_id: int, user_email: str, db_session: Session
HEAD:backend/onyx/db/mcp.py:513:                MCPConnectionConfig.mcp_server_id == server_id,
HEAD:backend/onyx/db/mcp.py:526:    server_id: int, db_session: Session
HEAD:backend/onyx/db/mcp.py:528:    """Delete all user connection configs for a specific MCP server"""
HEAD:backend/onyx/db/mcp.py:532:                MCPConnectionConfig.mcp_server_id == server_id,
HEAD:backend/onyx/db/models.py:97:    MCPServerStatus,
HEAD:backend/onyx/db/models.py:494:    # MCP servers accessible to this user
HEAD:backend/onyx/db/models.py:495:    accessible_mcp_servers: Mapped[list["MCPServer"]] = relationship(
HEAD:backend/onyx/db/models.py:496:        "MCPServer", secondary="mcp_server__user", back_populates="users"
HEAD:backend/onyx/db/models.py:4044:    # MCP server this tool is associated with (null for non-MCP tools)
HEAD:backend/onyx/db/models.py:4045:    mcp_server_id: Mapped[int | None] = mapped_column(
HEAD:backend/onyx/db/models.py:4046:        Integer, ForeignKey("mcp_server.id", ondelete="CASCADE"), nullable=True
HEAD:backend/onyx/db/models.py:4064:    # MCP server relationship
HEAD:backend/onyx/db/models.py:4065:    mcp_server: Mapped["MCPServer | None"] = relationship(
HEAD:backend/onyx/db/models.py:4066:        "MCPServer", back_populates="current_actions"
HEAD:backend/onyx/db/models.py:5251:    # MCP servers accessible to this user group
HEAD:backend/onyx/db/models.py:5252:    accessible_mcp_servers: Mapped[list["MCPServer"]] = relationship(
HEAD:backend/onyx/db/models.py:5253:        "MCPServer", secondary="mcp_server__user_group", back_populates="user_groups"
HEAD:backend/onyx/db/models.py:5813:class MCPServer(Base):
HEAD:backend/onyx/db/models.py:5814:    """Model for storing MCP server configurations"""
HEAD:backend/onyx/db/models.py:5816:    __tablename__ = "mcp_server"
HEAD:backend/onyx/db/models.py:5824:    # Transport type for connecting to the MCP server
HEAD:backend/onyx/db/models.py:5852:    status: Mapped[MCPServerStatus] = mapped_column(
HEAD:backend/onyx/db/models.py:5853:        Enum(MCPServerStatus, native_enum=False),
HEAD:backend/onyx/db/models.py:5895:        foreign_keys="MCPConnectionConfig.mcp_server_id",
HEAD:backend/onyx/db/models.py:5896:        back_populates="mcp_server",
HEAD:backend/onyx/db/models.py:5900:        "Tool", back_populates="mcp_server", cascade="all, delete-orphan"
HEAD:backend/onyx/db/models.py:5904:        "User", secondary="mcp_server__user", back_populates="accessible_mcp_servers"
HEAD:backend/onyx/db/models.py:5908:        secondary="mcp_server__user_group",
HEAD:backend/onyx/db/models.py:5909:        back_populates="accessible_mcp_servers",
HEAD:backend/onyx/db/models.py:5913:class MCPServer__User(Base):
HEAD:backend/onyx/db/models.py:5914:    __tablename__ = "mcp_server__user"
HEAD:backend/onyx/db/models.py:5915:    mcp_server_id: Mapped[int] = mapped_column(
HEAD:backend/onyx/db/models.py:5916:        ForeignKey("mcp_server.id", ondelete="CASCADE"), primary_key=True
HEAD:backend/onyx/db/models.py:5923:class MCPServer__UserGroup(Base):
HEAD:backend/onyx/db/models.py:5924:    __tablename__ = "mcp_server__user_group"
HEAD:backend/onyx/db/models.py:5925:    mcp_server_id: Mapped[int] = mapped_column(
HEAD:backend/onyx/db/models.py:5926:        ForeignKey("mcp_server.id"), primary_key=True
HEAD:backend/onyx/db/models.py:5940:    mcp_server_id: Mapped[int | None] = mapped_column(
HEAD:backend/onyx/db/models.py:5941:        Integer, ForeignKey("mcp_server.id", ondelete="CASCADE"), nullable=True
HEAD:backend/onyx/db/models.py:5971:    mcp_server: Mapped["MCPServer | None"] = relationship(
HEAD:backend/onyx/db/models.py:5972:        "MCPServer",
HEAD:backend/onyx/db/models.py:5973:        foreign_keys=[mcp_server_id],
HEAD:backend/onyx/db/models.py:5976:    admin_servers: Mapped[list["MCPServer"]] = relationship(
HEAD:backend/onyx/db/models.py:5977:        "MCPServer",
HEAD:backend/onyx/db/models.py:5978:        foreign_keys="MCPServer.admin_connection_config_id",
HEAD:backend/onyx/db/models.py:5984:        Index("ix_mcp_connection_config_server_user", "mcp_server_id", "user_email"),
HEAD:backend/onyx/db/models.py:6729:    # The gated target (external app or MCP server) this request hit, via the
HEAD:backend/onyx/db/models.py:6819:    def pre_approved_mcp_server_ids(self) -> list[int]:
HEAD:backend/onyx/db/models.py:6823:            grant.gated_app.mcp_server_id
HEAD:backend/onyx/db/models.py:6825:            if grant.gated_app.mcp_server_id is not None
HEAD:backend/onyx/db/models.py:6922:    The target is a ``gated_app`` row (external app or MCP server). Deleting the
HEAD:backend/onyx/db/models.py:7341:    or MCP server.
HEAD:backend/onyx/db/models.py:7351:    Exactly one of ``external_app_id`` / ``mcp_server_id`` is set; ``kind`` is
HEAD:backend/onyx/db/models.py:7364:    mcp_server_id: Mapped[int | None] = mapped_column(
HEAD:backend/onyx/db/models.py:7366:        ForeignKey("mcp_server.id", ondelete="CASCADE"),
HEAD:backend/onyx/db/models.py:7373:        UniqueConstraint("mcp_server_id", name="uq_gated_app_mcp_server"),
HEAD:backend/onyx/db/models.py:7375:            "num_nonnulls(external_app_id, mcp_server_id) = 1",
HEAD:backend/onyx/db/models.py:7387:            else GatedAppKind.MCP_SERVER
HEAD:backend/onyx/db/models.py:7396:            else self.mcp_server_id
HEAD:backend/onyx/db/models.py:7414:    ``action_id`` is a catalog id (external apps) or a tool name (MCP servers);
HEAD:backend/onyx/db/persona.py:1631:            from onyx.db.mcp import user_can_access_mcp_server
HEAD:backend/onyx/db/persona.py:1640:                server_id = tool.mcp_server_id
HEAD:backend/onyx/db/persona.py:1643:                    or server_id is None
HEAD:backend/onyx/db/persona.py:1644:                    or server_id in checked_servers
HEAD:backend/onyx/db/persona.py:1647:                checked_servers.add(server_id)
HEAD:backend/onyx/db/persona.py:1648:                if not user_can_access_mcp_server(user, server_id, db_session):
HEAD:backend/onyx/db/persona.py:1651:                        "selected MCP servers."
HEAD:backend/onyx/db/scheduled_task.py:63:    pre_approved_mcp_server_ids: list[int] | None = None,
HEAD:backend/onyx/db/scheduled_task.py:92:        mcp_server_ids=pre_approved_mcp_server_ids or [],
HEAD:backend/onyx/db/scheduled_task.py:104:    mcp_server_ids: list[int] | None = None,
HEAD:backend/onyx/db/scheduled_task.py:115:            (GatedAppKind.MCP_SERVER, mcp_server_ids),
HEAD:backend/onyx/db/scheduled_task.py:197:    pre_approved_mcp_server_ids: list[int] | None = None,
HEAD:backend/onyx/db/scheduled_task.py:227:        mcp_server_ids=pre_approved_mcp_server_ids,
HEAD:backend/onyx/db/scheduled_task.py:539:# target is a (kind, id) pair spanning external apps and MCP servers.
HEAD:backend/onyx/db/tools.py:10:from onyx.db.enums import MCPServerStatus, Permission, PermissionAuthority
HEAD:backend/onyx/db/tools.py:12:    MCPServer,
HEAD:backend/onyx/db/tools.py:44:        # 1. Don't have an MCP server (mcp_server_id IS NULL) - Non-MCP tools
HEAD:backend/onyx/db/tools.py:45:        # 2. Have an MCP server that is connected - Connected MCP tools
HEAD:backend/onyx/db/tools.py:46:        query = query.outerjoin(MCPServer, Tool.mcp_server_id == MCPServer.id).where(
HEAD:backend/onyx/db/tools.py:48:                Tool.mcp_server_id.is_(None),  # Non-MCP tools (built-in, custom)
HEAD:backend/onyx/db/tools.py:49:                MCPServer.status == MCPServerStatus.CONNECTED,  # MCP tools connected
HEAD:backend/onyx/db/tools.py:60:            # tools from mcp servers will not have an openapi schema but it has `null`, so we need to exclude them.
HEAD:backend/onyx/db/tools.py:69:def get_tools_by_mcp_server_id(
HEAD:backend/onyx/db/tools.py:70:    mcp_server_id: int,
HEAD:backend/onyx/db/tools.py:76:    query = select(Tool).where(Tool.mcp_server_id == mcp_server_id)
HEAD:backend/onyx/db/tools.py:111:def can_manage_mcp_server(user: User, server: MCPServer) -> bool:
HEAD:backend/onyx/db/tools.py:112:    """Owner-or-admin gate for every action on an MCP server (edit, delete, connect, status).
HEAD:backend/onyx/db/tools.py:127:    if tool.mcp_server is not None:
HEAD:backend/onyx/db/tools.py:128:        return can_manage_mcp_server(user, tool.mcp_server)
HEAD:backend/onyx/db/tools.py:174:def get_mcp_server_ids_connected_to_groups(
HEAD:backend/onyx/db/tools.py:177:    """MCP server ids reachable from ``group_ids``. A scoped manager may view these without
HEAD:backend/onyx/db/tools.py:182:        _connected_to_groups_stmt(Tool.mcp_server_id, group_ids).where(
HEAD:backend/onyx/db/tools.py:183:            Tool.mcp_server_id.is_not(None)
HEAD:backend/onyx/db/tools.py:186:    return {server_id for (server_id,) in rows if server_id is not None}
HEAD:backend/onyx/db/tools.py:214:    mcp_server_id: int | None = None,
HEAD:backend/onyx/db/tools.py:228:        mcp_server_id=mcp_server_id,
HEAD:backend/onyx/db/users.py:28:    MCPServer,
HEAD:backend/onyx/db/users.py:661:        update(MCPServer)
HEAD:backend/onyx/db/users.py:662:        .where(MCPServer.owner == old_email)
HEAD:backend/onyx/external_apps/matching/engine.py:41:    ``mcp_server``. Lookups key off ``(kind, id)``, never ``app_name``: the
HEAD:backend/onyx/external_apps/matching/engine.py:43:    app_type, and two MCP servers can share a display name).
HEAD:backend/onyx/mcp_server/README.md:1:# Onyx MCP Server
HEAD:backend/onyx/mcp_server/README.md:5:The Onyx MCP server allows LLMs to connect to your Onyx instance and access its knowledge base and search capabilities through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).
HEAD:backend/onyx/mcp_server/README.md:7:With the Onyx MCP Server, you can search your knowledgebase and
HEAD:backend/onyx/mcp_server/README.md:15:The MCP server quickly validates and passes through the token on every request.
HEAD:backend/onyx/mcp_server/README.md:22:Depending on usage, the MCP Server may support OAuth and stdio in the future.
HEAD:backend/onyx/mcp_server/README.md:32:The MCP server is built on [FastMCP](https://github.com/jlowin/fastmcp) and runs alongside the main Onyx API server:
HEAD:backend/onyx/mcp_server/README.md:43:│  MCP Server     │
HEAD:backend/onyx/mcp_server/README.md:69:  "mcpServers": {
HEAD:backend/onyx/mcp_server/README.md:119:### Running the MCP Server
HEAD:backend/onyx/mcp_server/README.md:121:The MCP Server automatically launches with the `Run All Onyx Services` task from the default launch.json.
HEAD:backend/onyx/mcp_server/README.md:127:The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is a debugging tool for MCP servers:
HEAD:backend/onyx/mcp_server/README.md:159:  "service": "mcp_server"
HEAD:backend/onyx/mcp_server/README.md:165:**MCP Server Configuration:**
HEAD:backend/onyx/mcp_server/README.md:166:- `MCP_SERVER_ENABLED`: Enable MCP server (set to "true" to enable, default: disabled)
HEAD:backend/onyx/mcp_server/README.md:167:- `MCP_SERVER_PORT`: Port for MCP server (default: 8090)
HEAD:backend/onyx/mcp_server/README.md:168:- `MCP_SERVER_CORS_ORIGINS`: Comma-separated CORS origins (optional)
HEAD:backend/onyx/mcp_server/README.md:173:- `API_SERVER_URL_OVERRIDE_FOR_HTTP_REQUESTS`: Optional override URL. If set, takes precedence over the protocol/host variables. Used for self-hosting the MCP server with Onyx Cloud as the backend.
HEAD:backend/onyx/mcp_server/api.py:1:"""MCP server with FastAPI wrapper."""
HEAD:backend/onyx/mcp_server/api.py:14:from onyx.configs.app_configs import MCP_SERVER_CORS_ORIGINS
HEAD:backend/onyx/mcp_server/api.py:16:from onyx.mcp_server.auth import OnyxTokenVerifier
HEAD:backend/onyx/mcp_server/api.py:17:from onyx.mcp_server.utils import shutdown_http_client
HEAD:backend/onyx/mcp_server/api.py:29:# (python -m onyx.mcp_server_main, uvicorn onyx.mcp_server.api:mcp_app, etc.).
HEAD:backend/onyx/mcp_server/api.py:32:logger.info("Creating Onyx MCP Server...")
HEAD:backend/onyx/mcp_server/api.py:34:mcp_server = FastMCP(
HEAD:backend/onyx/mcp_server/api.py:35:    name="Onyx MCP Server",
HEAD:backend/onyx/mcp_server/api.py:40:# Import tools and resources AFTER mcp_server is created to avoid circular imports
HEAD:backend/onyx/mcp_server/api.py:41:# Components register themselves via decorators on the shared mcp_server instance
HEAD:backend/onyx/mcp_server/api.py:42:from onyx.mcp_server.resources import indexed_sources  # noqa: E402, F401
HEAD:backend/onyx/mcp_server/api.py:43:from onyx.mcp_server.tools import search  # noqa: E402, F401
HEAD:backend/onyx/mcp_server/api.py:45:logger.info("MCP server instance created")
HEAD:backend/onyx/mcp_server/api.py:49:    """Create FastAPI app wrapping MCP server with auth and shared client lifecycle."""
HEAD:backend/onyx/mcp_server/api.py:50:    mcp_asgi_app = mcp_server.http_app(path="/")
HEAD:backend/onyx/mcp_server/api.py:74:        logger.info("MCP server starting up")
HEAD:backend/onyx/mcp_server/api.py:80:            logger.info("MCP server shutting down")
HEAD:backend/onyx/mcp_server/api.py:84:        title="Onyx MCP Server",
HEAD:backend/onyx/mcp_server/api.py:97:            return JSONResponse({"status": "healthy", "service": "mcp_server"})
HEAD:backend/onyx/mcp_server/api.py:102:    if MCP_SERVER_CORS_ORIGINS:
HEAD:backend/onyx/mcp_server/api.py:103:        logger.info("CORS origins: %s", MCP_SERVER_CORS_ORIGINS)
HEAD:backend/onyx/mcp_server/api.py:106:            allow_origins=MCP_SERVER_CORS_ORIGINS,
HEAD:backend/onyx/mcp_server/api.py:107:            allow_credentials=cors_allow_credentials(MCP_SERVER_CORS_ORIGINS),
HEAD:backend/onyx/mcp_server/auth.py:1:"""Authentication helpers for the Onyx MCP server."""
HEAD:backend/onyx/mcp_server/auth.py:7:from onyx.mcp_server.utils import get_http_client
HEAD:backend/onyx/mcp_server/auth.py:8:from onyx.server.metrics.mcp_server import MCPAuthResult, record_mcp_auth_result
HEAD:backend/onyx/mcp_server/auth.py:28:                "MCP server failed to reach API /me for authentication: %s",
HEAD:backend/onyx/mcp_server/mcp.json.template:2:    "mcpServers": {
HEAD:backend/onyx/mcp_server/resources/__init__.py:1:"""Resource registrations for the Onyx MCP server."""
HEAD:backend/onyx/mcp_server/resources/__init__.py:4:from onyx.mcp_server.resources import (
HEAD:backend/onyx/mcp_server/resources/agents.py:7:from onyx.mcp_server.api import mcp_server
HEAD:backend/onyx/mcp_server/resources/agents.py:8:from onyx.mcp_server.utils import get_accessible_agents, require_access_token
HEAD:backend/onyx/mcp_server/resources/agents.py:14:@mcp_server.resource(
HEAD:backend/onyx/mcp_server/resources/agents.py:35:        "Onyx MCP Server: agents resource returning %s entries",
HEAD:backend/onyx/mcp_server/resources/document_sets.py:7:from onyx.mcp_server.api import mcp_server
HEAD:backend/onyx/mcp_server/resources/document_sets.py:8:from onyx.mcp_server.utils import get_accessible_document_sets, require_access_token
HEAD:backend/onyx/mcp_server/resources/document_sets.py:14:@mcp_server.resource(
HEAD:backend/onyx/mcp_server/resources/document_sets.py:34:        "Onyx MCP Server: document_sets resource returning %s entries",
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:1:"""Resources that expose metadata for the Onyx MCP server."""
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:7:from onyx.mcp_server.api import mcp_server
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:8:from onyx.mcp_server.utils import get_indexed_sources, require_access_token
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:14:@mcp_server.resource(
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:31:        "Onyx MCP Server: indexed_sources resource returning %s entries",
HEAD:backend/onyx/mcp_server/tools/__init__.py:1:"""Tool registrations for the Onyx MCP server."""
HEAD:backend/onyx/mcp_server/tools/__init__.py:4:from onyx.mcp_server.tools import search  # noqa: F401
HEAD:backend/onyx/mcp_server/tools/search.py:1:"""Search tools for MCP server - document and web search."""
HEAD:backend/onyx/mcp_server/tools/search.py:13:from onyx.configs.app_configs import MCP_SERVER_API_REQUEST_TIMEOUT_SECONDS
HEAD:backend/onyx/mcp_server/tools/search.py:15:from onyx.mcp_server.api import mcp_server
HEAD:backend/onyx/mcp_server/tools/search.py:16:from onyx.mcp_server.utils import (
HEAD:backend/onyx/mcp_server/tools/search.py:36:from onyx.server.metrics.mcp_server import (
HEAD:backend/onyx/mcp_server/tools/search.py:38:    MCPServerToolName,
HEAD:backend/onyx/mcp_server/tools/search.py:41:    record_mcp_server_tool_outcome,
HEAD:backend/onyx/mcp_server/tools/search.py:63:            float(MCP_SERVER_API_REQUEST_TIMEOUT_SECONDS), connect=10.0
HEAD:backend/onyx/mcp_server/tools/search.py:95:        logger.debug("Onyx MCP Server: error body was not JSON (%s)", exc)
HEAD:backend/onyx/mcp_server/tools/search.py:272:@mcp_server.tool()
HEAD:backend/onyx/mcp_server/tools/search.py:334:    tool = MCPServerToolName.SEARCH_INDEXED_DOCUMENTS
HEAD:backend/onyx/mcp_server/tools/search.py:336:        "Onyx MCP Server: document search: query='%s', sources=%s, document_sets=%s, agent=%s",
HEAD:backend/onyx/mcp_server/tools/search.py:368:            logger.info("Onyx MCP Server: No indexed sources available for tenant")
HEAD:backend/onyx/mcp_server/tools/search.py:380:                "Onyx MCP Server: invalid time_cutoff '%s' (%s); continuing without time filter",
HEAD:backend/onyx/mcp_server/tools/search.py:404:            "Onyx MCP Server: Internal search returned %s results", len(results)
HEAD:backend/onyx/mcp_server/tools/search.py:408:        logger.error("Onyx MCP Server: Document search error: %s", err, exc_info=True)
HEAD:backend/onyx/mcp_server/tools/search.py:411:        record_mcp_server_tool_outcome(tool, _start, outcome)
HEAD:backend/onyx/mcp_server/tools/search.py:416:@mcp_server.tool()
HEAD:backend/onyx/mcp_server/tools/search.py:437:    tool = MCPServerToolName.SEARCH_WEB
HEAD:backend/onyx/mcp_server/tools/search.py:438:    logger.info("Onyx MCP Server: Web search: query='%s', limit=%s", query, limit)
HEAD:backend/onyx/mcp_server/tools/search.py:464:        logger.error("Onyx MCP Server: Web search error: %s", e, exc_info=True)
HEAD:backend/onyx/mcp_server/tools/search.py:471:        record_mcp_server_tool_outcome(tool, _start, outcome)
HEAD:backend/onyx/mcp_server/tools/search.py:476:@mcp_server.tool()
HEAD:backend/onyx/mcp_server/tools/search.py:497:    tool = MCPServerToolName.OPEN_URLS
HEAD:backend/onyx/mcp_server/tools/search.py:498:    logger.info("Onyx MCP Server: Open URL: fetching %s URLs", len(urls))
HEAD:backend/onyx/mcp_server/tools/search.py:517:        logger.error("Onyx MCP Server: URL fetch error: %s", err, exc_info=True)
HEAD:backend/onyx/mcp_server/tools/search.py:520:        record_mcp_server_tool_outcome(tool, _start, outcome)
HEAD:backend/onyx/mcp_server/utils.py:1:"""Utility helpers for the Onyx MCP server."""
HEAD:backend/onyx/mcp_server/utils.py:56:            "MCP Server requires an Onyx access token to authenticate your request"
HEAD:backend/onyx/mcp_server/utils.py:101:            "Onyx MCP Server: Failed to fetch indexed sources",
HEAD:backend/onyx/mcp_server/utils.py:108:            "Onyx MCP Server: Unexpected error fetching indexed sources",
HEAD:backend/onyx/mcp_server/utils.py:131:            "Onyx MCP Server: Failed to fetch document sets",
HEAD:backend/onyx/mcp_server/utils.py:137:            "Onyx MCP Server: Unexpected error fetching document sets",
HEAD:backend/onyx/mcp_server/utils.py:160:            "Onyx MCP Server: Failed to fetch agents",
HEAD:backend/onyx/mcp_server/utils.py:166:            "Onyx MCP Server: Unexpected error fetching agents",
HEAD:backend/onyx/mcp_server_main.py:1:"""Entry point for MCP server - HTTP POST transport with API key auth."""
HEAD:backend/onyx/mcp_server_main.py:6:    MCP_SERVER_ENABLED,
HEAD:backend/onyx/mcp_server_main.py:7:    MCP_SERVER_HOST,
HEAD:backend/onyx/mcp_server_main.py:8:    MCP_SERVER_PORT,
HEAD:backend/onyx/mcp_server_main.py:18:    """Run the MCP server."""
HEAD:backend/onyx/mcp_server_main.py:19:    if not MCP_SERVER_ENABLED:
HEAD:backend/onyx/mcp_server_main.py:20:        logger.info("MCP server is disabled (MCP_SERVER_ENABLED=false)")
HEAD:backend/onyx/mcp_server_main.py:25:    logger.info("Starting MCP server on %s:%s", MCP_SERVER_HOST, MCP_SERVER_PORT)
HEAD:backend/onyx/mcp_server_main.py:27:    from onyx.mcp_server.api import mcp_app
HEAD:backend/onyx/mcp_server_main.py:31:        host=MCP_SERVER_HOST,
HEAD:backend/onyx/mcp_server_main.py:32:        port=MCP_SERVER_PORT,
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:62:        refreshed at most once per interval (see `MCPServerResolver`).
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:23:from onyx.db.mcp import get_craft_enabled_mcp_servers
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:24:from onyx.db.models import ExternalApp, MCPServer
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:67:    external app and a craft MCP server, the external-app attribution governs,
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:147:    """Gates craft-enabled MCP servers: proxy-authoritative per-tool approvals.
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:149:    Attributes a request to a craft MCP server by the same host + path-prefix
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:176:                get_craft_enabled_mcp_servers(db, user) if user is not None else []
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:194:            server = servers_by_id[target.server_id]
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:196:                kind=GatedAppKind.MCP_SERVER, id=server.id, app_name=server.name
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:233:    server: MCPServer,
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:251:    stored = get_action_policies(db, GatedAppKind.MCP_SERVER, server.id)
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:4:craft-enabled `MCPServer` (if any) a sandbox request belongs to — otherwise a
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:29:    def __init__(self, host: str, path: str, server_ids: list[int]) -> None:
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:30:        self.server_ids = server_ids
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:33:            f"{len(server_ids)} MCP servers ({server_ids}) at the same "
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:43:    server_id: int
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:50:def parse_target(server_id: int, server_url: str) -> CraftMCPTarget | None:
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:57:            "craft MCP server %s has an unusable server_url; "
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:59:            server_id,
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:63:        server_id=server_id,
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:118:            request.host, path, sorted(w.server_id for w in winners)
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:3:Claims sandbox egress to a craft-enabled `MCPServer`'s `server_url` and injects
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:26:    get_craft_enabled_mcp_servers,
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:27:    get_mcp_server_by_id,
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:28:    user_can_access_mcp_server,
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:30:from onyx.db.models import MCPServer
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:63:class MCPServerResolver(CredentialResolver):
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:81:        # on a shared host (MCP servers aren't in that catalog) — defer. An MCP
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:84:        if actions is not None and actions.target.kind is not GatedAppKind.MCP_SERVER:
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:97:        if actions is not None and actions.target.kind is GatedAppKind.MCP_SERVER:
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:124:                    "Multiple MCP servers in Onyx are configured with the same "
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:126:                    "Ask a workspace admin to remove the duplicate MCP server "
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:136:                    "This host belongs to an MCP server configured in Onyx, but "
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:142:        return self._resolve_for_server(target.server_id, ctx)
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:145:        self, server_id: int, ctx: InjectionContext
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:150:            server = get_mcp_server_by_id(server_id, db)
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:155:                    f"MCP server {server.id} is no longer craft-enabled",
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:163:            if not user_can_access_mcp_server(user, server.id, db):
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:166:                    f"user {short_log_id(user_id)} lacks access to MCP server "
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:192:                    f"OAuth token for MCP server {server.id} is expired and "
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:208:    def _audit(self, server: MCPServer, user_id: UUID) -> None:
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:210:            credential_type="mcp_server",
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:232:            servers = get_craft_enabled_mcp_servers(db, None)
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:240:        return tuple(t for t in self._targets(tenant_id) if t.server_id in accessible)
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:258:                get_craft_enabled_mcp_servers(db, user) if user is not None else []
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:264:    tenant_id: str, server: MCPServer, connection_config_id: int
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:289:        f'The MCP server "{server_name}" is not connected. '
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:296:        f'The saved credentials for the MCP server "{server_name}" are expired and '
HEAD:backend/onyx/sandbox_proxy/server.py:32:from onyx.sandbox_proxy.resolvers.mcp_server import MCPServerResolver
HEAD:backend/onyx/sandbox_proxy/server.py:174:        MCPServerResolver(),
HEAD:backend/onyx/server/features/build/configs.py:142:# instead the per-session opencode.json stamps this header on each MCP server.
HEAD:backend/onyx/server/features/build/sandbox/README.md:15:- **OpenCode agent** - AI coding agent with access to tools and MCP servers
HEAD:backend/onyx/server/features/build/sandbox/README.md:278:### Adding New MCP Servers
HEAD:backend/onyx/server/features/build/sandbox/base.py:40:    CraftMCPServerConfig,
HEAD:backend/onyx/server/features/build/sandbox/base.py:139:        Craft MCP servers and the gateway provider catalog are NOT registered
HEAD:backend/onyx/server/features/build/sandbox/base.py:189:        mcp_servers: Sequence[CraftMCPServerConfig] = (),
HEAD:backend/onyx/server/features/build/sandbox/base.py:252:        mcp_servers: Sequence[CraftMCPServerConfig] = (),
HEAD:backend/onyx/server/features/build/sandbox/base.py:297:        mcp_servers: Sequence[CraftMCPServerConfig] = (),
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:128:    CraftMCPServerConfig,
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1122:        mcp_servers: Sequence[CraftMCPServerConfig] = (),
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1136:                mcp_servers=mcp_servers,
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1449:        mcp_servers: Sequence[CraftMCPServerConfig] = (),
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1518:            mcp_servers=mcp_servers,
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1546:        mcp_servers: Sequence[CraftMCPServerConfig] = (),
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1566:                    mcp_servers=mcp_servers,
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:110:    CraftMCPServerConfig,
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1379:        mcp_servers: Sequence[CraftMCPServerConfig] = (),
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1420:                mcp_servers=mcp_servers,
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1794:        mcp_servers: Sequence[CraftMCPServerConfig] = (),
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1851:                mcp_servers=mcp_servers,
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1896:        mcp_servers: Sequence[CraftMCPServerConfig] = (),
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1920:                    mcp_servers=mcp_servers,
HEAD:backend/onyx/server/features/build/sandbox/models.py:34:class CraftMCPServerConfig(BaseModel):
HEAD:backend/onyx/server/features/build/sandbox/models.py:35:    """A craft-enabled MCP server resolved for opencode `mcp` emission (URL only;
HEAD:backend/onyx/server/features/build/sandbox/models.py:38:    ``server_id`` is not emitted into ``opencode.json``; it feeds the per-session
HEAD:backend/onyx/server/features/build/sandbox/models.py:44:    server_id: int
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:1:"""Resolve craft-enabled MCP servers into opencode `mcp` config input."""
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:14:    get_craft_enabled_mcp_servers,
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:18:from onyx.db.models import MCPServer, User
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:19:from onyx.server.features.build.sandbox.models import CraftMCPServerConfig
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:28:def _server_key(server: MCPServer) -> str:
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:35:def resolve_craft_mcp_servers(
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:37:) -> list[CraftMCPServerConfig]:
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:38:    """Craft-enabled MCP servers ``user`` may use, as opencode config input.
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:47:    accessible = get_craft_enabled_mcp_servers(db_session, user)
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:51:    servers: list[MCPServer] = []
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:59:                "craft_mcp_skip_unauthenticated server_id=%s name=%r",
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:65:        if tool.mcp_server_id is not None and not tool.enabled:
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:66:            disabled_by_server[tool.mcp_server_id].append(tool.name)
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:68:        CraftMCPServerConfig(
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:72:            server_id=server.id,
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:78:def craft_mcp_fingerprint(mcp_servers: Sequence[CraftMCPServerConfig]) -> str:
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:82:    ``resolve_craft_mcp_servers`` omits what it can't authenticate.
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:86:            s.server_id,
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:90:        for s in mcp_servers
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:6:catalog + default model AND the craft MCP servers, both of which opencode
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:18:    CraftMCPServerConfig,
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:105:    mcp_servers: Sequence[CraftMCPServerConfig] = (),
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:119:    for server in mcp_servers:
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:127:    mcp_servers: Sequence[CraftMCPServerConfig],
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:151:        for server in mcp_servers
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:205:    Providers and craft MCP servers are NOT emitted here — they live in the
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:223:    mcp_servers: Sequence[CraftMCPServerConfig] = (),
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:227:    model, plus the craft MCP servers (session-tagged) and their per-tool
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:246:        "permission": _build_permissions(disabled_tools, dev_mode, mcp_servers),
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:250:    if mcp_servers:
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:252:            raise ValueError("session_id is required when mcp_servers are provided")
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:253:        config["mcp"] = _build_session_mcp_block(mcp_servers, session_id)
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:35:from onyx.db.mcp import get_craft_enabled_mcp_servers
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:126:    pre_approved_mcp_server_ids: list[int] = Field(default_factory=list)
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:144:    pre_approved_mcp_server_ids: list[int] | None = None
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:216:    pre_approved_mcp_server_ids: list[int]
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:305:        pre_approved_mcp_server_ids=task.pre_approved_mcp_server_ids,
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:328:def _validate_mcp_server_ids(
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:331:    server_ids: list[int],
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:332:    already_approved_server_ids: AbstractSet[int] = frozenset(),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:334:    """Reject new MCP server ids unavailable to this user in Craft.
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:339:    if not server_ids:
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:342:        server.id for server in get_craft_enabled_mcp_servers(db_session, user)
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:345:        set(server_ids) - available_ids - already_approved_server_ids
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:350:            f"Unknown or unavailable Craft MCP server id(s): {unavailable_ids}",
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:425:    _validate_mcp_server_ids(db_session, user, request.pre_approved_mcp_server_ids)
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:436:        pre_approved_mcp_server_ids=request.pre_approved_mcp_server_ids,
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:491:    if request.pre_approved_mcp_server_ids is not None:
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:497:        _validate_mcp_server_ids(
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:500:            request.pre_approved_mcp_server_ids,
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:501:            already_approved_server_ids=set(existing_task.pre_approved_mcp_server_ids),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:514:        pre_approved_mcp_server_ids=request.pre_approved_mcp_server_ids,
HEAD:backend/onyx/server/features/build/session/manager.py:79:    resolve_craft_mcp_servers,
HEAD:backend/onyx/server/features/build/session/manager.py:287:        mcp_servers = resolve_craft_mcp_servers(self._db_session, user)
HEAD:backend/onyx/server/features/build/session/manager.py:292:                mcp_servers=mcp_servers,
HEAD:backend/onyx/server/features/build/session/manager.py:351:            mcp_servers=mcp_servers,
HEAD:backend/onyx/server/features/build/session/manager.py:401:                    mcp_servers = resolve_craft_mcp_servers(self._db_session, user)
HEAD:backend/onyx/server/features/build/session/manager.py:416:                        mcp_servers=mcp_servers,
HEAD:backend/onyx/server/features/build/session/manager.py:688:            mcp_servers = resolve_craft_mcp_servers(self._db_session, user)
HEAD:backend/onyx/server/features/build/session/manager.py:708:                mcp_servers=mcp_servers,
HEAD:backend/onyx/server/features/build/session/sandbox_lifecycle.py:72:    resolve_craft_mcp_servers,
HEAD:backend/onyx/server/features/build/session/sandbox_lifecycle.py:229:            resolve_craft_mcp_servers(db_session, user)
HEAD:backend/onyx/server/features/build/session/sandbox_lifecycle.py:1011:                resolve_craft_mcp_servers(db_session, user)
HEAD:backend/onyx/server/features/build/session/session_ready.py:32:    resolve_craft_mcp_servers,
HEAD:backend/onyx/server/features/build/session/session_ready.py:121:    mcp_servers = resolve_craft_mcp_servers(db_session, user)
HEAD:backend/onyx/server/features/build/session/session_ready.py:144:                mcp_servers=mcp_servers,
HEAD:backend/onyx/server/features/build/session/session_ready.py:153:                mcp_servers=mcp_servers,
HEAD:backend/onyx/server/features/mcp/api.py:20:from onyx.auth.permission_projection import mcp_server_permissions, tool_permissions
HEAD:backend/onyx/server/features/mcp/api.py:35:    MCPServerStatus,
HEAD:backend/onyx/server/features/mcp/api.py:46:    affected_user_ids_for_mcp_server,
HEAD:backend/onyx/server/features/mcp/api.py:48:    create_mcp_server__no_commit,
HEAD:backend/onyx/server/features/mcp/api.py:51:    delete_mcp_server,
HEAD:backend/onyx/server/features/mcp/api.py:53:    get_all_mcp_servers,
HEAD:backend/onyx/server/features/mcp/api.py:55:    get_craft_enabled_mcp_servers,
HEAD:backend/onyx/server/features/mcp/api.py:56:    get_mcp_server_by_id,
HEAD:backend/onyx/server/features/mcp/api.py:57:    get_mcp_servers_accessible_to_user,
HEAD:backend/onyx/server/features/mcp/api.py:58:    get_mcp_servers_for_persona,
HEAD:backend/onyx/server/features/mcp/api.py:63:    update_mcp_server__no_commit,
HEAD:backend/onyx/server/features/mcp/api.py:65:    user_can_access_mcp_server,
HEAD:backend/onyx/server/features/mcp/api.py:68:from onyx.db.models import MCPServer as DbMCPServer
HEAD:backend/onyx/server/features/mcp/api.py:70:    can_manage_mcp_server,
HEAD:backend/onyx/server/features/mcp/api.py:74:    get_mcp_server_ids_connected_to_groups,
HEAD:backend/onyx/server/features/mcp/api.py:75:    get_tools_by_mcp_server_id,
HEAD:backend/onyx/server/features/mcp/api.py:101:    MCPServer,
HEAD:backend/onyx/server/features/mcp/api.py:102:    MCPServerCreateResponse,
HEAD:backend/onyx/server/features/mcp/api.py:103:    MCPServerSimpleCreateRequest,
HEAD:backend/onyx/server/features/mcp/api.py:104:    MCPServerSimpleUpdateRequest,
HEAD:backend/onyx/server/features/mcp/api.py:105:    MCPServersResponse,
HEAD:backend/onyx/server/features/mcp/api.py:106:    MCPServerUpdateResponse,
HEAD:backend/onyx/server/features/mcp/api.py:157:    " To reach a private-network MCP server, set SSRF Protection to Allow Private "
HEAD:backend/onyx/server/features/mcp/api.py:162:    " To reach a loopback MCP server, set SSRF Protection to Disabled in the admin "
HEAD:backend/onyx/server/features/mcp/api.py:195:def _validate_mcp_server_url(
HEAD:backend/onyx/server/features/mcp/api.py:481:            "OAuth client_id changed for existing MCP server; discarding "
HEAD:backend/onyx/server/features/mcp/api.py:494:    # Heal stale records that were seeded before `_upsert_mcp_server` always
HEAD:backend/onyx/server/features/mcp/api.py:523:    mcp_server: DbMCPServer,
HEAD:backend/onyx/server/features/mcp/api.py:527:    if mcp_server.admin_connection_config_id is not None:
HEAD:backend/onyx/server/features/mcp/api.py:529:            mcp_server.admin_connection_config_id, db_session, config_data
HEAD:backend/onyx/server/features/mcp/api.py:531:        return mcp_server.admin_connection_config_id
HEAD:backend/onyx/server/features/mcp/api.py:534:        mcp_server_id=mcp_server.id,
HEAD:backend/onyx/server/features/mcp/api.py:541:    mcp_server: DbMCPServer,
HEAD:backend/onyx/server/features/mcp/api.py:547:    existing = get_user_connection_config(mcp_server.id, user_email, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:560:        server_id=mcp_server.id,
HEAD:backend/onyx/server/features/mcp/api.py:595:def test_mcp_server_credentials(
HEAD:backend/onyx/server/features/mcp/api.py:601:    """Test if credentials work by calling the MCP server's tools/list endpoint"""
HEAD:backend/onyx/server/features/mcp/api.py:616:        logger.error("Failed to test MCP server credentials: %s", e)
HEAD:backend/onyx/server/features/mcp/api.py:628:    """Connect OAuth flow for admin MCP server authentication"""
HEAD:backend/onyx/server/features/mcp/api.py:647:    """Connect OAuth flow for per-user MCP server authentication"""
HEAD:backend/onyx/server/features/mcp/api.py:649:    logger.info("Initiating per-user OAuth for server: %s", request.server_id)
HEAD:backend/onyx/server/features/mcp/api.py:651:    server_id = request.server_id
HEAD:backend/onyx/server/features/mcp/api.py:653:        mcp_server = get_mcp_server_by_id(server_id, db)
HEAD:backend/onyx/server/features/mcp/api.py:655:        raise OnyxError(OnyxErrorCode.NOT_FOUND, "MCP server not found") from error
HEAD:backend/onyx/server/features/mcp/api.py:658:        _ensure_mcp_server_owner_or_admin(mcp_server, user)
HEAD:backend/onyx/server/features/mcp/api.py:659:    elif not user_can_access_mcp_server(user, server_id, db):
HEAD:backend/onyx/server/features/mcp/api.py:662:            "You do not have access to this MCP server.",
HEAD:backend/onyx/server/features/mcp/api.py:665:    if mcp_server.auth_type != MCPAuthenticationType.OAUTH:
HEAD:backend/onyx/server/features/mcp/api.py:666:        auth_type_str = mcp_server.auth_type.value if mcp_server.auth_type else "None"
HEAD:backend/onyx/server/features/mcp/api.py:671:    if mcp_server.auth_performer != MCPAuthenticationPerformer.PER_USER:
HEAD:backend/onyx/server/features/mcp/api.py:674:            "OAuth MCP servers must use per-user authentication.",
HEAD:backend/onyx/server/features/mcp/api.py:681:    if mcp_server.admin_connection_config:
HEAD:backend/onyx/server/features/mcp/api.py:683:            mcp_server.admin_connection_config, apply_mask=False
HEAD:backend/onyx/server/features/mcp/api.py:708:            auth_template=get_mcp_auth_template(mcp_server),
HEAD:backend/onyx/server/features/mcp/api.py:714:            auth_template=get_mcp_auth_template(mcp_server),
HEAD:backend/onyx/server/features/mcp/api.py:718:    if mcp_server.admin_connection_config_id is None:
HEAD:backend/onyx/server/features/mcp/api.py:727:            mcp_server_id=mcp_server.id,
HEAD:backend/onyx/server/features/mcp/api.py:731:        mcp_server.admin_connection_config = admin_config
HEAD:backend/onyx/server/features/mcp/api.py:732:        mcp_server.admin_connection_config_id = (
HEAD:backend/onyx/server/features/mcp/api.py:736:        update_connection_config(mcp_server.admin_connection_config_id, db, config_data)
HEAD:backend/onyx/server/features/mcp/api.py:738:    connection_config = get_user_connection_config(mcp_server.id, user.email, db)
HEAD:backend/onyx/server/features/mcp/api.py:749:            mcp_server,
HEAD:backend/onyx/server/features/mcp/api.py:752:            user_configs={mcp_server.id: connection_config},
HEAD:backend/onyx/server/features/mcp/api.py:755:    auth_template = get_mcp_auth_template(mcp_server)
HEAD:backend/onyx/server/features/mcp/api.py:791:            mcp_server_id=mcp_server.id,
HEAD:backend/onyx/server/features/mcp/api.py:804:    if mcp_server.oauth_provider_mode == MCPOAuthProviderMode.KNOWN_PROVIDER:
HEAD:backend/onyx/server/features/mcp/api.py:822:                server_id=server_id,
HEAD:backend/onyx/server/features/mcp/api.py:829:            mcp_server=mcp_server,
HEAD:backend/onyx/server/features/mcp/api.py:838:            server_id=int(request.server_id),
HEAD:backend/onyx/server/features/mcp/api.py:844:    if mcp_server.transport is None:
HEAD:backend/onyx/server/features/mcp/api.py:847:            "MCP server transport is not configured",
HEAD:backend/onyx/server/features/mcp/api.py:852:            mcp_server=mcp_server,
HEAD:backend/onyx/server/features/mcp/api.py:856:            shared_client_config_id=mcp_server.admin_connection_config_id,
HEAD:backend/onyx/server/features/mcp/api.py:858:            transport=mcp_server.transport,
HEAD:backend/onyx/server/features/mcp/api.py:880:        server_id=int(request.server_id),
HEAD:backend/onyx/server/features/mcp/api.py:913:        "OAuth callback: claimed flow for user_id=%s tenant=%s server_id=%s",
HEAD:backend/onyx/server/features/mcp/api.py:916:        flow.server_id,
HEAD:backend/onyx/server/features/mcp/api.py:926:        mcp_server = get_mcp_server_by_id(flow.server_id, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:928:        raise OnyxError(OnyxErrorCode.NOT_FOUND, "MCP server not found") from error
HEAD:backend/onyx/server/features/mcp/api.py:930:    if not user_can_access_mcp_server(
HEAD:backend/onyx/server/features/mcp/api.py:931:        user, mcp_server.id, db_session
HEAD:backend/onyx/server/features/mcp/api.py:932:    ) and not can_manage_mcp_server(user, mcp_server):
HEAD:backend/onyx/server/features/mcp/api.py:935:            "You no longer have access to or management authority for this MCP server.",
HEAD:backend/onyx/server/features/mcp/api.py:938:    user_config = get_user_connection_config(mcp_server.id, user.email, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:948:        mcp_server,
HEAD:backend/onyx/server/features/mcp/api.py:972:        mcp_server,
HEAD:backend/onyx/server/features/mcp/api.py:983:        "server_id=%s server_name=%s return_path=%s",
HEAD:backend/onyx/server/features/mcp/api.py:984:        str(mcp_server.id),
HEAD:backend/onyx/server/features/mcp/api.py:985:        mcp_server.name,
HEAD:backend/onyx/server/features/mcp/api.py:991:        server_id=mcp_server.id,
HEAD:backend/onyx/server/features/mcp/api.py:992:        server_name=mcp_server.name,
HEAD:backend/onyx/server/features/mcp/api.py:993:        message=f"OAuth authorization completed successfully for {mcp_server.name}",
HEAD:backend/onyx/server/features/mcp/api.py:1005:        mcp_server = get_mcp_server_by_id(request.server_id, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:1007:        raise OnyxError(OnyxErrorCode.NOT_FOUND, "MCP server not found")
HEAD:backend/onyx/server/features/mcp/api.py:1009:    server_id = mcp_server.id
HEAD:backend/onyx/server/features/mcp/api.py:1011:    template = get_mcp_auth_template(mcp_server)
HEAD:backend/onyx/server/features/mcp/api.py:1014:            mcp_server.auth_type != MCPAuthenticationType.API_TOKEN
HEAD:backend/onyx/server/features/mcp/api.py:1019:                "This MCP server has no user-configurable header template.",
HEAD:backend/onyx/server/features/mcp/api.py:1037:    if mcp_server.auth_type == MCPAuthenticationType.OAUTH:
HEAD:backend/onyx/server/features/mcp/api.py:1038:        existing_config = get_user_connection_config(server_id, email, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:1039:        source_config = existing_config or mcp_server.admin_connection_config
HEAD:backend/onyx/server/features/mcp/api.py:1050:    if mcp_server.auth_type != MCPAuthenticationType.OAUTH:
HEAD:backend/onyx/server/features/mcp/api.py:1052:        if mcp_server.auth_type == MCPAuthenticationType.PT_OAUTH:
HEAD:backend/onyx/server/features/mcp/api.py:1062:        is_valid, test_message = test_mcp_server_credentials(
HEAD:backend/onyx/server/features/mcp/api.py:1063:            mcp_server.server_url,
HEAD:backend/onyx/server/features/mcp/api.py:1079:        server_id=server_id,
HEAD:backend/onyx/server/features/mcp/api.py:1087:    resolved = resolve_mcp_credentials(mcp_server, user, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:1091:        server_id=request.server_id,
HEAD:backend/onyx/server/features/mcp/api.py:1092:        server_name=mcp_server.name,
HEAD:backend/onyx/server/features/mcp/api.py:1098:@router.delete("/user-credentials/{server_id}")
HEAD:backend/onyx/server/features/mcp/api.py:1100:    server_id: int,
HEAD:backend/onyx/server/features/mcp/api.py:1104:    """Disconnect the caller from an MCP server: remove their own connection
HEAD:backend/onyx/server/features/mcp/api.py:1107:        mcp_server = get_mcp_server_by_id(server_id, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:1109:        raise OnyxError(OnyxErrorCode.NOT_FOUND, "MCP server not found")
HEAD:backend/onyx/server/features/mcp/api.py:1112:    delete_user_connection_configs_for_server(server_id, user.email, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:1121:        server_id=server_id,
HEAD:backend/onyx/server/features/mcp/api.py:1122:        server_name=mcp_server.name,
HEAD:backend/onyx/server/features/mcp/api.py:1135:    server_id: int
HEAD:backend/onyx/server/features/mcp/api.py:1141:def _ensure_mcp_server_owner_or_admin(server: DbMCPServer, user: User) -> None:
HEAD:backend/onyx/server/features/mcp/api.py:1142:    """GATE 2 for every MCP server mutation. Delegates to the predicate the projection
HEAD:backend/onyx/server/features/mcp/api.py:1145:    if can_manage_mcp_server(user, server):
HEAD:backend/onyx/server/features/mcp/api.py:1148:        "Denied MCP server management: user=%s server=%s owner=%s",
HEAD:backend/onyx/server/features/mcp/api.py:1155:        "Only the server owner can modify MCP servers they have created.",
HEAD:backend/onyx/server/features/mcp/api.py:1159:def _ensure_mcp_server_viewable(
HEAD:backend/onyx/server/features/mcp/api.py:1160:    server: DbMCPServer, user: User, db_session: Session
HEAD:backend/onyx/server/features/mcp/api.py:1162:    """Read gate for a single MCP server: a global MANAGE_ACTIONS holder (incl. admins) views
HEAD:backend/onyx/server/features/mcp/api.py:1165:    owner-or-admin (``_ensure_mcp_server_owner_or_admin``)."""
HEAD:backend/onyx/server/features/mcp/api.py:1173:        if server.id in get_mcp_server_ids_connected_to_groups(managed, db_session):
```
MCP server records, user/group relationships and configuration form a
capability-authorization surface.
## MCP Tool Discovery
Evidence lines: 184
```text
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:135:                "mcp tools are not supported by the Onyx gateway.",
HEAD:backend/onyx/auth/permissions.py:180:        description="Add and update custom tools and MCP/OpenAPI actions.",
HEAD:backend/onyx/auth/users.py:2161:    PT_OAUTH MCP tools and any custom HTTP tool with bearer pass-through forward
HEAD:backend/onyx/chat/chat_utils.py:244:    prefetch_top_two_level_tool_calls: bool = True,
HEAD:backend/onyx/chat/chat_utils.py:257:        prefetch_top_two_level_tool_calls=prefetch_top_two_level_tool_calls,
HEAD:backend/onyx/chat/compression.py:406:    ``prefetch_top_two_level_tool_calls=True``); ``_build_llm_messages_for_summarization``
HEAD:backend/onyx/configs/app_configs.py:1689:# Per-call MCP read timeout; configurable since some tools (e.g. data-agent
HEAD:backend/onyx/configs/app_configs.py:1692:    os.environ.get("MCP_TOOL_CALL_TIMEOUT_SECONDS") or 300
HEAD:backend/onyx/db/chat.py:598:    prefetch_top_two_level_tool_calls: bool = True,
HEAD:backend/onyx/db/chat.py:621:    if prefetch_top_two_level_tool_calls:
HEAD:backend/onyx/db/enums.py:205:    FETCHING_TOOLS = "FETCHING_TOOLS"  # Auth complete, fetching tools
HEAD:backend/onyx/db/llm.py:629:def fetch_existing_tools(db_session: Session, tool_ids: list[int]) -> list[ToolModel]:
HEAD:backend/onyx/db/mcp.py:93:    # Collect unique MCP server IDs from the persona's tools
HEAD:backend/onyx/db/mcp.py:312:    """Delete an MCP server and all associated tools (via CASCADE)"""
HEAD:backend/onyx/db/mcp.py:316:    tools_count = db_session.query(Tool).filter(Tool.mcp_server_id == server_id).count()
HEAD:backend/onyx/db/mcp.py:318:        "Deleting MCP server %s with %s associated tools", server_id, tools_count
HEAD:backend/onyx/db/mcp.py:324:    logger.info("Successfully deleted MCP server %s and its tools", server_id)
HEAD:backend/onyx/db/mcp.py:327:def get_all_mcp_tools_for_server(server_id: int, db_session: Session) -> list[Tool]:
HEAD:backend/onyx/db/mcp.py:328:    """Get all MCP tools for a server"""
HEAD:backend/onyx/db/mcp.py:334:def get_mcp_tools_for_servers(server_ids: list[int], db_session: Session) -> list[Tool]:
HEAD:backend/onyx/db/mcp.py:335:    """All MCP tools across ``server_ids`` in a single query"""
HEAD:backend/onyx/db/models.py:4031:    # MCP tool input schema. Only applies to MCP tools.
HEAD:backend/onyx/db/models.py:4044:    # MCP server this tool is associated with (null for non-MCP tools)
HEAD:backend/onyx/db/models.py:7415:    display (name/description) comes from the code catalog / discovered tools.
HEAD:backend/onyx/db/persona.py:1621:    # Fetch and attach tools by IDs
HEAD:backend/onyx/db/tools.py:44:        # 1. Don't have an MCP server (mcp_server_id IS NULL) - Non-MCP tools
HEAD:backend/onyx/db/tools.py:45:        # 2. Have an MCP server that is connected - Connected MCP tools
HEAD:backend/onyx/db/tools.py:48:                Tool.mcp_server_id.is_(None),  # Non-MCP tools (built-in, custom)
HEAD:backend/onyx/db/tools.py:49:                MCPServer.status == MCPServerStatus.CONNECTED,  # MCP tools connected
HEAD:backend/onyx/db/tools.py:60:            # tools from mcp servers will not have an openapi schema but it has `null`, so we need to exclude them.
HEAD:backend/onyx/db/tools.py:69:def get_tools_by_mcp_server_id(
HEAD:backend/onyx/mcp_server/api.py:40:# Import tools and resources AFTER mcp_server is created to avoid circular imports
HEAD:backend/onyx/mcp_server/api.py:43:from onyx.mcp_server.tools import search  # noqa: E402, F401
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:19:        "This can be used to discover filters for the `search_indexed_documents` tool."
HEAD:backend/onyx/mcp_server/tools/__init__.py:4:from onyx.mcp_server.tools import search  # noqa: F401
HEAD:backend/onyx/mcp_server/tools/search.py:1:"""Search tools for MCP server - document and web search."""
HEAD:backend/onyx/mcp_server/tools/search.py:35:from onyx.server.metrics.mcp_common import MCPToolCallStatus
HEAD:backend/onyx/mcp_server/tools/search.py:71:    Renames ``link`` → ``url`` to match the conventional shape MCP tools
HEAD:backend/onyx/mcp_server/tools/search.py:72:    typically emit (most search-style MCP tools — Brave, Exa, etc. — use
HEAD:backend/onyx/mcp_server/tools/search.py:354:    outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/mcp_server/tools/search.py:369:            outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/mcp_server/tools/search.py:401:        outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/mcp_server/tools/search.py:441:    outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/mcp_server/tools/search.py:457:        outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/mcp_server/tools/search.py:501:    outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/mcp_server/tools/search.py:512:        outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/prompts/deep_research/orchestration_layer.py:161:There are cases where new discoveries from research may lead to a deviation from the original research plan. In these cases, ensure that the new directions are thoroughly investigated prior to calling {GENERATE_REPORT_TOOL_NAME}.
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:28:        "tools/list",
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:52:# MCP tools default to ASK; a server's self-declared `readOnlyHint` never
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:264:            policy=stored.get(tool_name, MCP_TOOL_DEFAULT_POLICY),
HEAD:backend/onyx/server/features/build/sandbox/README.md:15:- **OpenCode agent** - AI coding agent with access to tools and MCP servers
HEAD:backend/onyx/server/features/build/sandbox/image/opencode-plugins/turn-budget.ts:71:      // Built-in tools render `.output`; MCP results are rebuilt from
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:15:    get_mcp_tools_for_servers,
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:64:    for tool in get_mcp_tools_for_servers([s.id for s in servers], db_session):
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:246:        "permission": _build_permissions(disabled_tools, dev_mode, mcp_servers),
HEAD:backend/onyx/server/features/mcp/api.py:54:    get_all_mcp_tools_for_server,
HEAD:backend/onyx/server/features/mcp/api.py:75:    get_tools_by_mcp_server_id,
HEAD:backend/onyx/server/features/mcp/api.py:80:    discover_mcp_tools,
HEAD:backend/onyx/server/features/mcp/api.py:107:    MCPToolCreateRequest,
HEAD:backend/onyx/server/features/mcp/api.py:108:    MCPToolListResponse,
HEAD:backend/onyx/server/features/mcp/api.py:109:    MCPToolUpdateRequest,
HEAD:backend/onyx/server/features/mcp/api.py:601:    """Test if credentials work by calling the MCP server's tools/list endpoint"""
HEAD:backend/onyx/server/features/mcp/api.py:603:        # Attempt to discover tools using the provided credentials
HEAD:backend/onyx/server/features/mcp/api.py:604:        tools = discover_mcp_tools(
HEAD:backend/onyx/server/features/mcp/api.py:1127:class MCPToolDescription(BaseModel):
HEAD:backend/onyx/server/features/mcp/api.py:1138:    tools: list[MCPToolDescription]
HEAD:backend/onyx/server/features/mcp/api.py:1398:def admin_list_mcp_tools_by_id(
HEAD:backend/onyx/server/features/mcp/api.py:1404:) -> MCPToolListResponse:
HEAD:backend/onyx/server/features/mcp/api.py:1405:    return _list_mcp_tools_by_id(server_id, db, True, user)
HEAD:backend/onyx/server/features/mcp/api.py:1414:def get_mcp_server_tools_snapshots(
HEAD:backend/onyx/server/features/mcp/api.py:1423:    Get tools for an MCP server as ToolSnapshot objects.
HEAD:backend/onyx/server/features/mcp/api.py:1430:    from onyx.db.tools import get_tools_by_mcp_server_id
HEAD:backend/onyx/server/features/mcp/api.py:1438:    if source == ToolSnapshotSource.MCP:
HEAD:backend/onyx/server/features/mcp/api.py:1441:            # Discover tools from MCP server and sync to DB
HEAD:backend/onyx/server/features/mcp/api.py:1442:            _list_mcp_tools_by_id(server_id, db, True, user)
HEAD:backend/onyx/server/features/mcp/api.py:1444:            # Successfully discovered tools, update status to CONNECTED
HEAD:backend/onyx/server/features/mcp/api.py:1464:            logger.error("Failed to discover tools for MCP server: %s", e)
HEAD:backend/onyx/server/features/mcp/api.py:1465:            raise HTTPException(status_code=500, detail="Failed to discover tools")
HEAD:backend/onyx/server/features/mcp/api.py:1470:    mcp_tools = get_tools_by_mcp_server_id(server_id, db, order_by_id=True)
HEAD:backend/onyx/server/features/mcp/api.py:1476:        for tool in mcp_tools
HEAD:backend/onyx/server/features/mcp/api.py:1481:def user_list_mcp_tools_by_id(
HEAD:backend/onyx/server/features/mcp/api.py:1485:) -> MCPToolListResponse:
HEAD:backend/onyx/server/features/mcp/api.py:1486:    return _list_mcp_tools_by_id(server_id, db, False, user)
HEAD:backend/onyx/server/features/mcp/api.py:1490:    discovered_tools: list[MCPLibTool],
HEAD:backend/onyx/server/features/mcp/api.py:1496:    for tool in discovered_tools:
HEAD:backend/onyx/server/features/mcp/api.py:1530:def _sync_mcp_server_tools(
HEAD:backend/onyx/server/features/mcp/api.py:1532:    discovered_tools: list[MCPLibTool],
HEAD:backend/onyx/server/features/mcp/api.py:1535:    """Make the stored tools for the server match the discovered tools.
HEAD:backend/onyx/server/features/mcp/api.py:1546:    for db_tool in get_tools_by_mcp_server_id(mcp_server_id, db, order_by_id=True):
HEAD:backend/onyx/server/features/mcp/api.py:1555:        discovered_tools, existing_by_name, processed_names, mcp_server_id, db
HEAD:backend/onyx/server/features/mcp/api.py:1565:def _list_mcp_tools_by_id(
HEAD:backend/onyx/server/features/mcp/api.py:1570:) -> MCPToolListResponse:
HEAD:backend/onyx/server/features/mcp/api.py:1571:    """List available tools from an existing MCP server"""
HEAD:backend/onyx/server/features/mcp/api.py:1572:    logger.info("Listing tools for MCP server: %s", server_id)
HEAD:backend/onyx/server/features/mcp/api.py:1610:    logger.info("Discovering tools for MCP server: %s: %s", mcp_server.name, t1)
HEAD:backend/onyx/server/features/mcp/api.py:1620:        discovered_tools = discover_mcp_tools(
HEAD:backend/onyx/server/features/mcp/api.py:1629:        "Discovered %s tools for MCP server: %s: %s",
HEAD:backend/onyx/server/features/mcp/api.py:1630:        len(discovered_tools),
HEAD:backend/onyx/server/features/mcp/api.py:1642:        _sync_mcp_server_tools(mcp_server.id, discovered_tools, db)
HEAD:backend/onyx/server/features/mcp/api.py:1645:    for tool in discovered_tools:
HEAD:backend/onyx/server/features/mcp/api.py:1652:    return MCPToolListResponse(
HEAD:backend/onyx/server/features/mcp/api.py:1656:        tools=discovered_tools,
HEAD:backend/onyx/server/features/mcp/api.py:1711:    request: MCPToolCreateRequest,
HEAD:backend/onyx/server/features/mcp/api.py:2149:    """Toggle enabled state for MCP tools that exist for the server.
HEAD:backend/onyx/server/features/mcp/api.py:2158:    existing_tools = get_tools_by_mcp_server_id(mcp_server.id, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:2204:def get_all_mcp_tools(
HEAD:backend/onyx/server/features/mcp/api.py:2210:    """Get all tools associated with MCP servers, including both enabled and disabled tools"""
HEAD:backend/onyx/server/features/mcp/api.py:2213:    # Query MCP tools ordered by ID to maintain consistent ordering
HEAD:backend/onyx/server/features/mcp/api.py:2232:    mcp_tools = db.scalars(stmt).all()
HEAD:backend/onyx/server/features/mcp/api.py:2235:    return [ToolSnapshot.from_model(tool) for tool in mcp_tools]
HEAD:backend/onyx/server/features/mcp/api.py:2320:def get_mcp_server_db_tools(
HEAD:backend/onyx/server/features/mcp/api.py:2327:    """Get existing database tools created for an MCP server"""
HEAD:backend/onyx/server/features/mcp/api.py:2328:    logger.info("Getting database tools for MCP server: %s", server_id)
HEAD:backend/onyx/server/features/mcp/api.py:2338:    # Get all tools associated with this MCP server
HEAD:backend/onyx/server/features/mcp/api.py:2339:    mcp_tools = get_tools_by_mcp_server_id(server_id, db)
HEAD:backend/onyx/server/features/mcp/api.py:2343:    for tool in mcp_tools:
HEAD:backend/onyx/server/features/mcp/api.py:2350:            MCPToolDescription(
HEAD:backend/onyx/server/features/mcp/api.py:2368:    request: MCPToolCreateRequest,
HEAD:backend/onyx/server/features/mcp/api.py:2374:    """Create or update an MCP server (no tools yet)"""
HEAD:backend/onyx/server/features/mcp/api.py:2442:def update_mcp_server_with_tools(
HEAD:backend/onyx/server/features/mcp/api.py:2443:    request: MCPToolUpdateRequest,
HEAD:backend/onyx/server/features/mcp/api.py:2449:    """Update an MCP server and associated tools"""
HEAD:backend/onyx/server/features/mcp/api.py:2611:        known = {t.name for t in get_all_mcp_tools_for_server(server_id, db_session)}
HEAD:backend/onyx/server/features/mcp/api.py:2659:    """Delete an MCP server and cascading related objects (tools, configs)."""
HEAD:backend/onyx/server/features/mcp/api.py:2675:        tools_to_delete = get_tools_by_mcp_server_id(server_id, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:2677:            "Deleting MCP server %s (%s) with %s tools",
HEAD:backend/onyx/server/features/mcp/api.py:2689:        remaining_tools = get_tools_by_mcp_server_id(server_id, db_session)
HEAD:backend/onyx/server/features/mcp/api.py:2692:                "WARNING: %s tools still exist after deleting MCP server %s",
HEAD:backend/onyx/server/features/mcp/client.py:288:async def _discover_mcp_tools(session: ClientSession) -> list[MCPLibTool]:
HEAD:backend/onyx/server/features/mcp/client.py:296:    # 2) tools/list
HEAD:backend/onyx/server/features/mcp/client.py:298:    tools_response = await session.list_tools()  # sends JSON-RPC "tools/list"
HEAD:backend/onyx/server/features/mcp/client.py:303:def discover_mcp_tools(
HEAD:backend/onyx/server/features/mcp/client.py:310:    Synchronous wrapper for discovering MCP tools.
HEAD:backend/onyx/server/features/mcp/client.py:313:        _discover_mcp_tools,
HEAD:backend/onyx/server/features/mcp/models.py:206:class MCPToolCreateRequest(BaseModel):
HEAD:backend/onyx/server/features/mcp/models.py:309:    def validate_auth_configuration(self) -> "MCPToolCreateRequest":
HEAD:backend/onyx/server/features/mcp/models.py:408:class MCPToolUpdateRequest(BaseModel):
HEAD:backend/onyx/server/features/mcp/models.py:478:class MCPToolResponse(BaseModel):
HEAD:backend/onyx/server/features/mcp/models.py:483:    definition: Optional[dict] = None  # MCP tools don't use OpenAPI definitions
HEAD:backend/onyx/server/features/mcp/models.py:747:    """Response for creating multiple MCP tools"""
HEAD:backend/onyx/server/features/mcp/models.py:765:    """Response for updating multiple MCP tools"""
HEAD:backend/onyx/server/features/mcp/models.py:772:class MCPToolListResponse(BaseModel):
HEAD:backend/onyx/server/features/mcp/models.py:776:    tools: list[MCPLibTool]
HEAD:backend/onyx/server/features/mcp/oauth.py:3:Used by chat tool calls (`MCPTool.run`), the admin/user MCP API routes, and the
HEAD:backend/onyx/server/features/tool/api.py:102:    """Fetch a custom tool and assert the caller may manage it (owner or admin) — the gate for
HEAD:backend/onyx/server/features/tool/api.py:372:def list_tools(
HEAD:backend/onyx/server/features/tool/api.py:376:    tools = get_tools(db_session, only_enabled=True, only_connected_mcp=True)
HEAD:backend/onyx/server/features/tool/api.py:378:    # Attach catalog: omit MCP tools the user cannot put on a persona.
HEAD:backend/onyx/server/metrics/mcp_client.py:5:from onyx.server.metrics.mcp_common import MCPToolCallStatus
HEAD:backend/onyx/server/metrics/mcp_client.py:27:    status: MCPToolCallStatus,
HEAD:backend/onyx/server/metrics/mcp_common.py:4:class MCPToolCallStatus(str, Enum):
HEAD:backend/onyx/server/metrics/mcp_server.py:6:from onyx.server.metrics.mcp_common import MCPToolCallStatus
HEAD:backend/onyx/server/metrics/mcp_server.py:45:    "Results returned by MCP server search tools",
HEAD:backend/onyx/server/metrics/mcp_server.py:66:    status: MCPToolCallStatus,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:418:        prefetch_top_two_level_tool_calls=True,
HEAD:backend/onyx/server/security/models.py:67:    """Whether LLM-initiated outbound fetches (e.g. the ``open_url`` tool) may
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:13:> **Onyx Craft:** for basic reads of static pages, prefer the `webfetch` tool — it returns clean markdown, is faster, and is cheaper. Reach for `browser` only when the page needs JavaScript/SPA rendering, interaction (clicks, forms, login), multi-step navigation, or visual inspection.
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:57:browser mcp --tools all
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:58:browser mcp --tools core,network,react
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:61:Configure the MCP client to launch `browser` with `["mcp"]`. The server defaults to MCP protocol 2025-11-25 and accepts older supported client protocol versions during initialization. The default tools profile is `core`, which keeps MCP context small for everyday browser automation. Use `--tools all` for the full typed CLI parity surface, or combine profiles with commas, such as `--tools core,network,react`. Profiles are `core`, `network`, `state`, `debug`, `tabs`, `react`, `mobile`, and `all`; the `debug` profile includes plugin registry and command.run tools. Each tool accepts typed arguments plus `extraArgs` for advanced CLI flags and exact CLI parity. Tool discovery is paginated and includes read-only/open-world annotations so modern MCP clients can load the large typed surface incrementally. Use the tool `session` argument or `AGENT_BROWSER_SESSION` to isolate browser sessions.
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1181:browser mcp --tools all
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1182:browser mcp --tools core,network,react
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1187:The default tools profile is `core`, which keeps MCP context small for everyday browser automation. Use `--tools all` for the full typed CLI parity surface, or combine profiles with commas, such as `--tools core,network,react`.
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1215:Tool calls use the same config files and environment variables as the CLI. Each tool accepts typed arguments plus `extraArgs` for advanced CLI flags and exact CLI parity. Tool discovery is paginated and includes read-only/open-world annotations so modern MCP clients can load the large typed surface incrementally. Use the `session` tool argument or `AGENT_BROWSER_SESSION` to isolate browser state.
HEAD:backend/onyx/skills/builtin/craft-documentation/SKILL.md:14:copies of every page. Fetch those with the `webfetch` tool; there is no need to
HEAD:backend/onyx/tools/tool_constructor.py:16:    get_all_mcp_tools_for_server,
HEAD:backend/onyx/tools/tool_constructor.py:45:from onyx.tools.tool_implementations.mcp.mcp_tool import MCPTool
HEAD:backend/onyx/tools/tool_constructor.py:57:def _disambiguate_mcp_tool_names(tools: list[Tool]) -> None:
HEAD:backend/onyx/tools/tool_constructor.py:60:        if isinstance(tool, MCPTool) and tool_name_counts[tool.name] > 1:
HEAD:backend/onyx/tools/tool_constructor.py:201:    mcp_tool_cache: dict[int, dict[int, MCPTool]] = {}
HEAD:backend/onyx/tools/tool_constructor.py:452:        # Handle MCP tools
HEAD:backend/onyx/tools/tool_constructor.py:460:            mcp_server = get_mcp_server_by_id(db_tool_model.mcp_server_id, db_session)
HEAD:backend/onyx/tools/tool_constructor.py:468:            # Get all saved tools for this MCP server
HEAD:backend/onyx/tools/tool_constructor.py:469:            saved_tools = get_all_mcp_tools_for_server(mcp_server.id, db_session)
HEAD:backend/onyx/tools/tool_constructor.py:482:                # Create MCPTool instance for this specific tool
HEAD:backend/onyx/tools/tool_constructor.py:483:                mcp_tool = MCPTool(
HEAD:backend/onyx/tools/tool_constructor.py:542:    _disambiguate_mcp_tool_names(tools)
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:22:from onyx.server.metrics.mcp_common import MCPToolCallStatus
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:50:# class MCPToolCallSummary(BaseModel):
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:69:class MCPTool(Tool[None]):
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:153:        outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:210:                outcome = MCPToolCallStatus.AUTH_ERROR
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:285:            outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:297:                outcome = MCPToolCallStatus.AUTH_ERROR
```
Tool discovery controls which remote capabilities can become visible to the
application/model.
## MCP Tool Invocation
Evidence lines: 59
```text
HEAD:backend/onyx/configs/app_configs.py:1689:# Per-call MCP read timeout; configurable since some tools (e.g. data-agent
HEAD:backend/onyx/db/mcp.py:219:    auth_performer: MCPAuthenticationPerformer | None,
HEAD:backend/onyx/db/mcp.py:259:    auth_performer: MCPAuthenticationPerformer | None = None,
HEAD:backend/onyx/db/models.py:5833:    auth_performer: Mapped[MCPAuthenticationPerformer | None] = mapped_column(
HEAD:backend/onyx/mcp_server/tools/search.py:72:    typically emit (most search-style MCP tools — Brave, Exa, etc. — use
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:3:Every tool invocation is a JSON-RPC ``tools/call`` carrying the exact tool
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:19:_TOOL_CALL_METHOD = "tools/call"
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:53:    # Tool names of every `tools/call` in the (possibly batched) body, in order.
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:70:    * any message a well-formed ``tools/call`` (string ``params.name``) →
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:72:    * anything else (unknown method, malformed body, a ``tools/call`` missing its
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:155:    * ``tools/call`` → an ``AllMatchedActions`` over the invoked tool(s), each
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:82:        # `tools/call` the evaluator gated is still ours to inject onto.
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:151:            admin_managed = server.auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/api.py:601:    """Test if credentials work by calling the MCP server's tools/list endpoint"""
HEAD:backend/onyx/server/features/mcp/api.py:671:    if mcp_server.auth_performer != MCPAuthenticationPerformer.PER_USER:
HEAD:backend/onyx/server/features/mcp/api.py:1237:            and auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/api.py:1270:            and auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/api.py:1799:            and request.auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/api.py:1836:                and request.auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/api.py:1859:            and request.auth_performer == MCPAuthenticationPerformer.PER_USER
HEAD:backend/onyx/server/features/mcp/api.py:1865:                and request.auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/api.py:1872:            and request.auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/api.py:1878:            and request.auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/api.py:1887:                or request.auth_performer != mcp_server.auth_performer
HEAD:backend/onyx/server/features/mcp/api.py:1892:            or request.auth_performer != mcp_server.auth_performer
HEAD:backend/onyx/server/features/mcp/api.py:1931:                        request.auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/api.py:2061:            and request.auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/api.py:2081:        and request.auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/api.py:2538:        auth_performer=mcp_server.auth_performer,
HEAD:backend/onyx/server/features/mcp/client.py:223:def process_mcp_result(call_tool_result: CallToolResult) -> str:
HEAD:backend/onyx/server/features/mcp/client.py:227:    for content_block in call_tool_result.content:
HEAD:backend/onyx/server/features/mcp/client.py:243:    return "\n\n".join(p for p in parts if p) or str(call_tool_result.structuredContent)
HEAD:backend/onyx/server/features/mcp/client.py:246:def _call_mcp_tool(tool_name: str, arguments: dict[str, Any]) -> MCPClientFunction[str]:
HEAD:backend/onyx/server/features/mcp/client.py:247:    async def call_tool(session: ClientSession) -> str:
HEAD:backend/onyx/server/features/mcp/client.py:249:        result = await session.call_tool(tool_name, arguments)
HEAD:backend/onyx/server/features/mcp/client.py:252:    return call_tool
HEAD:backend/onyx/server/features/mcp/client.py:255:def call_mcp_tool(
HEAD:backend/onyx/server/features/mcp/client.py:265:        _call_mcp_tool(tool_name, arguments),
HEAD:backend/onyx/server/features/mcp/credentials.py:32:from onyx.db.enums import MCPAuthenticationPerformer, MCPAuthenticationType
HEAD:backend/onyx/server/features/mcp/credentials.py:103:    auth_performer: MCPAuthenticationPerformer | None,
HEAD:backend/onyx/server/features/mcp/credentials.py:110:    if auth_performer == MCPAuthenticationPerformer.ADMIN:
HEAD:backend/onyx/server/features/mcp/credentials.py:124:        and mcp_server.auth_performer == MCPAuthenticationPerformer.PER_USER
HEAD:backend/onyx/server/features/mcp/credentials.py:270:        if mcp_server.auth_performer == MCPAuthenticationPerformer.PER_USER:
HEAD:backend/onyx/server/features/mcp/models.py:211:    auth_performer: MCPAuthenticationPerformer = Field(
HEAD:backend/onyx/server/features/mcp/models.py:312:            and self.auth_performer != MCPAuthenticationPerformer.PER_USER
HEAD:backend/onyx/server/features/mcp/models.py:322:            and self.auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/models.py:332:            and self.auth_performer == MCPAuthenticationPerformer.ADMIN
HEAD:backend/onyx/server/features/mcp/models.py:349:            and self.auth_performer == MCPAuthenticationPerformer.PER_USER
HEAD:backend/onyx/server/features/mcp/models.py:360:            and self.auth_performer == MCPAuthenticationPerformer.PER_USER
HEAD:backend/onyx/server/features/mcp/models.py:583:    auth_performer: MCPAuthenticationPerformer
HEAD:backend/onyx/server/features/mcp/models.py:695:    auth_performer: Optional[MCPAuthenticationPerformer] = None
HEAD:backend/onyx/server/features/mcp/oauth.py:3:Used by chat tool calls (`MCPTool.run`), the admin/user MCP API routes, and the
HEAD:backend/onyx/server/features/mcp/oauth_flow.py:113:        auth_performer=mcp_server.auth_performer,
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1215:Tool calls use the same config files and environment variables as the CLI. Each tool accepts typed arguments plus `extraArgs` for advanced CLI flags and exact CLI parity. Tool discovery is paginated and includes read-only/open-world annotations so modern MCP clients can load the large typed surface incrementally. Use the `session` tool argument or `AGENT_BROWSER_SESSION` to isolate browser state.
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:10:from onyx.server.features.mcp.client import call_mcp_tool
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:150:        """Execute the MCP tool by calling the MCP server"""
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:250:            tool_result = call_mcp_tool(
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:259:            logger.info("MCP tool '%s' executed successfully", self._name)
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:290:            logger.error("Failed to execute MCP tool '%s': %s", self._name, e)
```
No MCP server was contacted.
These are only source-level candidate invocation paths.
## MCP Authentication / Token / Header Handling
Evidence lines: 650
```text
HEAD:backend/ee/onyx/auth/users.py:33:    api_key = request.headers.get("Authorization", "").replace("Bearer ", "")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:22:from ee.onyx.db.connector_credential_pair import get_all_auto_sync_cc_pairs
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:51:from onyx.db.connector_credential_pair import get_connector_credential_pair_from_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:53:    get_document_ids_for_connector_credential_pair,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:54:    get_documents_for_connector_credential_pair_limited_columns,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:55:    upsert_document_by_connector_credential_pair,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:64:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:71:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:163:def _is_external_doc_permissions_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:170:    if cc_pair.status != ConnectorCredentialPairStatus.ACTIVE:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:423:    Permission sync task that handles document permission syncing for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:438:            connector_credential_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:517:            cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:521:                eager_load_credential=True,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:525:                    f"No connector credential pair found for id: {cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:531:                    cc_pair.credential.id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:539:                        f"Unable to create connector credential pair for id: {cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:588:            credential_id = cc_pair.credential.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:597:                    get_documents_for_connector_credential_pair_limited_columns(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:600:                        credential_id=credential_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:607:                return get_document_ids_for_connector_credential_pair(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:610:                    credential_id=credential_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:613:        # cc_pair is detached: connectors may read eager-loaded connector/credential
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:640:                credential_id=credential_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:714:    credential_id: int,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:748:                    upsert_document_by_connector_credential_pair(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:751:                        credential_id=credential_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:779:            f"element_update_permissions exceptioned: {element_type}={element_id}, {connector_id=} {credential_id=}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:784:            f"element_update_permissions completed: {element_type}={element_id}, {connector_id=} {credential_id=}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:7:from onyx.db.connector_credential_pair import get_connector_credential_pairs_for_source
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:8:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:12:    db_session: Session, cc_pair: ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:17:    cc_pairs = get_connector_credential_pairs_for_source(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:24:    db_session: Session, cc_pair: ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:16:from ee.onyx.db.connector_credential_pair import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:50:from onyx.db.connector_credential_pair import get_connector_credential_pair_from_id
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:54:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:58:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:118:def _is_external_group_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:127:    if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:199:                    status=ConnectorCredentialPairStatus.ACTIVE,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:365:    External group sync task for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:489:            connector_credential_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:516:        cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:519:            eager_load_credential=True,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:522:            raise ValueError(f"No connector credential pair found for id: {cc_pair_id}")
HEAD:backend/ee/onyx/configs/license_enforcement_config.py:32:#   /mcp/oauth/client-metadata - Public OAuth client identity
HEAD:backend/ee/onyx/configs/license_enforcement_config.py:50:        "/mcp/oauth/client-metadata",
HEAD:backend/ee/onyx/configs/license_enforcement_config.py:64:        # SCIM discovery is unauthenticated. A bearer-less cloud probe resolves
HEAD:backend/ee/onyx/connectors/capability_applicability.py:15:from onyx.connectors.capabilities import CredentialCapability
HEAD:backend/ee/onyx/connectors/capability_applicability.py:20:) -> set[CredentialCapability]:
HEAD:backend/ee/onyx/connectors/capability_applicability.py:22:    applicable: set[CredentialCapability] = set()
HEAD:backend/ee/onyx/connectors/capability_applicability.py:24:        applicable.add(CredentialCapability.DOC_PERMISSION_SYNC)
HEAD:backend/ee/onyx/connectors/capability_applicability.py:26:        applicable.add(CredentialCapability.EXTERNAL_GROUP_SYNC)
HEAD:backend/ee/onyx/connectors/capability_checks.py:17:    CredentialCapability,
HEAD:backend/ee/onyx/connectors/capability_checks.py:48:        self, source: DocumentSource, capability: CredentialCapability
HEAD:backend/ee/onyx/connectors/capability_checks.py:80:    registered_by_capability: dict[CredentialCapability, list[CapabilityCheck]] = {
HEAD:backend/ee/onyx/connectors/capability_checks.py:81:        CredentialCapability.DOC_PERMISSION_SYNC: (
HEAD:backend/ee/onyx/connectors/capability_checks.py:84:        CredentialCapability.EXTERNAL_GROUP_SYNC: (
HEAD:backend/ee/onyx/db/connector_credential_pair.py:5:from onyx.db.connector_credential_pair import get_connector_credential_pair
HEAD:backend/ee/onyx/db/connector_credential_pair.py:6:from onyx.db.enums import AccessType, ConnectorCredentialPairStatus
HEAD:backend/ee/onyx/db/connector_credential_pair.py:9:    ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:10:    UserGroup__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:17:def _delete_connector_credential_pair_user_groups_relationship__no_commit(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:18:    db_session: Session, connector_id: int, credential_id: int
HEAD:backend/ee/onyx/db/connector_credential_pair.py:20:    cc_pair = get_connector_credential_pair(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:23:        credential_id=credential_id,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:27:            f"ConnectorCredentialPair with connector_id: {connector_id} and credential_id: {credential_id} not found"
HEAD:backend/ee/onyx/db/connector_credential_pair.py:30:    stmt = delete(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:31:        UserGroup__ConnectorCredentialPair.cc_pair_id == cc_pair.id,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:40:    status: ConnectorCredentialPairStatus | None = None,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:41:) -> list[ConnectorCredentialPair]:
HEAD:backend/ee/onyx/db/connector_credential_pair.py:47:        db_session.query(ConnectorCredentialPair)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:48:        .join(ConnectorCredentialPair.connector)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:50:        .order_by(ConnectorCredentialPair.id)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:54:        query = query.filter(ConnectorCredentialPair.access_type == access_type)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:57:        query = query.filter(ConnectorCredentialPair.status == status)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:65:) -> list[ConnectorCredentialPair]:
HEAD:backend/ee/onyx/db/connector_credential_pair.py:67:        db_session.query(ConnectorCredentialPair)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:69:            ConnectorCredentialPair.access_type == AccessType.SYNC,
HEAD:backend/ee/onyx/db/document_set.py:10:    ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/document_set.py:12:    DocumentSet__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/document_set.py:105:                    DocumentSet__ConnectorCredentialPair.connector_credential_pair_id
HEAD:backend/ee/onyx/db/document_set.py:107:                    DocumentSet__ConnectorCredentialPair.document_set_id.in_(
HEAD:backend/ee/onyx/db/document_set.py:110:                    DocumentSet__ConnectorCredentialPair.is_current.is_(True),
HEAD:backend/ee/onyx/db/document_set.py:152:) -> list[tuple[DocumentSet, list[ConnectorCredentialPair]]]:
HEAD:backend/ee/onyx/db/document_set.py:197:        tuple[DocumentSet, list[ConnectorCredentialPair]]
HEAD:backend/ee/onyx/db/document_set.py:201:        # Fetch the associated ConnectorCredentialPairs
HEAD:backend/ee/onyx/db/document_set.py:203:            db_session.query(ConnectorCredentialPair)
HEAD:backend/ee/onyx/db/document_set.py:205:                DocumentSet__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/document_set.py:206:                ConnectorCredentialPair.id
HEAD:backend/ee/onyx/db/document_set.py:207:                == DocumentSet__ConnectorCredentialPair.connector_credential_pair_id,
HEAD:backend/ee/onyx/db/document_set.py:210:                DocumentSet__ConnectorCredentialPair.document_set_id == document_set.id,
HEAD:backend/ee/onyx/db/hierarchy.py:11:from onyx.db.connector_credential_pair import build_user_cc_pair_access_filter
HEAD:backend/ee/onyx/db/hierarchy.py:13:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/db/hierarchy.py:18:    ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/hierarchy.py:20:    HierarchyNodeByConnectorCredentialPair,
HEAD:backend/ee/onyx/db/hierarchy.py:26:    node_cc_pair = HierarchyNodeByConnectorCredentialPair
HEAD:backend/ee/onyx/db/hierarchy.py:27:    cc_pair = ConnectorCredentialPair
HEAD:backend/ee/onyx/db/hierarchy.py:36:                cc_pair.credential_id == node_cc_pair.credential_id,
HEAD:backend/ee/onyx/db/hierarchy.py:41:            cc_pair.status != ConnectorCredentialPairStatus.DELETING,
HEAD:backend/ee/onyx/db/scim.py:70:        """Create a new SCIM bearer token.
HEAD:backend/ee/onyx/db/user_group.py:24:from onyx.db.connector_credential_pair import (
HEAD:backend/ee/onyx/db/user_group.py:26:    get_connector_credential_pair_from_id,
HEAD:backend/ee/onyx/db/user_group.py:31:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/db/user_group.py:37:    ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:38:    Credential,
HEAD:backend/ee/onyx/db/user_group.py:39:    Credential__UserGroup,
HEAD:backend/ee/onyx/db/user_group.py:41:    DocumentByConnectorCredentialPair,
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
HEAD:backend/ee/onyx/db/user_group.py:246:                selectinload(DocumentSet.connector_credential_pairs).selectinload(
HEAD:backend/ee/onyx/db/user_group.py:247:                    ConnectorCredentialPair.connector
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
HEAD:backend/ee/onyx/db/user_group.py:740:            select(ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/user_group.py:741:                ConnectorCredentialPair.id.in_(added_cc_pair_ids)
HEAD:backend/ee/onyx/db/user_group.py:751:                f"Connector credential pair '{cc_pair_id}' not found.",
HEAD:backend/ee/onyx/db/user_group.py:1038:    _cleanup_credential__user_group_relationships__no_commit(
HEAD:backend/ee/onyx/db/user_group.py:1097:    """Deletes all rows from UserGroup__ConnectorCredentialPair where the
HEAD:backend/ee/onyx/db/user_group.py:1098:    connector_credential_pair_id matches the given cc_pair_id.
HEAD:backend/ee/onyx/db/user_group.py:1101:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/ee/onyx/db/user_group.py:1106:        raise ValueError(f"Connector Credential Pair '{cc_pair_id}' does not exist")
HEAD:backend/ee/onyx/db/user_group.py:1108:    if cc_pair.status != ConnectorCredentialPairStatus.DELETING:
HEAD:backend/ee/onyx/db/user_group.py:1110:            f"Connector Credential Pair '{cc_pair_id}' is not in the DELETING state. status={cc_pair.status}"
HEAD:backend/ee/onyx/db/user_group.py:1113:    delete_stmt = delete(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/user_group.py:1114:        UserGroup__ConnectorCredentialPair.cc_pair_id == cc_pair_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:3:"Subject" throughout this module means the OAuth subject: the provider-issued
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:5:at that provider. It is the `(oauth_name, account_id)` pair.
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:25:from onyx.db.models import UserTenantMapping, UserTenantMappingOAuthAccount
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:36:def _oauth_identity_matches_mapping(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:37:    oauth_name: str, account_id: str
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:40:        select(UserTenantMappingOAuthAccount.oauth_name)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:42:            UserTenantMappingOAuthAccount.oauth_name == oauth_name,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:43:            UserTenantMappingOAuthAccount.account_id == account_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:44:            UserTenantMappingOAuthAccount.email == UserTenantMapping.email,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:45:            UserTenantMappingOAuthAccount.tenant_id == UserTenantMapping.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:142:    email: str, oauth_name: str | None = None, account_id: str | None = None
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:152:    if oauth_name and account_id:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:153:        tenant_id = get_tenant_id_for_oauth_account(oauth_name, account_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:156:        superseded_tenant_id = get_superseded_tenant_id_for_oauth_account(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:157:            oauth_name, account_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:172:def _oauth_account_tenant_id(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:173:    oauth_name: str, account_id: str, *, active: bool
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:179:                _oauth_identity_matches_mapping(oauth_name, account_id),
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:185:def get_tenant_id_for_oauth_account(oauth_name: str, account_id: str) -> str | None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:193:    return _oauth_account_tenant_id(oauth_name, account_id, active=True)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:196:def get_superseded_tenant_id_for_oauth_account(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:197:    oauth_name: str, account_id: str
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:208:    return _oauth_account_tenant_id(oauth_name, account_id, active=False)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:223:    tenant_id: str, email: str, oauth_name: str, account_id: str
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:243:    return get_tenant_id_for_oauth_account(oauth_name, account_id) == tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:247:    email: str, tenant_id: str, oauth_name: str, account_id: str
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:272:        accept_user_invite(normalized_email, tenant_id, [(oauth_name, account_id)])
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:275:def record_oauth_identity(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:276:    email: str, tenant_id: str, oauth_name: str, account_id: str
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:297:            pg_insert(UserTenantMappingOAuthAccount)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:299:                oauth_name=oauth_name,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:306:                    UserTenantMappingOAuthAccount.oauth_name,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:307:                    UserTenantMappingOAuthAccount.account_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:311:                UserTenantMappingOAuthAccount.email,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:312:                UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:318:                    UserTenantMappingOAuthAccount.email,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:319:                    UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:321:                    UserTenantMappingOAuthAccount.oauth_name == oauth_name,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:322:                    UserTenantMappingOAuthAccount.account_id == account_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:327:                    "OAuth identity is already linked to another tenant mapping"
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:337:        UserTenantMappingOAuthAccount.email,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:338:        UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:341:            UserTenantMappingOAuthAccount.oauth_name,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:342:            UserTenantMappingOAuthAccount.account_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:353:    oauth_identities: Sequence[tuple[str, str]],
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:370:    identities = list(dict.fromkeys(oauth_identities))
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:372:        logger.warning("No linked OAuth identity to rekey in tenant %s", tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:424:            select(UserTenantMappingOAuthAccount.account_id).where(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:426:                    UserTenantMappingOAuthAccount.email,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:427:                    UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:430:                    UserTenantMappingOAuthAccount.oauth_name,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:431:                    UserTenantMappingOAuthAccount.account_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:464:                db_session.query(UserTenantMappingOAuthAccount)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:467:                        UserTenantMappingOAuthAccount.email,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:468:                        UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:479:                        UserTenantMappingOAuthAccount.oauth_name,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:480:                        UserTenantMappingOAuthAccount.account_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:683:    oauth_identities: Sequence[tuple[str, str]] = (),
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:687:    ``oauth_identities`` are the ``(oauth_name, account_id)`` subjects the caller
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:692:    identities = list(dict.fromkeys(oauth_identities))
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:723:                            UserTenantMappingOAuthAccount.oauth_name,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:724:                            UserTenantMappingOAuthAccount.account_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:725:                            UserTenantMappingOAuthAccount.email,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:726:                            UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:729:                                UserTenantMappingOAuthAccount.oauth_name,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:730:                                UserTenantMappingOAuthAccount.account_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:738:                    (oauth_name, account_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:739:                    for oauth_name, account_id, _, _ in presented_links
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:741:                # Rows this login's OAuth subjects are already linked to. Matching
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:751:                    db_session.query(UserTenantMappingOAuthAccount)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:754:                            UserTenantMappingOAuthAccount.email,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:755:                            UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:769:                        UserTenantMappingOAuthAccount(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:770:                            oauth_name=oauth_name,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:775:                        for oauth_name, account_id in identities
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:776:                        if (oauth_name, account_id) not in linked_identities
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:788:                    # OAuth subject links belong to that address's previous holder.
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:18:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:24:    box_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:6:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:8:    BOX_ENTERPRISE_ID_CREDENTIAL_KEY,
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:15:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:56:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:58:    creds = credential_json(cc_pair)
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:59:    enterprise_id = creds[BOX_ENTERPRISE_ID_CREDENTIAL_KEY]
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:61:    connector.load_credentials(creds)
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:18:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:24:    canvas_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:5:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:14:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:75:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:78:    connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:16:from onyx.connectors.credentials_provider import OnyxDBCredentialsProvider
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:17:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:29:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:43:    provider = OnyxDBCredentialsProvider(
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:44:        get_current_tenant_id(), "confluence", cc_pair.credential_id
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:46:    confluence_connector.set_credentials_provider(provider)
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:11:from onyx.connectors.credentials_provider import OnyxDBCredentialsProvider
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:13:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:162:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:164:    provider = OnyxDBCredentialsProvider(tenant_id, "confluence", cc_pair.credential_id)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:20:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:25:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:36:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:49:    # Initialize GitHub connector with credentials
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:54:    github_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:55:    logger.info("GitHub connector credentials loaded successfully")
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:7:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:9:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:17:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:22:    github_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:8:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:18:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:26:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:45:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:57:    gmail_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:17:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:31:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:67:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:376:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:390:    google_drive_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:16:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:26:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:162:            # 401 indicates a customer-side credential issue (token revoked /
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:166:                    "Google Drive returned 401 for user %s; credentials may need to be reconnected. %s",
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:504:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:506:    # Initialize connector and build credential/service objects
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:510:    google_drive_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:21:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:29:    jira_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:9:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:151:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:166:        credentials=credential_json(cc_pair),
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:11:from onyx.db.models import ConnectorCredentialPair  # noqa
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:17:    """Protocol for a function that fetches documents for a connector credential pair.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:28:        Fetches documents for a connector credential pair.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:34:    """Protocol for a function that fetches document IDs for a connector credential pair.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:44:        Fetches document IDs for a connector credential pair.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:52:        ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:63:        ConnectorCredentialPair,  # cc_pair
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:1:from ee.onyx.db.connector_credential_pair import get_all_auto_sync_cc_pairs
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:10:from onyx.connectors.credentials_provider import build_db_credentials_provider
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:46:    cache_key: tuple[str, int], credential_updated_at: datetime
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:50:    if cached is None or cached[0] != credential_updated_at:
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:57:    credential_updated_at: datetime,
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:62:        if cached is not None and cached[0] >= credential_updated_at:
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:67:            _SALESFORCE_CLIENT_CACHE[cache_key] = (credential_updated_at, client)
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:78:    """Return the client for the document's first connector credential pair."""
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:82:            f"No connector credential pair found for Salesforce document: {doc_id}"
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:85:    credential = cc_pairs[0].credential
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:87:    cache_key = (tenant_id, credential.id)
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:88:    cached_client = _get_cached_salesforce_client(cache_key, credential.time_updated)
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:92:    provider = build_db_credentials_provider(DocumentSource.SALESFORCE, credential.id)
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:94:    return _cache_salesforce_client(cache_key, credential.time_updated, client)
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:21:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:29:    sharepoint_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:7:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:10:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:18:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:25:    # Create SharePoint connector instance and load credentials
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:27:    connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:14:from onyx.connectors.credentials_provider import build_db_credentials_provider
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:26:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:233:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:246:    provider = build_db_credentials_provider(
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:247:        DocumentSource.SLACK, cc_pair.credential.id
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:250:    slack_connector.set_credentials_provider(provider)
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:252:    assert slack_client is not None, "set_credentials_provider builds the gateway."
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:11:from onyx.connectors.credentials_provider import build_db_credentials_provider
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:13:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:56:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:62:    provider = build_db_credentials_provider(
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:63:        DocumentSource.SLACK, cc_pair.credential.id
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:65:    slack_client = SlackSourceOperations(credentials_provider=provider)
HEAD:backend/ee/onyx/external_permissions/sync_params.py:37:    from onyx.db.models import ConnectorCredentialPair  # noqa
HEAD:backend/ee/onyx/external_permissions/sync_params.py:46:        cc_pair: "ConnectorCredentialPair",
HEAD:backend/ee/onyx/external_permissions/sync_params.py:58:        tenant_id: str, cc_pair: "ConnectorCredentialPair"
HEAD:backend/ee/onyx/external_permissions/sync_params.py:209:    cc_pair: "ConnectorCredentialPair",  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:22:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:30:    teams_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/utils.py:14:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/utils.py:21:def credential_json(cc_pair: ConnectorCredentialPair) -> dict[str, Any]:
HEAD:backend/ee/onyx/external_permissions/utils.py:23:        cc_pair.credential.credential_json.get_value(apply_mask=False)
HEAD:backend/ee/onyx/external_permissions/utils.py:24:        if cc_pair.credential.credential_json
HEAD:backend/ee/onyx/external_permissions/utils.py:30:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/main.py:5:from httpx_oauth.clients.google import GoogleOAuth2
HEAD:backend/ee/onyx/main.py:30:from ee.onyx.server.oauth.api import router as ee_oauth_router
HEAD:backend/ee/onyx/main.py:43:from onyx.auth.users import auth_backend, create_onyx_oauth_router
HEAD:backend/ee/onyx/main.py:46:    GOOGLE_OAUTH_SCOPE_OVERRIDE,
HEAD:backend/ee/onyx/main.py:47:    OAUTH_CLIENT_ID,
HEAD:backend/ee/onyx/main.py:48:    OAUTH_CLIENT_SECRET,
HEAD:backend/ee/onyx/main.py:106:        # For Google OAuth, refresh tokens are requested by:
HEAD:backend/ee/onyx/main.py:108:        # 2. Properly configuring OAuth in Google Cloud Console to allow offline access
HEAD:backend/ee/onyx/main.py:110:            GOOGLE_OAUTH_SCOPE_OVERRIDE or GOOGLE_LOGIN_BASE_SCOPES
HEAD:backend/ee/onyx/main.py:113:        oauth_client = GoogleOAuth2(
HEAD:backend/ee/onyx/main.py:114:            OAUTH_CLIENT_ID,
HEAD:backend/ee/onyx/main.py:115:            OAUTH_CLIENT_SECRET,
HEAD:backend/ee/onyx/main.py:120:            create_onyx_oauth_router(
HEAD:backend/ee/onyx/main.py:121:                oauth_client,
HEAD:backend/ee/onyx/main.py:127:                redirect_url=f"{WEB_DOMAIN}/auth/oauth/callback",
HEAD:backend/ee/onyx/main.py:129:            prefix="/auth/oauth",
HEAD:backend/ee/onyx/main.py:142:    include_router_with_global_prefix_prepended(application, ee_oauth_router)
HEAD:backend/ee/onyx/main.py:172:    # they use their own SCIM bearer token auth).
HEAD:backend/ee/onyx/server/auth_check.py:7:    # before bearer token configuration is complete
HEAD:backend/ee/onyx/server/billing/service.py:47:        headers["Authorization"] = f"Bearer {license_data}"
HEAD:backend/ee/onyx/server/billing/service.py:59:        "Authorization": f"Bearer {token}",
HEAD:backend/ee/onyx/server/documents/cc_pair.py:14:from onyx.db.connector_credential_pair import (
HEAD:backend/ee/onyx/server/documents/cc_pair.py:15:    get_connector_credential_pair_from_id_for_user,
HEAD:backend/ee/onyx/server/documents/cc_pair.py:40:    cc_pair = get_connector_credential_pair_from_id_for_user(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:66:    cc_pair = get_connector_credential_pair_from_id_for_user(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:88:        "Permissions sync cc_pair=%s connector_id=%s credential_id=%s %s connector.",
HEAD:backend/ee/onyx/server/documents/cc_pair.py:91:        cc_pair.credential_id,
HEAD:backend/ee/onyx/server/documents/cc_pair.py:119:    cc_pair = get_connector_credential_pair_from_id_for_user(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:145:    cc_pair = get_connector_credential_pair_from_id_for_user(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:167:        "External group sync cc_pair=%s connector_id=%s credential_id=%s %s connector.",
HEAD:backend/ee/onyx/server/documents/cc_pair.py:170:        cc_pair.credential_id,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:41:from onyx.db.users import get_user_by_oauth_account
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:86:    and the subject has to belong to nobody. `oauth_callback` resolves by
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:95:        for account in user.oauth_accounts
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:96:        if account.oauth_name == "custom"
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:102:        if get_user_by_oauth_account("custom", account_id, db_session) is not None:
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:108:    # The subject, not the address, picks the tenant `oauth_callback` runs in:
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:130:    # in it to this user before `oauth_callback` resolves and rewrites the link
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:155:        await user_manager.oauth_callback(
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:156:            oauth_name="custom",
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:383:    """Create a new SCIM bearer token.
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:390:    # carry nothing but this bearer token, resolve to the right workspace.
HEAD:backend/ee/onyx/server/features/hooks/api.py:48:    and OAuth endpoints treat it: at the VALIDATE_* levels private/internal
HEAD:backend/ee/onyx/server/features/hooks/api.py:120:        raise OnyxError(OnyxErrorCode.CREDENTIAL_INVALID, validation.error_message)
HEAD:backend/ee/onyx/server/features/hooks/api.py:152:        headers["Authorization"] = f"Bearer {api_key}"
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:57:# not our credential. Everything else (401/403 describe OUR credential; other
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:145:    # Authorization header is an Onyx PAT, not an Anthropic key.
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:149:            "The selected provider has no credential configured.",
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:293:            # api_base values can embed query credentials; log the type only.
HEAD:backend/ee/onyx/server/gateway/api.py:149:            "This credential is not authorized to use the Onyx LLM gateway.",
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:54:# 401/403 describe OUR credential, not the caller's request, so they are
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:76:    # URLs, none of which this module's Bearer /v1/responses shape produces.
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:203:            "The selected provider has no credential configured.",
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:210:            "Authorization": f"Bearer {provider.api_key}",
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:320:            # api_base values can embed query credentials; log the type only.
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:19:    retrieve_auth_token_data_from_bearer,
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:126:    # Check for API key or PAT in Authorization header
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:134:        # an Authorization: Bearer header and carry no cookie.
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:137:            token_data = await retrieve_auth_token_data_from_bearer(request)
HEAD:backend/ee/onyx/server/middleware/tier_gate.py:93:            # to prevent authorization bypass. The request will be gated below if required > COMMUNITY.
HEAD:backend/ee/onyx/server/oauth/api.py:7:from ee.onyx.server.oauth.api_router import router
HEAD:backend/ee/onyx/server/oauth/api.py:8:from ee.onyx.server.oauth.confluence_cloud import ConfluenceCloudOAuth
HEAD:backend/ee/onyx/server/oauth/api.py:9:from ee.onyx.server.oauth.google_drive import GoogleDriveOAuth
HEAD:backend/ee/onyx/server/oauth/api.py:10:from ee.onyx.server.oauth.slack import SlackOAuth
HEAD:backend/ee/onyx/server/oauth/api.py:23:@router.post("/prepare-authorization-request")
HEAD:backend/ee/onyx/server/oauth/api.py:24:def prepare_authorization_request(
HEAD:backend/ee/onyx/server/oauth/api.py:32:    Example: https://www.oauth.com/oauth2-servers/authorization/the-authorization-request/
HEAD:backend/ee/onyx/server/oauth/api.py:35:    # create random oauth state param for security and to retrieve user data later
HEAD:backend/ee/onyx/server/oauth/api.py:36:    oauth_uuid = uuid.uuid4()
HEAD:backend/ee/onyx/server/oauth/api.py:37:    oauth_uuid_str = str(oauth_uuid)
HEAD:backend/ee/onyx/server/oauth/api.py:39:    # urlsafe b64 encode the uuid for the oauth url
HEAD:backend/ee/onyx/server/oauth/api.py:40:    oauth_state = (
HEAD:backend/ee/onyx/server/oauth/api.py:41:        base64.urlsafe_b64encode(oauth_uuid.bytes).rstrip(b"=").decode("utf-8")
HEAD:backend/ee/onyx/server/oauth/api.py:47:            oauth_url = SlackOAuth.generate_oauth_url(oauth_state)
HEAD:backend/ee/onyx/server/oauth/api.py:49:            oauth_url = SlackOAuth.generate_dev_oauth_url(oauth_state)
HEAD:backend/ee/onyx/server/oauth/api.py:51:        session = SlackOAuth.session_dump_json(
HEAD:backend/ee/onyx/server/oauth/api.py:56:            oauth_url = ConfluenceCloudOAuth.generate_oauth_url(oauth_state)
HEAD:backend/ee/onyx/server/oauth/api.py:58:            oauth_url = ConfluenceCloudOAuth.generate_dev_oauth_url(oauth_state)
HEAD:backend/ee/onyx/server/oauth/api.py:59:        session = ConfluenceCloudOAuth.session_dump_json(
HEAD:backend/ee/onyx/server/oauth/api.py:64:            oauth_url = GoogleDriveOAuth.generate_oauth_url(oauth_state)
HEAD:backend/ee/onyx/server/oauth/api.py:66:            oauth_url = GoogleDriveOAuth.generate_dev_oauth_url(oauth_state)
HEAD:backend/ee/onyx/server/oauth/api.py:67:        session = GoogleDriveOAuth.session_dump_json(
HEAD:backend/ee/onyx/server/oauth/api.py:71:        oauth_url = None
HEAD:backend/ee/onyx/server/oauth/api.py:73:    if not oauth_url:
HEAD:backend/ee/onyx/server/oauth/api.py:76:            detail=f"The document source type {connector} does not have OAuth implemented",
HEAD:backend/ee/onyx/server/oauth/api.py:82:            detail=f"The document source type {connector} failed to generate an OAuth session.",
HEAD:backend/ee/onyx/server/oauth/api.py:88:    # 10 min is the max we want an oauth flow to be valid
HEAD:backend/ee/onyx/server/oauth/api.py:89:    r.set(f"da_oauth:{oauth_uuid_str}", session, ex=600)
HEAD:backend/ee/onyx/server/oauth/api.py:91:    return JSONResponse(content={"url": oauth_url})
HEAD:backend/ee/onyx/server/oauth/api_router.py:3:router: APIRouter = APIRouter(prefix="/oauth")
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:12:from ee.onyx.server.oauth.api_router import router
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:16:    OAUTH_CONFLUENCE_CLOUD_CLIENT_ID,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:17:    OAUTH_CONFLUENCE_CLOUD_CLIENT_SECRET,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:21:from onyx.connectors.confluence.utils import CONFLUENCE_OAUTH_TOKEN_URL
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:22:from onyx.db.credentials import (
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:23:    create_credential,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:24:    fetch_credential_by_id_for_user,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:25:    update_credential_json,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:31:from onyx.server.documents.models import CredentialBase
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:38:class ConfluenceCloudOAuth:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:39:    # https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:41:    class OAuthSession(BaseModel):
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:45:        redirect_on_success: str | None  # Where to send the user if OAuth flow succeeds
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:48:        access_token: str
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:51:        refresh_token: str
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:61:    CLIENT_ID = OAUTH_CONFLUENCE_CLOUD_CLIENT_ID
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:62:    CLIENT_SECRET = OAUTH_CONFLUENCE_CLOUD_CLIENT_SECRET
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:63:    TOKEN_URL = CONFLUENCE_OAUTH_TOKEN_URL
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:66:        "https://api.atlassian.com/oauth/token/accessible-resources"
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:69:    # All read scopes per https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:70:    CONFLUENCE_OAUTH_SCOPE = (
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:88:    REDIRECT_URI = f"{WEB_DOMAIN}/admin/connectors/confluence/oauth/callback"
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:92:    # oauth_url = (
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:93:    #     f"http://localhost:8090/rest/oauth/v2/authorize?client_id={CONFLUENCE_OAUTH_CLIENT_ID}"
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:94:    #     f"&scope={CONFLUENCE_OAUTH_SCOPE_2}"
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:99:    def generate_oauth_url(cls, state: str) -> str:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:100:        return cls._generate_oauth_url_helper(cls.REDIRECT_URI, state)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:103:    def generate_dev_oauth_url(cls, state: str) -> str:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:105:        - https://www.nango.dev/blog/oauth-redirects-on-localhost-with-https
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:107:        return cls._generate_oauth_url_helper(cls.DEV_REDIRECT_URI, state)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:110:    def _generate_oauth_url_helper(cls, redirect_uri: str, state: str) -> str:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:111:        # https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#1--direct-the-user-to-the-authorization-url-to-get-an-authorization-code
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:117:            f"&scope={cls.CONFLUENCE_OAUTH_SCOPE}"
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:130:        session = ConfluenceCloudOAuth.OAuthSession(
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:136:    def parse_session(cls, session_json: str) -> OAuthSession:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:137:        session = ConfluenceCloudOAuth.OAuthSession.model_validate_json(session_json)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:141:    def generate_finalize_url(cls, credential_id: int) -> str:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:142:        return f"{WEB_DOMAIN}/admin/connectors/confluence/oauth/finalize?credential={credential_id}"
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:146:def confluence_oauth_callback(
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:154:    after visiting the oauth authorization url."""
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:156:    if not ConfluenceCloudOAuth.CLIENT_ID or not ConfluenceCloudOAuth.CLIENT_SECRET:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:173:    oauth_uuid = uuid.UUID(bytes=uuid_bytes)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:174:    oauth_uuid_str = str(oauth_uuid)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:176:    r_key = f"da_oauth:{oauth_uuid_str}"
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:182:            detail=f"Confluence Cloud OAuth failed - OAuth state key not found: key={r_key}",
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:187:        session = ConfluenceCloudOAuth.parse_session(session_json)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:190:            redirect_uri = ConfluenceCloudOAuth.REDIRECT_URI
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:192:            redirect_uri = ConfluenceCloudOAuth.DEV_REDIRECT_URI
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:194:        # Exchange the authorization code for an access token
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:196:            ConfluenceCloudOAuth.TOKEN_URL,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:197:            headers={"Content-Type": "application/x-www-form-urlencoded"},
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:199:                "client_id": ConfluenceCloudOAuth.CLIENT_ID,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:200:                "client_secret": ConfluenceCloudOAuth.CLIENT_SECRET,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:203:                "grant_type": "authorization_code",
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:207:        token_response: ConfluenceCloudOAuth.TokenResponse | None = None
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:210:            token_response = ConfluenceCloudOAuth.TokenResponse.model_validate_json(
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:215:                "Confluence Cloud OAuth failed during code/token exchange."
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:221:        credential_info = CredentialBase(
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:222:            credential_json={
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:223:                "confluence_access_token": token_response.access_token,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:224:                "confluence_refresh_token": token_response.refresh_token,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:232:            name="Confluence Cloud OAuth",
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:235:        credential = create_credential(credential_info, user, db_session)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:241:                "message": f"An error occurred during Confluence Cloud OAuth: {str(e)}",
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:251:            "message": "Confluence Cloud OAuth completed successfully.",
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:252:            "finalize_url": ConfluenceCloudOAuth.generate_finalize_url(credential.id),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:259:def confluence_oauth_accessible_resources(
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:260:    credential_id: int,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:269:    credential = fetch_credential_by_id_for_user(credential_id, user, db_session)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:270:    if not credential:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:271:        raise HTTPException(400, f"Credential {credential_id} not found.")
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:273:    credential_dict = (
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:274:        credential.credential_json.get_value(apply_mask=False)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:275:        if credential.credential_json
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:278:    access_token = credential_dict["confluence_access_token"]
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:281:        # Exchange the authorization code for an access token
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:283:            ConfluenceCloudOAuth.ACCESSIBLE_RESOURCE_URL,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:284:            headers={
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:285:                "Authorization": f"Bearer {access_token}",
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:296:                ConfluenceCloudOAuth.AccessibleResources(**resource)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:323:def confluence_oauth_finalize(
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:324:    credential_id: int,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:332:    """Saves the info for the selected cloud site to the credential.
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:333:    This is the final step in the confluence oauth flow where after the traditional
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:334:    OAuth process, the user has to select a site to associate with the credentials.
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:335:    After this, the credential is usable."""
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:337:    credential = fetch_credential_by_id_for_user(credential_id, user, db_session)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:338:    if not credential:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:341:            detail=f"Confluence Cloud OAuth failed - credential {credential_id} not found.",
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:344:    existing_credential_json = (
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:345:        credential.credential_json.get_value(apply_mask=False)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:346:        if credential.credential_json
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:349:    new_credential_json: dict[str, Any] = dict(existing_credential_json)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:350:    new_credential_json["cloud_id"] = cloud_id
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:351:    new_credential_json["cloud_name"] = cloud_name
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:352:    new_credential_json["wiki_base"] = cloud_url
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:355:        update_credential_json(credential_id, new_credential_json, user, db_session)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:361:                "message": f"An error occurred during Confluence Cloud OAuth: {str(e)}",
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:369:            "message": "Confluence Cloud OAuth finalized successfully.",
HEAD:backend/ee/onyx/server/oauth/google_drive.py:12:from ee.onyx.server.oauth.api_router import router
HEAD:backend/ee/onyx/server/oauth/google_drive.py:16:    OAUTH_GOOGLE_DRIVE_CLIENT_ID,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:17:    OAUTH_GOOGLE_DRIVE_CLIENT_SECRET,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:22:    get_google_oauth_creds,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:23:    sanitize_oauth_credentials,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:26:    DB_CREDENTIALS_AUTHENTICATION_METHOD,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:27:    DB_CREDENTIALS_DICT_TOKEN_KEY,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:28:    DB_CREDENTIALS_PRIMARY_ADMIN_KEY,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:29:    GoogleOAuthAuthenticationMethod,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:31:from onyx.db.credentials import create_credential
HEAD:backend/ee/onyx/server/oauth/google_drive.py:36:from onyx.server.documents.models import CredentialBase
HEAD:backend/ee/onyx/server/oauth/google_drive.py:40:class GoogleDriveOAuth:
HEAD:backend/ee/onyx/server/oauth/google_drive.py:41:    # https://developers.google.com/identity/protocols/oauth2
HEAD:backend/ee/onyx/server/oauth/google_drive.py:42:    # https://developers.google.com/identity/protocols/oauth2/web-server
HEAD:backend/ee/onyx/server/oauth/google_drive.py:44:    class OAuthSession(BaseModel):
HEAD:backend/ee/onyx/server/oauth/google_drive.py:48:        redirect_on_success: str | None  # Where to send the user if OAuth flow succeeds
HEAD:backend/ee/onyx/server/oauth/google_drive.py:50:    CLIENT_ID = OAUTH_GOOGLE_DRIVE_CLIENT_ID
HEAD:backend/ee/onyx/server/oauth/google_drive.py:51:    CLIENT_SECRET = OAUTH_GOOGLE_DRIVE_CLIENT_SECRET
HEAD:backend/ee/onyx/server/oauth/google_drive.py:53:    TOKEN_URL = "https://oauth2.googleapis.com/token"
HEAD:backend/ee/onyx/server/oauth/google_drive.py:64:    REDIRECT_URI = f"{WEB_DOMAIN}/admin/connectors/google-drive/oauth/callback"
HEAD:backend/ee/onyx/server/oauth/google_drive.py:68:    def generate_oauth_url(cls, state: str) -> str:
HEAD:backend/ee/onyx/server/oauth/google_drive.py:69:        return cls._generate_oauth_url_helper(cls.REDIRECT_URI, state)
HEAD:backend/ee/onyx/server/oauth/google_drive.py:72:    def generate_dev_oauth_url(cls, state: str) -> str:
HEAD:backend/ee/onyx/server/oauth/google_drive.py:74:        - https://www.nango.dev/blog/oauth-redirects-on-localhost-with-https
HEAD:backend/ee/onyx/server/oauth/google_drive.py:77:        return cls._generate_oauth_url_helper(cls.DEV_REDIRECT_URI, state)
HEAD:backend/ee/onyx/server/oauth/google_drive.py:80:    def _generate_oauth_url_helper(cls, redirect_uri: str, state: str) -> str:
HEAD:backend/ee/onyx/server/oauth/google_drive.py:83:            f"https://accounts.google.com/o/oauth2/v2/auth"
HEAD:backend/ee/onyx/server/oauth/google_drive.py:99:        session = GoogleDriveOAuth.OAuthSession(
HEAD:backend/ee/onyx/server/oauth/google_drive.py:105:    def parse_session(cls, session_json: str) -> OAuthSession:
HEAD:backend/ee/onyx/server/oauth/google_drive.py:106:        session = GoogleDriveOAuth.OAuthSession.model_validate_json(session_json)
HEAD:backend/ee/onyx/server/oauth/google_drive.py:111:def handle_google_drive_oauth_callback(
HEAD:backend/ee/onyx/server/oauth/google_drive.py:118:    if not GoogleDriveOAuth.CLIENT_ID or not GoogleDriveOAuth.CLIENT_SECRET:
HEAD:backend/ee/onyx/server/oauth/google_drive.py:135:    oauth_uuid = uuid.UUID(bytes=uuid_bytes)
HEAD:backend/ee/onyx/server/oauth/google_drive.py:136:    oauth_uuid_str = str(oauth_uuid)
HEAD:backend/ee/onyx/server/oauth/google_drive.py:138:    r_key = f"da_oauth:{oauth_uuid_str}"
HEAD:backend/ee/onyx/server/oauth/google_drive.py:144:            detail=f"Google Drive OAuth failed - OAuth state key not found: key={r_key}",
HEAD:backend/ee/onyx/server/oauth/google_drive.py:149:        session = GoogleDriveOAuth.parse_session(session_json)
HEAD:backend/ee/onyx/server/oauth/google_drive.py:152:            redirect_uri = GoogleDriveOAuth.REDIRECT_URI
HEAD:backend/ee/onyx/server/oauth/google_drive.py:154:            redirect_uri = GoogleDriveOAuth.DEV_REDIRECT_URI
HEAD:backend/ee/onyx/server/oauth/google_drive.py:156:        # Exchange the authorization code for an access token
HEAD:backend/ee/onyx/server/oauth/google_drive.py:158:            GoogleDriveOAuth.TOKEN_URL,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:159:            headers={"Content-Type": "application/x-www-form-urlencoded"},
HEAD:backend/ee/onyx/server/oauth/google_drive.py:161:                "client_id": GoogleDriveOAuth.CLIENT_ID,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:162:                "client_secret": GoogleDriveOAuth.CLIENT_SECRET,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:165:                "grant_type": "authorization_code",
HEAD:backend/ee/onyx/server/oauth/google_drive.py:171:        authorization_response: dict[str, Any] = response.json()
HEAD:backend/ee/onyx/server/oauth/google_drive.py:174:        # returned from OAuthCredentials.get_authorized_user_info().
HEAD:backend/ee/onyx/server/oauth/google_drive.py:175:        # So refresh immediately via get_google_oauth_creds with the params filled in
HEAD:backend/ee/onyx/server/oauth/google_drive.py:176:        # from fields in authorization_response to get the json we need
HEAD:backend/ee/onyx/server/oauth/google_drive.py:178:        authorized_user_info["client_id"] = OAUTH_GOOGLE_DRIVE_CLIENT_ID
HEAD:backend/ee/onyx/server/oauth/google_drive.py:179:        authorized_user_info["client_secret"] = OAUTH_GOOGLE_DRIVE_CLIENT_SECRET
HEAD:backend/ee/onyx/server/oauth/google_drive.py:180:        authorized_user_info["refresh_token"] = authorization_response["refresh_token"]
HEAD:backend/ee/onyx/server/oauth/google_drive.py:183:        oauth_creds = get_google_oauth_creds(
HEAD:backend/ee/onyx/server/oauth/google_drive.py:186:        if not oauth_creds:
HEAD:backend/ee/onyx/server/oauth/google_drive.py:187:            raise RuntimeError("get_google_oauth_creds returned None.")
HEAD:backend/ee/onyx/server/oauth/google_drive.py:189:        # save off the credentials
HEAD:backend/ee/onyx/server/oauth/google_drive.py:190:        oauth_creds_sanitized_json_str = sanitize_oauth_credentials(oauth_creds)
HEAD:backend/ee/onyx/server/oauth/google_drive.py:192:        credential_dict: dict[str, str] = {}
HEAD:backend/ee/onyx/server/oauth/google_drive.py:193:        credential_dict[DB_CREDENTIALS_DICT_TOKEN_KEY] = oauth_creds_sanitized_json_str
HEAD:backend/ee/onyx/server/oauth/google_drive.py:194:        credential_dict[DB_CREDENTIALS_PRIMARY_ADMIN_KEY] = session.email
HEAD:backend/ee/onyx/server/oauth/google_drive.py:195:        credential_dict[DB_CREDENTIALS_AUTHENTICATION_METHOD] = (
HEAD:backend/ee/onyx/server/oauth/google_drive.py:196:            GoogleOAuthAuthenticationMethod.OAUTH_INTERACTIVE.value
HEAD:backend/ee/onyx/server/oauth/google_drive.py:199:        credential_info = CredentialBase(
HEAD:backend/ee/onyx/server/oauth/google_drive.py:200:            credential_json=credential_dict,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:203:            name="OAuth (interactive)",
HEAD:backend/ee/onyx/server/oauth/google_drive.py:206:        create_credential(credential_info, user, db_session)
HEAD:backend/ee/onyx/server/oauth/google_drive.py:212:                "message": f"An error occurred during Google Drive OAuth: {str(e)}",
HEAD:backend/ee/onyx/server/oauth/google_drive.py:222:            "message": "Google Drive OAuth completed successfully.",
HEAD:backend/ee/onyx/server/oauth/slack.py:11:from ee.onyx.server.oauth.api_router import router
HEAD:backend/ee/onyx/server/oauth/slack.py:15:    OAUTH_SLACK_CLIENT_ID,
HEAD:backend/ee/onyx/server/oauth/slack.py:16:    OAUTH_SLACK_CLIENT_SECRET,
HEAD:backend/ee/onyx/server/oauth/slack.py:20:from onyx.db.credentials import create_credential
HEAD:backend/ee/onyx/server/oauth/slack.py:25:from onyx.server.documents.models import CredentialBase
HEAD:backend/ee/onyx/server/oauth/slack.py:29:class SlackOAuth:
HEAD:backend/ee/onyx/server/oauth/slack.py:30:    # https://knock.app/blog/how-to-authenticate-users-in-slack-using-oauth
HEAD:backend/ee/onyx/server/oauth/slack.py:31:    # Example: https://api.slack.com/authentication/oauth-v2#exchanging
HEAD:backend/ee/onyx/server/oauth/slack.py:33:    class OAuthSession(BaseModel):
HEAD:backend/ee/onyx/server/oauth/slack.py:37:        redirect_on_success: str | None  # Where to send the user if OAuth flow succeeds
HEAD:backend/ee/onyx/server/oauth/slack.py:39:    CLIENT_ID = OAUTH_SLACK_CLIENT_ID
HEAD:backend/ee/onyx/server/oauth/slack.py:40:    CLIENT_SECRET = OAUTH_SLACK_CLIENT_SECRET
HEAD:backend/ee/onyx/server/oauth/slack.py:42:    TOKEN_URL = "https://slack.com/api/oauth.v2.access"
HEAD:backend/ee/onyx/server/oauth/slack.py:57:    REDIRECT_URI = f"{WEB_DOMAIN}/admin/connectors/slack/oauth/callback"
HEAD:backend/ee/onyx/server/oauth/slack.py:61:    def generate_oauth_url(cls, state: str) -> str:
HEAD:backend/ee/onyx/server/oauth/slack.py:62:        return cls._generate_oauth_url_helper(cls.REDIRECT_URI, state)
HEAD:backend/ee/onyx/server/oauth/slack.py:65:    def generate_dev_oauth_url(cls, state: str) -> str:
HEAD:backend/ee/onyx/server/oauth/slack.py:67:        - https://www.nango.dev/blog/oauth-redirects-on-localhost-with-https
HEAD:backend/ee/onyx/server/oauth/slack.py:70:        return cls._generate_oauth_url_helper(cls.DEV_REDIRECT_URI, state)
HEAD:backend/ee/onyx/server/oauth/slack.py:73:    def _generate_oauth_url_helper(cls, redirect_uri: str, state: str) -> str:
HEAD:backend/ee/onyx/server/oauth/slack.py:75:            f"https://slack.com/oauth/v2/authorize"
HEAD:backend/ee/onyx/server/oauth/slack.py:88:        session = SlackOAuth.OAuthSession(
```
Authentication material crossing an MCP boundary must preserve least
privilege and the intended caller identity.
## External-App Credential Boundaries
Evidence lines: 650
```text
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:22:from ee.onyx.db.connector_credential_pair import get_all_auto_sync_cc_pairs
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:51:from onyx.db.connector_credential_pair import get_connector_credential_pair_from_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:53:    get_document_ids_for_connector_credential_pair,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:54:    get_documents_for_connector_credential_pair_limited_columns,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:55:    upsert_document_by_connector_credential_pair,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:64:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:71:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:163:def _is_external_doc_permissions_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:170:    if cc_pair.status != ConnectorCredentialPairStatus.ACTIVE:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:423:    Permission sync task that handles document permission syncing for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:438:            connector_credential_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:517:            cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:521:                eager_load_credential=True,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:525:                    f"No connector credential pair found for id: {cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:531:                    cc_pair.credential.id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:539:                        f"Unable to create connector credential pair for id: {cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:588:            credential_id = cc_pair.credential.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:597:                    get_documents_for_connector_credential_pair_limited_columns(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:600:                        credential_id=credential_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:607:                return get_document_ids_for_connector_credential_pair(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:610:                    credential_id=credential_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:613:        # cc_pair is detached: connectors may read eager-loaded connector/credential
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:640:                credential_id=credential_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:714:    credential_id: int,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:748:                    upsert_document_by_connector_credential_pair(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:751:                        credential_id=credential_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:779:            f"element_update_permissions exceptioned: {element_type}={element_id}, {connector_id=} {credential_id=}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:784:            f"element_update_permissions completed: {element_type}={element_id}, {connector_id=} {credential_id=}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:7:from onyx.db.connector_credential_pair import get_connector_credential_pairs_for_source
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:8:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:12:    db_session: Session, cc_pair: ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:17:    cc_pairs = get_connector_credential_pairs_for_source(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:24:    db_session: Session, cc_pair: ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:16:from ee.onyx.db.connector_credential_pair import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:50:from onyx.db.connector_credential_pair import get_connector_credential_pair_from_id
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:54:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:58:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:118:def _is_external_group_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:127:    if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:199:                    status=ConnectorCredentialPairStatus.ACTIVE,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:365:    External group sync task for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:489:            connector_credential_pair_id=cc_pair_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:516:        cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:519:            eager_load_credential=True,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:522:            raise ValueError(f"No connector credential pair found for id: {cc_pair_id}")
HEAD:backend/ee/onyx/connectors/capability_applicability.py:15:from onyx.connectors.capabilities import CredentialCapability
HEAD:backend/ee/onyx/connectors/capability_applicability.py:20:) -> set[CredentialCapability]:
HEAD:backend/ee/onyx/connectors/capability_applicability.py:22:    applicable: set[CredentialCapability] = set()
HEAD:backend/ee/onyx/connectors/capability_applicability.py:24:        applicable.add(CredentialCapability.DOC_PERMISSION_SYNC)
HEAD:backend/ee/onyx/connectors/capability_applicability.py:26:        applicable.add(CredentialCapability.EXTERNAL_GROUP_SYNC)
HEAD:backend/ee/onyx/connectors/capability_checks.py:17:    CredentialCapability,
HEAD:backend/ee/onyx/connectors/capability_checks.py:48:        self, source: DocumentSource, capability: CredentialCapability
HEAD:backend/ee/onyx/connectors/capability_checks.py:80:    registered_by_capability: dict[CredentialCapability, list[CapabilityCheck]] = {
HEAD:backend/ee/onyx/connectors/capability_checks.py:81:        CredentialCapability.DOC_PERMISSION_SYNC: (
HEAD:backend/ee/onyx/connectors/capability_checks.py:84:        CredentialCapability.EXTERNAL_GROUP_SYNC: (
HEAD:backend/ee/onyx/db/connector_credential_pair.py:5:from onyx.db.connector_credential_pair import get_connector_credential_pair
HEAD:backend/ee/onyx/db/connector_credential_pair.py:6:from onyx.db.enums import AccessType, ConnectorCredentialPairStatus
HEAD:backend/ee/onyx/db/connector_credential_pair.py:9:    ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:10:    UserGroup__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:17:def _delete_connector_credential_pair_user_groups_relationship__no_commit(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:18:    db_session: Session, connector_id: int, credential_id: int
HEAD:backend/ee/onyx/db/connector_credential_pair.py:20:    cc_pair = get_connector_credential_pair(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:23:        credential_id=credential_id,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:27:            f"ConnectorCredentialPair with connector_id: {connector_id} and credential_id: {credential_id} not found"
HEAD:backend/ee/onyx/db/connector_credential_pair.py:30:    stmt = delete(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/connector_credential_pair.py:31:        UserGroup__ConnectorCredentialPair.cc_pair_id == cc_pair.id,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:40:    status: ConnectorCredentialPairStatus | None = None,
HEAD:backend/ee/onyx/db/connector_credential_pair.py:41:) -> list[ConnectorCredentialPair]:
HEAD:backend/ee/onyx/db/connector_credential_pair.py:47:        db_session.query(ConnectorCredentialPair)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:48:        .join(ConnectorCredentialPair.connector)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:50:        .order_by(ConnectorCredentialPair.id)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:54:        query = query.filter(ConnectorCredentialPair.access_type == access_type)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:57:        query = query.filter(ConnectorCredentialPair.status == status)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:65:) -> list[ConnectorCredentialPair]:
HEAD:backend/ee/onyx/db/connector_credential_pair.py:67:        db_session.query(ConnectorCredentialPair)
HEAD:backend/ee/onyx/db/connector_credential_pair.py:69:            ConnectorCredentialPair.access_type == AccessType.SYNC,
HEAD:backend/ee/onyx/db/document_set.py:10:    ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/document_set.py:12:    DocumentSet__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/document_set.py:105:                    DocumentSet__ConnectorCredentialPair.connector_credential_pair_id
HEAD:backend/ee/onyx/db/document_set.py:107:                    DocumentSet__ConnectorCredentialPair.document_set_id.in_(
HEAD:backend/ee/onyx/db/document_set.py:110:                    DocumentSet__ConnectorCredentialPair.is_current.is_(True),
HEAD:backend/ee/onyx/db/document_set.py:152:) -> list[tuple[DocumentSet, list[ConnectorCredentialPair]]]:
HEAD:backend/ee/onyx/db/document_set.py:197:        tuple[DocumentSet, list[ConnectorCredentialPair]]
HEAD:backend/ee/onyx/db/document_set.py:201:        # Fetch the associated ConnectorCredentialPairs
HEAD:backend/ee/onyx/db/document_set.py:203:            db_session.query(ConnectorCredentialPair)
HEAD:backend/ee/onyx/db/document_set.py:205:                DocumentSet__ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/document_set.py:206:                ConnectorCredentialPair.id
HEAD:backend/ee/onyx/db/document_set.py:207:                == DocumentSet__ConnectorCredentialPair.connector_credential_pair_id,
HEAD:backend/ee/onyx/db/document_set.py:210:                DocumentSet__ConnectorCredentialPair.document_set_id == document_set.id,
HEAD:backend/ee/onyx/db/hierarchy.py:11:from onyx.db.connector_credential_pair import build_user_cc_pair_access_filter
HEAD:backend/ee/onyx/db/hierarchy.py:13:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/db/hierarchy.py:18:    ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/hierarchy.py:20:    HierarchyNodeByConnectorCredentialPair,
HEAD:backend/ee/onyx/db/hierarchy.py:26:    node_cc_pair = HierarchyNodeByConnectorCredentialPair
HEAD:backend/ee/onyx/db/hierarchy.py:27:    cc_pair = ConnectorCredentialPair
HEAD:backend/ee/onyx/db/hierarchy.py:36:                cc_pair.credential_id == node_cc_pair.credential_id,
HEAD:backend/ee/onyx/db/hierarchy.py:41:            cc_pair.status != ConnectorCredentialPairStatus.DELETING,
HEAD:backend/ee/onyx/db/user_group.py:24:from onyx.db.connector_credential_pair import (
HEAD:backend/ee/onyx/db/user_group.py:26:    get_connector_credential_pair_from_id,
HEAD:backend/ee/onyx/db/user_group.py:31:    ConnectorCredentialPairStatus,
HEAD:backend/ee/onyx/db/user_group.py:37:    ConnectorCredentialPair,
HEAD:backend/ee/onyx/db/user_group.py:38:    Credential,
HEAD:backend/ee/onyx/db/user_group.py:39:    Credential__UserGroup,
HEAD:backend/ee/onyx/db/user_group.py:41:    DocumentByConnectorCredentialPair,
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
HEAD:backend/ee/onyx/db/user_group.py:246:                selectinload(DocumentSet.connector_credential_pairs).selectinload(
HEAD:backend/ee/onyx/db/user_group.py:247:                    ConnectorCredentialPair.connector
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
HEAD:backend/ee/onyx/db/user_group.py:740:            select(ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/user_group.py:741:                ConnectorCredentialPair.id.in_(added_cc_pair_ids)
HEAD:backend/ee/onyx/db/user_group.py:751:                f"Connector credential pair '{cc_pair_id}' not found.",
HEAD:backend/ee/onyx/db/user_group.py:1038:    _cleanup_credential__user_group_relationships__no_commit(
HEAD:backend/ee/onyx/db/user_group.py:1097:    """Deletes all rows from UserGroup__ConnectorCredentialPair where the
HEAD:backend/ee/onyx/db/user_group.py:1098:    connector_credential_pair_id matches the given cc_pair_id.
HEAD:backend/ee/onyx/db/user_group.py:1101:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/ee/onyx/db/user_group.py:1106:        raise ValueError(f"Connector Credential Pair '{cc_pair_id}' does not exist")
HEAD:backend/ee/onyx/db/user_group.py:1108:    if cc_pair.status != ConnectorCredentialPairStatus.DELETING:
HEAD:backend/ee/onyx/db/user_group.py:1110:            f"Connector Credential Pair '{cc_pair_id}' is not in the DELETING state. status={cc_pair.status}"
HEAD:backend/ee/onyx/db/user_group.py:1113:    delete_stmt = delete(UserGroup__ConnectorCredentialPair).where(
HEAD:backend/ee/onyx/db/user_group.py:1114:        UserGroup__ConnectorCredentialPair.cc_pair_id == cc_pair_id,
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:18:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/box/doc_sync.py:24:    box_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:6:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:8:    BOX_ENTERPRISE_ID_CREDENTIAL_KEY,
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:15:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:56:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:58:    creds = credential_json(cc_pair)
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:59:    enterprise_id = creds[BOX_ENTERPRISE_ID_CREDENTIAL_KEY]
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:61:    connector.load_credentials(creds)
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:18:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/canvas/doc_sync.py:24:    canvas_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:5:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:14:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:75:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:78:    connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:16:from onyx.connectors.credentials_provider import OnyxDBCredentialsProvider
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:17:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:29:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:43:    provider = OnyxDBCredentialsProvider(
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:44:        get_current_tenant_id(), "confluence", cc_pair.credential_id
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:46:    confluence_connector.set_credentials_provider(provider)
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:11:from onyx.connectors.credentials_provider import OnyxDBCredentialsProvider
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:13:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:162:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:164:    provider = OnyxDBCredentialsProvider(tenant_id, "confluence", cc_pair.credential_id)
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:20:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:25:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:36:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:49:    # Initialize GitHub connector with credentials
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:54:    github_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/github/doc_sync.py:55:    logger.info("GitHub connector credentials loaded successfully")
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:7:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:9:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:17:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:22:    github_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:8:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:18:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:26:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:45:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/gmail/doc_sync.py:57:    gmail_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:17:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:31:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:67:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:376:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:390:    google_drive_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:16:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:26:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:162:            # 401 indicates a customer-side credential issue (token revoked /
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:166:                    "Google Drive returned 401 for user %s; credentials may need to be reconnected. %s",
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:504:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:506:    # Initialize connector and build credential/service objects
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:510:    google_drive_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:21:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/jira/doc_sync.py:29:    jira_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:9:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:151:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:166:        credentials=credential_json(cc_pair),
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:11:from onyx.db.models import ConnectorCredentialPair  # noqa
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:17:    """Protocol for a function that fetches documents for a connector credential pair.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:28:        Fetches documents for a connector credential pair.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:34:    """Protocol for a function that fetches document IDs for a connector credential pair.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:44:        Fetches document IDs for a connector credential pair.
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:52:        ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:63:        ConnectorCredentialPair,  # cc_pair
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:1:from ee.onyx.db.connector_credential_pair import get_all_auto_sync_cc_pairs
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:10:from onyx.connectors.credentials_provider import build_db_credentials_provider
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:46:    cache_key: tuple[str, int], credential_updated_at: datetime
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:50:    if cached is None or cached[0] != credential_updated_at:
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:57:    credential_updated_at: datetime,
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:62:        if cached is not None and cached[0] >= credential_updated_at:
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:67:            _SALESFORCE_CLIENT_CACHE[cache_key] = (credential_updated_at, client)
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:78:    """Return the client for the document's first connector credential pair."""
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:82:            f"No connector credential pair found for Salesforce document: {doc_id}"
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:85:    credential = cc_pairs[0].credential
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:87:    cache_key = (tenant_id, credential.id)
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:88:    cached_client = _get_cached_salesforce_client(cache_key, credential.time_updated)
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:92:    provider = build_db_credentials_provider(DocumentSource.SALESFORCE, credential.id)
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:94:    return _cache_salesforce_client(cache_key, credential.time_updated, client)
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:21:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/sharepoint/doc_sync.py:29:    sharepoint_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:7:from ee.onyx.external_permissions.utils import credential_json
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:10:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:18:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:25:    # Create SharePoint connector instance and load credentials
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:27:    connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:14:from onyx.connectors.credentials_provider import build_db_credentials_provider
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:26:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:233:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:246:    provider = build_db_credentials_provider(
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:247:        DocumentSource.SLACK, cc_pair.credential.id
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:250:    slack_connector.set_credentials_provider(provider)
HEAD:backend/ee/onyx/external_permissions/slack/doc_sync.py:252:    assert slack_client is not None, "set_credentials_provider builds the gateway."
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:11:from onyx.connectors.credentials_provider import build_db_credentials_provider
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:13:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:56:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:62:    provider = build_db_credentials_provider(
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:63:        DocumentSource.SLACK, cc_pair.credential.id
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:65:    slack_client = SlackSourceOperations(credentials_provider=provider)
HEAD:backend/ee/onyx/external_permissions/sync_params.py:37:    from onyx.db.models import ConnectorCredentialPair  # noqa
HEAD:backend/ee/onyx/external_permissions/sync_params.py:46:        cc_pair: "ConnectorCredentialPair",
HEAD:backend/ee/onyx/external_permissions/sync_params.py:58:        tenant_id: str, cc_pair: "ConnectorCredentialPair"
HEAD:backend/ee/onyx/external_permissions/sync_params.py:209:    cc_pair: "ConnectorCredentialPair",  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:7:from ee.onyx.external_permissions.utils import credential_json, generic_doc_sync
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:11:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:22:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/external_permissions/teams/doc_sync.py:30:    teams_connector.load_credentials(credential_json(cc_pair))
HEAD:backend/ee/onyx/external_permissions/utils.py:14:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/ee/onyx/external_permissions/utils.py:21:def credential_json(cc_pair: ConnectorCredentialPair) -> dict[str, Any]:
HEAD:backend/ee/onyx/external_permissions/utils.py:23:        cc_pair.credential.credential_json.get_value(apply_mask=False)
HEAD:backend/ee/onyx/external_permissions/utils.py:24:        if cc_pair.credential.credential_json
HEAD:backend/ee/onyx/external_permissions/utils.py:30:    cc_pair: ConnectorCredentialPair,
HEAD:backend/ee/onyx/server/documents/cc_pair.py:14:from onyx.db.connector_credential_pair import (
HEAD:backend/ee/onyx/server/documents/cc_pair.py:15:    get_connector_credential_pair_from_id_for_user,
HEAD:backend/ee/onyx/server/documents/cc_pair.py:40:    cc_pair = get_connector_credential_pair_from_id_for_user(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:66:    cc_pair = get_connector_credential_pair_from_id_for_user(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:88:        "Permissions sync cc_pair=%s connector_id=%s credential_id=%s %s connector.",
HEAD:backend/ee/onyx/server/documents/cc_pair.py:91:        cc_pair.credential_id,
HEAD:backend/ee/onyx/server/documents/cc_pair.py:119:    cc_pair = get_connector_credential_pair_from_id_for_user(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:145:    cc_pair = get_connector_credential_pair_from_id_for_user(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:167:        "External group sync cc_pair=%s connector_id=%s credential_id=%s %s connector.",
HEAD:backend/ee/onyx/server/documents/cc_pair.py:170:        cc_pair.credential_id,
HEAD:backend/ee/onyx/server/features/hooks/api.py:120:        raise OnyxError(OnyxErrorCode.CREDENTIAL_INVALID, validation.error_message)
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:57:# not our credential. Everything else (401/403 describe OUR credential; other
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:149:            "The selected provider has no credential configured.",
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:293:            # api_base values can embed query credentials; log the type only.
HEAD:backend/ee/onyx/server/gateway/api.py:149:            "This credential is not authorized to use the Onyx LLM gateway.",
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:54:# 401/403 describe OUR credential, not the caller's request, so they are
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:203:            "The selected provider has no credential configured.",
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:320:            # api_base values can embed query credentials; log the type only.
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:22:from onyx.db.credentials import (
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:23:    create_credential,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:24:    fetch_credential_by_id_for_user,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:25:    update_credential_json,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:31:from onyx.server.documents.models import CredentialBase
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:141:    def generate_finalize_url(cls, credential_id: int) -> str:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:142:        return f"{WEB_DOMAIN}/admin/connectors/confluence/oauth/finalize?credential={credential_id}"
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:221:        credential_info = CredentialBase(
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:222:            credential_json={
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:235:        credential = create_credential(credential_info, user, db_session)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:252:            "finalize_url": ConfluenceCloudOAuth.generate_finalize_url(credential.id),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:260:    credential_id: int,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:269:    credential = fetch_credential_by_id_for_user(credential_id, user, db_session)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:270:    if not credential:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:271:        raise HTTPException(400, f"Credential {credential_id} not found.")
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:273:    credential_dict = (
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:274:        credential.credential_json.get_value(apply_mask=False)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:275:        if credential.credential_json
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:278:    access_token = credential_dict["confluence_access_token"]
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:324:    credential_id: int,
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:332:    """Saves the info for the selected cloud site to the credential.
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:334:    OAuth process, the user has to select a site to associate with the credentials.
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:335:    After this, the credential is usable."""
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:337:    credential = fetch_credential_by_id_for_user(credential_id, user, db_session)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:338:    if not credential:
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:341:            detail=f"Confluence Cloud OAuth failed - credential {credential_id} not found.",
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:344:    existing_credential_json = (
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:345:        credential.credential_json.get_value(apply_mask=False)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:346:        if credential.credential_json
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:349:    new_credential_json: dict[str, Any] = dict(existing_credential_json)
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:350:    new_credential_json["cloud_id"] = cloud_id
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:351:    new_credential_json["cloud_name"] = cloud_name
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:352:    new_credential_json["wiki_base"] = cloud_url
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:355:        update_credential_json(credential_id, new_credential_json, user, db_session)
HEAD:backend/ee/onyx/server/oauth/google_drive.py:23:    sanitize_oauth_credentials,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:26:    DB_CREDENTIALS_AUTHENTICATION_METHOD,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:27:    DB_CREDENTIALS_DICT_TOKEN_KEY,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:28:    DB_CREDENTIALS_PRIMARY_ADMIN_KEY,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:31:from onyx.db.credentials import create_credential
HEAD:backend/ee/onyx/server/oauth/google_drive.py:36:from onyx.server.documents.models import CredentialBase
HEAD:backend/ee/onyx/server/oauth/google_drive.py:174:        # returned from OAuthCredentials.get_authorized_user_info().
HEAD:backend/ee/onyx/server/oauth/google_drive.py:189:        # save off the credentials
HEAD:backend/ee/onyx/server/oauth/google_drive.py:190:        oauth_creds_sanitized_json_str = sanitize_oauth_credentials(oauth_creds)
HEAD:backend/ee/onyx/server/oauth/google_drive.py:192:        credential_dict: dict[str, str] = {}
HEAD:backend/ee/onyx/server/oauth/google_drive.py:193:        credential_dict[DB_CREDENTIALS_DICT_TOKEN_KEY] = oauth_creds_sanitized_json_str
HEAD:backend/ee/onyx/server/oauth/google_drive.py:194:        credential_dict[DB_CREDENTIALS_PRIMARY_ADMIN_KEY] = session.email
HEAD:backend/ee/onyx/server/oauth/google_drive.py:195:        credential_dict[DB_CREDENTIALS_AUTHENTICATION_METHOD] = (
HEAD:backend/ee/onyx/server/oauth/google_drive.py:199:        credential_info = CredentialBase(
HEAD:backend/ee/onyx/server/oauth/google_drive.py:200:            credential_json=credential_dict,
HEAD:backend/ee/onyx/server/oauth/google_drive.py:206:        create_credential(credential_info, user, db_session)
HEAD:backend/ee/onyx/server/oauth/slack.py:20:from onyx.db.credentials import create_credential
HEAD:backend/ee/onyx/server/oauth/slack.py:25:from onyx.server.documents.models import CredentialBase
HEAD:backend/ee/onyx/server/oauth/slack.py:170:        credential_info = CredentialBase(
HEAD:backend/ee/onyx/server/oauth/slack.py:171:            credential_json={"slack_bot_token": access_token},
HEAD:backend/ee/onyx/server/oauth/slack.py:177:        create_credential(credential_info, user, db_session)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:36:    VERTEXAI_DEFAULT_CREDENTIALS,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:64:    VERTEX_CREDENTIALS_FILE_KWARG,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:468:    if VERTEXAI_DEFAULT_CREDENTIALS:
HEAD:backend/ee/onyx/server/tenants/provisioning.py:477:        # Vertex AI uses custom_config for credentials and location
HEAD:backend/ee/onyx/server/tenants/provisioning.py:479:            VERTEX_CREDENTIALS_FILE_KWARG: VERTEXAI_DEFAULT_CREDENTIALS,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:496:            "VERTEXAI_DEFAULT_CREDENTIALS not set, skipping Vertex AI provider configuration"
HEAD:backend/ee/onyx/server/user_group/api.py:115:    mask_credential_prefix = get_security_settings().mask_credential_prefix
HEAD:backend/ee/onyx/server/user_group/api.py:119:            mask_credential_prefix=mask_credential_prefix,
HEAD:backend/ee/onyx/server/user_group/api.py:157:        mask_credential_prefix=get_security_settings().mask_credential_prefix,
HEAD:backend/ee/onyx/server/user_group/api.py:298:        mask_credential_prefix=get_security_settings().mask_credential_prefix,
HEAD:backend/ee/onyx/server/user_group/api.py:333:            mask_credential_prefix=get_security_settings().mask_credential_prefix,
HEAD:backend/ee/onyx/server/user_group/api.py:366:            mask_credential_prefix=get_security_settings().mask_credential_prefix,
HEAD:backend/ee/onyx/server/user_group/api.py:389:            mask_credential_prefix=get_security_settings().mask_credential_prefix,
HEAD:backend/ee/onyx/server/user_group/api.py:412:            mask_credential_prefix=get_security_settings().mask_credential_prefix,
HEAD:backend/ee/onyx/server/user_group/models.py:8:    ConnectorCredentialPairDescriptor,
HEAD:backend/ee/onyx/server/user_group/models.py:10:    CredentialSnapshot,
HEAD:backend/ee/onyx/server/user_group/models.py:22:    cc_pairs: list[ConnectorCredentialPairDescriptor]
HEAD:backend/ee/onyx/server/user_group/models.py:40:        mask_credential_prefix: bool,
HEAD:backend/ee/onyx/server/user_group/models.py:68:                ConnectorCredentialPairDescriptor(
HEAD:backend/ee/onyx/server/user_group/models.py:73:                        credential_ids=[cc_pair_relationship.cc_pair.credential_id],
HEAD:backend/ee/onyx/server/user_group/models.py:75:                    credential=CredentialSnapshot.from_credential_db_model(
HEAD:backend/ee/onyx/server/user_group/models.py:76:                        cc_pair_relationship.cc_pair.credential,
HEAD:backend/ee/onyx/server/user_group/models.py:77:                        mask_credential_prefix=mask_credential_prefix,
HEAD:backend/ee/onyx/server/user_group/models.py:86:                    ds, mask_credential_prefix=mask_credential_prefix
HEAD:backend/ee/onyx/utils/license.py:303:    checkout id could replace this instance's credential with another tenant's.
HEAD:backend/ee/onyx/utils/license.py:402:    """The control plane refused the stored license as a credential.
HEAD:backend/ee/onyx/utils/license.py:415:    LicenseRejectedError when that credential is refused, ValueError on an
HEAD:backend/onyx/access/access.py:19:    DocumentByConnectorCredentialPair,
HEAD:backend/onyx/access/access.py:353:    credential) whose `Connector.connector_specific_config['file_locations']`
HEAD:backend/onyx/access/access.py:356:    different credentials can have different ACLs, and a user with access
HEAD:backend/onyx/access/access.py:357:    via one credential must not be denied because we sampled a doc from
HEAD:backend/onyx/access/access.py:369:            DocumentByConnectorCredentialPair.connector_id,
HEAD:backend/onyx/access/access.py:370:            DocumentByConnectorCredentialPair.credential_id,
HEAD:backend/onyx/access/access.py:374:            Connector.id == DocumentByConnectorCredentialPair.connector_id,
HEAD:backend/onyx/access/access.py:387:    for connector_id, credential_id in cc_pair_keys:
HEAD:backend/onyx/access/access.py:389:            select(DocumentByConnectorCredentialPair.id)
HEAD:backend/onyx/access/access.py:391:                DocumentByConnectorCredentialPair.connector_id == connector_id,
HEAD:backend/onyx/access/access.py:392:                DocumentByConnectorCredentialPair.credential_id == credential_id,
HEAD:backend/onyx/auth/mobile_sso/sso_completion.py:22:from onyx.auth.mobile_sso.tokens import issue_session_credential
HEAD:backend/onyx/auth/mobile_sso/sso_completion.py:117:    token = await issue_session_credential(user, strategy)
HEAD:backend/onyx/auth/mobile_sso/tokens.py:3:A single indirection point for minting the credential a native client receives.
HEAD:backend/onyx/auth/mobile_sso/tokens.py:17:async def issue_session_credential(
HEAD:backend/onyx/auth/oauth_refresher.py:31:# Legacy env-credential refresh endpoints, keyed by oauth_account.oauth_name.
HEAD:backend/onyx/auth/oauth_refresher.py:179:    """Legacy env-credential resolution for accounts with no provider row:
HEAD:backend/onyx/auth/oauth_refresher.py:200:    """Endpoint + client credentials for an account: the provider row matching
HEAD:backend/onyx/auth/oauth_refresher.py:256:            "No OAuth credentials configured to refresh provider: %s", oauth_name
HEAD:backend/onyx/auth/schemas.py:55:    endpoints, and strips the identity/credential fields the stock PATCH /users/me
HEAD:backend/onyx/auth/sso_url_guard.py:23:    """Require https, no embedded credentials, and an address the SSRF Protection
HEAD:backend/onyx/auth/sso_url_guard.py:28:        raise UnsafeSSOUrl(f"{field} must not carry credentials")
HEAD:backend/onyx/auth/users.py:177:    CURRENT_USAGE_CREDENTIAL_CONTEXTVAR,
HEAD:backend/onyx/auth/users.py:180:    UsageCredentialIdentity,
HEAD:backend/onyx/auth/users.py:183:from shared_configs.enums import UsageCredentialType
HEAD:backend/onyx/auth/users.py:1100:                    # Placeholders (EXT_PERM_USER, bots) carry no credentials or
HEAD:backend/onyx/auth/users.py:1485:        # Never log the verification token: it is a replayable credential that
HEAD:backend/onyx/auth/users.py:1525:        self, credentials: OAuth2PasswordRequestForm
HEAD:backend/onyx/auth/users.py:1527:        email = credentials.username
HEAD:backend/onyx/auth/users.py:1553:            # rather than be flattened into a generic credential failure.
HEAD:backend/onyx/auth/users.py:1557:                "User attempted to login with invalid credentials: %s", str(e)
HEAD:backend/onyx/auth/users.py:1562:            self.password_helper.hash(credentials.password)
HEAD:backend/onyx/auth/users.py:1578:                self.password_helper.hash(credentials.password)
HEAD:backend/onyx/auth/users.py:1589:                credentials.password, user.hashed_password
HEAD:backend/onyx/auth/users.py:2147:                    request.state.usage_credential = UsageCredentialIdentity(
HEAD:backend/onyx/auth/users.py:2148:                        UsageCredentialType.JWT
HEAD:backend/onyx/auth/users.py:2222:        request.state.usage_credential = UsageCredentialIdentity(
HEAD:backend/onyx/auth/users.py:2223:            UsageCredentialType.SESSION
HEAD:backend/onyx/auth/users.py:2239:                request.state.usage_credential = UsageCredentialIdentity(
HEAD:backend/onyx/auth/users.py:2241:                        UsageCredentialType.CRAFT_PAT
HEAD:backend/onyx/auth/users.py:2243:                        else UsageCredentialType.PAT
HEAD:backend/onyx/auth/users.py:2253:                request.state.usage_credential = UsageCredentialIdentity(
HEAD:backend/onyx/auth/users.py:2254:                    UsageCredentialType.API_KEY,
HEAD:backend/onyx/auth/users.py:2292:    credential_token = CURRENT_USAGE_CREDENTIAL_CONTEXTVAR.set(
HEAD:backend/onyx/auth/users.py:2293:        getattr(request.state, "usage_credential", None)  # ods: ignore[getattr]
HEAD:backend/onyx/auth/users.py:2298:        CURRENT_USAGE_CREDENTIAL_CONTEXTVAR.reset(credential_token)
HEAD:backend/onyx/auth/users.py:2693:            ErrorCode.LOGIN_BAD_CREDENTIALS,
HEAD:backend/onyx/auth/users.py:2915:                            ErrorCode.LOGIN_BAD_CREDENTIALS: {
HEAD:backend/onyx/auth/users.py:2917:                                "value": {"detail": ErrorCode.LOGIN_BAD_CREDENTIALS},
HEAD:backend/onyx/background/celery/apps/app_base.py:322:    # Initialize tracing in workers if credentials are available.
HEAD:backend/onyx/background/celery/apps/primary.py:234:                    f"cc_pair={attempt.connector_credential_pair_id} "
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:25:from onyx.db.credential_capability import (
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:31:from onyx.db.credentials import fetch_credential_by_id
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:43:    credential_id: int,
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:61:        # locks for the whole run. ``credential`` stays readable after the close
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:64:            credential = fetch_credential_by_id(credential_id, db_session)
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:65:            if credential is None:
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:68:                    f"Skipping capability checks for deleted credential "
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:69:                    f"{credential_id} (tenant {tenant_id})."
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:88:            credential,
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:97:                credential_id=credential_id,
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:99:                source=credential.source,
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:114:                f"credential {credential_id}, connector {connector_id} "
HEAD:backend/onyx/background/celery/tasks/capability_checks/tasks.py:124:                credential_id=credential_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:28:from onyx.db.connector_credential_pair import (
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:30:    delete_connector_credential_pair__no_commit,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:31:    get_connector_credential_pair_from_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:32:    get_connector_credential_pairs,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:35:    delete_all_documents_by_connector_credential_pair__no_commit,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:36:    get_document_ids_for_connector_credential_pair,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:41:    ConnectorCredentialPairStatus,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:181:            cc_pairs = get_connector_credential_pairs(db_session)
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:184:                if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:287:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:294:    if cc_pair.status != ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:451:        cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:455:        credential_id_to_delete: int | None = None
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:464:            doc_ids = get_document_ids_for_connector_credential_pair(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:465:                db_session, cc_pair.connector_id, cc_pair.credential_id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:507:                credential_id=cc_pair.credential_id,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:527:            credential_id_to_delete = cc_pair.credential_id
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:530:            # Explicitly delete document by connector credential pair records before deleting the connector
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:532:            delete_all_documents_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:535:                credential_id=credential_id_to_delete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:542:            # related to the deleted DocumentByConnectorCredentialPair during commit
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:546:            delete_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:549:                credential_id=credential_id_to_delete,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:558:            # if there are no credentials left, delete the connector
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:567:            elif not len(connector.credentials):
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:569:                    "Connector deletion - Found no credentials left for connector, deleting connector"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:621:                f"cc_pair={cc_pair_id} connector={connector_id_to_delete} credential={credential_id_to_delete}"
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:634:        f"credential={credential_id_to_delete} "
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:14:from onyx.db.enums import ConnectorCredentialPairStatus
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:17:from onyx.db.models import ConnectorCredentialPair, SearchSettings
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:23:    cc_pair: ConnectorCredentialPair,
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:56:        if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:43:from onyx.db.connector_credential_pair import get_connector_credential_pair_from_id
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:81:        if attempt.connector_credential_pair_id != cc_pair_id:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:83:                f"docfetching_task - CC pair mismatch: expected={cc_pair_id} actual={attempt.connector_credential_pair_id}",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:208:            cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:496:                index_attempt.connector_credential_pair.connector.source.value
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:499:            cc_pair = index_attempt.connector_credential_pair
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:75:from onyx.db.connector_credential_pair import (
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:76:    fetch_indexable_standard_connector_credential_pair_ids,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:77:    get_connector_credential_pair_from_id,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:79:    update_connector_credential_pair_from_id,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:84:    ConnectorCredentialPairStatus,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:436:    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:437:        db_session, attempt.connector_credential_pair_id
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:444:    if cc_pair.status == ConnectorCredentialPairStatus.SCHEDULED:
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:445:        cc_pair.status = ConnectorCredentialPairStatus.INITIAL_INDEXING
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:464:            f"cc_pair={attempt.connector_credential_pair_id} "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:479:        attempt.connector_credential_pair_id, attempt.id
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:584:        cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:586:            attempt.connector_credential_pair_id,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:591:                f"CC pair {attempt.connector_credential_pair_id} not found in database"
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:610:                ConnectorCredentialPairStatus.SCHEDULED,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:611:                ConnectorCredentialPairStatus.INITIAL_INDEXING,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:615:                cc_pair.status = ConnectorCredentialPairStatus.ACTIVE
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:659:                    cc_pair_id=attempt.connector_credential_pair_id,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:705:                IndexAttempt.connector_credential_pair_id == cc_pair_id,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:775:        cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:946:                fetch_indexable_standard_connector_credential_pair_ids(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:963:                    fetch_indexable_standard_connector_credential_pair_ids(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:975:                cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1023:                            f"history and credentials."
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1038:                        update_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1041:                            status=ConnectorCredentialPairStatus.PAUSED,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1127:                    f"cc_pair={attempt.connector_credential_pair_id} "
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1562:            cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1810:                connector_id=index_attempt.connector_credential_pair.connector.id,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1811:                credential_id=index_attempt.connector_credential_pair.credential.id,
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1819:                index_attempt.connector_credential_pair.connector.source.value
HEAD:backend/onyx/background/celery/tasks/docprocessing/tasks.py:1838:            credential_id=index_attempt_metadata.credential_id,
HEAD:backend/onyx/background/celery/tasks/docprocessing/utils.py:12:    ConnectorCredentialPairStatus,
HEAD:backend/onyx/background/celery/tasks/docprocessing/utils.py:20:from onyx.db.models import ConnectorCredentialPair, SearchSettings
HEAD:backend/onyx/background/celery/tasks/docprocessing/utils.py:150:    cc_pair: ConnectorCredentialPair, search_settings_id: int, db_session: Session
HEAD:backend/onyx/background/celery/tasks/docprocessing/utils.py:175:    cc_pair: ConnectorCredentialPair,
HEAD:backend/onyx/background/celery/tasks/docprocessing/utils.py:295:        cc_pair.status == ConnectorCredentialPairStatus.INITIAL_INDEXING
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:38:from onyx.db.connector_credential_pair import (
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:39:    fetch_indexable_standard_connector_credential_pair_ids,
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:40:    get_connector_credential_pair_from_id,
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:43:from onyx.db.enums import AccessType, ConnectorCredentialPairStatus
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:45:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:62:    cc_pair: ConnectorCredentialPair,
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:81:def _is_hierarchy_fetching_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:87:    if cc_pair.status != ConnectorCredentialPairStatus.ACTIVE:
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:107:    cc_pair: ConnectorCredentialPair,
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:131:        if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:203:            # Get all active connector credential pairs
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:204:            cc_pair_ids = fetch_indexable_standard_connector_credential_pair_ids(
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:211:                cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:257:    cc_pair: ConnectorCredentialPair,
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:270:    credential = cc_pair.credential
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:278:        credential=credential,
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:317:            credential_id=cc_pair.credential_id,
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:370:            cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/hierarchyfetching/tasks.py:381:            if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/index_reclaim/tasks.py:44:from onyx.db.connector_credential_pair import (
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:43:    ConnectorCredentialPair,
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:205:    cc_pair: ConnectorCredentialPair,
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:264:    cc_pair: ConnectorCredentialPair,
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:360:    # Get all connector credential pairs
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:361:    cc_pairs = db_session.scalars(select(ConnectorCredentialPair)).all()
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:373:                    IndexAttempt.connector_credential_pair_id == cc_pair.id,
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:40:from onyx.db.connector_credential_pair import (
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:41:    fetch_indexable_standard_connector_credential_pair_ids,
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:42:    get_connector_credential_pair_from_id,
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:51:    ConnectorCredentialPairStatus,
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:374:                cc_pair = get_connector_credential_pair_from_id(db_session, cc_pair_id)
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:377:                    or cc_pair.status == ConnectorCredentialPairStatus.DELETING
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:815:            cc_pair_ids = fetch_indexable_standard_connector_credential_pair_ids(
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:42:from onyx.db.connector_credential_pair import (
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:43:    get_connector_credential_pair,
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:44:    get_connector_credential_pair_from_id,
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:45:    get_connector_credential_pairs,
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:49:    get_documents_for_connector_credential_pair,
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:54:    ConnectorCredentialPairStatus,
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:64:from onyx.db.models import ConnectorCredentialPair
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:174:def _is_pruning_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:190:    if cc_pair.status != ConnectorCredentialPairStatus.ACTIVE:
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:238:                cc_pairs = get_connector_credential_pairs(db_session)
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:245:                    cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:336:    cc_pair: ConnectorCredentialPair,
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:403:        if cc_pair.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:443:                credential_id=cc_pair.credential_id,
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:485:    credential_id: int,
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:571:            cc_pair = get_connector_credential_pair(
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:574:                credential_id=credential_id,
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:579:                    f"cc_pair not found for {connector_id} {credential_id}"
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:608:                cc_pair.credential,
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:640:                    credential_id=credential_id,
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:682:                    for doc in get_documents_for_connector_credential_pair(
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:685:                        credential_id=credential_id,
HEAD:backend/onyx/background/celery/tasks/pruning/tasks.py:725:                credential_id=credential_id,
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:16:from onyx.db.connector_credential_pair import get_connector_credential_pair
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:18:    delete_document_by_connector_credential_pair__no_commit,
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:39:from onyx.server.documents.models import ConnectorCredentialPairIdentifier
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:79:    credential_id: int,
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:96:    cc_pair = get_connector_credential_pair(db_session, connector_id, credential_id)
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:115:    credential_id: int,
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:122:    To delete a connector / credential pair:
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:123:    (1) find all documents associated with connector / credential pair where there
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:124:    this the is only connector / credential pair that has indexed it
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:127:    (4) find all documents associated with connector / credential pair where there
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:128:    are multiple connector / credential pairs that have indexed it
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:130:    connector / credential pair from the access list
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:246:                delete_document_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:249:                    connector_credential_pair_identifier=ConnectorCredentialPairIdentifier(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:251:                        credential_id=credential_id,
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:261:                    db_session, connector_id, credential_id, document_id
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:299:                        db_session, connector_id, credential_id, document_id
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:324:                    delete_document_by_connector_credential_pair__no_commit(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:327:                        connector_credential_pair_identifier=ConnectorCredentialPairIdentifier(
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:329:                            credential_id=credential_id,
HEAD:backend/onyx/background/celery/tasks/shared/tasks.py:335:                        db_session, connector_id, credential_id, document_id
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:359:    connector.load_credentials({})
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:431:        has_connector_pairs = bool(document_set.connector_credential_pairs)
HEAD:backend/onyx/background/indexing/checkpointing_utils.py:76:    """Get the latest valid checkpoint for a given connector credential pair"""
HEAD:backend/onyx/background/indexing/index_attempt_utils.py:37:                    IndexAttempt.connector_credential_pair_id,
HEAD:backend/onyx/background/indexing/models.py:10:    connector_credential_pair_id: int
HEAD:backend/onyx/background/indexing/models.py:32:            connector_credential_pair_id=model.connector_credential_pair_id,
HEAD:backend/onyx/background/indexing/run_docfetching.py:54:from onyx.db.connector_credential_pair import (
HEAD:backend/onyx/background/indexing/run_docfetching.py:55:    get_connector_credential_pair_from_id,
HEAD:backend/onyx/background/indexing/run_docfetching.py:57:    update_connector_credential_pair,
HEAD:backend/onyx/background/indexing/run_docfetching.py:64:    ConnectorCredentialPairStatus,
HEAD:backend/onyx/background/indexing/run_docfetching.py:83:from onyx.db.models import Connector, Credential, IndexAttempt
HEAD:backend/onyx/background/indexing/run_docfetching.py:136:    task = attempt.connector_credential_pair.connector.input_type
HEAD:backend/onyx/background/indexing/run_docfetching.py:141:    credential_id = attempt.connector_credential_pair.credential.id
HEAD:backend/onyx/background/indexing/run_docfetching.py:142:    connector_id = attempt.connector_credential_pair.connector.id
HEAD:backend/onyx/background/indexing/run_docfetching.py:143:    source = attempt.connector_credential_pair.connector.source
HEAD:backend/onyx/background/indexing/run_docfetching.py:145:        attempt.connector_credential_pair.connector.connector_specific_config
HEAD:backend/onyx/background/indexing/run_docfetching.py:155:            credential_id=credential_id,
HEAD:backend/onyx/background/indexing/run_docfetching.py:168:                source=attempt.connector_credential_pair.connector.source,
HEAD:backend/onyx/background/indexing/run_docfetching.py:170:                connector_specific_config=attempt.connector_credential_pair.connector.connector_specific_config,
HEAD:backend/onyx/background/indexing/run_docfetching.py:171:                credential=attempt.connector_credential_pair.credential,
HEAD:backend/onyx/background/indexing/run_docfetching.py:181:            and attempt.connector_credential_pair.access_type == AccessType.SYNC
HEAD:backend/onyx/background/indexing/run_docfetching.py:207:            cc_pair = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/indexing/run_docfetching.py:209:                cc_pair_id=attempt.connector_credential_pair.id,
HEAD:backend/onyx/background/indexing/run_docfetching.py:211:            if cc_pair and cc_pair.status == ConnectorCredentialPairStatus.ACTIVE:
HEAD:backend/onyx/background/indexing/run_docfetching.py:212:                update_connector_credential_pair(
HEAD:backend/onyx/background/indexing/run_docfetching.py:214:                    connector_id=attempt.connector_credential_pair.connector.id,
HEAD:backend/onyx/background/indexing/run_docfetching.py:215:                    credential_id=attempt.connector_credential_pair.credential.id,
HEAD:backend/onyx/background/indexing/run_docfetching.py:216:                    status=ConnectorCredentialPairStatus.PAUSED,
HEAD:backend/onyx/background/indexing/run_docfetching.py:292:    Checks the status of the connector credential pair and index attempt.
HEAD:backend/onyx/background/indexing/run_docfetching.py:295:    cc_pair_loop = get_connector_credential_pair_from_id(
HEAD:backend/onyx/background/indexing/run_docfetching.py:303:        cc_pair_loop.status == ConnectorCredentialPairStatus.PAUSED
HEAD:backend/onyx/background/indexing/run_docfetching.py:305:    ) or cc_pair_loop.status == ConnectorCredentialPairStatus.DELETING:
HEAD:backend/onyx/background/indexing/run_docfetching.py:367:    connector_credential_pair_id: int,
HEAD:backend/onyx/background/indexing/run_docfetching.py:379:        (connector_credential_pair_id, index_attempt_id)
HEAD:backend/onyx/background/indexing/run_docfetching.py:388:        connector_name = attempt.connector_credential_pair.connector.name
HEAD:backend/onyx/background/indexing/run_docfetching.py:390:            attempt.connector_credential_pair.connector.connector_specific_config
HEAD:backend/onyx/background/indexing/run_docfetching.py:392:        credential_id = attempt.connector_credential_pair.credential_id
HEAD:backend/onyx/background/indexing/run_docfetching.py:395:        "Docfetching starting%s: connector='%s' config='%s' credentials='%s'",
HEAD:backend/onyx/background/indexing/run_docfetching.py:399:        credential_id,
HEAD:backend/onyx/background/indexing/run_docfetching.py:404:        cc_pair_id=connector_credential_pair_id,
HEAD:backend/onyx/background/indexing/run_docfetching.py:415:            cc_pair_id=connector_credential_pair_id,
HEAD:backend/onyx/background/indexing/run_docfetching.py:423:        attempt.connector_credential_pair_id,
HEAD:backend/onyx/background/indexing/run_docfetching.py:431:        "Docfetching finished%s: connector='%s' config='%s' credentials='%s'",
HEAD:backend/onyx/background/indexing/run_docfetching.py:435:        credential_id,
HEAD:backend/onyx/background/indexing/run_docfetching.py:491:        if index_attempt.connector_credential_pair.indexing_trigger is not None:
```
No credential value was accessed or used.
Static references identify where later credential-isolation testing should
focus.
## Code Interpreter / Sandbox Surface
Evidence lines: 650
```text
HEAD:backend/AGENTS.md:137:uv run --env-file .vscode/.env pytest backend/tests/external_dependency_unit
HEAD:backend/AGENTS.md:158:uv run --env-file .vscode/.env pytest backend/tests/integration
HEAD:backend/alembic/versions/07b98176f1de_code_interpreter_seed.py:1:"""code interpreter seed
HEAD:backend/alembic/versions/07b98176f1de_code_interpreter_seed.py:20:    # Seed the single instance of code_interpreter_server
HEAD:backend/alembic/versions/07b98176f1de_code_interpreter_seed.py:21:    # NOTE: There should only exist at most and at minimum 1 code_interpreter_server row
HEAD:backend/alembic/versions/07b98176f1de_code_interpreter_seed.py:23:        sa.text("INSERT INTO code_interpreter_server (server_enabled) VALUES (true)")
HEAD:backend/alembic/versions/07b98176f1de_code_interpreter_seed.py:28:    op.execute(sa.text("DELETE FROM code_interpreter_server"))
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:7:- sandbox: User-owned containerized environments (one per user)
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:9:- snapshot: Sandbox filesystem snapshots
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:45:    # Sandbox status enum
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:46:    sandbox_status_enum = sa.Enum(
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:53:        name="sandboxstatus",
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:119:    # SANDBOX TABLE (user-owned, one per user)
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:123:        "sandbox",
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:134:            sandbox_status_enum,
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:146:        sa.UniqueConstraint("user_id", name="sandbox_user_id_key"),
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:150:        "ix_sandbox_status",
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:151:        "sandbox",
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:156:        "ix_sandbox_container_id",
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:157:        "sandbox",
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:335:    # SANDBOX TABLE
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:338:    op.drop_index("ix_sandbox_container_id", table_name="sandbox")
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:339:    op.drop_index("ix_sandbox_status", table_name="sandbox")
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:340:    op.drop_table("sandbox")
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:341:    sa.Enum(name="sandboxstatus").drop(op.get_bind(), checkfirst=True)
HEAD:backend/alembic/versions/2c7f9d3a84a0_add_pat_type_and_encrypted_pat.py:25:        "sandbox",
HEAD:backend/alembic/versions/2c7f9d3a84a0_add_pat_type_and_encrypted_pat.py:31:    op.drop_column("sandbox", "encrypted_pat")
HEAD:backend/alembic/versions/3debc2b55899_durable_craft_provisioning_lifecycle.py:30:        "sandbox",
HEAD:backend/alembic/versions/3debc2b55899_durable_craft_provisioning_lifecycle.py:39:        "sandbox",
HEAD:backend/alembic/versions/3debc2b55899_durable_craft_provisioning_lifecycle.py:45:    # within one user's sandbox (each user has their own pod/container), so
HEAD:backend/alembic/versions/3debc2b55899_durable_craft_provisioning_lifecycle.py:76:    op.drop_column("sandbox", "provisioning_started_at")
HEAD:backend/alembic/versions/3debc2b55899_durable_craft_provisioning_lifecycle.py:77:    op.drop_column("sandbox", "provisioning_attempt_number")
HEAD:backend/alembic/versions/57122d037335_add_python_tool_on_default.py:1:"""add python tool on default
HEAD:backend/alembic/versions/57122d037335_add_python_tool_on_default.py:19:PYTHON_TOOL_NAME = "python"
HEAD:backend/alembic/versions/57122d037335_add_python_tool_on_default.py:25:    # Look up the PythonTool id
HEAD:backend/alembic/versions/57122d037335_add_python_tool_on_default.py:28:        {"name": PYTHON_TOOL_NAME},
HEAD:backend/alembic/versions/57122d037335_add_python_tool_on_default.py:52:        {"name": PYTHON_TOOL_NAME},
HEAD:backend/alembic/versions/7cb492013621_code_interpreter_server_model.py:1:"""code interpreter server model
HEAD:backend/alembic/versions/7cb492013621_code_interpreter_server_model.py:21:        "code_interpreter_server",
HEAD:backend/alembic/versions/7cb492013621_code_interpreter_server_model.py:30:    op.drop_table("code_interpreter_server")
HEAD:backend/alembic/versions/9cc89a7b96de_track_stale_build_session_skills.py:24:        "sandbox",
HEAD:backend/alembic/versions/9cc89a7b96de_track_stale_build_session_skills.py:30:    op.drop_column("sandbox", "skills_hash")
HEAD:backend/alembic/versions/c7e9f4a3b2d1_add_python_tool.py:1:"""add_python_tool
HEAD:backend/alembic/versions/c7e9f4a3b2d1_add_python_tool.py:21:    """Add PythonTool to built-in tools"""
HEAD:backend/alembic/versions/c7e9f4a3b2d1_add_python_tool.py:30:            "name": "PythonTool",
HEAD:backend/alembic/versions/c7e9f4a3b2d1_add_python_tool.py:31:            # in the UI, call it `Code Interpreter` since this is a well known term for this tool
HEAD:backend/alembic/versions/c7e9f4a3b2d1_add_python_tool.py:32:            "display_name": "Code Interpreter",
HEAD:backend/alembic/versions/c7e9f4a3b2d1_add_python_tool.py:34:                "The Code Interpreter Action allows the assistant to execute "
HEAD:backend/alembic/versions/c7e9f4a3b2d1_add_python_tool.py:38:            "in_code_tool_id": "PythonTool",
HEAD:backend/alembic/versions/c7e9f4a3b2d1_add_python_tool.py:43:    # needed to store files generated by the python tool
HEAD:backend/alembic/versions/c7e9f4a3b2d1_add_python_tool.py:55:    """Remove PythonTool from built-in tools"""
HEAD:backend/alembic/versions/c7e9f4a3b2d1_add_python_tool.py:64:            "in_code_tool_id": "PythonTool",
HEAD:backend/alembic/versions/d25168c2beee_tool_name_consistency.py:24:    "PythonTool",
HEAD:backend/alembic/versions/d25168c2beee_tool_name_consistency.py:36:    "PythonTool": "python",
HEAD:backend/alembic/versions/e2875ce6454b_rename_python_tool_llm_facing_name.py:1:"""rename python tool llm facing name
HEAD:backend/alembic/versions/e2875ce6454b_rename_python_tool_llm_facing_name.py:6:Interpreter tool moves to "run_python"; display_name and in_code_tool_id
HEAD:backend/alembic/versions/e2875ce6454b_rename_python_tool_llm_facing_name.py:30:            "WHERE in_code_tool_id = 'PythonTool' AND name = 'python'"
HEAD:backend/alembic/versions/e2875ce6454b_rename_python_tool_llm_facing_name.py:39:            "WHERE in_code_tool_id = 'PythonTool' AND name = 'run_python'"
HEAD:backend/alembic/versions/f3c9e59c3b07_seed_coding_agent_tool.py:24:        "repository. Clones the repo into an isolated sandbox and explores "
HEAD:backend/alembic/versions/fe958f19e42b_add_mcp_config_hash_to_sandbox_and_.py:1:"""add mcp_config_hash to sandbox and build_session
HEAD:backend/alembic/versions/fe958f19e42b_add_mcp_config_hash_to_sandbox_and_.py:22:        "sandbox",
HEAD:backend/alembic/versions/fe958f19e42b_add_mcp_config_hash_to_sandbox_and_.py:33:    op.drop_column("sandbox", "mcp_config_hash")
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:250:    rendered as an active document. `sandbox` stays off: the logo is embedded
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:258:        sandbox=False,
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:141:    bytes alone are not enough: `OnyxRuntime.get_emailable_logo` decodes the
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:69:_TOOL_TYPE_CODE_INTERPRETER = "code_interpreter"
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:144:        if tool_type == _TOOL_TYPE_CODE_INTERPRETER:
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:146:            # A string container references an existing sandbox under our
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:154:                    "code_interpreter tools referencing an existing container "
HEAD:backend/model_server/legacy/reranker.py:79:#             status_code=500, detail="Failed to run Cross-Encoder reranking"
HEAD:backend/onyx/auth/permissions.py:78:    Permission.CRAFT_SANDBOX.value: {
HEAD:backend/onyx/auth/permissions.py:95:        Permission.CRAFT_SANDBOX,
HEAD:backend/onyx/background/README.md:17:| Heavy                     | `apps/heavy.py`                | `connector_pruning`, `connector_doc_permissions_sync`, `connector_external_group_sync`, `csv_generation`, `sandbox`  |
HEAD:backend/onyx/background/README.md:83:Long running, resource intensive tasks, handles pruning and sandbox operations. Low concurrency - max concurrency of 4 with 1 prefetch.
HEAD:backend/onyx/background/README.md:89:Sandbox (new feature) for running Next.js, Python virtual env, OpenCode AI Agent, and access to knowledge files
HEAD:backend/onyx/background/celery/apps/heavy.py:134:            # Sandbox tasks (file sync, cleanup; build feature)
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:23:from onyx.server.features.build.configs import SANDBOX_IDLE_CLEANUP_INTERVAL_SECONDS
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:236:    # Sandbox sweep: background-snapshot changed sessions, sleep idle sandboxes.
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:238:        "name": "cleanup-idle-sandboxes",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:239:        "task": OnyxCeleryTask.CLEANUP_IDLE_SANDBOXES,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:242:        # the effective interval is SANDBOX_IDLE_CLEANUP_INTERVAL_SECONDS * 8;
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:244:        "schedule": timedelta(seconds=SANDBOX_IDLE_CLEANUP_INTERVAL_SECONDS),
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:248:            "queue": OnyxCeleryQueues.SANDBOX,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:1:"""Celery tasks for sandbox operations (cleanup, etc.)."""
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:12:from onyx.db.models import Sandbox
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:15:from onyx.server.features.build.configs import SANDBOX_IDLE_TIMEOUT_SECONDS
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:16:from onyx.server.features.build.db.sandbox import (
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:18:    get_running_sandboxes,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:21:from onyx.server.features.build.sandbox.factory import get_sandbox_manager
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:28:# so the data-loss bound scales with the pace of sandboxes going to sleep.
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:33:    name=OnyxCeleryTask.CLEANUP_IDLE_SANDBOXES,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:38:def cleanup_idle_sandboxes_task(self: Task, *, tenant_id: str) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:39:    """Sweep RUNNING sandboxes: background-snapshot sessions, sleep idle ones.
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:46:    The reap itself is ``sleep_sandbox`` (sandbox lifecycle), which stays
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:47:    fail-closed: snapshot failure on a reachable pod keeps the sandbox
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:51:    from onyx.server.features.build.session.sandbox_lifecycle import (
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:53:        is_sandbox_idle,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:55:        sleep_sandbox,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:58:    task_logger.info(f"cleanup_idle_sandboxes_task starting for tenant {tenant_id}")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:62:        OnyxRedisLocks.CLEANUP_IDLE_SANDBOXES_BEAT_LOCK,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:68:        task_logger.info("cleanup_idle_sandboxes_task - lock not acquired, skipping")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:72:        sandbox_manager = get_sandbox_manager()
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:75:            running_sandboxes = get_running_sandboxes(db_session)
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:76:            if not running_sandboxes:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:77:                task_logger.debug("No running sandboxes found")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:82:            maybe_mark_tenant_active(tenant_id, caller="sandbox_cleanup")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:86:                seconds=SANDBOX_IDLE_TIMEOUT_SECONDS // SNAPSHOT_INTERVAL_DIVISOR
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:89:            # Partition so idle sandboxes are reaped first (reclaiming pods
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:91:            idle_sandboxes: list[Sandbox] = []
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:92:            non_idle_sandboxes: list[Sandbox] = []
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:93:            for sandbox in running_sandboxes:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:95:                    idle_sandboxes
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:96:                    if is_sandbox_idle(sandbox, now)
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:97:                    else non_idle_sandboxes
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:98:                ).append(sandbox)
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:100:            for sandbox in idle_sandboxes:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:102:                    redis_client, sandbox.user_id
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:105:                    sleep_sandbox(
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:107:                        sandbox_manager=sandbox_manager,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:108:                        sandbox=sandbox,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:114:                        f"Failed to sweep sandbox {sandbox.id}: {e}",
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:119:            for sandbox in non_idle_sandboxes:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:120:                sandbox_id = sandbox.id
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:127:                        db_session, sandbox.user_id, snapshot_cutoff
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:132:                        redis_client, sandbox.user_id
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:136:                            "Skipping sandbox %s background snapshot while a "
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:138:                            sandbox.id,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:142:                        # List session directories in the sandbox via the
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:146:                            sandbox_manager,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:147:                            sandbox,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:167:                                sandbox_manager=sandbox_manager,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:169:                                sandbox_id=sandbox_id,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:191:                        and sandbox_manager.supports_opencode_history_persistence
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:194:                            sandbox_manager.create_opencode_history_snapshot(
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:195:                                sandbox_id, tenant_id
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:200:                                f"for sandbox {sandbox_id}: {e}"
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:205:                        f"Failed to sweep sandbox {sandbox_id}: {e}",
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:211:        task_logger.exception("Error in cleanup_idle_sandboxes_task")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:218:    task_logger.info("cleanup_idle_sandboxes_task completed")
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:187:        "sandbox_queue_length": OnyxCeleryQueues.SANDBOX,
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:987:    n_sandbox = celery_get_queue_length(OnyxCeleryQueues.SANDBOX, r_celery)
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:1024:        f"sandbox={n_sandbox} "
HEAD:backend/onyx/chat/chat_processing_checker.py:58:        run_id = int(raw.decode("utf-8") if isinstance(raw, bytes) else str(raw))
HEAD:backend/onyx/chat/chat_utils.py:30:from onyx.context.search.utils import sandbox_filename_for_document
HEAD:backend/onyx/chat/chat_utils.py:115:            "Use the file_reader or python tools to access "
HEAD:backend/onyx/chat/chat_utils.py:540:        # file store id (covers code-interpreter-generated files, etc.).
HEAD:backend/onyx/chat/chat_utils.py:1058:                "file_id=%r has origin=%r, not eligible for code-interpreter staging; skipping.",
HEAD:backend/onyx/chat/chat_utils.py:1072:        filename = sandbox_filename_for_document(doc.semantic_identifier, doc.file_id)
HEAD:backend/onyx/chat/llm_loop.py:73:    PythonToolRichResponse,
HEAD:backend/onyx/chat/llm_loop.py:81:from onyx.tools.tool_implementations.python.python_tool import PythonTool
HEAD:backend/onyx/chat/llm_loop.py:781:        # when a search hit carries an attached file the Python tool should
HEAD:backend/onyx/chat/llm_loop.py:841:        code_interpreter_file_generated: bool = False
HEAD:backend/onyx/chat/llm_loop.py:1010:                include_file_reminder=code_interpreter_file_generated,
HEAD:backend/onyx/chat/llm_loop.py:1165:                # Track if code interpreter generated files with download links
HEAD:backend/onyx/chat/llm_loop.py:1167:                    tool_call.tool_name == PythonTool.NAME
HEAD:backend/onyx/chat/llm_loop.py:1168:                    and not code_interpreter_file_generated
HEAD:backend/onyx/chat/llm_loop.py:1173:                            code_interpreter_file_generated = True
HEAD:backend/onyx/chat/llm_loop.py:1210:                    # the session's chat_files so the next Python tool call
HEAD:backend/onyx/chat/llm_loop.py:1231:                # Extract generated_files if this is a code interpreter response
HEAD:backend/onyx/chat/llm_loop.py:1233:                if isinstance(tool_response.rich_response, PythonToolRichResponse):
HEAD:backend/onyx/chat/process_message.py:223:    """Convert ChatLoadedFile objects to ChatFile for tool usage (e.g., PythonTool).
HEAD:backend/onyx/chat/process_message.py:230:    receive zero-byte content for empty files, which PythonTool handles fine
HEAD:backend/onyx/chat/process_message.py:263:    """Stage tabular project/persona files for code-interpreter as lazy
HEAD:backend/onyx/chat/process_message.py:267:    pulls from the file store only when PythonTool actually accesses
HEAD:backend/onyx/chat/process_message.py:269:    file into RAM for chats that never invoke the Python tool.
HEAD:backend/onyx/chat/process_message.py:296:            # hand PythonTool an empty payload instead of letting the
HEAD:backend/onyx/chat/process_message.py:302:                    "Failed to load context file %s for Python execution: %s",
HEAD:backend/onyx/chat/process_message.py:942:    # Convert loaded files to ChatFile format for tools like PythonTool
HEAD:backend/onyx/chat/prompt_utils.py:24:    PYTHON_TOOL_GUIDANCE,
HEAD:backend/onyx/chat/prompt_utils.py:47:from onyx.tools.tool_implementations.python.python_tool import PythonTool
HEAD:backend/onyx/chat/prompt_utils.py:289:            PYTHON_TOOL_GUIDANCE,
HEAD:backend/onyx/chat/prompt_utils.py:300:        has_python = any(isinstance(tool, PythonTool) for tool in tools)
HEAD:backend/onyx/chat/prompt_utils.py:331:            tool_guidance_sections.append(PYTHON_TOOL_GUIDANCE)
HEAD:backend/onyx/chat/save_chat.py:31:    """Extract FileDescriptors for code interpreter files referenced in the message text."""
HEAD:backend/onyx/chat/save_chat.py:354:    # 8. Attach code interpreter generated files that the assistant actually
HEAD:backend/onyx/coding_agent/mock_tools.py:21:            "repository. The agent clones the repo into an isolated sandbox and "
HEAD:backend/onyx/coding_agent/mock_tools.py:53:            "Run a bash command in the sandboxed session containing the "
HEAD:backend/onyx/configs/app_configs.py:1171:# can be long-running (LLM + tool calls in a sandbox).
HEAD:backend/onyx/configs/app_configs.py:1655:# Code Interpreter Service Configuration
HEAD:backend/onyx/configs/app_configs.py:1656:CODE_INTERPRETER_BASE_URL = os.environ.get(
HEAD:backend/onyx/configs/app_configs.py:1657:    "CODE_INTERPRETER_BASE_URL", "http://localhost:8000"
HEAD:backend/onyx/configs/app_configs.py:1660:CODE_INTERPRETER_DEFAULT_TIMEOUT_MS = int(
HEAD:backend/onyx/configs/app_configs.py:1661:    os.environ.get("CODE_INTERPRETER_DEFAULT_TIMEOUT_MS") or 60_000
HEAD:backend/onyx/configs/app_configs.py:1664:CODE_INTERPRETER_MAX_OUTPUT_LENGTH = int(
HEAD:backend/onyx/configs/app_configs.py:1665:    os.environ.get("CODE_INTERPRETER_MAX_OUTPUT_LENGTH") or 50_000
HEAD:backend/onyx/configs/app_configs.py:1673:CODE_INTERPRETER_MAX_STAGED_FILES = int(
HEAD:backend/onyx/configs/app_configs.py:1674:    os.environ.get("CODE_INTERPRETER_MAX_STAGED_FILES") or 25
HEAD:backend/onyx/configs/app_configs.py:1677:CODE_INTERPRETER_MAX_STAGED_BYTES = int(
HEAD:backend/onyx/configs/app_configs.py:1678:    os.environ.get("CODE_INTERPRETER_MAX_STAGED_BYTES") or 100 * 1024 * 1024
HEAD:backend/onyx/configs/app_configs.py:1682:# store and uploading cache misses to the sandbox — so neither blocks the
HEAD:backend/onyx/configs/app_configs.py:1685:CODE_INTERPRETER_STAGING_CONCURRENCY = int(
HEAD:backend/onyx/configs/app_configs.py:1686:    os.environ.get("CODE_INTERPRETER_STAGING_CONCURRENCY") or 8
HEAD:backend/onyx/configs/constants.py:312:    # Raw files for Craft sandbox access (xlsx, pptx, docx, etc.)
HEAD:backend/onyx/configs/constants.py:427:    SANDBOX_SNAPSHOT = "sandbox_snapshot"
HEAD:backend/onyx/configs/constants.py:498:    # Sandbox processing queue
HEAD:backend/onyx/configs/constants.py:499:    SANDBOX = "sandbox"
HEAD:backend/onyx/configs/constants.py:570:    # Sandbox cleanup
HEAD:backend/onyx/configs/constants.py:571:    CLEANUP_IDLE_SANDBOXES_BEAT_LOCK = "da_lock:cleanup_idle_sandboxes_beat"
HEAD:backend/onyx/configs/constants.py:722:    # Sandbox cleanup
HEAD:backend/onyx/configs/constants.py:723:    CLEANUP_IDLE_SANDBOXES = "cleanup_idle_sandboxes"
HEAD:backend/onyx/connectors/egnyte/connector.py:222:            raise RuntimeError(f"Failed to exchange code for token: {response.text}")
HEAD:backend/onyx/connectors/file/connector.py:190:    # code-interpreter sandbox" signal read by
HEAD:backend/onyx/connectors/linear/connector.py:145:            raise RuntimeError(f"Failed to exchange code for token: {response.text}")
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:80:For a sandbox, use its My Domain host, for example:
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:83:https://company--dev.sandbox.my.salesforce.com
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:116:- Sandbox selection
HEAD:backend/onyx/connectors/salesforce/auth.py:204:            domain="test" if credentials.is_sandbox else None,
HEAD:backend/onyx/connectors/salesforce/models.py:93:    is_sandbox: bool = False
HEAD:backend/onyx/connectors/sharepoint/connector.py:277:    validation; the runtime perm-sync code will surface real failures.
HEAD:backend/onyx/context/search/utils.py:54:_SANDBOX_FILENAME_MAX_LENGTH = 200
HEAD:backend/onyx/context/search/utils.py:179:def sandbox_filename_for_document(title: str, file_id: str) -> str:
HEAD:backend/onyx/context/search/utils.py:181:    unique sandbox filename. Extensions on the title are preserved verbatim."""
HEAD:backend/onyx/context/search/utils.py:187:    max_base_len = max(1, _SANDBOX_FILENAME_MAX_LENGTH - len(suffix))
HEAD:backend/onyx/db/code_interpreter.py:7:def fetch_code_interpreter_server(
HEAD:backend/onyx/db/code_interpreter.py:14:def update_code_interpreter_server_enabled(
HEAD:backend/onyx/db/enums.py:371:    IDLE:         sandbox slept; workspace must be restored before use.
HEAD:backend/onyx/db/enums.py:372:    FAILED:       initialization failed after the sandbox came up; the
HEAD:backend/onyx/db/enums.py:457:    SANDBOX_WAKE_FAILED = "sandbox_wake_failed"
HEAD:backend/onyx/db/enums.py:471:class SandboxStatus(str, PyEnum):
HEAD:backend/onyx/db/enums.py:479:        """Check if sandbox is in an active state (running)."""
HEAD:backend/onyx/db/enums.py:480:        return self == SandboxStatus.RUNNING
HEAD:backend/onyx/db/enums.py:483:        """Check if sandbox is in a terminal state."""
HEAD:backend/onyx/db/enums.py:484:        return self in (SandboxStatus.TERMINATED, SandboxStatus.FAILED)
HEAD:backend/onyx/db/enums.py:487:        """Check if sandbox is sleeping (pod terminated but can be restored)."""
HEAD:backend/onyx/db/enums.py:488:        return self == SandboxStatus.SLEEPING
HEAD:backend/onyx/db/enums.py:690:    CRAFT_SANDBOX = "craft_sandbox"
HEAD:backend/onyx/db/external_app.py:777:    Flush only; the caller refreshes the user's sandbox and commits.
HEAD:backend/onyx/db/mcp.py:16:    SandboxStatus,
HEAD:backend/onyx/db/mcp.py:25:    Sandbox,
HEAD:backend/onyx/db/mcp.py:158:    """User IDs with a RUNNING sandbox whose Craft session should be reloaded
HEAD:backend/onyx/db/mcp.py:160:    edited). Scoped to running sandboxes so the hot-reload push has somewhere to
HEAD:backend/onyx/db/mcp.py:165:    stmt = select(Sandbox.user_id).where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/mcp.py:189:        Sandbox.user_id.in_(group_users)
HEAD:backend/onyx/db/mcp.py:190:        | Sandbox.user_id.in_(direct_users)
HEAD:backend/onyx/db/mcp.py:191:        | Sandbox.user_id.in_(owner_users)
HEAD:backend/onyx/db/mcp.py:192:        | Sandbox.user_id.in_(admin_users)
HEAD:backend/onyx/db/models.py:109:    SandboxStatus,
HEAD:backend/onyx/db/models.py:971:    # FILE_SYSTEM: Write to file system only (for CLI agent sandbox)
HEAD:backend/onyx/db/models.py:4901:    # Immutable Agent Skills name and sandbox directory name.
HEAD:backend/onyx/db/models.py:4916:    # Existing custom rows are classified lazily before sandbox hydration.
HEAD:backend/onyx/db/models.py:6416:        # collide within one user's sandbox.
HEAD:backend/onyx/db/models.py:6427:class Sandbox(Base):
HEAD:backend/onyx/db/models.py:6428:    """Stores sandbox container metadata for users (one sandbox per user)."""
HEAD:backend/onyx/db/models.py:6430:    __tablename__ = "sandbox"
HEAD:backend/onyx/db/models.py:6442:    status: Mapped[SandboxStatus] = mapped_column(
HEAD:backend/onyx/db/models.py:6443:        Enum(SandboxStatus, native_enum=False, name="sandboxstatus"),
HEAD:backend/onyx/db/models.py:6445:        default=SandboxStatus.PROVISIONING,
HEAD:backend/onyx/db/models.py:6472:    # be taken over. Failure diagnostics live in logs (keyed by sandbox ID +
HEAD:backend/onyx/db/models.py:6482:        Index("ix_sandbox_status", "status"),
HEAD:backend/onyx/db/models.py:6483:        Index("ix_sandbox_container_id", "container_id"),
HEAD:backend/onyx/db/models.py:6503:    # path of artifact in sandbox relative to outputs/
HEAD:backend/onyx/db/models.py:6510:    # Content hash from the sandbox manifest. Drives change detection: an
HEAD:backend/onyx/db/models.py:6520:    # Reserved for archived bytes served without the sandbox. NULL until an
HEAD:backend/onyx/db/models.py:6652:    All message data is stored in message_metadata as JSON (the raw sandbox event packet).
HEAD:backend/onyx/db/models.py:7065:    """Details about the code interpreter server"""
HEAD:backend/onyx/db/models.py:7067:    __tablename__ = "code_interpreter_server"
HEAD:backend/onyx/db/skill.py:50:    SandboxStatus,
HEAD:backend/onyx/db/skill.py:59:    Sandbox,
HEAD:backend/onyx/db/skill.py:256:    """Return user IDs with a running sandbox that should contain this skill.
HEAD:backend/onyx/db/skill.py:262:        stmt = select(Sandbox.user_id).where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/skill.py:266:        select(Sandbox.user_id)
HEAD:backend/onyx/db/skill.py:269:            User__UserGroup.user_id == Sandbox.user_id,
HEAD:backend/onyx/db/skill.py:276:        .where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/skill.py:281:        select(Sandbox.user_id)
HEAD:backend/onyx/db/skill.py:284:            Skill__User.user_id == Sandbox.user_id,
HEAD:backend/onyx/db/skill.py:287:        .where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/skill.py:293:            select(Sandbox.user_id)
HEAD:backend/onyx/db/skill.py:294:            .where(Sandbox.user_id == skill.author_user_id)
HEAD:backend/onyx/db/skill.py:295:            .where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/skill.py:322:    """Return the user's effective sandbox skills.
HEAD:backend/onyx/db/users.py:693:    sandbox/session reservation). Hold only for a short transaction."""
HEAD:backend/onyx/evals/README.md:109:    "expected_tools": ["PythonTool"],
HEAD:backend/onyx/evals/README.md:157:- `PythonTool`: Python code execution
HEAD:backend/onyx/external_apps/matching/request.py:12:    """The normalised form of an outbound sandbox request, transport-agnostic.
HEAD:backend/onyx/external_apps/matching/request.py:14:    The proxy builds one of these from whatever the sandbox emitted (the Python
HEAD:backend/onyx/external_apps/providers/notion.py:26:# Pinned across the provider and the sandbox skill so request-shaping stays
HEAD:backend/onyx/file_store/serving.py:40:    sandbox: bool = True,
HEAD:backend/onyx/file_store/serving.py:50:    if sandbox:
HEAD:backend/onyx/file_store/serving.py:51:        headers["Content-Security-Policy"] = "sandbox"
HEAD:backend/onyx/file_store/utils.py:115:        # here so downstream tools (code interpreter, file reader) still
HEAD:backend/onyx/main.py:119:from onyx.server.manage.code_interpreter.api import (
HEAD:backend/onyx/main.py:120:    admin_router as code_interpreter_admin_router,
HEAD:backend/onyx/main.py:337:            "Onyx Craft requires background workers for sandbox lifecycle "
HEAD:backend/onyx/main.py:604:        application, code_interpreter_admin_router
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:10:You operate in a read-only, network-isolated sandbox with the repository checked out at the working directory of every `{BASH_TOOL_NAME}` call. Iteratively call `{BASH_TOOL_NAME}` to inspect the codebase, then call `{GENERATE_ANSWER_TOOL_NAME}` once you have gathered enough evidence to answer the user's query comprehensively.
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:37:A common failure mode is to find 3-4 differences all on one surface (typically control flow, because the entry-point file makes those visible) and stop. If every dimension on your list answers "*how the code executes*", you are missing the dimensions about "*what the code produces*" and "*what concepts the code models*". The output-side differences usually live in the helper functions called by the entry point (the value constructors, result assemblers, and serializers), not in the entry point itself.
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:64:- Network commands (`curl`, `pip install`, `npm install`, `git pull`) — the sandbox has no network.
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:81:You operate in a read-only, network-isolated sandbox with the repository checked out at the working directory of every `{BASH_TOOL_NAME}` call. Reason between calls about what you have learned and what to inspect next. When you have enough evidence to answer the query, call `{GENERATE_ANSWER_TOOL_NAME}`.
HEAD:backend/onyx/prompts/tool_prompts.py:54:PYTHON_TOOL_GUIDANCE = """
HEAD:backend/onyx/prompts/tool_prompts.py:56:Use the `run_python` tool to execute Python code in an isolated sandbox. The tool will respond with the output of the execution or time out after 60.0 seconds.
HEAD:backend/onyx/prompts/tool_prompts.py:63:The sandbox fonts cannot shape Arabic or render CJK glyphs (they come out as disconnected letters or boxes), so for those languages write the rendered text in English and explain the labels in your reply.
HEAD:backend/onyx/prompts/tool_prompts.py:64:IMPORTANT: each call to this tool runs in a fresh, stateless sandbox. Variables, imports, and in-memory state from previous calls will NOT be available, \
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1:"""Gate addon: enforces approval policy on identified sandbox egress.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:3:Fail-closed: identity, body-size cap, and unidentified-sandbox checks.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:36:from onyx.sandbox_proxy import approval_cache
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:37:from onyx.sandbox_proxy.credential_injection import (
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:42:from onyx.sandbox_proxy.errors import SandboxProxyError, http_403
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:43:from onyx.sandbox_proxy.identity import ResolvedSandbox, SessionContext
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:44:from onyx.sandbox_proxy.logging_utils import (
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:57:    sandbox_log_label,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:60:from onyx.sandbox_proxy.request_evaluator import RequestEvaluator
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:64:    SANDBOX_APPROVAL_WAIT_TIMEOUT_SECONDS,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:79:# A sandbox can only egress via the proxy, so the proxy is the single layer that can
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:81:# metadata endpoints) — that destination is invisible at the sandbox's own egress (it sees
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:89:# The single allowed internal destination: the api-server the sandbox calls via the
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:133:    """True if the sandbox must not be relayed to ``host:port``.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:167:    def resolve_sandbox(self, src_ip: str) -> ResolvedSandbox | None: ...
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:287:            flow.response = http_403(SandboxProxyError.DESTINATION_BLOCKED)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:328:        passthrough tunnel — which skips credential injection (the sandbox PAT is
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:329:        never swapped in, so the sandbox's placeholder leaks and the call 401s).
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:351:        Streams the response body to the sandbox instead of buffering it whole.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:379:            flow.response = http_403(SandboxProxyError.DESTINATION_BLOCKED)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:404:                    "approval_dispatch_error tenant=%s sandbox=%s "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:407:                    sandbox_log_label(ctx),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:413:                flow.response = http_403(SandboxProxyError.INTERNAL_ERROR)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:438:                    SandboxProxyError.USER_REJECTED.value
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:440:                    else SandboxProxyError.NOT_AUTHORIZED.value
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:451:                "approval_unhandled_error tenant=%s sandbox=%s session=%s "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:454:                sandbox_log_label(ctx),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:462:            flow.response = http_403(SandboxProxyError.INTERNAL_ERROR)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:480:            sandbox=ctx.without_session(),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:498:                SandboxProxyError.CREDENTIAL_ERROR.value,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:519:          sandbox, oversize body, unattributable gated request).
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:538:            flow.response = http_403(SandboxProxyError.UNIDENTIFIED_SANDBOX)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:542:            sandbox = self._identity.resolve_sandbox(src_ip)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:550:            flow.response = http_403(SandboxProxyError.UNIDENTIFIED_SANDBOX)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:552:        if sandbox is None:
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:555:            # (2) Deployment-shape SNAT masks the sandbox's real bridge IP (e.g.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:556:            # proxy outside the sandbox bridge).
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:558:                "identity_unknown_sandbox src_ip=%s host=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:562:            flow.response = http_403(SandboxProxyError.UNIDENTIFIED_SANDBOX)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:573:                *egress_target_args(flow, sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:574:                SandboxProxyError.BODY_TOO_LARGE.value,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:578:            flow.response = http_403(SandboxProxyError.BODY_TOO_LARGE)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:583:                flow.request, sandbox.tenant_id, sandbox.user_id
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:590:                "matcher_error tenant=%s sandbox=%s host=%s error=%r",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:591:                sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:592:                sandbox_log_label(sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:606:                sandbox=sandbox,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:614:                    *egress_target_args(flow, sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:615:                    SandboxProxyError.CREDENTIAL_ERROR.value,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:623:                    *egress_target_args(flow, sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:630:            flow.response = http_403(SandboxProxyError.POLICY_DENIED)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:634:                    flow, sandbox, matched_actions, EndpointPolicy.DENY
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:636:                SandboxProxyError.POLICY_DENIED.value,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:647:                sandbox=sandbox,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:656:                        flow, sandbox, matched_actions, EndpointPolicy.ALWAYS
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:658:                    SandboxProxyError.CREDENTIAL_ERROR.value,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:665:                        flow, sandbox, matched_actions, EndpointPolicy.ALWAYS
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:674:            session_id = self._resolve_gated_session(flow, sandbox)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:677:                "session_lookup_error tenant=%s sandbox=%s host=%s app_name=%r "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:679:                sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:680:                sandbox_log_label(sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:685:            flow.response = http_403(SandboxProxyError.NO_ACTIVE_SESSION)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:691:                    flow, sandbox, matched_actions, EndpointPolicy.ASK
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:693:                SandboxProxyError.NO_ACTIVE_SESSION.value,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:695:            flow.response = http_403(SandboxProxyError.NO_ACTIVE_SESSION)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:698:        ctx = sandbox.with_session(session_id)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:700:            "approval_match tenant=%s sandbox=%s session=%s host=%s "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:703:            sandbox_log_label(ctx),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:817:                "approval_grant_check_error tenant=%s sandbox=%s "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:821:                sandbox_log_label(ctx),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:928:            "approval_requested tenant=%s sandbox=%s session=%s approval=%s "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:932:            sandbox_log_label(ctx),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:970:                approval_id, SANDBOX_APPROVAL_WAIT_TIMEOUT_SECONDS, cache
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1000:            # Sandbox socket closed mid-wait. Terminalize the audit row, then
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1042:            SandboxProxyError.USER_REJECTED
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1044:            else SandboxProxyError.NOT_AUTHORIZED
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1052:        sandbox: ResolvedSandbox,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1059:                sandbox=sandbox,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1065:                SandboxProxyError.CREDENTIAL_ERROR, detail=result.block_detail
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1231:        self, flow: http.HTTPFlow, sandbox: ResolvedSandbox
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1242:                "session_missing tenant=%s sandbox=%s host=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1243:                sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1244:                sandbox_log_label(sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1252:                "session_malformed tenant=%s sandbox=%s host=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1253:                sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1254:                sandbox_log_label(sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1259:            tagged_id, sandbox.user_id, sandbox.tenant_id
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1264:                "session_unverified tenant=%s sandbox=%s session=%s host=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1265:                sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1266:                sandbox_log_label(sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1272:            "session_verified tenant=%s sandbox=%s session=%s host=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1273:            sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1274:            sandbox_log_label(sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1294:        # the sandbox is one trust domain per user, so a compromised process can
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1296:        # nothing (the value is stored in-sandbox in plaintext). Cross-user is
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1297:        # still blocked by the src-IP-pinned sandbox identity in resolve_sandbox.
HEAD:backend/onyx/sandbox_proxy/backend.py:5:correctly under either ``SANDBOX_BACKEND`` value.
HEAD:backend/onyx/sandbox_proxy/backend.py:14:from onyx.sandbox_proxy.ca import CAStore
HEAD:backend/onyx/sandbox_proxy/backend.py:15:from onyx.sandbox_proxy.identity import SandboxIPLookup
HEAD:backend/onyx/sandbox_proxy/backend.py:16:from onyx.server.features.build.configs import SANDBOX_BACKEND, SandboxBackend
HEAD:backend/onyx/sandbox_proxy/backend.py:20:    if SANDBOX_BACKEND is SandboxBackend.KUBERNETES:
HEAD:backend/onyx/sandbox_proxy/backend.py:21:        from onyx.sandbox_proxy.ca_k8s import K8sSecretCAStore
HEAD:backend/onyx/sandbox_proxy/backend.py:24:    if SANDBOX_BACKEND is SandboxBackend.DOCKER:
HEAD:backend/onyx/sandbox_proxy/backend.py:25:        from onyx.sandbox_proxy.ca_docker import FileCAStore
HEAD:backend/onyx/sandbox_proxy/backend.py:28:    raise RuntimeError(f"Unsupported SANDBOX_BACKEND={SANDBOX_BACKEND!r}.")
HEAD:backend/onyx/sandbox_proxy/backend.py:31:def build_ip_lookup() -> SandboxIPLookup:
HEAD:backend/onyx/sandbox_proxy/backend.py:32:    if SANDBOX_BACKEND is SandboxBackend.KUBERNETES:
HEAD:backend/onyx/sandbox_proxy/backend.py:33:        from onyx.sandbox_proxy.identity_k8s import K8sInformerLookup
HEAD:backend/onyx/sandbox_proxy/backend.py:36:    if SANDBOX_BACKEND is SandboxBackend.DOCKER:
HEAD:backend/onyx/sandbox_proxy/backend.py:37:        from onyx.sandbox_proxy.identity_docker import DockerEventsLookup
HEAD:backend/onyx/sandbox_proxy/backend.py:40:    raise RuntimeError(f"Unsupported SANDBOX_BACKEND={SANDBOX_BACKEND!r}.")
HEAD:backend/onyx/sandbox_proxy/ca.py:1:"""CA bootstrap for the sandbox egress proxy."""
HEAD:backend/onyx/sandbox_proxy/ca.py:18:_CA_COMMON_NAME = "Onyx Sandbox Proxy CA"
HEAD:backend/onyx/sandbox_proxy/ca.py:22:_DEFAULT_CA_PEM_PATH = "/var/run/sandbox-proxy/mitmproxy-confdir/mitmproxy-ca.pem"
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:4:read-write so it can persist on cold start; every sandbox container mounts it
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:6:That mount also makes ``ca.key`` present in Docker sandbox filesystems; the
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:7:key is protected by ``0600`` root ownership, and the sandbox agent runs as
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:11:``sandbox-proxy`` replica, so the cold-start race is not a routine concern in
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:16:   sandbox-proxy=2``. Without ``O_EXCL`` both replicas would race-overwrite each
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:17:   other's key, leaving sandbox trust stores pointing at a cert whose private
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:35:from onyx.sandbox_proxy.ca import CAStore, CAStoreConflictError
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:36:from onyx.server.features.build.configs import SANDBOX_PROXY_CA_VOLUME_PATH
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:54:            ca.crt   # public cert, world-readable; mounted into sandboxes
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:55:            ca.key   # private key, mode 0600; root-only in Docker sandboxes
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:63:    def __init__(self, root: str | Path = SANDBOX_PROXY_CA_VOLUME_PATH) -> None:
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:76:            # regenerating and orphaning the cert that sandboxes may have
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:113:        # a truncated CA would propagate silently into every sandbox's trust
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:118:        # doesn't leave sandboxes unable to read the cert.
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:4:ConfigMap in the sandbox namespace mirrors only the public cert so
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:5:sandbox init containers can mount it (K8s does not allow
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:16:from onyx.sandbox_proxy.ca import CAStore, CAStoreConflictError
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:18:    SANDBOX_NAMESPACE,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:19:    SANDBOX_PROXY_CA_CONFIGMAP,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:20:    SANDBOX_PROXY_CA_SECRET,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:21:    SANDBOX_PROXY_NAMESPACE,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:23:from onyx.server.features.build.sandbox.kubernetes.k8s_client import build_core_v1_api
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:24:from onyx.server.features.build.sandbox.labels import (
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:38:_COMPONENT_VALUE_PROXY = "sandbox-proxy"
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:40:_SECRET_RESOURCE_LABEL = "sandbox-proxy-ca"
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:41:_CONFIGMAP_RESOURCE_LABEL = "sandbox-proxy-ca-bundle"
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:58:        proxy_namespace: str = SANDBOX_PROXY_NAMESPACE,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:59:        sandbox_namespace: str = SANDBOX_NAMESPACE,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:60:        secret_name: str = SANDBOX_PROXY_CA_SECRET,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:61:        configmap_name: str = SANDBOX_PROXY_CA_CONFIGMAP,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:67:        self._sandbox_ns = sandbox_namespace
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:84:            # Fail loud: regenerating would invalidate sandboxes already
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:146:                namespace=self._sandbox_ns,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:158:                namespace=self._sandbox_ns,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:173:                    namespace=self._sandbox_ns,
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:1:"""Host-claim dispatcher for sandbox-proxy credential injection.
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:6:real secret never has to live in the sandbox pod. Resolution outcomes are
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:21:from onyx.sandbox_proxy.identity import ResolvedSandbox
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:30:    `sandbox_detail`, when set, is agent-facing 403-body prose — never secrets
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:34:    def __init__(self, message: str, *, sandbox_detail: str | None = None) -> None:
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:36:        self.sandbox_detail = sandbox_detail
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:44:    `external_app_id`), or `None` on off-catalog forwards. `sandbox.tenant_id` is
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:48:    sandbox: ResolvedSandbox
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:59:        `ctx.sandbox.tenant_id` for per-context routing). Avoid opening a DB
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:111:                outcome=InjectionOutcome.BLOCKED, block_detail=e.sandbox_detail
HEAD:backend/onyx/sandbox_proxy/errors.py:1:"""Sandbox-facing 403 error codes and response builder.
HEAD:backend/onyx/sandbox_proxy/errors.py:3:Every 403 the proxy returns to the sandbox carries a stable `error` code plus a
HEAD:backend/onyx/sandbox_proxy/errors.py:4:human-readable `message`. The agent running in the sandbox reads the `message`
HEAD:backend/onyx/sandbox_proxy/errors.py:19:class SandboxProxyError(str, Enum):
HEAD:backend/onyx/sandbox_proxy/errors.py:20:    """Stable `error` codes returned to the sandbox in a 403 body."""
HEAD:backend/onyx/sandbox_proxy/errors.py:22:    UNIDENTIFIED_SANDBOX = "unidentified_sandbox"
HEAD:backend/onyx/sandbox_proxy/errors.py:36:        Addressed to the agent in the sandbox that receives the 403.
HEAD:backend/onyx/sandbox_proxy/errors.py:38:        return _SANDBOX_ERROR_MESSAGES[self]
HEAD:backend/onyx/sandbox_proxy/errors.py:41:_SANDBOX_ERROR_MESSAGES: dict[SandboxProxyError, str] = {
HEAD:backend/onyx/sandbox_proxy/errors.py:42:    SandboxProxyError.UNIDENTIFIED_SANDBOX: (
HEAD:backend/onyx/sandbox_proxy/errors.py:49:    SandboxProxyError.NO_ACTIVE_SESSION: (
HEAD:backend/onyx/sandbox_proxy/errors.py:56:    SandboxProxyError.BODY_TOO_LARGE: (
HEAD:backend/onyx/sandbox_proxy/errors.py:63:    SandboxProxyError.USER_REJECTED: (
HEAD:backend/onyx/sandbox_proxy/errors.py:69:    SandboxProxyError.NOT_AUTHORIZED: (
HEAD:backend/onyx/sandbox_proxy/errors.py:76:    SandboxProxyError.INTERNAL_ERROR: (
HEAD:backend/onyx/sandbox_proxy/errors.py:82:    SandboxProxyError.POLICY_DENIED: (
HEAD:backend/onyx/sandbox_proxy/errors.py:89:    SandboxProxyError.CREDENTIAL_ERROR: (
HEAD:backend/onyx/sandbox_proxy/errors.py:96:    SandboxProxyError.DESTINATION_BLOCKED: (
HEAD:backend/onyx/sandbox_proxy/errors.py:97:        "This request targets an internal network address that sandboxes are not "
HEAD:backend/onyx/sandbox_proxy/errors.py:106:def http_403(code: SandboxProxyError, detail: str | None = None) -> http.Response:
HEAD:backend/onyx/sandbox_proxy/errors.py:107:    """Build a sandbox-visible 403.
HEAD:backend/onyx/sandbox_proxy/identity.py:1:"""Source-IP -> sandbox identity + in-band session resolution.
HEAD:backend/onyx/sandbox_proxy/identity.py:7:- `resolve_sandbox()` — pod IP -> sandbox + user + tenant; enforces "only known
HEAD:backend/onyx/sandbox_proxy/identity.py:8:  sandbox pods may egress".
HEAD:backend/onyx/sandbox_proxy/identity.py:23:from onyx.db.models import BuildSession, Sandbox
HEAD:backend/onyx/sandbox_proxy/identity.py:30:class SandboxIdentity:
HEAD:backend/onyx/sandbox_proxy/identity.py:31:    sandbox_id: UUID
HEAD:backend/onyx/sandbox_proxy/identity.py:33:    sandbox_name: str
HEAD:backend/onyx/sandbox_proxy/identity.py:34:    sandbox_ip: str
HEAD:backend/onyx/sandbox_proxy/identity.py:38:class ResolvedSandbox:
HEAD:backend/onyx/sandbox_proxy/identity.py:39:    """Sandbox identity + owning user. Authorizes egress."""
HEAD:backend/onyx/sandbox_proxy/identity.py:41:    sandbox_id: UUID
HEAD:backend/onyx/sandbox_proxy/identity.py:44:    sandbox_name: str
HEAD:backend/onyx/sandbox_proxy/identity.py:45:    sandbox_ip: str
HEAD:backend/onyx/sandbox_proxy/identity.py:51:            sandbox_id=self.sandbox_id,
HEAD:backend/onyx/sandbox_proxy/identity.py:53:            sandbox_name=self.sandbox_name,
HEAD:backend/onyx/sandbox_proxy/identity.py:54:            sandbox_ip=self.sandbox_ip,
HEAD:backend/onyx/sandbox_proxy/identity.py:60:    """Sandbox identity + the verified session to route the card to."""
HEAD:backend/onyx/sandbox_proxy/identity.py:64:    sandbox_id: UUID
HEAD:backend/onyx/sandbox_proxy/identity.py:66:    sandbox_name: str
HEAD:backend/onyx/sandbox_proxy/identity.py:67:    sandbox_ip: str
HEAD:backend/onyx/sandbox_proxy/identity.py:69:    def without_session(self) -> ResolvedSandbox:
HEAD:backend/onyx/sandbox_proxy/identity.py:71:        Inverse of `ResolvedSandbox.with_session(...)` — drops the session id.
HEAD:backend/onyx/sandbox_proxy/identity.py:73:        return ResolvedSandbox(
HEAD:backend/onyx/sandbox_proxy/identity.py:74:            sandbox_id=self.sandbox_id,
HEAD:backend/onyx/sandbox_proxy/identity.py:77:            sandbox_name=self.sandbox_name,
HEAD:backend/onyx/sandbox_proxy/identity.py:78:            sandbox_ip=self.sandbox_ip,
HEAD:backend/onyx/sandbox_proxy/identity.py:82:class SandboxIPLookup(Protocol):
HEAD:backend/onyx/sandbox_proxy/identity.py:83:    """Backend-specific IP -> SandboxIdentity resolver.
HEAD:backend/onyx/sandbox_proxy/identity.py:91:    def lookup(self, src_ip: str) -> SandboxIdentity | None: ...
HEAD:backend/onyx/sandbox_proxy/identity.py:101:    def __init__(self, ip_lookup: SandboxIPLookup) -> None:
HEAD:backend/onyx/sandbox_proxy/identity.py:104:    def resolve_sandbox(self, src_ip: str) -> ResolvedSandbox | None:
HEAD:backend/onyx/sandbox_proxy/identity.py:106:        Pod IP -> owning user + tenant; `None` if IP unknown or sandbox has no
HEAD:backend/onyx/sandbox_proxy/identity.py:118:                select(Sandbox.user_id).where(Sandbox.id == identity.sandbox_id)
HEAD:backend/onyx/sandbox_proxy/identity.py:123:        return ResolvedSandbox(
HEAD:backend/onyx/sandbox_proxy/identity.py:124:            sandbox_id=identity.sandbox_id,
HEAD:backend/onyx/sandbox_proxy/identity.py:127:            sandbox_name=identity.sandbox_name,
HEAD:backend/onyx/sandbox_proxy/identity.py:128:            sandbox_ip=identity.sandbox_ip,
HEAD:backend/onyx/sandbox_proxy/identity.py:134:        """Validates a sandbox-supplied `BuildSession` id against its owner.
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:1:"""Docker-compose implementation of ``SandboxIPLookup``.
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:3:Background thread streams ``DockerClient.events()`` filtered to sandbox
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:4:containers and maintains a ``{container_ip: SandboxIdentity}`` cache. On any
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:24:from onyx.sandbox_proxy.identity import SandboxIdentity, SandboxIPLookup
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:26:    SANDBOX_DOCKER_NETWORK,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:27:    SANDBOX_DOCKER_SOCKET,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:29:from onyx.server.features.build.sandbox.labels import (
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:31:    LABEL_DOCKER_COMPONENT_SANDBOX,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:32:    LABEL_SANDBOX_ID,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:53:) -> SandboxIdentity | None:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:54:    """Builds a ``SandboxIdentity`` from a container's labels + bridge IP.
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:56:    Returns ``None`` for containers that aren't sandbox-labelled, are missing
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:57:    the sandbox/tenant labels, have a non-UUID sandbox-id, or have no IP on the
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:58:    configured sandbox bridge yet (i.e. a sandbox in a creation race that hasn't
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:65:    if labels.get(LABEL_DOCKER_COMPONENT) != LABEL_DOCKER_COMPONENT_SANDBOX:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:68:    sandbox_id_raw = labels.get(LABEL_SANDBOX_ID)
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:70:    if not sandbox_id_raw or not tenant_id:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:74:        sandbox_id = UUID(sandbox_id_raw)
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:77:            "Skipping sandbox container %s with non-UUID sandbox-id label %r",
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:79:            sandbox_id_raw,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:91:    return SandboxIdentity(
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:92:        sandbox_id=sandbox_id,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:94:        sandbox_name=container.name or "",
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:95:        sandbox_ip=ip,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:99:class DockerEventsLookup(SandboxIPLookup):
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:105:        network: str = SANDBOX_DOCKER_NETWORK,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:108:            docker_client = DockerClient(base_url=f"unix://{SANDBOX_DOCKER_SOCKET}")
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:112:        self._cache: dict[str, SandboxIdentity] = {}
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:130:            target=self._run, name="sandbox-proxy-docker-events", daemon=True
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:153:    def lookup(self, src_ip: str) -> SandboxIdentity | None:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:164:                # silently drops events: a sandbox starting in that window would
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:201:                "label": f"{LABEL_DOCKER_COMPONENT}={LABEL_DOCKER_COMPONENT_SANDBOX}"
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:204:        new_cache: dict[str, SandboxIdentity] = {}
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:216:            existing = new_cache.get(identity.sandbox_ip)
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:217:            if existing is not None and existing.sandbox_id != identity.sandbox_id:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:219:                    f"Duplicate sandbox IP {identity.sandbox_ip} mapped to "
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:220:                    f"{existing.sandbox_id} and {identity.sandbox_id}; "
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:223:            new_cache[identity.sandbox_ip] = identity
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:224:            new_by_id[c.id] = identity.sandbox_ip
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:231:            "Docker events initial sync: %d sandbox containers cached.", len(new_cache)
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:240:                "label": f"{LABEL_DOCKER_COMPONENT}={LABEL_DOCKER_COMPONENT_SANDBOX}",
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:283:                if stale_ip is not None and stale_ip != identity.sandbox_ip:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:293:                # un-identifying the new container. Don't gate on sandbox_id --
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:294:                # a sandbox restart keeps the sandbox_id label but gets a fresh
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:299:                    if ip == identity.sandbox_ip and cid != container_id
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:306:                        "for %s (new container=%s, sandbox_id=%s).",
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:307:                        identity.sandbox_ip,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:310:                        identity.sandbox_id,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:313:                self._cache[identity.sandbox_ip] = identity
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:314:                self._by_id[container_id] = identity.sandbox_ip
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:1:"""Kubernetes implementation of `SandboxIPLookup`.
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:3:Background thread watches sandbox pods and maintains a `{pod_ip:
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:4:SandboxIdentity}` cache. On any error or EOF the watch loop reconnects with
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:15:from onyx.sandbox_proxy.identity import SandboxIdentity, SandboxIPLookup
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:16:from onyx.server.features.build.configs import SANDBOX_NAMESPACE
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:17:from onyx.server.features.build.sandbox.kubernetes.k8s_client import build_core_v1_api
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:18:from onyx.server.features.build.sandbox.labels import (
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:20:    LABEL_K8S_COMPONENT_SANDBOX,
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:23:    LABEL_SANDBOX_ID,
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:37:_SANDBOX_POD_SELECTOR = ",".join(
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:39:        f"{LABEL_K8S_COMPONENT}={LABEL_K8S_COMPONENT_SANDBOX}",
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:47:def _identity_from_pod(pod: client.V1Pod) -> SandboxIdentity | None:
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:61:    sandbox_id_raw = labels.get(LABEL_SANDBOX_ID)
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:63:    if not sandbox_id_raw or not tenant_id:
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:67:        sandbox_id = UUID(sandbox_id_raw)
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:70:            "Skipping sandbox pod %s with non-UUID sandbox-id label %r",
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:72:            sandbox_id_raw,
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:76:    return SandboxIdentity(
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:77:        sandbox_id=sandbox_id,
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:79:        sandbox_name=metadata.name or "",
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:80:        sandbox_ip=status.pod_ip,
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:84:class K8sInformerLookup(SandboxIPLookup):
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:88:        namespace: str = SANDBOX_NAMESPACE,
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:94:        self._cache: dict[str, SandboxIdentity] = {}
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:102:            target=self._run, name="sandbox-proxy-informer", daemon=True
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:119:    def lookup(self, src_ip: str) -> SandboxIdentity | None:
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:170:            label_selector=_SANDBOX_POD_SELECTOR,
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:172:        new_cache: dict[str, SandboxIdentity] = {}
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:177:            existing = new_cache.get(identity.sandbox_ip)
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:178:            if existing is not None and existing.sandbox_id != identity.sandbox_id:
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:182:                    f"Duplicate sandbox IP {identity.sandbox_ip} mapped to {existing.sandbox_id} "
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:183:                    f"and {identity.sandbox_id}; Refusing to serve traffic with ambiguous identity."
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:185:            new_cache[identity.sandbox_ip] = identity
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:190:        logger.info("Informer initial sync: %d sandbox pods cached.", len(new_cache))
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:207:                label_selector=_SANDBOX_POD_SELECTOR,
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:243:                if cached_identity.sandbox_name == pod_name
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:244:                and cached_ip != identity.sandbox_ip
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:248:            self._cache[identity.sandbox_ip] = identity
HEAD:backend/onyx/sandbox_proxy/identity_k8s.py:255:                if cached_identity.sandbox_name == pod_name
HEAD:backend/onyx/sandbox_proxy/logging_utils.py:1:"""Shared rendering helpers for sandbox proxy logs."""
HEAD:backend/onyx/sandbox_proxy/logging_utils.py:9:from onyx.sandbox_proxy.credential_injection import InjectionOutcome
HEAD:backend/onyx/sandbox_proxy/logging_utils.py:10:from onyx.sandbox_proxy.identity import ResolvedSandbox, SessionContext
HEAD:backend/onyx/sandbox_proxy/logging_utils.py:12:_EGRESS_CONTEXT_FIELDS = "tenant=%s sandbox=%s"
HEAD:backend/onyx/sandbox_proxy/logging_utils.py:52:def sandbox_log_label(sandbox: ResolvedSandbox | SessionContext) -> str:
HEAD:backend/onyx/sandbox_proxy/logging_utils.py:53:    return sandbox.sandbox_name or short_log_id(sandbox.sandbox_id)
HEAD:backend/onyx/sandbox_proxy/logging_utils.py:70:def _egress_context_args(sandbox: ResolvedSandbox | SessionContext) -> tuple[str, str]:
HEAD:backend/onyx/sandbox_proxy/logging_utils.py:71:    return sandbox.tenant_id, sandbox_log_label(sandbox)
HEAD:backend/onyx/sandbox_proxy/logging_utils.py:91:    flow: http.HTTPFlow, sandbox: ResolvedSandbox | SessionContext
HEAD:backend/onyx/sandbox_proxy/logging_utils.py:94:        *_egress_context_args(sandbox),
HEAD:backend/onyx/sandbox_proxy/logging_utils.py:101:    sandbox: ResolvedSandbox | SessionContext,
HEAD:backend/onyx/sandbox_proxy/logging_utils.py:106:        *egress_target_args(flow, sandbox),
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:35:from onyx.sandbox_proxy.mcp_jsonrpc import (
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:40:from onyx.sandbox_proxy.resolvers.mcp_matching import (
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:150:    rule the credential resolver uses, scoped to the servers the sandbox user may
HEAD:backend/onyx/sandbox_proxy/resolvers/external_app.py:17:from onyx.sandbox_proxy.credential_injection import (
HEAD:backend/onyx/sandbox_proxy/resolvers/external_app.py:59:            ctx.sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/resolvers/external_app.py:61:            ctx.sandbox.user_id,
HEAD:backend/onyx/sandbox_proxy/resolvers/external_app.py:64:        with get_session_with_tenant(tenant_id=ctx.sandbox.tenant_id) as db:
HEAD:backend/onyx/sandbox_proxy/resolvers/external_app.py:66:                db, external_app_id, ctx.sandbox.user_id
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:4:craft-enabled `MCPServer` (if any) a sandbox request belongs to — otherwise a
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:3:Claims sandbox egress to a craft-enabled `MCPServer`'s `server_url` and injects
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:4:the sandbox owner's credentials from the same `mcp_connection_config` rows chat
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:32:from onyx.sandbox_proxy.credential_injection import (
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:37:from onyx.sandbox_proxy.logging_utils import short_log_id
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:38:from onyx.sandbox_proxy.mcp_jsonrpc import McpRpcKind, classify_mcp_request
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:39:from onyx.sandbox_proxy.resolvers.mcp_matching import (
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:88:                self._targets(ctx.sandbox.tenant_id),
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:111:                sandbox_detail=(
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:118:                self._user_targets(ctx.sandbox.tenant_id, ctx.sandbox.user_id), request
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:123:                sandbox_detail=(
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:135:                sandbox_detail=(
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:147:        tenant_id = ctx.sandbox.tenant_id
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:148:        user_id = ctx.sandbox.user_id
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:156:                    sandbox_detail=_connect_detail(server.name, admin_managed),
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:161:                    f"sandbox user {short_log_id(user_id)} not found"
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:173:                    str(e), sandbox_detail=_connect_detail(server.name, admin_managed)
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:194:                    sandbox_detail=_reconnect_detail(server.name, admin_managed),
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:202:                sandbox_detail=_connect_detail(server.name, admin_managed),
HEAD:backend/onyx/sandbox_proxy/resolvers/onyx_pat.py:4:and sets both auth headers to the sandbox's real per-sandbox PAT, read
HEAD:backend/onyx/sandbox_proxy/resolvers/onyx_pat.py:5:encrypted off ``Sandbox.encrypted_pat``. The tenant is embedded in the PAT
HEAD:backend/onyx/sandbox_proxy/resolvers/onyx_pat.py:21:from onyx.sandbox_proxy.credential_injection import (
HEAD:backend/onyx/sandbox_proxy/resolvers/onyx_pat.py:26:from onyx.sandbox_proxy.logging_utils import full_log_id, short_log_id
HEAD:backend/onyx/sandbox_proxy/resolvers/onyx_pat.py:28:from onyx.server.features.build.db.sandbox import get_sandbox_by_id
HEAD:backend/onyx/sandbox_proxy/resolvers/onyx_pat.py:35:    """Injects the sandbox's Onyx API PAT on requests to the configured API host."""
HEAD:backend/onyx/sandbox_proxy/resolvers/onyx_pat.py:58:        sandbox_id = ctx.sandbox.sandbox_id
HEAD:backend/onyx/sandbox_proxy/resolvers/onyx_pat.py:59:        with get_session_with_tenant(tenant_id=ctx.sandbox.tenant_id) as db:
HEAD:backend/onyx/sandbox_proxy/resolvers/onyx_pat.py:60:            sandbox = get_sandbox_by_id(db, sandbox_id)
HEAD:backend/onyx/sandbox_proxy/resolvers/onyx_pat.py:61:            if sandbox is None:
HEAD:backend/onyx/sandbox_proxy/resolvers/onyx_pat.py:63:                    f"sandbox {full_log_id(sandbox_id)} not found"
HEAD:backend/onyx/sandbox_proxy/resolvers/onyx_pat.py:65:            if sandbox.encrypted_pat is None:
```
Code execution changes the risk model substantially because generated or
user-influenced instructions can become executable behavior.
No code was executed.
## Execution Resource / Network / File Controls
Evidence lines: 600
```text
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:7:- sandbox: User-owned containerized environments (one per user)
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:9:- snapshot: Sandbox filesystem snapshots
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:45:    # Sandbox status enum
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:46:    sandbox_status_enum = sa.Enum(
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:53:        name="sandboxstatus",
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:119:    # SANDBOX TABLE (user-owned, one per user)
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:123:        "sandbox",
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:134:            sandbox_status_enum,
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:146:        sa.UniqueConstraint("user_id", name="sandbox_user_id_key"),
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:150:        "ix_sandbox_status",
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:151:        "sandbox",
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:156:        "ix_sandbox_container_id",
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:157:        "sandbox",
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:335:    # SANDBOX TABLE
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:338:    op.drop_index("ix_sandbox_container_id", table_name="sandbox")
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:339:    op.drop_index("ix_sandbox_status", table_name="sandbox")
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:340:    op.drop_table("sandbox")
HEAD:backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py:341:    sa.Enum(name="sandboxstatus").drop(op.get_bind(), checkfirst=True)
HEAD:backend/alembic/versions/2c7f9d3a84a0_add_pat_type_and_encrypted_pat.py:25:        "sandbox",
HEAD:backend/alembic/versions/2c7f9d3a84a0_add_pat_type_and_encrypted_pat.py:31:    op.drop_column("sandbox", "encrypted_pat")
HEAD:backend/alembic/versions/3debc2b55899_durable_craft_provisioning_lifecycle.py:30:        "sandbox",
HEAD:backend/alembic/versions/3debc2b55899_durable_craft_provisioning_lifecycle.py:39:        "sandbox",
HEAD:backend/alembic/versions/3debc2b55899_durable_craft_provisioning_lifecycle.py:45:    # within one user's sandbox (each user has their own pod/container), so
HEAD:backend/alembic/versions/3debc2b55899_durable_craft_provisioning_lifecycle.py:76:    op.drop_column("sandbox", "provisioning_started_at")
HEAD:backend/alembic/versions/3debc2b55899_durable_craft_provisioning_lifecycle.py:77:    op.drop_column("sandbox", "provisioning_attempt_number")
HEAD:backend/alembic/versions/689433b0d8de_add_hook_and_hook_execution_log_tables.py:38:        sa.Column("timeout_seconds", sa.Float(), nullable=False),
HEAD:backend/alembic/versions/9cc89a7b96de_track_stale_build_session_skills.py:24:        "sandbox",
HEAD:backend/alembic/versions/9cc89a7b96de_track_stale_build_session_skills.py:30:    op.drop_column("sandbox", "skills_hash")
HEAD:backend/alembic/versions/a01bf2971c5d_update_default_tool_descriptions.py:26:        "The Web Search Action allows the agent to perform internet searches for up-to-date information."
HEAD:backend/alembic/versions/b51c6844d1df_seed_memory_tool.py:1:"""seed_memory_tool and add enable_memory_tool to user
HEAD:backend/alembic/versions/b51c6844d1df_seed_memory_tool.py:19:MEMORY_TOOL = {
HEAD:backend/alembic/versions/b51c6844d1df_seed_memory_tool.py:20:    "name": "MemoryTool",
HEAD:backend/alembic/versions/b51c6844d1df_seed_memory_tool.py:21:    "display_name": "Add Memory",
HEAD:backend/alembic/versions/b51c6844d1df_seed_memory_tool.py:23:    "in_code_tool_id": "MemoryTool",
HEAD:backend/alembic/versions/b51c6844d1df_seed_memory_tool.py:35:        {"in_code_tool_id": MEMORY_TOOL["in_code_tool_id"]},
HEAD:backend/alembic/versions/b51c6844d1df_seed_memory_tool.py:47:            MEMORY_TOOL,
HEAD:backend/alembic/versions/b51c6844d1df_seed_memory_tool.py:55:            MEMORY_TOOL,
HEAD:backend/alembic/versions/b51c6844d1df_seed_memory_tool.py:61:            "enable_memory_tool",
HEAD:backend/alembic/versions/b51c6844d1df_seed_memory_tool.py:70:    op.drop_column("user", "enable_memory_tool")
HEAD:backend/alembic/versions/b51c6844d1df_seed_memory_tool.py:75:        {"in_code_tool_id": MEMORY_TOOL["in_code_tool_id"]},
HEAD:backend/alembic/versions/d09fc20a3c66_seed_builtin_tools.py:41:            "The Web Search Action allows the assistant to perform internet searches for up-to-date information."
HEAD:backend/alembic/versions/d09fc20a3c66_seed_builtin_tools.py:81:        # Handle historical rename: InternetSearchTool -> WebSearchTool
HEAD:backend/alembic/versions/d09fc20a3c66_seed_builtin_tools.py:85:            and "InternetSearchTool" in existing_tool_ids
HEAD:backend/alembic/versions/d09fc20a3c66_seed_builtin_tools.py:87:            # Rename the existing InternetSearchTool row in place and update fields
HEAD:backend/alembic/versions/d09fc20a3c66_seed_builtin_tools.py:95:                    WHERE in_code_tool_id = 'InternetSearchTool'
HEAD:backend/alembic/versions/d09fc20a3c66_seed_builtin_tools.py:100:            existing_tool_ids.discard("InternetSearchTool")
HEAD:backend/alembic/versions/f3c9e59c3b07_seed_coding_agent_tool.py:24:        "repository. Clones the repo into an isolated sandbox and explores "
HEAD:backend/alembic/versions/fe958f19e42b_add_mcp_config_hash_to_sandbox_and_.py:1:"""add mcp_config_hash to sandbox and build_session
HEAD:backend/alembic/versions/fe958f19e42b_add_mcp_config_hash_to_sandbox_and_.py:22:        "sandbox",
HEAD:backend/alembic/versions/fe958f19e42b_add_mcp_config_hash_to_sandbox_and_.py:33:    op.drop_column("sandbox", "mcp_config_hash")
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:171:                OnyxErrorCode.NOT_FOUND, "This workspace has not claimed that domain."
HEAD:backend/ee/onyx/server/billing/api.py:339:            OnyxErrorCode.GATEWAY_TIMEOUT.status_code,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:250:    rendered as an active document. `sandbox` stays off: the logo is embedded
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:258:        sandbox=False,
HEAD:backend/ee/onyx/server/features/hooks/api.py:123:            OnyxErrorCode.GATEWAY_TIMEOUT,
HEAD:backend/ee/onyx/server/features/hooks/api.py:463:    logs = get_hook_execution_logs(db_session=db_session, hook_id=hook_id, limit=limit)
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:288:            raise OnyxError(OnyxErrorCode.BAD_GATEWAY, _TIMEOUT_ERROR[0]) from e
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:146:            # A string container references an existing sandbox under our
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:315:            raise OnyxError(OnyxErrorCode.BAD_GATEWAY, _TIMEOUT_ERROR) from e
HEAD:backend/model_server/encoders.py:138:        # Run CPU-bound embedding in a thread pool
HEAD:backend/onyx/auth/mobile_sso/sso_completion.py:103:    silently fall back to a non-PKCE code) and an allowlisted redirect URI.
HEAD:backend/onyx/auth/permissions.py:78:    Permission.CRAFT_SANDBOX.value: {
HEAD:backend/onyx/auth/permissions.py:95:        Permission.CRAFT_SANDBOX,
HEAD:backend/onyx/auth/users.py:2314:        enable_memory_tool=False,
HEAD:backend/onyx/background/README.md:17:| Heavy                     | `apps/heavy.py`                | `connector_pruning`, `connector_doc_permissions_sync`, `connector_external_group_sync`, `csv_generation`, `sandbox`  |
HEAD:backend/onyx/background/README.md:83:Long running, resource intensive tasks, handles pruning and sandbox operations. Low concurrency - max concurrency of 4 with 1 prefetch.
HEAD:backend/onyx/background/README.md:89:Sandbox (new feature) for running Next.js, Python virtual env, OpenCode AI Agent, and access to knowledge files
HEAD:backend/onyx/background/celery/apps/app_base.py:327:    """Waits for redis to become ready subject to a hardcoded timeout.
HEAD:backend/onyx/background/celery/apps/app_base.py:369:    """Waits for the db to become ready subject to a hardcoded timeout.
HEAD:backend/onyx/background/celery/apps/heavy.py:134:            # Sandbox tasks (file sync, cleanup; build feature)
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:23:from onyx.server.features.build.configs import SANDBOX_IDLE_CLEANUP_INTERVAL_SECONDS
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:236:    # Sandbox sweep: background-snapshot changed sessions, sleep idle sandboxes.
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:238:        "name": "cleanup-idle-sandboxes",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:239:        "task": OnyxCeleryTask.CLEANUP_IDLE_SANDBOXES,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:242:        # the effective interval is SANDBOX_IDLE_CLEANUP_INTERVAL_SECONDS * 8;
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:244:        "schedule": timedelta(seconds=SANDBOX_IDLE_CLEANUP_INTERVAL_SECONDS),
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:248:            "queue": OnyxCeleryQueues.SANDBOX,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:1:"""Celery tasks for sandbox operations (cleanup, etc.)."""
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:12:from onyx.db.models import Sandbox
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:15:from onyx.server.features.build.configs import SANDBOX_IDLE_TIMEOUT_SECONDS
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:16:from onyx.server.features.build.db.sandbox import (
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:18:    get_running_sandboxes,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:21:from onyx.server.features.build.sandbox.factory import get_sandbox_manager
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:28:# so the data-loss bound scales with the pace of sandboxes going to sleep.
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:33:    name=OnyxCeleryTask.CLEANUP_IDLE_SANDBOXES,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:38:def cleanup_idle_sandboxes_task(self: Task, *, tenant_id: str) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:39:    """Sweep RUNNING sandboxes: background-snapshot sessions, sleep idle ones.
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:46:    The reap itself is ``sleep_sandbox`` (sandbox lifecycle), which stays
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:47:    fail-closed: snapshot failure on a reachable pod keeps the sandbox
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:51:    from onyx.server.features.build.session.sandbox_lifecycle import (
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:53:        is_sandbox_idle,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:55:        sleep_sandbox,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:58:    task_logger.info(f"cleanup_idle_sandboxes_task starting for tenant {tenant_id}")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:62:        OnyxRedisLocks.CLEANUP_IDLE_SANDBOXES_BEAT_LOCK,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:68:        task_logger.info("cleanup_idle_sandboxes_task - lock not acquired, skipping")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:72:        sandbox_manager = get_sandbox_manager()
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:75:            running_sandboxes = get_running_sandboxes(db_session)
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:76:            if not running_sandboxes:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:77:                task_logger.debug("No running sandboxes found")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:82:            maybe_mark_tenant_active(tenant_id, caller="sandbox_cleanup")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:86:                seconds=SANDBOX_IDLE_TIMEOUT_SECONDS // SNAPSHOT_INTERVAL_DIVISOR
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:89:            # Partition so idle sandboxes are reaped first (reclaiming pods
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:91:            idle_sandboxes: list[Sandbox] = []
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:92:            non_idle_sandboxes: list[Sandbox] = []
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:93:            for sandbox in running_sandboxes:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:95:                    idle_sandboxes
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:96:                    if is_sandbox_idle(sandbox, now)
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:97:                    else non_idle_sandboxes
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:98:                ).append(sandbox)
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:100:            for sandbox in idle_sandboxes:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:102:                    redis_client, sandbox.user_id
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:105:                    sleep_sandbox(
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:107:                        sandbox_manager=sandbox_manager,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:108:                        sandbox=sandbox,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:114:                        f"Failed to sweep sandbox {sandbox.id}: {e}",
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:119:            for sandbox in non_idle_sandboxes:
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:120:                sandbox_id = sandbox.id
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:127:                        db_session, sandbox.user_id, snapshot_cutoff
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:132:                        redis_client, sandbox.user_id
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:136:                            "Skipping sandbox %s background snapshot while a "
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:138:                            sandbox.id,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:142:                        # List session directories in the sandbox via the
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:146:                            sandbox_manager,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:147:                            sandbox,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:167:                                sandbox_manager=sandbox_manager,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:169:                                sandbox_id=sandbox_id,
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:191:                        and sandbox_manager.supports_opencode_history_persistence
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:194:                            sandbox_manager.create_opencode_history_snapshot(
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:195:                                sandbox_id, tenant_id
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:200:                                f"for sandbox {sandbox_id}: {e}"
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:205:                        f"Failed to sweep sandbox {sandbox_id}: {e}",
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:211:        task_logger.exception("Error in cleanup_idle_sandboxes_task")
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:218:    task_logger.info("cleanup_idle_sandboxes_task completed")
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:187:        "sandbox_queue_length": OnyxCeleryQueues.SANDBOX,
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:987:    n_sandbox = celery_get_queue_length(OnyxCeleryQueues.SANDBOX, r_celery)
HEAD:backend/onyx/background/celery/tasks/monitoring/tasks.py:1024:        f"sandbox={n_sandbox} "
HEAD:backend/onyx/chat/chat_utils.py:30:from onyx.context.search.utils import sandbox_filename_for_document
HEAD:backend/onyx/chat/chat_utils.py:1072:        filename = sandbox_filename_for_document(doc.semantic_identifier, doc.file_id)
HEAD:backend/onyx/chat/llm_loop.py:72:    MemoryToolResponseSnapshot,
HEAD:backend/onyx/chat/llm_loop.py:79:from onyx.tools.tool_implementations.memory.models import MemoryToolResponse
HEAD:backend/onyx/chat/llm_loop.py:1249:                # Persist memory if this is a memory tool response
HEAD:backend/onyx/chat/llm_loop.py:1250:                memory_snapshot: MemoryToolResponseSnapshot | None = None
HEAD:backend/onyx/chat/llm_loop.py:1252:                if isinstance(tool_response.rich_response, MemoryToolResponse):
HEAD:backend/onyx/chat/llm_loop.py:1268:                                    new_text=tool_response.rich_response.memory_text,
HEAD:backend/onyx/chat/llm_loop.py:1273:                                    memory_text=tool_response.rich_response.memory_text,
HEAD:backend/onyx/chat/llm_loop.py:1280:                        memory_snapshot = MemoryToolResponseSnapshot(
HEAD:backend/onyx/chat/llm_loop.py:1281:                            memory_text=tool_response.rich_response.memory_text,
HEAD:backend/onyx/chat/llm_loop.py:1290:                    tool_response.llm_facing_response = incognito_memory_refusal
HEAD:backend/onyx/chat/process_message.py:861:    # memory tool persistence.
HEAD:backend/onyx/chat/prompt_utils.py:45:from onyx.tools.tool_implementations.memory.memory_tool import MemoryTool
HEAD:backend/onyx/chat/prompt_utils.py:304:        has_memory = any(isinstance(tool, MemoryTool) for tool in tools)
HEAD:backend/onyx/chat/prompt_utils.py:337:            tool_guidance_sections.append(MEMORY_GUIDANCE)
HEAD:backend/onyx/coding_agent/mock_tools.py:21:            "repository. The agent clones the repo into an isolated sandbox and "
HEAD:backend/onyx/coding_agent/mock_tools.py:53:            "Run a bash command in the sandboxed session containing the "
HEAD:backend/onyx/coding_agent/mock_tools.py:54:            "checked-out repository. The session has no network access. "
HEAD:backend/onyx/configs/app_configs.py:1171:# can be long-running (LLM + tool calls in a sandbox).
HEAD:backend/onyx/configs/app_configs.py:1660:CODE_INTERPRETER_DEFAULT_TIMEOUT_MS = int(
HEAD:backend/onyx/configs/app_configs.py:1661:    os.environ.get("CODE_INTERPRETER_DEFAULT_TIMEOUT_MS") or 60_000
HEAD:backend/onyx/configs/app_configs.py:1673:CODE_INTERPRETER_MAX_STAGED_FILES = int(
HEAD:backend/onyx/configs/app_configs.py:1674:    os.environ.get("CODE_INTERPRETER_MAX_STAGED_FILES") or 25
HEAD:backend/onyx/configs/app_configs.py:1682:# store and uploading cache misses to the sandbox — so neither blocks the
HEAD:backend/onyx/configs/app_configs.py:1689:# Per-call MCP read timeout; configurable since some tools (e.g. data-agent
HEAD:backend/onyx/configs/app_configs.py:1691:MCP_TOOL_CALL_TIMEOUT_SECONDS = int(
HEAD:backend/onyx/configs/app_configs.py:1692:    os.environ.get("MCP_TOOL_CALL_TIMEOUT_SECONDS") or 300
HEAD:backend/onyx/configs/app_configs.py:1798:# timeout above which raises an exception in our code when exceeded. This
HEAD:backend/onyx/configs/constants.py:312:    # Raw files for Craft sandbox access (xlsx, pptx, docx, etc.)
HEAD:backend/onyx/configs/constants.py:427:    SANDBOX_SNAPSHOT = "sandbox_snapshot"
HEAD:backend/onyx/configs/constants.py:498:    # Sandbox processing queue
HEAD:backend/onyx/configs/constants.py:499:    SANDBOX = "sandbox"
HEAD:backend/onyx/configs/constants.py:570:    # Sandbox cleanup
HEAD:backend/onyx/configs/constants.py:571:    CLEANUP_IDLE_SANDBOXES_BEAT_LOCK = "da_lock:cleanup_idle_sandboxes_beat"
HEAD:backend/onyx/configs/constants.py:722:    # Sandbox cleanup
HEAD:backend/onyx/configs/constants.py:723:    CLEANUP_IDLE_SANDBOXES = "cleanup_idle_sandboxes"
HEAD:backend/onyx/connectors/document360/connector.py:82:                if project["version_code_name"] == self.workspace
HEAD:backend/onyx/connectors/file/connector.py:190:    # code-interpreter sandbox" signal read by
HEAD:backend/onyx/connectors/google_drive/connector.py:2277:                f"Unexpected Google Workspace directory API error (status={status_code}): {e}"
HEAD:backend/onyx/connectors/jira/connector.py:423:    if len(ticket_content.encode("utf-8")) > JIRA_CONNECTOR_MAX_TICKET_SIZE:
HEAD:backend/onyx/connectors/mediawiki/family.py:103:@functools.lru_cache(maxsize=None)
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:80:For a sandbox, use its My Domain host, for example:
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:83:https://company--dev.sandbox.my.salesforce.com
HEAD:backend/onyx/connectors/salesforce/OAUTH.md:116:- Sandbox selection
HEAD:backend/onyx/connectors/salesforce/auth.py:204:            domain="test" if credentials.is_sandbox else None,
HEAD:backend/onyx/connectors/salesforce/models.py:93:    is_sandbox: bool = False
HEAD:backend/onyx/context/search/utils.py:54:_SANDBOX_FILENAME_MAX_LENGTH = 200
HEAD:backend/onyx/context/search/utils.py:179:def sandbox_filename_for_document(title: str, file_id: str) -> str:
HEAD:backend/onyx/context/search/utils.py:181:    unique sandbox filename. Extensions on the title are preserved verbatim."""
HEAD:backend/onyx/context/search/utils.py:187:    max_base_len = max(1, _SANDBOX_FILENAME_MAX_LENGTH - len(suffix))
HEAD:backend/onyx/db/enums.py:368:    INITIALIZING: reserved identity committed; workspace/OpenCode setup is
HEAD:backend/onyx/db/enums.py:370:    ACTIVE:       workspace, config, and OpenCode session are usable.
HEAD:backend/onyx/db/enums.py:371:    IDLE:         sandbox slept; workspace must be restored before use.
HEAD:backend/onyx/db/enums.py:372:    FAILED:       initialization failed after the sandbox came up; the
HEAD:backend/onyx/db/enums.py:457:    SANDBOX_WAKE_FAILED = "sandbox_wake_failed"
HEAD:backend/onyx/db/enums.py:471:class SandboxStatus(str, PyEnum):
HEAD:backend/onyx/db/enums.py:479:        """Check if sandbox is in an active state (running)."""
HEAD:backend/onyx/db/enums.py:480:        return self == SandboxStatus.RUNNING
HEAD:backend/onyx/db/enums.py:483:        """Check if sandbox is in a terminal state."""
HEAD:backend/onyx/db/enums.py:484:        return self in (SandboxStatus.TERMINATED, SandboxStatus.FAILED)
HEAD:backend/onyx/db/enums.py:487:        """Check if sandbox is sleeping (pod terminated but can be restored)."""
HEAD:backend/onyx/db/enums.py:488:        return self == SandboxStatus.SLEEPING
HEAD:backend/onyx/db/enums.py:690:    CRAFT_SANDBOX = "craft_sandbox"
HEAD:backend/onyx/db/external_app.py:777:    Flush only; the caller refreshes the user's sandbox and commits.
HEAD:backend/onyx/db/mcp.py:16:    SandboxStatus,
HEAD:backend/onyx/db/mcp.py:25:    Sandbox,
HEAD:backend/onyx/db/mcp.py:158:    """User IDs with a RUNNING sandbox whose Craft session should be reloaded
HEAD:backend/onyx/db/mcp.py:160:    edited). Scoped to running sandboxes so the hot-reload push has somewhere to
HEAD:backend/onyx/db/mcp.py:165:    stmt = select(Sandbox.user_id).where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/mcp.py:189:        Sandbox.user_id.in_(group_users)
HEAD:backend/onyx/db/mcp.py:190:        | Sandbox.user_id.in_(direct_users)
HEAD:backend/onyx/db/mcp.py:191:        | Sandbox.user_id.in_(owner_users)
HEAD:backend/onyx/db/mcp.py:192:        | Sandbox.user_id.in_(admin_users)
HEAD:backend/onyx/db/models.py:109:    SandboxStatus,
HEAD:backend/onyx/db/models.py:405:    enable_memory_tool: Mapped[bool] = mapped_column(
HEAD:backend/onyx/db/models.py:971:    # FILE_SYSTEM: Write to file system only (for CLI agent sandbox)
HEAD:backend/onyx/db/models.py:4901:    # Immutable Agent Skills name and sandbox directory name.
HEAD:backend/onyx/db/models.py:4916:    # Existing custom rows are classified lazily before sandbox hydration.
HEAD:backend/onyx/db/models.py:6416:        # collide within one user's sandbox.
HEAD:backend/onyx/db/models.py:6427:class Sandbox(Base):
HEAD:backend/onyx/db/models.py:6428:    """Stores sandbox container metadata for users (one sandbox per user)."""
HEAD:backend/onyx/db/models.py:6430:    __tablename__ = "sandbox"
HEAD:backend/onyx/db/models.py:6442:    status: Mapped[SandboxStatus] = mapped_column(
HEAD:backend/onyx/db/models.py:6443:        Enum(SandboxStatus, native_enum=False, name="sandboxstatus"),
HEAD:backend/onyx/db/models.py:6445:        default=SandboxStatus.PROVISIONING,
HEAD:backend/onyx/db/models.py:6472:    # be taken over. Failure diagnostics live in logs (keyed by sandbox ID +
HEAD:backend/onyx/db/models.py:6482:        Index("ix_sandbox_status", "status"),
HEAD:backend/onyx/db/models.py:6483:        Index("ix_sandbox_container_id", "container_id"),
HEAD:backend/onyx/db/models.py:6503:    # path of artifact in sandbox relative to outputs/
HEAD:backend/onyx/db/models.py:6510:    # Content hash from the sandbox manifest. Drives change detection: an
HEAD:backend/onyx/db/models.py:6520:    # Reserved for archived bytes served without the sandbox. NULL until an
HEAD:backend/onyx/db/models.py:6652:    All message data is stored in message_metadata as JSON (the raw sandbox event packet).
HEAD:backend/onyx/db/skill.py:50:    SandboxStatus,
HEAD:backend/onyx/db/skill.py:59:    Sandbox,
HEAD:backend/onyx/db/skill.py:256:    """Return user IDs with a running sandbox that should contain this skill.
HEAD:backend/onyx/db/skill.py:262:        stmt = select(Sandbox.user_id).where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/skill.py:266:        select(Sandbox.user_id)
HEAD:backend/onyx/db/skill.py:269:            User__UserGroup.user_id == Sandbox.user_id,
HEAD:backend/onyx/db/skill.py:276:        .where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/skill.py:281:        select(Sandbox.user_id)
HEAD:backend/onyx/db/skill.py:284:            Skill__User.user_id == Sandbox.user_id,
HEAD:backend/onyx/db/skill.py:287:        .where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/skill.py:293:            select(Sandbox.user_id)
HEAD:backend/onyx/db/skill.py:294:            .where(Sandbox.user_id == skill.author_user_id)
HEAD:backend/onyx/db/skill.py:295:            .where(Sandbox.status == SandboxStatus.RUNNING)
HEAD:backend/onyx/db/skill.py:322:    """Return the user's effective sandbox skills.
HEAD:backend/onyx/db/user_preferences.py:254:    enable_memory_tool: bool,
HEAD:backend/onyx/db/user_preferences.py:266:            enable_memory_tool=enable_memory_tool,
HEAD:backend/onyx/db/users.py:693:    sandbox/session reservation). Hold only for a short transaction."""
HEAD:backend/onyx/error_handling/error_codes.py:113:    GATEWAY_TIMEOUT = ("GATEWAY_TIMEOUT", 504)
HEAD:backend/onyx/error_handling/error_codes.py:161:    504: OnyxErrorCode.GATEWAY_TIMEOUT,
HEAD:backend/onyx/evals/README.md:155:- `WebSearchTool`: Internet/web search
HEAD:backend/onyx/external_apps/matching/request.py:12:    """The normalised form of an outbound sandbox request, transport-agnostic.
HEAD:backend/onyx/external_apps/matching/request.py:14:    The proxy builds one of these from whatever the sandbox emitted (the Python
HEAD:backend/onyx/external_apps/providers/notion.py:26:# Pinned across the provider and the sandbox skill so request-shaping stays
HEAD:backend/onyx/file_store/serving.py:40:    sandbox: bool = True,
HEAD:backend/onyx/file_store/serving.py:50:    if sandbox:
HEAD:backend/onyx/file_store/serving.py:51:        headers["Content-Security-Policy"] = "sandbox"
HEAD:backend/onyx/main.py:337:            "Onyx Craft requires background workers for sandbox lifecycle "
HEAD:backend/onyx/mcp_server/tools/search.py:13:from onyx.configs.app_configs import MCP_SERVER_API_REQUEST_TIMEOUT_SECONDS
HEAD:backend/onyx/mcp_server/tools/search.py:62:        timeout=httpx.Timeout(
HEAD:backend/onyx/mcp_server/tools/search.py:63:            float(MCP_SERVER_API_REQUEST_TIMEOUT_SECONDS), connect=10.0
HEAD:backend/onyx/mcp_server/tools/search.py:422:    Search the public internet for general knowledge, current events, and publicly available information.
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:10:You operate in a read-only, network-isolated sandbox with the repository checked out at the working directory of every `{BASH_TOOL_NAME}` call. Iteratively call `{BASH_TOOL_NAME}` to inspect the codebase, then call `{GENERATE_ANSWER_TOOL_NAME}` once you have gathered enough evidence to answer the user's query comprehensively.
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:64:- Network commands (`curl`, `pip install`, `npm install`, `git pull`) — the sandbox has no network.
HEAD:backend/onyx/prompts/coding_agent/coding_agent.py:81:You operate in a read-only, network-isolated sandbox with the repository checked out at the working directory of every `{BASH_TOOL_NAME}` call. Reason between calls about what you have learned and what to inspect next. When you have enough evidence to answer the query, call `{GENERATE_ANSWER_TOOL_NAME}`.
HEAD:backend/onyx/prompts/tool_prompts.py:38:- Niche Information: when detailed info is not widely known or understood (but is likely found on the internet).{site_colon_disabled}
HEAD:backend/onyx/prompts/tool_prompts.py:56:Use the `run_python` tool to execute Python code in an isolated sandbox. The tool will respond with the output of the execution or time out after 60.0 seconds.
HEAD:backend/onyx/prompts/tool_prompts.py:60:Internet access for this session is disabled. Do not make external web requests or API calls as they will fail.
HEAD:backend/onyx/prompts/tool_prompts.py:63:The sandbox fonts cannot shape Arabic or render CJK glyphs (they come out as disconnected letters or boxes), so for those languages write the rendered text in English and explain the labels in your reply.
HEAD:backend/onyx/prompts/tool_prompts.py:64:IMPORTANT: each call to this tool runs in a fresh, stateless sandbox. Variables, imports, and in-memory state from previous calls will NOT be available, \
HEAD:backend/onyx/prompts/tool_prompts.py:77:MEMORY_GUIDANCE = """
HEAD:backend/onyx/prompts/tool_prompts.py:78:## add_memory
HEAD:backend/onyx/prompts/tool_prompts.py:79:Use the `add_memory` tool for facts shared by the user that should be remembered for future conversations. \
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1:"""Gate addon: enforces approval policy on identified sandbox egress.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:3:Fail-closed: identity, body-size cap, and unidentified-sandbox checks.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:36:from onyx.sandbox_proxy import approval_cache
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:37:from onyx.sandbox_proxy.credential_injection import (
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:42:from onyx.sandbox_proxy.errors import SandboxProxyError, http_403
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:43:from onyx.sandbox_proxy.identity import ResolvedSandbox, SessionContext
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:44:from onyx.sandbox_proxy.logging_utils import (
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:46:    EGRESS_APPROVAL_MATCHED_FIELDS,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:47:    EGRESS_MATCHED_FIELDS,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:48:    EGRESS_SESSION_MATCHED_FIELDS,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:49:    EGRESS_TARGET_FIELDS,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:52:    egress_approval_matched_args,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:53:    egress_matched_args,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:54:    egress_session_matched_args,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:55:    egress_target_args,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:57:    sandbox_log_label,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:60:from onyx.sandbox_proxy.request_evaluator import RequestEvaluator
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:64:    SANDBOX_APPROVAL_WAIT_TIMEOUT_SECONDS,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:78:# --- internal-destination egress lockdown: closes the proxy-relay path ---
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:79:# A sandbox can only egress via the proxy, so the proxy is the single layer that can
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:81:# metadata endpoints) — that destination is invisible at the sandbox's own egress (it sees
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:84:# the public internet. Keying off "not globally routable" — not a hostname allow-list —
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:89:# The single allowed internal destination: the api-server the sandbox calls via the
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:117:    under custom networking), loopback, link-local (incl. cloud metadata / IMDS),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:133:    """True if the sandbox must not be relayed to ``host:port``.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:156:            "egress_destination_resolution_failed host=%s error=%s", host, exc
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:167:    def resolve_sandbox(self, src_ip: str) -> ResolvedSandbox | None: ...
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:258:            maxsize=_GRANT_CACHE_MAX_ENTRIES, ttl=_GRANT_CACHE_TTL_S
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:283:                "egress_denied_internal_destination phase=connect host=%s port=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:287:            flow.response = http_403(SandboxProxyError.DESTINATION_BLOCKED)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:309:        """Drops the connection's cached session tag to bound memory."""
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:328:        passthrough tunnel — which skips credential injection (the sandbox PAT is
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:329:        never swapped in, so the sandbox's placeholder leaks and the call 401s).
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:343:                "egress_denied_internal_destination phase=server_connect host=%s port=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:351:        Streams the response body to the sandbox instead of buffering it whole.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:375:                "egress_denied_internal_destination phase=request host=%s port=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:379:            flow.response = http_403(SandboxProxyError.DESTINATION_BLOCKED)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:404:                    "approval_dispatch_error tenant=%s sandbox=%s "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:407:                    sandbox_log_label(ctx),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:413:                flow.response = http_403(SandboxProxyError.INTERNAL_ERROR)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:438:                    SandboxProxyError.USER_REJECTED.value
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:440:                    else SandboxProxyError.NOT_AUTHORIZED.value
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:443:                    "egress_block " + EGRESS_APPROVAL_MATCHED_FIELDS + " reason=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:444:                    *egress_approval_matched_args(
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:451:                "approval_unhandled_error tenant=%s sandbox=%s session=%s "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:454:                sandbox_log_label(ctx),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:462:            flow.response = http_403(SandboxProxyError.INTERNAL_ERROR)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:480:            sandbox=ctx.without_session(),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:484:            fields = EGRESS_SESSION_MATCHED_FIELDS
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:485:            args = egress_session_matched_args(
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:489:            fields = EGRESS_APPROVAL_MATCHED_FIELDS
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:490:            args = egress_approval_matched_args(
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:496:                "egress_block " + fields + " reason=%s credential_outcome=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:498:                SandboxProxyError.CREDENTIAL_ERROR.value,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:503:                "egress_allow " + fields + " credential_outcome=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:519:          sandbox, oversize body, unattributable gated request).
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:538:            flow.response = http_403(SandboxProxyError.UNIDENTIFIED_SANDBOX)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:542:            sandbox = self._identity.resolve_sandbox(src_ip)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:544:            # A DB blip can't be allowed to grant ungated egress.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:550:            flow.response = http_403(SandboxProxyError.UNIDENTIFIED_SANDBOX)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:552:        if sandbox is None:
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:555:            # (2) Deployment-shape SNAT masks the sandbox's real bridge IP (e.g.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:556:            # proxy outside the sandbox bridge).
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:558:                "identity_unknown_sandbox src_ip=%s host=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:562:            flow.response = http_403(SandboxProxyError.UNIDENTIFIED_SANDBOX)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:570:                "egress_block "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:571:                + EGRESS_TARGET_FIELDS
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:573:                *egress_target_args(flow, sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:574:                SandboxProxyError.BODY_TOO_LARGE.value,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:578:            flow.response = http_403(SandboxProxyError.BODY_TOO_LARGE)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:583:                flow.request, sandbox.tenant_id, sandbox.user_id
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:590:                "matcher_error tenant=%s sandbox=%s host=%s error=%r",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:591:                sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:592:                sandbox_log_label(sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:606:                sandbox=sandbox,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:611:                    "egress_block "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:612:                    + EGRESS_TARGET_FIELDS
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:614:                    *egress_target_args(flow, sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:615:                    SandboxProxyError.CREDENTIAL_ERROR.value,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:620:                    "egress_allow "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:621:                    + EGRESS_TARGET_FIELDS
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:623:                    *egress_target_args(flow, sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:630:            flow.response = http_403(SandboxProxyError.POLICY_DENIED)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:632:                "egress_block " + EGRESS_MATCHED_FIELDS + " reason=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:633:                *egress_matched_args(
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:634:                    flow, sandbox, matched_actions, EndpointPolicy.DENY
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:636:                SandboxProxyError.POLICY_DENIED.value,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:647:                sandbox=sandbox,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:652:                    "egress_block "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:653:                    + EGRESS_MATCHED_FIELDS
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:655:                    *egress_matched_args(
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:656:                        flow, sandbox, matched_actions, EndpointPolicy.ALWAYS
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:658:                    SandboxProxyError.CREDENTIAL_ERROR.value,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:663:                    "egress_allow " + EGRESS_MATCHED_FIELDS + " credential_outcome=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:664:                    *egress_matched_args(
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:665:                        flow, sandbox, matched_actions, EndpointPolicy.ALWAYS
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:674:            session_id = self._resolve_gated_session(flow, sandbox)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:677:                "session_lookup_error tenant=%s sandbox=%s host=%s app_name=%r "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:679:                sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:680:                sandbox_log_label(sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:685:            flow.response = http_403(SandboxProxyError.NO_ACTIVE_SESSION)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:689:                "egress_block " + EGRESS_MATCHED_FIELDS + " reason=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:690:                *egress_matched_args(
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:691:                    flow, sandbox, matched_actions, EndpointPolicy.ASK
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:693:                SandboxProxyError.NO_ACTIVE_SESSION.value,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:695:            flow.response = http_403(SandboxProxyError.NO_ACTIVE_SESSION)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:698:        ctx = sandbox.with_session(session_id)
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:700:            "approval_match tenant=%s sandbox=%s session=%s host=%s "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:703:            sandbox_log_label(ctx),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:817:                "approval_grant_check_error tenant=%s sandbox=%s "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:821:                sandbox_log_label(ctx),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:928:            "approval_requested tenant=%s sandbox=%s session=%s approval=%s "
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:932:            sandbox_log_label(ctx),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:963:        """Parks on the wake channel; claims EXPIRED on timeout / cancel.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:970:                approval_id, SANDBOX_APPROVAL_WAIT_TIMEOUT_SECONDS, cache
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:986:            source = "timeout" if resolved == ApprovalDecision.EXPIRED else "db_winner"
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1000:            # Sandbox socket closed mid-wait. Terminalize the audit row, then
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1042:            SandboxProxyError.USER_REJECTED
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1044:            else SandboxProxyError.NOT_AUTHORIZED
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1052:        sandbox: ResolvedSandbox,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1059:                sandbox=sandbox,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1065:                SandboxProxyError.CREDENTIAL_ERROR, detail=result.block_detail
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1231:        self, flow: http.HTTPFlow, sandbox: ResolvedSandbox
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1242:                "session_missing tenant=%s sandbox=%s host=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1243:                sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1244:                sandbox_log_label(sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1252:                "session_malformed tenant=%s sandbox=%s host=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1253:                sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1254:                sandbox_log_label(sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1259:            tagged_id, sandbox.user_id, sandbox.tenant_id
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1264:                "session_unverified tenant=%s sandbox=%s session=%s host=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1265:                sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1266:                sandbox_log_label(sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1272:            "session_verified tenant=%s sandbox=%s session=%s host=%s",
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1273:            sandbox.tenant_id,
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1274:            sandbox_log_label(sandbox),
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1294:        # the sandbox is one trust domain per user, so a compromised process can
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1296:        # nothing (the value is stored in-sandbox in plaintext). Cross-user is
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1297:        # still blocked by the src-IP-pinned sandbox identity in resolve_sandbox.
HEAD:backend/onyx/sandbox_proxy/approval_cache.py:10:  recorded; the parked proxy BLPOPs to wake before the wait timeout.
HEAD:backend/onyx/sandbox_proxy/approval_cache.py:153:    approval_id: UUID, timeout_s: int, cache: CacheBackend
HEAD:backend/onyx/sandbox_proxy/approval_cache.py:155:    """Block for a decision. `None` on timeout/unparseable payload (caller re-reads the row)."""
HEAD:backend/onyx/sandbox_proxy/approval_cache.py:156:    if timeout_s <= 0:
HEAD:backend/onyx/sandbox_proxy/approval_cache.py:159:    deadline = time.monotonic() + timeout_s
HEAD:backend/onyx/sandbox_proxy/approval_cache.py:183:    """Wake the parked proxy. A miss just means it waits out the wait timeout."""
HEAD:backend/onyx/sandbox_proxy/approval_cache.py:189:    session_id: UUID, timeout_s: int, cache: CacheBackend
HEAD:backend/onyx/sandbox_proxy/approval_cache.py:192:    result = cache.blpop([announce_key(session_id)], timeout_s)
HEAD:backend/onyx/sandbox_proxy/backend.py:5:correctly under either ``SANDBOX_BACKEND`` value.
HEAD:backend/onyx/sandbox_proxy/backend.py:14:from onyx.sandbox_proxy.ca import CAStore
HEAD:backend/onyx/sandbox_proxy/backend.py:15:from onyx.sandbox_proxy.identity import SandboxIPLookup
HEAD:backend/onyx/sandbox_proxy/backend.py:16:from onyx.server.features.build.configs import SANDBOX_BACKEND, SandboxBackend
HEAD:backend/onyx/sandbox_proxy/backend.py:20:    if SANDBOX_BACKEND is SandboxBackend.KUBERNETES:
HEAD:backend/onyx/sandbox_proxy/backend.py:21:        from onyx.sandbox_proxy.ca_k8s import K8sSecretCAStore
HEAD:backend/onyx/sandbox_proxy/backend.py:24:    if SANDBOX_BACKEND is SandboxBackend.DOCKER:
HEAD:backend/onyx/sandbox_proxy/backend.py:25:        from onyx.sandbox_proxy.ca_docker import FileCAStore
HEAD:backend/onyx/sandbox_proxy/backend.py:28:    raise RuntimeError(f"Unsupported SANDBOX_BACKEND={SANDBOX_BACKEND!r}.")
HEAD:backend/onyx/sandbox_proxy/backend.py:31:def build_ip_lookup() -> SandboxIPLookup:
HEAD:backend/onyx/sandbox_proxy/backend.py:32:    if SANDBOX_BACKEND is SandboxBackend.KUBERNETES:
HEAD:backend/onyx/sandbox_proxy/backend.py:33:        from onyx.sandbox_proxy.identity_k8s import K8sInformerLookup
HEAD:backend/onyx/sandbox_proxy/backend.py:36:    if SANDBOX_BACKEND is SandboxBackend.DOCKER:
HEAD:backend/onyx/sandbox_proxy/backend.py:37:        from onyx.sandbox_proxy.identity_docker import DockerEventsLookup
HEAD:backend/onyx/sandbox_proxy/backend.py:40:    raise RuntimeError(f"Unsupported SANDBOX_BACKEND={SANDBOX_BACKEND!r}.")
HEAD:backend/onyx/sandbox_proxy/ca.py:1:"""CA bootstrap for the sandbox egress proxy."""
HEAD:backend/onyx/sandbox_proxy/ca.py:18:_CA_COMMON_NAME = "Onyx Sandbox Proxy CA"
HEAD:backend/onyx/sandbox_proxy/ca.py:22:_DEFAULT_CA_PEM_PATH = "/var/run/sandbox-proxy/mitmproxy-confdir/mitmproxy-ca.pem"
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:4:read-write so it can persist on cold start; every sandbox container mounts it
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:6:That mount also makes ``ca.key`` present in Docker sandbox filesystems; the
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:7:key is protected by ``0600`` root ownership, and the sandbox agent runs as
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:11:``sandbox-proxy`` replica, so the cold-start race is not a routine concern in
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:16:   sandbox-proxy=2``. Without ``O_EXCL`` both replicas would race-overwrite each
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:17:   other's key, leaving sandbox trust stores pointing at a cert whose private
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:35:from onyx.sandbox_proxy.ca import CAStore, CAStoreConflictError
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:36:from onyx.server.features.build.configs import SANDBOX_PROXY_CA_VOLUME_PATH
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:54:            ca.crt   # public cert, world-readable; mounted into sandboxes
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:55:            ca.key   # private key, mode 0600; root-only in Docker sandboxes
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:63:    def __init__(self, root: str | Path = SANDBOX_PROXY_CA_VOLUME_PATH) -> None:
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:76:            # regenerating and orphaning the cert that sandboxes may have
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:113:        # a truncated CA would propagate silently into every sandbox's trust
HEAD:backend/onyx/sandbox_proxy/ca_docker.py:118:        # doesn't leave sandboxes unable to read the cert.
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:4:ConfigMap in the sandbox namespace mirrors only the public cert so
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:5:sandbox init containers can mount it (K8s does not allow
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:16:from onyx.sandbox_proxy.ca import CAStore, CAStoreConflictError
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:18:    SANDBOX_NAMESPACE,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:19:    SANDBOX_PROXY_CA_CONFIGMAP,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:20:    SANDBOX_PROXY_CA_SECRET,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:21:    SANDBOX_PROXY_NAMESPACE,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:23:from onyx.server.features.build.sandbox.kubernetes.k8s_client import build_core_v1_api
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:24:from onyx.server.features.build.sandbox.labels import (
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:38:_COMPONENT_VALUE_PROXY = "sandbox-proxy"
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:40:_SECRET_RESOURCE_LABEL = "sandbox-proxy-ca"
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:41:_CONFIGMAP_RESOURCE_LABEL = "sandbox-proxy-ca-bundle"
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:58:        proxy_namespace: str = SANDBOX_PROXY_NAMESPACE,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:59:        sandbox_namespace: str = SANDBOX_NAMESPACE,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:60:        secret_name: str = SANDBOX_PROXY_CA_SECRET,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:61:        configmap_name: str = SANDBOX_PROXY_CA_CONFIGMAP,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:67:        self._sandbox_ns = sandbox_namespace
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:84:            # Fail loud: regenerating would invalidate sandboxes already
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:146:                namespace=self._sandbox_ns,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:158:                namespace=self._sandbox_ns,
HEAD:backend/onyx/sandbox_proxy/ca_k8s.py:173:                    namespace=self._sandbox_ns,
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:1:"""Host-claim dispatcher for sandbox-proxy credential injection.
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:6:real secret never has to live in the sandbox pod. Resolution outcomes are
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:21:from onyx.sandbox_proxy.identity import ResolvedSandbox
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:30:    `sandbox_detail`, when set, is agent-facing 403-body prose — never secrets
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:34:    def __init__(self, message: str, *, sandbox_detail: str | None = None) -> None:
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:36:        self.sandbox_detail = sandbox_detail
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:44:    `external_app_id`), or `None` on off-catalog forwards. `sandbox.tenant_id` is
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:48:    sandbox: ResolvedSandbox
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:59:        `ctx.sandbox.tenant_id` for per-context routing). Avoid opening a DB
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:111:                outcome=InjectionOutcome.BLOCKED, block_detail=e.sandbox_detail
HEAD:backend/onyx/sandbox_proxy/errors.py:1:"""Sandbox-facing 403 error codes and response builder.
HEAD:backend/onyx/sandbox_proxy/errors.py:3:Every 403 the proxy returns to the sandbox carries a stable `error` code plus a
HEAD:backend/onyx/sandbox_proxy/errors.py:4:human-readable `message`. The agent running in the sandbox reads the `message`
HEAD:backend/onyx/sandbox_proxy/errors.py:19:class SandboxProxyError(str, Enum):
HEAD:backend/onyx/sandbox_proxy/errors.py:20:    """Stable `error` codes returned to the sandbox in a 403 body."""
HEAD:backend/onyx/sandbox_proxy/errors.py:22:    UNIDENTIFIED_SANDBOX = "unidentified_sandbox"
HEAD:backend/onyx/sandbox_proxy/errors.py:36:        Addressed to the agent in the sandbox that receives the 403.
HEAD:backend/onyx/sandbox_proxy/errors.py:38:        return _SANDBOX_ERROR_MESSAGES[self]
HEAD:backend/onyx/sandbox_proxy/errors.py:41:_SANDBOX_ERROR_MESSAGES: dict[SandboxProxyError, str] = {
HEAD:backend/onyx/sandbox_proxy/errors.py:42:    SandboxProxyError.UNIDENTIFIED_SANDBOX: (
HEAD:backend/onyx/sandbox_proxy/errors.py:43:        "The proxy could not identify which workspace this request came from, so "
HEAD:backend/onyx/sandbox_proxy/errors.py:44:        "it was blocked before reaching the network. This is an internal setup "
HEAD:backend/onyx/sandbox_proxy/errors.py:49:    SandboxProxyError.NO_ACTIVE_SESSION: (
HEAD:backend/onyx/sandbox_proxy/errors.py:56:    SandboxProxyError.BODY_TOO_LARGE: (
HEAD:backend/onyx/sandbox_proxy/errors.py:63:    SandboxProxyError.USER_REJECTED: (
HEAD:backend/onyx/sandbox_proxy/errors.py:69:    SandboxProxyError.NOT_AUTHORIZED: (
HEAD:backend/onyx/sandbox_proxy/errors.py:76:    SandboxProxyError.INTERNAL_ERROR: (
HEAD:backend/onyx/sandbox_proxy/errors.py:82:    SandboxProxyError.POLICY_DENIED: (
HEAD:backend/onyx/sandbox_proxy/errors.py:83:        "This request targets an integration that the workspace administrator "
HEAD:backend/onyx/sandbox_proxy/errors.py:89:    SandboxProxyError.CREDENTIAL_ERROR: (
HEAD:backend/onyx/sandbox_proxy/errors.py:96:    SandboxProxyError.DESTINATION_BLOCKED: (
HEAD:backend/onyx/sandbox_proxy/errors.py:97:        "This request targets an internal network address that sandboxes are not "
HEAD:backend/onyx/sandbox_proxy/errors.py:99:        "the public internet and the Onyx API server are reachable from here. "
HEAD:backend/onyx/sandbox_proxy/errors.py:106:def http_403(code: SandboxProxyError, detail: str | None = None) -> http.Response:
HEAD:backend/onyx/sandbox_proxy/errors.py:107:    """Build a sandbox-visible 403.
HEAD:backend/onyx/sandbox_proxy/identity.py:1:"""Source-IP -> sandbox identity + in-band session resolution.
HEAD:backend/onyx/sandbox_proxy/identity.py:7:- `resolve_sandbox()` — pod IP -> sandbox + user + tenant; enforces "only known
HEAD:backend/onyx/sandbox_proxy/identity.py:8:  sandbox pods may egress".
HEAD:backend/onyx/sandbox_proxy/identity.py:23:from onyx.db.models import BuildSession, Sandbox
HEAD:backend/onyx/sandbox_proxy/identity.py:30:class SandboxIdentity:
HEAD:backend/onyx/sandbox_proxy/identity.py:31:    sandbox_id: UUID
HEAD:backend/onyx/sandbox_proxy/identity.py:33:    sandbox_name: str
HEAD:backend/onyx/sandbox_proxy/identity.py:34:    sandbox_ip: str
HEAD:backend/onyx/sandbox_proxy/identity.py:38:class ResolvedSandbox:
HEAD:backend/onyx/sandbox_proxy/identity.py:39:    """Sandbox identity + owning user. Authorizes egress."""
HEAD:backend/onyx/sandbox_proxy/identity.py:41:    sandbox_id: UUID
HEAD:backend/onyx/sandbox_proxy/identity.py:44:    sandbox_name: str
HEAD:backend/onyx/sandbox_proxy/identity.py:45:    sandbox_ip: str
HEAD:backend/onyx/sandbox_proxy/identity.py:51:            sandbox_id=self.sandbox_id,
HEAD:backend/onyx/sandbox_proxy/identity.py:53:            sandbox_name=self.sandbox_name,
HEAD:backend/onyx/sandbox_proxy/identity.py:54:            sandbox_ip=self.sandbox_ip,
HEAD:backend/onyx/sandbox_proxy/identity.py:60:    """Sandbox identity + the verified session to route the card to."""
HEAD:backend/onyx/sandbox_proxy/identity.py:64:    sandbox_id: UUID
HEAD:backend/onyx/sandbox_proxy/identity.py:66:    sandbox_name: str
HEAD:backend/onyx/sandbox_proxy/identity.py:67:    sandbox_ip: str
HEAD:backend/onyx/sandbox_proxy/identity.py:69:    def without_session(self) -> ResolvedSandbox:
HEAD:backend/onyx/sandbox_proxy/identity.py:71:        Inverse of `ResolvedSandbox.with_session(...)` — drops the session id.
HEAD:backend/onyx/sandbox_proxy/identity.py:73:        return ResolvedSandbox(
HEAD:backend/onyx/sandbox_proxy/identity.py:74:            sandbox_id=self.sandbox_id,
HEAD:backend/onyx/sandbox_proxy/identity.py:77:            sandbox_name=self.sandbox_name,
HEAD:backend/onyx/sandbox_proxy/identity.py:78:            sandbox_ip=self.sandbox_ip,
HEAD:backend/onyx/sandbox_proxy/identity.py:82:class SandboxIPLookup(Protocol):
HEAD:backend/onyx/sandbox_proxy/identity.py:83:    """Backend-specific IP -> SandboxIdentity resolver.
HEAD:backend/onyx/sandbox_proxy/identity.py:91:    def lookup(self, src_ip: str) -> SandboxIdentity | None: ...
HEAD:backend/onyx/sandbox_proxy/identity.py:93:    def wait_for_initial_sync(self, timeout_seconds: float) -> bool: ...
HEAD:backend/onyx/sandbox_proxy/identity.py:101:    def __init__(self, ip_lookup: SandboxIPLookup) -> None:
HEAD:backend/onyx/sandbox_proxy/identity.py:104:    def resolve_sandbox(self, src_ip: str) -> ResolvedSandbox | None:
HEAD:backend/onyx/sandbox_proxy/identity.py:106:        Pod IP -> owning user + tenant; `None` if IP unknown or sandbox has no
HEAD:backend/onyx/sandbox_proxy/identity.py:118:                select(Sandbox.user_id).where(Sandbox.id == identity.sandbox_id)
HEAD:backend/onyx/sandbox_proxy/identity.py:123:        return ResolvedSandbox(
HEAD:backend/onyx/sandbox_proxy/identity.py:124:            sandbox_id=identity.sandbox_id,
HEAD:backend/onyx/sandbox_proxy/identity.py:127:            sandbox_name=identity.sandbox_name,
HEAD:backend/onyx/sandbox_proxy/identity.py:128:            sandbox_ip=identity.sandbox_ip,
HEAD:backend/onyx/sandbox_proxy/identity.py:134:        """Validates a sandbox-supplied `BuildSession` id against its owner.
HEAD:backend/onyx/sandbox_proxy/identity.py:142:        originated the egress regardless of its current status.
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:1:"""Docker-compose implementation of ``SandboxIPLookup``.
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:3:Background thread streams ``DockerClient.events()`` filtered to sandbox
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:4:containers and maintains a ``{container_ip: SandboxIdentity}`` cache. On any
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:24:from onyx.sandbox_proxy.identity import SandboxIdentity, SandboxIPLookup
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:26:    SANDBOX_DOCKER_NETWORK,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:27:    SANDBOX_DOCKER_SOCKET,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:29:from onyx.server.features.build.sandbox.labels import (
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:31:    LABEL_DOCKER_COMPONENT_SANDBOX,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:32:    LABEL_SANDBOX_ID,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:52:    network: str,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:53:) -> SandboxIdentity | None:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:54:    """Builds a ``SandboxIdentity`` from a container's labels + bridge IP.
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:56:    Returns ``None`` for containers that aren't sandbox-labelled, are missing
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:57:    the sandbox/tenant labels, have a non-UUID sandbox-id, or have no IP on the
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:58:    configured sandbox bridge yet (i.e. a sandbox in a creation race that hasn't
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:59:    been attached to the network).
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:65:    if labels.get(LABEL_DOCKER_COMPONENT) != LABEL_DOCKER_COMPONENT_SANDBOX:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:68:    sandbox_id_raw = labels.get(LABEL_SANDBOX_ID)
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:70:    if not sandbox_id_raw or not tenant_id:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:74:        sandbox_id = UUID(sandbox_id_raw)
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:77:            "Skipping sandbox container %s with non-UUID sandbox-id label %r",
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:79:            sandbox_id_raw,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:83:    networks = ((container.attrs or {}).get("NetworkSettings") or {}).get(
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:84:        "Networks"
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:86:    bridge = networks.get(network) or {}
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:91:    return SandboxIdentity(
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:92:        sandbox_id=sandbox_id,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:94:        sandbox_name=container.name or "",
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:95:        sandbox_ip=ip,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:99:class DockerEventsLookup(SandboxIPLookup):
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:105:        network: str = SANDBOX_DOCKER_NETWORK,
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:108:            docker_client = DockerClient(base_url=f"unix://{SANDBOX_DOCKER_SOCKET}")
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:110:        self._network = network
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:112:        self._cache: dict[str, SandboxIdentity] = {}
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:130:            target=self._run, name="sandbox-proxy-docker-events", daemon=True
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:147:    def wait_for_initial_sync(self, timeout_seconds: float) -> bool:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:148:        return self._initial_sync_done.wait(timeout=timeout_seconds)
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:153:    def lookup(self, src_ip: str) -> SandboxIdentity | None:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:164:                # silently drops events: a sandbox starting in that window would
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:201:                "label": f"{LABEL_DOCKER_COMPONENT}={LABEL_DOCKER_COMPONENT_SANDBOX}"
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:204:        new_cache: dict[str, SandboxIdentity] = {}
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:213:            identity = _identity_from_container(c, self._network)
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:216:            existing = new_cache.get(identity.sandbox_ip)
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:217:            if existing is not None and existing.sandbox_id != identity.sandbox_id:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:219:                    f"Duplicate sandbox IP {identity.sandbox_ip} mapped to "
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:220:                    f"{existing.sandbox_id} and {identity.sandbox_id}; "
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:223:            new_cache[identity.sandbox_ip] = identity
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:224:            new_by_id[c.id] = identity.sandbox_ip
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:231:            "Docker events initial sync: %d sandbox containers cached.", len(new_cache)
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:240:                "label": f"{LABEL_DOCKER_COMPONENT}={LABEL_DOCKER_COMPONENT_SANDBOX}",
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:269:        # container is attached to its network and has an IP;
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:276:            identity = _identity_from_container(container, self._network)
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:283:                if stale_ip is not None and stale_ip != identity.sandbox_ip:
HEAD:backend/onyx/sandbox_proxy/identity_docker.py:293:                # un-identifying the new container. Don't gate on sandbox_id --
```
Runtime effectiveness of sandboxing, resource limits, filesystem isolation
and egress controls remains unverified.
## Failure and Timeout Semantics
Evidence lines: 252
```text
HEAD:backend/ee/onyx/auth/users.py:39:            status_code=status.HTTP_403_FORBIDDEN,
HEAD:backend/ee/onyx/db/user_group.py:302:            nothing (fail-closed); ``None`` returns all groups (admin/global).
HEAD:backend/ee/onyx/external_permissions/box/access.py:30:# Keeping an allowlist ensures new SDK roles fail closed until reviewed.
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:25:class BoxGroupTooLargeError(Exception):
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:50:            raise BoxGroupTooLargeError(group_id)
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:71:            except BoxGroupTooLargeError:
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:174:                status_code=status.HTTP_401_UNAUTHORIZED,
HEAD:backend/ee/onyx/server/middleware/tier_gate.py:92:            # Fail closed: on any tier resolution error, treat as COMMUNITY (most restrictive)
HEAD:backend/ee/onyx/server/settings/api.py:61:        # Fail closed - if Redis is down, other things will break anyway
HEAD:backend/ee/onyx/server/settings/api.py:137:        # Fail closed - disable EE features if we can't verify license
HEAD:backend/ee/onyx/server/tenants/billing.py:203:    Stripe errors propagate (fail closed). No-op when current quantity
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:15:FORBIDDEN_COMMON_EMAIL_SUBSTRINGS = [
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:32:    if any(substring in domain for substring in FORBIDDEN_COMMON_EMAIL_SUBSTRINGS):
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:16:    FORBIDDEN_COMMON_EMAIL_SUBSTRINGS,
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:53:    # Case-folded: the forbidden list is lower case, so GMAIL.com would pass it.
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:56:    if not any(substring in domain for substring in FORBIDDEN_COMMON_EMAIL_SUBSTRINGS):
HEAD:backend/onyx/auth/mobile_sso/code_store.py:71:        # fail-closed contract.
HEAD:backend/onyx/auth/mobile_sso/code_store.py:74:        # A malformed verifier (e.g. non-ascii) must fail closed as the same
HEAD:backend/onyx/auth/permission_projection.py:7:its own guard as the security boundary. Fail-closed — a key absent from the map reads
HEAD:backend/onyx/auth/scoped_permissions.py:79:    requested) is one they manage, landing in >=1 group. Fail-closed: NONE,
HEAD:backend/onyx/auth/scoped_permissions.py:151:    for a group they manage. Fail-closed: empty managed scope is ``False``.
HEAD:backend/onyx/auth/sso_tenant_token.py:43:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/auth/sso_tenant_token.py:50:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/auth/users.py:304:        # Fail closed: if the setting can't be read, treat the workspace as
HEAD:backend/onyx/auth/users.py:341:        OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/auth/users.py:1061:                        OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/auth/users.py:1951:            status.HTTP_401_UNAUTHORIZED: {
HEAD:backend/onyx/auth/users.py:2201:    """Whether a scoped PAT may proceed on this route (fail-closed)."""
HEAD:backend/onyx/auth/users.py:2263:    # Fail-closed: a scoped PAT may only reach routes guarded by a
HEAD:backend/onyx/background/celery/tasks/build/tasks.py:47:    fail-closed: snapshot failure on a reachable pod keeps the sandbox
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:1231:    """Retry deletion of tool-generated blobs whose teardown pass failed.
HEAD:backend/onyx/cache/interface.py:13:failures. Callers that want to fail-open (or fail-closed) on cache errors should
HEAD:backend/onyx/chat/chat_utils.py:214:                OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/chat/compression.py:407:    walks ``msg.tool_calls`` and would raise ``DetachedInstanceError`` if
HEAD:backend/onyx/chat/incognito.py:136:    """Retry deletion of tool-generated blobs a teardown pass failed to remove.
HEAD:backend/onyx/chat/llm_loop.py:181:    # the likely account-level cause instead of a generic tool-calling error.
HEAD:backend/onyx/chat/llm_loop.py:628:    reject such history with an "unexpected tool call id" error.
HEAD:backend/onyx/chat/process_message.py:1143:        details["tool_choice"] = error.tool_choice.value
HEAD:backend/onyx/chat/process_message.py:1716:                    unauthorized = sorted(
HEAD:backend/onyx/chat/process_message.py:1721:                    if unauthorized:
HEAD:backend/onyx/chat/process_message.py:1725:                            % unauthorized,
HEAD:backend/onyx/configs/app_configs.py:86:# name that doesn't exist matches nothing (fail-closed) and is logged. Read at import — restart to change.
HEAD:backend/onyx/configs/app_configs.py:1689:# Per-call MCP read timeout; configurable since some tools (e.g. data-agent
HEAD:backend/onyx/configs/app_configs.py:1691:MCP_TOOL_CALL_TIMEOUT_SECONDS = int(
HEAD:backend/onyx/configs/app_configs.py:1692:    os.environ.get("MCP_TOOL_CALL_TIMEOUT_SECONDS") or 300
HEAD:backend/onyx/configs/app_configs.py:1969:# to bypass login captcha. Empty value = bypass disabled (fail-closed). Sent by
HEAD:backend/onyx/connectors/blob/connector.py:315:        # Accessing through the browser will always return an unauthorized error
HEAD:backend/onyx/connectors/box/connector.py:165:_BOX_CREDENTIAL_OAUTH_ERRORS = frozenset({"invalid_client", "unauthorized_client"})
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:1083:                "Unauthorized (401) when calling JSON-RPC API for space permissions. "
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:1215:                "Unauthorized (401) when calling REST space-permissions API. "
HEAD:backend/onyx/connectors/confluence/utils.py:399:        FORBIDDEN_MAX_RETRY_ATTEMPTS = 7
HEAD:backend/onyx/connectors/confluence/utils.py:400:        FORBIDDEN_RETRY_DELAY = 10
HEAD:backend/onyx/connectors/confluence/utils.py:401:        if attempt < FORBIDDEN_MAX_RETRY_ATTEMPTS:
HEAD:backend/onyx/connectors/confluence/utils.py:404:                FORBIDDEN_RETRY_DELAY,
HEAD:backend/onyx/connectors/confluence/utils.py:406:            return FORBIDDEN_RETRY_DELAY
HEAD:backend/onyx/connectors/sharepoint/connector.py:275:    status), False if SP rejected it as unauthorized. Transport-level errors are
HEAD:backend/onyx/connectors/sharepoint/connector.py:779:        unauthorized_sites: list[str] = [
HEAD:backend/onyx/connectors/sharepoint/connector.py:785:        if not unauthorized_sites:
HEAD:backend/onyx/connectors/sharepoint/connector.py:788:        sites_summary = ", ".join(unauthorized_sites)
HEAD:backend/onyx/connectors/teams/connector.py:172:                    "Invalid or expired Microsoft Teams credentials (401 Unauthorized)."
HEAD:backend/onyx/connectors/teams/connector.py:176:                    "Your app lacks sufficient permissions to read Teams (403 Forbidden)."
HEAD:backend/onyx/connectors/teams/connector.py:183:                "unauthorized" in error_str
HEAD:backend/onyx/connectors/teams/connector.py:190:            elif "forbidden" in error_str or "403" in error_str:
HEAD:backend/onyx/connectors/web/connector.py:211:                "Received 403 Forbidden for %s, will retry with browser automation", url
HEAD:backend/onyx/connectors/web/connector.py:217:            401: "Unauthorized",
HEAD:backend/onyx/connectors/web/connector.py:218:            403: "Forbidden",
HEAD:backend/onyx/connectors/web/connector.py:836:                    f"Unauthorized access to '{test_url}': {e}"
HEAD:backend/onyx/connectors/web/connector.py:840:                    f"Forbidden access to '{test_url}': {e}"
HEAD:backend/onyx/connectors/zoom/client.py:197:                f"Zoom rejected {description} as unauthorized, even with a fresh token"
HEAD:backend/onyx/context/search/forced_document_set.py:7:Fail-closed by construction: a name that doesn't exist matches no chunk, so the
HEAD:backend/onyx/context/search/pipeline.py:77:        unauthorized = sorted(
HEAD:backend/onyx/context/search/pipeline.py:80:        if unauthorized:
HEAD:backend/onyx/context/search/pipeline.py:83:                f"User does not have access to document sets: {unauthorized}",
HEAD:backend/onyx/db/enums.py:814:        """None outside incognito. Unknown values fail closed to USAGE_ONLY."""
HEAD:backend/onyx/db/models.py:611:    # user access). An empty list grants nothing (fail-closed).
HEAD:backend/onyx/document_index/opensearch/schema.py:31:    DocumentIDTooLongError,
HEAD:backend/onyx/document_index/opensearch/schema.py:112:    except DocumentIDTooLongError:
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:6:class DocumentIDTooLongError(ValueError):
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:35:        DocumentIDTooLongError: If the document ID is too long after filtering.
HEAD:backend/onyx/document_index/opensearch/string_filtering.py:45:        raise DocumentIDTooLongError(
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:280:                    HTTPStatus.UNAUTHORIZED,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:281:                    HTTPStatus.FORBIDDEN,
HEAD:backend/onyx/error_handling/error_codes.py:39:    UNAUTHORIZED = ("UNAUTHORIZED", 403)
HEAD:backend/onyx/error_handling/error_codes.py:151:    403: OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/file_store/azure_blob_file_store.py:173:                    "Azure container '%s' exists but access is forbidden",
HEAD:backend/onyx/file_store/file_store.py:326:                    "S3 bucket '%s' exists but access is forbidden", bucket_name
HEAD:backend/onyx/file_store/gcs_file_store.py:128:        from google.api_core.exceptions import Forbidden, NotFound
HEAD:backend/onyx/file_store/gcs_file_store.py:138:        except Forbidden:
HEAD:backend/onyx/file_store/gcs_file_store.py:140:                "GCS bucket '%s' exists but access is forbidden", self._bucket_name
HEAD:backend/onyx/llm/multi_llm.py:274:    to avoid the "toolConfig field must be defined" error.
HEAD:backend/onyx/main.py:543:    application.add_exception_handler(status.HTTP_401_UNAUTHORIZED, log_http_error)
HEAD:backend/onyx/main.py:544:    application.add_exception_handler(status.HTTP_403_FORBIDDEN, log_http_error)
HEAD:backend/onyx/mcp_server/tools/search.py:354:    outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/mcp_server/tools/search.py:441:    outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/mcp_server/tools/search.py:501:    outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:103:_AUTH_ERROR_UNAUTHORIZED = "unauthorized"
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:234:        or _AUTH_ERROR_UNAUTHORIZED in error_str
HEAD:backend/onyx/onyxbot/discord/handle_commands.py:50:    except (discord.Forbidden, discord.HTTPException) as e:
HEAD:backend/onyx/onyxbot/discord/handle_commands.py:64:    except (discord.Forbidden, discord.HTTPException) as e:
HEAD:backend/onyx/onyxbot/discord/handle_commands.py:77:    except (discord.Forbidden, discord.HTTPException) as e:
HEAD:backend/onyx/onyxbot/slack/handlers/handle_message.py:318:                        OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/onyxbot/slack/handlers/handle_message.py:330:                            if e.error_code == OnyxErrorCode.UNAUTHORIZED
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:3:Fail-closed: identity, body-size cap, and unidentified-sandbox checks.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:71:# Bodies over this cap are fail-closed (rejected), not parsed by the matcher.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:136:    api-server (host + port) and any public address. Fail closed: a resolution
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:395:            # Fail closed: an unguarded raise here would let mitmproxy forward
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:417:        # silently bypassing the gate. Fail closed instead.
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:518:        * fail-closed — sets a 403 `flow.response` first (unidentified
HEAD:backend/onyx/sandbox_proxy/addons/gate.py:1262:            # Stale, foreign, or tampered tag. Fail closed — do not guess.
HEAD:backend/onyx/sandbox_proxy/credential_injection.py:67:        """Render auth headers; raise `CredentialUnavailableError` to fail closed."""
HEAD:backend/onyx/sandbox_proxy/identity.py:139:        bounds a tampered tag to the same user; mismatches fail closed.
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:46:    UNCLASSIFIABLE = "UNCLASSIFIABLE"  # fail closed — deny
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:108:    classify → fail closed)."""
HEAD:backend/onyx/sandbox_proxy/mcp_jsonrpc.py:114:        # RecursionError: a deeply-nested body must fail closed, not crash the
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:49:# action_type for an unclassifiable request to a matched MCP host (fail closed).
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:199:            # Once attributed to an MCP host, a failure must fail closed: the
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:27:    attribution is arbitrary, so consumers must fail closed."""
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:104:        # evaluator failed and the gate fell open — fail closed here so no
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:113:                    "gate. Retry the tool call."
HEAD:backend/onyx/server/auth/captcha_api.py:76:        raise OnyxError(OnyxErrorCode.UNAUTHORIZED, str(exc))
HEAD:backend/onyx/server/auth/captcha_api.py:111:                        OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/auth/captcha_api.py:133:    server-side shared secret. Empty env var = bypass disabled (fail-closed)
HEAD:backend/onyx/server/auth/captcha_api.py:186:                        OnyxError(OnyxErrorCode.UNAUTHORIZED, str(exc))
HEAD:backend/onyx/server/documents/connector.py:992:                status.setdefault("permissions", {})  # fail-closed for mock rows
HEAD:backend/onyx/server/features/build/db/build_session.py:274:    Returns the updated session, or None if not found/unauthorized.
HEAD:backend/onyx/server/features/build/interactive_turns/executor.py:73:_TOOL_TIMEOUT_CONTINUATION_PROMPT = (
HEAD:backend/onyx/server/features/build/interactive_turns/executor.py:490:                current_prompt = _TOOL_TIMEOUT_CONTINUATION_PROMPT
HEAD:backend/onyx/server/features/build/sandbox/image/opencode-plugins/webapp.ts:1:// Failures are returned as observations, never thrown; a thrown tool error
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:295:    Error-state tool parts carry their message in ``state.error`` instead of
HEAD:backend/onyx/server/features/build/session/sandbox_lifecycle.py:820:    Invariant: snapshot before terminate, fail-closed — a snapshot failure on
HEAD:backend/onyx/server/features/build/session/sandbox_lifecycle.py:896:    # Fail-closed: terminating with an unsnapshotted workspace loses it
HEAD:backend/onyx/server/features/build/timeouts.py:172:# "snapshotting can take minutes"; the reaper is fail-closed on snapshot
HEAD:backend/onyx/server/features/document_set/models.py:157:    # Defaults empty (fail-closed); the list endpoint stamps the real map.
HEAD:backend/onyx/server/features/document_set/models.py:171:        an empty (fail-closed) map — the document-set list endpoint stamps the real one;
HEAD:backend/onyx/server/features/mcp/api.py:661:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/features/mcp/api.py:934:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/features/mcp/api.py:1585:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/features/mcp/api.py:2191:    #     raise HTTPException(status_code=403, detail="Forbidden")
HEAD:backend/onyx/server/features/mcp/client.py:25:from onyx.configs.app_configs import MCP_TOOL_CALL_TIMEOUT_SECONDS
HEAD:backend/onyx/server/features/mcp/client.py:165:                read_timeout_seconds=timedelta(seconds=MCP_TOOL_CALL_TIMEOUT_SECONDS),
HEAD:backend/onyx/server/features/mcp/models.py:730:    # Server-stamped affordance map; fail-closed empty (only the admin server list stamps it).
HEAD:backend/onyx/server/features/notifications/api.py:232:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/features/persona/api.py:596:        # not forbidden. Only checked once the delete has already failed, so the
HEAD:backend/onyx/server/features/persona/api.py:625:# so without this a scoped PAT is rejected fail-closed. MCP clients need this
HEAD:backend/onyx/server/features/persona/models.py:239:    # stamp it (fail-closed on the client). List endpoints stamp it so each card
HEAD:backend/onyx/server/features/persona/models.py:248:        # Fail closed: the owner email is PII and is only included when a caller
HEAD:backend/onyx/server/features/projects/api.py:189:                OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/features/search/api.py:113:            raise OnyxError(OnyxErrorCode.UNAUTHORIZED)
HEAD:backend/onyx/server/features/tool/models.py:42:    # Server-stamped affordance map; fail-closed empty (only the admin actions list stamps it).
HEAD:backend/onyx/server/manage/users.py:1068:        raise BasicAuthenticationError(detail="Unauthorized")
HEAD:backend/onyx/server/oidc_multi.py:117:        raise OnyxError(OnyxErrorCode.UNAUTHORIZED, _NO_WORKSPACE_DETAIL)
HEAD:backend/onyx/server/oidc_multi.py:135:        raise OnyxError(OnyxErrorCode.UNAUTHORIZED, _NO_WORKSPACE_DETAIL)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:32:    CustomToolErrorInfo,
HEAD:backend/onyx/server/query_and_chat/session_loading.py:194:    error: CustomToolErrorInfo | None = None,
HEAD:backend/onyx/server/query_and_chat/session_loading.py:747:                        custom_error: CustomToolErrorInfo | None = None
HEAD:backend/onyx/server/query_and_chat/session_loading.py:758:                                    custom_error = CustomToolErrorInfo(
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:283:class CustomToolErrorInfo(BaseModel):
HEAD:backend/onyx/server/query_and_chat/streaming_models.py:300:    error: CustomToolErrorInfo | None = None
HEAD:backend/onyx/server/saml_multi.py:156:    raise OnyxError(OnyxErrorCode.UNAUTHORIZED, "unrecognized SAML issuer")
HEAD:backend/onyx/server/saml_multi.py:167:        raise OnyxError(OnyxErrorCode.UNAUTHORIZED, "malformed SAML response")
HEAD:backend/onyx/server/saml_multi.py:179:    raise OnyxError(OnyxErrorCode.UNAUTHORIZED, "SAML response missing issuer")
HEAD:backend/onyx/server/saml_multi.py:196:    raise OnyxError(OnyxErrorCode.UNAUTHORIZED, detail)
HEAD:backend/onyx/server/saml_multi.py:250:        OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/saml_multi.py:325:        raise OnyxError(OnyxErrorCode.UNAUTHORIZED, "missing SAML response")
HEAD:backend/onyx/server/saml_multi.py:350:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/settings/api.py:85:        # Fail closed: a settings-read error must not fall back to defaults and
HEAD:backend/onyx/server/settings/store.py:65:        # re-raise so they can fail closed instead of trusting the default.
HEAD:backend/onyx/server/utils.py:13:        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:445:Without `--enable react-devtools`, the `react …` commands error. `vitals` and `pushstate` work on any site regardless of framework. `vitals` prints a summary by default; use `--json` for the full structured payload.
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1131:Use `-b`/`--base64` or `--stdin` for reliable execution. Shell escaping with nested quotes and special characters is error-prone.
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1288:Supported formats: JSON array of `{name, value}`, a cURL dump from DevTools -> Network -> Copy as cURL, or a bare Cookie header. Errors never echo cookie values.
HEAD:backend/onyx/tools/models.py:21:    CustomToolErrorInfo,
HEAD:backend/onyx/tools/models.py:31:class ToolCallException(Exception):
HEAD:backend/onyx/tools/models.py:42:class ToolExecutionException(Exception):
HEAD:backend/onyx/tools/models.py:65:    error: CustomToolErrorInfo | None = None
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:21:from onyx.tools.models import ToolCallException, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:136:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:146:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:19:from onyx.tools.models import ToolCallException, ToolCallKickoff, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:127:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:135:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:18:    CustomToolErrorInfo,
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:31:    ToolCallException,
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:80:                "Tool '%s' has both an Authorization header and OAuth token set. This is likely a configuration error as the OAuth token will override the custom header.",
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:160:                raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:200:        error_info: CustomToolErrorInfo | None = None
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:202:            error_info = CustomToolErrorInfo(
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:22:from onyx.tools.models import ToolCallException, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:126:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:132:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:154:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:179:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:198:        except ToolCallException:
HEAD:backend/onyx/tools/tool_implementations/file_reader/file_reader_tool.py:201:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:37:from onyx.tools.models import ToolCallException, ToolExecutionException, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:175:            raise ToolExecutionException(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:187:                    raise ToolExecutionException(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:195:                    raise ToolExecutionException(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:200:                    raise ToolExecutionException(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:205:            raise ToolExecutionException(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:222:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:246:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:271:                raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:280:                raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:288:                raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:311:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:38:    "unauthorized",
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:40:    "forbidden",
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:153:        outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:210:                outcome = MCPToolCallStatus.AUTH_ERROR
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:215:                        tool_result=error_result,
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:297:                outcome = MCPToolCallStatus.AUTH_ERROR
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:325:                    tool_result=error_result,
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:25:from onyx.tools.models import ChatMinimalTextMessage, ToolCallException, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:114:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:35:from onyx.tools.models import OpenURLToolOverrideKwargs, ToolCallException, ToolResponse
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:556:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/python/code_interpreter_client.py:170:    """SSE 'error' event: execution-level error"""
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:37:    ToolCallException,
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:223:    # rejects requests that define a tool with that name (400 invalid_request_error,
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:367:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:113:    ToolCallException,
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:703:                unauthorized = sorted(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:706:                if unauthorized:
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:709:                        f"User does not have access to document sets: {unauthorized}",
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:766:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:21:    ToolCallException,
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:208:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:218:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:269:        # If all queries failed, raise ToolCallException with details
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:272:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:308:            raise ToolCallException(
HEAD:backend/onyx/tools/tool_runner.py:23:    ToolCallException,
HEAD:backend/onyx/tools/tool_runner.py:25:    ToolExecutionException,
HEAD:backend/onyx/tools/tool_runner.py:50:GENERIC_TOOL_ERROR_MESSAGE = "Tool failed with error: {error}"
HEAD:backend/onyx/tools/tool_runner.py:52:# 10 minute timeout for tool execution to prevent indefinite hangs
HEAD:backend/onyx/tools/tool_runner.py:53:TOOL_EXECUTION_TIMEOUT_SECONDS = 10 * 60
HEAD:backend/onyx/tools/tool_runner.py:128:    - ToolCallException: Expected errors from tool execution (e.g., invalid input,
HEAD:backend/onyx/tools/tool_runner.py:147:        except ToolCallException as e:
HEAD:backend/onyx/tools/tool_runner.py:148:            # ToolCallException is an expected error from tool execution
HEAD:backend/onyx/tools/tool_runner.py:150:            logger.error("Tool call error for %s: %s", tool.name, e)
HEAD:backend/onyx/tools/tool_runner.py:153:                llm_facing_response=GENERIC_TOOL_ERROR_MESSAGE.format(
HEAD:backend/onyx/tools/tool_runner.py:159:                    message="Tool call error (expected)",
HEAD:backend/onyx/tools/tool_runner.py:167:                        "error_type": "ToolCallException",
HEAD:backend/onyx/tools/tool_runner.py:171:        except ToolExecutionException as e:
HEAD:backend/onyx/tools/tool_runner.py:176:                llm_facing_response=GENERIC_TOOL_ERROR_MESSAGE.format(error=str(e)),
HEAD:backend/onyx/tools/tool_runner.py:180:                    message="Tool execution error (unexpected)",
HEAD:backend/onyx/tools/tool_runner.py:203:                llm_facing_response=GENERIC_TOOL_ERROR_MESSAGE.format(error=str(e)),
HEAD:backend/onyx/tools/tool_runner.py:207:                    message="Tool execution error (unexpected)",
HEAD:backend/onyx/tools/tool_runner.py:435:        timeout=TOOL_EXECUTION_TIMEOUT_SECONDS,
HEAD:backend/onyx/utils/external_endpoint.py:123:        # logs, hook execution records, and user-facing error details.
HEAD:backend/onyx/utils/external_endpoint.py:244:            # reach logs, execution records, or user-facing error details.
```
## Execution Audit / Logging Signals
Evidence lines: 490
```text
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:71:            "name": "hook-execution-log-cleanup",
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:72:            "task": OnyxCeleryTask.HOOK_EXECUTION_LOG_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:6:from onyx.db.hook import cleanup_old_execution_logs__no_commit
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:11:_HOOK_EXECUTION_LOG_RETENTION_DAYS: int = 30
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:15:    name=OnyxCeleryTask.HOOK_EXECUTION_LOG_CLEANUP_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:20:def hook_execution_log_cleanup_task(*, tenant_id: str) -> None:  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:23:            deleted: int = cleanup_old_execution_logs__no_commit(
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:25:                max_age_days=_HOOK_EXECUTION_LOG_RETENTION_DAYS,
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:30:                    "Deleted %s hook execution log(s) older than %s days.",
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:32:                    _HOOK_EXECUTION_LOG_RETENTION_DAYS,
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:35:        logger.exception("Failed to clean up hook execution logs")
HEAD:backend/ee/onyx/db/user_group.py:70:    AuditAction,
HEAD:backend/ee/onyx/db/user_group.py:916:            AuditAction.USER_GROUP_CHANGE,
HEAD:backend/ee/onyx/hooks/executor.py:42:     completes to write the HookExecutionLog row on failure. Success runs are
HEAD:backend/ee/onyx/hooks/executor.py:48:     prevent the execution log from being written. This update is best-effort.
HEAD:backend/ee/onyx/hooks/executor.py:59:    create_hook_execution_log__no_commit,
HEAD:backend/ee/onyx/hooks/executor.py:112:    """Write the execution log on failure and optionally update is_reachable, each
HEAD:backend/ee/onyx/hooks/executor.py:114:    # Only write the execution log on failure — success runs are not recorded.
HEAD:backend/ee/onyx/hooks/executor.py:120:                create_hook_execution_log__no_commit(
HEAD:backend/ee/onyx/hooks/executor.py:131:                "Failed to persist hook execution log for hook_id=%s", hook_id
HEAD:backend/ee/onyx/server/billing/service.py:127:        logger.error("%s: %s - %s", error_message, e.response.status_code, detail)
HEAD:backend/ee/onyx/server/enterprise_settings/store.py:169:        logger.warning("Logo has a %s header but does not decode", mime_type)
HEAD:backend/ee/onyx/server/features/hooks/api.py:14:    get_hook_execution_logs,
HEAD:backend/ee/onyx/server/features/hooks/api.py:450:# Execution log endpoints
HEAD:backend/ee/onyx/server/features/hooks/api.py:454:@router.get("/{hook_id}/execution-logs")
HEAD:backend/ee/onyx/server/features/hooks/api.py:455:def list_hook_execution_logs(
HEAD:backend/ee/onyx/server/features/hooks/api.py:463:    logs = get_hook_execution_logs(db_session=db_session, hook_id=hook_id, limit=limit)
HEAD:backend/ee/onyx/server/scim/api.py:76:    AuditAction,
HEAD:backend/ee/onyx/server/scim/api.py:111:            AuditAction.USER_GROUP_RENAME,
HEAD:backend/ee/onyx/server/scim/api.py:121:            AuditAction.USER_GROUP_CHANGE,
HEAD:backend/ee/onyx/server/scim/api.py:1375:        AuditAction.USER_GROUP_CREATE,
HEAD:backend/ee/onyx/server/scim/api.py:1590:        AuditAction.USER_GROUP_DELETE,
HEAD:backend/ee/onyx/server/seeding.py:80:        logger.notice("Seeding Custom Tools")
HEAD:backend/ee/onyx/server/seeding.py:83:                logger.debug("Attempting to seed tool: %s", tool.name)
HEAD:backend/ee/onyx/server/seeding.py:84:                logger.debug("Reading definition from: %s", tool.definition_path)
HEAD:backend/ee/onyx/server/seeding.py:100:                logger.debug("Successfully added tool: %s", tool.name)
HEAD:backend/ee/onyx/server/seeding.py:112:                logger.error("Failed to seed tool %s: %s", tool.name, str(e))
HEAD:backend/ee/onyx/server/seeding.py:114:        logger.notice("Successfully seeded %s Custom Tools", len(tools))
HEAD:backend/ee/onyx/server/tenants/admin_api.py:12:    AuditAction,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:39:            AuditAction.IMPERSONATE,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:76:                AuditAction.IMPERSONATE,
HEAD:backend/ee/onyx/server/tenants/admin_api.py:100:        AuditAction.IMPERSONATE,
HEAD:backend/ee/onyx/server/tenants/proxy.py:214:        logger.error("Control plane returned %s: %s", status_code, detail)
HEAD:backend/ee/onyx/server/user_group/api.py:70:    AuditAction,
HEAD:backend/ee/onyx/server/user_group/api.py:253:        AuditAction.USER_GROUP_PERMISSION_CHANGE,
HEAD:backend/ee/onyx/server/user_group/api.py:284:        AuditAction.USER_GROUP_CREATE,
HEAD:backend/ee/onyx/server/user_group/api.py:324:            AuditAction.USER_GROUP_RENAME,
HEAD:backend/ee/onyx/server/user_group/api.py:438:        AuditAction.USER_GROUP_DELETE,
HEAD:backend/ee/onyx/server/user_group/api.py:646:        AuditAction.USER_GROUP_MANAGER_CHANGE,
HEAD:backend/ee/onyx/utils/license.py:224:        logger.error("[verify_license] FAILED: JSON decode error: %s", e)
HEAD:backend/onyx/auth/email_utils.py:267:        logger.warning("Unexpected status code %s", response.status_code)
HEAD:backend/onyx/auth/login_claims_capture.py:321:                logger.warning("OAuth claims capture: id_token decode failed: %s", e)
HEAD:backend/onyx/auth/mobile_sso/code_store.py:81:        logger.error(
HEAD:backend/onyx/auth/scoped_permissions.py:25:    AuditAction,
HEAD:backend/onyx/auth/scoped_permissions.py:40:        AuditAction.PERMISSION_DENIED,
HEAD:backend/onyx/auth/users.py:159:from onyx.utils.audit import AuditAction, AuditActor, AuditOutcome, emit_audit_event
HEAD:backend/onyx/auth/users.py:1298:            AuditAction.LOGIN,
HEAD:backend/onyx/auth/users.py:1410:            AuditAction.REGISTER,
HEAD:backend/onyx/auth/users.py:1449:            AuditAction.PASSWORD_FORGOT,
HEAD:backend/onyx/auth/users.py:1460:            AuditAction.PASSWORD_RESET,
HEAD:backend/onyx/auth/users.py:1508:                AuditAction.EMAIL_VERIFY,
HEAD:backend/onyx/auth/users.py:1533:                AuditAction.LOGIN_FAILURE,
HEAD:backend/onyx/background/celery/tasks/vespa/tasks.py:587:            task_logger.info(f"doc={document_id} action=sync elapsed={elapsed:.2f}")
HEAD:backend/onyx/chat/llm_loop.py:1093:            # Run the LLM selected tools, there is some more logic here than a simple execution
HEAD:backend/onyx/chat/llm_loop.py:1094:            # each tool might have custom logic here
HEAD:backend/onyx/chat/llm_step.py:281:    """Format message history for logging, with special handling for tool calls.
HEAD:backend/onyx/chat/llm_step.py:1543:            logger.debug("Tool calls:\n%s", tool_calls_str)
HEAD:backend/onyx/chat/llm_step.py:1545:            logger.debug("Tool calls: []")
HEAD:backend/onyx/configs/app_configs.py:1556:# validation, execution logs, and reachability tracking. If both are set, this
HEAD:backend/onyx/configs/constants.py:715:    # Hook execution log retention
HEAD:backend/onyx/configs/constants.py:716:    HOOK_EXECUTION_LOG_CLEANUP_TASK = "hook_execution_log_cleanup_task"
HEAD:backend/onyx/configs/tool_configs.py:23:        logger.error(
HEAD:backend/onyx/connectors/gmail/connector.py:179:            logger.warning("Failed to decode Gmail message part: %s", error)
HEAD:backend/onyx/connectors/imap/connector.py:417:            logger.warning("Could not decode part with charset %s: %s", charset, e)
HEAD:backend/onyx/connectors/slack/connector.py:473:                f"{list(itertools.islice(all_channel_names, SlackConnector.MAX_CHANNELS_TO_LOG))}"
HEAD:backend/onyx/context/search/federated/slack_search.py:372:        logger.debug("Failed to parse entities for channel data extraction")
HEAD:backend/onyx/db/hook.py:11:from onyx.db.models import Hook, HookExecutionLog
HEAD:backend/onyx/db/hook.py:176:# ── HookExecutionLog CRUD ────────────────────────────────────────────────
HEAD:backend/onyx/db/hook.py:179:def create_hook_execution_log__no_commit(
HEAD:backend/onyx/db/hook.py:187:) -> HookExecutionLog:
HEAD:backend/onyx/db/hook.py:188:    log = HookExecutionLog(
HEAD:backend/onyx/db/hook.py:200:def get_hook_execution_logs(
HEAD:backend/onyx/db/hook.py:205:) -> list[HookExecutionLog]:
HEAD:backend/onyx/db/hook.py:207:        select(HookExecutionLog)
HEAD:backend/onyx/db/hook.py:208:        .where(HookExecutionLog.hook_id == hook_id)
HEAD:backend/onyx/db/hook.py:209:        .order_by(HookExecutionLog.created_at.desc())
HEAD:backend/onyx/db/hook.py:215:def cleanup_old_execution_logs__no_commit(
HEAD:backend/onyx/db/hook.py:220:    """Delete execution logs older than max_age_days. Returns the number of rows deleted."""
HEAD:backend/onyx/db/hook.py:225:        delete(HookExecutionLog)
HEAD:backend/onyx/db/hook.py:226:        .where(HookExecutionLog.created_at < cutoff)
HEAD:backend/onyx/db/mcp.py:317:    logger.info(
HEAD:backend/onyx/db/mcp.py:324:    logger.info("Successfully deleted MCP server %s and its tools", server_id)
HEAD:backend/onyx/db/memory.py:76:        logger.warning("Unknown user language %r, omitting the language hint", code)
HEAD:backend/onyx/db/models.py:7140:    execution_logs: Mapped[list["HookExecutionLog"]] = relationship(
HEAD:backend/onyx/db/models.py:7141:        "HookExecutionLog", back_populates="hook", cascade="all, delete-orphan"
HEAD:backend/onyx/db/models.py:7154:class HookExecutionLog(Base):
HEAD:backend/onyx/db/models.py:7162:    __tablename__ = "hook_execution_log"
HEAD:backend/onyx/db/models.py:7179:    hook: Mapped["Hook"] = relationship("Hook", back_populates="execution_logs")
HEAD:backend/onyx/db/models.py:7414:    ``action_id`` is a catalog id (external apps) or a tool name (MCP servers);
HEAD:backend/onyx/db/models.py:7415:    display (name/description) comes from the code catalog / discovered tools.
HEAD:backend/onyx/deep_research/dr_loop.py:574:                    logger.warning("No tool calls found, this should not happen.")
HEAD:backend/onyx/error_handling/exceptions.py:71:        logger.error("OnyxError %s: %s", exc.error_code.code, detail)
HEAD:backend/onyx/error_handling/exceptions.py:73:        logger.warning("OnyxError %s: %s", exc.error_code.code, detail)
HEAD:backend/onyx/external_apps/presentation/decode.py:29:        logger.exception("payload_decode_failed action_type=%s", action_type)
HEAD:backend/onyx/file_processing/extract_file_text.py:339:        logger.warning("Invalid PDF file, skipping content extraction: %s", e)
HEAD:backend/onyx/file_processing/extract_file_text.py:344:        logger.warning("Failed to read PDF, skipping content extraction: %s", e)
HEAD:backend/onyx/kg/extractions/extraction_processing.py:227:    logger.info("Starting kg extraction for tenant %s", tenant_id)
HEAD:backend/onyx/kg/extractions/extraction_processing.py:284:                logger.info(
HEAD:backend/onyx/kg/extractions/extraction_processing.py:295:            logger.info("Processing document batch %s", document_batch_counter)
HEAD:backend/onyx/kg/extractions/extraction_processing.py:311:                    logger.debug(
HEAD:backend/onyx/kg/extractions/extraction_processing.py:459:                    logger.error(
HEAD:backend/onyx/kg/extractions/extraction_processing.py:522:                    logger.error("Error adding entity %s. Error message: %s", entity, e)
HEAD:backend/onyx/kg/extractions/extraction_processing.py:528:                    logger.error(
HEAD:backend/onyx/kg/extractions/extraction_processing.py:559:                        logger.error(
HEAD:backend/onyx/kg/extractions/extraction_processing.py:575:                            logger.error(
HEAD:backend/onyx/kg/utils/extraction_utils.py:475:        logger.error(
HEAD:backend/onyx/kg/utils/extraction_utils.py:556:        logger.error(
HEAD:backend/onyx/llm/multi_llm.py:414:def _log_chat_completions_tools_disable_reasoning(
HEAD:backend/onyx/llm/multi_llm.py:805:            _log_chat_completions_tools_disable_reasoning(model, self._api_base)
HEAD:backend/onyx/llm/multi_llm.py:1112:                        _log_chat_completions_tools_disable_reasoning(
HEAD:backend/onyx/llm/tracing_wrap.py:178:    wrap reassembles them via ``_merge_tool_call_delta`` before logging so
HEAD:backend/onyx/mcp_server/api.py:32:logger.info("Creating Onyx MCP Server...")
HEAD:backend/onyx/mcp_server/api.py:45:logger.info("MCP server instance created")
HEAD:backend/onyx/mcp_server/api.py:74:        logger.info("MCP server starting up")
HEAD:backend/onyx/mcp_server/api.py:80:            logger.info("MCP server shutting down")
HEAD:backend/onyx/mcp_server/api.py:103:        logger.info("CORS origins: %s", MCP_SERVER_CORS_ORIGINS)
HEAD:backend/onyx/mcp_server/auth.py:27:            logger.error(
HEAD:backend/onyx/mcp_server/auth.py:36:            logger.warning(
HEAD:backend/onyx/mcp_server/resources/agents.py:34:    logger.info(
HEAD:backend/onyx/mcp_server/resources/document_sets.py:33:    logger.info(
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:30:    logger.info(
HEAD:backend/onyx/mcp_server/tools/search.py:95:        logger.debug("Onyx MCP Server: error body was not JSON (%s)", exc)
HEAD:backend/onyx/mcp_server/tools/search.py:335:    logger.info(
HEAD:backend/onyx/mcp_server/tools/search.py:368:            logger.info("Onyx MCP Server: No indexed sources available for tenant")
HEAD:backend/onyx/mcp_server/tools/search.py:379:            logger.warning(
HEAD:backend/onyx/mcp_server/tools/search.py:403:        logger.info(
HEAD:backend/onyx/mcp_server/tools/search.py:408:        logger.error("Onyx MCP Server: Document search error: %s", err, exc_info=True)
HEAD:backend/onyx/mcp_server/tools/search.py:438:    logger.info("Onyx MCP Server: Web search: query='%s', limit=%s", query, limit)
HEAD:backend/onyx/mcp_server/tools/search.py:464:        logger.error("Onyx MCP Server: Web search error: %s", e, exc_info=True)
HEAD:backend/onyx/mcp_server/tools/search.py:498:    logger.info("Onyx MCP Server: Open URL: fetching %s URLs", len(urls))
HEAD:backend/onyx/mcp_server/tools/search.py:517:        logger.error("Onyx MCP Server: URL fetch error: %s", err, exc_info=True)
HEAD:backend/onyx/mcp_server/utils.py:100:        logger.error(
HEAD:backend/onyx/mcp_server/utils.py:107:        logger.error(
HEAD:backend/onyx/mcp_server/utils.py:130:        logger.error(
HEAD:backend/onyx/mcp_server/utils.py:136:        logger.error(
HEAD:backend/onyx/mcp_server/utils.py:159:        logger.error(
HEAD:backend/onyx/mcp_server/utils.py:165:        logger.error(
HEAD:backend/onyx/mcp_server_main.py:20:        logger.info("MCP server is disabled (MCP_SERVER_ENABLED=false)")
HEAD:backend/onyx/mcp_server_main.py:25:    logger.info("Starting MCP server on %s:%s", MCP_SERVER_HOST, MCP_SERVER_PORT)
HEAD:backend/onyx/natural_language_processing/search_nlp_models.py:1402:    logger.debug("Warming up encoder model: %s", embedding_model.model_name)
HEAD:backend/onyx/onyxbot/slack/handlers/handle_buttons.py:96:        logger.error("Missing actions. Unable to build the source feedback view")
HEAD:backend/onyx/onyxbot/slack/listener.py:906:        logger.error("Unable to process feedback. Action not found")
HEAD:backend/onyx/onyxbot/slack/utils.py:182:            logger.error("Failed to remove Reaction due to: %s", e)
HEAD:backend/onyx/sandbox_proxy/request_evaluator.py:200:            # gate turns evaluator exceptions into "off-catalog", and the MCP
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_matching.py:56:        logger.warning(
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:54:from onyx.utils.credential_audit import emit_credential_access
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:81:        # on a shared host (MCP servers aren't in that catalog) — defer. An MCP
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:166:                    f"user {short_log_id(user_id)} lacks access to MCP server "
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:205:            self._audit(server, user_id)
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:208:    def _audit(self, server: MCPServer, user_id: UUID) -> None:
HEAD:backend/onyx/sandbox_proxy/resolvers/mcp_server.py:273:        logger.exception("mcp_token_refresh.failed config_id=%s", connection_config_id)
HEAD:backend/onyx/server/api_key/api.py:21:    AuditAction,
HEAD:backend/onyx/server/api_key/api.py:64:        AuditAction.API_KEY_CREATE,
HEAD:backend/onyx/server/api_key/api.py:84:        AuditAction.API_KEY_REGENERATE,
HEAD:backend/onyx/server/api_key/api.py:106:        AuditAction.API_KEY_UPDATE,
HEAD:backend/onyx/server/api_key/api.py:126:        AuditAction.API_KEY_DELETE,
HEAD:backend/onyx/server/documents/cc_pair.py:88:    AuditAction,
HEAD:backend/onyx/server/documents/cc_pair.py:556:        AuditAction.CC_PAIR_UPDATE,
HEAD:backend/onyx/server/documents/cc_pair.py:885:            AuditAction.CC_PAIR_CREATE,
HEAD:backend/onyx/server/documents/cc_pair.py:950:            AuditAction.CC_PAIR_DELETE,
HEAD:backend/onyx/server/documents/connector.py:154:    AuditAction,
HEAD:backend/onyx/server/documents/connector.py:1485:            AuditAction.CONNECTOR_CREATE,
HEAD:backend/onyx/server/documents/connector.py:1610:        AuditAction.CONNECTOR_UPDATE,
HEAD:backend/onyx/server/documents/connector.py:1654:        AuditAction.CONNECTOR_DELETE,
HEAD:backend/onyx/server/documents/credential.py:42:    AuditAction,
HEAD:backend/onyx/server/documents/credential.py:111:        AuditAction.CREDENTIAL_DELETE,
HEAD:backend/onyx/server/documents/credential.py:180:        AuditAction.CREDENTIAL_CREATE,
HEAD:backend/onyx/server/documents/credential.py:244:        AuditAction.CREDENTIAL_CREATE,
HEAD:backend/onyx/server/documents/credential.py:395:        AuditAction.CREDENTIAL_UPDATE,
HEAD:backend/onyx/server/documents/credential.py:435:        AuditAction.CREDENTIAL_DELETE,
HEAD:backend/onyx/server/documents/credential.py:456:        AuditAction.CREDENTIAL_DELETE,
HEAD:backend/onyx/server/features/build/sandbox/base.py:139:        Craft MCP servers and the gateway provider catalog are NOT registered
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:208:# Surfaces the `webapp` tool (start/status/logs/restart); always on.
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1352:            logger.info("No opencode history to snapshot for sandbox %s.", sandbox_id)
HEAD:backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py:1863:            logger.warning("AGENTS.md attachments section update failed: %s", e)
HEAD:backend/onyx/server/features/build/sandbox/image/templates/outputs/web/AGENTS.md:7:- **The development server is already running** (started by the `webapp` tool, which scaffolded this app) on a dynamically allocated port. Do NOT run `bun run dev` yourself. Use the `webapp` tool's `status`/`logs` actions to check on it (logs also at `../../nextjs.log`).
HEAD:backend/onyx/server/features/build/sandbox/image/templates/outputs/web/bun.lock:878:    "radix-ui": ["radix-ui@1.4.3", "", { "dependencies": { "@radix-ui/primitive": "1.1.3", "@radix-ui/react-accessible-icon": "1.1.7", "@radix-ui/react-accordion": "1.2.12", "@radix-ui/react-alert-dialog": "1.1.15", "@radix-ui/react-arrow": "1.1.7", "@radix-ui/react-aspect-ratio": "1.1.7", "@radix-ui/react-avatar": "1.1.10", "@radix-ui/react-checkbox": "1.3.3", "@radix-ui/react-collapsible": "1.1.12", "@radix-ui/react-collection": "1.1.7", "@radix-ui/react-compose-refs": "1.1.2", "@radix-ui/react-context": "1.1.2", "@radix-ui/react-context-menu": "2.2.16", "@radix-ui/react-dialog": "1.1.15", "@radix-ui/react-direction": "1.1.1", "@radix-ui/react-dismissable-layer": "1.1.11", "@radix-ui/react-dropdown-menu": "2.1.16", "@radix-ui/react-focus-guards": "1.1.3", "@radix-ui/react-focus-scope": "1.1.7", "@radix-ui/react-form": "0.1.8", "@radix-ui/react-hover-card": "1.1.15", "@radix-ui/react-label": "2.1.7", "@radix-ui/react-menu": "2.1.16", "@radix-ui/react-menubar": "1.1.16", "@radix-ui/react-navigation-menu": "1.2.14", "@radix-ui/react-one-time-password-field": "0.1.8", "@radix-ui/react-password-toggle-field": "0.1.3", "@radix-ui/react-popover": "1.1.15", "@radix-ui/react-popper": "1.2.8", "@radix-ui/react-portal": "1.1.9", "@radix-ui/react-presence": "1.1.5", "@radix-ui/react-primitive": "2.1.3", "@radix-ui/react-progress": "1.1.7", "@radix-ui/react-radio-group": "1.3.8", "@radix-ui/react-roving-focus": "1.1.11", "@radix-ui/react-scroll-area": "1.2.10", "@radix-ui/react-select": "2.2.6", "@radix-ui/react-separator": "1.1.7", "@radix-ui/react-slider": "1.3.6", "@radix-ui/react-slot": "1.2.3", "@radix-ui/react-switch": "1.2.6", "@radix-ui/react-tabs": "1.1.13", "@radix-ui/react-toast": "1.2.15", "@radix-ui/react-toggle": "1.1.10", "@radix-ui/react-toggle-group": "1.1.11", "@radix-ui/react-toolbar": "1.1.11", "@radix-ui/react-tooltip": "1.2.8", "@radix-ui/react-use-callback-ref": "1.1.1", "@radix-ui/react-use-controllable-state": "1.2.2", "@radix-ui/react-use-effect-event": "0.0.2", "@radix-ui/react-use-escape-keydown": "1.1.1", "@radix-ui/react-use-is-hydrated": "0.1.0", "@radix-ui/react-use-layout-effect": "1.1.1", "@radix-ui/react-use-size": "1.1.1", "@radix-ui/react-visually-hidden": "1.2.3" }, "peerDependencies": { "@types/react": "*", "@types/react-dom": "*", "react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc", "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc" } }, "sha512-aWizCQiyeAenIdUbqEpXgRA1ya65P13NKn/W8rWkcN0OPkRDxdBVLWnIEDsS2RpwCK2nobI7oMUSmexzTDyAmA=="],
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:183:# Surfaces the `webapp` tool (start/status/logs/restart); always on.
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:366:            logger.info("Created opencode secret %s", secret_name)
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:422:            logger.info("Deleted opencode auth secret %s", secret_name)
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1636:            logger.info("No opencode history snapshot found for sandbox %s", sandbox_id)
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:1666:            logger.info("Restored opencode history snapshot for sandbox %s", sandbox_id)
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:2101:                logger.error("Failed to decode base64 content: %s", e)
HEAD:backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py:2265:            logger.warning("Failed to ensure AGENTS.md attachments section: %s", e)
HEAD:backend/onyx/server/features/build/sandbox/opencode/event_bus.py:145:                logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/event_bus.py:188:                    logger.info(
HEAD:backend/onyx/server/features/build/sandbox/opencode/event_bus.py:203:                    logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/event_bus.py:217:                    logger.error(
HEAD:backend/onyx/server/features/build/sandbox/opencode/event_bus.py:233:        logger.info("PodEventBus reader exiting (stop signaled)")
HEAD:backend/onyx/server/features/build/sandbox/opencode/event_bus.py:252:            logger.info(
HEAD:backend/onyx/server/features/build/sandbox/opencode/event_bus.py:279:            logger.warning("PodEventBus reload_auth failed after 401: %s", e)
HEAD:backend/onyx/server/features/build/sandbox/opencode/event_bus.py:284:        logger.info("PodEventBus reloaded auth after 401 on %s/event", self._base_url)
HEAD:backend/onyx/server/features/build/sandbox/opencode/event_bus.py:310:                            logger.info(
HEAD:backend/onyx/server/features/build/sandbox/opencode/event_bus.py:361:                    logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:332:        logger.warning("hydrate(%s): empty/failed fetch", msg_id)
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:337:        logger.warning("hydrate(%s): no info object", msg_id)
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:341:    logger.info(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:824:        logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1088:                logger.info(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1122:        logger.info(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1172:                logger.info(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1179:                logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1188:            logger.info(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1212:        logger.info(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1233:            logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1242:        logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1289:            logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1307:            logger.warning("get_message(%s) network error: %s", message_id, e)
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1310:            logger.warning("get_message(%s) -> HTTP %s", message_id, r.status_code)
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1681:            logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1692:        logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1719:            logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1728:            logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1751:            logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1765:            logger.warning(
HEAD:backend/onyx/server/features/build/sandbox/opencode/serve_client.py:1801:            logger.exception(
HEAD:backend/onyx/server/features/build/sandbox/util/agent_instructions.py:128:        logger.warning("AGENTS.template.md not found at %s", template_path)
HEAD:backend/onyx/server/features/build/sandbox/util/mcp_config.py:58:            logger.info(
HEAD:backend/onyx/server/features/build/sandbox/util/opencode_config.py:6:catalog + default model AND the craft MCP servers, both of which opencode
HEAD:backend/onyx/server/features/build/session/streaming.py:976:        logger.exception("Error in subagent message streaming")
HEAD:backend/onyx/server/features/mcp/api.py:480:        logger.info(
HEAD:backend/onyx/server/features/mcp/api.py:616:        logger.error("Failed to test MCP server credentials: %s", e)
HEAD:backend/onyx/server/features/mcp/api.py:649:    logger.info("Initiating per-user OAuth for server: %s", request.server_id)
HEAD:backend/onyx/server/features/mcp/api.py:866:        logger.error("OAuth initialization failed: %s", saved_e)
HEAD:backend/onyx/server/features/mcp/api.py:912:    logger.info(
HEAD:backend/onyx/server/features/mcp/api.py:982:    logger.info(
HEAD:backend/onyx/server/features/mcp/api.py:1147:    logger.warning(
HEAD:backend/onyx/server/features/mcp/api.py:1326:    logger.info("Fetching MCP servers for assistant: %s", assistant_id)
HEAD:backend/onyx/server/features/mcp/api.py:1343:        logger.error("Failed to fetch MCP servers: %s", e)
HEAD:backend/onyx/server/features/mcp/api.py:1464:            logger.error("Failed to discover tools for MCP server: %s", e)
HEAD:backend/onyx/server/features/mcp/api.py:1572:    logger.info("Listing tools for MCP server: %s", server_id)
HEAD:backend/onyx/server/features/mcp/api.py:1610:    logger.info("Discovering tools for MCP server: %s: %s", mcp_server.name, t1)
HEAD:backend/onyx/server/features/mcp/api.py:1628:    logger.info(
HEAD:backend/onyx/server/features/mcp/api.py:1995:        logger.info(
HEAD:backend/onyx/server/features/mcp/api.py:2034:        logger.info(
HEAD:backend/onyx/server/features/mcp/api.py:2248:    logger.info("Updating MCP server %s status to %s", server_id, status)
HEAD:backend/onyx/server/features/mcp/api.py:2264:    logger.info("Successfully updated MCP server %s status to %s", server_id, status)
HEAD:backend/onyx/server/features/mcp/api.py:2277:    logger.info("Fetching all MCP servers for admin display")
HEAD:backend/onyx/server/features/mcp/api.py:2315:        logger.error("Failed to fetch MCP servers for admin: %s:%s", type(e), e)
HEAD:backend/onyx/server/features/mcp/api.py:2328:    logger.info("Getting database tools for MCP server: %s", server_id)
HEAD:backend/onyx/server/features/mcp/api.py:2396:        logger.info(
HEAD:backend/onyx/server/features/mcp/api.py:2432:        logger.warning("Rejected MCP server upsert: %s", e)
HEAD:backend/onyx/server/features/mcp/api.py:2435:        logger.exception("Failed to create/update MCP tool")
HEAD:backend/onyx/server/features/mcp/api.py:2674:        # Log tools that will be deleted for debugging
HEAD:backend/onyx/server/features/mcp/api.py:2676:        logger.info(
HEAD:backend/onyx/server/features/mcp/api.py:2683:            logger.debug("  - Tool to delete: %s (ID: %s)", tool.name, tool.id)
HEAD:backend/onyx/server/features/mcp/api.py:2691:            logger.error(
HEAD:backend/onyx/server/features/mcp/api.py:2698:                logger.info(
HEAD:backend/onyx/server/features/mcp/api.py:2712:        logger.error("Failed to delete MCP server %s: %s", server_id, e)
HEAD:backend/onyx/server/features/mcp/client.py:173:    logger.error(e)
HEAD:backend/onyx/server/features/mcp/client.py:179:            logger.error(err)
HEAD:backend/onyx/server/features/mcp/client.py:199:        logger.error("Failed to call MCP client function: %s", e)
HEAD:backend/onyx/server/features/mcp/client.py:294:    logger.info("Initialized with server: %s", init_result.serverInfo)
HEAD:backend/onyx/server/features/mcp/client.py:295:    logger.info("Initialized with server time: %s", time.time() - t1)
HEAD:backend/onyx/server/features/mcp/client.py:299:    logger.info("Listed tools with server time: %s", time.time() - t2)
HEAD:backend/onyx/server/features/mcp/credentials.py:194:            logger.warning(
HEAD:backend/onyx/server/features/mcp/oauth.py:94:class MCPRefreshLogContext(TypedDict):
HEAD:backend/onyx/server/features/mcp/oauth.py:119:) -> MCPRefreshLogContext:
HEAD:backend/onyx/server/features/mcp/oauth.py:235:        logger.info("mcp_token_refresh.superseded config_id=%s", connection_config_id)
HEAD:backend/onyx/server/features/mcp/oauth.py:240:        logger.info(
HEAD:backend/onyx/server/features/mcp/oauth.py:285:        refresh_log_context: MCPRefreshLogContext | None = None,
HEAD:backend/onyx/server/features/mcp/oauth.py:471:            logger.info(
HEAD:backend/onyx/server/features/mcp/oauth.py:677:        refresh_log_context: MCPRefreshLogContext,
HEAD:backend/onyx/server/features/mcp/oauth.py:848:                f"'{self.refresh_log_context['mcp_server_name']}' "
HEAD:backend/onyx/server/features/mcp/oauth.py:853:        logger.info(
HEAD:backend/onyx/server/features/mcp/oauth.py:855:            self.refresh_log_context["mcp_server_name"],
HEAD:backend/onyx/server/features/mcp/oauth.py:883:        logger.info(
HEAD:backend/onyx/server/features/mcp/oauth.py:931:            logger.warning("mcp_oauth.refresh.failed", extra=response_fields)
HEAD:backend/onyx/server/features/mcp/oauth.py:939:                    logger.warning("mcp_oauth.tokens_discarded", extra=response_fields)
HEAD:backend/onyx/server/features/mcp/oauth.py:941:                    logger.info(
HEAD:backend/onyx/server/features/mcp/oauth.py:949:            logger.warning("mcp_oauth.refresh.invalid_response", extra=response_fields)
HEAD:backend/onyx/server/features/mcp/oauth.py:961:            logger.info(
HEAD:backend/onyx/server/features/mcp/oauth.py:968:        logger.info(
HEAD:backend/onyx/server/features/mcp/oauth.py:990:    refresh_log_context = _refresh_log_context(mcp_server, connection_config_id)
HEAD:backend/onyx/server/features/mcp/oauth_flow.py:353:                logger.info(
HEAD:backend/onyx/server/features/mcp/oauth_flow.py:422:            logger.info(
HEAD:backend/onyx/server/features/persona/api.py:236:        logger.exception("Failed to update agent display priorities.")
HEAD:backend/onyx/server/features/tool/api.py:378:    # Attach catalog: omit MCP tools the user cannot put on a persona.
HEAD:backend/onyx/server/manage/llm/api.py:132:    AuditAction,
HEAD:backend/onyx/server/manage/llm/api.py:713:            AuditAction.LLM_PROVIDER_CREATE
HEAD:backend/onyx/server/manage/llm/api.py:715:            else AuditAction.LLM_PROVIDER_UPDATE,
HEAD:backend/onyx/server/manage/llm/api.py:758:        AuditAction.LLM_PROVIDER_DELETE,
HEAD:backend/onyx/server/manage/search_settings.py:83:    AuditAction,
HEAD:backend/onyx/server/manage/search_settings.py:690:        AuditAction.CONTEXTUAL_RAG_MODEL_UPDATE,
HEAD:backend/onyx/server/manage/users.py:136:    AuditAction,
HEAD:backend/onyx/server/manage/users.py:182:        AuditAction.USER_ROLE_CHANGE,
HEAD:backend/onyx/server/manage/users.py:224:        AuditAction.USER_CRAFT_ACCESS_CHANGE,
HEAD:backend/onyx/server/manage/users.py:720:            AuditAction.USER_CREATE,
HEAD:backend/onyx/server/manage/users.py:792:        AuditAction.USER_DEACTIVATE,
HEAD:backend/onyx/server/manage/users.py:844:            AuditAction.USER_DELETE,
HEAD:backend/onyx/server/manage/users.py:888:        AuditAction.USER_REACTIVATE,
HEAD:backend/onyx/server/manage/users.py:1018:        logger.error("Failed to decode JWT for iat claim")
HEAD:backend/onyx/server/metrics/mcp_client.py:40:        logger.debug("Failed to record MCP client tool metrics", exc_info=True)
HEAD:backend/onyx/server/metrics/mcp_server.py:60:        logger.debug("Failed to record MCP auth metric", exc_info=True)
HEAD:backend/onyx/server/metrics/mcp_server.py:77:        logger.debug("Failed to record MCP server tool metrics", exc_info=True)
HEAD:backend/onyx/server/metrics/mcp_server.py:87:        logger.debug("Failed to record MCP search result metric", exc_info=True)
HEAD:backend/onyx/server/metrics/mcp_server.py:94:        logger.debug("Failed to record MCP search source metric", exc_info=True)
HEAD:backend/onyx/server/query_and_chat/session_loading.py:796:                    logger.warning("Error processing tool call %s: %s", tool_call.id, e)
HEAD:backend/onyx/server/security/store.py:34:from onyx.utils.audit import AuditAction, AuditActor, AuditOutcome, emit_audit_event
HEAD:backend/onyx/server/security/store.py:321:        AuditAction.SECURITY_SETTINGS_CHANGE,
HEAD:backend/onyx/server/settings/api.py:49:    AuditAction,
HEAD:backend/onyx/server/settings/api.py:131:                AuditAction.CRAFT_DEFAULT_CHANGE,
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:13:> **Onyx Craft:** for basic reads of static pages, prefer the `webfetch` tool — it returns clean markdown, is faster, and is cheaper. Reach for `browser` only when the page needs JavaScript/SPA rendering, interaction (clicks, forms, login), multi-step navigation, or visual inspection.
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:1362:- `devtools.timeline` -- standard DevTools performance traces
HEAD:backend/onyx/skills/builtin/browser/SKILL.md:2078:The hook in particular exposes `window.__REACT_DEVTOOLS_GLOBAL_HOOK__` to every page in the browsing context, including third-party iframes. For production-auditing tasks against sites that handle secrets, consider whether you want that global exposed during the session.
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:113:        logger.info("Created coding agent session %s", session_id)
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:132:            logger.info("Extracted repo into session %s", session_id)
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:137:                logger.info("Deleted coding agent session %s", session_id)
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:141:                logger.warning(
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:153:        logger.warning(
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:161:    logger.info(
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:173:    logger.info(
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:310:                        logger.info(
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:399:                        logger.warning(
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:449:                        logger.warning(
HEAD:backend/onyx/tools/fake_tools/coding_agent.py:513:            logger.exception("Error running coding agent call: %s", e)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:278:                    logger.info(
HEAD:backend/onyx/tools/fake_tools/research_agent.py:287:                    logger.debug("Auto-generating intermediate report on last cycle.")
HEAD:backend/onyx/tools/fake_tools/research_agent.py:638:            logger.error("Error running research agent call: %s", e)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:662:    logger.warning(
HEAD:backend/onyx/tools/fake_tools/research_agent.py:796:        logger.info("Running research agent with prompt: %s", RESEARCH_PROMPT)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:797:        logger.info("LLM: %s/%s", llm.config.model_provider, llm.config.model_name)
HEAD:backend/onyx/tools/fake_tools/research_agent.py:798:        logger.info("Tools: %s", [t.name for t in tools])
HEAD:backend/onyx/tools/fake_tools/research_agent.py:819:            logger.error("Research agent returned no result")
HEAD:backend/onyx/tools/tool_constructor.py:192:    # Log which tools are attached to the persona for debugging
HEAD:backend/onyx/tools/tool_constructor.py:194:    logger.debug(
HEAD:backend/onyx/tools/tool_constructor.py:257:                logger.exception(
HEAD:backend/onyx/tools/tool_constructor.py:263:                logger.debug(
HEAD:backend/onyx/tools/tool_constructor.py:314:                    logger.error("Failed to initialize Internet Search Tool: %s", e)
HEAD:backend/onyx/tools/tool_constructor.py:324:                    logger.debug(
HEAD:backend/onyx/tools/tool_constructor.py:340:                    logger.error("Failed to initialize Open URL Tool: %s", e)
HEAD:backend/onyx/tools/tool_constructor.py:380:            #         logger.debug("Knowledge Graph Tool is not enabled/exposed")
HEAD:backend/onyx/tools/tool_constructor.py:403:                    logger.warning(
HEAD:backend/onyx/tools/tool_constructor.py:414:                        logger.warning(
HEAD:backend/onyx/tools/tool_constructor.py:423:                    logger.warning(
HEAD:backend/onyx/tools/tool_constructor.py:465:                logger.warning(str(e))
HEAD:backend/onyx/tools/tool_constructor.py:502:                logger.warning(
HEAD:backend/onyx/tools/tool_constructor.py:535:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:166:                logger.debug("Executing bash in session %s: %s", self._session_id, cmd)
HEAD:backend/onyx/tools/tool_implementations/bash/bash_tool.py:173:            logger.error("Bash execution failed: %s", e)
HEAD:backend/onyx/tools/tool_implementations/coding_agent/coding_agent_tool.py:182:            logger.warning("Coding agent run returned None for query: %s", query)
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:79:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:207:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:238:                logger.exception(
HEAD:backend/onyx/tools/tool_implementations/custom/custom_tool.py:245:        logger.info(
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:157:        logger.debug("Generating image with model: %s, size: %s", self.model, size)
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:174:            logger.error("Error fetching or converting image: %s", e)
HEAD:backend/onyx/tools/tool_implementations/images/image_generation_tool.py:179:            logger.debug("Error occurred during image generation: %s", e)
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:163:                logger.warning(
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:190:                logger.warning(
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:239:                        logger.exception(
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:259:            logger.info("MCP tool '%s' executed successfully", self._name)
HEAD:backend/onyx/tools/tool_implementations/mcp/mcp_tool.py:290:            logger.error("Failed to execute MCP tool '%s': %s", self._name, e)
HEAD:backend/onyx/tools/tool_implementations/memory/memory_tool.py:139:            logger.info("New memory to be added: %s", memory_text)
HEAD:backend/onyx/tools/tool_implementations/open_url/firecrawl.py:160:            logger.warning("Firecrawl returned empty content for url=%s", url)
HEAD:backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py:141:        logger.warning(
HEAD:backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py:219:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py:235:            logger.error(
HEAD:backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py:242:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py:266:                logger.info(
HEAD:backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py:280:            logger.warning("Onyx crawler received %s for %s", response.status_code, url)
HEAD:backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py:296:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py:311:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py:323:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py:366:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py:379:            logger.info(
HEAD:backend/onyx/tools/tool_implementations/open_url/onyx_web_crawler.py:389:        logger.info("Playwright fallback succeeded for %s", url)
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:548:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:716:            logger.warning("OpenURL tool failed: %s", failure_msg)
HEAD:backend/onyx/tools/tool_implementations/open_url/open_url_tool.py:830:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/open_url/tavily.py:121:            logger.warning("Tavily extract failed for url=%s: %s", url, error)
HEAD:backend/onyx/tools/tool_implementations/open_url/url_normalization.py:56:            logger.debug(
HEAD:backend/onyx/tools/tool_implementations/open_url/url_normalization.py:96:            logger.debug(
HEAD:backend/onyx/tools/tool_implementations/python/code_interpreter_client.py:285:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/python/code_interpreter_client.py:293:            logger.warning("Exception caught when checking health, e=%s", e)
HEAD:backend/onyx/tools/tool_implementations/python/code_interpreter_client.py:366:            logger.info(
HEAD:backend/onyx/tools/tool_implementations/python/code_interpreter_client.py:404:                        logger.warning("Unknown SSE event type: %s", event_type)
HEAD:backend/onyx/tools/tool_implementations/python/code_interpreter_client.py:413:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:168:                logger.warning(
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:332:                    logger.warning(
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:346:            logger.info("Staged file for Python execution: %s", plan.file_name)
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:408:                logger.warning(staging_notice)
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:411:                logger.debug("Executing code: %s", code)
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:503:                        logger.error(
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:514:                        logger.error(
HEAD:backend/onyx/tools/tool_implementations/python/python_tool.py:557:                logger.error("Python execution failed: %s", e)
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:259:    logger.debug(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:344:                logger.debug(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:363:                    logger.debug("Found Slack federated connector config: %s", entities)
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:367:                logger.debug(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:400:                logger.warning("Could not fetch Slack bot tokens: %s", e)
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:424:                logger.warning("Could not fetch Slack OAuth token: %s", e)
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:469:            logger.info("Slack federated search returned %s chunks", len(chunks))
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:473:            logger.error("Slack federated search error: %s", e, exc_info=True)
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:822:        logger.info(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:904:            logger.info(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:957:        logger.debug(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:1053:            logger.info("Search tool - no results found, returning empty response")
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:1117:        logger.debug(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:1160:                logger.warning(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:1189:        logger.debug(
HEAD:backend/onyx/tools/tool_implementations/search/search_tool.py:1213:        logger.debug(
HEAD:backend/onyx/tools/tool_implementations/search/search_utils.py:186:            logger.warning("Failed to retrieve chunks above section: %s", e)
HEAD:backend/onyx/tools/tool_implementations/search/search_utils.py:208:            logger.warning("Failed to retrieve chunks below section: %s", e)
HEAD:backend/onyx/tools/tool_implementations/search/search_utils.py:422:        logger.debug(
HEAD:backend/onyx/tools/tool_implementations/search/search_utils.py:430:        logger.debug(
HEAD:backend/onyx/tools/tool_implementations/search/search_utils.py:438:        logger.debug(
HEAD:backend/onyx/tools/tool_implementations/search/search_utils.py:458:            logger.debug(
HEAD:backend/onyx/tools/tool_implementations/search/search_utils.py:463:            logger.debug(
HEAD:backend/onyx/tools/tool_implementations/search/search_utils.py:479:            logger.warning(
HEAD:backend/onyx/tools/tool_implementations/search/search_utils.py:495:        logger.warning(
HEAD:backend/onyx/tools/tool_implementations/utils.py:17:        logger.debug("Truncated %s: %s", label, truncated)
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/brave_client.py:47:        logger.debug("Count of results passed to BraveClient: %s", num_results)
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/brave_client.py:178:        logger.info("Web search provider test succeeded for Brave.")
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/exa_client.py:192:        logger.info("Web search provider test succeeded for Exa.")
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/google_pse_client.py:107:                        logger.debug(
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/google_pse_client.py:158:        logger.info("Web search provider test succeeded for Google PSE.")
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/searxng_client.py:20:        logger.debug("Initializing SearXNGClient with base URL: %s", searxng_base_url)
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/searxng_client.py:30:        logger.debug(
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/searxng_client.py:55:            logger.debug("Testing connection to %s/config", self._searxng_base_url)
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/searxng_client.py:57:            logger.debug("Response: %s, text: %s", response.status_code, response.text)
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/searxng_client.py:61:            logger.debug(
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/searxng_client.py:103:        logger.info("Web search provider test succeeded for SearXNG.")
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/serper_client.py:103:        logger.info("Web search provider test succeeded for Serper.")
HEAD:backend/onyx/tools/tool_implementations/web_search/clients/tavily_client.py:163:        logger.info("Web search provider test succeeded for Tavily.")
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:197:            logger.warning("Web search query '%s' failed: %s", query, error_msg)
HEAD:backend/onyx/tools/tool_implementations/web_search/web_search_tool.py:262:            logger.warning(
HEAD:backend/onyx/tools/tool_runner.py:150:            logger.error("Tool call error for %s: %s", tool.name, e)
HEAD:backend/onyx/tools/tool_runner.py:173:            logger.error("Unexpected error running tool %s: %s", tool.name, e)
HEAD:backend/onyx/tools/tool_runner.py:200:            logger.error("Unexpected error running tool %s: %s", tool.name, e)
HEAD:backend/onyx/tools/tool_runner.py:308:            logger.warning("Tool %s not found in tools list", tool_call.tool_name)
HEAD:backend/onyx/tracing/braintrust_tracing_processor.py:220:        # Include the full tool catalog (name, description, parameters) offered
HEAD:backend/onyx/tracing/framework/spans.py:34:    A span represents a single operation within a trace (e.g., an LLM call, tool execution,
HEAD:backend/onyx/utils/audit.py:53:class AuditAction(str, Enum):
HEAD:backend/onyx/utils/audit.py:54:    """Audited-action taxonomy. Values are an append-only schema contract
HEAD:backend/onyx/utils/audit.py:111:_OCSF_CLASS_BY_ACTION: dict[AuditAction, OCSFEventClass] = {
HEAD:backend/onyx/utils/audit.py:112:    AuditAction.LOGIN: OCSFEventClass.AUTHENTICATION,
HEAD:backend/onyx/utils/audit.py:113:    AuditAction.LOGIN_FAILURE: OCSFEventClass.AUTHENTICATION,
HEAD:backend/onyx/utils/audit.py:114:    AuditAction.LOGOUT: OCSFEventClass.AUTHENTICATION,
HEAD:backend/onyx/utils/audit.py:115:    AuditAction.REGISTER: OCSFEventClass.AUTHENTICATION,
HEAD:backend/onyx/utils/audit.py:116:    AuditAction.PASSWORD_FORGOT: OCSFEventClass.AUTHENTICATION,
HEAD:backend/onyx/utils/audit.py:117:    AuditAction.PASSWORD_RESET: OCSFEventClass.AUTHENTICATION,
HEAD:backend/onyx/utils/audit.py:118:    AuditAction.EMAIL_VERIFY: OCSFEventClass.AUTHENTICATION,
HEAD:backend/onyx/utils/audit.py:119:    AuditAction.IMPERSONATE: OCSFEventClass.AUTHENTICATION,
HEAD:backend/onyx/utils/audit.py:120:    AuditAction.USER_CREATE: OCSFEventClass.ACCOUNT_CHANGE,
HEAD:backend/onyx/utils/audit.py:121:    AuditAction.USER_DELETE: OCSFEventClass.ACCOUNT_CHANGE,
HEAD:backend/onyx/utils/audit.py:122:    AuditAction.USER_DEACTIVATE: OCSFEventClass.ACCOUNT_CHANGE,
HEAD:backend/onyx/utils/audit.py:123:    AuditAction.USER_REACTIVATE: OCSFEventClass.ACCOUNT_CHANGE,
HEAD:backend/onyx/utils/audit.py:124:    AuditAction.USER_ROLE_CHANGE: OCSFEventClass.USER_ACCESS_MANAGEMENT,
HEAD:backend/onyx/utils/audit.py:125:    AuditAction.USER_CRAFT_ACCESS_CHANGE: OCSFEventClass.USER_ACCESS_MANAGEMENT,
HEAD:backend/onyx/utils/audit.py:126:    AuditAction.USER_GROUP_CHANGE: OCSFEventClass.GROUP_MANAGEMENT,
HEAD:backend/onyx/utils/audit.py:127:    AuditAction.USER_GROUP_CREATE: OCSFEventClass.GROUP_MANAGEMENT,
HEAD:backend/onyx/utils/audit.py:128:    AuditAction.USER_GROUP_RENAME: OCSFEventClass.GROUP_MANAGEMENT,
HEAD:backend/onyx/utils/audit.py:129:    AuditAction.USER_GROUP_DELETE: OCSFEventClass.GROUP_MANAGEMENT,
HEAD:backend/onyx/utils/audit.py:130:    AuditAction.USER_GROUP_PERMISSION_CHANGE: OCSFEventClass.GROUP_MANAGEMENT,
HEAD:backend/onyx/utils/audit.py:131:    AuditAction.USER_GROUP_MANAGER_CHANGE: OCSFEventClass.GROUP_MANAGEMENT,
HEAD:backend/onyx/utils/audit.py:132:    AuditAction.CRAFT_DEFAULT_CHANGE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:133:    AuditAction.SECURITY_SETTINGS_CHANGE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:134:    AuditAction.CONTEXTUAL_RAG_MODEL_UPDATE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:135:    AuditAction.LLM_PROVIDER_CREATE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:136:    AuditAction.LLM_PROVIDER_UPDATE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:137:    AuditAction.LLM_PROVIDER_DELETE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:138:    AuditAction.CONNECTOR_CREATE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:139:    AuditAction.CONNECTOR_UPDATE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:140:    AuditAction.CONNECTOR_DELETE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:141:    AuditAction.CC_PAIR_CREATE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:142:    AuditAction.CC_PAIR_UPDATE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:143:    AuditAction.CC_PAIR_DELETE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:144:    AuditAction.API_KEY_CREATE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:145:    AuditAction.API_KEY_REGENERATE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:146:    AuditAction.API_KEY_UPDATE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:147:    AuditAction.API_KEY_DELETE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:148:    AuditAction.CREDENTIAL_CREATE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:149:    AuditAction.CREDENTIAL_UPDATE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:150:    AuditAction.CREDENTIAL_DELETE: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:151:    AuditAction.CREDENTIAL_ACCESS: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:154:    AuditAction.PERMISSION_DENIED: OCSFEventClass.API_ACTIVITY,
HEAD:backend/onyx/utils/audit.py:158:_unmapped = set(AuditAction) - set(_OCSF_CLASS_BY_ACTION)
HEAD:backend/onyx/utils/audit.py:161:        f"AuditAction members missing an OCSF class mapping: "
HEAD:backend/onyx/utils/audit.py:262:    action: AuditAction,
```
## Current Capability-Flow Model
```text
Stage | Static evidence status
------|-----------------------
Tool definitions/schemas | OBSERVED
Tool availability/registry | OBSERVED
Tool/agent authorization mechanisms | OBSERVED
LLM tool-call production/parsing | OBSERVED
Tool argument parsing/validation | OBSERVED
Tool execution dispatch | OBSERVED
Tool-result return to model | OBSERVED
Multi-step/agent-loop controls | OBSERVED
MCP configuration/access model | OBSERVED
MCP tool discovery | OBSERVED
MCP tool invocation | OBSERVED
MCP auth/token/header handling | OBSERVED
External-app credential boundary | OBSERVED
Code-interpreter/sandbox surface | OBSERVED
Execution resource/network/file controls | OBSERVED
Failure/timeout semantics | OBSERVED
Execution logging/audit signals | OBSERVED
Actual tool execution | NOT EXECUTED
Actual MCP connection | NOT EXECUTED
Actual code execution | NOT EXECUTED
Authorization correctness | NOT PROVEN
Argument safety | NOT PROVEN
Sandbox isolation | NOT PROVEN
Credential isolation | NOT PROVEN
Prompt-injection resistance | NOT PROVEN
```
## Provisional Evidence-Backed Flow
Static evidence supports the following general capability model:
1. tool definitions and schemas describe capabilities to application/model
   layers;
2. an availability/registry layer determines candidate tools;
3. model output can contain structured tool calls;
4. tool-call arguments are parsed and transformed;
5. application code dispatches tool execution;
6. credentials or caller context may cross the execution boundary;
7. execution returns structured or textual results;
8. tool results may become input to later LLM reasoning;
9. the cycle may repeat during multi-step agent behavior;
10. MCP provides an additional remote-capability discovery/execution surface;
11. code-interpreter functionality provides an executable-computation
    boundary.
## Security Decisions That Must Remain Separate
### Tool visibility
Can the model see that a capability exists?
### Tool authorization
May this user/persona/session invoke it?
### Argument authorization
Is this specific requested operation permitted?
### Credential authorization
Which identity or credential should execute the action?
### Execution isolation
What can the capability reach or modify?
### Result trust
Can returned data safely influence another model decision?
Passing one layer does not imply that later layers are secure.
## Critical Trust Boundaries
### Model output -> tool call
Probabilistic/untrusted model output becomes a structured capability request.
### Tool arguments -> executor
Model-generated parameters become deterministic inputs to application code.
### Application -> external service
Credentials, tenant identity and sensitive data may cross system boundaries.
### MCP server -> discovered tools
A remote capability catalog becomes part of the model's effective capability
set.
### MCP result -> model
Remote/untrusted output can influence subsequent reasoning and actions.
### Model/application -> code interpreter
Model or user-controlled content may become executable computation.
### Code interpreter -> filesystem/network
Execution isolation determines the blast radius of malicious or accidental
code.
## High-Value Future Security Tests
Later phases must verify:
- unauthorized tool discovery;
- unauthorized tool invocation;
- user-to-user capability isolation;
- tenant-to-tenant capability isolation;
- persona/agent sharing authorization;
- tool argument tampering;
- hidden parameter injection;
- indirect prompt injection causing tool execution;
- confused-deputy behavior;
- credential passthrough correctness;
- privilege amplification;
- MCP server ownership and sharing controls;
- MCP tool discovery poisoning;
- MCP token leakage;
- malicious MCP tool descriptions;
- malicious MCP results;
- tool-result prompt injection;
- excessive agent loops;
- replay/double execution;
- timeout handling;
- idempotency of state-changing tools;
- code-interpreter filesystem isolation;
- code-interpreter network isolation;
- resource exhaustion;
- secret exposure inside execution environments.
No vulnerability claim is made by Action 6.8.
## Interpretation Boundary
This action proves static mechanisms and candidate capability flow only.
It does not prove:
- active tool configuration;
- active MCP configuration;
- runtime authorization correctness;
- tool argument safety;
- effective credential scoping;
- MCP identity propagation;
- runtime sandbox isolation;
- runtime network restrictions;
- runtime filesystem restrictions;
- absence of prompt injection;
- absence of confused-deputy behavior;
- absence of arbitrary code execution outside intended boundaries.
## Safety Record
During Action 6.8:
- Onyx application execution: NO
- Docker execution: NO
- agent execution: NO
- tool invocation: NO
- MCP connection: NO
- MCP discovery request: NO
- credential use: NO
- external-service call: NO
- code execution: NO
- sandbox started: NO
- network probing: NO
- production/customer data: NO
- vulnerability exploitation: NO
- Onyx source modification: NO
## Result
Action 6.8 agent, tool, MCP and code-execution flow trace: **PASS**.
