# Phase 6 Action 6.3 - Major Component and Responsibility Mapping
## Purpose
Move from repository-topology reconnaissance to evidence-backed identification
of major Onyx application components.
This action uses source code, Docker Compose definitions, build files, package
metadata and documentation from the exact pinned Onyx revision.
No component was executed.
## Verified baseline
- Evidence branch: `security/phase-6-onyx-baseline`
- Action 6.2 parent: `837879ac1c02c38216ead47810dfe2fafcc69b4c`
- Onyx repository: `https://github.com/onyx-dot-app/onyx.git`
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx working tree clean: PASS
## Method
Component conclusions in this document use three confidence levels:
1. **Observed** - directly present in source/configuration.
2. **Provisional responsibility** - responsibility strongly suggested by
   source names/configuration but not yet runtime verified.
3. **Unverified relationship** - requires deeper source tracing or runtime
   observation before being treated as architecture fact.
## Deployment Service Inventory
### Standard Compose
Observed services: 11
```text
api_server
background
web_server
inference_model_server
indexing_model_server
relational_db
opensearch
nginx
cache
minio
code-interpreter
```
### Onyx Lite Compose
Observed services: 7
```text
api_server
background
cache
indexing_model_server
inference_model_server
opensearch
minio
```
### Standard-only Service Names
```text
code-interpreter
nginx
relational_db
web_server
```
### Lite-only Service Names
```text

```
## Provisional Component Classification
This table is derived only from observed deployment service names.
It is **not yet a runtime-verified architecture**.
```text
Observed service | Provisional class
-----------------|------------------
api_server | backend API candidate
background | asynchronous worker candidate
cache | cache / queue-broker candidate
code-interpreter | unclassified; requires source trace
indexing_model_server | indexing/embedding model service candidate
inference_model_server | model inference service candidate
minio | unclassified; requires source trace
nginx | reverse-proxy / ingress candidate
opensearch | search/index candidate
relational_db | relational persistence candidate
web_server | web/UI service candidate
```
## Standard Deployment Configuration Evidence
Bounded extraction of service declarations and configuration keys.
```text
47:  api_server:
48:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
49:    build:
55:    command: >
63:    depends_on:
129:  background:
130:    image: ${ONYX_BACKEND_IMAGE:-onyxdotapp/onyx-backend:${IMAGE_TAG:-latest}}
131:    build:
137:    command: >
146:    depends_on:
201:  web_server:
202:    image: ${ONYX_WEB_SERVER_IMAGE:-onyxdotapp/onyx-web-server:${IMAGE_TAG:-latest}}
203:    build:
217:    depends_on:
281:  inference_model_server:
282:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
283:    build:
324:  indexing_model_server:
325:    image: ${ONYX_MODEL_SERVER_IMAGE:-onyxdotapp/onyx-model-server:${IMAGE_TAG:-latest}}
326:    build:
369:  relational_db:
370:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/postgres:15.2-alpine
372:    command: -c 'max_connections=250'
399:  opensearch:
400:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/opensearchproject/opensearch:3.6.0
438:  nginx:
439:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/nginx:1.25.5-alpine
443:    depends_on:
457:    ports:
477:    command: >
498:  cache:
499:    image: ${BASE_IMAGE_REGISTRY:-docker.io}/library/redis:7.4-alpine
508:    command: redis-server --save "" --appendonly no
516:  minio:
521:    image: quay.io/minio/minio:RELEASE.2025-09-07T16-13-09Z-cpuv1@sha256:13582eff79c6605a2d315bdd0e70164142ea7e98fc8411e9e10d089502a6d883
522:    profiles: ["s3-filestore"]
540:    command: server /data --console-address ":9001"
547:  code-interpreter:
551:    image: onyxdotapp/code-interpreter:${CODE_INTERPRETER_IMAGE_TAG:-0.4.7}
552:    command: ["bash", "./entrypoint.sh", "code-interpreter-api"]
602:  db_volume:
603:  minio_data:
605:  model_cache_huggingface:
606:  indexing_huggingface_model_cache:
608:  api_server_logs:
609:  background_logs:
611:  inference_model_server_logs:
612:  indexing_model_server_logs:
614:  file-system:
616:  opensearch-data:
```
## Lite Deployment Configuration Evidence
```text
37:  api_server:
38:    depends_on:
59:  background:
60:    profiles: ["background"]
61:    depends_on:
71:  cache:
72:    profiles: ["redis"]
75:  indexing_model_server:
76:    profiles: ["vectordb"]
79:  inference_model_server:
80:    profiles: ["inference"]
83:  opensearch:
84:    profiles: ["opensearch"]
87:  minio:
88:    profiles: ["s3-filestore"]
```
## Backend API Evidence
Source matches captured: 250
```text
HEAD:backend/ee/onyx/main.py:55:    include_router_with_global_prefix_prepended,
HEAD:backend/ee/onyx/main.py:133:    include_router_with_global_prefix_prepended(application, user_group_router)
HEAD:backend/ee/onyx/main.py:135:    include_router_with_global_prefix_prepended(application, analytics_router)
HEAD:backend/ee/onyx/main.py:136:    include_router_with_global_prefix_prepended(application, query_history_router)
HEAD:backend/ee/onyx/main.py:138:    include_router_with_global_prefix_prepended(application, query_router)
HEAD:backend/ee/onyx/main.py:139:    include_router_with_global_prefix_prepended(application, ee_query_router)
HEAD:backend/ee/onyx/main.py:140:    include_router_with_global_prefix_prepended(application, search_router)
HEAD:backend/ee/onyx/main.py:141:    include_router_with_global_prefix_prepended(application, standard_answer_router)
HEAD:backend/ee/onyx/main.py:142:    include_router_with_global_prefix_prepended(application, ee_oauth_router)
HEAD:backend/ee/onyx/main.py:143:    include_router_with_global_prefix_prepended(application, ee_document_cc_pair_router)
HEAD:backend/ee/onyx/main.py:144:    include_router_with_global_prefix_prepended(application, evals_router)
HEAD:backend/ee/onyx/main.py:145:    include_router_with_global_prefix_prepended(application, hook_router)
HEAD:backend/ee/onyx/main.py:146:    include_router_with_global_prefix_prepended(application, llm_gateway_router)
HEAD:backend/ee/onyx/main.py:149:    include_router_with_global_prefix_prepended(
HEAD:backend/ee/onyx/main.py:153:    include_router_with_global_prefix_prepended(
HEAD:backend/ee/onyx/main.py:156:    include_router_with_global_prefix_prepended(application, enterprise_settings_router)
HEAD:backend/ee/onyx/main.py:157:    include_router_with_global_prefix_prepended(application, usage_export_router)
HEAD:backend/ee/onyx/main.py:159:    include_router_with_global_prefix_prepended(application, log_export_router)
HEAD:backend/ee/onyx/main.py:161:    include_router_with_global_prefix_prepended(application, license_router)
HEAD:backend/ee/onyx/main.py:165:    include_router_with_global_prefix_prepended(application, billing_router)
HEAD:backend/ee/onyx/main.py:169:        include_router_with_global_prefix_prepended(application, tenants_router)
HEAD:backend/ee/onyx/main.py:174:    application.include_router(scim_router)
HEAD:backend/ee/onyx/server/analytics/api.py:28:router = APIRouter(prefix="/analytics", tags=PUBLIC_API_TAGS)
HEAD:backend/ee/onyx/server/billing/api.py:79:router = APIRouter(prefix="/admin/billing")
HEAD:backend/ee/onyx/server/documents/cc_pair.py:29:router = APIRouter(prefix="/manage")
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:54:admin_router = APIRouter(prefix="/admin/enterprise-settings")
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:55:basic_router = APIRouter(prefix="/enterprise-settings")
HEAD:backend/ee/onyx/server/evals/api.py:13:router = APIRouter(prefix="/evals")
HEAD:backend/ee/onyx/server/features/hooks/api.py:190:router = APIRouter(prefix="/admin/hooks")
HEAD:backend/ee/onyx/server/gateway/api.py:133:router = APIRouter(prefix=GATEWAY_PATH_PREFIX)
HEAD:backend/ee/onyx/server/license/api.py:50:router = APIRouter(prefix="/license")
HEAD:backend/ee/onyx/server/log_export/api.py:46:router = APIRouter()
HEAD:backend/ee/onyx/server/manage/standard_answer.py:27:router = APIRouter(prefix="/manage")
HEAD:backend/ee/onyx/server/oauth/api_router.py:3:router: APIRouter = APIRouter(prefix="/oauth")
HEAD:backend/ee/onyx/server/query_and_chat/query_backend.py:19:basic_router = APIRouter(prefix="/query")
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:50:router = APIRouter(prefix="/search")
HEAD:backend/ee/onyx/server/query_history/api.py:56:router = APIRouter()
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:27:router = APIRouter()
HEAD:backend/ee/onyx/server/scim/api.py:153:scim_router = APIRouter(prefix="/scim/v2", tags=["SCIM"])
HEAD:backend/ee/onyx/server/scim/api.py:161:    Call this after ``app.include_router(scim_router)`` so that auth
HEAD:backend/ee/onyx/server/tenants/admin_api.py:23:router = APIRouter(prefix="/tenants")
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:25:router = APIRouter(prefix="/tenants")
HEAD:backend/ee/onyx/server/tenants/api.py:29:    router = APIRouter()
HEAD:backend/ee/onyx/server/tenants/api.py:30:    router.include_router(anonymous_users_router)
HEAD:backend/ee/onyx/server/tenants/api.py:31:    router.include_router(billing_router)
HEAD:backend/ee/onyx/server/tenants/api.py:32:    router.include_router(team_membership_router)
HEAD:backend/ee/onyx/server/tenants/api.py:33:    router.include_router(tenant_management_router)
HEAD:backend/ee/onyx/server/tenants/api.py:34:    router.include_router(user_invitations_router)
HEAD:backend/ee/onyx/server/tenants/api.py:35:    router.include_router(proxy_router)
HEAD:backend/ee/onyx/server/tenants/api.py:37:        router.include_router(admin_router)
HEAD:backend/ee/onyx/server/tenants/billing_api.py:71:router = APIRouter(prefix="/tenants")
HEAD:backend/ee/onyx/server/tenants/proxy.py:44:router = APIRouter(prefix="/proxy")
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:21:router = APIRouter(prefix="/tenants")
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:13:router = APIRouter(prefix="/tenants")
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:35:router = APIRouter(prefix="/tenants")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:43:router = APIRouter(prefix="/admin/token-rate-limits", tags=PUBLIC_API_TAGS)
HEAD:backend/ee/onyx/server/user_group/api.py:80:router = APIRouter(prefix="/manage", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/auth/users.py:1944:        router = APIRouter()
HEAD:backend/onyx/auth/users.py:2769:    router = APIRouter()
HEAD:backend/onyx/db/engine/async_sql_engine.py:160:    leaking them when the worker exits — uvicorn ``--reload`` exercises this
HEAD:backend/onyx/main.py:9:import uvicorn
HEAD:backend/onyx/main.py:172:from onyx.utils.logger import setup_logger, setup_uvicorn_logger
HEAD:backend/onyx/main.py:207:setup_uvicorn_logger(shared_file_handlers=file_handlers)
HEAD:backend/onyx/main.py:265:def include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:281:    application.include_router(router, **final_kwargs)
HEAD:backend/onyx/main.py:292:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:468:    # remaining pools — this path runs on every uvicorn ``--reload`` worker
HEAD:backend/onyx/main.py:517:    application = FastAPI(
HEAD:backend/onyx/main.py:552:    include_router_with_global_prefix_prepended(application, password_router)
HEAD:backend/onyx/main.py:553:    include_router_with_global_prefix_prepended(application, chat_router)
HEAD:backend/onyx/main.py:554:    include_router_with_global_prefix_prepended(application, query_router)
HEAD:backend/onyx/main.py:555:    include_router_with_global_prefix_prepended(application, document_router)
HEAD:backend/onyx/main.py:556:    include_router_with_global_prefix_prepended(application, user_router)
HEAD:backend/onyx/main.py:557:    include_router_with_global_prefix_prepended(application, oauth_test_admin_router)
HEAD:backend/onyx/main.py:558:    include_router_with_global_prefix_prepended(application, admin_query_router)
HEAD:backend/onyx/main.py:559:    include_router_with_global_prefix_prepended(application, admin_router)
HEAD:backend/onyx/main.py:560:    include_router_with_global_prefix_prepended(application, connector_router)
HEAD:backend/onyx/main.py:561:    include_router_with_global_prefix_prepended(application, credential_router)
HEAD:backend/onyx/main.py:562:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:565:    include_router_with_global_prefix_prepended(application, input_prompt_router)
HEAD:backend/onyx/main.py:566:    include_router_with_global_prefix_prepended(application, admin_input_prompt_router)
HEAD:backend/onyx/main.py:567:    include_router_with_global_prefix_prepended(application, cc_pair_router)
HEAD:backend/onyx/main.py:568:    include_router_with_global_prefix_prepended(application, targeted_reindex_router)
HEAD:backend/onyx/main.py:569:    include_router_with_global_prefix_prepended(application, projects_router)
HEAD:backend/onyx/main.py:570:    include_router_with_global_prefix_prepended(application, public_build_router)
HEAD:backend/onyx/main.py:571:    include_router_with_global_prefix_prepended(application, build_router)
HEAD:backend/onyx/main.py:572:    include_router_with_global_prefix_prepended(application, build_admin_router)
HEAD:backend/onyx/main.py:573:    include_router_with_global_prefix_prepended(application, image_generation_router)
HEAD:backend/onyx/main.py:574:    include_router_with_global_prefix_prepended(application, document_set_router)
HEAD:backend/onyx/main.py:575:    include_router_with_global_prefix_prepended(application, hierarchy_router)
HEAD:backend/onyx/main.py:576:    include_router_with_global_prefix_prepended(application, search_api_router)
HEAD:backend/onyx/main.py:577:    include_router_with_global_prefix_prepended(application, search_settings_router)
HEAD:backend/onyx/main.py:578:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:581:    include_router_with_global_prefix_prepended(application, discord_bot_router)
HEAD:backend/onyx/main.py:582:    include_router_with_global_prefix_prepended(application, persona_router)
HEAD:backend/onyx/main.py:583:    include_router_with_global_prefix_prepended(application, admin_persona_router)
HEAD:backend/onyx/main.py:584:    include_router_with_global_prefix_prepended(application, agents_router)
HEAD:backend/onyx/main.py:585:    include_router_with_global_prefix_prepended(application, admin_agents_router)
HEAD:backend/onyx/main.py:586:    include_router_with_global_prefix_prepended(application, default_assistant_router)
HEAD:backend/onyx/main.py:587:    include_router_with_global_prefix_prepended(application, notification_router)
HEAD:backend/onyx/main.py:588:    include_router_with_global_prefix_prepended(application, admin_banner_router)
HEAD:backend/onyx/main.py:589:    include_router_with_global_prefix_prepended(application, tool_router)
HEAD:backend/onyx/main.py:590:    include_router_with_global_prefix_prepended(application, admin_tool_router)
HEAD:backend/onyx/main.py:591:    include_router_with_global_prefix_prepended(application, oauth_config_router)
HEAD:backend/onyx/main.py:592:    include_router_with_global_prefix_prepended(application, admin_oauth_config_router)
HEAD:backend/onyx/main.py:593:    include_router_with_global_prefix_prepended(application, user_oauth_token_router)
HEAD:backend/onyx/main.py:594:    include_router_with_global_prefix_prepended(application, state_router)
HEAD:backend/onyx/main.py:595:    include_router_with_global_prefix_prepended(application, onyx_api_router)
HEAD:backend/onyx/main.py:596:    include_router_with_global_prefix_prepended(application, settings_router)
HEAD:backend/onyx/main.py:597:    include_router_with_global_prefix_prepended(application, settings_admin_router)
HEAD:backend/onyx/main.py:598:    include_router_with_global_prefix_prepended(application, security_admin_router)
HEAD:backend/onyx/main.py:599:    include_router_with_global_prefix_prepended(application, sso_admin_router)
HEAD:backend/onyx/main.py:600:    include_router_with_global_prefix_prepended(application, llm_admin_router)
HEAD:backend/onyx/main.py:601:    include_router_with_global_prefix_prepended(application, kg_admin_router)
HEAD:backend/onyx/main.py:602:    include_router_with_global_prefix_prepended(application, llm_router)
HEAD:backend/onyx/main.py:603:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:606:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:609:    include_router_with_global_prefix_prepended(application, embedding_admin_router)
HEAD:backend/onyx/main.py:610:    include_router_with_global_prefix_prepended(application, embedding_router)
HEAD:backend/onyx/main.py:611:    include_router_with_global_prefix_prepended(application, web_search_router)
HEAD:backend/onyx/main.py:612:    include_router_with_global_prefix_prepended(application, web_search_admin_router)
HEAD:backend/onyx/main.py:613:    include_router_with_global_prefix_prepended(application, tracing_admin_router)
HEAD:backend/onyx/main.py:614:    include_router_with_global_prefix_prepended(application, voice_admin_router)
HEAD:backend/onyx/main.py:615:    include_router_with_global_prefix_prepended(application, voice_router)
HEAD:backend/onyx/main.py:616:    include_router_with_global_prefix_prepended(application, voice_websocket_router)
HEAD:backend/onyx/main.py:617:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:620:    include_router_with_global_prefix_prepended(application, cost_override_router)
HEAD:backend/onyx/main.py:621:    include_router_with_global_prefix_prepended(application, user_usage_router)
HEAD:backend/onyx/main.py:622:    include_router_with_global_prefix_prepended(application, admin_usage_router)
HEAD:backend/onyx/main.py:623:    include_router_with_global_prefix_prepended(application, api_key_router)
HEAD:backend/onyx/main.py:624:    include_router_with_global_prefix_prepended(application, standard_oauth_router)
HEAD:backend/onyx/main.py:625:    include_router_with_global_prefix_prepended(application, federated_router)
HEAD:backend/onyx/main.py:626:    include_router_with_global_prefix_prepended(application, mcp_router)
HEAD:backend/onyx/main.py:627:    include_router_with_global_prefix_prepended(application, mcp_admin_router)
HEAD:backend/onyx/main.py:628:    include_router_with_global_prefix_prepended(application, skill_router)
HEAD:backend/onyx/main.py:630:    include_router_with_global_prefix_prepended(application, pat_router)
HEAD:backend/onyx/main.py:631:    include_router_with_global_prefix_prepended(application, captcha_router)
HEAD:backend/onyx/main.py:811:    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
HEAD:backend/onyx/mcp_server/api.py:29:# (python -m onyx.mcp_server_main, uvicorn onyx.mcp_server.api:mcp_app, etc.).
HEAD:backend/onyx/mcp_server/api.py:83:    app = FastAPI(
HEAD:backend/onyx/mcp_server_main.py:3:import uvicorn
HEAD:backend/onyx/mcp_server_main.py:29:    uvicorn.run(
HEAD:backend/onyx/server/api_key/api.py:27:router = APIRouter(prefix="/admin/api-key")
HEAD:backend/onyx/server/auth/captcha_api.py:42:router = APIRouter(prefix="/auth/captcha", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/auth/mobile.py:30:router = APIRouter()
HEAD:backend/onyx/server/auth/mobile.py:32:router.include_router(fastapi_users.get_auth_router(mobile_auth_backend))
HEAD:backend/onyx/server/auth/mobile.py:33:router.include_router(fastapi_users.get_refresh_router(mobile_auth_backend))
HEAD:backend/onyx/server/documents/cc_pair.py:98:router = APIRouter(prefix="/manage")
HEAD:backend/onyx/server/documents/connector.py:176:router = APIRouter(prefix="/manage", dependencies=[Depends(require_vector_db)])
HEAD:backend/onyx/server/documents/credential.py:52:router = APIRouter(prefix="/manage", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/credential_capabilities.py:58:router = APIRouter(prefix="/manage", dependencies=[Depends(require_vector_db)])
HEAD:backend/onyx/server/documents/document.py:20:router = APIRouter(prefix="/document")
HEAD:backend/onyx/server/documents/standard_oauth.py:31:router = APIRouter(prefix="/connector/oauth")
HEAD:backend/onyx/server/documents/targeted_reindex.py:43:router = APIRouter(prefix="/manage")
HEAD:backend/onyx/server/features/admin_banner/api.py:33:admin_router = APIRouter(prefix="/admin/banner")
HEAD:backend/onyx/server/features/build/api.py:45:router = APIRouter(prefix="/build", dependencies=[Depends(require_onyx_craft_enabled)])
HEAD:backend/onyx/server/features/build/api.py:49:admin_router = APIRouter(
HEAD:backend/onyx/server/features/build/api.py:53:admin_router.include_router(external_apps_admin_router, tags=["build"])
HEAD:backend/onyx/server/features/build/api.py:69:router.include_router(sessions_router, tags=["build"])
HEAD:backend/onyx/server/features/build/api.py:70:router.include_router(messages_router, tags=["build"])
HEAD:backend/onyx/server/features/build/api.py:71:router.include_router(turns_router, tags=["build"])
HEAD:backend/onyx/server/features/build/api.py:72:router.include_router(user_library_router, tags=["build"])
HEAD:backend/onyx/server/features/build/api.py:73:router.include_router(scheduled_tasks_router, tags=["build"])
HEAD:backend/onyx/server/features/build/api.py:74:router.include_router(external_apps_router, tags=["build"])
HEAD:backend/onyx/server/features/build/api.py:75:router.include_router(external_apps_oauth_router, tags=["build"])
HEAD:backend/onyx/server/features/build/api.py:76:router.include_router(debug_router, tags=["build-debug"])
HEAD:backend/onyx/server/features/build/api.py:77:router.include_router(approvals_router, tags=["build"])
HEAD:backend/onyx/server/features/build/approvals/api.py:37:router = APIRouter(prefix="/approvals")
HEAD:backend/onyx/server/features/build/debug.py:29:router = APIRouter()
HEAD:backend/onyx/server/features/build/external_apps/api.py:67:router = APIRouter()
HEAD:backend/onyx/server/features/build/external_apps/api.py:69:admin_router = APIRouter()
HEAD:backend/onyx/server/features/build/external_apps/oauth.py:37:router = APIRouter()
HEAD:backend/onyx/server/features/build/interactive_turns/api.py:41:router = APIRouter()
HEAD:backend/onyx/server/features/build/sandbox/image/initial-requirements.in:17:uvicorn[standard]
HEAD:backend/onyx/server/features/build/sandbox/image/initial-requirements.txt:22:    # via uvicorn
HEAD:backend/onyx/server/features/build/sandbox/image/initial-requirements.txt:40:    # via uvicorn
HEAD:backend/onyx/server/features/build/sandbox/image/initial-requirements.txt:42:    # via uvicorn
HEAD:backend/onyx/server/features/build/sandbox/image/initial-requirements.txt:101:    # via uvicorn
HEAD:backend/onyx/server/features/build/sandbox/image/initial-requirements.txt:105:    # via uvicorn
HEAD:backend/onyx/server/features/build/sandbox/image/initial-requirements.txt:128:uvicorn[standard]==0.49.0
HEAD:backend/onyx/server/features/build/sandbox/image/initial-requirements.txt:131:    # via uvicorn
HEAD:backend/onyx/server/features/build/sandbox/image/initial-requirements.txt:133:    # via uvicorn
HEAD:backend/onyx/server/features/build/sandbox/image/initial-requirements.txt:135:    # via uvicorn
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py:13:import uvicorn
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py:52:app = FastAPI(title="sandbox-sidecar", docs_url=None, redoc_url=None)
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py:425:    uvicorn.run(app, host="0.0.0.0", port=PUSH_DAEMON_PORT)  # noqa: S104
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:76:router = APIRouter(prefix="/scheduled-tasks")
HEAD:backend/onyx/server/features/build/session/api.py:79:router = APIRouter(prefix="/sessions")
HEAD:backend/onyx/server/features/build/session/messages.py:58:router = APIRouter()
HEAD:backend/onyx/server/features/build/user_library/api.py:48:router = APIRouter(prefix="/user-library")
HEAD:backend/onyx/server/features/build/webapp_proxy.py:391:public_build_router = APIRouter(prefix="/build")
HEAD:backend/onyx/server/features/default_assistant/api.py:23:router = APIRouter(prefix="/admin/default-assistant")
HEAD:backend/onyx/server/features/document_set/api.py:44:router = APIRouter(prefix="/manage")
HEAD:backend/onyx/server/features/hierarchy/api.py:48:router = APIRouter(prefix=HIERARCHY_NODES_PREFIX)
HEAD:backend/onyx/server/features/image_generation/api.py:31:router = APIRouter(prefix="/image-generation")
HEAD:backend/onyx/server/features/input_prompt/api.py:26:basic_router = APIRouter(prefix="/input_prompt")
HEAD:backend/onyx/server/features/input_prompt/api.py:27:admin_router = APIRouter(prefix="/admin/input_prompt")
HEAD:backend/onyx/server/features/mcp/api.py:567:router = APIRouter(prefix="/mcp")
HEAD:backend/onyx/server/features/mcp/api.py:568:router.include_router(client_metadata_router)
HEAD:backend/onyx/server/features/mcp/api.py:569:admin_router = APIRouter(prefix="/admin/mcp")
HEAD:backend/onyx/server/features/mcp/client_metadata.py:19:router = APIRouter()
HEAD:backend/onyx/server/features/notifications/api.py:39:router = APIRouter(prefix="/notifications")
HEAD:backend/onyx/server/features/oauth_config/api.py:40:admin_router = APIRouter(prefix="/admin/oauth-config")
HEAD:backend/onyx/server/features/oauth_config/api.py:41:router = APIRouter(prefix="/oauth-config")
HEAD:backend/onyx/server/features/password/api.py:16:router = APIRouter(prefix="/password")
HEAD:backend/onyx/server/features/persona/api.py:145:admin_router = APIRouter(prefix="/admin/persona")
HEAD:backend/onyx/server/features/persona/api.py:146:basic_router = APIRouter(prefix="/persona")
HEAD:backend/onyx/server/features/persona/api.py:150:admin_agents_router = APIRouter(prefix=ADMIN_AGENTS_RESOURCE)
HEAD:backend/onyx/server/features/persona/api.py:151:agents_router = APIRouter(prefix=AGENTS_RESOURCE)
HEAD:backend/onyx/server/features/projects/api.py:53:router = APIRouter(prefix="/user/projects")
HEAD:backend/onyx/server/features/search/api.py:53:router = APIRouter(prefix="/search")
HEAD:backend/onyx/server/features/skill/api.py:96:user_router = APIRouter(prefix="/skills")
HEAD:backend/onyx/server/features/tool/api.py:45:router = APIRouter(prefix="/tool")
HEAD:backend/onyx/server/features/tool/api.py:46:admin_router = APIRouter(prefix="/admin/tool")
HEAD:backend/onyx/server/features/usage/api.py:217:router = APIRouter(prefix="/admin/cost-overrides", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/features/usage/api.py:219:user_usage_router = APIRouter(prefix="/user/usage", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/features/usage/api.py:221:admin_usage_router = APIRouter(prefix="/admin/usage", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/features/user_oauth_token/api.py:14:router = APIRouter(prefix="/user-oauth-token")
HEAD:backend/onyx/server/features/web_search/api.py:51:router = APIRouter(prefix="/web-search", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/federated/api.py:54:router = APIRouter(prefix="/federated")
HEAD:backend/onyx/server/kg/api.py:51:admin_router = APIRouter(prefix="/admin/kg")
HEAD:backend/onyx/server/manage/administrative.py:55:router = APIRouter(prefix="/manage")
HEAD:backend/onyx/server/manage/code_interpreter/api.py:20:admin_router = APIRouter(prefix="/admin/code-interpreter")
HEAD:backend/onyx/server/manage/discord_bot/api.py:40:router = APIRouter(prefix="/manage/admin/discord-bot")
HEAD:backend/onyx/server/manage/embedding/api.py:34:admin_router = APIRouter(prefix="/admin/embedding")
HEAD:backend/onyx/server/manage/embedding/api.py:35:basic_router = APIRouter(prefix="/embedding")
HEAD:backend/onyx/server/manage/get_state.py:40:router = APIRouter()
HEAD:backend/onyx/server/manage/image_generation/api.py:45:admin_router = APIRouter(prefix="/admin/image-generation")
HEAD:backend/onyx/server/manage/llm/api.py:143:admin_router = APIRouter(prefix="/admin/llm")
HEAD:backend/onyx/server/manage/llm/api.py:144:basic_router = APIRouter(prefix="/llm")
HEAD:backend/onyx/server/manage/oauth_test.py:26:router = APIRouter(prefix="/admin/oauth-test")
HEAD:backend/onyx/server/manage/opensearch_migration/api.py:20:admin_router = APIRouter(prefix="/admin/opensearch-migration")
HEAD:backend/onyx/server/manage/search_settings.py:92:router = APIRouter(prefix="/search-settings")
HEAD:backend/onyx/server/manage/slack_bot.py:48:router = APIRouter(prefix="/manage")
HEAD:backend/onyx/server/manage/sso/api.py:111:admin_router = APIRouter(prefix="/admin/sso")
HEAD:backend/onyx/server/manage/tracing/api.py:44:admin_router = APIRouter(
HEAD:backend/onyx/server/manage/users.py:151:router = APIRouter()
HEAD:backend/onyx/server/manage/voice/api.py:38:admin_router = APIRouter(prefix="/admin/voice")
HEAD:backend/onyx/server/manage/voice/user_api.py:29:router = APIRouter(prefix="/voice")
HEAD:backend/onyx/server/manage/voice/websocket_api.py:31:router = APIRouter(prefix="/voice")
HEAD:backend/onyx/server/manage/web_search/api.py:50:admin_router = APIRouter(prefix="/admin/web-search")
HEAD:backend/onyx/server/oidc_multi.py:85:router = APIRouter(prefix="/auth/oidc")
HEAD:backend/onyx/server/onyx_api/ingestion.py:55:router = APIRouter(prefix="/onyx-api", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/pat/api.py:24:router = APIRouter(prefix="/user/pats")
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:159:router = APIRouter(prefix="/chat")
HEAD:backend/onyx/server/query_and_chat/query_backend.py:29:admin_router = APIRouter(prefix="/admin")
HEAD:backend/onyx/server/query_and_chat/query_backend.py:30:basic_router = APIRouter(prefix="/query")
HEAD:backend/onyx/server/saml_multi.py:52:router = APIRouter(prefix="/auth/saml", dependencies=[Depends(_reject_if_unsupported)])
HEAD:backend/onyx/server/security/api.py:30:admin_router = APIRouter(prefix="/admin/security")
HEAD:backend/onyx/server/settings/api.py:64:admin_router = APIRouter(prefix="/admin/settings")
```
### Interpretation
The repository contains explicit HTTP/API framework and routing evidence.
The exact request lifecycle, middleware ordering, authentication dependency
chain and authorization enforcement path remain subject to later tracing.
## Web Application Evidence
Evidence lines captured: 9
```text
10:    "dev": "next dev",
11:    "dev:profile": "NEXT_PUBLIC_ENABLE_STATS=true next dev",
12:    "dev:clean": "bun run clean && next dev",
14:    "build": "next build",
15:    "build:fast": "SKIP_TYPE_CHECK=1 next build",
16:    "start": "next start",
76:    "next": "16.3.3",
81:    "react": "19.2.8",
140:    "typescript": "^5.9.3",
```
The web directory contains independent package/build metadata, supporting its
classification as a distinct web application component.
## Background Worker Evidence
Evidence lines captured: 300
```text
HEAD:backend/ee/onyx/background/celery/apps/docfetching.py:2:from onyx.background.celery.apps.docfetching import celery_app
HEAD:backend/ee/onyx/background/celery/apps/docfetching.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/docprocessing.py:2:from onyx.background.celery.apps.docprocessing import celery_app
HEAD:backend/ee/onyx/background/celery/apps/docprocessing.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:2:from onyx.background.celery.apps.heavy import celery_app
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/light.py:2:from onyx.background.celery.apps.light import celery_app
HEAD:backend/ee/onyx/background/celery/apps/light.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/monitoring.py:2:from onyx.background.celery.apps.monitoring import celery_app
HEAD:backend/ee/onyx/background/celery/apps/monitoring.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/primary.py:2:from onyx.background.celery.apps.primary import celery_app
HEAD:backend/ee/onyx/background/celery/apps/primary.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/scheduled_tasks.py:2:from onyx.background.celery.apps.scheduled_tasks import celery_app
HEAD:backend/ee/onyx/background/celery/apps/scheduled_tasks.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/apps/user_file_processing.py:2:from onyx.background.celery.apps.user_file_processing import celery_app
HEAD:backend/ee/onyx/background/celery/apps/user_file_processing.py:4:celery_app.autodiscover_tasks(
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:5:from onyx.background.celery.tasks.beat_schedule import (
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:9:from onyx.background.celery.tasks.beat_schedule import (
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:12:from onyx.background.celery.tasks.beat_schedule import (
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:15:from onyx.background.celery.tasks.beat_schedule import (
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:125:                # Cleanup belongs on the heavy worker; it shares the queue the
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:3:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:16:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:3:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:9:from onyx.background.celery.tasks.beat_schedule import BEAT_EXPIRES_DEFAULT
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:71:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:8:from celery import Celery, Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:34:from onyx.background.celery.tasks.beat_schedule import CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:206:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:262:            # tasks can be in the queue in redis, in reserved tasks (prefetched by the worker),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:409:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:450:    # the primary worker sends the task and it is immediately executed
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:451:    # before the primary worker can finalize the fence
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:846:    This can happen if the indexing worker hard crashes or is terminated.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:865:    2. Redis can be inspected for the task id, but the task id is gone between the time a worker receives the task
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:866:    and the time it actually starts on the worker.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:924:        # the celery task was prefetched and is reserved within a worker
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:7:from celery import Celery, Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:36:from onyx.background.celery.tasks.beat_schedule import CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:163:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:236:            # tasks can be in the queue in redis, in reserved tasks (prefetched by the worker),
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:351:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:374:    # the primary worker sends the task and it is immediately executed
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:375:    # before the primary worker can finalize the fence
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:681:    celery_app: Celery,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:718:    This can happen if the indexing worker hard crashes or is terminated.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:737:    2. Redis can be inspected for the task id, but the task id is gone between the time a worker receives the task
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:738:    and the time it actually starts on the worker.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:791:        # the celery task was prefetched and is reserved within the indexing worker
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:1:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:14:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:2:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:24:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:4:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:82:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:3:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:17:# Supervisord captures each worker program's stdout to
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:26:# workers (replicas > 1) only one pod per worker type is sampled, and nothing
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:32:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:40:    worker_name: str,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:48:        worker_name=worker_name,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:53:        "Log export collection finished: export_id=%s worker_name=%s "
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:56:        worker_name,
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:62:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:5:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:30:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:8:from celery import shared_task
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:18:@shared_task(
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:9:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:37:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:3:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:54:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:74:    expired sessions and exits, so it occupies a single light-worker thread for
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:84:    per tenant at a time, so at most one light-worker thread does TTL work.
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:147:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:4:from celery import Task, shared_task
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:14:@shared_task(  # ty: ignore[invalid-argument-type]
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:22:    """This function is likely to move in the worker refactor happening next."""
HEAD:backend/ee/onyx/configs/app_configs.py:104:NUM_PERMISSION_WORKERS = int(os.environ.get("NUM_PERMISSION_WORKERS") or 2)
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:53:            "enumeration; failing the sync so the worker releases its lock "
HEAD:backend/ee/onyx/external_permissions/sync_params.py:42:# google, github, ...), which cost ~60 MB. Load them on first call so workers
HEAD:backend/ee/onyx/server/evals/api.py:4:from onyx.background.celery.apps.client import celery_app as client_app
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:26:    _stream_worker_guard,
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:260:            _passthrough_stream_worker,
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:346:def _passthrough_stream_worker(
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:377:        with _stream_worker_guard(
HEAD:backend/ee/onyx/server/gateway/anthropic_passthrough.py:395:            # iter_lines() read would otherwise hold the worker thread and the
HEAD:backend/ee/onyx/server/gateway/api.py:30:    _stream_worker_guard,
HEAD:backend/ee/onyx/server/gateway/api.py:305:def _stream_worker(
HEAD:backend/ee/onyx/server/gateway/api.py:329:        with _stream_worker_guard(
HEAD:backend/ee/onyx/server/gateway/api.py:381:            _stream_worker,
HEAD:backend/ee/onyx/server/gateway/api.py:541:def _responses_stream_worker(
HEAD:backend/ee/onyx/server/gateway/api.py:625:        with _stream_worker_guard(
HEAD:backend/ee/onyx/server/gateway/api.py:759:            _responses_stream_worker,
HEAD:backend/ee/onyx/server/gateway/api.py:1076:def _anthropic_stream_worker(
HEAD:backend/ee/onyx/server/gateway/api.py:1196:        with _stream_worker_guard(
HEAD:backend/ee/onyx/server/gateway/api.py:1309:            _anthropic_stream_worker,
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:21:    _stream_worker_guard,
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:287:            _openai_passthrough_stream_worker,
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:389:def _openai_passthrough_stream_worker(
HEAD:backend/ee/onyx/server/gateway/openai_passthrough.py:434:        with _stream_worker_guard(
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:89:def _stream_worker_guard(
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:99:    """The HTTP status is already sent by the time a worker runs, so upstream
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:154:    worker: Callable[..., None], worker_kwargs: dict[str, Any]
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:156:    """Bridge a stream worker through a queue so the whole consumption —
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:163:    worker_thread = start_thread_with_context(
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:164:        worker,
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:167:        kwargs={**worker_kwargs, "out": out, "cancelled": cancelled},
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:171:            if worker_thread.is_alive():
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:177:                # Worker died before signalling: drain, or the stream truncates.
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:190:    worker: Callable[..., None], worker_kwargs: dict[str, Any]
HEAD:backend/ee/onyx/server/gateway/stream_bridge.py:193:        _run_bridged_stream(worker, worker_kwargs),
HEAD:backend/ee/onyx/server/log_export/api.py:93:API_SERVER_WORKER_NAME = "api_server"
HEAD:backend/ee/onyx/server/log_export/api.py:95:# One collector task per worker type, each routed to a queue that worker
HEAD:backend/ee/onyx/server/log_export/api.py:97:WORKER_COLLECT_QUEUES: dict[str, str] = {
HEAD:backend/ee/onyx/server/log_export/api.py:139:    Starts an export: fans out one collector task per worker type, collects the
HEAD:backend/ee/onyx/server/log_export/api.py:143:    onyx-lite overlay); a failing broker degrades the export to the workers
HEAD:backend/ee/onyx/server/log_export/api.py:168:        # Fan out before the inline collection below so workers get the full
HEAD:backend/ee/onyx/server/log_export/api.py:172:        # workers to collect from, so the fan-out is skipped outright
HEAD:backend/ee/onyx/server/log_export/api.py:175:        enqueued_worker_names: list[str] = []
HEAD:backend/ee/onyx/server/log_export/api.py:183:            for worker_name, queue in WORKER_COLLECT_QUEUES.items():
HEAD:backend/ee/onyx/server/log_export/api.py:192:                            "worker_name": worker_name,
HEAD:backend/ee/onyx/server/log_export/api.py:197:                    # rest would fail too. Only the workers already enqueued are
HEAD:backend/ee/onyx/server/log_export/api.py:202:                        worker_name,
HEAD:backend/ee/onyx/server/log_export/api.py:203:                        enqueued_worker_names,
HEAD:backend/ee/onyx/server/log_export/api.py:207:                enqueued_worker_names.append(worker_name)
HEAD:backend/ee/onyx/server/log_export/api.py:215:            worker_names=[API_SERVER_WORKER_NAME, *enqueued_worker_names],
HEAD:backend/ee/onyx/server/log_export/api.py:219:        # No celery worker runs in the api_server container, so its logs are
HEAD:backend/ee/onyx/server/log_export/api.py:223:            worker_name=API_SERVER_WORKER_NAME,
HEAD:backend/ee/onyx/server/log_export/api.py:250:    reported = {receipt.worker_name for receipt in snapshot.receipts}
HEAD:backend/ee/onyx/server/log_export/api.py:257:        pending_worker_names=[
HEAD:backend/ee/onyx/server/log_export/api.py:258:            worker_name
HEAD:backend/ee/onyx/server/log_export/api.py:259:            for worker_name in snapshot.manifest.worker_names
HEAD:backend/ee/onyx/server/log_export/api.py:260:            if worker_name not in reported
HEAD:backend/ee/onyx/server/log_export/collection.py:4:per-worker celery collector tasks once fan-out collection lands.
HEAD:backend/ee/onyx/server/log_export/models.py:18:    """Outcome report written by each collector, one per fanned-out worker.
HEAD:backend/ee/onyx/server/log_export/models.py:20:    Receipts mean "this worker reported"; pieces must be discovered by listing
HEAD:backend/ee/onyx/server/log_export/models.py:25:    worker_name: str
HEAD:backend/ee/onyx/server/log_export/models.py:49:    # Every worker expected to write a receipt, including the api_server's
HEAD:backend/ee/onyx/server/log_export/models.py:51:    worker_names: list[str]
HEAD:backend/ee/onyx/server/log_export/models.py:85:    # Manifest workers that have not written a receipt yet.
HEAD:backend/ee/onyx/server/log_export/models.py:86:    pending_worker_names: list[str]
HEAD:backend/ee/onyx/server/log_export/storage.py:5:``receipt_{worker_name}.json`` per fanned-out worker. Shared by the collector
HEAD:backend/ee/onyx/server/log_export/storage.py:45:# How long an export waits for worker receipts before reporting ``READY``
HEAD:backend/ee/onyx/server/log_export/storage.py:47:# a dead worker never picked up is discarded instead of running late.
HEAD:backend/ee/onyx/server/log_export/storage.py:67:def receipt_file_id(export_id: str, worker_name: str) -> str:
HEAD:backend/ee/onyx/server/log_export/storage.py:68:    """Returns the file ID of the given worker's collection receipt."""
HEAD:backend/ee/onyx/server/log_export/storage.py:69:    return f"{export_file_id_prefix(export_id)}receipt_{worker_name}.json"
HEAD:backend/ee/onyx/server/log_export/storage.py:119:    """Returns ``READY`` once every worker reported or the deadline passed."""
HEAD:backend/ee/onyx/server/log_export/storage.py:120:    reported = {receipt.worker_name for receipt in snapshot.receipts}
HEAD:backend/ee/onyx/server/log_export/storage.py:121:    if set(snapshot.manifest.worker_names) <= reported:
HEAD:backend/ee/onyx/server/log_export/storage.py:143:        f"{BUNDLE_MANIFEST_FILE_NAME} with per-worker receipt outcomes.",
HEAD:backend/ee/onyx/server/log_export/storage.py:144:        "On Kubernetes, each piece samples a single replica per worker type;",
HEAD:backend/ee/onyx/server/log_export/storage.py:147:        "Worker outcomes:",
HEAD:backend/ee/onyx/server/log_export/storage.py:149:    reported = {receipt.worker_name for receipt in snapshot.receipts}
HEAD:backend/ee/onyx/server/log_export/storage.py:154:        lines.append(f"  {receipt.worker_name}: {receipt.status.value}{detail}")
HEAD:backend/ee/onyx/server/log_export/storage.py:156:        f"  {worker_name}: no receipt (did not report before the deadline)"
HEAD:backend/ee/onyx/server/log_export/storage.py:157:        for worker_name in manifest.worker_names
HEAD:backend/ee/onyx/server/log_export/storage.py:158:        if worker_name not in reported
HEAD:backend/ee/onyx/server/log_export/storage.py:209:    worker_name: str,
HEAD:backend/ee/onyx/server/log_export/storage.py:217:    dedupe: collectors fanned out simultaneously to worker types sharing a
HEAD:backend/ee/onyx/server/log_export/storage.py:221:    Writes ``receipt_{worker_name}.json`` recording the outcome, including a
HEAD:backend/ee/onyx/server/log_export/storage.py:222:    ``FAILED`` receipt when collection raises. Receipts mean "this worker
HEAD:backend/ee/onyx/server/log_export/storage.py:230:        worker_name: Worker type this collector runs as, recorded in the
HEAD:backend/ee/onyx/server/log_export/storage.py:260:                f"{worker_name} worker."
HEAD:backend/ee/onyx/server/log_export/storage.py:289:            "Log export collection failed: export_id=%s worker_name=%s",
HEAD:backend/ee/onyx/server/log_export/storage.py:291:            worker_name,
HEAD:backend/ee/onyx/server/log_export/storage.py:300:        worker_name=worker_name,
HEAD:backend/ee/onyx/server/log_export/storage.py:310:        display_name=f"receipt_{worker_name}.json",
HEAD:backend/ee/onyx/server/log_export/storage.py:313:        file_id=receipt_file_id(export_id, worker_name),
HEAD:backend/ee/onyx/server/middleware/license_enforcement.py:87:# Caps the gated re-check at one DB re-check per worker per interval, since every
HEAD:backend/ee/onyx/server/middleware/tier_gate.py:81:        # CP round-trip on cache miss. Offload to a worker so the event loop
HEAD:backend/ee/onyx/server/user_group/api.py:53:from onyx.background.celery.tasks.beat_schedule import BEAT_EXPIRES_DEFAULT
HEAD:backend/onyx/background/README.md:11:## Worker → Queue Mapping
HEAD:backend/onyx/background/README.md:13:| Worker                    | File                           | Queues                                                                                                               |
HEAD:backend/onyx/background/README.md:24:## Non-Worker Apps
HEAD:backend/onyx/background/README.md:29:| **Client** | `client.py` | Minimal app for task submission from non-worker processes (e.g., API server)                          |
HEAD:backend/onyx/background/README.md:39:## Worker Details
HEAD:backend/onyx/background/README.md:43:It is the single worker which handles tasks from the default celery queue. It is a singleton worker ensured by the `PRIMARY_WORKER` Redis lock
HEAD:backend/onyx/background/README.md:44:which it touches every `CELERY_PRIMARY_WORKER_LOCK_TIMEOUT / 8` seconds (using Celery Bootsteps)
HEAD:backend/onyx/background/README.md:66:Watchdog is a separate Python process managed by supervisord which runs alongside celery workers. It checks the ONYX_CELERY_BEAT_HEARTBEAT_KEY in
HEAD:backend/onyx/background/README.md:73:Can have 24 concurrent workers, each with a prefetch of 8 for a total of 192 tasks in flight at once.
HEAD:backend/onyx/background/README.md:104:- Memory of supervisor managed processes (workers, beat, slack)
HEAD:backend/onyx/background/README.md:109:Workers can expose Prometheus metrics via a standalone HTTP server. Currently docfetching and docprocessing have push-based task lifecycle metrics; the monitoring worker runs pull-based collectors for queue depth and connector health.
HEAD:backend/onyx/background/README.md:111:For the full metric reference, integration guide, and PromQL examples, see [`docs/METRICS.md`](../../../docs/METRICS.md#celery-worker-metrics).
HEAD:backend/onyx/background/celery/apps/app_base.py:13:from celery.exceptions import WorkerShutdown
HEAD:backend/onyx/background/celery/apps/app_base.py:17:from celery.worker import strategy
HEAD:backend/onyx/background/celery/apps/app_base.py:18:from celery.worker.control import control_command
HEAD:backend/onyx/background/celery/apps/app_base.py:30:    celery_is_worker_primary,
HEAD:backend/onyx/background/celery/apps/app_base.py:92:    """Remote command to wipe this worker's in-memory revoked-task set.
HEAD:backend/onyx/background/celery/apps/app_base.py:94:    The set lives only in memory, propagates between workers via mingle, and its
HEAD:backend/onyx/background/celery/apps/app_base.py:102:    from celery.worker import state as worker_state
HEAD:backend/onyx/background/celery/apps/app_base.py:104:    count = len(worker_state.revoked)
HEAD:backend/onyx/background/celery/apps/app_base.py:105:    worker_state.revoked.clear()
HEAD:backend/onyx/background/celery/apps/app_base.py:127:            # so it does not leak into any subsequent tasks on the same worker process
HEAD:backend/onyx/background/celery/apps/app_base.py:131:@before_task_publish.connect
HEAD:backend/onyx/background/celery/apps/app_base.py:137:    workers can compute queue wait time (time between publish and execution)."""
HEAD:backend/onyx/background/celery/apps/app_base.py:142:@task_prerun.connect
HEAD:backend/onyx/background/celery/apps/app_base.py:152:    # from a previous task executed in the same worker process do not leak
HEAD:backend/onyx/background/celery/apps/app_base.py:178:    This also does not fire if a worker with acks_late=False crashes (which all of our
HEAD:backend/onyx/background/celery/apps/app_base.py:179:    long running workers are)
HEAD:backend/onyx/background/celery/apps/app_base.py:294:    """The first signal sent on celery worker startup"""
HEAD:backend/onyx/background/celery/apps/app_base.py:322:    # Initialize tracing in workers if credentials are available.
HEAD:backend/onyx/background/celery/apps/app_base.py:328:    Will raise WorkerShutdown to kill the celery worker if the timeout
HEAD:backend/onyx/background/celery/apps/app_base.py:362:        raise WorkerShutdown(msg)
HEAD:backend/onyx/background/celery/apps/app_base.py:370:    Will raise WorkerShutdown to kill the celery worker if the timeout is reached."""
HEAD:backend/onyx/background/celery/apps/app_base.py:403:        raise WorkerShutdown(msg)
HEAD:backend/onyx/background/celery/apps/app_base.py:409:def on_secondary_worker_init(sender: Any, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/app_base.py:410:    logger.info("Running as a secondary celery worker: pid=%s", os.getpid())
HEAD:backend/onyx/background/celery/apps/app_base.py:412:    # Set up variables for waiting on primary worker
HEAD:backend/onyx/background/celery/apps/app_base.py:418:    logger.info("Waiting for primary worker to be ready...")
HEAD:backend/onyx/background/celery/apps/app_base.py:420:        if r.exists(OnyxRedisLocks.PRIMARY_WORKER):
HEAD:backend/onyx/background/celery/apps/app_base.py:425:            "Primary worker is not ready yet. elapsed=%s timeout=%s",
HEAD:backend/onyx/background/celery/apps/app_base.py:430:            msg = f"Primary worker was not ready within the timeout. ({WAIT_LIMIT} seconds). Exiting..."
HEAD:backend/onyx/background/celery/apps/app_base.py:432:            raise WorkerShutdown(msg)
HEAD:backend/onyx/background/celery/apps/app_base.py:436:    logger.info("Wait for primary worker completed successfully. Continuing...")
HEAD:backend/onyx/background/celery/apps/app_base.py:440:def on_worker_ready(sender: Any, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/app_base.py:441:    task_logger.info("worker_ready signal received.")
HEAD:backend/onyx/background/celery/apps/app_base.py:453:def on_worker_shutdown(sender: Any, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/app_base.py:460:    if not celery_is_worker_primary(sender):
HEAD:backend/onyx/background/celery/apps/app_base.py:463:    if not hasattr(sender, "primary_worker_lock"):
HEAD:backend/onyx/background/celery/apps/app_base.py:464:        # primary_worker_lock will not exist when MULTI_TENANT is True
HEAD:backend/onyx/background/celery/apps/app_base.py:467:    if not sender.primary_worker_lock:
HEAD:backend/onyx/background/celery/apps/app_base.py:470:    logger.info("Releasing primary worker lock.")
HEAD:backend/onyx/background/celery/apps/app_base.py:471:    lock: RedisLock = sender.primary_worker_lock
HEAD:backend/onyx/background/celery/apps/app_base.py:476:                sender.primary_worker_lock = None
HEAD:backend/onyx/background/celery/apps/app_base.py:478:                logger.exception("Failed to release primary worker lock")
HEAD:backend/onyx/background/celery/apps/app_base.py:480:        logger.exception("Failed to check if primary worker lock is owned")
HEAD:backend/onyx/background/celery/apps/app_base.py:506:    Returns the (level, human-readable explanation) for celery worker logging.
HEAD:backend/onyx/background/celery/apps/app_base.py:509:    default. An operator-supplied CLI flag is treated as a per-worker
HEAD:backend/onyx/background/celery/apps/app_base.py:511:    server, model servers, and all Celery workers.
HEAD:backend/onyx/background/celery/apps/app_base.py:582:    # this worker actually runs at.
HEAD:backend/onyx/background/celery/apps/app_base.py:656:@task_postrun.connect
HEAD:backend/onyx/background/celery/apps/app_base.py:674:    Raises WorkerShutdown if the timeout is reached.
HEAD:backend/onyx/background/celery/apps/app_base.py:688:            raise WorkerShutdown(msg)
HEAD:backend/onyx/background/celery/apps/app_base.py:691:        # Imported here: opensearchpy costs ~18 MB and not every worker needs it.
HEAD:backend/onyx/background/celery/apps/app_base.py:699:            raise WorkerShutdown(msg)
HEAD:backend/onyx/background/celery/apps/app_base.py:702:# File for validating worker liveness
HEAD:backend/onyx/background/celery/apps/app_base.py:704:    requires = {"celery.worker.components:Timer"}
HEAD:backend/onyx/background/celery/apps/app_base.py:706:    def __init__(self, worker: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/app_base.py:707:        super().__init__(worker, **kwargs)
HEAD:backend/onyx/background/celery/apps/app_base.py:710:        self.path = make_probe_path("liveness", worker.hostname)
HEAD:backend/onyx/background/celery/apps/app_base.py:712:    def start(self, worker: Any) -> None:  # ty: ignore[invalid-method-override]
HEAD:backend/onyx/background/celery/apps/app_base.py:713:        self.task_tref = worker.timer.call_repeatedly(
HEAD:backend/onyx/background/celery/apps/app_base.py:716:            (worker,),
HEAD:backend/onyx/background/celery/apps/app_base.py:720:    def stop(self, worker: Any) -> None:  # noqa: ARG002  # ty: ignore[invalid-method-override]
HEAD:backend/onyx/background/celery/apps/app_base.py:725:    def update_liveness_file(self, worker: Any) -> None:  # noqa: ARG002
HEAD:backend/onyx/background/celery/apps/beat.py:12:from onyx.background.celery.tasks.beat_schedule import CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/onyx/background/celery/apps/beat.py:22:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/beat.py:23:celery_app.config_from_object("onyx.background.celery.configs.beat")
HEAD:backend/onyx/background/celery/apps/beat.py:91:                "onyx.background.celery.tasks.beat_schedule",
HEAD:backend/onyx/background/celery/apps/beat.py:117:            "onyx.background.celery.tasks.beat_schedule", "get_tasks_to_schedule"
HEAD:backend/onyx/background/celery/apps/beat.py:275:celery_app.conf.beat_scheduler = DynamicTenantScheduler
HEAD:backend/onyx/background/celery/apps/beat.py:276:celery_app.conf.task_default_base = app_base.TenantAwareTask
HEAD:backend/onyx/background/celery/apps/client.py:5:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/client.py:6:celery_app.config_from_object("onyx.background.celery.configs.client")
HEAD:backend/onyx/background/celery/apps/client.py:7:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/docfetching.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/docfetching.py:7:    worker_init,
HEAD:backend/onyx/background/celery/apps/docfetching.py:8:    worker_ready,
HEAD:backend/onyx/background/celery/apps/docfetching.py:9:    worker_shutdown,
HEAD:backend/onyx/background/celery/apps/docfetching.py:10:    worker_shutting_down,
HEAD:backend/onyx/background/celery/apps/docfetching.py:14:from onyx.background.celery.tasks.docfetching.worker_shutdown import (
HEAD:backend/onyx/background/celery/apps/docfetching.py:15:    signal_worker_shutting_down,
HEAD:backend/onyx/background/celery/apps/docfetching.py:17:from onyx.configs.constants import POSTGRES_CELERY_WORKER_DOCFETCHING_APP_NAME
HEAD:backend/onyx/background/celery/apps/docfetching.py:36:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/docfetching.py:37:celery_app.config_from_object("onyx.background.celery.configs.docfetching")
HEAD:backend/onyx/background/celery/apps/docfetching.py:38:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/docfetching.py:41:@signals.task_prerun.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:55:@signals.task_postrun.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:71:@signals.task_retry.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:83:@signals.task_revoked.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:89:@signals.task_rejected.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:108:@worker_init.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:109:def on_worker_init(sender: Worker, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docfetching.py:110:    logger.info("worker_init signal received.")
HEAD:backend/onyx/background/celery/apps/docfetching.py:112:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_DOCFETCHING_APP_NAME)
HEAD:backend/onyx/background/celery/apps/docfetching.py:124:    app_base.on_secondary_worker_init(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/docfetching.py:127:@worker_ready.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:128:def on_worker_ready(sender: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docfetching.py:130:    app_base.on_worker_ready(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/docfetching.py:133:@worker_shutting_down.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:134:def on_worker_shutting_down(**kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/docfetching.py:138:        "worker_shutting_down received, flagging docfetching for graceful interrupt."
HEAD:backend/onyx/background/celery/apps/docfetching.py:140:    signal_worker_shutting_down()
HEAD:backend/onyx/background/celery/apps/docfetching.py:143:@worker_shutdown.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:144:def on_worker_shutdown(sender: Any, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docfetching.py:145:    app_base.on_worker_shutdown(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/docfetching.py:157:    celery_app.steps["worker"].add(bootstep)
HEAD:backend/onyx/background/celery/apps/docfetching.py:159:celery_app.autodiscover_tasks(
HEAD:backend/onyx/background/celery/apps/docprocessing.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/docprocessing.py:7:    worker_init,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:8:    worker_process_init,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:9:    worker_ready,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:10:    worker_shutdown,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:18:from onyx.configs.constants import POSTGRES_CELERY_WORKER_DOCPROCESSING_APP_NAME
HEAD:backend/onyx/background/celery/apps/docprocessing.py:37:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:38:celery_app.config_from_object("onyx.background.celery.configs.docprocessing")
HEAD:backend/onyx/background/celery/apps/docprocessing.py:39:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/docprocessing.py:42:@signals.task_prerun.connect
```
Asynchronous/background processing is an observed architectural surface.
Individual queues, task ownership and privilege boundaries remain to be
mapped.
## Model Service Evidence
Evidence lines captured: 300
### Model Dockerfile
```text
# Registry prefix for the base images below. Defaults to Docker Hub; CI overrides it to
# the ECR pull-through cache to dodge rate limits. It only applies to the default images
# -- the DHI overrides below carry their own registry (dhi.io), which the cache does not serve.
ARG BASE_IMAGE_REGISTRY=docker.io

# Python bases. The defaults are the public slim images, so a plain `docker build` needs no
# extra registry access. CI overrides both with the matching Docker Hardened Images from
# dhi.io, which need a Docker account with DHI catalog access.
# Refresh a digest with: docker buildx imagetools inspect <image reference>
ARG PYTHON_BUILDER_IMAGE=${BASE_IMAGE_REGISTRY}/library/python:3.13-slim@sha256:9d2e5553305c7c7b0097999bb17187c69b921ccd6bc9d40e4bb5ebe652c00285
ARG PYTHON_RUNTIME_IMAGE=${BASE_IMAGE_REGISTRY}/library/python:3.13-slim@sha256:9d2e5553305c7c7b0097999bb17187c69b921ccd6bc9d40e4bb5ebe652c00285

# Build stage. Needs a root user plus a shell and build tooling to install the wheels,
# which both the default slim image and the DHI "-dev" variant provide.
FROM ${PYTHON_BUILDER_IMAGE} AS builder

ENV ONYX_RUNNING_IN_DOCKER="true" \
    HF_HOME=/app/.cache/huggingface \
    VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON_PREFERENCE=only-system

COPY --from=ghcr.io/astral-sh/uv:0.11.25@sha256:1e3808aa9023d0980e7c15b1fa7c1ac16ff35925780cf5c459858b2d693f01a9 /uv /uvx /bin/

# Install into a self-contained venv rather than the system site-packages. The
# venv lives at a fixed path we control (/app/.venv), so the runtime stage can
# copy it wholesale without depending on the base image's Python layout.
RUN uv venv /app/.venv --python 3.13

# Pre-create the runtime writable dirs here (the DHI runtime has no shell
# to mkdir). Left empty in this stage; the model download happens downstream.
RUN mkdir -p /app/.cache/huggingface /var/log/onyx

# Recreate the `onyx` user (UID 1001) from the previous image so deployments that
# pin `-u onyx` / `user: onyx` keep resolving and their 1001-owned volumes stay
# writable. The DHI "-dev" image ships a shell but not the `shadow` tools
# (groupadd/useradd), so write the passwd/group entries directly; they're copied
# into the runtime stage below.
RUN printf 'onyx:x:1001:\n' >> /etc/group && \
    printf 'onyx:x:1001:1001::/home/onyx:/usr/sbin/nologin\n' >> /etc/passwd

COPY ./requirements/model_server.txt /tmp/requirements.txt

# Install torch + CUDA/GPU deps in a dedicated layer: together they are ~3GB,
# and isolating them avoids a single oversized layer that is unreliable to push.
# awk extracts each matching package block in full — the package line plus its
# `--hash=...` continuation lines — so --require-hashes can verify them.
RUN awk '/^[[:alnum:]]/ { keep = ($0 ~ /^(torch|nvidia-[a-z0-9-]+|triton)==/) } keep' /tmp/requirements.txt \
        | uv pip install --python /app/.venv/bin/python --no-cache-dir --no-deps --require-hashes -r /dev/stdin && \
    rm -rf ~/.cache/uv

# TODO: drop --no-deps once we upgrade to a litellm version with looser dependencies.
RUN uv pip install --python /app/.venv/bin/python --no-cache-dir --no-deps --require-hashes \
        -r /tmp/requirements.txt && \
    rm -rf ~/.cache/uv /tmp/*.txt

# Cache the embedding model's weights, tokenizer, and metadata in the image.
FROM builder AS embedding-models
RUN python -c "from sentence_transformers import SentenceTransformer; \
SentenceTransformer(model_name_or_path='nomic-ai/nomic-embed-text-v1', trust_remote_code=False);"

# Runtime stage. We run as the `onyx` user (UID 1001, carried over from the previous
# image; see USER below) and chown everything the runtime writes to it. The DHI runtime
# variant is near-distroless: no shell or package manager, so keep this stage free of
# RUN instructions.
FROM ${PYTHON_RUNTIME_IMAGE} AS final

LABEL com.danswer.maintainer="founders@onyx.app"
LABEL com.danswer.description="This image is for the Onyx model server which runs all of the \
AI models for Onyx. This container and all the code is MIT Licensed and free for all to use. \
You can find it at https://hub.docker.com/r/onyx/onyx-model-server. For more details, \
visit https://github.com/onyx-dot-app/onyx."

WORKDIR /app

ENV ONYX_RUNNING_IN_DOCKER="true" \
    HF_HOME=/app/.cache/huggingface \
    HOME=/app/.cache/huggingface \
    PYTHONPATH=/app \
    VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

# Bring the `onyx` user (1001) into the runtime stage. The -dev builder's
# passwd/group are a superset of the runtime's, so copying them preserves the
# base's own entries while adding `onyx`, letting `USER onyx` and any runtime
# `-u onyx` override resolve the name.
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group

# Installed dependencies (the venv) plus the writable runtime dirs, owned by the
# onyx UID (1001) so the process can write the HF cache and logs. When users mount
# named volumes over these paths, the volume seeds with the same ownership.
COPY --from=builder --chown=1001:1001 /app/.venv /app/.venv
COPY --from=builder --chown=1001:1001 /app/.cache/huggingface /app/.cache/huggingface
COPY --from=builder --chown=1001:1001 /var/log/onyx /var/log/onyx

# In case the user has volumes mounted to /app/.cache/huggingface that they've downloaded while
# running Onyx, move the current contents of the cache folder to a temporary location to ensure
# it's preserved in order to combine with the user's cache contents
COPY --chown=1001:1001 --from=embedding-models /app/.cache/huggingface /app/.cache/temp_huggingface

# Utils used by model server
COPY --chown=1001:1001 ./onyx/utils/logger.py /app/onyx/utils/logger.py
COPY --chown=1001:1001 ./onyx/utils/platform_utils.py /app/onyx/utils/platform_utils.py
COPY --chown=1001:1001 ./onyx/utils/middleware.py /app/onyx/utils/middleware.py
COPY --chown=1001:1001 ./onyx/utils/tenant.py /app/onyx/utils/tenant.py

# Sentry configuration (used when SENTRY_DSN is set)
COPY --chown=1001:1001 ./onyx/configs/__init__.py /app/onyx/configs/__init__.py
COPY --chown=1001:1001 ./onyx/configs/sentry.py /app/onyx/configs/sentry.py

# Place to fetch version information
COPY --chown=1001:1001 ./onyx/__init__.py /app/onyx/__init__.py

# Shared between Onyx Backend and Model Server
COPY --chown=1001:1001 ./shared_configs /app/shared_configs

# Model Server main code
COPY --chown=1001:1001 ./model_server /app/model_server

# Default ONYX_VERSION, typically overriden during builds by GitHub Actions.
ARG ONYX_VERSION=0.0.0-dev
ENV ONYX_VERSION=${ONYX_VERSION}

USER onyx

CMD ["python", "-m", "model_server"]
```
### Model-related Source Evidence
```text
HEAD:backend/model_server/__main__.py:1:"""Process entry point for the model server (`python -m model_server`).
HEAD:backend/model_server/__main__.py:3:The `DISABLE_MODEL_SERVER` gate runs here, ahead of `model_server.main`'s heavy ML
HEAD:backend/model_server/__main__.py:10:from shared_configs.configs import DISABLE_MODEL_SERVER
HEAD:backend/model_server/__main__.py:16:    if DISABLE_MODEL_SERVER:
HEAD:backend/model_server/__main__.py:17:        # The deployment points inference/indexing at an external model server, so this
HEAD:backend/model_server/__main__.py:19:        logger.notice("DISABLE_MODEL_SERVER is set; skipping model server startup.")
HEAD:backend/model_server/__main__.py:23:    from model_server.main import run_server
HEAD:backend/model_server/encoders.py:7:from model_server.utils import simple_log_function_time
HEAD:backend/model_server/encoders.py:11:from shared_configs.model_server_models import Embedding, EmbedRequest, EmbedResponse
HEAD:backend/model_server/encoders.py:24:def get_embedding_model(
HEAD:backend/model_server/encoders.py:49:                normalize_embeddings=False,
HEAD:backend/model_server/encoders.py:82:def _concurrent_embedding(
HEAD:backend/model_server/encoders.py:83:    texts: list[str], model: "SentenceTransformer", normalize_embeddings: bool
HEAD:backend/model_server/encoders.py:85:    """Synchronous wrapper for concurrent_embedding to use with run_in_executor."""
HEAD:backend/model_server/encoders.py:88:            return model.encode(texts, normalize_embeddings=normalize_embeddings)
HEAD:backend/model_server/encoders.py:92:            # concurrent embedding, hence we retry (the specific error is
HEAD:backend/model_server/encoders.py:96:    return model.encode(texts, normalize_embeddings=normalize_embeddings)
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
HEAD:backend/model_server/legacy/README.md:3:We stopped using rerankers because the state of the art rerankers are not significantly better than the biencoders and much worse than LLMs which are also capable of acting on a small set of documents for filtering, reranking, etc.
HEAD:backend/model_server/legacy/custom_models.py:12:# from model_server.constants import MODEL_WARM_UP_STRING
HEAD:backend/model_server/legacy/custom_models.py:13:# from model_server.legacy.onyx_torch_model import ConnectorClassifier
HEAD:backend/model_server/legacy/custom_models.py:14:# from model_server.legacy.onyx_torch_model import HybridClassifier
HEAD:backend/model_server/legacy/custom_models.py:15:# from model_server.utils import simple_log_function_time
HEAD:backend/model_server/legacy/custom_models.py:19:# from shared_configs.configs import INDEXING_ONLY
HEAD:backend/model_server/legacy/custom_models.py:22:# from shared_configs.model_server_models import IntentRequest
HEAD:backend/model_server/legacy/custom_models.py:23:# from shared_configs.model_server_models import IntentResponse
HEAD:backend/model_server/legacy/custom_models.py:32:# INDEXING_INFORMATION_CONTENT_CLASSIFICATION_MAX = 1.0
HEAD:backend/model_server/legacy/custom_models.py:33:# INDEXING_INFORMATION_CONTENT_CLASSIFICATION_MIN = 0.7
HEAD:backend/model_server/legacy/custom_models.py:34:# INDEXING_INFORMATION_CONTENT_CLASSIFICATION_TEMPERATURE = 4.0
HEAD:backend/model_server/legacy/custom_models.py:35:# INDEXING_INFORMATION_CONTENT_CLASSIFICATION_CUTOFF_LENGTH = 10
HEAD:backend/model_server/legacy/custom_models.py:290:# def run_inference(tokens: "BatchEncoding") -> tuple[list[float], list[float]]:
HEAD:backend/model_server/legacy/custom_models.py:313:# def run_content_classification_inference(
HEAD:backend/model_server/legacy/custom_models.py:319:#     In the code outside of the model/inference model servers that score will be converted into the actual
HEAD:backend/model_server/legacy/custom_models.py:336:#             INDEXING_INFORMATION_CONTENT_CLASSIFICATION_MIN
HEAD:backend/model_server/legacy/custom_models.py:338:#                 INDEXING_INFORMATION_CONTENT_CLASSIFICATION_MAX
HEAD:backend/model_server/legacy/custom_models.py:339:#                 - INDEXING_INFORMATION_CONTENT_CLASSIFICATION_MIN
HEAD:backend/model_server/legacy/custom_models.py:370:#                 <= INDEXING_INFORMATION_CONTENT_CLASSIFICATION_CUTOFF_LENGTH
HEAD:backend/model_server/legacy/custom_models.py:401:#         logit / INDEXING_INFORMATION_CONTENT_CLASSIFICATION_TEMPERATURE
HEAD:backend/model_server/legacy/custom_models.py:520:#     intent_probs, token_probs = run_inference(model_input)
HEAD:backend/model_server/legacy/custom_models.py:546:#     if INDEXING_ONLY:
HEAD:backend/model_server/legacy/custom_models.py:548:#             "Indexing model server should not call connector classification endpoint"
HEAD:backend/model_server/legacy/custom_models.py:562:#     if INDEXING_ONLY:
HEAD:backend/model_server/legacy/custom_models.py:563:#         raise RuntimeError("Indexing model server should not call intent endpoint")
HEAD:backend/model_server/legacy/custom_models.py:573:#     return run_content_classification_inference(content_classification_requests)
HEAD:backend/model_server/legacy/onyx_torch_model.py:73:#         # Eval doesn't set requires_grad to False, do it manually to save memory and have faster inference
HEAD:backend/model_server/legacy/reranker.py:8:# from model_server.utils import simple_log_function_time
HEAD:backend/model_server/legacy/reranker.py:10:# from shared_configs.configs import INDEXING_ONLY
HEAD:backend/model_server/legacy/reranker.py:11:# from shared_configs.model_server_models import RerankRequest
HEAD:backend/model_server/legacy/reranker.py:12:# from shared_configs.model_server_models import RerankResponse
HEAD:backend/model_server/legacy/reranker.py:21:# _RERANK_MODEL: Optional["CrossEncoder"] = None
HEAD:backend/model_server/legacy/reranker.py:24:# def get_local_reranking_model(
HEAD:backend/model_server/legacy/reranker.py:27:#     global _RERANK_MODEL
HEAD:backend/model_server/legacy/reranker.py:30:#     if _RERANK_MODEL is None:
HEAD:backend/model_server/legacy/reranker.py:33:#         _RERANK_MODEL = model
HEAD:backend/model_server/legacy/reranker.py:34:#     return _RERANK_MODEL
HEAD:backend/model_server/legacy/reranker.py:38:# async def local_rerank(query: str, docs: list[str], model_name: str) -> list[float]:
HEAD:backend/model_server/legacy/reranker.py:39:#     cross_encoder = get_local_reranking_model(model_name)
HEAD:backend/model_server/legacy/reranker.py:40:#     # Run CPU-bound reranking in a thread pool
HEAD:backend/model_server/legacy/reranker.py:48:# async def process_rerank_request(rerank_request: RerankRequest) -> RerankResponse:
HEAD:backend/model_server/legacy/reranker.py:51:#     if rerank_request.provider_type is not None:
HEAD:backend/model_server/legacy/reranker.py:53:#             f"Model server reranking endpoint should only be used for local models. "
HEAD:backend/model_server/legacy/reranker.py:54:#             f"API provider '{rerank_request.provider_type}' should make direct API calls instead."
HEAD:backend/model_server/legacy/reranker.py:57:#     if INDEXING_ONLY:
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
HEAD:backend/model_server/main.py:16:from model_server.ca_certs import configure_trusted_ca_bundle
HEAD:backend/model_server/main.py:17:from model_server.encoders import router as encoders_router
HEAD:backend/model_server/main.py:18:from model_server.management_endpoints import router as management_router
HEAD:backend/model_server/main.py:19:from model_server.utils import get_cgroup_cpu_limit, get_gpu_type
HEAD:backend/model_server/main.py:27:    INDEXING_ONLY,
HEAD:backend/model_server/main.py:29:    MODEL_SERVER_PORT,
HEAD:backend/model_server/main.py:136:    if INDEXING_ONLY:
HEAD:backend/model_server/main.py:154:    # `--host 0.0.0.0`; MODEL_SERVER_HOST is a client-side address and must not
HEAD:backend/model_server/main.py:160:        str(MODEL_SERVER_PORT),
HEAD:backend/model_server/main.py:163:    uvicorn.run(app, host=host, port=MODEL_SERVER_PORT)
HEAD:backend/model_server/management_endpoints.py:3:from model_server.constants import GPUStatus
HEAD:backend/model_server/management_endpoints.py:4:from model_server.utils import get_gpu_type
HEAD:backend/model_server/utils.py:10:from model_server.constants import GPUStatus
HEAD:backend/onyx/access/access.py:93:    # Sometimes the document has not been indexed by the indexing job yet, in those cases
HEAD:backend/onyx/access/access.py:145:def source_should_fetch_permissions_during_indexing(source: DocumentSource) -> bool:
HEAD:backend/onyx/access/access.py:146:    _source_should_fetch_permissions_during_indexing_func = cast(
HEAD:backend/onyx/access/access.py:150:            "source_should_fetch_permissions_during_indexing",
HEAD:backend/onyx/access/access.py:154:    return _source_should_fetch_permissions_during_indexing_func(source)
HEAD:backend/onyx/background/README.md:5:1. Pulling/Indexing documents (from connectors)
HEAD:backend/onyx/background/README.md:7:3. Cleaning up checkpoints and logic around indexing work (indexing indexing checkpoints and index attempt metadata)
HEAD:backend/onyx/background/README.md:57:| `check_for_indexing`              | 15s       | Scans for connectors needing indexing → dispatches to `DOCFETCHING` queue                  |
HEAD:backend/onyx/background/README.md:62:| `check_for_checkpoint_cleanup`    | 1h        | Cleans up old indexing checkpoints                                                         |
HEAD:backend/onyx/background/README.md:93:Docprocessing and Docfetching are for indexing documents:
HEAD:backend/onyx/background/README.md:96:- Docprocessing retrieves batches, runs the indexing pipeline (chunking, embedding), and indexes into the Document Index
HEAD:backend/onyx/background/celery/apps/app_base.py:39:    ENABLE_OPENSEARCH_INDEXING_FOR_ONYX,
HEAD:backend/onyx/background/celery/apps/app_base.py:154:    # prefixes observed when a pruning task finishes and an indexing task
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
HEAD:backend/onyx/background/celery/apps/primary.py:30:from onyx.db.indexing_coordination import IndexingCoordination
HEAD:backend/onyx/background/celery/apps/primary.py:207:        potentially_orphaned_ids = IndexingCoordination.get_orphaned_index_attempt_ids(
HEAD:backend/onyx/background/celery/apps/primary.py:214:            # handle case where not started or docfetching is done but indexing is not
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
HEAD:backend/onyx/background/celery/memory_monitoring.py:101:    if INDEXING_WORKER_MEMORY_LIMIT_MB <= 0:
HEAD:backend/onyx/background/celery/memory_monitoring.py:104:    if INDEXING_WORKER_TRACEMALLOC and not tracemalloc.is_tracing():
HEAD:backend/onyx/background/celery/memory_monitoring.py:127:    report_threshold_mb = int(INDEXING_WORKER_MEMORY_LIMIT_MB * _REPORT_FRACTION)
HEAD:backend/onyx/background/celery/memory_monitoring.py:143:        "Indexing worker memory nearing the limit: attempt=%s rss_mb=%s limit_mb=%s",
HEAD:backend/onyx/background/celery/memory_monitoring.py:146:        INDEXING_WORKER_MEMORY_LIMIT_MB,
HEAD:backend/onyx/background/celery/memory_monitoring.py:151:            "tracemalloc is disabled; set INDEXING_WORKER_TRACEMALLOC=true to "
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:12:    ENABLE_OPENSEARCH_INDEXING_FOR_ONYX,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:83:        "name": "check-for-indexing",
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:84:        "task": OnyxCeleryTask.CHECK_FOR_INDEXING,
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:317:    ENABLE_OPENSEARCH_INDEXING_FOR_ONYX
HEAD:backend/onyx/background/celery/tasks/beat_schedule.py:339:    "check-for-indexing",
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:42:    IndexingStatus,
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:101:                and recent_index_attempts[0].status == IndexingStatus.IN_PROGRESS
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:106:                    f"Revoked indexing task {recent_index_attempts[0].celery_task_id}."
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:109:            task_logger.exception("Exception while revoking indexing task")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:271:    Will raise TaskDependencyError if dependent tasks such as indexing and pruning are
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:314:        # do not proceed if connector indexing or connector pruning are running
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:325:                and recent_index_attempts[0].status == IndexingStatus.IN_PROGRESS
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:327:                inc_deletion_blocked(tenant_id, "indexing")
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:329:                    "Connector deletion - Delayed (indexing in progress): "
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:469:                # deletion was in progress. Likely a bug gating off pruning and indexing
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:687:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:688:    This can happen if the indexing worker hard crashes or is terminated.
HEAD:backend/onyx/background/celery/tasks/connector_deletion/tasks.py:699:    2.2. The indexing watchdog checks the spawned task.
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:16:from onyx.db.indexing_coordination import IndexingCoordination
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:30:    """Checks for any conditions that should block the indexing task from being
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:34:    is used to trigger indexing immediately.
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:41:    # we need to serialize any attempt to trigger indexing since it can be triggered
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:44:        DANSWER_REDIS_FUNCTION_LOCK_PREFIX + "try_creating_indexing_task",
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:64:        index_attempt_id = IndexingCoordination.try_create_index_attempt(
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:73:            # Another indexing attempt is already running
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:76:        # Use higher priority for first-time indexing to ensure new connectors
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:77:        # get processed before re-indexing of existing connectors
HEAD:backend/onyx/background/celery/tasks/docfetching/task_creation_utils.py:113:            f"try_creating_indexing_task - Unexpected exception: cc_pair={cc_pair.id} search_settings={search_settings.id}"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:23:from onyx.background.celery.tasks.docprocessing.tasks import ConnectorIndexingLogBuilder
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:24:from onyx.background.celery.tasks.docprocessing.utils import IndexingCallback
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:27:    IndexingWatchdogTerminalStatus,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:30:from onyx.background.indexing.job_client import (
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:35:from onyx.background.indexing.run_docfetching import run_docfetching_entrypoint
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:36:from onyx.configs.app_configs import INDEXING_WORKER_MEMORY_LIMIT_MB
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:38:    CELERY_INDEXING_WATCHDOG_CONNECTOR_TIMEOUT,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:39:    CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:45:from onyx.db.enums import IndexingStatus
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:52:from onyx.db.indexing_coordination import IndexingCoordination
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:63:def _verify_indexing_attempt(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:69:    Verify that the indexing attempt exists and is in the correct state.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:78:                code=IndexingWatchdogTerminalStatus.FENCE_NOT_FOUND.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:84:                code=IndexingWatchdogTerminalStatus.FENCE_MISMATCH.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:90:                code=IndexingWatchdogTerminalStatus.FENCE_MISMATCH.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:94:            IndexingStatus.NOT_STARTED,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:95:            IndexingStatus.IN_PROGRESS,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:99:                code=IndexingWatchdogTerminalStatus.FENCE_MISMATCH.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:103:        if IndexingCoordination.check_cancellation_requested(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:108:                code=IndexingWatchdogTerminalStatus.BLOCKED_BY_STOP_SIGNAL.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:129:    some stuff, but basically it just calls run_indexing_entrypoint.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:133:    This will cause the primary worker to abort the indexing attempt and clean up.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:136:    # Start heartbeat for this indexing attempt
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:157:    # Since connector_indexing_proxy_task spawns a new process using this function as
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:167:        "Indexing spawned task starting: attempt=%s tenant=%s cc_pair=%s search_settings=%s",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:179:            f"Indexing will not start because connector deletion is in progress: "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:183:            code=IndexingWatchdogTerminalStatus.BLOCKED_BY_DELETION.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:188:            f"Indexing will not start because a connector stop signal was detected: "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:192:            code=IndexingWatchdogTerminalStatus.BLOCKED_BY_STOP_SIGNAL.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:195:    # Verify the indexing attempt exists and is valid
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:197:    _verify_indexing_attempt(index_attempt_id, cc_pair_id, search_settings_id)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:205:                    code=IndexingWatchdogTerminalStatus.INDEX_ATTEMPT_MISMATCH.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:216:                    code=IndexingWatchdogTerminalStatus.INDEX_ATTEMPT_MISMATCH.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:220:        callback = IndexingCallback(
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:225:            "Indexing spawned task running entrypoint: attempt=%s tenant=%s cc_pair=%s search_settings=%s",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:244:            f"Indexing task failed: attempt={index_attempt_id} "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:248:            code=IndexingWatchdogTerminalStatus.CONNECTOR_VALIDATION_ERROR.code,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:253:            "Indexing spawned task failed: attempt=%s tenant=%s cc_pair=%s search_settings=%s",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:271:        "Indexing spawned task finished: attempt=%s cc_pair=%s search_settings=%s",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:285:    log_builder: ConnectorIndexingLogBuilder,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:294:        result.status = IndexingWatchdogTerminalStatus.SUCCEEDED
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:309:        result.status = IndexingWatchdogTerminalStatus.SUCCEEDED
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:312:                "Indexing watchdog - spawned task has non-zero exit code but completion signal is OK. Continuing...",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:318:            result.status = IndexingWatchdogTerminalStatus.from_code(result.exit_code)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:340:    This task is the entrypoint for the full indexing pipeline, which is composed of two tasks:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:342:    This task is spawned by "try_creating_indexing_task" which is called in the "check_for_indexing" task.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:347:    1)  determines parameters of the indexing attempt (which connector indexing function to run,
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:360:    6) update document and indexing metadata in postgres
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:366:    - docfetching proxy tasks are spawned by check_for_indexing. The proxy then runs the docfetching_task wrapped in a watchdog.
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:375:    How we deal with failures/ partial indexing:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:381:    - Heartbeat spawned in docfetching and docprocessing is how check_for_indexing monitors liveliness
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:415:    log_builder = ConnectorIndexingLogBuilder(ctx)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:419:            "Indexing watchdog - starting",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:441:        result.status = IndexingWatchdogTerminalStatus.SPAWN_FAILED
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:444:                "Indexing watchdog - finished",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:455:            result.status = IndexingWatchdogTerminalStatus.SPAWN_NOT_ALIVE
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:458:                    "Indexing watchdog - finished",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:474:            "Indexing watchdog - spawn succeeded",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:518:                    IndexingWatchdogTerminalStatus.TERMINATED_BY_WORKER_SHUTDOWN
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:527:                                "Indexing worker shutting down (deploy or "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:534:                            "Indexing watchdog - transient exception marking index "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:540:                        CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:545:                            "Indexing watchdog - exception while terminating "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:562:                            "Indexing watchdog - spawned task exceptioned"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:577:                        "indexing_worker",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:591:                if INDEXING_WORKER_MEMORY_LIMIT_MB > 0:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:599:                    if rss_mb is not None and rss_mb > INDEXING_WORKER_MEMORY_LIMIT_MB:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:602:                                "Indexing watchdog - memory limit exceeded; "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:605:                                limit_mb=str(INDEXING_WORKER_MEMORY_LIMIT_MB),
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:610:                            IndexingWatchdogTerminalStatus.TERMINATED_BY_MEMORY_LIMIT
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:613:                            "Indexing worker exceeded the memory limit while "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:615:                            f"limit_mb={INDEXING_WORKER_MEMORY_LIMIT_MB}. "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:632:                                    "Indexing watchdog - transient exception marking "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:639:                                CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:644:                                    "Indexing watchdog - exception while terminating "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:672:                        "Indexing watchdog - transient exception looking up index attempt"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:679:                    "Indexing watchdog - IndexAttempt reached terminal status while "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:686:                IndexingWatchdogTerminalStatus.TERMINATED_BY_ATTEMPT_FINALIZED
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:689:                job.terminate_and_wait(CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:693:                        "Indexing watchdog - exception while terminating subprocess "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:702:        result.status = IndexingWatchdogTerminalStatus.WATCHDOG_EXCEPTIONED
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:732:                    "Indexing watchdog - transient exception marking index attempt as failed"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:744:                "Indexing watchdog - finished",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:755:    if result.status == IndexingWatchdogTerminalStatus.TERMINATED_BY_SIGNAL:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:770:                    "Indexing watchdog - transient exception marking index attempt as canceled"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:774:        job.terminate_and_wait(CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:775:    elif result.status == IndexingWatchdogTerminalStatus.TERMINATED_BY_ACTIVITY_TIMEOUT:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:781:                    "Indexing watchdog - activity timeout exceeded: "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:783:                    f"timeout={CELERY_INDEXING_WATCHDOG_CONNECTOR_TIMEOUT}s",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:788:                    "Indexing watchdog - transient exception marking index attempt as failed"
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:791:        job.terminate_and_wait(CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS)
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:793:        result.status == IndexingWatchdogTerminalStatus.TERMINATED_BY_ATTEMPT_FINALIZED
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:801:    elif result.status == IndexingWatchdogTerminalStatus.TERMINATED_BY_WORKER_SHUTDOWN:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:805:    elif result.status == IndexingWatchdogTerminalStatus.TERMINATED_BY_MEMORY_LIMIT:
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:818:                        or "Indexing worker exceeded the memory limit",
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:823:                    "Indexing watchdog - transient exception marking index attempt "
HEAD:backend/onyx/background/celery/tasks/docfetching/tasks.py:832:            "Indexing watchdog - finished",
HEAD:backend/onyx/background/celery/tasks/docfetching/worker_shutdown.py:3:The ``worker_shutting_down`` handler sets it on SIGTERM. The indexing watchdog
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:6:from onyx.configs.constants import INDEXING_WORKER_HEARTBEAT_INTERVAL
HEAD:backend/onyx/background/celery/tasks/docprocessing/heartbeat.py:19:        while not stop_event.wait(INDEXING_WORKER_HEARTBEAT_INTERVAL):
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:6:connector invocation + indexing pipeline plumbing live in
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:7:`onyx.background.indexing.run_targeted_reindex`.
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:18:from onyx.db.enums import IndexingStatus
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:38:    from onyx.background.indexing.run_targeted_reindex import (
HEAD:backend/onyx/background/celery/tasks/docprocessing/targeted_reindex_task.py:65:            attempt.status = IndexingStatus.IN_PROGRESS
```
Model-serving/indexing roles are present as source/deployment candidates.
Their precise data inputs, trust assumptions and call paths are not yet
runtime verified.
## MCP Component Evidence
Evidence lines captured: 300
### MCP README
```text
# Onyx MCP Server

## Overview

The Onyx MCP server allows LLMs to connect to your Onyx instance and access its knowledge base and search capabilities through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).

With the Onyx MCP Server, you can search your knowledgebase and
give your LLMs web search.

All access controls are managed within the main Onyx application.

### Authentication

Provide an Onyx Personal Access Token or API Key in the `Authorization` header as a Bearer token.
The MCP server quickly validates and passes through the token on every request.

A token scoped to `read:search` covers the document-search tool, including the listings of indexed
sources and document sets that a search may be filtered by. Add
`read:chat` or `write:chat` only if the client needs the chat surfaces. An unscoped token carries
the user's full access, so prefer a scoped one.

Depending on usage, the MCP Server may support OAuth and stdio in the future.

### Default Configuration
- **Transport**: HTTP POST (MCP over HTTP)
- **Port**: 8090 (shares domain with API server)
- **Framework**: FastMCP with FastAPI wrapper
- **Database**: None (all work delegates to the API server)

### Architecture

The MCP server is built on [FastMCP](https://github.com/jlowin/fastmcp) and runs alongside the main Onyx API server:

```
┌─────────────────┐
│  LLM Client     │
│  (Claude, etc)  │
└────────┬────────┘
         │ MCP over HTTP
         │ (POST with bearer)
         ▼
