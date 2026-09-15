# Phase 5 Action 5.10 - MCP Foundations Evidence

## Provenance
- Branch: `security/phase-5-ai-foundations`
- Baseline HEAD: `40c7e6a70b0d7e6dfb493a5f24e54b235308fc8e`

## Observation boundary

**STATIC SOURCE CANDIDATES ONLY. AGENT/TOOL/MCP RUNTIME BEHAVIOR IS UNVERIFIED.**

## Review scope

Model Context Protocol clients, servers, transports, tools, resources, prompts, discovery, capability negotiation, configuration, authentication and MCP trust boundaries.

## Static observations
- Candidate files: **374**
- Matching lines: **2234**

## Representative candidate files

- `backend/alembic/versions/2a391f840e85_add_last_refreshed_at_mcp_server.py`
- `backend/alembic/versions/3a9b8d7c6e5f_add_mcp_known_provider_fields.py`
- `backend/alembic/versions/565c5b57a573_add_available_in_craft_to_mcp_server.py`
- `backend/alembic/versions/7ed603b64d5a_add_mcp_server_and_connection_config_.py`
- `backend/alembic/versions/96a5702df6aa_mcp_tool_enabled.py`
- `backend/alembic/versions/b30353be4eec_add_mcp_auth_performer.py`
- `backend/alembic/versions/b7e9a3c1d2f4_add_is_public_to_mcp_server.py`
- `backend/alembic/versions/bc9e56f2fb96_polymorphic_gated_app.py`
- `backend/alembic/versions/c9e2cd766c29_add_s3_file_store_table.py`
- `backend/alembic/versions/e8f0d2a38171_add_status_to_mcp_server_and_make_auth_.py`
- `backend/alembic/versions/fe958f19e42b_add_mcp_config_hash_to_sandbox_and_.py`
- `backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py`
- `backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py`
- `backend/ee/onyx/db/mcp.py`
- `backend/ee/onyx/db/user_group.py`
- `backend/ee/onyx/external_permissions/confluence/group_sync.py`
- `backend/ee/onyx/external_permissions/sharepoint/group_sync.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/ee/onyx/server/middleware/tenant_tracking.py`
- `backend/onyx/auth/disposable_email_validator.py`

## Security questions
- Which MCP servers may the application connect to?
- Who controls MCP server configuration?
- How is server identity authenticated or pinned?
- Which tools, resources and prompts can a server expose?
- Can server capabilities change after initial approval?
- Are MCP tool calls authorized independently of model intent?
- Can an untrusted MCP response inject instructions into the model?
- Can one MCP server influence calls to another server?
- Are credentials scoped per server and least privilege?
- Are local stdio servers treated as code-execution trust boundaries?
- Are network MCP transports restricted to approved destinations?
- Is MCP activity attributable, logged and bounded?

## Security interpretation

Static matches identify trust boundaries and review targets.

They do not prove authorization, safe tool execution, agent containment, MCP trust or runtime enforcement.

## Safety
- No agent executed.
- No tool/function invoked.
- No shell/code execution triggered.
- No MCP client connected.
- No MCP server contacted.
- No external AI API contacted.
- No real credential used.
- No real customer data used.
- No paid service used.

## Result

Action 5.10 static foundation result: **PASS**
