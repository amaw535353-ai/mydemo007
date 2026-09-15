# Phase 5 Action 5.9 - Tools & Function Calling Foundations Evidence

## Provenance
- Branch: `security/phase-5-ai-foundations`
- Baseline HEAD: `85cb25773003a9a066a28be00d7742089dfde690`

## Observation boundary

**STATIC SOURCE CANDIDATES ONLY. AGENT/TOOL/MCP RUNTIME BEHAVIOR IS UNVERIFIED.**

## Review scope

Tool/function schemas, selection, arguments, dispatch, execution, side effects, authorization, approval, command/code execution and tool-result trust boundaries.

## Static observations
- Candidate files: **333**
- Matching lines: **3208**

## Representative candidate files

- `backend/alembic/run_multitenant_migrations.py`
- `backend/alembic/versions/33cb72ea4d80_single_tool_call_per_message.py`
- `backend/alembic/versions/35e518e0ddf4_properly_cascade.py`
- `backend/alembic/versions/48d14957fe80_add_support_for_custom_tools.py`
- `backend/alembic/versions/4cebcbc9b2ae_add_tab_index_to_tool_call.py`
- `backend/alembic/versions/a852cbe15577_new_chat_history.py`
- `backend/alembic/versions/d25168c2beee_tool_name_consistency.py`
- `backend/alembic/versions/f3c9e59c3b07_seed_coding_agent_tool.py`
- `backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py`
- `backend/ee/onyx/external_permissions/confluence/group_sync.py`
- `backend/ee/onyx/external_permissions/google_drive/folder_retrieval.py`
- `backend/ee/onyx/external_permissions/google_drive/group_sync.py`
- `backend/ee/onyx/external_permissions/google_drive/permission_retrieval.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/ee/onyx/server/gateway/api.py`
- `backend/ee/onyx/server/gateway/openai_passthrough.py`
- `backend/ee/onyx/server/gateway/stream_bridge.py`
- `backend/model_server/legacy/onyx_torch_model.py`
- `backend/model_server/main.py`
- `backend/onyx/access/access.py`

## Security questions
- Is authorization enforced outside the model before tool execution?
- Can the model select privileged tools directly?
- Are tool arguments schema-validated?
- Are user or retrieved inputs passed into dangerous arguments?
- Which tools cause irreversible or external side effects?
- Which tools require confirmation or step-up authorization?
- Are filesystem, network and shell capabilities minimized?
- Can tool output contain instructions that influence later decisions?
- Are tool calls bounded, logged and attributable to a user/session?

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

Action 5.9 static foundation result: **PASS**