┌─────────────────┐
│  MCP Server     │
│  Port 8090      │
│  ├─ Auth        │
│  ├─ Tools       │
│  └─ Resources   │
└────────┬────────┘
         │ Internal HTTP
         │ (authenticated)
         ▼
┌─────────────────┐
│  API Server     │
│  Port 8080      │
│  ├─ /me (auth)  │
│  ├─ Search APIs │
│  └─ ACL checks  │
└─────────────────┘
```

## Configuring MCP Clients

### Claude Desktop

Add to your Claude Desktop configuration (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "onyx": {
      "url": "https://[YOUR_ONYX_DOMAIN]:8090/",
      "transport": "http",
      "headers": {
        "Authorization": "Bearer YOUR_ONYX_TOKEN_HERE"
      }
    }
  }
}
```

### Other MCP Clients

Most MCP clients support HTTP transport with custom headers. Refer to your client's documentation for configuration details.

## Capabilities

### Tools

The server provides three tools for searching and retrieving information:

1. `search_indexed_documents`
Search the user's private knowledge base indexed in Onyx. Returns ranked documents with content snippets, scores, and metadata.

Pass `agent` with an agent name to run the search as that Onyx agent. The search then applies the agent's knowledge scope (document sets, attached documents, start date) and its configured model. An unresolvable name returns an error listing the agents available to the user, so no lookup call is needed first.

`agent` and `document_set_names` are mutually exclusive. Explicit document sets replace an agent's knowledge scope rather than narrowing it, so passing both is rejected instead of silently returning out-of-scope results.

Filter values resolve on the search call, so clients do not need a lookup call first. `agent`, `source_types` and `document_set_names` are all validated: a value that does not resolve returns an error naming close matches, or the available values when there are few of them, rather than being dropped. A dropped filter would return a wider result set that looks correctly scoped, so these fail instead.

2. `search_web`
Search the public internet for current events and general knowledge. Returns web search results with titles, URLs, and snippets.

3. `open_urls`
Retrieve the complete text content from specific web URLs. Useful for fetching full page content after finding relevant URLs via `search_web`.

### Resources

1. `indexed_sources`
Lists all document sources currently indexed in the tenant (e.g., `"confluence"`, `"github"`). Use these values to filter results when calling `search_indexed_documents`.

2. `document_sets`
Lists the Document Sets accessible to the user. Use the returned `name` values with the `document_set_names` filter of `search_indexed_documents`.

3. `agents`
Lists the Onyx agents accessible to the user (`id`, `name`, `description`). Use a returned `name` with the `agent` filter of `search_indexed_documents`.

## Local Development

### Running the MCP Server

The MCP Server automatically launches with the `Run All Onyx Services` task from the default launch.json.

You can also independently launch the Server via the vscode debugger.

### Testing with MCP Inspector

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is a debugging tool for MCP servers:

```bash
npx @modelcontextprotocol/inspector http://localhost:8090/
```

**Setup in Inspector:**

1. Ignore the OAuth configuration menus
2. Open the **Authentication** tab
3. Select **Bearer Token** authentication
4. Paste your Onyx bearer token
5. Click **Connect**

Once connected, you can:
- Browse available tools
- Test tool calls with different parameters
- View request/response payloads
- Debug authentication issues

### Health Check

Verify the server is running:

```bash
curl http://localhost:8090/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "mcp_server"
}
```

### Environment Variables

**MCP Server Configuration:**
- `MCP_SERVER_ENABLED`: Enable MCP server (set to "true" to enable, default: disabled)
- `MCP_SERVER_PORT`: Port for MCP server (default: 8090)
- `MCP_SERVER_CORS_ORIGINS`: Comma-separated CORS origins (optional)

**API Server Connection:**
- `API_SERVER_PROTOCOL`: Protocol for API server connection (default: "http")
- `API_SERVER_HOST`: Hostname for API server connection (default: "127.0.0.1")
- `API_SERVER_URL_OVERRIDE_FOR_HTTP_REQUESTS`: Optional override URL. If set, takes precedence over the protocol/host variables. Used for self-hosting the MCP server with Onyx Cloud as the backend.
```
### MCP Source / Deployment Evidence
```text
HEAD:backend/onyx/mcp_server/README.md:1:# Onyx MCP Server
HEAD:backend/onyx/mcp_server/README.md:5:The Onyx MCP server allows LLMs to connect to your Onyx instance and access its knowledge base and search capabilities through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).
HEAD:backend/onyx/mcp_server/README.md:7:With the Onyx MCP Server, you can search your knowledgebase and
HEAD:backend/onyx/mcp_server/README.md:14:Provide an Onyx Personal Access Token or API Key in the `Authorization` header as a Bearer token.
HEAD:backend/onyx/mcp_server/README.md:15:The MCP server quickly validates and passes through the token on every request.
HEAD:backend/onyx/mcp_server/README.md:22:Depending on usage, the MCP Server may support OAuth and stdio in the future.
HEAD:backend/onyx/mcp_server/README.md:25:- **Transport**: HTTP POST (MCP over HTTP)
HEAD:backend/onyx/mcp_server/README.md:27:- **Framework**: FastMCP with FastAPI wrapper
HEAD:backend/onyx/mcp_server/README.md:32:The MCP server is built on [FastMCP](https://github.com/jlowin/fastmcp) and runs alongside the main Onyx API server:
HEAD:backend/onyx/mcp_server/README.md:39:         │ MCP over HTTP
HEAD:backend/onyx/mcp_server/README.md:43:│  MCP Server     │
HEAD:backend/onyx/mcp_server/README.md:61:## Configuring MCP Clients
HEAD:backend/onyx/mcp_server/README.md:69:  "mcpServers": {
HEAD:backend/onyx/mcp_server/README.md:81:### Other MCP Clients
HEAD:backend/onyx/mcp_server/README.md:83:Most MCP clients support HTTP transport with custom headers. Refer to your client's documentation for configuration details.
HEAD:backend/onyx/mcp_server/README.md:119:### Running the MCP Server
HEAD:backend/onyx/mcp_server/README.md:121:The MCP Server automatically launches with the `Run All Onyx Services` task from the default launch.json.
HEAD:backend/onyx/mcp_server/README.md:125:### Testing with MCP Inspector
HEAD:backend/onyx/mcp_server/README.md:127:The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is a debugging tool for MCP servers:
HEAD:backend/onyx/mcp_server/README.md:135:1. Ignore the OAuth configuration menus
HEAD:backend/onyx/mcp_server/README.md:159:  "service": "mcp_server"
HEAD:backend/onyx/mcp_server/README.md:165:**MCP Server Configuration:**
HEAD:backend/onyx/mcp_server/README.md:166:- `MCP_SERVER_ENABLED`: Enable MCP server (set to "true" to enable, default: disabled)
HEAD:backend/onyx/mcp_server/README.md:167:- `MCP_SERVER_PORT`: Port for MCP server (default: 8090)
HEAD:backend/onyx/mcp_server/README.md:168:- `MCP_SERVER_CORS_ORIGINS`: Comma-separated CORS origins (optional)
HEAD:backend/onyx/mcp_server/README.md:173:- `API_SERVER_URL_OVERRIDE_FOR_HTTP_REQUESTS`: Optional override URL. If set, takes precedence over the protocol/host variables. Used for self-hosting the MCP server with Onyx Cloud as the backend.
HEAD:backend/onyx/mcp_server/api.py:1:"""MCP server with FastAPI wrapper."""
HEAD:backend/onyx/mcp_server/api.py:9:from fastmcp import FastMCP
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
HEAD:backend/onyx/mcp_server/api.py:48:def create_mcp_fastapi_app() -> FastAPI:
HEAD:backend/onyx/mcp_server/api.py:49:    """Create FastAPI app wrapping MCP server with auth and shared client lifecycle."""
HEAD:backend/onyx/mcp_server/api.py:50:    mcp_asgi_app = mcp_server.http_app(path="/")
HEAD:backend/onyx/mcp_server/api.py:55:        """Ensure Accept header includes types required by FastMCP streamable HTTP."""
HEAD:backend/onyx/mcp_server/api.py:69:        await mcp_asgi_app(scope, receive, send)
HEAD:backend/onyx/mcp_server/api.py:73:        """Initializes MCP session manager."""
HEAD:backend/onyx/mcp_server/api.py:74:        logger.info("MCP server starting up")
HEAD:backend/onyx/mcp_server/api.py:77:            async with mcp_asgi_app.lifespan(app):
HEAD:backend/onyx/mcp_server/api.py:80:            logger.info("MCP server shutting down")
HEAD:backend/onyx/mcp_server/api.py:84:        title="Onyx MCP Server",
HEAD:backend/onyx/mcp_server/api.py:91:    # Public health check endpoint (bypasses MCP auth)
HEAD:backend/onyx/mcp_server/api.py:97:            return JSONResponse({"status": "healthy", "service": "mcp_server"})
HEAD:backend/onyx/mcp_server/api.py:100:    # Authentication is handled by FastMCP's OnyxTokenVerifier (see auth.py)
HEAD:backend/onyx/mcp_server/api.py:102:    if MCP_SERVER_CORS_ORIGINS:
HEAD:backend/onyx/mcp_server/api.py:103:        logger.info("CORS origins: %s", MCP_SERVER_CORS_ORIGINS)
HEAD:backend/onyx/mcp_server/api.py:106:            allow_origins=MCP_SERVER_CORS_ORIGINS,
HEAD:backend/onyx/mcp_server/api.py:107:            allow_credentials=cors_allow_credentials(MCP_SERVER_CORS_ORIGINS),
HEAD:backend/onyx/mcp_server/api.py:119:mcp_app = create_mcp_fastapi_app()
HEAD:backend/onyx/mcp_server/auth.py:1:"""Authentication helpers for the Onyx MCP server."""
HEAD:backend/onyx/mcp_server/auth.py:5:from fastmcp.server.auth.auth import AccessToken, TokenVerifier
HEAD:backend/onyx/mcp_server/auth.py:7:from onyx.mcp_server.utils import get_http_client
HEAD:backend/onyx/mcp_server/auth.py:8:from onyx.server.metrics.mcp_server import MCPAuthResult, record_mcp_auth_result
HEAD:backend/onyx/mcp_server/auth.py:26:            record_mcp_auth_result(MCPAuthResult.ERROR)
HEAD:backend/onyx/mcp_server/auth.py:28:                "MCP server failed to reach API /me for authentication: %s",
HEAD:backend/onyx/mcp_server/auth.py:35:            record_mcp_auth_result(MCPAuthResult.REJECTED)
HEAD:backend/onyx/mcp_server/auth.py:37:                "API server rejected MCP auth token with status %s",
HEAD:backend/onyx/mcp_server/auth.py:42:        record_mcp_auth_result(MCPAuthResult.SUCCESS)
HEAD:backend/onyx/mcp_server/auth.py:45:            client_id="mcp",
HEAD:backend/onyx/mcp_server/auth.py:46:            scopes=["mcp:use"],
HEAD:backend/onyx/mcp_server/mcp.json.template:2:    "mcpServers": {
HEAD:backend/onyx/mcp_server/mcp.json.template:4:        "url": "https://cloud.onyx.app/mcp",
HEAD:backend/onyx/mcp_server/mcp.json.template:6:          "Authorization": "Bearer [YOUR PAT OR API KEY HERE]"
HEAD:backend/onyx/mcp_server/resources/__init__.py:1:"""Resource registrations for the Onyx MCP server."""
HEAD:backend/onyx/mcp_server/resources/__init__.py:4:from onyx.mcp_server.resources import (
HEAD:backend/onyx/mcp_server/resources/agents.py:7:from onyx.mcp_server.api import mcp_server
HEAD:backend/onyx/mcp_server/resources/agents.py:8:from onyx.mcp_server.utils import get_accessible_agents, require_access_token
HEAD:backend/onyx/mcp_server/resources/agents.py:14:@mcp_server.resource(
HEAD:backend/onyx/mcp_server/resources/agents.py:35:        "Onyx MCP Server: agents resource returning %s entries",
HEAD:backend/onyx/mcp_server/resources/agents.py:39:    # FastMCP 3.2+ requires str/bytes/list[ResourceContent] — it no longer
HEAD:backend/onyx/mcp_server/resources/document_sets.py:7:from onyx.mcp_server.api import mcp_server
HEAD:backend/onyx/mcp_server/resources/document_sets.py:8:from onyx.mcp_server.utils import get_accessible_document_sets, require_access_token
HEAD:backend/onyx/mcp_server/resources/document_sets.py:14:@mcp_server.resource(
HEAD:backend/onyx/mcp_server/resources/document_sets.py:34:        "Onyx MCP Server: document_sets resource returning %s entries",
HEAD:backend/onyx/mcp_server/resources/document_sets.py:38:    # FastMCP 3.2+ requires str/bytes/list[ResourceContent] — it no longer
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:1:"""Resources that expose metadata for the Onyx MCP server."""
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:7:from onyx.mcp_server.api import mcp_server
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:8:from onyx.mcp_server.utils import get_indexed_sources, require_access_token
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:14:@mcp_server.resource(
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:31:        "Onyx MCP Server: indexed_sources resource returning %s entries",
HEAD:backend/onyx/mcp_server/resources/indexed_sources.py:35:    # FastMCP 3.2+ requires str/bytes/list[ResourceContent] — it no longer
HEAD:backend/onyx/mcp_server/tools/__init__.py:1:"""Tool registrations for the Onyx MCP server."""
HEAD:backend/onyx/mcp_server/tools/__init__.py:4:from onyx.mcp_server.tools import search  # noqa: F401
HEAD:backend/onyx/mcp_server/tools/search.py:1:"""Search tools for MCP server - document and web search."""
HEAD:backend/onyx/mcp_server/tools/search.py:10:from fastmcp.server.auth.auth import AccessToken
HEAD:backend/onyx/mcp_server/tools/search.py:13:from onyx.configs.app_configs import MCP_SERVER_API_REQUEST_TIMEOUT_SECONDS
HEAD:backend/onyx/mcp_server/tools/search.py:15:from onyx.mcp_server.api import mcp_server
HEAD:backend/onyx/mcp_server/tools/search.py:16:from onyx.mcp_server.utils import (
HEAD:backend/onyx/mcp_server/tools/search.py:35:from onyx.server.metrics.mcp_common import MCPToolCallStatus
HEAD:backend/onyx/mcp_server/tools/search.py:36:from onyx.server.metrics.mcp_server import (
HEAD:backend/onyx/mcp_server/tools/search.py:38:    MCPServerToolName,
HEAD:backend/onyx/mcp_server/tools/search.py:39:    record_mcp_search_results,
HEAD:backend/onyx/mcp_server/tools/search.py:40:    record_mcp_search_source,
HEAD:backend/onyx/mcp_server/tools/search.py:41:    record_mcp_server_tool_outcome,
HEAD:backend/onyx/mcp_server/tools/search.py:63:            float(MCP_SERVER_API_REQUEST_TIMEOUT_SECONDS), connect=10.0
HEAD:backend/onyx/mcp_server/tools/search.py:68:def _to_mcp_dict(result: SearchResult) -> dict[str, Any]:
HEAD:backend/onyx/mcp_server/tools/search.py:69:    """Convert a search API result into the dict shape MCP clients receive.
HEAD:backend/onyx/mcp_server/tools/search.py:71:    Renames ``link`` → ``url`` to match the conventional shape MCP tools
HEAD:backend/onyx/mcp_server/tools/search.py:72:    typically emit (most search-style MCP tools — Brave, Exa, etc. — use
HEAD:backend/onyx/mcp_server/tools/search.py:95:        logger.debug("Onyx MCP Server: error body was not JSON (%s)", exc)
HEAD:backend/onyx/mcp_server/tools/search.py:100:    """Build the standard MCP error response envelope used by every tool."""
HEAD:backend/onyx/mcp_server/tools/search.py:269:        record_mcp_search_source(source)
HEAD:backend/onyx/mcp_server/tools/search.py:272:@mcp_server.tool()
HEAD:backend/onyx/mcp_server/tools/search.py:334:    tool = MCPServerToolName.SEARCH_INDEXED_DOCUMENTS
HEAD:backend/onyx/mcp_server/tools/search.py:336:        "Onyx MCP Server: document search: query='%s', sources=%s, document_sets=%s, agent=%s",
HEAD:backend/onyx/mcp_server/tools/search.py:352:    # Get authenticated user from FastMCP's access token
HEAD:backend/onyx/mcp_server/tools/search.py:354:    outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/mcp_server/tools/search.py:368:            logger.info("Onyx MCP Server: No indexed sources available for tenant")
HEAD:backend/onyx/mcp_server/tools/search.py:369:            outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/mcp_server/tools/search.py:380:                "Onyx MCP Server: invalid time_cutoff '%s' (%s); continuing without time filter",
HEAD:backend/onyx/mcp_server/tools/search.py:400:        results = [_to_mcp_dict(result) for result in payload.results]
HEAD:backend/onyx/mcp_server/tools/search.py:401:        outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/mcp_server/tools/search.py:404:            "Onyx MCP Server: Internal search returned %s results", len(results)
HEAD:backend/onyx/mcp_server/tools/search.py:408:        logger.error("Onyx MCP Server: Document search error: %s", err, exc_info=True)
HEAD:backend/onyx/mcp_server/tools/search.py:411:        record_mcp_server_tool_outcome(tool, _start, outcome)
HEAD:backend/onyx/mcp_server/tools/search.py:413:            record_mcp_search_results(tool, result_count)
HEAD:backend/onyx/mcp_server/tools/search.py:416:@mcp_server.tool()
HEAD:backend/onyx/mcp_server/tools/search.py:437:    tool = MCPServerToolName.SEARCH_WEB
HEAD:backend/onyx/mcp_server/tools/search.py:438:    logger.info("Onyx MCP Server: Web search: query='%s', limit=%s", query, limit)
HEAD:backend/onyx/mcp_server/tools/search.py:441:    outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/mcp_server/tools/search.py:457:        outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/mcp_server/tools/search.py:464:        logger.error("Onyx MCP Server: Web search error: %s", e, exc_info=True)
HEAD:backend/onyx/mcp_server/tools/search.py:471:        record_mcp_server_tool_outcome(tool, _start, outcome)
HEAD:backend/onyx/mcp_server/tools/search.py:473:            record_mcp_search_results(tool, result_count)
HEAD:backend/onyx/mcp_server/tools/search.py:476:@mcp_server.tool()
HEAD:backend/onyx/mcp_server/tools/search.py:497:    tool = MCPServerToolName.OPEN_URLS
HEAD:backend/onyx/mcp_server/tools/search.py:498:    logger.info("Onyx MCP Server: Open URL: fetching %s URLs", len(urls))
HEAD:backend/onyx/mcp_server/tools/search.py:501:    outcome = MCPToolCallStatus.ERROR
HEAD:backend/onyx/mcp_server/tools/search.py:512:        outcome = MCPToolCallStatus.SUCCESS
HEAD:backend/onyx/mcp_server/tools/search.py:517:        logger.error("Onyx MCP Server: URL fetch error: %s", err, exc_info=True)
HEAD:backend/onyx/mcp_server/tools/search.py:520:        record_mcp_server_tool_outcome(tool, _start, outcome)
HEAD:backend/onyx/mcp_server/utils.py:1:"""Utility helpers for the Onyx MCP server."""
HEAD:backend/onyx/mcp_server/utils.py:6:from fastmcp.server.auth.auth import AccessToken
HEAD:backend/onyx/mcp_server/utils.py:7:from fastmcp.server.dependencies import get_access_token
HEAD:backend/onyx/mcp_server/utils.py:15:    """Minimal document-set shape surfaced to MCP clients.
HEAD:backend/onyx/mcp_server/utils.py:17:    Projected from the backend's DocumentSetSummary to avoid coupling MCP to
HEAD:backend/onyx/mcp_server/utils.py:26:    """Minimal agent (persona) shape surfaced to MCP clients.
HEAD:backend/onyx/mcp_server/utils.py:28:    Projected from the backend's MinimalPersonaSnapshot to keep MCP decoupled
HEAD:backend/onyx/mcp_server/utils.py:56:            "MCP Server requires an Onyx access token to authenticate your request"
HEAD:backend/onyx/mcp_server/utils.py:101:            "Onyx MCP Server: Failed to fetch indexed sources",
HEAD:backend/onyx/mcp_server/utils.py:108:            "Onyx MCP Server: Unexpected error fetching indexed sources",
HEAD:backend/onyx/mcp_server/utils.py:131:            "Onyx MCP Server: Failed to fetch document sets",
HEAD:backend/onyx/mcp_server/utils.py:137:            "Onyx MCP Server: Unexpected error fetching document sets",
HEAD:backend/onyx/mcp_server/utils.py:160:            "Onyx MCP Server: Failed to fetch agents",
HEAD:backend/onyx/mcp_server/utils.py:166:            "Onyx MCP Server: Unexpected error fetching agents",
HEAD:deployment/docker_compose/docker-compose.dev.yml:50:  # Uncomment the block below to enable the MCP server for Onyx.
HEAD:deployment/docker_compose/docker-compose.dev.yml:51:  # mcp_server:
HEAD:deployment/docker_compose/docker-compose.mcp-api-key-test.yml:4:  mcp_api_key_server:
HEAD:deployment/docker_compose/docker-compose.mcp-api-key-test.yml:9:      - MCP_API_KEY_TEST_PORT=${MCP_API_KEY_TEST_PORT:-8005}
HEAD:deployment/docker_compose/docker-compose.mcp-api-key-test.yml:10:      - MCP_API_KEY=${MCP_API_KEY:-test-api-key-12345}
HEAD:deployment/docker_compose/docker-compose.mcp-api-key-test.yml:11:      - MCP_SERVER_HOST=${MCP_API_KEY_SERVER_HOST:-0.0.0.0}
HEAD:deployment/docker_compose/docker-compose.mcp-api-key-test.yml:12:      - MCP_SERVER_PUBLIC_HOST=${MCP_API_KEY_SERVER_PUBLIC_HOST:-host.docker.internal}
HEAD:deployment/docker_compose/docker-compose.mcp-api-key-test.yml:15:      python backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_api_key.py ${MCP_API_KEY:-test-api-key-12345} ${MCP_API_KEY_TEST_PORT:-8005}
HEAD:deployment/docker_compose/docker-compose.mcp-api-key-test.yml:18:      - "${MCP_API_KEY_TEST_PORT:-8005}:${MCP_API_KEY_TEST_PORT:-8005}"
HEAD:deployment/docker_compose/docker-compose.mcp-api-key-test.yml:27:          "import os, urllib.request; urllib.request.urlopen(f\"http://127.0.0.1:{os.environ['MCP_API_KEY_TEST_PORT']}/healthz\")",
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:4:  # Self-hosted mock OIDC / OAuth2 authorization server. Replaces the real Okta
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:5:  # org the OAuth tests used to depend on: no secrets, no hosted login page
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:7:  # is served at /jwks so the mcp_oauth_server's JWTVerifier accepts them. The
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:18:      - MOCK_OIDC_ISSUER=${MCP_OAUTH_ISSUER:-http://host.docker.internal:8090}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:19:      - MOCK_OIDC_AUDIENCE=${MCP_OAUTH_AUDIENCE:-api://mcp}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:20:      - MOCK_OIDC_SCOPE=${MCP_OAUTH_REQUIRED_SCOPES:-mcp:use}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:23:      python backend/tests/integration/mock_services/mcp_test_server/run_mock_oidc_idp.py ${MOCK_OIDC_PORT:-8090}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:42:  mcp_oauth_server:
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:49:    # Unlike the api-key/per-user mocks (which only receive connections), this
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:55:      - MCP_OAUTH_CLIENT_ID=${MCP_OAUTH_CLIENT_ID:-}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:56:      - MCP_OAUTH_CLIENT_SECRET=${MCP_OAUTH_CLIENT_SECRET:-}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:57:      - MCP_OAUTH_ISSUER=${MCP_OAUTH_ISSUER:-}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:58:      - MCP_OAUTH_JWKS_URI=${MCP_OAUTH_JWKS_URI:-}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:59:      - MCP_OAUTH_AUDIENCE=${MCP_OAUTH_AUDIENCE:-api://mcp}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:60:      - MCP_OAUTH_USERNAME=${MCP_OAUTH_USERNAME:-}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:61:      - MCP_OAUTH_PASSWORD=${MCP_OAUTH_PASSWORD:-}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:62:      - MCP_OAUTH_REQUIRED_SCOPES=${MCP_OAUTH_REQUIRED_SCOPES:-mcp:use}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:63:      - MCP_TEST_SERVER_PORT=${MCP_TEST_SERVER_PORT:-8004}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:64:      - MCP_SERVER_PORT=${MCP_TEST_SERVER_PORT:-8004}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:65:      - MCP_SERVER_HOST=${MCP_SERVER_HOST:-0.0.0.0}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:66:      - MCP_SERVER_PUBLIC_HOST=${MCP_SERVER_PUBLIC_HOST:-host.docker.internal}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:67:      - MCP_SERVER_PUBLIC_URL=${MCP_SERVER_PUBLIC_URL:-}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:70:      python backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_oauth.py ${MCP_TEST_SERVER_PORT:-8004}
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:73:      - "${MCP_TEST_SERVER_PORT:-8004}:${MCP_TEST_SERVER_PORT:-8004}"
HEAD:deployment/docker_compose/docker-compose.mcp-oauth-test.yml:82:          "import os, urllib.request; urllib.request.urlopen(f\"http://127.0.0.1:{os.environ['MCP_TEST_SERVER_PORT']}/healthz\")",
HEAD:deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml:4:  mcp_per_user_key_server:
HEAD:deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml:9:      - MCP_PER_USER_KEY_TEST_PORT=${MCP_PER_USER_KEY_TEST_PORT:-8007}
HEAD:deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml:10:      - MCP_PER_USER_KEY_REQUIRED_HEADER=${MCP_PER_USER_KEY_REQUIRED_HEADER:-X-Username}
HEAD:deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml:11:      - MCP_SERVER_HOST=${MCP_PER_USER_KEY_SERVER_HOST:-0.0.0.0}
HEAD:deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml:12:      - MCP_SERVER_PUBLIC_HOST=${MCP_PER_USER_KEY_SERVER_PUBLIC_HOST:-host.docker.internal}
HEAD:deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml:15:      python backend/tests/integration/mock_services/mcp_test_server/run_mcp_server_per_user_key.py ${MCP_PER_USER_KEY_TEST_PORT:-8007} --require-header ${MCP_PER_USER_KEY_REQUIRED_HEADER:-X-Username}
HEAD:deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml:18:      - "${MCP_PER_USER_KEY_TEST_PORT:-8007}:${MCP_PER_USER_KEY_TEST_PORT:-8007}"
HEAD:deployment/docker_compose/docker-compose.mcp-per-user-key-test.yml:27:          "import os, urllib.request; urllib.request.urlopen(f\"http://127.0.0.1:{os.environ['MCP_PER_USER_KEY_TEST_PORT']}/healthz\")",
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:199:  # Uncomment the block below to enable the MCP server for Onyx.
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:200:  # mcp_server:
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:207:  #     /bin/sh -c "if [ \"${MCP_SERVER_ENABLED:-}\" != \"True\" ] && [ \"${MCP_SERVER_ENABLED:-}\" != \"true\" ]; then
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:208:  #       echo 'MCP server is disabled (MCP_SERVER_ENABLED=false), skipping...';
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:211:  #       exec python -m onyx.mcp_server_main;
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:223:  #     # MCP Server Configuration
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:224:  #     - MCP_SERVER_ENABLED=${MCP_SERVER_ENABLED:-false}
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:225:  #     - MCP_SERVER_PORT=${MCP_SERVER_PORT:-8090}
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:226:  #     - MCP_SERVER_CORS_ORIGINS=${MCP_SERVER_CORS_ORIGINS:-}
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:238:  #     - mcp_server_logs:/var/log/onyx
HEAD:deployment/docker_compose/docker-compose.prod-no-letsencrypt.yml:525:  # mcp_server_logs:
HEAD:deployment/docker_compose/docker-compose.prod.yml:199:  # Uncomment the block below to enable the MCP server for Onyx.
HEAD:deployment/docker_compose/docker-compose.prod.yml:200:  # mcp_server:
HEAD:deployment/docker_compose/docker-compose.prod.yml:207:  #     /bin/sh -c "if [ \"${MCP_SERVER_ENABLED:-}\" != \"True\" ] && [ \"${MCP_SERVER_ENABLED:-}\" != \"true\" ]; then
HEAD:deployment/docker_compose/docker-compose.prod.yml:208:  #       echo 'MCP server is disabled (MCP_SERVER_ENABLED=false), skipping...';
HEAD:deployment/docker_compose/docker-compose.prod.yml:211:  #       exec python -m onyx.mcp_server_main;
HEAD:deployment/docker_compose/docker-compose.prod.yml:223:  #     # MCP Server Configuration
HEAD:deployment/docker_compose/docker-compose.prod.yml:224:  #     - MCP_SERVER_ENABLED=${MCP_SERVER_ENABLED:-false}
HEAD:deployment/docker_compose/docker-compose.prod.yml:225:  #     - MCP_SERVER_PORT=${MCP_SERVER_PORT:-8090}
HEAD:deployment/docker_compose/docker-compose.prod.yml:226:  #     - MCP_SERVER_CORS_ORIGINS=${MCP_SERVER_CORS_ORIGINS:-}
HEAD:deployment/docker_compose/docker-compose.prod.yml:238:  #     - mcp_server_logs:/var/log/onyx
HEAD:deployment/docker_compose/docker-compose.prod.yml:540:  # mcp_server_logs:
HEAD:deployment/docker_compose/docker-compose.template.yml:283:  # Uncomment the block below to enable the MCP server for Onyx.
HEAD:deployment/docker_compose/docker-compose.template.yml:284:  # mcp_server:
HEAD:deployment/docker_compose/docker-compose.template.yml:291:  #     /bin/sh -c "if [ \"${MCP_SERVER_ENABLED:-}\" != \"True\" ] && [ \"${MCP_SERVER_ENABLED:-}\" != \"true\" ]; then
HEAD:deployment/docker_compose/docker-compose.template.yml:292:  #       echo 'MCP server is disabled (MCP_SERVER_ENABLED=false), skipping...';
HEAD:deployment/docker_compose/docker-compose.template.yml:295:  #       exec python -m onyx.mcp_server_main;
HEAD:deployment/docker_compose/docker-compose.template.yml:307:  #     # MCP Server Configuration
HEAD:deployment/docker_compose/docker-compose.template.yml:308:  #     - MCP_SERVER_ENABLED=${MCP_SERVER_ENABLED:-false}
HEAD:deployment/docker_compose/docker-compose.template.yml:309:  #     - MCP_SERVER_PORT=${MCP_SERVER_PORT:-8090}
HEAD:deployment/docker_compose/docker-compose.template.yml:310:  #     - MCP_SERVER_CORS_ORIGINS=${MCP_SERVER_CORS_ORIGINS:-}
HEAD:deployment/docker_compose/docker-compose.template.yml:322:  #     - mcp_server_logs:/var/log/onyx
HEAD:deployment/docker_compose/docker-compose.template.yml:725:  # mcp_server_logs:
HEAD:deployment/docker_compose/docker-compose.yml:240:  # Uncomment the block below to enable the MCP server for Onyx.
HEAD:deployment/docker_compose/docker-compose.yml:241:  # mcp_server:
HEAD:deployment/docker_compose/docker-compose.yml:248:  #     /bin/sh -c "if [ \"${MCP_SERVER_ENABLED:-}\" != \"True\" ] && [ \"${MCP_SERVER_ENABLED:-}\" != \"true\" ]; then
HEAD:deployment/docker_compose/docker-compose.yml:249:  #       echo 'MCP server is disabled (MCP_SERVER_ENABLED=false), skipping...';
HEAD:deployment/docker_compose/docker-compose.yml:252:  #       exec python -m onyx.mcp_server_main;
HEAD:deployment/docker_compose/docker-compose.yml:264:  #     # MCP Server Configuration
HEAD:deployment/docker_compose/docker-compose.yml:265:  #     - MCP_SERVER_ENABLED=${MCP_SERVER_ENABLED:-false}
HEAD:deployment/docker_compose/docker-compose.yml:266:  #     - MCP_SERVER_PORT=${MCP_SERVER_PORT:-8090}
HEAD:deployment/docker_compose/docker-compose.yml:267:  #     - MCP_SERVER_CORS_ORIGINS=${MCP_SERVER_CORS_ORIGINS:-}
HEAD:deployment/docker_compose/docker-compose.yml:279:  #     - mcp_server_logs:/var/log/onyx
HEAD:deployment/docker_compose/docker-compose.yml:610:  # mcp_server_logs:
HEAD:deployment/docker_compose/env.prod.template:27:#GOOGLE_OAUTH_CLIENT_ID=
HEAD:deployment/docker_compose/env.prod.template:28:#GOOGLE_OAUTH_CLIENT_SECRET=
HEAD:deployment/docker_compose/env.prod.template:29:#OAUTH_CLIENT_ID=
HEAD:deployment/docker_compose/env.prod.template:30:#OAUTH_CLIENT_SECRET=
HEAD:deployment/docker_compose/env.template:62:### Signs password reset, email verification, OAuth login state, and captcha cookies.
HEAD:deployment/docker_compose/env.template:80:# API_KEY_HASH_ROUNDS=
HEAD:deployment/docker_compose/env.template:206:## MCP Server Configuration
HEAD:deployment/docker_compose/env.template:207:## The MCP (Model Context Protocol) server allows external MCP clients to interact with Onyx
HEAD:deployment/docker_compose/env.template:208:## Set to true to enable the MCP server (disabled by default)
HEAD:deployment/docker_compose/env.template:209:# MCP_SERVER_ENABLED=false
HEAD:deployment/docker_compose/env.template:210:## Port for the MCP server (defaults to 8090)
HEAD:deployment/docker_compose/env.template:211:# MCP_SERVER_PORT=8090
HEAD:deployment/docker_compose/env.template:212:## CORS origins for MCP clients (comma-separated list)
HEAD:deployment/docker_compose/env.template:213:# MCP_SERVER_CORS_ORIGINS=
HEAD:deployment/docker_compose/env.template:214:## Read timeout in seconds for MCP server requests to the API server (defaults to 300)
HEAD:deployment/docker_compose/env.template:215:# MCP_SERVER_API_REQUEST_TIMEOUT_SECONDS=300
HEAD:deployment/docker_compose/env.template:295:# Opt-in: capture IdP directory claims at OAuth/OIDC login to enrich chat
HEAD:deployment/docker_compose/env.template:305:# GOOGLE_OAUTH_CLIENT_ID=
HEAD:deployment/docker_compose/env.template:306:# GOOGLE_OAUTH_CLIENT_SECRET=
HEAD:deployment/docker_compose/env.template:307:# OAUTH_CLIENT_ID=
HEAD:deployment/docker_compose/env.template:308:# OAUTH_CLIENT_SECRET=
HEAD:deployment/docker_compose/env.template:328:# GEN_AI_API_KEY=
HEAD:deployment/docker_compose/env.template:385:# DOCUMENT_PUSH_API_KEY=
HEAD:deployment/docker_compose/env.template:388:## OAuth Connector Configs
HEAD:deployment/helm/charts/onyx/templates/ingress-mcp-oauth-callback.yaml:1:{{- if and .Values.ingress.enabled .Values.mcpServer.enabled -}}
HEAD:deployment/helm/charts/onyx/templates/ingress-mcp-oauth-callback.yaml:5:  name: {{ include "onyx.resourceName" (list . "ingress-mcp-oauth-callback") }}
HEAD:deployment/helm/charts/onyx/templates/ingress-mcp-oauth-callback.yaml:19:          - path: /mcp/oauth/callback
HEAD:deployment/helm/charts/onyx/templates/ingress-mcp-oauth-callback.yaml:29:      secretName: {{ include "onyx.resourceName" (list . "ingress-mcp-oauth-callback-tls") }}
HEAD:deployment/helm/charts/onyx/templates/ingress-mcp.yaml:1:{{- if and .Values.ingress.enabled .Values.mcpServer.enabled -}}
HEAD:deployment/helm/charts/onyx/templates/ingress-mcp.yaml:5:  name: {{ include "onyx.resourceName" (list . "ingress-mcp") }}
HEAD:deployment/helm/charts/onyx/templates/ingress-mcp.yaml:21:          - path: /mcp(/|$)(.*)
HEAD:deployment/helm/charts/onyx/templates/ingress-mcp.yaml:25:                name: {{ include "onyx.resourceName" (list . "mcp-server-service") }}
HEAD:deployment/helm/charts/onyx/templates/ingress-mcp.yaml:27:                  number: {{ .Values.mcpServer.service.servicePort }}
HEAD:deployment/helm/charts/onyx/templates/ingress-mcp.yaml:31:      secretName: {{ include "onyx.resourceName" (list . "ingress-mcp-tls") }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:1:{{- if .Values.mcpServer.enabled }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:5:  name: {{ include "onyx.resourceName" (list . "mcp-server") }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:8:    {{- with .Values.mcpServer.deploymentLabels }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:12:  replicas: {{ .Values.mcpServer.replicaCount }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:16:      {{- if .Values.mcpServer.deploymentLabels }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:17:      {{- toYaml .Values.mcpServer.deploymentLabels | nindent 6 }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:23:      {{- with .Values.mcpServer.podAnnotations }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:28:        {{- with .Values.mcpServer.deploymentLabels }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:31:        {{- with .Values.mcpServer.podLabels }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:41:        {{- toYaml .Values.mcpServer.podSecurityContext | nindent 8 }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:42:      {{- with .Values.mcpServer.nodeSelector }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:46:      {{- with .Values.mcpServer.affinity }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:50:      {{- with .Values.mcpServer.tolerations }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:55:        - name: mcp-server
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:57:            {{- toYaml .Values.mcpServer.securityContext | nindent 12 }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:58:          image: "{{ .Values.mcpServer.image.repository }}:{{ .Values.mcpServer.image.tag | default .Values.global.version }}"
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:60:          command: [{{ include "onyx.customCACerts.commandPrefix" . }}"python", "onyx/mcp_server_main.py"]
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:62:            - name: mcp-server-port
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:63:              containerPort: {{ .Values.mcpServer.containerPorts.server }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:68:              port: mcp-server-port
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:69:            initialDelaySeconds: {{ .Values.mcpServer.livenessProbe.initialDelaySeconds }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:70:            periodSeconds: {{ .Values.mcpServer.livenessProbe.periodSeconds }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:71:            timeoutSeconds: {{ .Values.mcpServer.livenessProbe.timeoutSeconds }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:72:            failureThreshold: {{ .Values.mcpServer.livenessProbe.failureThreshold }}
HEAD:deployment/helm/charts/onyx/templates/mcp-server-deployment.yaml:76:              port: mcp-server-port
```
MCP is an explicit architectural surface in this pinned revision.
Authentication, authorization, credential propagation, tool exposure and
network boundaries require dedicated tracing later in Phase 6 and testing
in later security phases.
## Data, Queue and Search Infrastructure Evidence
Evidence lines captured: 400
```text
HEAD:backend/onyx/access/access.py:6:from sqlalchemy.dialects import postgresql
HEAD:backend/onyx/access/access.py:378:                sa_cast([file_id], postgresql.JSONB)
HEAD:backend/onyx/access/models.py:73:    together. It's used for syncing document permissions to Vespa.
HEAD:backend/onyx/auth/captcha.py:36:from onyx.redis.redis_pool import get_async_redis_connection
HEAD:backend/onyx/auth/captcha.py:117:    the TTL returns False → raise. Redis errors fail open so a blip does
HEAD:backend/onyx/auth/captcha.py:120:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/captcha.py:121:        claimed = await redis.set(
HEAD:backend/onyx/auth/captcha.py:143:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/captcha.py:144:        await redis.delete(_replay_cache_key(token))
HEAD:backend/onyx/auth/login_claims_capture.py:9:attribute set into Redis at login time and derives a "directory profile"
HEAD:backend/onyx/auth/login_claims_capture.py:42:from onyx.redis.redis_pool import get_async_redis_connection
HEAD:backend/onyx/auth/login_claims_capture.py:50:# Redis HASH per (tenant, email): field = provider name, value = snapshot JSON.
HEAD:backend/onyx/auth/login_claims_capture.py:59:# flow, so a slow userinfo/Graph endpoint or an unreachable Redis must never
HEAD:backend/onyx/auth/login_claims_capture.py:155:    redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/login_claims_capture.py:157:    old_raw = await cast(Awaitable[Any], redis.hget(key, provider))
HEAD:backend/onyx/auth/login_claims_capture.py:185:    pipe = redis.pipeline()
HEAD:backend/onyx/auth/login_claims_capture.py:284:    """Snapshot the claims the IdP sent for this login into Redis.
HEAD:backend/onyx/auth/login_claims_capture.py:492:    and the tenant-prefixing TenantRedisClient would look up a different key
HEAD:backend/onyx/auth/login_claims_capture.py:495:    from onyx.redis.redis_pool import get_raw_redis_client
HEAD:backend/onyx/auth/login_claims_capture.py:497:    redis = get_raw_redis_client()
HEAD:backend/onyx/auth/login_claims_capture.py:498:    raw_map = redis.hgetall(_idp_claims_key(get_current_tenant_id(), email))
HEAD:backend/onyx/auth/login_claims_capture.py:561:    """Both derived views of the directory profile from one Redis read.
HEAD:backend/onyx/auth/login_claims_capture.py:564:    nothing is captured, or Redis is unavailable. Callers must treat the
HEAD:backend/onyx/auth/login_claims_capture.py:600:    redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/login_claims_capture.py:601:    # redis-py types hash commands as a sync-or-async union. This is the async client.
HEAD:backend/onyx/auth/login_claims_capture.py:604:        redis.hgetall(_idp_claims_key(get_current_tenant_id(), email)),
HEAD:backend/onyx/auth/mobile_sso/code_store.py:1:"""One-time, PKCE-bound SSO code store (Redis).
HEAD:backend/onyx/auth/mobile_sso/code_store.py:5:Redis under a short-lived, single-use code bound to an app-supplied PKCE
HEAD:backend/onyx/auth/mobile_sso/code_store.py:16:Redis is core infra (always available, even when ``AUTH_BACKEND=jwt``), so this
HEAD:backend/onyx/auth/mobile_sso/code_store.py:27:from onyx.redis.redis_pool import get_async_redis_connection
HEAD:backend/onyx/auth/mobile_sso/code_store.py:41:    redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/mobile_sso/code_store.py:42:    await redis.set(
HEAD:backend/onyx/auth/mobile_sso/code_store.py:59:    redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/mobile_sso/code_store.py:60:    # Atomic get-and-delete enforces single use (Redis 6.2+).
HEAD:backend/onyx/auth/mobile_sso/code_store.py:61:    raw = await redis.getdel(f"{MOBILE_SSO_CODE_PREFIX}{code}")
HEAD:backend/onyx/auth/mobile_sso/tokens.py:5:strategy's ``write_token``) — server-revocable under the redis/postgres backends,
HEAD:backend/onyx/auth/schemas.py:69:    REDIS = "redis"
HEAD:backend/onyx/auth/schemas.py:70:    POSTGRES = "postgres"
HEAD:backend/onyx/auth/session_tokens.py:1:"""Redis session-token value format and rejection classification.
HEAD:backend/onyx/auth/session_tokens.py:6:(no entry: cookie outlived the grace window, or Redis dropped the key),
HEAD:backend/onyx/auth/session_tokens.py:12:bearer transport and legitimately miss in Redis), so the classification is
HEAD:backend/onyx/auth/session_tokens.py:219:            "Presented session token has no Redis entry: the cookie outlived "
HEAD:backend/onyx/auth/session_tokens.py:220:            "the grace window, or Redis dropped the key (restart/eviction/flush)."
HEAD:backend/onyx/auth/signup_rate_limit.py:10:from onyx.redis.redis_pool import get_async_redis_connection
HEAD:backend/onyx/auth/signup_rate_limit.py:19:_REDIS_KEY_PREFIX = "signup_rate:"
HEAD:backend/onyx/auth/signup_rate_limit.py:36:    return f"{_REDIS_KEY_PREFIX}{ip}:{bucket}"
HEAD:backend/onyx/auth/signup_rate_limit.py:48:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/signup_rate_limit.py:49:        pipe = redis.pipeline()
HEAD:backend/onyx/auth/signup_rate_limit.py:55:        logger.error("Signup rate-limit Redis error: %s", e)
HEAD:backend/onyx/auth/users.py:43:    RedisStrategy,  # ty: ignore[possibly-missing-import]
HEAD:backend/onyx/auth/users.py:47:    AccessTokenDatabase,
HEAD:backend/onyx/auth/users.py:48:    DatabaseStrategy,
HEAD:backend/onyx/auth/users.py:55:from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
HEAD:backend/onyx/auth/users.py:103:    REDIS_AUTH_KEY_PREFIX,
HEAD:backend/onyx/auth/users.py:119:    OnyxRedisLocks,
HEAD:backend/onyx/auth/users.py:155:from onyx.redis.redis_pool import get_async_redis_connection, retrieve_ws_token_data
HEAD:backend/onyx/auth/users.py:172:    POSTGRES_DEFAULT_SCHEMA,
HEAD:backend/onyx/auth/users.py:292:    value = cache.get(OnyxRedisLocks.ANONYMOUS_USER_ENABLED)
HEAD:backend/onyx/auth/users.py:590:    user_db: SQLAlchemyUserDatabase[User, uuid.UUID]
HEAD:backend/onyx/auth/users.py:601:                self.user_db = SQLAlchemyUserDatabase[User, uuid.UUID](
HEAD:backend/onyx/auth/users.py:615:                tenant_user_db = SQLAlchemyUserDatabase[User, uuid.UUID](
HEAD:backend/onyx/auth/users.py:664:                tenant_user_db = SQLAlchemyUserDatabase[User, uuid.UUID](
HEAD:backend/onyx/auth/users.py:793:                    tenant_user_db = SQLAlchemyUserDatabase[User, uuid.UUID](
HEAD:backend/onyx/auth/users.py:1497:            POSTGRES_DEFAULT_SCHEMA,
HEAD:backend/onyx/auth/users.py:1547:                POSTGRES_DEFAULT_SCHEMA,
HEAD:backend/onyx/auth/users.py:1568:            tenant_user_db: SQLAlchemyUserDatabase = SQLAlchemyUserDatabase(
HEAD:backend/onyx/auth/users.py:1637:    user_db: SQLAlchemyUserDatabase = Depends(get_user_db),
HEAD:backend/onyx/auth/users.py:1679:class TenantAwareRedisStrategy(RedisStrategy[User, uuid.UUID]):
HEAD:backend/onyx/auth/users.py:1681:    A custom strategy that fetches the actual async Redis connection inside each method.
HEAD:backend/onyx/auth/users.py:1682:    We do NOT pass a synchronous or "coroutine" redis object to the constructor.
HEAD:backend/onyx/auth/users.py:1691:        key_prefix: str = REDIS_AUTH_KEY_PREFIX,
HEAD:backend/onyx/auth/users.py:1697:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/users.py:1705:        await redis.set(
HEAD:backend/onyx/auth/users.py:1723:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/users.py:1724:        raw_value = await redis.get(f"{self.key_prefix}{token}")
HEAD:backend/onyx/auth/users.py:1747:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/users.py:1749:        previous_raw_value = await redis.get(token_key)
HEAD:backend/onyx/auth/users.py:1750:        await redis.set(
HEAD:backend/onyx/auth/users.py:1759:        """Refreshes a token by extending its expiration time in Redis."""
HEAD:backend/onyx/auth/users.py:1764:        redis = await get_async_redis_connection()
HEAD:backend/onyx/auth/users.py:1767:        raw_value = await redis.get(token_key)
HEAD:backend/onyx/auth/users.py:1775:        await redis.set(
HEAD:backend/onyx/auth/users.py:1789:class RefreshableDatabaseStrategy(DatabaseStrategy[User, uuid.UUID, AccessToken]):
HEAD:backend/onyx/auth/users.py:1790:    """Database strategy with token refreshing capabilities."""
HEAD:backend/onyx/auth/users.py:1794:        access_token_db: AccessTokenDatabase[AccessToken],
HEAD:backend/onyx/auth/users.py:1801:        """Refresh a token by updating its expiration time in the database."""
HEAD:backend/onyx/auth/users.py:1805:        # Find the token in database
HEAD:backend/onyx/auth/users.py:1824:    Tokens are self-contained and verified via signature — no Redis or DB
HEAD:backend/onyx/auth/users.py:1878:def get_redis_strategy() -> TenantAwareRedisStrategy:
HEAD:backend/onyx/auth/users.py:1879:    return TenantAwareRedisStrategy()
HEAD:backend/onyx/auth/users.py:1882:def get_database_strategy(
HEAD:backend/onyx/auth/users.py:1883:    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
HEAD:backend/onyx/auth/users.py:1884:) -> RefreshableDatabaseStrategy:
HEAD:backend/onyx/auth/users.py:1885:    return RefreshableDatabaseStrategy(
HEAD:backend/onyx/auth/users.py:1900:            "JWT auth backend is only supported for single-tenant, self-hosted deployments. Use 'redis' or 'postgres' instead."
HEAD:backend/onyx/auth/users.py:1905:if AUTH_BACKEND == AuthBackend.REDIS:
HEAD:backend/onyx/auth/users.py:1907:        name="redis", transport=cookie_transport, get_strategy=get_redis_strategy
HEAD:backend/onyx/auth/users.py:1909:elif AUTH_BACKEND == AuthBackend.POSTGRES:
HEAD:backend/onyx/auth/users.py:1911:        name="postgres", transport=cookie_transport, get_strategy=get_database_strategy
HEAD:backend/onyx/auth/users.py:2089:    user_db: SQLAlchemyUserDatabase[User, uuid.UUID] = SQLAlchemyUserDatabase(
HEAD:backend/onyx/auth/users.py:2477:    # Validate WS token in Redis (single-use, deleted after retrieval)
HEAD:backend/onyx/auth/users.py:2501:        token_tenant_id = POSTGRES_DEFAULT_SCHEMA
HEAD:backend/onyx/background/README.md:9:5. Reporting metrics on things like queue length for monitoring purposes
HEAD:backend/onyx/background/README.md:11:## Worker → Queue Mapping
HEAD:backend/onyx/background/README.md:13:| Worker                    | File                           | Queues                                                                                                               |
HEAD:backend/onyx/background/README.md:15:| Primary                   | `apps/primary.py`              | `celery`                                                                                                             |
HEAD:backend/onyx/background/README.md:16:| Light                     | `apps/light.py`                | `vespa_metadata_sync`, `connector_deletion`, `doc_permissions_upsert`, `checkpoint_cleanup`, `index_attempt_cleanup` |
HEAD:backend/onyx/background/README.md:22:| Background (consolidated) | `apps/background.py`           | All queues above except `celery`                                                                                     |
HEAD:backend/onyx/background/README.md:28:| **Beat**   | `beat.py`   | Celery beat scheduler with `DynamicTenantScheduler` that generates per-tenant periodic task schedules |
HEAD:backend/onyx/background/README.md:43:It is the single worker which handles tasks from the default celery queue. It is a singleton worker ensured by the `PRIMARY_WORKER` Redis lock
HEAD:backend/onyx/background/README.md:44:which it touches every `CELERY_PRIMARY_WORKER_LOCK_TIMEOUT / 8` seconds (using Celery Bootsteps)
HEAD:backend/onyx/background/README.md:48:- waits for redis, postgres, document index to all be healthy
HEAD:backend/onyx/background/README.md:50:- cleans all the redis states associated with background jobs
HEAD:backend/onyx/background/README.md:53:Then it cycles through its tasks as scheduled by Celery Beat:
HEAD:backend/onyx/background/README.md:57:| `check_for_indexing`              | 15s       | Scans for connectors needing indexing → dispatches to `DOCFETCHING` queue                  |
HEAD:backend/onyx/background/README.md:58:| `check_for_vespa_sync_task`       | 20s       | Finds stale documents/document sets → dispatches sync tasks to `VESPA_METADATA_SYNC` queue |
HEAD:backend/onyx/background/README.md:59:| `check_for_pruning`               | 20s       | Finds connectors due for pruning → dispatches to `CONNECTOR_PRUNING` queue                 |
HEAD:backend/onyx/background/README.md:60:| `check_for_connector_deletion`    | 20s       | Processes deletion requests → dispatches to `CONNECTOR_DELETION` queue                     |
HEAD:backend/onyx/background/README.md:61:| `check_for_user_file_processing`  | 20s       | Checks for user uploads → dispatches to `USER_FILE_PROCESSING` queue                       |
HEAD:backend/onyx/background/README.md:64:| `celery_beat_heartbeat`           | 1m        | Heartbeat for Beat watchdog                                                                |
HEAD:backend/onyx/background/README.md:66:Watchdog is a separate Python process managed by supervisord which runs alongside celery workers. It checks the ONYX_CELERY_BEAT_HEARTBEAT_KEY in
HEAD:backend/onyx/background/README.md:67:Redis to ensure Celery Beat is not dead. Beat schedules the celery_beat_heartbeat for Primary to touch the key and share that it's still alive.
HEAD:backend/onyx/background/README.md:78:- Deletes documents that are marked for deletion in Postgres
HEAD:backend/onyx/background/README.md:87:Generates CSV exports which may take a long time with significant data in Postgres.
HEAD:backend/onyx/background/README.md:103:- Queue lengths, connector success/failure, connector latencies
HEAD:backend/onyx/background/README.md:109:Workers can expose Prometheus metrics via a standalone HTTP server. Currently docfetching and docprocessing have push-based task lifecycle metrics; the monitoring worker runs pull-based collectors for queue depth and connector health.
HEAD:backend/onyx/background/README.md:111:For the full metric reference, integration guide, and PromQL examples, see [`docs/METRICS.md`](../../../docs/METRICS.md#celery-worker-metrics).
HEAD:backend/onyx/background/celery/apps/app_base.py:8:from celery import (
HEAD:backend/onyx/background/celery/apps/app_base.py:12:from celery.app import trace
HEAD:backend/onyx/background/celery/apps/app_base.py:13:from celery.exceptions import WorkerShutdown
HEAD:backend/onyx/background/celery/apps/app_base.py:14:from celery.signals import before_task_publish, task_postrun, task_prerun
HEAD:backend/onyx/background/celery/apps/app_base.py:15:from celery.states import READY_STATES
HEAD:backend/onyx/background/celery/apps/app_base.py:16:from celery.utils.log import get_task_logger
HEAD:backend/onyx/background/celery/apps/app_base.py:17:from celery.worker import strategy
HEAD:backend/onyx/background/celery/apps/app_base.py:18:from celery.worker.control import control_command
HEAD:backend/onyx/background/celery/apps/app_base.py:19:from redis.lock import Lock as RedisLock
HEAD:backend/onyx/background/celery/apps/app_base.py:20:from sentry_sdk.integrations.celery import CeleryIntegration
HEAD:backend/onyx/background/celery/apps/app_base.py:24:from onyx.background.celery.apps.task_formatters import (
HEAD:backend/onyx/background/celery/apps/app_base.py:25:    CeleryTaskColoredFormatter,
HEAD:backend/onyx/background/celery/apps/app_base.py:26:    CeleryTaskJsonFormatter,
HEAD:backend/onyx/background/celery/apps/app_base.py:27:    CeleryTaskPlainFormatter,
HEAD:backend/onyx/background/celery/apps/app_base.py:29:from onyx.background.celery.celery_utils import (
HEAD:backend/onyx/background/celery/apps/app_base.py:30:    celery_is_worker_primary,
HEAD:backend/onyx/background/celery/apps/app_base.py:33:from onyx.background.celery.tasks.vespa.document_sync import (
HEAD:backend/onyx/background/celery/apps/app_base.py:39:    ENABLE_OPENSEARCH_INDEXING_FOR_ONYX,
HEAD:backend/onyx/background/celery/apps/app_base.py:40:    ONYX_DISABLE_VESPA,
HEAD:backend/onyx/background/celery/apps/app_base.py:42:from onyx.configs.constants import ONYX_CLOUD_CELERY_TASK_PREFIX, OnyxRedisLocks
HEAD:backend/onyx/background/celery/apps/app_base.py:44:from onyx.document_index.vespa.shared_utils.utils import wait_for_vespa_with_timeout
HEAD:backend/onyx/background/celery/apps/app_base.py:46:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/onyx/background/celery/apps/app_base.py:47:from onyx.redis.redis_connector_delete import RedisConnectorDelete
HEAD:backend/onyx/background/celery/apps/app_base.py:48:from onyx.redis.redis_connector_doc_perm_sync import RedisConnectorPermissionSync
HEAD:backend/onyx/background/celery/apps/app_base.py:49:from onyx.redis.redis_connector_ext_group_sync import RedisConnectorExternalGroupSync
HEAD:backend/onyx/background/celery/apps/app_base.py:50:from onyx.redis.redis_connector_prune import RedisConnectorPrune
HEAD:backend/onyx/background/celery/apps/app_base.py:51:from onyx.redis.redis_document_set import RedisDocumentSet
HEAD:backend/onyx/background/celery/apps/app_base.py:52:from onyx.redis.redis_pool import get_redis_client
HEAD:backend/onyx/background/celery/apps/app_base.py:53:from onyx.redis.redis_usergroup import RedisUserGroup
HEAD:backend/onyx/background/celery/apps/app_base.py:68:    POSTGRES_DEFAULT_SCHEMA,
HEAD:backend/onyx/background/celery/apps/app_base.py:69:    SENTRY_CELERY_TRACES_SAMPLE_RATE,
HEAD:backend/onyx/background/celery/apps/app_base.py:83:        traces_sample_rate=SENTRY_CELERY_TRACES_SAMPLE_RATE,
HEAD:backend/onyx/background/celery/apps/app_base.py:84:        integrations=[CeleryIntegration()],
HEAD:backend/onyx/background/celery/apps/app_base.py:99:    Intentionally ungated, like Celery's built-in shutdown/terminate/revoke control
HEAD:backend/onyx/background/celery/apps/app_base.py:102:    from celery.worker import state as worker_state
HEAD:backend/onyx/background/celery/apps/app_base.py:113:    abstract = True  # So Celery knows not to register this as a real task.
HEAD:backend/onyx/background/celery/apps/app_base.py:117:        tenant_id = kwargs.get("tenant_id", None) or POSTGRES_DEFAULT_SCHEMA
HEAD:backend/onyx/background/celery/apps/app_base.py:137:    workers can compute queue wait time (time between publish and execution)."""
HEAD:backend/onyx/background/celery/apps/app_base.py:139:        headers["enqueued_at"] = time.time()
HEAD:backend/onyx/background/celery/apps/app_base.py:194:    if task.name.startswith(ONYX_CLOUD_CELERY_TASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:198:    # Get tenant_id directly from kwargs- each celery task has a tenant_id kwarg
HEAD:backend/onyx/background/celery/apps/app_base.py:201:        tenant_id = POSTGRES_DEFAULT_SCHEMA
HEAD:backend/onyx/background/celery/apps/app_base.py:203:        tenant_id = cast(str, kwargs.get("tenant_id", POSTGRES_DEFAULT_SCHEMA))
HEAD:backend/onyx/background/celery/apps/app_base.py:213:    r = get_redis_client(tenant_id=tenant_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:215:    # NOTE: we want to remove the `Redis*` classes, prefer to just have functions to
HEAD:backend/onyx/background/celery/apps/app_base.py:222:    if task_id.startswith(RedisDocumentSet.PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:223:        document_set_id = RedisDocumentSet.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:225:            rds = RedisDocumentSet(tenant_id, int(document_set_id))
HEAD:backend/onyx/background/celery/apps/app_base.py:229:    if task_id.startswith(RedisUserGroup.PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:230:        usergroup_id = RedisUserGroup.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:232:            rug = RedisUserGroup(tenant_id, int(usergroup_id))
HEAD:backend/onyx/background/celery/apps/app_base.py:236:    if task_id.startswith(RedisConnectorDelete.PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:237:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:239:            RedisConnectorDelete.remove_from_taskset(int(cc_pair_id), task_id, r)
HEAD:backend/onyx/background/celery/apps/app_base.py:242:    if task_id.startswith(RedisConnectorPrune.SUBTASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:243:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:245:            RedisConnectorPrune.remove_from_taskset(int(cc_pair_id), task_id, r)
HEAD:backend/onyx/background/celery/apps/app_base.py:248:    if task_id.startswith(RedisConnectorPermissionSync.SUBTASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:249:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:251:            RedisConnectorPermissionSync.remove_from_taskset(
HEAD:backend/onyx/background/celery/apps/app_base.py:256:    if task_id.startswith(RedisConnectorExternalGroupSync.SUBTASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:257:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:259:            RedisConnectorExternalGroupSync.remove_from_taskset(
HEAD:backend/onyx/background/celery/apps/app_base.py:283:    tenant_id = cast(str, request_kwargs.get("tenant_id", POSTGRES_DEFAULT_SCHEMA))
HEAD:backend/onyx/background/celery/apps/app_base.py:285:    r = get_redis_client(tenant_id=tenant_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:289:def on_celeryd_init(
HEAD:backend/onyx/background/celery/apps/app_base.py:294:    """The first signal sent on celery worker startup"""
HEAD:backend/onyx/background/celery/apps/app_base.py:326:def wait_for_redis(sender: Any, **kwargs: Any) -> None:  # noqa: ARG001
HEAD:backend/onyx/background/celery/apps/app_base.py:327:    """Waits for redis to become ready subject to a hardcoded timeout.
HEAD:backend/onyx/background/celery/apps/app_base.py:328:    Will raise WorkerShutdown to kill the celery worker if the timeout
HEAD:backend/onyx/background/celery/apps/app_base.py:331:    r = get_redis_client(tenant_id=POSTGRES_DEFAULT_SCHEMA)
HEAD:backend/onyx/background/celery/apps/app_base.py:338:    logger.info("Redis: Readiness probe starting.")
HEAD:backend/onyx/background/celery/apps/app_base.py:352:            "Redis: Readiness probe ongoing. elapsed=%s timeout=%s",
HEAD:backend/onyx/background/celery/apps/app_base.py:360:        msg = f"Redis: Readiness probe did not succeed within the timeout ({WAIT_LIMIT} seconds). Exiting..."
HEAD:backend/onyx/background/celery/apps/app_base.py:364:    logger.info("Redis: Readiness probe succeeded. Continuing...")
HEAD:backend/onyx/background/celery/apps/app_base.py:370:    Will raise WorkerShutdown to kill the celery worker if the timeout is reached."""
HEAD:backend/onyx/background/celery/apps/app_base.py:377:    logger.info("Database: Readiness probe starting.")
HEAD:backend/onyx/background/celery/apps/app_base.py:393:            "Database: Readiness probe ongoing. elapsed=%s timeout=%s",
HEAD:backend/onyx/background/celery/apps/app_base.py:401:        msg = f"Database: Readiness probe did not succeed within the timeout ({WAIT_LIMIT} seconds). Exiting..."
HEAD:backend/onyx/background/celery/apps/app_base.py:405:    logger.info("Database: Readiness probe succeeded. Continuing...")
HEAD:backend/onyx/background/celery/apps/app_base.py:410:    logger.info("Running as a secondary celery worker: pid=%s", os.getpid())
HEAD:backend/onyx/background/celery/apps/app_base.py:415:    r = get_redis_client(tenant_id=POSTGRES_DEFAULT_SCHEMA)
HEAD:backend/onyx/background/celery/apps/app_base.py:420:        if r.exists(OnyxRedisLocks.PRIMARY_WORKER):
HEAD:backend/onyx/background/celery/apps/app_base.py:444:    # https://medium.com/ambient-innovation/health-checks-for-celery-in-kubernetes-cf3274a3e106
HEAD:backend/onyx/background/celery/apps/app_base.py:445:    # https://github.com/celery/celery/issues/4079#issuecomment-1270085680
HEAD:backend/onyx/background/celery/apps/app_base.py:460:    if not celery_is_worker_primary(sender):
HEAD:backend/onyx/background/celery/apps/app_base.py:471:    lock: RedisLock = sender.primary_worker_lock
HEAD:backend/onyx/background/celery/apps/app_base.py:485:    Returns True iff --loglevel or -l was explicitly passed on the celery CLI.
HEAD:backend/onyx/background/celery/apps/app_base.py:489:    Celery substitutes its own default. To distinguish "operator passed it" (CLI
HEAD:backend/onyx/background/celery/apps/app_base.py:490:    should win) from "Celery defaulted it" (LOG_LEVEL env should win) we have to
HEAD:backend/onyx/background/celery/apps/app_base.py:506:    Returns the (level, human-readable explanation) for celery worker logging.
HEAD:backend/onyx/background/celery/apps/app_base.py:508:    Precedence: explicit --loglevel CLI flag > LOG_LEVEL env var > Celery
HEAD:backend/onyx/background/celery/apps/app_base.py:511:    server, model servers, and all Celery workers.
HEAD:backend/onyx/background/celery/apps/app_base.py:519:        return cli_loglevel, "celery --loglevel CLI arg"
HEAD:backend/onyx/background/celery/apps/app_base.py:528:    return cli_loglevel, "celery default (no --loglevel, no LOG_LEVEL)"
HEAD:backend/onyx/background/celery/apps/app_base.py:539:    # celery's config
HEAD:backend/onyx/background/celery/apps/app_base.py:590:        "Celery effective log level: %s (source: %s)",
HEAD:backend/onyx/background/celery/apps/app_base.py:601:        CeleryTaskJsonFormatter()
HEAD:backend/onyx/background/celery/apps/app_base.py:603:        else CeleryTaskColoredFormatter(log_format, datefmt="%m/%d/%Y %I:%M:%S %p")
HEAD:backend/onyx/background/celery/apps/app_base.py:613:            CeleryTaskJsonFormatter()
HEAD:backend/onyx/background/celery/apps/app_base.py:615:            else CeleryTaskPlainFormatter(log_format, datefmt="%m/%d/%Y %I:%M:%S %p")
HEAD:backend/onyx/background/celery/apps/app_base.py:623:    # hide celery task received spam
HEAD:backend/onyx/background/celery/apps/app_base.py:627:    # uncomment this to hide celery task succeeded/failed spam
HEAD:backend/onyx/background/celery/apps/app_base.py:666:    CURRENT_TENANT_ID_CONTEXTVAR.set(POSTGRES_DEFAULT_SCHEMA)
HEAD:backend/onyx/background/celery/apps/app_base.py:678:            "DISABLE_VECTOR_DB is set — skipping Vespa/OpenSearch readiness check."
HEAD:backend/onyx/background/celery/apps/app_base.py:682:    if not ONYX_DISABLE_VESPA:
HEAD:backend/onyx/background/celery/apps/app_base.py:683:        if not wait_for_vespa_with_timeout():
HEAD:backend/onyx/background/celery/apps/app_base.py:685:                "[Vespa] Readiness probe did not succeed within the timeout. Exiting..."
HEAD:backend/onyx/background/celery/apps/app_base.py:690:    if ENABLE_OPENSEARCH_INDEXING_FOR_ONYX:
HEAD:backend/onyx/background/celery/apps/app_base.py:691:        # Imported here: opensearchpy costs ~18 MB and not every worker needs it.
HEAD:backend/onyx/background/celery/apps/app_base.py:692:        from onyx.document_index.opensearch.client import (
HEAD:backend/onyx/background/celery/apps/app_base.py:693:            wait_for_opensearch_with_timeout,
HEAD:backend/onyx/background/celery/apps/app_base.py:696:        if not wait_for_opensearch_with_timeout():
HEAD:backend/onyx/background/celery/apps/app_base.py:697:            msg = "[OpenSearch] Readiness probe did not succeed within the timeout. Exiting..."
HEAD:backend/onyx/background/celery/apps/app_base.py:704:    requires = {"celery.worker.components:Timer"}
HEAD:backend/onyx/background/celery/apps/app_base.py:733:# Task modules that require a vector DB (Vespa/OpenSearch).
HEAD:backend/onyx/background/celery/apps/app_base.py:736:    "onyx.background.celery.tasks.connector_deletion",
HEAD:backend/onyx/background/celery/apps/app_base.py:737:    "onyx.background.celery.tasks.docprocessing",
HEAD:backend/onyx/background/celery/apps/app_base.py:738:    "onyx.background.celery.tasks.docfetching",
HEAD:backend/onyx/background/celery/apps/app_base.py:739:    "onyx.background.celery.tasks.pruning",
HEAD:backend/onyx/background/celery/apps/app_base.py:740:    "onyx.background.celery.tasks.vespa",
HEAD:backend/onyx/background/celery/apps/app_base.py:741:    "onyx.background.celery.tasks.opensearch_migration",
HEAD:backend/onyx/background/celery/apps/app_base.py:742:    "onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/onyx/background/celery/apps/app_base.py:743:    "onyx.background.celery.tasks.hierarchyfetching",
HEAD:backend/onyx/background/celery/apps/app_base.py:745:    "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/onyx/background/celery/apps/app_base.py:746:    "ee.onyx.background.celery.tasks.external_group_syncing",
HEAD:backend/onyx/background/celery/apps/app_base.py:748:# NOTE: "onyx.background.celery.tasks.shared" is intentionally NOT in the set
HEAD:backend/onyx/background/celery/apps/app_base.py:749:# above. It contains celery_beat_heartbeat (which only writes to Redis) alongside
HEAD:backend/onyx/background/celery/apps/beat.py:5:from celery import Celery, signals
HEAD:backend/onyx/background/celery/apps/beat.py:6:from celery.beat import PersistentScheduler
HEAD:backend/onyx/background/celery/apps/beat.py:7:from celery.signals import beat_init
HEAD:backend/onyx/background/celery/apps/beat.py:8:from celery.utils.log import get_task_logger
HEAD:backend/onyx/background/celery/apps/beat.py:10:import onyx.background.celery.apps.app_base as app_base
HEAD:backend/onyx/background/celery/apps/beat.py:11:from onyx.background.celery.celery_utils import make_probe_path
HEAD:backend/onyx/background/celery/apps/beat.py:12:from onyx.background.celery.tasks.beat_schedule import CLOUD_BEAT_MULTIPLIER_DEFAULT
HEAD:backend/onyx/background/celery/apps/beat.py:13:from onyx.configs.constants import POSTGRES_CELERY_BEAT_APP_NAME
HEAD:backend/onyx/background/celery/apps/beat.py:22:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/beat.py:23:celery_app.config_from_object("onyx.background.celery.configs.beat")
HEAD:backend/onyx/background/celery/apps/beat.py:84:        """Given a list of tenant id's, generates a new beat schedule for celery."""
HEAD:backend/onyx/background/celery/apps/beat.py:91:                "onyx.background.celery.tasks.beat_schedule",
HEAD:backend/onyx/background/celery/apps/beat.py:117:            "onyx.background.celery.tasks.beat_schedule", "get_tasks_to_schedule"
HEAD:backend/onyx/background/celery/apps/beat.py:155:        """Only updates the actual beat schedule on the celery app when it changes"""
HEAD:backend/onyx/background/celery/apps/beat.py:254:    # Celery beat shouldn't touch the db at all. But just setting a low minimum here.
HEAD:backend/onyx/background/celery/apps/beat.py:255:    SqlEngine.set_app_name(POSTGRES_CELERY_BEAT_APP_NAME)
HEAD:backend/onyx/background/celery/apps/beat.py:258:    app_base.wait_for_redis(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/beat.py:275:celery_app.conf.beat_scheduler = DynamicTenantScheduler
HEAD:backend/onyx/background/celery/apps/beat.py:276:celery_app.conf.task_default_base = app_base.TenantAwareTask
HEAD:backend/onyx/background/celery/apps/client.py:1:from celery import Celery
HEAD:backend/onyx/background/celery/apps/client.py:3:import onyx.background.celery.apps.app_base as app_base
HEAD:backend/onyx/background/celery/apps/client.py:5:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/client.py:6:celery_app.config_from_object("onyx.background.celery.configs.client")
HEAD:backend/onyx/background/celery/apps/client.py:7:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/docfetching.py:3:from celery import Celery, Task, signals
HEAD:backend/onyx/background/celery/apps/docfetching.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/docfetching.py:5:from celery.signals import (
HEAD:backend/onyx/background/celery/apps/docfetching.py:6:    celeryd_init,
HEAD:backend/onyx/background/celery/apps/docfetching.py:13:import onyx.background.celery.apps.app_base as app_base
HEAD:backend/onyx/background/celery/apps/docfetching.py:14:from onyx.background.celery.tasks.docfetching.worker_shutdown import (
HEAD:backend/onyx/background/celery/apps/docfetching.py:17:from onyx.configs.constants import POSTGRES_CELERY_WORKER_DOCFETCHING_APP_NAME
HEAD:backend/onyx/background/celery/apps/docfetching.py:19:from onyx.server.metrics.celery_task_metrics import (
HEAD:backend/onyx/background/celery/apps/docfetching.py:20:    on_celery_task_postrun,
HEAD:backend/onyx/background/celery/apps/docfetching.py:21:    on_celery_task_prerun,
HEAD:backend/onyx/background/celery/apps/docfetching.py:22:    on_celery_task_rejected,
HEAD:backend/onyx/background/celery/apps/docfetching.py:23:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/docfetching.py:24:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/docfetching.py:36:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/docfetching.py:37:celery_app.config_from_object("onyx.background.celery.configs.docfetching")
HEAD:backend/onyx/background/celery/apps/docfetching.py:38:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/docfetching.py:51:    on_celery_task_prerun(task_id, task)
HEAD:backend/onyx/background/celery/apps/docfetching.py:67:    on_celery_task_postrun(task_id, task, state)
HEAD:backend/onyx/background/celery/apps/docfetching.py:80:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/apps/docfetching.py:86:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/apps/docfetching.py:92:    # The task name must be extracted from the Celery message headers.
HEAD:backend/onyx/background/celery/apps/docfetching.py:100:    on_celery_task_rejected(None, task_name)
HEAD:backend/onyx/background/celery/apps/docfetching.py:103:@celeryd_init.connect
HEAD:backend/onyx/background/celery/apps/docfetching.py:104:def on_celeryd_init(sender: str, conf: Any = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docfetching.py:105:    app_base.on_celeryd_init(sender, conf, **kwargs)
HEAD:backend/onyx/background/celery/apps/docfetching.py:112:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_DOCFETCHING_APP_NAME)
HEAD:backend/onyx/background/celery/apps/docfetching.py:116:    app_base.wait_for_redis(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/docfetching.py:157:    celery_app.steps["worker"].add(bootstep)
HEAD:backend/onyx/background/celery/apps/docfetching.py:159:celery_app.autodiscover_tasks(
HEAD:backend/onyx/background/celery/apps/docfetching.py:162:            "onyx.background.celery.tasks.docfetching",
HEAD:backend/onyx/background/celery/apps/docprocessing.py:3:from celery import Celery, Task, signals
HEAD:backend/onyx/background/celery/apps/docprocessing.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/docprocessing.py:5:from celery.signals import (
HEAD:backend/onyx/background/celery/apps/docprocessing.py:6:    celeryd_init,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:13:import onyx.background.celery.apps.app_base as app_base
HEAD:backend/onyx/background/celery/apps/docprocessing.py:14:from onyx.background.celery.tasks.docprocessing.batch_counters import (
HEAD:backend/onyx/background/celery/apps/docprocessing.py:18:from onyx.configs.constants import POSTGRES_CELERY_WORKER_DOCPROCESSING_APP_NAME
HEAD:backend/onyx/background/celery/apps/docprocessing.py:20:from onyx.server.metrics.celery_task_metrics import (
HEAD:backend/onyx/background/celery/apps/docprocessing.py:21:    on_celery_task_postrun,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:22:    on_celery_task_prerun,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:23:    on_celery_task_rejected,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:24:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:25:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:37:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:38:celery_app.config_from_object("onyx.background.celery.configs.docprocessing")
HEAD:backend/onyx/background/celery/apps/docprocessing.py:39:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/docprocessing.py:52:    on_celery_task_prerun(task_id, task)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:69:    on_celery_task_postrun(task_id, task, state)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:83:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:89:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:95:    # The task name must be extracted from the Celery message headers.
HEAD:backend/onyx/background/celery/apps/docprocessing.py:103:    on_celery_task_rejected(None, task_name)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:106:@celeryd_init.connect
HEAD:backend/onyx/background/celery/apps/docprocessing.py:107:def on_celeryd_init(sender: str, conf: Any = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/docprocessing.py:108:    app_base.on_celeryd_init(sender, conf, **kwargs)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:115:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_DOCPROCESSING_APP_NAME)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:124:    app_base.wait_for_redis(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:166:    celery_app.steps["worker"].add(bootstep)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:168:celery_app.autodiscover_tasks(
HEAD:backend/onyx/background/celery/apps/docprocessing.py:171:            "onyx.background.celery.tasks.docprocessing",
HEAD:backend/onyx/background/celery/apps/docprocessing.py:172:            "onyx.background.celery.tasks.port",
HEAD:backend/onyx/background/celery/apps/heavy.py:3:from celery import Celery, Task, signals
HEAD:backend/onyx/background/celery/apps/heavy.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/heavy.py:5:from celery.signals import celeryd_init, worker_init, worker_ready, worker_shutdown
HEAD:backend/onyx/background/celery/apps/heavy.py:7:import onyx.background.celery.apps.app_base as app_base
HEAD:backend/onyx/background/celery/apps/heavy.py:8:from onyx.configs.constants import POSTGRES_CELERY_WORKER_HEAVY_APP_NAME
HEAD:backend/onyx/background/celery/apps/heavy.py:10:from onyx.server.metrics.celery_task_metrics import (
HEAD:backend/onyx/background/celery/apps/heavy.py:11:    on_celery_task_postrun,
HEAD:backend/onyx/background/celery/apps/heavy.py:12:    on_celery_task_prerun,
HEAD:backend/onyx/background/celery/apps/heavy.py:13:    on_celery_task_rejected,
HEAD:backend/onyx/background/celery/apps/heavy.py:14:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/heavy.py:15:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/heavy.py:23:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/heavy.py:24:celery_app.config_from_object("onyx.background.celery.configs.heavy")
HEAD:backend/onyx/background/celery/apps/heavy.py:25:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/heavy.py:38:    on_celery_task_prerun(task_id, task)
HEAD:backend/onyx/background/celery/apps/heavy.py:53:    on_celery_task_postrun(task_id, task, state)
HEAD:backend/onyx/background/celery/apps/heavy.py:63:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/apps/heavy.py:69:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/apps/heavy.py:81:    on_celery_task_rejected(None, task_name)
HEAD:backend/onyx/background/celery/apps/heavy.py:84:@celeryd_init.connect
HEAD:backend/onyx/background/celery/apps/heavy.py:85:def on_celeryd_init(sender: str, conf: Any = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/heavy.py:86:    app_base.on_celeryd_init(sender, conf, **kwargs)
HEAD:backend/onyx/background/celery/apps/heavy.py:93:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_HEAVY_APP_NAME)
HEAD:backend/onyx/background/celery/apps/heavy.py:97:    app_base.wait_for_redis(sender, **kwargs)
HEAD:backend/onyx/background/celery/apps/heavy.py:128:    celery_app.steps["worker"].add(bootstep)
HEAD:backend/onyx/background/celery/apps/heavy.py:130:celery_app.autodiscover_tasks(
HEAD:backend/onyx/background/celery/apps/heavy.py:133:            "onyx.background.celery.tasks.pruning",
HEAD:backend/onyx/background/celery/apps/heavy.py:135:            "onyx.background.celery.tasks.build",
HEAD:backend/onyx/background/celery/apps/heavy.py:136:            "onyx.background.celery.tasks.hierarchyfetching",
HEAD:backend/onyx/background/celery/apps/heavy.py:137:            "onyx.background.celery.tasks.capability_checks",
HEAD:backend/onyx/background/celery/apps/light.py:3:from celery import Celery, Task, signals
HEAD:backend/onyx/background/celery/apps/light.py:4:from celery.apps.worker import Worker
HEAD:backend/onyx/background/celery/apps/light.py:5:from celery.signals import celeryd_init, worker_init, worker_ready, worker_shutdown
HEAD:backend/onyx/background/celery/apps/light.py:7:import onyx.background.celery.apps.app_base as app_base
HEAD:backend/onyx/background/celery/apps/light.py:8:from onyx.background.celery.celery_utils import httpx_init_vespa_pool
HEAD:backend/onyx/background/celery/apps/light.py:10:    MANAGED_VESPA,
HEAD:backend/onyx/background/celery/apps/light.py:11:    VESPA_CLOUD_CERT_PATH,
HEAD:backend/onyx/background/celery/apps/light.py:12:    VESPA_CLOUD_KEY_PATH,
HEAD:backend/onyx/background/celery/apps/light.py:14:from onyx.configs.constants import POSTGRES_CELERY_WORKER_LIGHT_APP_NAME
HEAD:backend/onyx/background/celery/apps/light.py:16:from onyx.server.metrics.celery_task_metrics import (
HEAD:backend/onyx/background/celery/apps/light.py:17:    on_celery_task_postrun,
HEAD:backend/onyx/background/celery/apps/light.py:18:    on_celery_task_prerun,
HEAD:backend/onyx/background/celery/apps/light.py:19:    on_celery_task_rejected,
HEAD:backend/onyx/background/celery/apps/light.py:20:    on_celery_task_retry,
HEAD:backend/onyx/background/celery/apps/light.py:21:    on_celery_task_revoked,
HEAD:backend/onyx/background/celery/apps/light.py:29:celery_app = Celery(__name__)
HEAD:backend/onyx/background/celery/apps/light.py:30:celery_app.config_from_object("onyx.background.celery.configs.light")
HEAD:backend/onyx/background/celery/apps/light.py:31:celery_app.Task = app_base.TenantAwareTask  # ty: ignore[invalid-assignment]
HEAD:backend/onyx/background/celery/apps/light.py:44:    on_celery_task_prerun(task_id, task)
HEAD:backend/onyx/background/celery/apps/light.py:59:    on_celery_task_postrun(task_id, task, state)
HEAD:backend/onyx/background/celery/apps/light.py:69:    on_celery_task_retry(task_id, sender)
HEAD:backend/onyx/background/celery/apps/light.py:75:    on_celery_task_revoked(kwargs.get("task_id"), task_name)
HEAD:backend/onyx/background/celery/apps/light.py:88:    on_celery_task_rejected(None, task_name)
HEAD:backend/onyx/background/celery/apps/light.py:91:@celeryd_init.connect
HEAD:backend/onyx/background/celery/apps/light.py:92:def on_celeryd_init(sender: str, conf: Any = None, **kwargs: Any) -> None:
HEAD:backend/onyx/background/celery/apps/light.py:93:    app_base.on_celeryd_init(sender, conf, **kwargs)
HEAD:backend/onyx/background/celery/apps/light.py:107:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_LIGHT_APP_NAME)
HEAD:backend/onyx/background/celery/apps/light.py:113:    if MANAGED_VESPA:
HEAD:backend/onyx/background/celery/apps/light.py:114:        httpx_init_vespa_pool(
HEAD:backend/onyx/background/celery/apps/light.py:116:            ssl_cert=VESPA_CLOUD_CERT_PATH,
```
The repository explicitly references relational persistence, queue/cache and
search/index infrastructure.
The exact active backend depends on deployment mode/configuration and must not
be inferred solely from the existence of these paths.
## Connector and Document-Ingestion Evidence
Evidence lines captured: 350
```text
HEAD:backend/ee/onyx/background/celery/apps/docfetching.py:2:from onyx.background.celery.apps.docfetching import celery_app
HEAD:backend/ee/onyx/background/celery/apps/docprocessing.py:2:from onyx.background.celery.apps.docprocessing import celery_app
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
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:81:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:82:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:83:from onyx.redis.redis_connector_doc_perm_sync import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:84:    RedisConnectorPermissionSync,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:85:    RedisConnectorPermissionSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:118:# 5 seconds more than RetryDocumentIndex STOP_AFTER+MAX_WAIT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:163:def _is_external_doc_permissions_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:170:    if cc_pair.status != ConnectorCredentialPairStatus.ACTIVE:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:173:    sync_config = get_source_perm_sync_config(cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:175:        logger.error("No sync config found for %s", cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:179:        logger.error("No doc sync config found for %s", cc_pair.connector.source)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:182:    # if indexing also does perm sync, don't start running doc_sync until at
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:183:    # least one indexing is done
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
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:845:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:846:    This can happen if the indexing worker hard crashes or is terminated.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:857:    2.2. The indexing watchdog checks the spawned task.
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
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:988:class PermissionSyncCallback(IndexingHeartbeatInterface):
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
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:717:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:718:    This can happen if the indexing worker hard crashes or is terminated.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:729:    2.2. The indexing watchdog checks the spawned task.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:742:    cc_pair_id_str = RedisConnector.get_id_from_fence_key(fence_key)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:754:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:757:    if not redis_connector.external_group_sync.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:761:        payload = redis_connector.external_group_sync.payload
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:772:        redis_connector.external_group_sync.reset()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:783:        payload.celery_task_id, OnyxCeleryQueues.CONNECTOR_EXTERNAL_GROUP_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:787:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:791:        # the celery task was prefetched and is reserved within the indexing worker
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:792:        redis_connector.external_group_sync.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:799:    if redis_connector.external_group_sync.active():
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:814:    redis_connector.external_group_sync.reset()
HEAD:backend/onyx/background/README.md:5:1. Pulling/Indexing documents (from connectors)
HEAD:backend/onyx/background/README.md:6:2. Updating document metadata (from connectors)
HEAD:backend/onyx/background/README.md:7:3. Cleaning up checkpoints and logic around indexing work (indexing indexing checkpoints and index attempt metadata)
HEAD:backend/onyx/background/README.md:16:| Light                     | `apps/light.py`                | `vespa_metadata_sync`, `connector_deletion`, `doc_permissions_upsert`, `checkpoint_cleanup`, `index_attempt_cleanup` |
HEAD:backend/onyx/background/README.md:17:| Heavy                     | `apps/heavy.py`                | `connector_pruning`, `connector_doc_permissions_sync`, `connector_external_group_sync`, `csv_generation`, `sandbox`  |
HEAD:backend/onyx/background/README.md:18:| Docprocessing             | `apps/docprocessing.py`        | `docprocessing`, `port`                                                                                              |
HEAD:backend/onyx/background/README.md:19:| Docfetching               | `apps/docfetching.py`          | `connector_doc_fetching`                                                                                             |
HEAD:backend/onyx/background/README.md:48:- waits for redis, postgres, document index to all be healthy
HEAD:backend/onyx/background/README.md:57:| `check_for_indexing`              | 15s       | Scans for connectors needing indexing → dispatches to `DOCFETCHING` queue                  |
HEAD:backend/onyx/background/README.md:59:| `check_for_pruning`               | 20s       | Finds connectors due for pruning → dispatches to `CONNECTOR_PRUNING` queue                 |
HEAD:backend/onyx/background/README.md:60:| `check_for_connector_deletion`    | 20s       | Processes deletion requests → dispatches to `CONNECTOR_DELETION` queue                     |
HEAD:backend/onyx/background/README.md:62:| `check_for_checkpoint_cleanup`    | 1h        | Cleans up old indexing checkpoints                                                         |
HEAD:backend/onyx/background/README.md:85:Does not interact with the Document Index, it handles the syncs with external systems. Large volume API calls to handle pruning and fetching permissions, etc.
HEAD:backend/onyx/background/README.md:91:### Docprocessing, Docfetching, User File Processing
HEAD:backend/onyx/background/README.md:93:Docprocessing and Docfetching are for indexing documents:
HEAD:backend/onyx/background/README.md:95:- Docfetching runs connectors to pull documents from external APIs (Google Drive, Confluence, etc.), stores batches to file storage, and dispatches docprocessing tasks
HEAD:backend/onyx/background/README.md:96:- Docprocessing retrieves batches, runs the indexing pipeline (chunking, embedding), and indexes into the Document Index
HEAD:backend/onyx/background/README.md:103:- Queue lengths, connector success/failure, connector latencies
HEAD:backend/onyx/background/README.md:109:Workers can expose Prometheus metrics via a standalone HTTP server. Currently docfetching and docprocessing have push-based task lifecycle metrics; the monitoring worker runs pull-based collectors for queue depth and connector health.
HEAD:backend/onyx/background/celery/apps/app_base.py:39:    ENABLE_OPENSEARCH_INDEXING_FOR_ONYX,
HEAD:backend/onyx/background/celery/apps/app_base.py:44:from onyx.document_index.vespa.shared_utils.utils import wait_for_vespa_with_timeout
HEAD:backend/onyx/background/celery/apps/app_base.py:46:from onyx.redis.redis_connector import RedisConnector
HEAD:backend/onyx/background/celery/apps/app_base.py:47:from onyx.redis.redis_connector_delete import RedisConnectorDelete
HEAD:backend/onyx/background/celery/apps/app_base.py:48:from onyx.redis.redis_connector_doc_perm_sync import RedisConnectorPermissionSync
HEAD:backend/onyx/background/celery/apps/app_base.py:49:from onyx.redis.redis_connector_ext_group_sync import RedisConnectorExternalGroupSync
HEAD:backend/onyx/background/celery/apps/app_base.py:50:from onyx.redis.redis_connector_prune import RedisConnectorPrune
HEAD:backend/onyx/background/celery/apps/app_base.py:154:    # prefixes observed when a pruning task finishes and an indexing task
HEAD:backend/onyx/background/celery/apps/app_base.py:236:    if task_id.startswith(RedisConnectorDelete.PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:237:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:239:            RedisConnectorDelete.remove_from_taskset(int(cc_pair_id), task_id, r)
HEAD:backend/onyx/background/celery/apps/app_base.py:242:    if task_id.startswith(RedisConnectorPrune.SUBTASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:243:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:245:            RedisConnectorPrune.remove_from_taskset(int(cc_pair_id), task_id, r)
HEAD:backend/onyx/background/celery/apps/app_base.py:248:    if task_id.startswith(RedisConnectorPermissionSync.SUBTASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:249:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:251:            RedisConnectorPermissionSync.remove_from_taskset(
HEAD:backend/onyx/background/celery/apps/app_base.py:256:    if task_id.startswith(RedisConnectorExternalGroupSync.SUBTASK_PREFIX):
HEAD:backend/onyx/background/celery/apps/app_base.py:257:        cc_pair_id = RedisConnector.get_id_from_task_id(task_id)
HEAD:backend/onyx/background/celery/apps/app_base.py:259:            RedisConnectorExternalGroupSync.remove_from_taskset(
HEAD:backend/onyx/background/celery/apps/app_base.py:322:    # Initialize tracing in workers if credentials are available.
HEAD:backend/onyx/background/celery/apps/app_base.py:669:def wait_for_document_index_or_shutdown() -> None:
HEAD:backend/onyx/background/celery/apps/app_base.py:690:    if ENABLE_OPENSEARCH_INDEXING_FOR_ONYX:
HEAD:backend/onyx/background/celery/apps/app_base.py:692:        from onyx.document_index.opensearch.client import (
HEAD:backend/onyx/background/celery/apps/app_base.py:736:    "onyx.background.celery.tasks.connector_deletion",
HEAD:backend/onyx/background/celery/apps/app_base.py:737:    "onyx.background.celery.tasks.docprocessing",
HEAD:backend/onyx/background/celery/apps/app_base.py:738:    "onyx.background.celery.tasks.docfetching",
HEAD:backend/onyx/background/celery/apps/docfetching.py:14:from onyx.background.celery.tasks.docfetching.worker_shutdown import (
HEAD:backend/onyx/background/celery/apps/docfetching.py:17:from onyx.configs.constants import POSTGRES_CELERY_WORKER_DOCFETCHING_APP_NAME
HEAD:backend/onyx/background/celery/apps/docfetching.py:26:from onyx.server.metrics.indexing_task_metrics import (
HEAD:backend/onyx/background/celery/apps/docfetching.py:27:    on_indexing_task_postrun,
HEAD:backend/onyx/background/celery/apps/docfetching.py:28:    on_indexing_task_prerun,
HEAD:backend/onyx/background/celery/apps/docfetching.py:37:celery_app.config_from_object("onyx.background.celery.configs.docfetching")
HEAD:backend/onyx/background/celery/apps/docfetching.py:52:    on_indexing_task_prerun(task_id, task, kwargs)
HEAD:backend/onyx/background/celery/apps/docfetching.py:68:    on_indexing_task_postrun(task_id, task, kwargs, state)
HEAD:backend/onyx/background/celery/apps/docfetching.py:112:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_DOCFETCHING_APP_NAME)
HEAD:backend/onyx/background/celery/apps/docfetching.py:118:    app_base.wait_for_document_index_or_shutdown()
HEAD:backend/onyx/background/celery/apps/docfetching.py:129:    start_metrics_server("docfetching")
HEAD:backend/onyx/background/celery/apps/docfetching.py:138:        "worker_shutting_down received, flagging docfetching for graceful interrupt."
HEAD:backend/onyx/background/celery/apps/docfetching.py:162:            "onyx.background.celery.tasks.docfetching",
HEAD:backend/onyx/background/celery/apps/docprocessing.py:14:from onyx.background.celery.tasks.docprocessing.batch_counters import (
HEAD:backend/onyx/background/celery/apps/docprocessing.py:15:    on_docprocessing_task_postrun,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:16:    on_docprocessing_task_prerun,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:18:from onyx.configs.constants import POSTGRES_CELERY_WORKER_DOCPROCESSING_APP_NAME
HEAD:backend/onyx/background/celery/apps/docprocessing.py:27:from onyx.server.metrics.indexing_task_metrics import (
HEAD:backend/onyx/background/celery/apps/docprocessing.py:28:    on_indexing_task_postrun,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:29:    on_indexing_task_prerun,
HEAD:backend/onyx/background/celery/apps/docprocessing.py:38:celery_app.config_from_object("onyx.background.celery.configs.docprocessing")
HEAD:backend/onyx/background/celery/apps/docprocessing.py:53:    on_indexing_task_prerun(task_id, task, kwargs)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:54:    on_docprocessing_task_prerun(task_id, task, kwargs)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:70:    on_indexing_task_postrun(task_id, task, kwargs, state)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:71:    on_docprocessing_task_postrun(task_id, task, kwargs, state)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:115:    SqlEngine.set_app_name(POSTGRES_CELERY_WORKER_DOCPROCESSING_APP_NAME)
HEAD:backend/onyx/background/celery/apps/docprocessing.py:117:    # rkuo: Transient errors keep happening in the indexing watchdog threads.
HEAD:backend/onyx/background/celery/apps/docprocessing.py:126:    app_base.wait_for_document_index_or_shutdown()
HEAD:backend/onyx/background/celery/apps/docprocessing.py:137:    start_metrics_server("docprocessing")
HEAD:backend/onyx/background/celery/apps/docprocessing.py:146:# Note: worker_process_init only fires in prefork pool mode. Docprocessing uses
HEAD:backend/onyx/background/celery/apps/docprocessing.py:147:# worker_pool="threads" (see configs/docprocessing.py), so this handler is
HEAD:backend/onyx/background/celery/apps/docprocessing.py:171:            "onyx.background.celery.tasks.docprocessing",
HEAD:backend/onyx/background/celery/apps/heavy.py:99:    app_base.wait_for_document_index_or_shutdown()
HEAD:backend/onyx/background/celery/apps/light.py:126:    app_base.wait_for_document_index_or_shutdown()
HEAD:backend/onyx/background/celery/apps/light.py:162:            "onyx.background.celery.tasks.connector_deletion",
HEAD:backend/onyx/background/celery/apps/light.py:165:            "onyx.background.celery.tasks.docprocessing",
HEAD:backend/onyx/background/celery/apps/monitoring.py:86:        from onyx.server.metrics.indexing_pipeline_setup import (
HEAD:backend/onyx/background/celery/apps/monitoring.py:87:            setup_indexing_pipeline_metrics,
HEAD:backend/onyx/background/celery/apps/monitoring.py:90:        setup_indexing_pipeline_metrics(sender.app)
HEAD:backend/onyx/background/celery/apps/monitoring.py:91:        logger.info("Prometheus indexing pipeline collectors registered")
HEAD:backend/onyx/background/celery/apps/monitoring.py:94:        logger.exception("Failed to register Prometheus indexing pipeline collectors")
HEAD:backend/onyx/background/celery/apps/monitoring.py:101:    Isolated from the indexing-pipeline registration on purpose: that one gates
HEAD:backend/onyx/background/celery/apps/primary.py:30:from onyx.db.indexing_coordination import IndexingCoordination
HEAD:backend/onyx/background/celery/apps/primary.py:31:from onyx.redis.redis_connector_delete import RedisConnectorDelete
HEAD:backend/onyx/background/celery/apps/primary.py:32:from onyx.redis.redis_connector_doc_perm_sync import RedisConnectorPermissionSync
HEAD:backend/onyx/background/celery/apps/primary.py:33:from onyx.redis.redis_connector_ext_group_sync import RedisConnectorExternalGroupSync
HEAD:backend/onyx/background/celery/apps/primary.py:34:from onyx.redis.redis_connector_prune import RedisConnectorPrune
HEAD:backend/onyx/background/celery/apps/primary.py:35:from onyx.redis.redis_connector_stop import RedisConnectorStop
HEAD:backend/onyx/background/celery/apps/primary.py:130:    app_base.wait_for_document_index_or_shutdown()
HEAD:backend/onyx/background/celery/apps/primary.py:197:    RedisConnectorDelete.reset_all(r)
HEAD:backend/onyx/background/celery/apps/primary.py:198:    RedisConnectorPrune.reset_all(r)
HEAD:backend/onyx/background/celery/apps/primary.py:199:    RedisConnectorStop.reset_all(r)
HEAD:backend/onyx/background/celery/apps/primary.py:200:    RedisConnectorPermissionSync.reset_all(r)
HEAD:backend/onyx/background/celery/apps/primary.py:201:    RedisConnectorExternalGroupSync.reset_all(r)
HEAD:backend/onyx/background/celery/apps/primary.py:207:        potentially_orphaned_ids = IndexingCoordination.get_orphaned_index_attempt_ids(
HEAD:backend/onyx/background/celery/apps/primary.py:214:            # handle case where not started or docfetching is done but indexing is not
HEAD:backend/onyx/background/celery/apps/primary.py:234:                    f"cc_pair={attempt.connector_credential_pair_id} "
HEAD:backend/onyx/background/celery/apps/primary.py:354:            "onyx.background.celery.tasks.connector_deletion",
HEAD:backend/onyx/background/celery/apps/primary.py:355:            "onyx.background.celery.tasks.docprocessing",
HEAD:backend/onyx/background/celery/apps/scheduled_tasks.py:99:    app_base.wait_for_document_index_or_shutdown()
HEAD:backend/onyx/background/celery/apps/user_file_processing.py:63:    # rkuo: Transient errors keep happening in the indexing watchdog threads.
HEAD:backend/onyx/background/celery/apps/user_file_processing.py:72:    app_base.wait_for_document_index_or_shutdown()
HEAD:backend/onyx/background/celery/celery_redis.py:71:    There can be other tasks in here besides indexing tasks, so this is mostly useful
HEAD:backend/onyx/background/celery/celery_redis.py:83:    Unacked entries belonging to the indexing queues are "prefetched", so this gives
HEAD:backend/onyx/background/celery/celery_redis.py:188:    # filter for and create an indexing specific inspect object
HEAD:backend/onyx/background/celery/celery_utils.py:14:from onyx.connectors.connector_runner import CheckpointOutputWrapper
HEAD:backend/onyx/background/celery/celery_utils.py:15:from onyx.connectors.cross_connector_utils.rate_limit_wrapper import rate_limit_builder
HEAD:backend/onyx/background/celery/celery_utils.py:16:from onyx.connectors.interfaces import (
HEAD:backend/onyx/background/celery/celery_utils.py:17:    BaseConnector,
HEAD:backend/onyx/background/celery/celery_utils.py:18:    CheckpointedConnector,
HEAD:backend/onyx/background/celery/celery_utils.py:19:    ConnectorCheckpoint,
HEAD:backend/onyx/background/celery/celery_utils.py:20:    LoadConnector,
HEAD:backend/onyx/background/celery/celery_utils.py:21:    PollConnector,
HEAD:backend/onyx/background/celery/celery_utils.py:22:    SlimConnector,
HEAD:backend/onyx/background/celery/celery_utils.py:23:    SlimConnectorWithPermSync,
HEAD:backend/onyx/background/celery/celery_utils.py:25:from onyx.connectors.models import (
HEAD:backend/onyx/background/celery/celery_utils.py:26:    ConnectorFailure,
HEAD:backend/onyx/background/celery/celery_utils.py:36:from onyx.indexing.indexing_heartbeat import IndexingHeartbeatInterface
HEAD:backend/onyx/background/celery/celery_utils.py:45:CT = TypeVar("CT", bound=ConnectorCheckpoint)
HEAD:backend/onyx/background/celery/celery_utils.py:48:class SlimConnectorExtractionResult(BaseModel):
HEAD:backend/onyx/background/celery/celery_utils.py:49:    """Result of extracting document IDs and hierarchy nodes from a connector.
HEAD:backend/onyx/background/celery/celery_utils.py:61:    connector: CheckpointedConnector[CT],
HEAD:backend/onyx/background/celery/celery_utils.py:64:) -> Generator[list[Document | HierarchyNode | ConnectorFailure], None, None]:
HEAD:backend/onyx/background/celery/celery_utils.py:67:    Some checkpointed connectors (e.g. IMAP) are multi-step: the first
```
Connector ingestion, document processing and indexing are distinct
security-relevant surfaces.
The end-to-end data path remains to be traced.
## Authentication and Authorization Evidence
Evidence lines captured: 350
```text
HEAD:backend/ee/onyx/access/access.py:1:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/access/access.py:11:from ee.onyx.external_permissions.sync_params import get_source_perm_sync_config
HEAD:backend/ee/onyx/access/access.py:29:    db_session: Session,
HEAD:backend/ee/onyx/access/access.py:31:    id_to_access = _get_access_for_documents([document_id], db_session)
HEAD:backend/ee/onyx/access/access.py:46:    db_session: Session,
HEAD:backend/ee/onyx/access/access.py:50:        db_session=db_session,
HEAD:backend/ee/onyx/access/access.py:55:            db_session=db_session,
HEAD:backend/ee/onyx/access/access.py:60:        db_session=db_session,
HEAD:backend/ee/onyx/access/access.py:67:        db_session=db_session,
HEAD:backend/ee/onyx/access/access.py:71:    all_public_ext_u_group_ids = set(fetch_public_external_group_ids(db_session))
HEAD:backend/ee/onyx/access/access.py:102:        # If its censored, then it's public anywhere during the search and then permissions are
HEAD:backend/ee/onyx/access/access.py:136:    db_session: Session,
HEAD:backend/ee/onyx/access/access.py:147:        user_file_ids, db_session, eager_load_groups=True
HEAD:backend/ee/onyx/access/access.py:184:def _get_acl_for_user(user: User, db_session: Session) -> set[str]:
HEAD:backend/ee/onyx/access/access.py:194:        [] if is_anonymous else fetch_user_groups_for_user(db_session, user.id)
HEAD:backend/ee/onyx/access/access.py:201:        [] if is_anonymous else fetch_external_groups_for_user(db_session, user.id)
HEAD:backend/ee/onyx/access/access.py:209:    user_acl.update(get_acl_for_user_without_groups(user, db_session))
HEAD:backend/ee/onyx/access/hierarchy_access.py:1:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/access/hierarchy_access.py:7:def _get_user_external_group_ids(db_session: Session, user: User) -> list[str]:
HEAD:backend/ee/onyx/access/hierarchy_access.py:10:    external_groups = fetch_external_groups_for_user(db_session, user.id)
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:16:from ee.onyx.db.tenant_sso_domain import (
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:23:from onyx.db.sso_provider import is_valid_email_domain
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:38:def _domain_token(tenant_id: str, domain: str) -> str:
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:40:    tenant's published record cannot verify another's claim, and unguessable
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:43:    message = f"sso-domain:{tenant_id}:{domain}".encode()
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:48:def verification_record(tenant_id: str, domain: str) -> tuple[str, str]:
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:52:    return host, f"{_VALUE_PREFIX}{_domain_token(tenant_id, domain)}"
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:77:def verify_domain_via_dns(tenant_id: str, domain: str) -> bool:
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:86:    if not is_claimed_domain(tenant_id, domain):
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:92:    host, expected = verification_record(tenant_id, domain)
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:94:        mark_domain_verified(tenant_id, domain)
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:99:def _proof_still_present(tenant_id: str, domain: str) -> bool:
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:105:    host, expected = verification_record(tenant_id, domain)
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:109:def revalidate_tenant_domains(tenant_id: str) -> None:
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:119:    for record in list_login_domains(tenant_id):
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:123:            if _proof_still_present(tenant_id, record.domain):
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:125:            mark_domain_unverified(tenant_id, record.domain)
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:127:                "Dropped SSO routing for %s: its TXT proof no longer resolves",
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:131:            logger.exception("Failed to re-validate SSO domain %s", record.domain)
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:136:            f"Could not re-validate SSO domains, still routing: {', '.join(failed)}"
HEAD:backend/ee/onyx/auth/users.py:9:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/auth/users.py:11:from onyx.db.enums import Permission
HEAD:backend/ee/onyx/auth/users.py:27:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/auth/users.py:33:    api_key = request.headers.get("Authorization", "").replace("Bearer ", "")
HEAD:backend/ee/onyx/auth/users.py:45:def generate_anonymous_user_jwt_token(tenant_id: str) -> str:
HEAD:backend/ee/onyx/auth/users.py:47:        "tenant_id": tenant_id,
HEAD:backend/ee/onyx/background/celery/apps/heavy.py:7:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/light.py:7:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/monitoring.py:7:            "ee.onyx.background.celery.tasks.tenant_provisioning",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:8:            "ee.onyx.background.celery.tasks.doc_permission_syncing",
HEAD:backend/ee/onyx/background/celery/apps/primary.py:16:            "ee.onyx.background.celery.tasks.sso_domain_revalidation",
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:19:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:53:        "name": "revalidate-sso-domains",
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:54:        "task": OnyxCeleryTask.REVALIDATE_SSO_DOMAINS_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:68:if not MULTI_TENANT:
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:116:        # Log export is rejected in multi-tenant deployments, so its cleanup
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:8:from onyx.db.engine.sql_engine import get_session_with_tenant
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:21:def export_query_history_cleanup_task(*, tenant_id: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:22:    with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:23:        tasks = get_all_query_history_export_tasks(db_session=db_session)
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:27:                delete_task_with_id(db_session=db_session, task_id=task.task_id)
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:39:                delete_task_with_id(db_session=db_session, task_id=task.task_id)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:7:from ee.onyx.server.tenants.product_gating import get_gated_tenants
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:12:    ONYX_CLOUD_TENANT_ID,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:17:from onyx.db.engine.tenant_utils import get_all_tenant_ids
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:19:from onyx.redis.redis_tenant_work_gating import (
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:21:    get_active_tenants,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:26:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:28:from shared_configs.configs import IGNORED_SYNCING_TENANT_LIST
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:30:_FULL_FANOUT_TIMESTAMP_KEY_PREFIX = "tenant_work_gating_last_full_fanout_ms"
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:34:    redis_client: TenantRedisClient, task_name: str, interval_seconds: int
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:48:        # tenant during a Redis hiccup.
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:86:    """a lightweight task used to kick off individual beat tasks per tenant."""
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:89:    redis_client = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:101:    tenant_ids: list[str] = []
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:102:    num_processed_tenants = 0
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:107:    # Tenant-work-gating read path. Resolve once per invocation.
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:111:    active_tenants: set[str] | None = None
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:118:                gate_enabled = OnyxRuntime.get_tenant_work_gating_enabled()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:119:                gate_enforce = OnyxRuntime.get_tenant_work_gating_enforce()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:121:                task_logger.exception("tenant work gating: runtime flag read failed")
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:127:                    OnyxRuntime.get_tenant_work_gating_full_fanout_interval_seconds()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:135:                        ttl_s = OnyxRuntime.get_tenant_work_gating_ttl_seconds()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:139:                            "tenant work gating: cleanup_expired failed"
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:142:                    ttl_s = OnyxRuntime.get_tenant_work_gating_ttl_seconds()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:143:                    active_tenants = get_active_tenants(ttl_s)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:144:                    if active_tenants is None:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:154:        tenant_ids = get_all_tenant_ids()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:156:        # Per-task control over whether gated tenants are included. Most periodic tasks
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:157:        # do no useful work on gated tenants and just waste DB connections fanning out
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:158:        # to ~10k+ inactive tenants. A small number of cleanup tasks (connector deletion,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:159:        # checkpoint/index attempt cleanup) need to run on gated tenants and pass
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:161:        gated_tenants: set[str] = get_gated_tenants() if skip_gated else set()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:163:        for tenant_id in tenant_ids:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:164:            if tenant_id in gated_tenants:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:174:            if IGNORED_SYNCING_TENANT_LIST and tenant_id in IGNORED_SYNCING_TENANT_LIST:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:177:            # Tenant work gate: if the feature is on, check membership. Skip
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:178:            # unmarked tenants when enforce=True AND we're not in a full-
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:182:                    active_tenants is not None and tenant_id not in active_tenants
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:195:                    tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:203:            num_processed_tenants += 1
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:223:        f"num_processed_tenants={num_processed_tenants} "
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:231:        f"num_tenants={len(tenant_ids)} "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:14:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:24:from ee.onyx.external_permissions.sync_params import get_source_perm_sync_config
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:38:    CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:50:from onyx.db.connector import mark_cc_pair_as_permissions_synced
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:58:    get_session_with_current_tenant,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:59:    get_session_with_tenant,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:69:    update_hierarchy_node_permissions as db_update_hierarchy_node_permissions,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:72:from onyx.db.permission_sync_attempt import (
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:73:    complete_doc_permission_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:74:    create_doc_permission_sync_attempt,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:75:    mark_doc_permission_sync_attempt_failed,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:76:    mark_doc_permission_sync_attempt_in_progress,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:84:    RedisConnectorPermissionSync,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:85:    RedisConnectorPermissionSyncPayload,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:92:from onyx.redis.redis_tenant_work_gating import maybe_mark_tenant_active
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:93:from onyx.redis.tenant_redis_client import TenantRedisClient
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:103:    doc_permission_sync_ctx,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:108:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:113:DOCUMENT_PERMISSIONS_UPDATE_MAX_RETRIES = 3
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:114:DOCUMENT_PERMISSIONS_UPDATE_STOP_AFTER = 10 * 60
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:115:DOCUMENT_PERMISSIONS_UPDATE_MAX_WAIT = 60
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:126:    Base expiration is 300 seconds, multiplied by the beat multiplier only in MULTI_TENANT mode.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:130:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:141:"""Jobs / utils for kicking off doc permissions sync tasks."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:144:def _fail_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:149:    docs_with_permission_errors: int = 0,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:151:    """Helper to mark a doc permission sync attempt as failed with an error message."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:152:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:153:        mark_doc_permission_sync_attempt_failed(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:155:            db_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:159:            docs_with_permission_errors=docs_with_permission_errors,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:163:def _is_external_doc_permissions_sync_due(cc_pair: ConnectorCredentialPair) -> bool:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:164:    """Returns boolean indicating if external doc permissions sync is due."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:169:    # skip doc permissions sync if not active
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:196:    source_sync_period *= int(OnyxRuntime.get_doc_permission_sync_multiplier())
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:207:    name=OnyxCeleryTask.CHECK_FOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:212:def check_for_doc_permissions_sync(self: Task, *, tenant_id: str) -> bool | None:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:221:        OnyxRedisLocks.CHECK_CONNECTOR_DOC_PERMISSIONS_SYNC_BEAT_LOCK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:232:        with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:233:            cc_pairs = get_all_auto_sync_cc_pairs(db_session)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:238:                if _is_external_doc_permissions_sync_due(cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:241:        # Tenant-work-gating hook: refresh this tenant's active-set membership
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:242:        # whenever doc-permission sync has any due cc_pairs to dispatch.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:244:            maybe_mark_tenant_active(tenant_id, caller="doc_permission_sync")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:248:            payload_id = try_creating_permissions_sync_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:249:                self.app, cc_pair_id, r, tenant_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:255:                f"Permissions sync queued: cc_pair={cc_pair_id} id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:260:        if not r.exists(OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:261:            # clear any permission fences that don't have associated celery tasks in progress
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:266:                validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:267:                    tenant_id, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:271:                    "Exception while validating permission sync fences"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:275:                OnyxRedisSignals.BLOCK_VALIDATE_PERMISSION_SYNC_FENCES,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:292:            if key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:293:                with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:294:                    monitor_ccpair_permissions_taskset(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:295:                        tenant_id, key_bytes, r, db_session
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:297:        task_logger.info(f"check_for_doc_permissions_sync finished: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:305:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:308:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:317:def try_creating_permissions_sync_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:320:    r: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:321:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:329:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:332:        DANSWER_REDIS_FUNCTION_LOCK_PREFIX + "try_generate_permissions_sync_tasks",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:341:        if redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:350:        redis_connector.permissions.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:351:        redis_connector.permissions.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:353:        custom_task_id = f"{redis_connector.permissions.generator_task_key}_{uuid4()}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:358:            with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:360:                    db_session=db_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:362:                    sync_type=SyncType.EXTERNAL_PERMISSIONS,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:368:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:369:        payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:375:        redis_connector.permissions.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:378:            OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:381:                tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:383:            queue=OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:390:        redis_connector.permissions.set_fence(payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:396:            f"Unexpected try_creating_permissions_sync_task exception: cc_pair={cc_pair_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:404:        f"try_creating_permissions_sync_task finished: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:410:    name=OnyxCeleryTask.CONNECTOR_PERMISSION_SYNC_GENERATOR_TASK,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:417:def connector_permission_sync_generator_task(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:420:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:423:    Permission sync task that handles document permission syncing for a given connector credential pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:431:    doc_permission_sync_ctx_dict = dict(doc_permission_sync_ctx.get())
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:432:    doc_permission_sync_ctx_dict["cc_pair_id"] = cc_pair_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:433:    doc_permission_sync_ctx_dict["request_id"] = self.request.id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:434:    doc_permission_sync_ctx.set(doc_permission_sync_ctx_dict)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:436:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:437:        attempt_id = create_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:439:            db_session=db_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:442:            f"Created doc permission sync attempt: {attempt_id} for cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:445:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:456:                f"connector_permission_sync_generator_task - timed out waiting for fence to be ready: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:457:                f"fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:459:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:462:        if not redis_connector.permissions.fenced:  # The fence must exist
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:463:            error_msg = f"connector_permission_sync_generator_task - fence not found: fence={redis_connector.permissions.fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:464:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:467:        payload = redis_connector.permissions.payload  # The payload must exist
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:470:                "connector_permission_sync_generator_task: payload invalid or not found"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:472:            _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:477:                "connector_permission_sync_generator_task - Waiting for fence: fence=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:478:                redis_connector.permissions.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:486:            "connector_permission_sync_generator_task - Fence found, continuing...: fence=%s payload_id=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:487:            redis_connector.permissions.fence_key,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:493:        OnyxRedisLocks.CONNECTOR_DOC_PERMISSIONS_SYNC_LOCK_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:495:        timeout=CELERY_PERMISSIONS_SYNC_LOCK_TIMEOUT,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:502:            f"Permission sync task already running, exiting...: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:505:        _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:513:        # Scoped to setup, never across the crawl below: on multi-tenant this session
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:516:        with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:518:                db_session=db_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:533:                    db_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:543:                    f"validate_ccpair_permissions_sync exceptioned: cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:554:                _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:560:                    _fail_doc_permission_sync_attempt(attempt_id, error_msg)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:569:            mark_doc_permission_sync_attempt_in_progress(attempt_id, db_session)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:571:            payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:575:            new_payload = RedisConnectorPermissionSyncPayload(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:581:            redis_connector.permissions.set_fence(new_payload)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:583:            callback = PermissionSyncCallback(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:595:            with get_session_with_current_tenant() as fetch_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:598:                        db_session=fetch_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:606:            with get_session_with_current_tenant() as fetch_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:608:                    db_session=fetch_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:624:            f"RedisConnector.permissions.generate_tasks starting. cc_pair={cc_pair_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:630:                    f"Permission sync task timed out or stop signal detected: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:635:            result = redis_connector.permissions.update_db(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:637:                new_permissions=[doc_external_access],
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:647:            f"RedisConnector.permissions.generate_tasks finished. "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:655:        with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:656:            complete_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:657:                db_session=db_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:660:                docs_with_permission_errors=docs_with_errors,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:663:            f"Completed doc permission sync attempt {attempt_id}: {tasks_generated} docs, {docs_with_errors} errors"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:666:        redis_connector.permissions.generator_complete = tasks_generated
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:673:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:676:            f"Permission sync exceptioned: cc_pair={cc_pair_id} payload_id={payload_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:679:        _fail_doc_permission_sync_attempt(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:684:            docs_with_permission_errors=docs_with_errors,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:687:        redis_connector.permissions.generator_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:688:        redis_connector.permissions.taskset_clear()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:689:        redis_connector.permissions.set_fence(None)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:697:        f"Permission sync finished: cc_pair={cc_pair_id} payload_id={payload.id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:705:        multiplier=1, max=DOCUMENT_PERMISSIONS_UPDATE_MAX_WAIT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:707:    stop=stop_after_delay(DOCUMENT_PERMISSIONS_UPDATE_STOP_AFTER),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:709:def element_update_permissions(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:710:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:711:    permissions: ElementExternalAccess,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:716:    """Update permissions for a document or hierarchy node."""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:718:    external_access = permissions.external_access
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:721:    if isinstance(permissions, DocExternalAccess):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:722:        element_id = permissions.doc_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:725:        element_id = permissions.raw_node_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:729:        with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:732:                db_session=db_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:737:            if isinstance(permissions, DocExternalAccess):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:738:                # Document permission update
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:740:                    db_session=db_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:741:                    doc_id=permissions.doc_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:747:                    # If a new document was created, we associate it with the cc_pair
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:749:                        db_session=db_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:752:                        document_ids=[permissions.doc_id],
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:755:                # Hierarchy node permission update
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:756:                db_update_hierarchy_node_permissions(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:757:                    db_session=db_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:758:                    raw_node_id=permissions.raw_node_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:759:                    source=DocumentSource(permissions.source),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:775:                f"{element_type}={element_id} action=update_permissions elapsed={elapsed:.2f}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:779:            f"element_update_permissions exceptioned: {element_type}={element_id}, {connector_id=} {credential_id=}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:784:            f"element_update_permissions completed: {element_type}={element_id}, {connector_id=} {credential_id=}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:790:def validate_permission_sync_fences(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:791:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:792:    r: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:793:    r_replica: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:799:    PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN = 1024
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:802:        OnyxCeleryQueues.DOC_PERMISSIONS_UPSERT, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:804:    if queue_len > PERMISSION_SYNC_VALIDATION_MAX_QUEUE_LEN:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:808:        OnyxCeleryQueues.DOC_PERMISSIONS_UPSERT, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:811:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC, r_celery
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:814:    # validate all existing permission sync jobs
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:820:        if not key_str.startswith(RedisConnectorPermissionSync.FENCE_PREFIX):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:823:        validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:824:            tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:837:def validate_permission_sync_fence(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:838:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:842:    r: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:845:    """Checks for the error condition where an indexing fence is set but the associated celery tasks don't exist.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:868:    queued_tasks: the celery queue of lightweight permission sync tasks
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:876:            f"validate_permission_sync_fence - could not parse id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:882:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:885:    if not redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:892:        payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:895:            "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:901:        redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:915:        OnyxCeleryQueues.CONNECTOR_DOC_PERMISSIONS_SYNC,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:920:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:925:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:929:    # every entry in the taskset should have an associated entry in the celery task queue
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:930:    # because we get the celery tasks first, the entries in our own permissions taskset
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:943:    for member in r.sscan_iter(redis_connector.permissions.taskset_key):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:956:        f"validate_permission_sync_fence task check: tasks_scanned={tasks_scanned} tasks_not_in_celery={tasks_not_in_celery}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:961:        redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:968:    # if we get here, we didn't find any direct indication that the associated celery tasks exist,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:972:    if redis_connector.permissions.active():
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:977:        "validate_permission_sync_fence - "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:978:        "Resetting fence because no associated celery tasks were found: "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:984:    redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:988:class PermissionSyncCallback(IndexingHeartbeatInterface):
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:995:        redis_client: TenantRedisClient,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1006:        self.last_tag: str = "PermissionSyncCallback.__init__"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1023:                    "PermissionSyncCallback - task timeout exceeded: elapsed=%ss timeout=%ss cc_pair=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1034:            self.redis_connector.permissions.set_active()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1047:                "PermissionSyncCallback - lock.reacquire exceptioned: lock_timeout=%s start=%s last_tag=%s last_reacquired=%s now=%s",
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1059:"""Monitoring CCPair permissions utils"""
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1062:def monitor_ccpair_permissions_taskset(
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1063:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1065:    r: TenantRedisClient,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1066:    db_session: Session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1072:            f"monitor_ccpair_permissions_taskset: could not parse cc_pair_id from {fence_key}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1078:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1079:    if not redis_connector.permissions.fenced:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1082:    initial = redis_connector.permissions.generator_complete
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1087:        payload = redis_connector.permissions.payload
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1090:            "Permissions sync payload failed to validate. Schema may have been updated."
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1097:    remaining = redis_connector.permissions.get_remaining()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1099:        f"Permissions sync progress: cc_pair={cc_pair_id} id={payload.id} remaining={remaining} initial={initial}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1102:    # Add telemetry for permission syncing progress
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1104:        record_type=RecordType.PERMISSION_SYNC_PROGRESS,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1110:        tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1116:    mark_cc_pair_as_permissions_synced(db_session, int(cc_pair_id), payload.started)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1118:        f"Permissions sync finished: cc_pair={cc_pair_id} id={payload.id} num_synced={initial}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1121:    # Add telemetry for permission syncing complete
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1123:        record_type=RecordType.PERMISSION_SYNC_COMPLETE,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1125:        tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1129:        db_session=db_session,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1131:        sync_type=SyncType.EXTERNAL_PERMISSIONS,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1136:    redis_connector.permissions.reset()
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:1:from sqlalchemy.orm import Session
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:3:from ee.onyx.external_permissions.sync_params import (
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:12:    db_session: Session, cc_pair: ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:18:        db_session, cc_pair.connector.source
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:24:    db_session: Session, cc_pair: ConnectorCredentialPair
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:28:    cc_pair_ids = _get_all_cc_pair_ids_to_mark_as_group_synced(db_session, cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/group_sync_utils.py:30:        mark_cc_pair_as_external_group_synced(db_session, cc_pair_id)
```
Authentication, authorization, permissions, roles and tenant-related code
are clearly present.
No claim is made yet that every API route is correctly protected.
## Network / Port Evidence
Evidence lines captured: 19
```text
79:    # ports:
80:    #   - "8080:8080"
113:          "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')",
233:          "require('http').get('http://127.0.0.1:3000/', (r) => process.exit(r.statusCode < 500 ? 0 : 1)).on('error', () => process.exit(1))",
315:          "import urllib.request; urllib.request.urlopen('http://localhost:9000/api/health')",
360:          "import urllib.request; urllib.request.urlopen('http://localhost:9000/api/health')",
384:    # ports:
385:    #   - "5432:5432"
452:      - DOMAIN=localhost
457:    ports:
459:      - "${HOST_PORT:-3000}:80" # allow for localhost:3000 usage, since that is the norm
491:          "http://127.0.0.1/nginx-health",
504:    # ports:
505:    #   - "6379:6379"
521:    image: quay.io/minio/minio:RELEASE.2025-09-07T16-13-09Z-cpuv1@sha256:13582eff79c6605a2d315bdd0e70164142ea7e98fc8411e9e10d089502a6d883
527:    # ports:
528:    #   - "9004:9000"
529:    #   - "9005:9001"
569:          "import json,urllib.request; r = json.load(urllib.request.urlopen('http://localhost:8000/health', timeout=5)); raise SystemExit(0 if r['status'] == 'ok' else 1)",
```
Network declarations are configuration evidence only. Runtime exposure has
not been tested.
## Deployment Mode Documentation
```text
## 🚀 Deployment Modes

> Onyx supports deployments in Docker, Kubernetes, Helm/Terraform and provides guides for major cloud providers.
> Detailed deployment guides found [here](https://docs.onyx.app/deployment/overview).

Onyx supports two separate deployment options: standard and lite.

#### Onyx Lite

The Lite mode can be thought of as a lightweight Chat UI. It requires less resources (under 1GB memory) and runs a less complex stack.
It is great for users who want to test out Onyx quickly or for teams who are only interested in the Chat UI and Agents functionalities.

#### Standard Onyx

The complete feature set of Onyx which is recommended for serious users and larger teams. Additional components not included in Lite mode:
- Vector + Keyword index for RAG.
- Background containers to run job queues and workers for syncing knowledge from connectors.
- AI model inference servers to run deep learning models used during indexing and inference.
- Performance optimizations for large scale use via in memory cache (Redis) and blob store (MinIO).

> [!TIP]
> **To try Onyx for free without deploying, visit [Onyx Cloud](https://cloud.onyx.app/signup?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme)**.

---

## 🏢 Onyx for Enterprise
```
## Current Architecture Model
Based on source/configuration evidence, the major architectural categories
requiring continued tracing are:
1. Web/client surface.
2. Reverse proxy / ingress surface where configured.
3. Backend HTTP/API application.
4. Authentication, authorization and tenant-control code.
5. Relational persistence.
6. Cache / asynchronous queue infrastructure.
7. Background task workers.
8. Connector and document-ingestion pipeline.
9. Search/index infrastructure.
10. Model-serving / embedding / reranking infrastructure.
11. LLM/chat orchestration code.
12. MCP integration/service surface.
13. Sandboxed or isolated execution functionality where configured.
14. Deployment/configuration control plane.
## Candidate Trust Boundaries
These are **candidates**, not final conclusions:
- external user/browser -> web or ingress;
- web/client -> backend API;
- backend API -> persistence systems;
- backend API -> queue/cache infrastructure;
- background workers -> persistence/search systems;
- ingestion/connectors -> internal document-processing pipeline;
- document-processing pipeline -> search/index infrastructure;
- application orchestration -> model/LLM services;
- application/MCP surface -> tools or external integrations;
- sandbox controller -> isolated execution environment.
Each boundary requires later source-flow or runtime verification.
## Safety Record
During Action 6.3:
- Onyx application execution: NO
- Docker execution: NO
- Dependency installation: NO
- Database startup: NO
- Database migrations: NO
- Network probing: NO
- External AI API invocation: NO
- Production credentials: NO
- Production/customer data: NO
- Onyx source modification: NO
## Interpretation Boundary
This action establishes the first component-responsibility model.
It does **not** yet prove:
- runtime startup ordering;
- actual inter-service traffic;
- authentication middleware ordering;
- route-level authorization correctness;
- tenant-isolation guarantees;
- credential propagation behavior;
- RAG document lifecycle;
- retrieval/reranking sequence;
- LLM provider call sequence;
- tool execution authorization;
- MCP trust decisions;
- deletion/revocation behavior;
- logging/data-leak behavior.
## Result
Action 6.3 major component and responsibility mapping: **PASS**.
