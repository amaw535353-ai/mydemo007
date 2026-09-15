# Phase 6 Action 6.5 - Identity and Request-Context Flow Trace
## Purpose
Trace the security-critical request context through Onyx using static source
evidence.
The target flow is:
external request -> application/router -> authentication -> user identity ->
tenant context -> permission decision -> object/resource access.
This action does not test whether those controls are bypassable.
## Verified Baseline
- Evidence branch: `security/phase-6-onyx-baseline`
- Action 6.4 parent: `3d9d102b5857124bd17856e9a2d8932fa1dca4ff`
- Onyx repository: `https://github.com/onyx-dot-app/onyx.git`
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx source clean: PASS
## Application and Middleware Wiring
Evidence lines: 167
```text
HEAD:backend/ee/onyx/main.py:26:from ee.onyx.server.middleware.tenant_tracking import (
HEAD:backend/ee/onyx/main.py:27:    add_api_server_tenant_id_middleware,
HEAD:backend/ee/onyx/main.py:37:from ee.onyx.server.tenants.api import router as tenants_router
HEAD:backend/ee/onyx/main.py:55:    include_router_with_global_prefix_prepended,
HEAD:backend/ee/onyx/main.py:58:from onyx.main import lifespan as lifespan_base
HEAD:backend/ee/onyx/main.py:62:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/main.py:68:async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
HEAD:backend/ee/onyx/main.py:69:    """Small wrapper around the lifespan of the MIT application.
HEAD:backend/ee/onyx/main.py:70:    Basically just calls the base lifespan, and then adds EE-only
HEAD:backend/ee/onyx/main.py:73:    async with lifespan_base(app):
HEAD:backend/ee/onyx/main.py:88:    application = get_application_base(lifespan_override=lifespan)
HEAD:backend/ee/onyx/main.py:92:    # AFTER tenant_tracking has populated CURRENT_TENANT_ID_CONTEXTVAR.
HEAD:backend/ee/onyx/main.py:95:    add_tier_gate_middleware(application, logger)
HEAD:backend/ee/onyx/main.py:97:    if MULTI_TENANT:
HEAD:backend/ee/onyx/main.py:98:        add_api_server_tenant_id_middleware(application, logger)
HEAD:backend/ee/onyx/main.py:102:        # MT deployments use control plane gating via is_tenant_gated() instead
HEAD:backend/ee/onyx/main.py:103:        add_license_enforcement_middleware(application, logger)
HEAD:backend/ee/onyx/main.py:105:    if MULTI_TENANT:
HEAD:backend/ee/onyx/main.py:106:        # For Google OAuth, refresh tokens are requested by:
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
HEAD:backend/ee/onyx/main.py:167:    if MULTI_TENANT:
HEAD:backend/ee/onyx/main.py:168:        # Tenant management
HEAD:backend/ee/onyx/main.py:169:        include_router_with_global_prefix_prepended(application, tenants_router)
HEAD:backend/ee/onyx/main.py:174:    application.include_router(scim_router)
HEAD:backend/onyx/main.py:11:from fastapi import APIRouter, FastAPI, HTTPException, Request, status
HEAD:backend/onyx/main.py:12:from fastapi.exceptions import RequestValidationError
HEAD:backend/onyx/main.py:19:from starlette.types import Lifespan
HEAD:backend/onyx/main.py:61:from onyx.db.engine.sql_engine import SqlEngine, get_session_with_current_tenant
HEAD:backend/onyx/main.py:168:from onyx.server.utils import BasicAuthenticationError
HEAD:backend/onyx/main.py:169:from onyx.setup import setup_multitenant_onyx, setup_onyx
HEAD:backend/onyx/main.py:175:    add_onyx_request_id_middleware,
HEAD:backend/onyx/main.py:187:    MULTI_TENANT,
HEAD:backend/onyx/main.py:192:from shared_configs.contextvars import CURRENT_TENANT_ID_CONTEXTVAR
HEAD:backend/onyx/main.py:210:def validation_exception_handler(request: Request, exc: Exception) -> JSONResponse:
HEAD:backend/onyx/main.py:211:    if not isinstance(exc, RequestValidationError):
HEAD:backend/onyx/main.py:218:    logger.exception("%s: %s", request, exc_str)
HEAD:backend/onyx/main.py:230:def value_error_handler(_: Request, exc: Exception) -> JSONResponse:
HEAD:backend/onyx/main.py:246:            **OnyxErrorCode.BAD_REQUEST.detail(str(exc)),
HEAD:backend/onyx/main.py:265:def include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:281:    application.include_router(router, **final_kwargs)
HEAD:backend/onyx/main.py:292:    include_router_with_global_prefix_prepended(
HEAD:backend/onyx/main.py:318:    Raises RuntimeError if DISABLE_VECTOR_DB is set alongside MULTI_TENANT or ENABLE_CRAFT,
HEAD:backend/onyx/main.py:324:    if MULTI_TENANT:
HEAD:backend/onyx/main.py:326:            "DISABLE_VECTOR_DB cannot be used with MULTI_TENANT. "
HEAD:backend/onyx/main.py:327:            "Multi-tenant deployments require the vector database for "
HEAD:backend/onyx/main.py:328:            "per-tenant document indexing and search. Run in single-tenant "
HEAD:backend/onyx/main.py:344:async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:  # noqa: ARG001
HEAD:backend/onyx/main.py:414:    if not MULTI_TENANT:
HEAD:backend/onyx/main.py:416:        CURRENT_TENANT_ID_CONTEXTVAR.set(POSTGRES_DEFAULT_SCHEMA)
HEAD:backend/onyx/main.py:419:        # If we are multi-tenant, we need to only set up initial public tables
HEAD:backend/onyx/main.py:420:        with get_session_with_current_tenant() as db_session:
HEAD:backend/onyx/main.py:428:            # set up the file store (e.g. create bucket if needed). On multi-tenant,
HEAD:backend/onyx/main.py:432:        setup_multitenant_onyx()
HEAD:backend/onyx/main.py:434:    if not MULTI_TENANT:
HEAD:backend/onyx/main.py:487:def log_http_error(request: Request, exc: Exception) -> JSONResponse:
HEAD:backend/onyx/main.py:490:    if isinstance(exc, BasicAuthenticationError):
HEAD:backend/onyx/main.py:491:        # For BasicAuthenticationError, just log a brief message without stack trace
HEAD:backend/onyx/main.py:493:        logger.debug("Authentication failed: %s", str(exc))
HEAD:backend/onyx/main.py:495:    elif status_code == 404 and request.url.path == "/metrics":
HEAD:backend/onyx/main.py:516:def get_application(lifespan_override: Lifespan | None = None) -> FastAPI:
HEAD:backend/onyx/main.py:517:    application = FastAPI(
HEAD:backend/onyx/main.py:530:        lifespan=lifespan_override or lifespan,
HEAD:backend/onyx/main.py:542:    application.add_exception_handler(status.HTTP_400_BAD_REQUEST, log_http_error)
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
HEAD:backend/onyx/main.py:711:    # The only SAML router. Always mounted: it resolves provider rows per request
HEAD:backend/onyx/main.py:713:    # requests when no rows exist, so it ships dark. A single-SAML deployment's row is seeded from
HEAD:backend/onyx/main.py:721:    # provider rows per request and 404s when none exist, so it ships dark.
HEAD:backend/onyx/main.py:728:    # run. Mounted unconditionally: single-tenant answers from its one schema.
HEAD:backend/onyx/main.py:741:        RequestValidationError, validation_exception_handler
HEAD:backend/onyx/main.py:749:            "requests will be served without credentials. Set "
HEAD:backend/onyx/main.py:751:            "credentialed cross-origin requests."
HEAD:backend/onyx/main.py:753:    application.add_middleware(
HEAD:backend/onyx/main.py:763:    application.add_middleware(CaptchaCookieMiddleware)
HEAD:backend/onyx/main.py:764:    application.add_middleware(LoginCaptchaMiddleware)
HEAD:backend/onyx/main.py:769:    # ``current_client_ip()`` rather than threading the request through.
HEAD:backend/onyx/main.py:770:    application.add_middleware(ClientIPMiddleware)
HEAD:backend/onyx/main.py:773:        add_latency_logging_middleware(application, logger)
HEAD:backend/onyx/main.py:775:    add_onyx_request_id_middleware(application, "API", logger)
HEAD:backend/onyx/main.py:779:    add_endpoint_context_middleware(application)
HEAD:backend/onyx/main.py:781:    # HTTP request metrics (latency histograms, in-progress gauge, slow request
HEAD:backend/onyx/main.py:783:    # instrumentator adds middleware via app.add_middleware().
```
## Authentication Backend Evidence
Evidence lines: 125
```text
HEAD:backend/ee/onyx/auth/users.py:4:import jwt
HEAD:backend/ee/onyx/auth/users.py:45:def generate_anonymous_user_jwt_token(tenant_id: str) -> str:
HEAD:backend/ee/onyx/auth/users.py:52:    return jwt.encode(payload, USER_AUTH_SECRET, algorithm="HS256")
HEAD:backend/ee/onyx/auth/users.py:55:def decode_anonymous_user_jwt_token(token: str) -> dict:
HEAD:backend/ee/onyx/auth/users.py:56:    return jwt.decode(token, USER_AUTH_SECRET, algorithms=["HS256"])
HEAD:backend/onyx/auth/jwt.py:6:import jwt
HEAD:backend/onyx/auth/jwt.py:9:from jwt import (
HEAD:backend/onyx/auth/jwt.py:14:    PyJWTError,
HEAD:backend/onyx/auth/jwt.py:16:from jwt import decode as jwt_decode
HEAD:backend/onyx/auth/jwt.py:17:from jwt.algorithms import RSAAlgorithm  # ty: ignore[possibly-missing-import]
HEAD:backend/onyx/auth/jwt.py:48:    """Fetch and cache the raw JWT verification material. A DB-origin URL is
HEAD:backend/onyx/auth/jwt.py:69:        logger.error("Failed to fetch JWT public key: %s", str(exc))
HEAD:backend/onyx/auth/jwt.py:79:            logger.error("JWT public key URL returned invalid JSON")
HEAD:backend/onyx/auth/jwt.py:86:            "JWT public key URL returned JSON but no JWKS 'keys' field was found"
HEAD:backend/onyx/auth/jwt.py:92:        logger.error("JWT public key URL returned an empty response")
HEAD:backend/onyx/auth/jwt.py:104:    """Return the concrete public key used to verify the provided JWT token."""
HEAD:backend/onyx/auth/jwt.py:129:        header = jwt.get_unverified_header(token)
HEAD:backend/onyx/auth/jwt.py:130:    except PyJWTError as e:
HEAD:backend/onyx/auth/jwt.py:131:        logger.error("Unable to parse JWT header: %s", str(e))
HEAD:backend/onyx/auth/jwt.py:170:async def verify_jwt_token(token: str) -> dict[str, Any] | None:
HEAD:backend/onyx/auth/jwt.py:172:    if settings.jwt_public_key_url is None:
HEAD:backend/onyx/auth/jwt.py:173:        logger.error("JWT public key URL is not configured")
HEAD:backend/onyx/auth/jwt.py:178:    operator_pinned = "jwt_public_key_url" in env_pinned_active_fields()
HEAD:backend/onyx/auth/jwt.py:181:            validate_idp_url(settings.jwt_public_key_url, field="jwt_public_key_url")
HEAD:backend/onyx/auth/jwt.py:183:            logger.error("JWT public key URL rejected: %s", e)
HEAD:backend/onyx/auth/jwt.py:189:            settings.jwt_public_key_url,
HEAD:backend/onyx/auth/jwt.py:194:            logger.error("Unable to resolve a public key for JWT verification")
HEAD:backend/onyx/auth/jwt.py:203:            payload = jwt_decode(
HEAD:backend/onyx/auth/jwt.py:207:                audience=settings.jwt_expected_audience,
HEAD:backend/onyx/auth/jwt.py:208:                issuer=settings.jwt_expected_issuer,
HEAD:backend/onyx/auth/jwt.py:209:                options={"verify_aud": settings.jwt_expected_audience is not None},
HEAD:backend/onyx/auth/jwt.py:218:            logger.warning("JWT rejected by aud/iss enforcement: %s", str(e))
HEAD:backend/onyx/auth/jwt.py:221:            logger.error("Invalid JWT token: %s", str(e))
HEAD:backend/onyx/auth/jwt.py:226:        except PyJWTError as e:
HEAD:backend/onyx/auth/jwt.py:227:            logger.error("JWT decoding error: %s", str(e))
HEAD:backend/onyx/auth/login_claims_capture.py:35:import jwt
HEAD:backend/onyx/auth/login_claims_capture.py:224:    return jwt.decode(
HEAD:backend/onyx/auth/mobile_sso/code_store.py:16:Redis is core infra (always available, even when ``AUTH_BACKEND=jwt``), so this
HEAD:backend/onyx/auth/mobile_sso/tokens.py:6:a self-contained non-revocable JWT under ``AUTH_BACKEND=jwt`` — differing from web
HEAD:backend/onyx/auth/schemas.py:68:class AuthBackend(str, Enum):
HEAD:backend/onyx/auth/schemas.py:71:    JWT = "jwt"
HEAD:backend/onyx/auth/session_tokens.py:11:``read_token`` must return None rather than raise (API keys/PATs/JWTs share the
HEAD:backend/onyx/auth/session_tokens.py:136:    Excludes API keys / PATs / JWTs so their expected misses never classify.
HEAD:backend/onyx/auth/sso_tenant_token.py:13:import jwt
HEAD:backend/onyx/auth/sso_tenant_token.py:14:from fastapi_users.jwt import decode_jwt, generate_jwt
HEAD:backend/onyx/auth/sso_tenant_token.py:33:    return generate_jwt(data, USER_AUTH_SECRET, SSO_TENANT_TOKEN_LIFETIME_SECONDS)
HEAD:backend/onyx/auth/sso_tenant_token.py:40:        payload = decode_jwt(token, USER_AUTH_SECRET, [SSO_TENANT_TOKEN_AUDIENCE])
HEAD:backend/onyx/auth/sso_tenant_token.py:41:    except jwt.PyJWTError as e:
HEAD:backend/onyx/auth/users.py:15:import jwt
HEAD:backend/onyx/auth/users.py:42:    JWTStrategy,
HEAD:backend/onyx/auth/users.py:43:    RedisStrategy,  # ty: ignore[possibly-missing-import]
HEAD:backend/onyx/auth/users.py:48:    DatabaseStrategy,
HEAD:backend/onyx/auth/users.py:51:from fastapi_users.jwt import SecretType, decode_jwt, generate_jwt
HEAD:backend/onyx/auth/users.py:72:from onyx.auth.jwt import verify_jwt_token
HEAD:backend/onyx/auth/users.py:83:from onyx.auth.schemas import AuthBackend, UserCreate
HEAD:backend/onyx/auth/users.py:98:    AUTH_BACKEND,
HEAD:backend/onyx/auth/users.py:635:        # tenant from the JWT email and run the update against a tenant-bound
HEAD:backend/onyx/auth/users.py:638:            data = decode_jwt(
HEAD:backend/onyx/auth/users.py:643:        except jwt.PyJWTError:
HEAD:backend/onyx/auth/users.py:1645:cookie_transport = CookieTransport(
HEAD:backend/onyx/auth/users.py:1655:# (see `mobile_auth_backend` below).
HEAD:backend/onyx/auth/users.py:1679:class TenantAwareRedisStrategy(RedisStrategy[User, uuid.UUID]):
HEAD:backend/onyx/auth/users.py:1726:            # Expected miss for API keys / PATs / JWTs on the bearer transport.
HEAD:backend/onyx/auth/users.py:1789:class RefreshableDatabaseStrategy(DatabaseStrategy[User, uuid.UUID, AccessToken]):
HEAD:backend/onyx/auth/users.py:1821:class SingleTenantJWTStrategy(JWTStrategy[User, uuid.UUID]):
HEAD:backend/onyx/auth/users.py:1822:    """Stateless JWT strategy for single-tenant deployments.
HEAD:backend/onyx/auth/users.py:1829:    Refresh is implemented by issuing a brand-new JWT (the old one remains
HEAD:backend/onyx/auth/users.py:1831:    JWTs cannot be server-side invalidated.
HEAD:backend/onyx/auth/users.py:1856:        return generate_jwt(
HEAD:backend/onyx/auth/users.py:1861:        # JWTs are stateless — nothing to invalidate server-side.
HEAD:backend/onyx/auth/users.py:1862:        # NOTE: a compromise that makes JWT auth stateful but revocable
HEAD:backend/onyx/auth/users.py:1863:        # is to include a token_version claim in the JWT payload. The token_version
HEAD:backend/onyx/auth/users.py:1865:        # the JWT is used, it is only valid if the token_version claim is the same as the one
HEAD:backend/onyx/auth/users.py:1866:        # in the db. If not, the JWT is invalid and the user needs to login again.
HEAD:backend/onyx/auth/users.py:1874:        """Issue a fresh JWT with a new expiry."""
HEAD:backend/onyx/auth/users.py:1878:def get_redis_strategy() -> TenantAwareRedisStrategy:
HEAD:backend/onyx/auth/users.py:1879:    return TenantAwareRedisStrategy()
HEAD:backend/onyx/auth/users.py:1882:def get_database_strategy(
HEAD:backend/onyx/auth/users.py:1884:) -> RefreshableDatabaseStrategy:
HEAD:backend/onyx/auth/users.py:1885:    return RefreshableDatabaseStrategy(
HEAD:backend/onyx/auth/users.py:1890:def get_jwt_strategy() -> SingleTenantJWTStrategy:
HEAD:backend/onyx/auth/users.py:1891:    return SingleTenantJWTStrategy(
HEAD:backend/onyx/auth/users.py:1897:if AUTH_BACKEND == AuthBackend.JWT:
HEAD:backend/onyx/auth/users.py:1900:            "JWT auth backend is only supported for single-tenant, self-hosted deployments. Use 'redis' or 'postgres' instead."
HEAD:backend/onyx/auth/users.py:1903:        raise ValueError("USER_AUTH_SECRET is required for JWT auth backend.")
HEAD:backend/onyx/auth/users.py:1905:if AUTH_BACKEND == AuthBackend.REDIS:
HEAD:backend/onyx/auth/users.py:1906:    auth_backend = AuthenticationBackend(
HEAD:backend/onyx/auth/users.py:1907:        name="redis", transport=cookie_transport, get_strategy=get_redis_strategy
HEAD:backend/onyx/auth/users.py:1909:elif AUTH_BACKEND == AuthBackend.POSTGRES:
HEAD:backend/onyx/auth/users.py:1910:    auth_backend = AuthenticationBackend(
HEAD:backend/onyx/auth/users.py:1911:        name="postgres", transport=cookie_transport, get_strategy=get_database_strategy
HEAD:backend/onyx/auth/users.py:1913:elif AUTH_BACKEND == AuthBackend.JWT:
HEAD:backend/onyx/auth/users.py:1914:    auth_backend = AuthenticationBackend(
HEAD:backend/onyx/auth/users.py:1915:        name="jwt", transport=cookie_transport, get_strategy=get_jwt_strategy
HEAD:backend/onyx/auth/users.py:1918:    raise ValueError(f"Invalid auth backend: {AUTH_BACKEND}")
HEAD:backend/onyx/auth/users.py:1925:mobile_auth_backend = AuthenticationBackend(
HEAD:backend/onyx/auth/users.py:1928:    get_strategy=auth_backend.get_strategy,
HEAD:backend/onyx/auth/users.py:2016:    get_user_manager, [auth_backend, mobile_auth_backend]
HEAD:backend/onyx/auth/users.py:2027:_JWT_EMAIL_CLAIM_KEYS = ("email", "preferred_username", "upn")
HEAD:backend/onyx/auth/users.py:2030:def _extract_email_from_jwt(payload: dict[str, Any]) -> str | None:
HEAD:backend/onyx/auth/users.py:2031:    """Return the best-effort email/username from a decoded JWT payload."""
HEAD:backend/onyx/auth/users.py:2032:    for key in _JWT_EMAIL_CLAIM_KEYS:
HEAD:backend/onyx/auth/users.py:2044:async def _sync_jwt_oidc_expiry(
HEAD:backend/onyx/auth/users.py:2054:            logger.warning("Invalid exp claim on JWT for user %s", user.email)
HEAD:backend/onyx/auth/users.py:2070:async def _get_or_create_user_from_jwt(
HEAD:backend/onyx/auth/users.py:2075:    email = _extract_email_from_jwt(payload)
HEAD:backend/onyx/auth/users.py:2078:            "JWT token decoded successfully but no email claim found; skipping auth"
HEAD:backend/onyx/auth/users.py:2097:            logger.warning("Inactive user %s attempted JWT login; skipping", email)
HEAD:backend/onyx/auth/users.py:2102:        logger.info("Provisioning user %s from JWT login", email)
HEAD:backend/onyx/auth/users.py:2116:                    "Inactive user %s attempted JWT login during provisioning race; skipping",
HEAD:backend/onyx/auth/users.py:2122:                    "Non-web-login user %s attempted JWT login during provisioning race; skipping",
HEAD:backend/onyx/auth/users.py:2127:    await _sync_jwt_oidc_expiry(user_manager, user, payload)
HEAD:backend/onyx/auth/users.py:2131:async def _check_for_saml_and_jwt(
HEAD:backend/onyx/auth/users.py:2136:    # If user is None, check for JWT in Authorization header
HEAD:backend/onyx/auth/users.py:2137:    if user is None and get_security_settings().jwt_public_key_url is not None:
HEAD:backend/onyx/auth/users.py:2141:            payload = await verify_jwt_token(token)
HEAD:backend/onyx/auth/users.py:2143:                user = await _get_or_create_user_from_jwt(
HEAD:backend/onyx/auth/users.py:2148:                        UsageCredentialType.JWT
HEAD:backend/onyx/auth/users.py:2226:    if user := await _check_for_saml_and_jwt(request, user, async_db_session):
HEAD:backend/onyx/auth/users.py:2227:        # If user is already set, _check_for_saml_and_jwt returns the same user object
HEAD:backend/onyx/auth/users.py:2553:    return generate_jwt(data, secret, lifetime_seconds)
HEAD:backend/onyx/auth/users.py:2577:        state_data = decode_jwt(state_value, state_secret, [STATE_TOKEN_AUDIENCE])
HEAD:backend/onyx/auth/users.py:2578:    except jwt.DecodeError:
HEAD:backend/onyx/auth/users.py:2582:    except jwt.ExpiredSignatureError:
HEAD:backend/onyx/auth/users.py:2586:    except jwt.PyJWTError:
```
Static source contains authentication-backend selection and strategy logic.
Existence of a backend does not imply every route uses it correctly.
## User Identity Dependencies
Evidence lines: 450
```text
HEAD:backend/ee/onyx/auth/users.py:27:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/db/user_group.py:618:    current_user_ids = [user.id for user in db_user_group.users]
HEAD:backend/ee/onyx/db/user_group.py:619:    current_user_ids_set = set(current_user_ids)
HEAD:backend/ee/onyx/db/user_group.py:621:        user_id for user_id in user_ids if user_id not in current_user_ids_set
HEAD:backend/ee/onyx/db/user_group.py:628:        user_ids=current_user_ids + new_user_ids,
HEAD:backend/ee/onyx/db/user_group.py:833:    current_user_ids = set([user.id for user in db_user_group.users])
HEAD:backend/ee/onyx/db/user_group.py:835:    added_user_ids = list(updated_user_ids - current_user_ids)
HEAD:backend/ee/onyx/db/user_group.py:836:    removed_user_ids = list(current_user_ids - updated_user_ids)
HEAD:backend/ee/onyx/server/analytics/api.py:57:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:89:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:124:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:161:    user: User = Depends(require_permission(Permission.READ_AGENT_ANALYTICS)),
HEAD:backend/ee/onyx/server/analytics/api.py:201:    user: User = Depends(require_permission(Permission.READ_AGENT_ANALYTICS)),
HEAD:backend/ee/onyx/server/analytics/api.py:241:    user: User = Depends(require_permission(Permission.READ_AGENT_ANALYTICS)),
HEAD:backend/ee/onyx/server/billing/api.py:171:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:221:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:284:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:360:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:406:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:504:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/documents/cc_pair.py:35:    user: User = Depends(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:58:    user: User = Depends(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:114:    user: User = Depends(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:137:    user: User = Depends(
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:35:    current_user_with_expired_token,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:125:    user: User = Depends(current_user_with_expired_token),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:126:    user_manager: UserManager = Depends(get_user_manager),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:201:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:240:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:316:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:350:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:380:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/evals/api.py:19:    user: User = Depends(current_cloud_superuser),  # noqa: ARG001
HEAD:backend/ee/onyx/server/features/hooks/api.py:200:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:221:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:232:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:268:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:280:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:354:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:365:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:407:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:435:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:458:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/gateway/api.py:1395:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1408:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1432:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1462:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1495:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/license/api.py:55:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:81:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:104:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:184:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:220:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:251:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/log_export/api.py:136:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/log_export/api.py:239:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/log_export/api.py:268:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:34:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:50:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:64:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:90:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:102:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:114:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:130:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:154:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/oauth/api.py:27:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:149:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:261:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:328:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/google_drive.py:114:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/slack.py:103:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/query_and_chat/query_backend.py:26:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:56:    _: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:124:    user: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:174:    user: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/ee/onyx/server/query_history/api.py:161:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:210:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:250:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:285:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:313:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:360:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:394:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:39:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:74:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:98:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/admin_api.py:29:    superuser: User = Depends(current_cloud_superuser),
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:30:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:46:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:148:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:158:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:167:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:189:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:212:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:27:    current_user: User = Depends(
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:34:    if current_user.email != user_email.user_email:
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:29:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:67:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:83:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:92:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:109:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:131:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:53:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:65:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:85:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:103:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:121:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:140:    user: User = Depends(
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:161:    user: User = Depends(
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:241:    user: User = Depends(
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:264:    user: User = Depends(
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:283:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:295:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:86:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:139:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:174:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:196:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:205:    _: User = Depends(require_permission(Permission.MANAGE_USER_GROUPS)),
HEAD:backend/ee/onyx/server/user_group/api.py:225:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:271:    user: User = Depends(require_permission(Permission.MANAGE_USER_GROUPS)),
HEAD:backend/ee/onyx/server/user_group/api.py:305:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:351:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:376:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:399:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:421:    user: User = Depends(require_permission(Permission.MANAGE_USER_GROUPS)),
HEAD:backend/ee/onyx/server/user_group/api.py:460:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:530:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:617:    user: User = Depends(
HEAD:backend/onyx/auth/email_utils.py:405:def send_user_email_invite(user_email: str, current_user: User) -> None:
HEAD:backend/onyx/auth/email_utils.py:420:        current_user.email, user_email, application_name
HEAD:backend/onyx/auth/permissions.py:336:    from onyx.auth.users import current_chat_accessible_user, current_user
HEAD:backend/onyx/auth/permissions.py:338:    base_user = current_chat_accessible_user if allow_anonymous else current_user
HEAD:backend/onyx/auth/permissions.py:340:    async def dependency(request: Request, user: User = Depends(base_user)) -> User:
HEAD:backend/onyx/auth/users.py:178:    CURRENT_USER_ID_CONTEXTVAR,
HEAD:backend/onyx/auth/users.py:1637:    user_db: SQLAlchemyUserDatabase = Depends(get_user_db),
HEAD:backend/onyx/auth/users.py:1659:# Onyx's own API-key/PAT handlers (see `optional_user`).
HEAD:backend/onyx/auth/users.py:1946:        get_current_user_token = self.authenticator.current_user_token(
HEAD:backend/onyx/auth/users.py:1961:            user_token: Tuple[models.UP, str] = Depends(get_current_user_token),
HEAD:backend/onyx/auth/users.py:2024:optional_fastapi_current_user = fastapi_users.current_user(active=True, optional=True)
HEAD:backend/onyx/auth/users.py:2215:async def _resolve_optional_user(
HEAD:backend/onyx/auth/users.py:2279:async def optional_user(
HEAD:backend/onyx/auth/users.py:2282:    user: User | None = Depends(optional_fastapi_current_user),
HEAD:backend/onyx/auth/users.py:2283:    user_manager: BaseUserManager[User, uuid.UUID] = Depends(get_user_manager),
HEAD:backend/onyx/auth/users.py:2285:    user = await _resolve_optional_user(
HEAD:backend/onyx/auth/users.py:2291:    token = CURRENT_USER_ID_CONTEXTVAR.set(str(user.id) if user is not None else None)
HEAD:backend/onyx/auth/users.py:2299:        CURRENT_USER_ID_CONTEXTVAR.reset(token)
HEAD:backend/onyx/auth/users.py:2355:async def current_user_with_expired_token(
HEAD:backend/onyx/auth/users.py:2356:    user: User | None = Depends(optional_user),
HEAD:backend/onyx/auth/users.py:2362:    user: User | None = Depends(optional_user),
HEAD:backend/onyx/auth/users.py:2368:    user: User | None = Depends(optional_user),
HEAD:backend/onyx/auth/users.py:2374:    token = CURRENT_USER_ID_CONTEXTVAR.set(str(user.id))
HEAD:backend/onyx/auth/users.py:2378:        CURRENT_USER_ID_CONTEXTVAR.reset(token)
HEAD:backend/onyx/auth/users.py:2381:async def current_user(
HEAD:backend/onyx/auth/users.py:2382:    user: User | None = Depends(optional_user),
HEAD:backend/onyx/auth/users.py:2445:async def current_user_from_websocket(
HEAD:backend/onyx/auth/users.py:2462:    This applies the same auth checks as current_user() for HTTP endpoints.
HEAD:backend/onyx/auth/users.py:2521:        user_context_token = CURRENT_USER_ID_CONTEXTVAR.set(str(user.id))
HEAD:backend/onyx/auth/users.py:2525:            CURRENT_USER_ID_CONTEXTVAR.reset(user_context_token)
HEAD:backend/onyx/auth/users.py:2933:        user_manager: BaseUserManager[models.UP, models.ID] = Depends(get_user_manager),
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:30:    MAX_CONCURRENT_USER_FILE_PORT_ATTEMPTS,
HEAD:backend/onyx/background/celery/tasks/port/tasks.py:838:                MAX_CONCURRENT_USER_FILE_PORT_ATTEMPTS,
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:711:                current_user_file = db_session.get(UserFile, _as_uuid(user_file_id))
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:713:                    current_user_file
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:714:                    and current_user_file.status != UserFileStatus.DELETING
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:716:                    current_user_file.status = UserFileStatus.FAILED
HEAD:backend/onyx/background/celery/tasks/user_file_processing/tasks.py:717:                    db_session.add(current_user_file)
HEAD:backend/onyx/chat/process_message.py:1010:            current_user = simple_chat_history[-1].model_copy(
HEAD:backend/onyx/chat/process_message.py:1013:            simple_chat_history = stored_messages + [current_user]
HEAD:backend/onyx/chat/process_message.py:1014:            append_incognito_message(chat_session.id, current_user)
HEAD:backend/onyx/configs/app_configs.py:1098:MAX_CONCURRENT_USER_FILE_PORT_ATTEMPTS = max(
HEAD:backend/onyx/configs/app_configs.py:1099:    1, _non_negative_int_env("MAX_CONCURRENT_USER_FILE_PORT_ATTEMPTS", 1)
HEAD:backend/onyx/connectors/confluence/onyx_confluence.py:1278:    def get_current_user(self, expand: str | None = None) -> Any:
HEAD:backend/onyx/db/users.py:61:    access by ``current_user`` and should not receive default-group
HEAD:backend/onyx/db/users.py:766:        concurrent_user = get_user_by_email(SLACK_SERVICE_ACCOUNT_EMAIL, db_session)
HEAD:backend/onyx/db/users.py:767:        if concurrent_user is None:
HEAD:backend/onyx/db/users.py:769:        return concurrent_user
HEAD:backend/onyx/file_store/utils.py:229:    current_user_files = []
HEAD:backend/onyx/file_store/utils.py:237:        current_user_files.append(user_file)
HEAD:backend/onyx/file_store/utils.py:239:    return current_user_files
HEAD:backend/onyx/onyxbot/slack/handlers/handle_regular_answer.py:41:from shared_configs.contextvars import CURRENT_USER_ID_CONTEXTVAR
HEAD:backend/onyx/onyxbot/slack/handlers/handle_regular_answer.py:311:        token = CURRENT_USER_ID_CONTEXTVAR.set(str(usage_user.id))
HEAD:backend/onyx/onyxbot/slack/handlers/handle_regular_answer.py:322:            CURRENT_USER_ID_CONTEXTVAR.reset(token)
HEAD:backend/onyx/server/api_key/api.py:32:    _: User = Depends(require_permission(Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS)),
HEAD:backend/onyx/server/api_key/api.py:41:    _: User = Depends(require_permission(Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS)),
HEAD:backend/onyx/server/api_key/api.py:55:    user: User = Depends(
HEAD:backend/onyx/server/api_key/api.py:77:    user: User = Depends(
HEAD:backend/onyx/server/api_key/api.py:97:    user: User = Depends(
HEAD:backend/onyx/server/api_key/api.py:119:    user: User = Depends(
HEAD:backend/onyx/server/auth_check.py:10:    current_user,
HEAD:backend/onyx/server/auth_check.py:11:    current_user_from_websocket,
HEAD:backend/onyx/server/auth_check.py:12:    current_user_with_expired_token,
HEAD:backend/onyx/server/auth_check.py:172:                    or depends_fn == current_user
HEAD:backend/onyx/server/auth_check.py:173:                    or depends_fn == current_user_with_expired_token
HEAD:backend/onyx/server/auth_check.py:175:                    or depends_fn == current_user_from_websocket
HEAD:backend/onyx/server/documents/cc_pair.py:122:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:162:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:239:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:289:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:340:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:362:    is_editable_for_current_user = editable_cc_pair is not None
HEAD:backend/onyx/server/documents/cc_pair.py:430:        is_editable_for_current_user=is_editable_for_current_user,
HEAD:backend/onyx/server/documents/cc_pair.py:473:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:580:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:614:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:669:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:687:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:743:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/documents/cc_pair.py:759:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/documents/cc_pair.py:801:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:928:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:185:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:205:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:224:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:436:    _: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:444:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:563:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:784:    _: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:818:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:905:    user: User = Depends(
HEAD:backend/onyx/server/documents/connector.py:968:    user: User = Depends(
HEAD:backend/onyx/server/documents/connector.py:1460:    user: User = Depends(
HEAD:backend/onyx/server/documents/connector.py:1501:    user: User = Depends(
HEAD:backend/onyx/server/documents/connector.py:1591:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:1641:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:1666:    user: User = Depends(
HEAD:backend/onyx/server/documents/connector.py:1749:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1770:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1791:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1821:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1849:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:1866:    _: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/onyx/server/documents/connector.py:1878:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:1907:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1993:    user: User = Depends(current_chat_accessible_user),
HEAD:backend/onyx/server/documents/credential.py:60:    user: User = Depends(
HEAD:backend/onyx/server/documents/credential.py:82:    user: User = Depends(
HEAD:backend/onyx/server/documents/credential.py:105:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/credential.py:125:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/credential.py:171:    user: User = Depends(
HEAD:backend/onyx/server/documents/credential.py:204:    user: User = Depends(
HEAD:backend/onyx/server/documents/credential.py:265:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:281:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:305:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/credential.py:336:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/credential.py:382:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:425:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:450:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential_capabilities.py:137:    user: User = Depends(
HEAD:backend/onyx/server/documents/credential_capabilities.py:266:    user: User = Depends(
HEAD:backend/onyx/server/documents/credential_capabilities.py:310:    user: User = Depends(
HEAD:backend/onyx/server/documents/document.py:28:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/document.py:73:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/models.py:452:    is_editable_for_current_user: bool
HEAD:backend/onyx/server/documents/models.py:531:        is_editable_for_current_user: bool,
HEAD:backend/onyx/server/documents/models.py:586:            is_editable_for_current_user=is_editable_for_current_user,
HEAD:backend/onyx/server/documents/models.py:588:                is_editable=is_editable_for_current_user,
HEAD:backend/onyx/server/documents/standard_oauth.py:201:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/standard_oauth.py:247:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/standard_oauth.py:297:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/targeted_reindex.py:80:    user: User = Depends(
HEAD:backend/onyx/server/documents/targeted_reindex.py:174:    user: User = Depends(
HEAD:backend/onyx/server/features/admin_banner/api.py:38:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/admin_banner/api.py:46:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/admin_banner/api.py:66:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/api.py:35:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/api.py:58:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/approvals/api.py:123:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/approvals/api.py:148:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/approvals/api.py:204:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/debug.py:42:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:161:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:207:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:280:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:316:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:333:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:342:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:375:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:405:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:421:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:440:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/oauth.py:87:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/oauth.py:137:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/interactive_turns/api.py:111:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/interactive_turns/api.py:132:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:399:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:411:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:460:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:472:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:524:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:538:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:563:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:89:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:108:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:167:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:204:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:215:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:234:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:267:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:285:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:305:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:323:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:359:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:438:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:473:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:506:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:524:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:562:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:613:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:655:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:681:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:703:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:734:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:771:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:822:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:873:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:925:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/messages.py:64:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/messages.py:84:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/messages.py:225:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/messages.py:292:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/user_library/api.py:153:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/user_library/api.py:183:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/user_library/api.py:287:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/user_library/api.py:451:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/user_library/api.py:485:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/webapp_proxy.py:31:    optional_user,
HEAD:backend/onyx/server/features/build/webapp_proxy.py:272:    user_manager: BaseUserManager[User, UUID] = Depends(get_user_manager),
HEAD:backend/onyx/server/features/build/webapp_proxy.py:402:    user: User | None = Depends(optional_user),
HEAD:backend/onyx/server/features/build/webapp_proxy.py:424:    user: User = Depends(_current_webapp_websocket_user),
HEAD:backend/onyx/server/features/default_assistant/api.py:28:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/default_assistant/api.py:53:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/document_set/api.py:50:    user: User = Depends(
HEAD:backend/onyx/server/features/document_set/api.py:116:    user: User = Depends(
HEAD:backend/onyx/server/features/document_set/api.py:184:    user: User = Depends(
HEAD:backend/onyx/server/features/document_set/api.py:233:    user: User = Depends(
HEAD:backend/onyx/server/features/document_set/api.py:289:    user: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/onyx/server/features/document_set/api.py:339:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/hierarchy/api.py:71:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/hierarchy/api.py:99:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/hierarchy/api.py:156:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/image_generation/api.py:221:    _user: User = Depends(require_permission(Permission.GENERATE_IMAGE)),
HEAD:backend/onyx/server/features/input_prompt/api.py:32:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/input_prompt/api.py:47:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/input_prompt/api.py:62:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/input_prompt/api.py:86:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/input_prompt/api.py:109:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/input_prompt/api.py:127:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/input_prompt/api.py:142:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:624:    user: User = Depends(
HEAD:backend/onyx/server/features/mcp/api.py:636:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:891:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:1002:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:1102:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:1322:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:1350:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:1367:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:1401:    user: User = Depends(
HEAD:backend/onyx/server/features/mcp/api.py:1418:    user: User = Depends(
HEAD:backend/onyx/server/features/mcp/api.py:1484:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:2175:    user: User = Depends(
HEAD:backend/onyx/server/features/mcp/api.py:2206:    user: User = Depends(
HEAD:backend/onyx/server/features/mcp/api.py:2243:    user: User = Depends(
HEAD:backend/onyx/server/features/mcp/api.py:2271:    user: User = Depends(
HEAD:backend/onyx/server/features/mcp/api.py:2323:    user: User = Depends(
HEAD:backend/onyx/server/features/mcp/api.py:2370:    user: User = Depends(
HEAD:backend/onyx/server/features/mcp/api.py:2445:    user: User = Depends(
HEAD:backend/onyx/server/features/mcp/api.py:2499:    user: User = Depends(
HEAD:backend/onyx/server/features/mcp/api.py:2562:    user: User = Depends(
HEAD:backend/onyx/server/features/mcp/api.py:2655:    user: User = Depends(
HEAD:backend/onyx/server/features/notifications/api.py:122:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/notifications/api.py:197:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/notifications/api.py:216:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/notifications/api.py:225:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/oauth_config/api.py:88:    _: User = Depends(require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)),
HEAD:backend/onyx/server/features/oauth_config/api.py:111:    _: User = Depends(require_permission(Permission.MANAGE_ACTIONS)),
HEAD:backend/onyx/server/features/oauth_config/api.py:122:    user: User = Depends(
HEAD:backend/onyx/server/features/oauth_config/api.py:142:    user: User = Depends(
HEAD:backend/onyx/server/features/oauth_config/api.py:177:    user: User = Depends(
HEAD:backend/onyx/server/features/oauth_config/api.py:203:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/oauth_config/api.py:240:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/oauth_config/api.py:301:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/password/api.py:22:    user_manager: UserManager = Depends(get_user_manager),
HEAD:backend/onyx/server/features/password/api.py:23:    current_user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/password/api.py:30:            user=current_user,
HEAD:backend/onyx/server/features/password/api.py:45:    user_manager: UserManager = Depends(get_user_manager),
HEAD:backend/onyx/server/features/password/api.py:47:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:170:    user: User = Depends(require_permission(Permission.MANAGE_AGENTS)),
HEAD:backend/onyx/server/features/persona/api.py:188:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:207:    user: User = Depends(require_permission(Permission.MANAGE_AGENTS)),
HEAD:backend/onyx/server/features/persona/api.py:225:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:251:    user: User = Depends(require_permission(Permission.READ_AGENTS, allow_scope=True)),
HEAD:backend/onyx/server/features/persona/api.py:268:    user: User = Depends(require_permission(Permission.READ_AGENTS, allow_scope=True)),
HEAD:backend/onyx/server/features/persona/api.py:314:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:328:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:347:    user: User = Depends(require_permission(Permission.ADD_AGENTS, allow_scope=True)),
HEAD:backend/onyx/server/features/persona/api.py:379:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:404:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:416:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:433:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:446:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:491:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:540:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:565:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:584:    user: User = Depends(require_permission(Permission.ADD_AGENTS, allow_scope=True)),
HEAD:backend/onyx/server/features/persona/api.py:629:    user: User = Depends(current_chat_accessible_user),
HEAD:backend/onyx/server/features/persona/api.py:651:    user: User = Depends(current_chat_accessible_user),
HEAD:backend/onyx/server/features/persona/api.py:698:    user: User = Depends(current_limited_user),
HEAD:backend/onyx/server/features/persona/api.py:772:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:148:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:161:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:181:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:240:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:257:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:284:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:329:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:376:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:404:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:435:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:465:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:492:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:521:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:581:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:609:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:635:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:654:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:673:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:701:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:739:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/search/api.py:59:    user: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/onyx/server/features/skill/api.py:177:def list_skills_for_current_user(
HEAD:backend/onyx/server/features/skill/api.py:178:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:190:def set_skill_enabled_for_current_user(
HEAD:backend/onyx/server/features/skill/api.py:193:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:210:def fetch_skill_for_current_user(
HEAD:backend/onyx/server/features/skill/api.py:212:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:227:def preview_skill_for_current_user(
HEAD:backend/onyx/server/features/skill/api.py:229:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:247:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:291:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:316:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:418:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:506:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:524:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),  # noqa: ARG001
HEAD:backend/onyx/server/features/skill/api.py:554:def replace_current_user_skill_bundle(
HEAD:backend/onyx/server/features/skill/api.py:557:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:599:def upload_current_user_skill_files(
HEAD:backend/onyx/server/features/skill/api.py:602:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:627:def remove_current_user_skill_file(
HEAD:backend/onyx/server/features/skill/api.py:630:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:655:def patch_current_user_skill(
HEAD:backend/onyx/server/features/skill/api.py:658:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
```
These are candidate mechanisms by which authenticated or optional user
identity enters request handling.
## Permission Model
Evidence lines: 450
```text
HEAD:backend/ee/onyx/auth/users.py:9:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/auth/users.py:27:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:988:class PermissionSyncCallback(IndexingHeartbeatInterface):
HEAD:backend/ee/onyx/db/persona.py:5:from onyx.auth.permissions import has_global_permission, has_permission
HEAD:backend/ee/onyx/db/persona.py:40:        group_id: existing.get(group_id, PersonaSharePermission.VIEWER)
HEAD:backend/ee/onyx/db/persona.py:95:    if has_global_permission(acting_user, Permission.MANAGE_USER_GROUPS):
HEAD:backend/ee/onyx/db/persona.py:119:        has_permission(acting_user, Permission.MANAGE_AGENTS)
HEAD:backend/ee/onyx/db/persona.py:126:        permission=Permission.MANAGE_AGENTS,
HEAD:backend/ee/onyx/db/user_group.py:17:    get_effective_permissions,
HEAD:backend/ee/onyx/db/user_group.py:19:    has_permission,
HEAD:backend/ee/onyx/db/user_group.py:20:    resolve_effective_permissions,
HEAD:backend/ee/onyx/db/user_group.py:539:            permission=Permission.BASIC_ACCESS,
HEAD:backend/ee/onyx/db/user_group.py:661:    group_permissions.discard(Permission.BASIC_ACCESS)
HEAD:backend/ee/onyx/db/user_group.py:662:    excess = group_permissions - get_effective_permissions(user)
HEAD:backend/ee/onyx/db/user_group.py:667:            "hold: " + ", ".join(sorted(permission.value for permission in excess)),
HEAD:backend/ee/onyx/db/user_group.py:699:    if not has_global_permission(user, Permission.FULL_ADMIN_PANEL_ACCESS):
HEAD:backend/ee/onyx/db/user_group.py:727:        has_permission(user, Permission.MANAGE_USER_GROUPS)
HEAD:backend/ee/onyx/db/user_group.py:756:            permission=Permission.MANAGE_CONNECTORS,
HEAD:backend/ee/onyx/db/user_group.py:768:    Reads grants directly rather than ``effective_permissions``, which still reflects the
HEAD:backend/ee/onyx/db/user_group.py:771:        permission.value
HEAD:backend/ee/onyx/db/user_group.py:785:    return Permission.MANAGE_USER_GROUPS.value in resolve_effective_permissions(granted)
HEAD:backend/ee/onyx/db/user_group.py:848:    # effective_permissions is derived from group grants — so leaving can revoke the very
HEAD:backend/ee/onyx/db/user_group.py:1119:class PermissionChange(NamedTuple):
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:118:        operation = permission.get("operation") or {}
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:124:        subject = permission.get("subject") or {}
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:182:        if user_name := permission.get("userName"):
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:184:        if group_name := permission.get("groupName"):
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:264:        subs = permission.get("subjects")
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:273:            if permission.get("operation", {}).get(
HEAD:backend/ee/onyx/external_permissions/confluence/space_access.py:275:            ) == "read" and permission.get("anonymousAccess", False):
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:49:    if not permission.domain:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:54:    if permission.allow_file_discovery is False:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:56:    if permission.domain != own_domain:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:61:            permission.domain,
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:63:    return build_domain_group_id(permission.domain)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:95:            if permission.id not in seen_permission_ids:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:97:                seen_permission_ids.add(permission.id)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:139:            GoogleDrivePermission.from_drive_permission(p) for p in permissions
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:225:        if permission.inherited_from:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:226:            folder_ids_to_inherit_permissions_from.add(permission.inherited_from)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:228:        if permission.type == PermissionType.USER:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:229:            if permission.email_address:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:230:                user_emails.add(permission.email_address)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:242:        elif permission.type == PermissionType.GROUP:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:244:            if permission.email_address:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:245:                group_emails.add(permission.email_address)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:252:        elif permission.type == PermissionType.DOMAIN:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:258:        elif permission.type == PermissionType.ANYONE:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:336:        if permission.type == PermissionType.USER:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:337:            if permission.email_address:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:338:                user_emails.add(permission.email_address)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:341:        elif permission.type == PermissionType.GROUP:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:343:            if permission.email_address:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:344:                group_emails.add(permission.email_address)
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:349:        elif permission.type == PermissionType.DOMAIN:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:355:        elif permission.type == PermissionType.ANYONE:
HEAD:backend/ee/onyx/external_permissions/google_drive/doc_sync.py:358:            is_public = permission.allow_file_discovery is not False
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:124:                    GoogleDrivePermission.from_drive_permission(permission)
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:133:                if permission.inherited_from is None
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:197:        if permission.type == PermissionType.USER:
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:198:            if permission.email_address is None:
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:205:            folder_member_emails.add(permission.email_address)
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:206:        elif permission.type == PermissionType.GROUP:
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:207:            if permission.email_address not in group_email_to_member_emails_map:
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:210:                    permission.email_address,
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:215:                group_email_to_member_emails_map[permission.email_address]
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:217:        elif permission.type == PermissionType.ANYONE:
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:459:            if permission.type == PermissionType.USER:
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:460:                if permission.email_address is None:
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:467:                folder_member_emails.add(permission.email_address)
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:468:            elif permission.type == PermissionType.GROUP:
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:469:                if permission.email_address not in group_email_to_member_emails_map:
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:472:                        permission.email_address,
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:477:                    group_email_to_member_emails_map[permission.email_address]
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:479:            elif permission.type == PermissionType.ANYONE:
HEAD:backend/ee/onyx/external_permissions/google_drive/models.py:7:class PermissionType(str, Enum):
HEAD:backend/ee/onyx/external_permissions/google_drive/models.py:44:        permission_details_list = drive_permission.get("permissionDetails", [])
HEAD:backend/ee/onyx/external_permissions/google_drive/models.py:50:            email_address=drive_permission.get("emailAddress"),
HEAD:backend/ee/onyx/external_permissions/google_drive/models.py:52:            domain=drive_permission.get("domain"),
HEAD:backend/ee/onyx/external_permissions/google_drive/models.py:53:            allow_file_discovery=drive_permission.get("allowFileDiscovery"),
HEAD:backend/ee/onyx/external_permissions/google_drive/permission_retrieval.py:46:        permission_id = permission.get("id")
HEAD:backend/ee/onyx/external_permissions/google_drive/permission_retrieval.py:48:            google_drive_permission = GoogleDrivePermission.from_drive_permission(
HEAD:backend/ee/onyx/external_permissions/jira/models.py:9:class Permission(BaseModel):
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:95:    A "Holder" in JIRA is a person / entity who "holds" the corresponding permission.
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:144:        if permission.permission != BROWSE_PROJECTS_PERMISSION:
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:149:        if not permission.holder:
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:156:        type = permission.holder.get("type")
HEAD:backend/ee/onyx/external_permissions/jira/page_access.py:164:        holder_map[type].append(permission.holder)
HEAD:backend/ee/onyx/external_permissions/sharepoint/permission_utils.py:132:            if permission.link and permission.link.scope in (
HEAD:backend/ee/onyx/server/analytics/api.py:20:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/analytics/api.py:57:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:89:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:124:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:161:    user: User = Depends(require_permission(Permission.READ_AGENT_ANALYTICS)),
HEAD:backend/ee/onyx/server/analytics/api.py:201:    user: User = Depends(require_permission(Permission.READ_AGENT_ANALYTICS)),
HEAD:backend/ee/onyx/server/analytics/api.py:241:    user: User = Depends(require_permission(Permission.READ_AGENT_ANALYTICS)),
HEAD:backend/ee/onyx/server/billing/api.py:60:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/billing/api.py:171:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:221:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:284:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:360:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:406:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:504:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/documents/cc_pair.py:12:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/documents/cc_pair.py:36:        require_permission(Permission.READ_CONNECTORS, allow_scope=True)
HEAD:backend/ee/onyx/server/documents/cc_pair.py:59:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/ee/onyx/server/documents/cc_pair.py:115:        require_permission(Permission.READ_CONNECTORS, allow_scope=True)
HEAD:backend/ee/onyx/server/documents/cc_pair.py:138:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:32:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:201:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:240:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:316:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:350:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:380:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:5:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/features/hooks/api.py:200:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:221:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:232:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:268:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:280:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:354:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:365:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:407:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:435:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:458:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/gateway/api.py:33:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/gateway/api.py:1395:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1408:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1432:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1462:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1495:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/license/api.py:39:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/license/api.py:55:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:81:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:104:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:184:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:220:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:251:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/log_export/api.py:27:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/log_export/api.py:136:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/log_export/api.py:239:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/log_export/api.py:268:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:16:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/manage/standard_answer.py:34:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:50:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:64:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:90:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:102:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:114:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:130:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:154:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/oauth/api.py:11:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/oauth/api.py:27:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:13:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:149:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:261:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:328:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/google_drive.py:13:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/oauth/google_drive.py:114:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/slack.py:12:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/oauth/slack.py:103:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/query_and_chat/query_backend.py:11:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/query_and_chat/query_backend.py:26:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:35:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:56:    _: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:124:    user: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:174:    user: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/ee/onyx/server/query_history/api.py:24:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/query_history/api.py:161:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:210:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:250:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:285:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:313:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:360:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:394:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:16:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:39:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:74:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:98:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/scim/api.py:1359:        permission=Permission.BASIC_ACCESS,
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:12:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:30:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:46:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:52:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/tenants/billing_api.py:148:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:158:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:167:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:189:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:212:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:9:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:28:        require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:5:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:29:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:22:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:67:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:83:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:92:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:109:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:131:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:11:from onyx.auth.permissions import require_permission
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:53:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:65:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:85:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:103:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:121:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:141:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:162:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:171:        permission=Permission.MANAGE_USER_GROUPS,
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:204:        permission=Permission.MANAGE_USER_GROUPS,
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:226:        permission=Permission.MANAGE_USER_GROUPS,
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:234:# Separate from the shared by-id routes so this route's require_permission caps a scoped
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:242:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:265:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:283:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:295:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:42:    get_effective_permissions,
HEAD:backend/ee/onyx/server/user_group/api.py:44:    has_permission,
HEAD:backend/ee/onyx/server/user_group/api.py:45:    require_permission,
HEAD:backend/ee/onyx/server/user_group/api.py:87:        require_permission(Permission.READ_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:96:        get_scoped_groups(user, db_session, Permission.MANAGE_USER_GROUPS)
HEAD:backend/ee/onyx/server/user_group/api.py:97:        if has_permission(user, Permission.MANAGE_USER_GROUPS)
HEAD:backend/ee/onyx/server/user_group/api.py:101:    is_user_groups_admin = has_global_permission(user, Permission.MANAGE_USER_GROUPS)
HEAD:backend/ee/onyx/server/user_group/api.py:102:    is_full_admin = has_global_permission(user, Permission.FULL_ADMIN_PANEL_ACCESS)
HEAD:backend/ee/onyx/server/user_group/api.py:105:        if has_global_permission(user, Permission.READ_USER_GROUPS)
HEAD:backend/ee/onyx/server/user_group/api.py:140:        require_permission(Permission.READ_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:148:    if not has_global_permission(user, Permission.READ_USER_GROUPS) and not can_manage:
HEAD:backend/ee/onyx/server/user_group/api.py:161:                user, Permission.MANAGE_USER_GROUPS
HEAD:backend/ee/onyx/server/user_group/api.py:164:                user, Permission.FULL_ADMIN_PANEL_ACCESS
HEAD:backend/ee/onyx/server/user_group/api.py:174:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:177:    if Permission.FULL_ADMIN_PANEL_ACCESS in get_effective_permissions(user):
HEAD:backend/ee/onyx/server/user_group/api.py:196:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:205:    _: User = Depends(require_permission(Permission.MANAGE_USER_GROUPS)),
HEAD:backend/ee/onyx/server/user_group/api.py:225:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:260:            "added": [permission.value for permission in change.added],
HEAD:backend/ee/onyx/server/user_group/api.py:261:            "removed": [permission.value for permission in change.removed],
HEAD:backend/ee/onyx/server/user_group/api.py:271:    user: User = Depends(require_permission(Permission.MANAGE_USER_GROUPS)),
HEAD:backend/ee/onyx/server/user_group/api.py:306:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:351:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:377:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:400:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:421:    user: User = Depends(require_permission(Permission.MANAGE_USER_GROUPS)),
HEAD:backend/ee/onyx/server/user_group/api.py:461:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:488:    get_editable = not has_global_permission(user, Permission.MANAGE_USER_GROUPS)
HEAD:backend/ee/onyx/server/user_group/api.py:531:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:572:    if not has_global_permission(user, Permission.MANAGE_USER_GROUPS):
HEAD:backend/ee/onyx/server/user_group/api.py:586:                permission=Permission.MANAGE_DOCUMENT_SETS,
HEAD:backend/ee/onyx/server/user_group/api.py:618:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/utils/license_notifications.py:245:        user, Permission.FULL_ADMIN_PANEL_ACCESS
HEAD:backend/onyx/auth/permissions.py:32:    Permission.MANAGE_AGENTS.value: {
HEAD:backend/onyx/auth/permissions.py:33:        Permission.ADD_AGENTS.value,
HEAD:backend/onyx/auth/permissions.py:34:        Permission.READ_AGENTS.value,
HEAD:backend/onyx/auth/permissions.py:35:        Permission.READ_DOCUMENT_SETS.value,
HEAD:backend/onyx/auth/permissions.py:38:        Permission.READ_AGENT_ANALYTICS.value,
HEAD:backend/onyx/auth/permissions.py:40:    Permission.MANAGE_DOCUMENT_SETS.value: {
HEAD:backend/onyx/auth/permissions.py:41:        Permission.READ_DOCUMENT_SETS.value,
HEAD:backend/onyx/auth/permissions.py:42:        Permission.READ_CONNECTORS.value,
HEAD:backend/onyx/auth/permissions.py:43:        Permission.READ_USER_GROUPS.value,
HEAD:backend/onyx/auth/permissions.py:45:    Permission.MANAGE_CONNECTORS.value: {
HEAD:backend/onyx/auth/permissions.py:46:        Permission.READ_CONNECTORS.value,
HEAD:backend/onyx/auth/permissions.py:47:        Permission.READ_USER_GROUPS.value,
HEAD:backend/onyx/auth/permissions.py:49:    Permission.MANAGE_USER_GROUPS.value: {
HEAD:backend/onyx/auth/permissions.py:50:        Permission.READ_CONNECTORS.value,
HEAD:backend/onyx/auth/permissions.py:51:        Permission.READ_DOCUMENT_SETS.value,
HEAD:backend/onyx/auth/permissions.py:52:        Permission.READ_AGENTS.value,
HEAD:backend/onyx/auth/permissions.py:53:        Permission.READ_USERS.value,
HEAD:backend/onyx/auth/permissions.py:54:        Permission.READ_USER_GROUPS.value,
HEAD:backend/onyx/auth/permissions.py:56:    Permission.MANAGE_LLMS.value: {
HEAD:backend/onyx/auth/permissions.py:57:        Permission.READ_USER_GROUPS.value,
HEAD:backend/onyx/auth/permissions.py:58:        Permission.READ_AGENTS.value,
HEAD:backend/onyx/auth/permissions.py:59:        Permission.READ_USERS.value,
HEAD:backend/onyx/auth/permissions.py:61:    Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS.value: {
HEAD:backend/onyx/auth/permissions.py:62:        Permission.READ_USER_GROUPS.value,
HEAD:backend/onyx/auth/permissions.py:64:    Permission.MANAGE_ACTIONS.value: {
HEAD:backend/onyx/auth/permissions.py:65:        Permission.READ_USER_GROUPS.value,
HEAD:backend/onyx/auth/permissions.py:69:    # resolve_effective_permissions.
HEAD:backend/onyx/auth/permissions.py:70:    Permission.BASIC_ACCESS.value: {
HEAD:backend/onyx/auth/permissions.py:71:        Permission.READ_SEARCH.value,
HEAD:backend/onyx/auth/permissions.py:72:        Permission.READ_CHAT.value,
HEAD:backend/onyx/auth/permissions.py:73:        Permission.WRITE_CHAT.value,
HEAD:backend/onyx/auth/permissions.py:74:        Permission.GENERATE_IMAGE.value,
HEAD:backend/onyx/auth/permissions.py:75:        Permission.USE_LLM_GATEWAY.value,
HEAD:backend/onyx/auth/permissions.py:77:    Permission.WRITE_CHAT.value: {Permission.READ_CHAT.value},
HEAD:backend/onyx/auth/permissions.py:78:    Permission.CRAFT_SANDBOX.value: {
HEAD:backend/onyx/auth/permissions.py:79:        Permission.READ_SEARCH.value,
HEAD:backend/onyx/auth/permissions.py:80:        Permission.GENERATE_IMAGE.value,
HEAD:backend/onyx/auth/permissions.py:81:        Permission.USE_LLM_GATEWAY.value,
HEAD:backend/onyx/auth/permissions.py:93:        Permission.BASIC_ACCESS,
HEAD:backend/onyx/auth/permissions.py:94:        Permission.FULL_ADMIN_PANEL_ACCESS,
HEAD:backend/onyx/auth/permissions.py:95:        Permission.CRAFT_SANDBOX,
HEAD:backend/onyx/auth/permissions.py:96:        Permission.MANAGE_SKILLS,
HEAD:backend/onyx/auth/permissions.py:98:    | Permission.IMPLIED
HEAD:backend/onyx/auth/permissions.py:107:        Permission.ADD_AGENTS,
HEAD:backend/onyx/auth/permissions.py:112:# Never persisted to permission_grant or merged into effective_permissions
HEAD:backend/onyx/auth/permissions.py:113:# (which stays global-only); has_permission reads it to classify SCOPED
HEAD:backend/onyx/auth/permissions.py:117:        Permission.MANAGE_CONNECTORS,
HEAD:backend/onyx/auth/permissions.py:118:        Permission.MANAGE_DOCUMENT_SETS,
HEAD:backend/onyx/auth/permissions.py:119:        Permission.MANAGE_AGENTS,
HEAD:backend/onyx/auth/permissions.py:120:        Permission.ADD_AGENTS,
HEAD:backend/onyx/auth/permissions.py:121:        Permission.MANAGE_USER_GROUPS,
HEAD:backend/onyx/auth/permissions.py:122:        Permission.MANAGE_ACTIONS,  # scoped via its agents at GATE 2
HEAD:backend/onyx/auth/permissions.py:123:        Permission.MANAGE_SKILLS,  # scoped via Skill__UserGroup at GATE 2
HEAD:backend/onyx/auth/permissions.py:128:class PermissionRegistryEntry(BaseModel):
HEAD:backend/onyx/auth/permissions.py:164:        permissions=[Permission.MANAGE_LLMS],
HEAD:backend/onyx/auth/permissions.py:172:            Permission.MANAGE_CONNECTORS,
HEAD:backend/onyx/auth/permissions.py:173:            Permission.MANAGE_DOCUMENT_SETS,
HEAD:backend/onyx/auth/permissions.py:181:        permissions=[Permission.MANAGE_ACTIONS],
HEAD:backend/onyx/auth/permissions.py:189:        permissions=[Permission.MANAGE_USER_GROUPS],
HEAD:backend/onyx/auth/permissions.py:196:        permissions=[Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS],
HEAD:backend/onyx/auth/permissions.py:203:        permissions=[Permission.MANAGE_BOTS],
HEAD:backend/onyx/auth/permissions.py:211:        permissions=[Permission.ADD_AGENTS],
HEAD:backend/onyx/auth/permissions.py:218:        permissions=[Permission.MANAGE_AGENTS],
HEAD:backend/onyx/auth/permissions.py:226:        permissions=[Permission.READ_AGENT_ANALYTICS],
HEAD:backend/onyx/auth/permissions.py:233:        permissions=[Permission.READ_QUERY_HISTORY],
HEAD:backend/onyx/auth/permissions.py:240:        permissions=[Permission.CREATE_USER_API_KEYS],
HEAD:backend/onyx/auth/permissions.py:246:def resolve_effective_permissions(granted: set[str]) -> set[str]:
HEAD:backend/onyx/auth/permissions.py:251:    if Permission.FULL_ADMIN_PANEL_ACCESS.value in granted:
HEAD:backend/onyx/auth/permissions.py:268:# — scoped to their managed groups. has_permission classifies against this so a
HEAD:backend/onyx/auth/permissions.py:272:    resolve_effective_permissions({p.value for p in SCOPED_MANAGER_PERMISSIONS})
HEAD:backend/onyx/auth/permissions.py:276:def get_effective_permissions(user: User) -> set[Permission]:
HEAD:backend/onyx/auth/permissions.py:280:    granted = set(parse_permission_values(user.effective_permissions or []))
HEAD:backend/onyx/auth/permissions.py:281:    if Permission.FULL_ADMIN_PANEL_ACCESS in granted:
HEAD:backend/onyx/auth/permissions.py:292:    expanded = resolve_effective_permissions({p.value for p in granted})
HEAD:backend/onyx/auth/permissions.py:296:def has_permission(user: User, permission: Permission) -> PermissionAuthority:
HEAD:backend/onyx/auth/permissions.py:303:    if permission in get_effective_permissions(user):
HEAD:backend/onyx/auth/permissions.py:307:        and permission.value in SCOPED_MANAGER_PERMISSIONS_EXPANDED
HEAD:backend/onyx/auth/permissions.py:315:    GLOBAL-only convenience over has_permission, for checks that must exclude
HEAD:backend/onyx/auth/permissions.py:317:    return has_permission(user, permission) is PermissionAuthority.GLOBAL
HEAD:backend/onyx/auth/permissions.py:320:def require_permission(
HEAD:backend/onyx/auth/permissions.py:335:    # (users.py imports has_permission from this module at top level).
HEAD:backend/onyx/auth/permissions.py:344:        authority = has_permission(user, required)
HEAD:backend/onyx/auth/permissions.py:351:            resolve_effective_permissions({s.value for s in token_scopes})
HEAD:backend/onyx/auth/permissions.py:362:    dependency._is_require_permission = True  # ty: ignore[unresolved-attribute]
HEAD:backend/onyx/auth/scoped_permissions.py:17:    has_permission,
HEAD:backend/onyx/auth/scoped_permissions.py:57:    Gate on the *expanded* bundle to match has_permission: an implied read a
HEAD:backend/onyx/auth/scoped_permissions.py:61:        and permission.value not in SCOPED_MANAGER_PERMISSIONS_EXPANDED
HEAD:backend/onyx/auth/scoped_permissions.py:84:    authority = has_permission(user, permission)
HEAD:backend/onyx/auth/scoped_permissions.py:129:                "permission": permission.value,
HEAD:backend/onyx/auth/scoped_permissions.py:154:    if has_global_permission(user, Permission.MANAGE_USER_GROUPS):
HEAD:backend/onyx/auth/scoped_permissions.py:159:        else get_scoped_groups(user, db_session, Permission.MANAGE_USER_GROUPS)
HEAD:backend/onyx/auth/scoped_permissions.py:173:            extra={"permission": Permission.MANAGE_USER_GROUPS.value},
HEAD:backend/onyx/auth/scoped_permissions.py:185:    if has_permission(user, permission) is not PermissionAuthority.GLOBAL:
HEAD:backend/onyx/auth/scoped_permissions.py:186:        _emit_denial(user, "global_only", extra={"permission": permission.value})
HEAD:backend/onyx/auth/users.py:191:    return has_global_permission(user, Permission.FULL_ADMIN_PANEL_ACCESS)
HEAD:backend/onyx/auth/users.py:2208:            dependency.call, "_is_require_permission", False
HEAD:backend/onyx/auth/users.py:2236:                # Expose the token's scopes so require_permission can cap the
HEAD:backend/onyx/auth/users.py:2264:    # require_permission its scopes can satisfy (see require_permission).
HEAD:backend/onyx/auth/users.py:2312:        effective_permissions=[Permission.BASIC_ACCESS.value],
HEAD:backend/onyx/db/auth.py:70:            User.effective_permissions.contains(
HEAD:backend/onyx/db/auth.py:71:                [Permission.FULL_ADMIN_PANEL_ACCESS.value]
HEAD:backend/onyx/db/connector_credential_pair.py:12:from onyx.auth.permissions import get_effective_permissions
HEAD:backend/onyx/db/connector_credential_pair.py:182:    user_permissions = get_effective_permissions(user)
HEAD:backend/onyx/db/connector_credential_pair.py:184:    if Permission.MANAGE_CONNECTORS in user_permissions:
HEAD:backend/onyx/db/connector_credential_pair.py:189:    if not get_editable and Permission.READ_CONNECTORS in user_permissions:
HEAD:backend/onyx/db/credentials.py:7:from onyx.auth.permissions import get_effective_permissions
HEAD:backend/onyx/db/credentials.py:48:    effective = get_effective_permissions(user)
HEAD:backend/onyx/db/credentials.py:50:    if Permission.MANAGE_CONNECTORS in effective:
HEAD:backend/onyx/db/document_set.py:44:    if has_global_permission(user, Permission.MANAGE_DOCUMENT_SETS):
HEAD:backend/onyx/db/document_set.py:74:    if has_global_permission(user, Permission.READ_DOCUMENT_SETS):
HEAD:backend/onyx/db/enums.py:86:class PermissionSyncStatus(str, PyEnum):
HEAD:backend/onyx/db/enums.py:640:class Permission(str, PyEnum):
HEAD:backend/onyx/db/enums.py:700:Permission.IMPLIED = frozenset(
HEAD:backend/onyx/db/enums.py:702:        Permission.READ_CONNECTORS,
HEAD:backend/onyx/db/enums.py:703:        Permission.READ_DOCUMENT_SETS,
HEAD:backend/onyx/db/enums.py:704:        Permission.READ_AGENTS,
HEAD:backend/onyx/db/enums.py:705:        Permission.READ_USERS,
HEAD:backend/onyx/db/enums.py:706:        Permission.READ_USER_GROUPS,
HEAD:backend/onyx/db/enums.py:707:        Permission.READ_SEARCH,
HEAD:backend/onyx/db/enums.py:708:        Permission.READ_CHAT,
HEAD:backend/onyx/db/enums.py:709:        Permission.WRITE_CHAT,
HEAD:backend/onyx/db/enums.py:710:        Permission.READ_ADMIN,
HEAD:backend/onyx/db/enums.py:711:        Permission.GENERATE_IMAGE,
HEAD:backend/onyx/db/enums.py:712:        Permission.USE_LLM_GATEWAY,
HEAD:backend/onyx/db/enums.py:717:class PermissionAuthority(PyEnum):
HEAD:backend/onyx/db/enums.py:718:    """The authority a user holds for a permission, returned by has_permission.
HEAD:backend/onyx/db/external_app.py:376:                public_permission=SkillSharePermission.VIEWER,
HEAD:backend/onyx/db/external_app.py:386:    skill.public_permission = SkillSharePermission.VIEWER
HEAD:backend/onyx/db/external_app.py:457:    skill.public_permission = SkillSharePermission.VIEWER
HEAD:backend/onyx/db/external_app.py:570:        skill.public_permission = SkillSharePermission.VIEWER
HEAD:backend/onyx/db/feedback.py:43:        user, Permission.FULL_ADMIN_PANEL_ACCESS
HEAD:backend/onyx/db/feedback.py:44:    ) or has_global_permission(user, Permission.MANAGE_CONNECTORS):
HEAD:backend/onyx/db/llm.py:720:    can_manage_llms = has_global_permission(user, Permission.MANAGE_LLMS)
HEAD:backend/onyx/db/llm.py:756:    can_manage_llms = has_global_permission(user, Permission.MANAGE_LLMS)
HEAD:backend/onyx/db/llm.py:783:    can_manage_llms = has_global_permission(user, Permission.MANAGE_LLMS)
HEAD:backend/onyx/db/llm.py:852:        can_manage_llms=has_global_permission(user, Permission.MANAGE_LLMS),
HEAD:backend/onyx/db/mcp.py:114:    if has_global_permission(user, Permission.FULL_ADMIN_PANEL_ACCESS):
HEAD:backend/onyx/db/mcp.py:186:        User.effective_permissions.contains([Permission.FULL_ADMIN_PANEL_ACCESS.value])
HEAD:backend/onyx/db/models.py:429:    effective_permissions: Mapped[list[str]] = mapped_column(
HEAD:backend/onyx/db/models.py:710:        default=PersonaSharePermission.VIEWER,
HEAD:backend/onyx/db/models.py:711:        server_default=PersonaSharePermission.VIEWER.value,
HEAD:backend/onyx/db/models.py:732:        default=SkillSharePermission.VIEWER,
HEAD:backend/onyx/db/models.py:733:        server_default=SkillSharePermission.VIEWER.value,
HEAD:backend/onyx/db/models.py:4289:        default=PersonaSharePermission.VIEWER,
HEAD:backend/onyx/db/models.py:4290:        server_default=PersonaSharePermission.VIEWER.value,
HEAD:backend/onyx/db/models.py:5027:class PermissionGrant(Base):
HEAD:backend/onyx/db/models.py:5067:        if value in Permission.IMPLIED:
HEAD:backend/onyx/db/models.py:5109:        default=PersonaSharePermission.VIEWER,
HEAD:backend/onyx/db/models.py:5110:        server_default=PersonaSharePermission.VIEWER.value,
HEAD:backend/onyx/db/models.py:5132:        default=SkillSharePermission.VIEWER,
HEAD:backend/onyx/db/models.py:5133:        server_default=SkillSharePermission.VIEWER.value,
HEAD:backend/onyx/db/notification.py:153:        and has_global_permission(user, Permission.FULL_ADMIN_PANEL_ACCESS)
HEAD:backend/onyx/db/permissions.py:2:DB operations for recomputing user effective_permissions.
HEAD:backend/onyx/db/permissions.py:5:that query PermissionGrant rows and update the User.effective_permissions
HEAD:backend/onyx/db/permissions.py:48:        return {Permission.WRITE_CHAT.value}
HEAD:backend/onyx/db/permissions.py:57:    time via get_effective_permissions().
HEAD:backend/onyx/db/permissions.py:63:    happens at read time via get_effective_permissions().
HEAD:backend/onyx/db/permissions.py:147:                effective_permissions=sorted(perms),
HEAD:backend/onyx/db/persona.py:12:from onyx.auth.permissions import has_global_permission, has_permission
HEAD:backend/onyx/db/persona.py:92:    if has_global_permission(user, Permission.MANAGE_AGENTS):
HEAD:backend/onyx/db/persona.py:94:    if not get_editable and has_global_permission(user, Permission.READ_AGENTS):
HEAD:backend/onyx/db/persona.py:135:            Persona__User.permission == PersonaSharePermission.EDITOR
HEAD:backend/onyx/db/persona.py:139:            Persona__UG.permission == PersonaSharePermission.EDITOR
HEAD:backend/onyx/db/persona.py:143:            Persona.public_permission == PersonaSharePermission.EDITOR
HEAD:backend/onyx/db/persona.py:251:    if user and not has_global_permission(user, Permission.MANAGE_AGENTS):
HEAD:backend/onyx/db/persona.py:318:        user_id: existing.get(user_id, PersonaSharePermission.VIEWER)
HEAD:backend/onyx/db/persona.py:390:    if has_permission(user, Permission.MANAGE_AGENTS) is not PermissionAuthority.SCOPED:
HEAD:backend/onyx/db/persona.py:428:        permission=Permission.MANAGE_AGENTS,
HEAD:backend/onyx/db/persona.py:450:    if has_permission(user, Permission.MANAGE_AGENTS) is not PermissionAuthority.SCOPED:
HEAD:backend/onyx/db/persona.py:459:        permission=Permission.MANAGE_AGENTS,
HEAD:backend/onyx/db/persona.py:514:    if not has_global_permission(user, Permission.READ_AGENT_ANALYTICS):
HEAD:backend/onyx/db/persona.py:533:    if has_global_permission(user, Permission.MANAGE_AGENTS):
HEAD:backend/onyx/db/persona.py:577:        if has_permission(user, Permission.MANAGE_AGENTS) is PermissionAuthority.SCOPED
HEAD:backend/onyx/db/persona.py:580:    is_manage_agents_admin = has_global_permission(user, Permission.MANAGE_AGENTS)
HEAD:backend/onyx/db/persona.py:581:    is_full_admin = has_global_permission(user, Permission.FULL_ADMIN_PANEL_ACCESS)
HEAD:backend/onyx/db/persona.py:584:        has_permission(user, Permission.ADD_AGENTS) is not PermissionAuthority.NONE
HEAD:backend/onyx/db/persona.py:635:            if not has_global_permission(user, Permission.MANAGE_AGENTS):
HEAD:backend/onyx/db/persona.py:739:    # user/group shares but must not flip is_public / public_permission. Reuse the
HEAD:backend/onyx/db/persona.py:803:        not has_global_permission(user, Permission.MANAGE_AGENTS)
HEAD:backend/onyx/db/persona.py:825:        user, Permission.MANAGE_AGENTS
HEAD:backend/onyx/db/persona.py:916:            existing_share.permission = PersonaSharePermission.EDITOR
HEAD:backend/onyx/db/persona.py:922:                    permission=PersonaSharePermission.EDITOR,
HEAD:backend/onyx/db/persona.py:938:            existing_group_share.permission = PersonaSharePermission.EDITOR
HEAD:backend/onyx/db/persona.py:944:                    permission=PersonaSharePermission.EDITOR,
HEAD:backend/onyx/db/persona.py:1027:        has_global_permission(user, Permission.MANAGE_AGENTS)
HEAD:backend/onyx/db/persona.py:1669:        user, Permission.MANAGE_AGENTS
HEAD:backend/onyx/db/persona.py:1800:            user, Permission.MANAGE_AGENTS
HEAD:backend/onyx/db/persona.py:1979:        or has_global_permission(user, Permission.MANAGE_AGENTS)
HEAD:backend/onyx/db/persona.py:1980:        or (not is_for_edit and has_global_permission(user, Permission.READ_AGENTS))
HEAD:backend/onyx/db/persona_sharing.py:54:    if has_global_permission(user, Permission.MANAGE_AGENTS):
HEAD:backend/onyx/db/persona_sharing.py:60:            if user_share.permission == PersonaSharePermission.EDITOR:
HEAD:backend/onyx/db/persona_sharing.py:65:            if group_share.permission == PersonaSharePermission.EDITOR:
HEAD:backend/onyx/db/persona_sharing.py:69:        if persona.public_permission == PersonaSharePermission.EDITOR:
HEAD:backend/onyx/db/skill.py:45:from onyx.auth.permissions import has_global_permission, has_permission
HEAD:backend/onyx/db/skill.py:137:        non_public_clause=Skill.public_permission.is_(None),
HEAD:backend/onyx/db/skill.py:151:        Skill.public_permission.isnot(None),
HEAD:backend/onyx/db/skill.py:161:        _is_shared_with_user(user, SkillSharePermission.EDITOR),
HEAD:backend/onyx/db/skill.py:162:        _is_shared_with_user_group(user, SkillSharePermission.EDITOR),
HEAD:backend/onyx/db/skill.py:163:        Skill.public_permission == SkillSharePermission.EDITOR,
HEAD:backend/onyx/db/skill.py:165:    if has_permission(user, Permission.MANAGE_SKILLS) is PermissionAuthority.SCOPED:
HEAD:backend/onyx/db/skill.py:230:        if has_global_permission(user, Permission.MANAGE_SKILLS):
HEAD:backend/onyx/db/skill.py:237:        if has_global_permission(user, Permission.MANAGE_SKILLS):
```
## require_permission Implementation Evidence
Evidence lines: 102
```text
HEAD:backend/onyx/auth/permissions.py:2:Permission resolution for group-based authorization.
HEAD:backend/onyx/auth/permissions.py:15:from onyx.db.enums import AccountType, Permission, PermissionAuthority
HEAD:backend/onyx/auth/permissions.py:25:ALL_PERMISSIONS: frozenset[str] = frozenset(p.value for p in Permission)
HEAD:backend/onyx/auth/permissions.py:32:    Permission.MANAGE_AGENTS.value: {
HEAD:backend/onyx/auth/permissions.py:33:        Permission.ADD_AGENTS.value,
HEAD:backend/onyx/auth/permissions.py:34:        Permission.READ_AGENTS.value,
HEAD:backend/onyx/auth/permissions.py:35:        Permission.READ_DOCUMENT_SETS.value,
HEAD:backend/onyx/auth/permissions.py:38:        Permission.READ_AGENT_ANALYTICS.value,
HEAD:backend/onyx/auth/permissions.py:40:    Permission.MANAGE_DOCUMENT_SETS.value: {
HEAD:backend/onyx/auth/permissions.py:41:        Permission.READ_DOCUMENT_SETS.value,
HEAD:backend/onyx/auth/permissions.py:42:        Permission.READ_CONNECTORS.value,
HEAD:backend/onyx/auth/permissions.py:43:        Permission.READ_USER_GROUPS.value,
HEAD:backend/onyx/auth/permissions.py:45:    Permission.MANAGE_CONNECTORS.value: {
HEAD:backend/onyx/auth/permissions.py:46:        Permission.READ_CONNECTORS.value,
HEAD:backend/onyx/auth/permissions.py:47:        Permission.READ_USER_GROUPS.value,
HEAD:backend/onyx/auth/permissions.py:49:    Permission.MANAGE_USER_GROUPS.value: {
HEAD:backend/onyx/auth/permissions.py:50:        Permission.READ_CONNECTORS.value,
HEAD:backend/onyx/auth/permissions.py:51:        Permission.READ_DOCUMENT_SETS.value,
HEAD:backend/onyx/auth/permissions.py:52:        Permission.READ_AGENTS.value,
HEAD:backend/onyx/auth/permissions.py:53:        Permission.READ_USERS.value,
HEAD:backend/onyx/auth/permissions.py:54:        Permission.READ_USER_GROUPS.value,
HEAD:backend/onyx/auth/permissions.py:56:    Permission.MANAGE_LLMS.value: {
HEAD:backend/onyx/auth/permissions.py:57:        Permission.READ_USER_GROUPS.value,
HEAD:backend/onyx/auth/permissions.py:58:        Permission.READ_AGENTS.value,
HEAD:backend/onyx/auth/permissions.py:59:        Permission.READ_USERS.value,
HEAD:backend/onyx/auth/permissions.py:61:    Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS.value: {
HEAD:backend/onyx/auth/permissions.py:62:        Permission.READ_USER_GROUPS.value,
HEAD:backend/onyx/auth/permissions.py:64:    Permission.MANAGE_ACTIONS.value: {
HEAD:backend/onyx/auth/permissions.py:65:        Permission.READ_USER_GROUPS.value,
HEAD:backend/onyx/auth/permissions.py:70:    Permission.BASIC_ACCESS.value: {
HEAD:backend/onyx/auth/permissions.py:71:        Permission.READ_SEARCH.value,
HEAD:backend/onyx/auth/permissions.py:72:        Permission.READ_CHAT.value,
HEAD:backend/onyx/auth/permissions.py:73:        Permission.WRITE_CHAT.value,
HEAD:backend/onyx/auth/permissions.py:74:        Permission.GENERATE_IMAGE.value,
HEAD:backend/onyx/auth/permissions.py:75:        Permission.USE_LLM_GATEWAY.value,
HEAD:backend/onyx/auth/permissions.py:77:    Permission.WRITE_CHAT.value: {Permission.READ_CHAT.value},
HEAD:backend/onyx/auth/permissions.py:78:    Permission.CRAFT_SANDBOX.value: {
HEAD:backend/onyx/auth/permissions.py:79:        Permission.READ_SEARCH.value,
HEAD:backend/onyx/auth/permissions.py:80:        Permission.GENERATE_IMAGE.value,
HEAD:backend/onyx/auth/permissions.py:81:        Permission.USE_LLM_GATEWAY.value,
HEAD:backend/onyx/auth/permissions.py:85:# Permissions that cannot be toggled via the group-permission API.
HEAD:backend/onyx/auth/permissions.py:91:NON_TOGGLEABLE_PERMISSIONS: frozenset[Permission] = frozenset(
HEAD:backend/onyx/auth/permissions.py:93:        Permission.BASIC_ACCESS,
HEAD:backend/onyx/auth/permissions.py:94:        Permission.FULL_ADMIN_PANEL_ACCESS,
HEAD:backend/onyx/auth/permissions.py:95:        Permission.CRAFT_SANDBOX,
HEAD:backend/onyx/auth/permissions.py:96:        Permission.MANAGE_SKILLS,
HEAD:backend/onyx/auth/permissions.py:98:    | Permission.IMPLIED
HEAD:backend/onyx/auth/permissions.py:101:# Permissions auto-granted to all users in Community Edition.
HEAD:backend/onyx/auth/permissions.py:105:CE_UNGATED_PERMISSIONS: frozenset[Permission] = frozenset(
HEAD:backend/onyx/auth/permissions.py:107:        Permission.ADD_AGENTS,
HEAD:backend/onyx/auth/permissions.py:115:SCOPED_MANAGER_PERMISSIONS: frozenset[Permission] = frozenset(
HEAD:backend/onyx/auth/permissions.py:117:        Permission.MANAGE_CONNECTORS,
HEAD:backend/onyx/auth/permissions.py:118:        Permission.MANAGE_DOCUMENT_SETS,
HEAD:backend/onyx/auth/permissions.py:119:        Permission.MANAGE_AGENTS,
HEAD:backend/onyx/auth/permissions.py:120:        Permission.ADD_AGENTS,
HEAD:backend/onyx/auth/permissions.py:121:        Permission.MANAGE_USER_GROUPS,
HEAD:backend/onyx/auth/permissions.py:122:        Permission.MANAGE_ACTIONS,  # scoped via its agents at GATE 2
HEAD:backend/onyx/auth/permissions.py:123:        Permission.MANAGE_SKILLS,  # scoped via Skill__UserGroup at GATE 2
HEAD:backend/onyx/auth/permissions.py:128:class PermissionRegistryEntry(BaseModel):
HEAD:backend/onyx/auth/permissions.py:138:    permissions: list[Permission]
HEAD:backend/onyx/auth/permissions.py:143:    def must_be_toggleable(cls, v: list[Permission]) -> list[Permission]:
HEAD:backend/onyx/auth/permissions.py:147:                    f"Permission '{p.value}' is not toggleable and "
HEAD:backend/onyx/auth/permissions.py:158:PERMISSION_REGISTRY: list[PermissionRegistryEntry] = [
HEAD:backend/onyx/auth/permissions.py:160:    PermissionRegistryEntry(
HEAD:backend/onyx/auth/permissions.py:164:        permissions=[Permission.MANAGE_LLMS],
HEAD:backend/onyx/auth/permissions.py:167:    PermissionRegistryEntry(
HEAD:backend/onyx/auth/permissions.py:172:            Permission.MANAGE_CONNECTORS,
HEAD:backend/onyx/auth/permissions.py:173:            Permission.MANAGE_DOCUMENT_SETS,
HEAD:backend/onyx/auth/permissions.py:177:    PermissionRegistryEntry(
HEAD:backend/onyx/auth/permissions.py:181:        permissions=[Permission.MANAGE_ACTIONS],
HEAD:backend/onyx/auth/permissions.py:185:    PermissionRegistryEntry(
HEAD:backend/onyx/auth/permissions.py:189:        permissions=[Permission.MANAGE_USER_GROUPS],
HEAD:backend/onyx/auth/permissions.py:192:    PermissionRegistryEntry(
HEAD:backend/onyx/auth/permissions.py:196:        permissions=[Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS],
HEAD:backend/onyx/auth/permissions.py:199:    PermissionRegistryEntry(
HEAD:backend/onyx/auth/permissions.py:203:        permissions=[Permission.MANAGE_BOTS],
HEAD:backend/onyx/auth/permissions.py:207:    PermissionRegistryEntry(
HEAD:backend/onyx/auth/permissions.py:211:        permissions=[Permission.ADD_AGENTS],
HEAD:backend/onyx/auth/permissions.py:214:    PermissionRegistryEntry(
HEAD:backend/onyx/auth/permissions.py:218:        permissions=[Permission.MANAGE_AGENTS],
HEAD:backend/onyx/auth/permissions.py:222:    PermissionRegistryEntry(
HEAD:backend/onyx/auth/permissions.py:226:        permissions=[Permission.READ_AGENT_ANALYTICS],
HEAD:backend/onyx/auth/permissions.py:229:    PermissionRegistryEntry(
HEAD:backend/onyx/auth/permissions.py:233:        permissions=[Permission.READ_QUERY_HISTORY],
HEAD:backend/onyx/auth/permissions.py:236:    PermissionRegistryEntry(
HEAD:backend/onyx/auth/permissions.py:240:        permissions=[Permission.CREATE_USER_API_KEYS],
HEAD:backend/onyx/auth/permissions.py:251:    if Permission.FULL_ADMIN_PANEL_ACCESS.value in granted:
HEAD:backend/onyx/auth/permissions.py:276:def get_effective_permissions(user: User) -> set[Permission]:
HEAD:backend/onyx/auth/permissions.py:281:    if Permission.FULL_ADMIN_PANEL_ACCESS in granted:
HEAD:backend/onyx/auth/permissions.py:282:        return set(Permission)
HEAD:backend/onyx/auth/permissions.py:293:    return {Permission(p) for p in expanded}
HEAD:backend/onyx/auth/permissions.py:296:def has_permission(user: User, permission: Permission) -> PermissionAuthority:
HEAD:backend/onyx/auth/permissions.py:304:        return PermissionAuthority.GLOBAL
HEAD:backend/onyx/auth/permissions.py:309:        return PermissionAuthority.SCOPED
HEAD:backend/onyx/auth/permissions.py:310:    return PermissionAuthority.NONE
HEAD:backend/onyx/auth/permissions.py:313:def has_global_permission(user: User, permission: Permission) -> bool:
HEAD:backend/onyx/auth/permissions.py:317:    return has_permission(user, permission) is PermissionAuthority.GLOBAL
HEAD:backend/onyx/auth/permissions.py:320:def require_permission(
HEAD:backend/onyx/auth/permissions.py:321:    required: Permission,
HEAD:backend/onyx/auth/permissions.py:341:        token_scopes: list[Permission] | None = getattr(  # ods: ignore[getattr]
HEAD:backend/onyx/auth/permissions.py:347:            permitted_by_user = authority is not PermissionAuthority.NONE
HEAD:backend/onyx/auth/permissions.py:349:            permitted_by_user = authority is PermissionAuthority.GLOBAL
```
## Routes Using Permission Dependencies
Evidence lines: 450
```text
HEAD:backend/ee/onyx/auth/users.py:27:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:57:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:89:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:124:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:161:    user: User = Depends(require_permission(Permission.READ_AGENT_ANALYTICS)),
HEAD:backend/ee/onyx/server/analytics/api.py:201:    user: User = Depends(require_permission(Permission.READ_AGENT_ANALYTICS)),
HEAD:backend/ee/onyx/server/analytics/api.py:241:    user: User = Depends(require_permission(Permission.READ_AGENT_ANALYTICS)),
HEAD:backend/ee/onyx/server/billing/api.py:171:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:221:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:284:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:360:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:406:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:504:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/documents/cc_pair.py:36:        require_permission(Permission.READ_CONNECTORS, allow_scope=True)
HEAD:backend/ee/onyx/server/documents/cc_pair.py:59:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/ee/onyx/server/documents/cc_pair.py:115:        require_permission(Permission.READ_CONNECTORS, allow_scope=True)
HEAD:backend/ee/onyx/server/documents/cc_pair.py:138:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:201:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:240:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:316:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:350:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:380:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:200:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:221:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:232:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:268:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:280:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:354:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:365:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:407:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:435:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:458:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/gateway/api.py:1395:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1408:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1432:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1462:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1495:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/license/api.py:55:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:81:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:104:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:184:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:220:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:251:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/log_export/api.py:136:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/log_export/api.py:239:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/log_export/api.py:268:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:34:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:50:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:64:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:90:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:102:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:114:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:130:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:154:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/oauth/api.py:27:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:149:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:261:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:328:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/google_drive.py:114:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/slack.py:103:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/query_and_chat/query_backend.py:26:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:56:    _: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:124:    user: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:174:    user: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/ee/onyx/server/query_history/api.py:161:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:210:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:250:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:285:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:313:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:360:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:394:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:39:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:74:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:98:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:30:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:46:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:148:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:158:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:167:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:189:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:212:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:28:        require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:29:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:67:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:83:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:92:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:109:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:131:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:53:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:65:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:85:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:103:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:121:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:141:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:162:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:242:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:265:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:283:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:295:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:87:        require_permission(Permission.READ_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:140:        require_permission(Permission.READ_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:174:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:196:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:205:    _: User = Depends(require_permission(Permission.MANAGE_USER_GROUPS)),
HEAD:backend/ee/onyx/server/user_group/api.py:225:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:271:    user: User = Depends(require_permission(Permission.MANAGE_USER_GROUPS)),
HEAD:backend/ee/onyx/server/user_group/api.py:306:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:351:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:377:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:400:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:421:    user: User = Depends(require_permission(Permission.MANAGE_USER_GROUPS)),
HEAD:backend/ee/onyx/server/user_group/api.py:461:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:531:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/ee/onyx/server/user_group/api.py:618:        require_permission(Permission.MANAGE_USER_GROUPS, allow_scope=True)
HEAD:backend/onyx/server/api_key/api.py:32:    _: User = Depends(require_permission(Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS)),
HEAD:backend/onyx/server/api_key/api.py:41:    _: User = Depends(require_permission(Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS)),
HEAD:backend/onyx/server/api_key/api.py:56:        require_permission(Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS)
HEAD:backend/onyx/server/api_key/api.py:78:        require_permission(Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS)
HEAD:backend/onyx/server/api_key/api.py:98:        require_permission(Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS)
HEAD:backend/onyx/server/api_key/api.py:120:        require_permission(Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS)
HEAD:backend/onyx/server/documents/cc_pair.py:123:        require_permission(Permission.READ_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/cc_pair.py:163:        require_permission(Permission.READ_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/cc_pair.py:240:        require_permission(Permission.READ_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/cc_pair.py:290:        require_permission(Permission.READ_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/cc_pair.py:341:        require_permission(Permission.READ_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/cc_pair.py:474:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/cc_pair.py:581:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/cc_pair.py:615:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/cc_pair.py:670:        require_permission(Permission.READ_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/cc_pair.py:688:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/cc_pair.py:743:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/documents/cc_pair.py:759:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/documents/cc_pair.py:802:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/cc_pair.py:928:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:185:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:205:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:224:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:436:    _: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:444:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:563:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:784:    _: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:818:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:906:        require_permission(Permission.READ_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/connector.py:969:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/connector.py:1461:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/connector.py:1502:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/connector.py:1591:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:1641:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:1667:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/connector.py:1749:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1770:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1791:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1821:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1849:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:1866:    _: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/onyx/server/documents/connector.py:1878:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:1907:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:61:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/credential.py:83:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/credential.py:105:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/credential.py:125:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/credential.py:172:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/credential.py:205:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/credential.py:265:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:281:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:305:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/credential.py:336:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/credential.py:382:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:425:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:450:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential_capabilities.py:138:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/credential_capabilities.py:267:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/credential_capabilities.py:311:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/document.py:28:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/document.py:73:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/standard_oauth.py:201:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/standard_oauth.py:247:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/standard_oauth.py:297:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/targeted_reindex.py:81:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/documents/targeted_reindex.py:175:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/features/admin_banner/api.py:38:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/admin_banner/api.py:46:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/admin_banner/api.py:66:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/api.py:35:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/api.py:51:    dependencies=[Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS))],
HEAD:backend/onyx/server/features/build/api.py:58:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/approvals/api.py:123:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/approvals/api.py:148:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/approvals/api.py:204:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/debug.py:42:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:161:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:207:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:280:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:316:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:333:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:342:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:375:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:405:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:421:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:440:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/oauth.py:87:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/oauth.py:137:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/interactive_turns/api.py:111:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/interactive_turns/api.py:132:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:399:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:411:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:460:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:472:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:524:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:538:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/scheduled_tasks/api.py:563:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:89:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:108:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:167:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:204:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:215:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:234:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:267:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:285:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:305:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:323:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:359:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:438:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:473:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:506:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:524:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:562:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:613:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:655:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:681:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:703:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:734:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:771:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:822:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:873:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/api.py:925:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/messages.py:64:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/messages.py:84:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/messages.py:225:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/session/messages.py:292:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/user_library/api.py:153:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/user_library/api.py:183:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/user_library/api.py:287:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/user_library/api.py:451:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/user_library/api.py:485:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/default_assistant/api.py:28:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/default_assistant/api.py:53:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/document_set/api.py:51:        require_permission(Permission.MANAGE_DOCUMENT_SETS, allow_scope=True)
HEAD:backend/onyx/server/features/document_set/api.py:117:        require_permission(Permission.MANAGE_DOCUMENT_SETS, allow_scope=True)
HEAD:backend/onyx/server/features/document_set/api.py:185:        require_permission(Permission.MANAGE_DOCUMENT_SETS, allow_scope=True)
HEAD:backend/onyx/server/features/document_set/api.py:234:        require_permission(Permission.MANAGE_DOCUMENT_SETS, allow_scope=True)
HEAD:backend/onyx/server/features/document_set/api.py:289:    user: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/onyx/server/features/document_set/api.py:339:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/hierarchy/api.py:71:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/hierarchy/api.py:99:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/hierarchy/api.py:156:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/image_generation/api.py:221:    _user: User = Depends(require_permission(Permission.GENERATE_IMAGE)),
HEAD:backend/onyx/server/features/input_prompt/api.py:32:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/input_prompt/api.py:47:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/input_prompt/api.py:62:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/input_prompt/api.py:86:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/input_prompt/api.py:109:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/input_prompt/api.py:127:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/input_prompt/api.py:142:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:625:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/mcp/api.py:636:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:891:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:1002:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:1102:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:1322:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:1350:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:1367:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:1402:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/mcp/api.py:1419:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/mcp/api.py:1484:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/mcp/api.py:2176:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/mcp/api.py:2207:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/mcp/api.py:2244:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/mcp/api.py:2272:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/mcp/api.py:2324:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/mcp/api.py:2371:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/mcp/api.py:2446:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/mcp/api.py:2500:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/mcp/api.py:2563:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/mcp/api.py:2656:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/notifications/api.py:122:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/notifications/api.py:197:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/notifications/api.py:216:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/notifications/api.py:225:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/oauth_config/api.py:88:    _: User = Depends(require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)),
HEAD:backend/onyx/server/features/oauth_config/api.py:111:    _: User = Depends(require_permission(Permission.MANAGE_ACTIONS)),
HEAD:backend/onyx/server/features/oauth_config/api.py:123:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/oauth_config/api.py:143:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/oauth_config/api.py:178:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/oauth_config/api.py:203:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/oauth_config/api.py:240:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/oauth_config/api.py:301:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/password/api.py:23:    current_user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/password/api.py:47:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:170:    user: User = Depends(require_permission(Permission.MANAGE_AGENTS)),
HEAD:backend/onyx/server/features/persona/api.py:188:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:207:    user: User = Depends(require_permission(Permission.MANAGE_AGENTS)),
HEAD:backend/onyx/server/features/persona/api.py:225:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:251:    user: User = Depends(require_permission(Permission.READ_AGENTS, allow_scope=True)),
HEAD:backend/onyx/server/features/persona/api.py:268:    user: User = Depends(require_permission(Permission.READ_AGENTS, allow_scope=True)),
HEAD:backend/onyx/server/features/persona/api.py:314:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:328:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:347:    user: User = Depends(require_permission(Permission.ADD_AGENTS, allow_scope=True)),
HEAD:backend/onyx/server/features/persona/api.py:379:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:404:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:416:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:433:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:446:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:491:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:540:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:565:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/persona/api.py:584:    user: User = Depends(require_permission(Permission.ADD_AGENTS, allow_scope=True)),
HEAD:backend/onyx/server/features/persona/api.py:772:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:148:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:161:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:181:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:240:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:257:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:284:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:329:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:376:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:404:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:435:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:465:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:492:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:521:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:581:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:609:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:635:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:654:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:673:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:701:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/projects/api.py:739:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/search/api.py:59:    user: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/onyx/server/features/skill/api.py:178:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:193:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:212:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:229:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:247:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:291:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:316:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:418:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:506:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:524:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),  # noqa: ARG001
HEAD:backend/onyx/server/features/skill/api.py:557:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:602:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:630:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:658:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:789:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:867:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/skill/api.py:940:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/tool/api.py:153:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/tool/api.py:181:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/tool/api.py:215:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/tool/api.py:244:        require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)
HEAD:backend/onyx/server/features/tool/api.py:299:    _: User = Depends(require_permission(Permission.MANAGE_ACTIONS, allow_scope=True)),
HEAD:backend/onyx/server/features/tool/api.py:331:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/tool/api.py:357:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/tool/api.py:374:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/usage/api.py:311:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/usage/api.py:357:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/usage/api.py:403:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/usage/api.py:426:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/features/usage/api.py:435:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/features/usage/api.py:457:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/features/user_oauth_token/api.py:26:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/web_search/api.py:233:    _: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/onyx/server/features/web_search/api.py:276:    _: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/onyx/server/features/web_search/api.py:292:    _: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/onyx/server/federated/api.py:71:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/federated/api.py:116:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/federated/api.py:158:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/federated/api.py:203:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/federated/api.py:231:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/federated/api.py:263:    _: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/federated/api.py:287:    _: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/federated/api.py:330:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/federated/api.py:379:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/federated/api.py:458:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/federated/api.py:478:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/federated/api.py:524:    user: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/federated/api.py:571:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/federated/api.py:602:    _: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/federated/api.py:620:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/kg/api.py:60:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/kg/api.py:71:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/kg/api.py:84:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/kg/api.py:93:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/kg/api.py:178:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/kg/api.py:209:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/administrative.py:65:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/manage/administrative.py:90:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/manage/administrative.py:105:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/manage/administrative.py:119:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/administrative.py:153:        require_permission(Permission.MANAGE_CONNECTORS, allow_scope=True)
HEAD:backend/onyx/server/manage/administrative.py:241:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/code_interpreter/api.py:25:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/code_interpreter/api.py:40:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/code_interpreter/api.py:50:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/discord_bot/api.py:68:    __: User = Depends(require_permission(Permission.MANAGE_BOTS)),
HEAD:backend/onyx/server/manage/discord_bot/api.py:86:    __: User = Depends(require_permission(Permission.MANAGE_BOTS)),
HEAD:backend/onyx/server/manage/discord_bot/api.py:112:    __: User = Depends(require_permission(Permission.MANAGE_BOTS)),
HEAD:backend/onyx/server/manage/discord_bot/api.py:135:    _: User = Depends(require_permission(Permission.MANAGE_BOTS)),
HEAD:backend/onyx/server/manage/discord_bot/api.py:158:    _: User = Depends(require_permission(Permission.MANAGE_BOTS)),
HEAD:backend/onyx/server/manage/discord_bot/api.py:168:    _: User = Depends(require_permission(Permission.MANAGE_BOTS)),
HEAD:backend/onyx/server/manage/discord_bot/api.py:187:    _: User = Depends(require_permission(Permission.MANAGE_BOTS)),
HEAD:backend/onyx/server/manage/discord_bot/api.py:201:    _: User = Depends(require_permission(Permission.MANAGE_BOTS)),
HEAD:backend/onyx/server/manage/discord_bot/api.py:223:    _: User = Depends(require_permission(Permission.MANAGE_BOTS)),
HEAD:backend/onyx/server/manage/discord_bot/api.py:252:    _: User = Depends(require_permission(Permission.MANAGE_BOTS)),
HEAD:backend/onyx/server/manage/discord_bot/api.py:274:    _: User = Depends(require_permission(Permission.MANAGE_BOTS)),
HEAD:backend/onyx/server/manage/embedding/api.py:41:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/embedding/api.py:72:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/embedding/api.py:81:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/embedding/api.py:93:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/embedding/api.py:108:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/embedding/api.py:128:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/image_generation/api.py:210:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/image_generation/api.py:309:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/image_generation/api.py:372:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/image_generation/api.py:383:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/image_generation/api.py:404:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/image_generation/api.py:501:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/image_generation/api.py:533:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/image_generation/api.py:546:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/llm/api.py:402:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/llm/api.py:425:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:433:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:445:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:508:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:524:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:574:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:596:    user: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:736:    user: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:770:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:784:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:798:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/llm/api.py:811:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/manage/llm/api.py:823:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:836:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:846:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:864:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:1154:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:1238:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:1437:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
HEAD:backend/onyx/server/manage/llm/api.py:1563:    _: User = Depends(require_permission(Permission.MANAGE_LLMS)),
```
Static evidence confirms permission dependencies are used by application
routes.
This does not prove complete route coverage.
## Tenant Context
Evidence lines: 500
```text
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:38:def _domain_token(tenant_id: str, domain: str) -> str:
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
HEAD:backend/ee/onyx/auth/users.py:45:def generate_anonymous_user_jwt_token(tenant_id: str) -> str:
HEAD:backend/ee/onyx/auth/users.py:47:        "tenant_id": tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:19:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/background/celery/tasks/beat_schedule.py:68:if not MULTI_TENANT:
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:21:def export_query_history_cleanup_task(*, tenant_id: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:22:    with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:12:    ONYX_CLOUD_TENANT_ID,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:17:from onyx.db.engine.tenant_utils import get_all_tenant_ids
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:89:    redis_client = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:101:    tenant_ids: list[str] = []
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:154:        tenant_ids = get_all_tenant_ids()
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:163:        for tenant_id in tenant_ids:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:164:            if tenant_id in gated_tenants:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:174:            if IGNORED_SYNCING_TENANT_LIST and tenant_id in IGNORED_SYNCING_TENANT_LIST:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:182:                    active_tenants is not None and tenant_id not in active_tenants
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:195:                    tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:231:        f"num_tenants={len(tenant_ids)} "
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:58:    get_session_with_current_tenant,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:102:    LoggerContextVars,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:108:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:126:    Base expiration is 300 seconds, multiplied by the beat multiplier only in MULTI_TENANT mode.
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:130:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:152:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:212:def check_for_doc_permissions_sync(self: Task, *, tenant_id: str) -> bool | None:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:232:        with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:244:            maybe_mark_tenant_active(tenant_id, caller="doc_permission_sync")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:249:                self.app, cc_pair_id, r, tenant_id
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:267:                    tenant_id, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:293:                with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:295:                        tenant_id, key_bytes, r, db_session
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:297:        task_logger.info(f"check_for_doc_permissions_sync finished: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:305:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:308:            f"Unexpected check_for_doc_permissions_sync exception: tenant={tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:321:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:329:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:358:            with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:381:                tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:420:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:429:    LoggerContextVars.reset()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:436:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:445:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:516:        with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:595:            with get_session_with_current_tenant() as fetch_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:606:            with get_session_with_current_tenant() as fetch_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:655:        with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:710:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:729:        with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:791:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:824:            tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:838:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:882:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1063:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1078:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1110:        tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:1125:        tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:51:from onyx.db.engine.sql_engine import get_session_with_current_tenant
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:84:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:94:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:103:    Base expiration is 300 seconds, multiplied by the beat multiplier only in MULTI_TENANT mode.
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:107:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:169:def check_for_external_group_sync(self: Task, *, tenant_id: str) -> bool | None:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:183:            f"Failed to acquire beat lock for external group sync: {tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:189:        with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:218:            maybe_mark_tenant_active(tenant_id, caller="external_group_sync")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:223:                self.app, cc_pair_id, r, tenant_id
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:241:                    tenant_id, self.app, r, r_replica, r_celery, lock_beat
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:260:            f"Unexpected check_for_external_group_sync exception: tenant={tenant_id} {error_msg}"
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:262:        task_logger.exception(f"Unexpected exception: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:267:    task_logger.info(f"check_for_external_group_sync finished: tenant={tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:275:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:281:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:298:            with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:324:                tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:362:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:369:    redis_connector = RedisConnector(tenant_id, cc_pair_id)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:434:            tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:437:        with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:457:        with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:481:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:487:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:501:            tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:511:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:515:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:575:            external_user_group_generator = ext_group_sync_func(tenant_id, cc_pair)
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:680:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:701:            tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:712:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py:754:    redis_connector = RedisConnector(tenant_id, int(cc_pair_id))
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:5:from onyx.db.engine.sql_engine import get_session_with_current_tenant
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:20:def hook_execution_log_cleanup_task(*, tenant_id: str) -> None:  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/hooks/tasks.py:22:        with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:17:from onyx.db.engine.sql_engine import get_session_with_current_tenant
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:19:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:29:def check_license_expiry_notifications_task(*, tenant_id: str) -> None:  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:30:    if MULTI_TENANT:
HEAD:backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py:33:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:20:from onyx.db.engine.sql_engine import get_session_with_current_tenant
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:23:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:87:def reclaim_license_task(*, tenant_id: str) -> None:  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:88:    if MULTI_TENANT:
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:91:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:120:                payload.tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/license_reclaim/tasks.py:132:                "Failed to reclaim license for tenant %s: %s", payload.tenant_id, e
HEAD:backend/ee/onyx/background/celery/tasks/log_export/tasks.py:69:    tenant_id: str,  # noqa: ARG001  # Injected into every beat task by ``DynamicTenantScheduler``.
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:16:from onyx.db.engine.sql_engine import get_session_with_current_tenant
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:43:    # Need to include the tenant_id since the TenantAwareTask needs this
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:44:    tenant_id: str,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:62:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/query_history/tasks.py:99:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:24:def revalidate_sso_domains_task(*, tenant_id: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:31:        reproject_tenant_login_domains(tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:33:        logger.exception("Failed to re-project login domains for %s", tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/sso_domain_revalidation/tasks.py:34:    revalidate_tenant_domains(tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:15:    ONYX_CLOUD_TENANT_ID,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:25:from shared_configs.configs import MULTI_TENANT, TENANT_ID_PREFIX
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:52:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:58:    r = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:139:        tenant_ids = [t.tenant_id for t in pool_tenants]
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:141:    if not tenant_ids:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:145:        f"Checking {len(tenant_ids)} pool tenant(s) for pending migrations"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:148:    for tenant_id in tenant_ids:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:150:            run_alembic_migrations(tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:151:            new_version = get_current_alembic_version(tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:155:                    .filter_by(tenant_id=tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:160:                        f"Migrated pool tenant {tenant_id}: {tenant.alembic_version} -> {new_version}"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:166:                f"Failed to migrate pool tenant {tenant_id}, skipping"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:178:    # The MULTI_TENANT check is now done at the caller level (check_available_tenants)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:188:    r = get_redis_client(tenant_id=ONYX_CLOUD_TENANT_ID)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:201:    tenant_id: str | None = None
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:204:        tenant_id = TENANT_ID_PREFIX + str(uuid.uuid4())
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:206:        task_logger.info(f"Pre-provisioning tenant {tenant_id} on shard {shard_name}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:209:        record_tenant_placement(tenant_id, shard_name)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:212:        schema_created = create_schema_if_not_exists(tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:214:            task_logger.debug(f"Created schema for tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:216:            task_logger.debug(f"Schema already exists for tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:219:        task_logger.debug(f"Setting up tenant configuration: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:220:        asyncio.run(setup_tenant(tenant_id))
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:221:        task_logger.debug(f"Tenant configuration completed: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:224:        alembic_version = get_current_alembic_version(tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:226:            f"Tenant {tenant_id} using Alembic version: {alembic_version}"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:230:        task_logger.debug(f"Storing pre-provisioned tenant in database: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:236:                    tenant_id=tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:243:                task_logger.info(f"Successfully pre-provisioned tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:248:                    f"Failed to store pre-provisioned tenant: {tenant_id}",
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:255:        # If we have a tenant_id, attempt to rollback any partially completed provisioning
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:256:        if tenant_id:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:258:                f"Rolling back failed tenant provisioning for: {tenant_id}"
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:265:                asyncio.run(rollback_tenant_provisioning(tenant_id))
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:267:                task_logger.exception(f"Error during rollback for tenant: {tenant_id}")
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:16:from onyx.db.engine.sql_engine import get_session_with_current_tenant
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:69:    tenant_id: str,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:92:    redis_client = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:103:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:110:            with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:134:                    "tenant_id": tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:154:def check_ttl_management_task(self: Task, *, tenant_id: str) -> None:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:164:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:170:    redis_client = get_redis_client(tenant_id=tenant_id)
HEAD:backend/ee/onyx/background/celery/tasks/ttl_management/tasks.py:188:                "tenant_id": tenant_id,
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:8:from onyx.db.engine.sql_engine import get_session_with_current_tenant
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:24:    tenant_id: str,  # noqa: ARG001
HEAD:backend/ee/onyx/background/celery/tasks/usage_reporting/tasks.py:42:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:20:    tenant_id: str, key_bytes: bytes, r: TenantRedisClient, db_session: Session
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:35:    rug = RedisUserGroup(tenant_id, usergroup_id)
HEAD:backend/ee/onyx/background/task_name_builders.py:10:    tenant_id: str | None = None,  # noqa: ARG001
HEAD:backend/ee/onyx/configs/app_configs.py:169:# Used when MULTI_TENANT=false (self-hosted mode)
HEAD:backend/ee/onyx/configs/license_enforcement_config.py:16:Multi-tenant cloud gating lives in `multi_tenant_gating_config.py` and is
HEAD:backend/ee/onyx/configs/license_enforcement_config.py:48:        # Proxy endpoints for self-hosted billing (no tenant context)
HEAD:backend/ee/onyx/configs/multi_tenant_gating_config.py:6:Consumed by `tenant_tracking` middleware. When a tenant is in the
HEAD:backend/ee/onyx/configs/multi_tenant_gating_config.py:28:MULTI_TENANT_GATING_ALLOWED_PREFIXES: frozenset[str] = frozenset(
HEAD:backend/ee/onyx/db/license.py:20:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/db/license.py:21:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/ee/onyx/db/license.py:39:def _advisory_lock_id(namespace: str, tenant_id: str) -> int:
HEAD:backend/ee/onyx/db/license.py:40:    digest = hashlib.sha256(f"{namespace}:{tenant_id}".encode()).digest()
HEAD:backend/ee/onyx/db/license.py:45:def seat_lock_id_for_tenant(tenant_id: str) -> int:
HEAD:backend/ee/onyx/db/license.py:46:    return _advisory_lock_id(_SEAT_LOCK_NAMESPACE, tenant_id)
HEAD:backend/ee/onyx/db/license.py:58:        _advisory_lock_id(_LICENSE_STORE_LOCK_NAMESPACE, get_current_tenant_id()),
HEAD:backend/ee/onyx/db/license.py:62:def acquire_seat_lock(db_session: Session, tenant_id: str | None = None) -> None:
HEAD:backend/ee/onyx/db/license.py:69:        db_session, seat_lock_id_for_tenant(tenant_id or get_current_tenant_id())
HEAD:backend/ee/onyx/db/license.py:197:def get_used_seats(tenant_id: str | None = None) -> int:
HEAD:backend/ee/onyx/db/license.py:207:    if MULTI_TENANT:
HEAD:backend/ee/onyx/db/license.py:210:        return get_tenant_count(tenant_id or get_current_tenant_id())
HEAD:backend/ee/onyx/db/license.py:212:        from onyx.db.engine.sql_engine import get_session_with_current_tenant
HEAD:backend/ee/onyx/db/license.py:214:        with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/db/license.py:233:def get_cached_license_metadata(tenant_id: str | None = None) -> LicenseMetadata | None:
HEAD:backend/ee/onyx/db/license.py:238:        tenant_id: Tenant ID (for multi-tenant deployments)
HEAD:backend/ee/onyx/db/license.py:243:    cache = get_cache_backend(tenant_id=tenant_id)
HEAD:backend/ee/onyx/db/license.py:258:def invalidate_license_cache(tenant_id: str | None = None) -> None:
HEAD:backend/ee/onyx/db/license.py:267:        tenant_id: Tenant ID (for multi-tenant deployments)
HEAD:backend/ee/onyx/db/license.py:269:    cache = get_cache_backend(tenant_id=tenant_id)
HEAD:backend/ee/onyx/db/license.py:277:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/db/license.py:287:    used_seats = get_used_seats(tenant_id)
HEAD:backend/ee/onyx/db/license.py:301:        tenant_id=payload.tenant_id,
HEAD:backend/ee/onyx/db/license.py:327:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/db/license.py:334:    metadata, ttl = build_license_metadata(payload, grace_period_end, tenant_id)
HEAD:backend/ee/onyx/db/license.py:335:    cache = get_cache_backend(tenant_id=tenant_id)
HEAD:backend/ee/onyx/db/license.py:352:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/db/license.py:372:    with _license_cache_lock(tenant_id, wait_for_lock) as lock:
HEAD:backend/ee/onyx/db/license.py:376:            invalidate_license_cache(tenant_id)
HEAD:backend/ee/onyx/db/license.py:382:            metadata, _ = build_license_metadata(payload, tenant_id=tenant_id)
HEAD:backend/ee/onyx/db/license.py:384:        metadata = update_license_cache(payload, tenant_id=tenant_id)
HEAD:backend/ee/onyx/db/license.py:390:            invalidate_license_cache(tenant_id)
HEAD:backend/ee/onyx/db/license.py:396:    tenant_id: str | None, wait: bool
HEAD:backend/ee/onyx/db/license.py:406:        candidate = get_cache_backend(tenant_id=tenant_id).lock(
HEAD:backend/ee/onyx/db/license.py:429:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/db/license.py:436:        tenant_id: Tenant ID (for multi-tenant deployments)
HEAD:backend/ee/onyx/db/license.py:445:            db_session, tenant_id=tenant_id, wait_for_lock=False
HEAD:backend/ee/onyx/db/license.py:449:        invalidate_license_cache(tenant_id)
HEAD:backend/ee/onyx/db/license.py:455:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/db/license.py:462:        tenant_id: Tenant ID (for multi-tenant deployments)
HEAD:backend/ee/onyx/db/license.py:468:    cached = get_cached_license_metadata(tenant_id)
HEAD:backend/ee/onyx/db/license.py:473:    return refresh_license_cache(db_session, tenant_id)
HEAD:backend/ee/onyx/db/license.py:479:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/db/license.py:487:        tenant_id: Tenant ID (for multi-tenant deployments)
HEAD:backend/ee/onyx/db/license.py:494:    metadata = get_license_metadata(db_session, tenant_id)
HEAD:backend/ee/onyx/db/license.py:501:    current_used = get_used_seats(tenant_id)
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:29:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:45:def lookup_tenant_id_for_email_domain(email: str) -> str | None:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:48:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:57:            select(TenantSSODomain.tenant_id).where(
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:64:def is_email_domain_verified(tenant_id: str, email: str) -> bool:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:72:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:82:                select(TenantSSODomain.tenant_id).where(
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:83:                    TenantSSODomain.tenant_id == tenant_id,
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:92:def claim_email_domains(tenant_id: str, domains: list[str]) -> None:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:99:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:108:                    TenantSSODomain.tenant_id == tenant_id
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:117:                    TenantSSODomain.tenant_id == tenant_id,
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:123:            db_session.add(TenantSSODomain(tenant_id=tenant_id, domain=domain))
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:133:def list_login_domains(tenant_id: str) -> list[LoginDomainRecord]:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:135:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:141:                TenantSSODomain.tenant_id == tenant_id
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:151:def is_claimed_domain(tenant_id: str, domain: str) -> bool:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:152:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:156:            db_session.get(TenantSSODomain, (tenant_id, _catalog_key(domain)))
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:161:def mark_domain_verified(tenant_id: str, domain: str) -> None:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:164:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:168:        row = db_session.get(TenantSSODomain, (tenant_id, _catalog_key(domain)))
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:186:def mark_domain_unverified(tenant_id: str, domain: str) -> None:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:189:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:193:        row = db_session.get(TenantSSODomain, (tenant_id, _catalog_key(domain)))
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:200:def reproject_tenant_login_domains(tenant_id: str) -> None:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:204:    with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:206:    claim_email_domains(tenant_id, sorted(domains))
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:30:from shared_configs.configs import MULTI_TENANT, POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:31:from shared_configs.contextvars import CURRENT_TENANT_ID_CONTEXTVAR
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:45:            UserTenantMappingOAuthAccount.tenant_id == UserTenantMapping.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:51:def get_tenant_id_for_email(email: str) -> str:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:52:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:58:            select(UserTenantMapping.tenant_id).where(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:63:        tenant_id = result.scalar_one_or_none()
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:67:        if tenant_id is None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:68:            inactive_tenant_ids = (
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:70:                    select(UserTenantMapping.tenant_id).where(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:78:            if len(inactive_tenant_ids) == 1:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:79:                tenant_id = inactive_tenant_ids[0]
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:82:                    UserTenantMapping.tenant_id == tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:85:            elif inactive_tenant_ids:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:95:    if tenant_id is None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:97:    return tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:100:def lookup_tenant_id_for_login(email: str) -> str | None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:104:    ``get_tenant_id_for_email`` it must not accept a pending invitation on the
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:108:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:113:        active_tenant_ids = (
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:115:                select(UserTenantMapping.tenant_id).where(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:123:        if len(active_tenant_ids) == 1:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:124:            return active_tenant_ids[0]
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:125:        if active_tenant_ids:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:128:        pending_tenant_ids = (
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:130:                select(UserTenantMapping.tenant_id).where(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:138:        return pending_tenant_ids[0] if len(pending_tenant_ids) == 1 else None
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:141:def resolve_tenant_id(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:151:    superseded_tenant_id: str | None = None
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:153:        tenant_id = get_tenant_id_for_oauth_account(oauth_name, account_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:154:        if tenant_id:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:155:            return tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:156:        superseded_tenant_id = get_superseded_tenant_id_for_oauth_account(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:161:        return get_tenant_id_for_email(email)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:163:        return superseded_tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:167:        if superseded_tenant_id is None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:169:        return superseded_tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:172:def _oauth_account_tenant_id(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:178:            select(UserTenantMapping.tenant_id).where(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:185:def get_tenant_id_for_oauth_account(oauth_name: str, account_id: str) -> str | None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:190:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:193:    return _oauth_account_tenant_id(oauth_name, account_id, active=True)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:196:def get_superseded_tenant_id_for_oauth_account(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:205:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:208:    return _oauth_account_tenant_id(oauth_name, account_id, active=False)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:223:    tenant_id: str, email: str, oauth_name: str, account_id: str
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:225:    """Whether this login is already an active member of tenant_id, by address
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:229:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:235:            select(UserTenantMapping.tenant_id).where(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:237:                UserTenantMapping.tenant_id == tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:243:    return get_tenant_id_for_oauth_account(oauth_name, account_id) == tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:247:    email: str, tenant_id: str, oauth_name: str, account_id: str
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:261:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:265:    add_users_to_tenant([normalized_email], tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:268:        mapping = db_session.get(UserTenantMapping, (normalized_email, tenant_id))
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:272:        accept_user_invite(normalized_email, tenant_id, [(oauth_name, account_id)])
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:276:    email: str, tenant_id: str, oauth_name: str, account_id: str
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:287:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:292:        if db_session.get(UserTenantMapping, (normalized_email, tenant_id)) is None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:293:            logger.info("No mapping row to link in tenant %s", tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:302:                tenant_id=tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:312:                UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:319:                    UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:325:            if owner is None or tuple(owner) != (normalized_email, tenant_id):
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:338:        UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:345:    return tuple_(UserTenantMapping.email, UserTenantMapping.tenant_id).in_(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:352:    tenant_id: str,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:367:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:372:        logger.warning("No linked OAuth identity to rekey in tenant %s", tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:381:            select(UserTenantMapping.tenant_id).where(
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:383:                UserTenantMapping.tenant_id != tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:391:                tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:398:                UserTenantMapping.tenant_id == tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:405:            logger.warning("No mapping row to rekey in tenant %s", tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:411:                UserTenantMapping.tenant_id == tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:420:        candidate_keys = {(row.email, row.tenant_id) for row in matched_mappings}
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:422:            candidate_keys.add((destination.email, destination.tenant_id))
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:427:                    UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:438:                tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:468:                        UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:471:                            (mapping.email, mapping.tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:488:                account.tenant_id = destination.tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:503:def add_users_to_tenant(emails: list[str], tenant_id: str) -> None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:526:                    UserTenantMapping.tenant_id == tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:560:                    tenant_id=tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:574:                        tenant_id=tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:581:            logger.info("Successfully added users %s to tenant %s", emails, tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:584:            logger.exception("Failed to add users to tenant %s", tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:589:def remove_users_from_tenant(emails: list[str], tenant_id: str) -> None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:597:                    UserTenantMapping.tenant_id == tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:608:                "Failed to remove users from tenant %s: %s", tenant_id, str(e)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:613:def remove_all_users_from_tenant(tenant_id: str) -> None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:616:            UserTenantMapping.tenant_id == tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:621:def approve_user_invite(email: str, tenant_id: str) -> None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:638:                if candidate.tenant_id == tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:656:                tenant_id=tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:682:    tenant_id: str,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:713:                    and candidate.tenant_id == tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:726:                            UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:745:                    (owner_email, owner_tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:746:                    for _, _, owner_email, owner_tenant_id in presented_links
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:747:                } - {(mapping.email, mapping.tenant_id)}
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:755:                            UserTenantMappingOAuthAccount.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:765:                    account.tenant_id = mapping.tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:773:                            tenant_id=mapping.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:789:                    if (candidate.email, candidate.tenant_id) in owned_mapping_keys:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:800:                    "User %s accepted invitation to tenant %s", email, tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:804:                    "No invitation found for user %s in tenant %s", email, tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:812:                tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:818:    token = CURRENT_TENANT_ID_CONTEXTVAR.set(tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:826:        CURRENT_TENANT_ID_CONTEXTVAR.reset(token)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:829:def deny_user_invite(email: str, tenant_id: str) -> None:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:841:                UserTenantMapping.tenant_id == tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:849:            logger.info("User %s denied invitation to tenant %s", email, tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:852:                "No invitation found for user %s in tenant %s", email, tenant_id
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:854:    token = CURRENT_TENANT_ID_CONTEXTVAR.set(tenant_id)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:861:        CURRENT_TENANT_ID_CONTEXTVAR.reset(token)
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:864:def get_tenant_count(tenant_id: str) -> int:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:885:                UserTenantMapping.tenant_id == tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:897:    with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:932:                    UserTenantMapping.tenant_id == invitation.tenant_id,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:938:                tenant_id=invitation.tenant_id, number_of_users=user_count
HEAD:backend/ee/onyx/external_permissions/box/group_sync.py:55:    tenant_id: str,  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/canvas/group_sync.py:74:    tenant_id: str,  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:20:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/ee/onyx/external_permissions/confluence/doc_sync.py:44:        get_current_tenant_id(), "confluence", cc_pair.credential_id
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:12:from onyx.db.engine.sql_engine import get_session_with_current_tenant
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:84:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:161:    tenant_id: str,
HEAD:backend/ee/onyx/external_permissions/confluence/group_sync.py:164:    provider = OnyxDBCredentialsProvider(tenant_id, "confluence", cc_pair.credential_id)
HEAD:backend/ee/onyx/external_permissions/github/group_sync.py:16:    tenant_id: str,  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/google_drive/group_sync.py:503:    tenant_id: str,  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/jira/group_sync.py:150:    tenant_id: str,  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/perm_sync_types.py:62:        str,  # tenant_id
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:8:from onyx.db.engine.sql_engine import get_session_with_current_tenant
HEAD:backend/ee/onyx/external_permissions/post_query_censoring.py:27:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:11:from onyx.db.engine.sql_engine import get_session_with_current_tenant
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:47:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/external_permissions/salesforce/postprocessing.py:220:    with get_session_with_current_tenant() as db_session:
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:16:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:33:    tenant_id: str, sf_client: OnyxSalesforce
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:39:            if key[0] == tenant_id and key[1]() is sf_client
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:86:    tenant_id = get_current_tenant_id()
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:87:    cache_key = (tenant_id, credential.id)
HEAD:backend/ee/onyx/external_permissions/salesforce/utils.py:123:    cache_key = (get_current_tenant_id(), ref(sf_client), user_email)
HEAD:backend/ee/onyx/external_permissions/sharepoint/group_sync.py:17:    tenant_id: str,  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:55:    tenant_id: str,  # noqa: ARG001
HEAD:backend/ee/onyx/external_permissions/slack/group_sync.py:61:    # The provider derives the tenant from the request context, like doc sync.
HEAD:backend/ee/onyx/external_permissions/sync_params.py:58:        tenant_id: str, cc_pair: "ConnectorCredentialPair"
HEAD:backend/ee/onyx/external_permissions/sync_params.py:60:        return load()(tenant_id, cc_pair)
HEAD:backend/ee/onyx/feature_flags/posthog_provider.py:60:        self, flag_key: str, tenant_id: str
HEAD:backend/ee/onyx/feature_flags/posthog_provider.py:68:                tenant_id,
HEAD:backend/ee/onyx/feature_flags/posthog_provider.py:69:                person_properties={"tenant_id": tenant_id},
HEAD:backend/ee/onyx/feature_flags/posthog_provider.py:75:                tenant_id,
HEAD:backend/ee/onyx/hooks/executor.py:56:from onyx.db.engine.sql_engine import get_session_with_current_tenant
HEAD:backend/ee/onyx/hooks/executor.py:73:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/hooks/executor.py:95:    if MULTI_TENANT:
HEAD:backend/ee/onyx/hooks/executor.py:119:            with get_session_with_current_tenant() as log_session:
HEAD:backend/ee/onyx/hooks/executor.py:140:            with get_session_with_current_tenant() as reachable_session:
HEAD:backend/ee/onyx/main.py:27:    add_api_server_tenant_id_middleware,
HEAD:backend/ee/onyx/main.py:62:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/main.py:92:    # AFTER tenant_tracking has populated CURRENT_TENANT_ID_CONTEXTVAR.
HEAD:backend/ee/onyx/main.py:97:    if MULTI_TENANT:
HEAD:backend/ee/onyx/main.py:98:        add_api_server_tenant_id_middleware(application, logger)
HEAD:backend/ee/onyx/main.py:105:    if MULTI_TENANT:
HEAD:backend/ee/onyx/main.py:167:    if MULTI_TENANT:
HEAD:backend/ee/onyx/server/auth_check.py:24:    ("/proxy/license/{tenant_id}", {"GET"}),
HEAD:backend/ee/onyx/server/billing/api.py:9:- Cloud (MULTI_TENANT): Routes directly to control plane
HEAD:backend/ee/onyx/server/billing/api.py:74:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/server/billing/api.py:75:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/ee/onyx/server/billing/api.py:101:    if MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/api.py:119:    if MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/api.py:141:    if MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/api.py:155:    if MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/api.py:161:def _get_tenant_id() -> str | None:
HEAD:backend/ee/onyx/server/billing/api.py:163:    if MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/api.py:164:        return get_current_tenant_id()
HEAD:backend/ee/onyx/server/billing/api.py:177:    For renewals, existing license (self-hosted) or tenant_id (cloud) is used.
HEAD:backend/ee/onyx/server/billing/api.py:184:    tenant_id = _get_tenant_id()
HEAD:backend/ee/onyx/server/billing/api.py:191:        used_seats = get_used_seats(tenant_id)
HEAD:backend/ee/onyx/server/billing/api.py:208:        tenant_id=tenant_id,
HEAD:backend/ee/onyx/server/billing/api.py:229:    tenant_id = _get_tenant_id()
HEAD:backend/ee/onyx/server/billing/api.py:232:    if not MULTI_TENANT and not license_data:
HEAD:backend/ee/onyx/server/billing/api.py:240:        tenant_id=tenant_id,
HEAD:backend/ee/onyx/server/billing/api.py:255:        if MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/api.py:256:            return get_redis_client(tenant_id=get_current_tenant_id())
HEAD:backend/ee/onyx/server/billing/api.py:278:    if MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/api.py:279:        invalidate_indexing_trial_cache(get_current_tenant_id())
HEAD:backend/ee/onyx/server/billing/api.py:298:    tenant_id = _get_tenant_id()
HEAD:backend/ee/onyx/server/billing/api.py:301:    if not MULTI_TENANT and not license_data:
HEAD:backend/ee/onyx/server/billing/api.py:332:            tenant_id=tenant_id,
HEAD:backend/ee/onyx/server/billing/api.py:370:    tenant_id = _get_tenant_id()
HEAD:backend/ee/onyx/server/billing/api.py:373:    if not MULTI_TENANT and not license_data:
HEAD:backend/ee/onyx/server/billing/api.py:377:    used_seats = get_used_seats(tenant_id)
HEAD:backend/ee/onyx/server/billing/api.py:391:        tenant_id=tenant_id,
HEAD:backend/ee/onyx/server/billing/api.py:417:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/api.py:423:    tenant_id = _get_tenant_id()
HEAD:backend/ee/onyx/server/billing/api.py:424:    result = await end_trial_service(tenant_id=tenant_id)
HEAD:backend/ee/onyx/server/billing/api.py:512:    if MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/billing_cache.py:31:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/server/billing/billing_cache.py:35:BILLING_CACHE_KEY = "billing:info:{tenant_id}"
HEAD:backend/ee/onyx/server/billing/billing_cache.py:45:def _cache_key(tenant_id: str) -> str:
HEAD:backend/ee/onyx/server/billing/billing_cache.py:46:    return BILLING_CACHE_KEY.format(tenant_id=tenant_id)
HEAD:backend/ee/onyx/server/billing/billing_cache.py:81:    tenant_id: str,
HEAD:backend/ee/onyx/server/billing/billing_cache.py:92:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/billing_cache.py:94:            "cached_fetch_billing_information is cloud-only; gate callers on MULTI_TENANT"
HEAD:backend/ee/onyx/server/billing/billing_cache.py:98:    key = _cache_key(tenant_id)
HEAD:backend/ee/onyx/server/billing/billing_cache.py:105:            tenant_id,
HEAD:backend/ee/onyx/server/billing/billing_cache.py:108:        return fetch_billing_information(tenant_id)
HEAD:backend/ee/onyx/server/billing/billing_cache.py:121:                tenant_id,
HEAD:backend/ee/onyx/server/billing/billing_cache.py:125:    info = fetch_billing_information(tenant_id)
HEAD:backend/ee/onyx/server/billing/billing_cache.py:130:        logger.warning("billing cache write failed for tenant %s: %s", tenant_id, e)
HEAD:backend/ee/onyx/server/billing/billing_cache.py:135:def cached_is_tenant_on_trial(tenant_id: str) -> bool:
HEAD:backend/ee/onyx/server/billing/billing_cache.py:140:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/billing_cache.py:144:    info = cached_fetch_billing_information(tenant_id)
HEAD:backend/ee/onyx/server/billing/billing_cache.py:152:def invalidate_billing_cache(tenant_id: str) -> bool:
HEAD:backend/ee/onyx/server/billing/billing_cache.py:157:    if not MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/billing_cache.py:161:        get_shared_redis_client().delete(_cache_key(tenant_id))
HEAD:backend/ee/onyx/server/billing/billing_cache.py:165:            "billing cache invalidate failed for tenant %s: %s", tenant_id, e
HEAD:backend/ee/onyx/server/billing/models.py:49:    tenant_id: str
HEAD:backend/ee/onyx/server/billing/service.py:6:- Self-hosted (not MULTI_TENANT): Routes through cloud data plane proxy
HEAD:backend/ee/onyx/server/billing/service.py:9:- Cloud (MULTI_TENANT): Routes directly to control plane
HEAD:backend/ee/onyx/server/billing/service.py:32:from shared_configs.configs import MULTI_TENANT
HEAD:backend/ee/onyx/server/billing/service.py:65:    if MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/service.py:72:    if MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/service.py:147:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/server/billing/service.py:157:        tenant_id: Tenant ID (cloud only, for renewals)
HEAD:backend/ee/onyx/server/billing/service.py:169:    if tenant_id and MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/service.py:170:        body["tenant_id"] = tenant_id
HEAD:backend/ee/onyx/server/billing/service.py:194:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/server/billing/service.py:202:        tenant_id: Tenant ID (cloud only)
HEAD:backend/ee/onyx/server/billing/service.py:212:    if tenant_id and MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/service.py:213:        body["tenant_id"] = tenant_id
HEAD:backend/ee/onyx/server/billing/service.py:229:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/server/billing/service.py:235:        tenant_id: Tenant ID (cloud only)
HEAD:backend/ee/onyx/server/billing/service.py:241:    if tenant_id and MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/service.py:242:        params["tenant_id"] = tenant_id
HEAD:backend/ee/onyx/server/billing/service.py:262:    tenant_id: str | None = None,
HEAD:backend/ee/onyx/server/billing/service.py:269:        tenant_id: Tenant ID (cloud only)
HEAD:backend/ee/onyx/server/billing/service.py:275:    if tenant_id and MULTI_TENANT:
HEAD:backend/ee/onyx/server/billing/service.py:276:        body["tenant_id"] = tenant_id
HEAD:backend/ee/onyx/server/billing/service.py:295:async def end_trial(tenant_id: str | None) -> EndTrialResponse:
```
Tenant identifiers and tenant-context mechanisms are security-critical
because incorrect propagation may create cross-tenant access.
## Tenant-Aware Database / Session Evidence
Evidence lines: 137
```text
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:8:from onyx.db.engine.sql_engine import get_session_with_tenant
HEAD:backend/ee/onyx/background/celery/tasks/cleanup/tasks.py:22:    with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:17:from onyx.db.engine.tenant_utils import get_all_tenant_ids
HEAD:backend/ee/onyx/background/celery/tasks/cloud/tasks.py:154:        tenant_ids = get_all_tenant_ids()
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:59:    get_session_with_tenant,
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:295:                        tenant_id, key_bytes, r, db_session
HEAD:backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py:729:        with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:129:    tenants are always current so that signup doesn't hit schema mismatches
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:132:    from ee.onyx.server.tenants.schema_management import (
HEAD:backend/ee/onyx/background/celery/tasks/tenant_provisioning/tasks.py:183:    from ee.onyx.server.tenants.schema_management import (
HEAD:backend/ee/onyx/background/celery/tasks/vespa/tasks.py:20:    tenant_id: str, key_bytes: bytes, r: TenantRedisClient, db_session: Session
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:23:from onyx.db.engine.sql_engine import get_catalog_session, get_session_with_tenant
HEAD:backend/ee/onyx/db/tenant_sso_domain.py:204:    with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:23:    get_session_with_tenant,
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:30:from shared_configs.configs import MULTI_TENANT, POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:53:        return POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:109:        return POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:191:        return POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:897:    with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:51:from shared_configs.configs import MULTI_TENANT, POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:230:        if not tenant_id or tenant_id == POSTGRES_DEFAULT_SCHEMA:
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:328:        if not tenant_id or tenant_id == POSTGRES_DEFAULT_SCHEMA:
HEAD:backend/ee/onyx/server/metrics/license_metrics.py:18:from onyx.db.engine.sql_engine import get_session_with_tenant
HEAD:backend/ee/onyx/server/metrics/license_metrics.py:22:from shared_configs.configs import MULTI_TENANT, POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/server/metrics/license_metrics.py:34:        with get_session_with_tenant(tenant_id=POSTGRES_DEFAULT_SCHEMA) as db_session:
HEAD:backend/ee/onyx/server/metrics/license_metrics.py:36:                db_session, tenant_id=POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/server/metrics/license_metrics.py:40:            used_seats = get_used_seats(POSTGRES_DEFAULT_SCHEMA)
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:23:from shared_configs.configs import MULTI_TENANT, POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:50:                CURRENT_TENANT_ID_CONTEXTVAR.set(POSTGRES_DEFAULT_SCHEMA)
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:56:                tenant_id = POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:72:                and tenant_id != POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:141:                "tenant_id", POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:150:            if tenant_id and not is_valid_schema_name(tenant_id):
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:161:                    "tenant_id", POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:164:                if not tenant_id or not is_valid_schema_name(tenant_id):
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:176:            "Token data not found or expired in Redis, defaulting to POSTGRES_DEFAULT_SCHEMA"
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:179:        # Return POSTGRES_DEFAULT_SCHEMA, so non-authenticated requests are sent to the default schema
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:180:        # The CURRENT_TENANT_ID_CONTEXTVAR is initialized with POSTGRES_DEFAULT_SCHEMA,
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:182:        return POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:192:            return tenant_id or POSTGRES_DEFAULT_SCHEMA  # noqa: B012
HEAD:backend/ee/onyx/server/tenants/admin_api.py:9:from onyx.db.engine.sql_engine import get_session_with_tenant
HEAD:backend/ee/onyx/server/tenants/admin_api.py:66:    with get_session_with_tenant(tenant_id=tenant_id) as tenant_session:
HEAD:backend/ee/onyx/server/tenants/anonymous_user_path.py:7:def get_anonymous_user_path(tenant_id: str, db_session: Session) -> str | None:
HEAD:backend/ee/onyx/server/tenants/anonymous_user_path.py:21:    tenant_id: str, anonymous_user_path: str, db_session: Session
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:38:        current_path = get_anonymous_user_path(tenant_id, db_session)
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:56:            modify_anonymous_user_path(tenant_id, anonymous_user_path, db_session)
HEAD:backend/ee/onyx/server/tenants/provisioning.py:23:from ee.onyx.server.tenants.schema_management import (
HEAD:backend/ee/onyx/server/tenants/provisioning.py:42:    get_session_with_tenant,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:81:    POSTGRES_DEFAULT_SCHEMA,
HEAD:backend/ee/onyx/server/tenants/provisioning.py:110:        return POSTGRES_DEFAULT_SCHEMA
HEAD:backend/ee/onyx/server/tenants/provisioning.py:124:            # Run migrations to ensure the pre-provisioned tenant schema is current.
HEAD:backend/ee/onyx/server/tenants/provisioning.py:274:    # 1. Try to drop the tenant's schema
HEAD:backend/ee/onyx/server/tenants/provisioning.py:345:            "Keeping shard mapping for tenant %s: its schema was not dropped, and the "
HEAD:backend/ee/onyx/server/tenants/provisioning.py:747:        with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/ee/onyx/server/tenants/schema_management.py:23:    """Alembic URL for the database holding this tenant's schema.
HEAD:backend/ee/onyx/server/tenants/schema_management.py:51:            _tenant_connection_string(schema_name)
HEAD:backend/ee/onyx/server/tenants/schema_management.py:82:    with Session(get_engine_for_tenant(tenant_id)) as db_session:
HEAD:backend/ee/onyx/server/tenants/schema_management.py:99:    """Drop a tenant's schema.
HEAD:backend/ee/onyx/server/tenants/schema_management.py:120:    # Set the search path to the tenant's schema
HEAD:backend/onyx/auth/login_claims_capture.py:83:    unauthenticated, so the tenant contextvar still holds the default schema
HEAD:backend/onyx/auth/sso_tenant_token.py:48:    if not isinstance(tenant_id, str) or not is_valid_schema_name(tenant_id):
HEAD:backend/onyx/auth/users.py:134:    get_session_with_tenant,
HEAD:backend/onyx/auth/users.py:172:    POSTGRES_DEFAULT_SCHEMA,
HEAD:backend/onyx/auth/users.py:391:    with get_session_with_tenant(tenant_id=tenant_id) as db_session:
HEAD:backend/onyx/auth/users.py:600:            async with get_async_session_context_manager(tenant_id) as db_session:
HEAD:backend/onyx/auth/users.py:613:        async with get_async_session_context_manager(tenant_id) as db_session:
HEAD:backend/onyx/auth/users.py:634:        # tenant middleware fell back to the default schema. Re-resolve the
HEAD:backend/onyx/auth/users.py:663:            async with get_async_session_context_manager(tenant_id) as db_session:
HEAD:backend/onyx/auth/users.py:780:            async with get_async_session_context_manager(tenant_id) as db_session:
HEAD:backend/onyx/auth/users.py:1039:        async with self._tenant_session_with_bound_user_db(tenant_id) as db_session:
HEAD:backend/onyx/auth/users.py:1337:            # otherwise get_session_with_current_tenant() targets the wrong schema.
HEAD:backend/onyx/auth/users.py:1491:        # default schema. On multi-tenant that schema owns neither the user rows
HEAD:backend/onyx/auth/users.py:1497:            POSTGRES_DEFAULT_SCHEMA,
HEAD:backend/onyx/auth/users.py:1547:                POSTGRES_DEFAULT_SCHEMA,
HEAD:backend/onyx/auth/users.py:1567:        async with get_async_session_context_manager(tenant_id) as tenant_session:
HEAD:backend/onyx/auth/users.py:2500:        # Single-tenant deployments always run on the default schema.
HEAD:backend/onyx/auth/users.py:2501:        token_tenant_id = POSTGRES_DEFAULT_SCHEMA
HEAD:backend/onyx/db/api_key.py:153:    # Get tenant_id from context var (will be default schema for single tenant)
HEAD:backend/onyx/db/api_key.py:248:    # Get tenant_id from context var (will be default schema for single tenant)
HEAD:backend/onyx/db/dal.py:38:from onyx.db.engine.sql_engine import get_session_with_tenant
HEAD:backend/onyx/db/dal.py:73:        with get_session_with_tenant(tenant_id=tenant_id) as session:
HEAD:backend/onyx/db/engine/async_sql_engine.py:36:from shared_configs.configs import MULTI_TENANT, POSTGRES_DEFAULT_SCHEMA_STANDARD_VALUE
HEAD:backend/onyx/db/engine/async_sql_engine.py:119:    """Async engine for the database holding this tenant's schema.
HEAD:backend/onyx/db/engine/async_sql_engine.py:185:    # Routes to the tenant's shard, not just its schema. With one shard configured
HEAD:backend/onyx/db/engine/async_sql_engine.py:190:    if not MULTI_TENANT and tenant_id == POSTGRES_DEFAULT_SCHEMA_STANDARD_VALUE:
HEAD:backend/onyx/db/engine/async_sql_engine.py:196:    schema_translate_map = {None: tenant_id}
HEAD:backend/onyx/db/engine/async_sql_engine.py:199:            schema_translate_map=schema_translate_map
HEAD:backend/onyx/db/engine/shard_registry.py:3:Onyx addresses a tenant by *schema* via ``schema_translate_map``. This module adds
HEAD:backend/onyx/db/engine/shard_routing.py:1:"""Resolve a tenant to the physical database ("shard") holding its schema.
HEAD:backend/onyx/db/engine/shard_routing.py:207:    """Name of the shard holding this tenant's schema."""
HEAD:backend/onyx/db/engine/shard_routing.py:261:    """Engine for the database holding this tenant's schema.
HEAD:backend/onyx/db/engine/sql_engine.py:46:    POSTGRES_DEFAULT_SCHEMA,
HEAD:backend/onyx/db/engine/sql_engine.py:47:    POSTGRES_DEFAULT_SCHEMA_STANDARD_VALUE,
HEAD:backend/onyx/db/engine/sql_engine.py:445:    with get_session_with_tenant(tenant_id=tenant_id) as session:
HEAD:backend/onyx/db/engine/sql_engine.py:455:        with get_session_with_tenant(tenant_id=tenant_id) as session:
HEAD:backend/onyx/db/engine/sql_engine.py:470:    token = CURRENT_TENANT_ID_CONTEXTVAR.set(POSTGRES_DEFAULT_SCHEMA)
HEAD:backend/onyx/db/engine/sql_engine.py:481:            schema_translate_map={None: POSTGRES_DEFAULT_SCHEMA}
HEAD:backend/onyx/db/engine/sql_engine.py:518:def get_session_with_tenant(*, tenant_id: str) -> Generator[Session, None, None]:
HEAD:backend/onyx/db/engine/sql_engine.py:522:    The tenant selects both the schema (via `schema_translate_map`, below) and the
HEAD:backend/onyx/db/engine/sql_engine.py:532:    if not MULTI_TENANT and tenant_id == POSTGRES_DEFAULT_SCHEMA_STANDARD_VALUE:
HEAD:backend/onyx/db/engine/sql_engine.py:541:    schema_translate_map = {None: tenant_id}
HEAD:backend/onyx/db/engine/sql_engine.py:543:        schema_translate_map=schema_translate_map
HEAD:backend/onyx/db/engine/sql_engine.py:558:    if tenant_id == POSTGRES_DEFAULT_SCHEMA and MULTI_TENANT:
HEAD:backend/onyx/db/engine/sql_engine.py:584:    if not MULTI_TENANT and tenant_id == POSTGRES_DEFAULT_SCHEMA_STANDARD_VALUE:
HEAD:backend/onyx/db/engine/sql_engine.py:589:    schema_translate_map = {None: tenant_id}
HEAD:backend/onyx/db/engine/sql_engine.py:591:        schema_translate_map=schema_translate_map
HEAD:backend/onyx/db/engine/tenant_utils.py:14:    POSTGRES_DEFAULT_SCHEMA,
HEAD:backend/onyx/db/engine/tenant_utils.py:42:    tenant_schemas: list[str], head_rev: str, shard_name: str
HEAD:backend/onyx/db/engine/tenant_utils.py:51:    if not tenant_schemas:
HEAD:backend/onyx/db/engine/tenant_utils.py:61:        # schemas instead of every tenant_% schema in the database.
HEAD:backend/onyx/db/engine/tenant_utils.py:63:        conn.execute(text("DROP TABLE IF EXISTS _tenant_schemas_input"))
HEAD:backend/onyx/db/engine/tenant_utils.py:64:        conn.execute(text("CREATE TEMP TABLE _tenant_schemas_input (schema_name text)"))
HEAD:backend/onyx/db/engine/tenant_utils.py:67:                "INSERT INTO _tenant_schemas_input (schema_name) SELECT unnest(CAST(:schemas AS text[]))"
HEAD:backend/onyx/db/engine/tenant_utils.py:69:            {"schemas": tenant_schemas},
HEAD:backend/onyx/db/engine/tenant_utils.py:85:                    FROM _tenant_schemas_input;
HEAD:backend/onyx/db/engine/tenant_utils.py:88:                        RAISE NOTICE 'No tenant schemas found.';
HEAD:backend/onyx/db/engine/tenant_utils.py:121:        conn.execute(text("DROP TABLE IF EXISTS _tenant_schemas_input"))
HEAD:backend/onyx/db/engine/tenant_utils.py:126:    return [s for s in tenant_schemas if version_by_schema.get(s) != head_rev]
HEAD:backend/onyx/db/engine/tenant_utils.py:129:def _tenant_schemas_on(engine: Engine) -> list[str]:
HEAD:backend/onyx/db/engine/tenant_utils.py:130:    """Tenant schemas physically present in one database."""
HEAD:backend/onyx/db/engine/tenant_utils.py:139:            {"default_schema": POSTGRES_DEFAULT_SCHEMA},
HEAD:backend/onyx/db/engine/tenant_utils.py:144:def count_tenant_schemas_on_shard(shard_name: str) -> int:
HEAD:backend/onyx/db/engine/tenant_utils.py:145:    """How many tenant schemas one shard is holding.
HEAD:backend/onyx/db/engine/tenant_utils.py:151:    return len(_tenant_schemas_on(get_engine_for_shard(shard_name)))
HEAD:backend/onyx/db/engine/tenant_utils.py:155:    """Tenant schemas on each configured shard, keyed by shard name.
HEAD:backend/onyx/db/engine/tenant_utils.py:163:        return {get_default_shard_name(): [POSTGRES_DEFAULT_SCHEMA]}
HEAD:backend/onyx/db/engine/tenant_utils.py:166:        shard_name: _tenant_schemas_on(get_engine_for_shard(shard_name))
HEAD:backend/onyx/db/engine/tenant_utils.py:171:def get_all_tenant_ids() -> list[str]:
HEAD:backend/onyx/db/engine/tenant_utils.py:174:    Returning [POSTGRES_DEFAULT_SCHEMA] means the only tenant is the 'public' or self
HEAD:backend/onyx/db/engine/tenant_utils.py:179:        return [POSTGRES_DEFAULT_SCHEMA]
HEAD:backend/onyx/db/models.py:5660:        considers creating them inside a tenant schema, and
HEAD:backend/onyx/db/models.py:5796:# Maps a tenant to the physical database ("shard") holding its schema.
HEAD:backend/onyx/db/models.py:6185:        # Ensure only one row per window start (tenant_id is in the schema name)
HEAD:backend/onyx/db/pat.py:93:            async with get_async_session_context_manager(tenant_id) as session:
HEAD:backend/onyx/db/security_settings.py:3:One row per tenant schema (boolean PK pinned to ``true``). Every column is
HEAD:backend/onyx/db/tenant_shard.py:3:Schema-qualified raw SQL, matching the read side: `schema_translate_map` only rewrites
HEAD:backend/onyx/db/tenant_shard.py:18:    """Record where a tenant's schema is about to be created.
```
## Object-Level Access Control
Evidence lines: 246
```text
HEAD:backend/ee/onyx/access/access.py:13:    _get_access_for_documents as get_access_for_documents_without_groups,
HEAD:backend/ee/onyx/access/access.py:15:from onyx.access.access import _get_acl_for_user as get_acl_for_user_without_groups
HEAD:backend/ee/onyx/access/access.py:17:from onyx.access.models import DocumentAccess
HEAD:backend/ee/onyx/access/access.py:27:def _get_access_for_document(
HEAD:backend/ee/onyx/access/access.py:30:) -> DocumentAccess:
HEAD:backend/ee/onyx/access/access.py:31:    id_to_access = _get_access_for_documents([document_id], db_session)
HEAD:backend/ee/onyx/access/access.py:33:        return DocumentAccess.build(
HEAD:backend/ee/onyx/access/access.py:44:def _get_access_for_documents(
HEAD:backend/ee/onyx/access/access.py:47:) -> dict[str, DocumentAccess]:
HEAD:backend/ee/onyx/access/access.py:48:    non_ee_access_dict = get_access_for_documents_without_groups(
HEAD:backend/ee/onyx/access/access.py:74:    for document_id, non_ee_access in non_ee_access_dict.items():
HEAD:backend/ee/onyx/access/access.py:112:        access_map[document_id] = DocumentAccess.build(
HEAD:backend/ee/onyx/access/access.py:134:def get_access_for_user_files_impl(
HEAD:backend/ee/onyx/access/access.py:137:) -> dict[str, DocumentAccess]:
HEAD:backend/ee/onyx/access/access.py:138:    """EE version: extends the MIT user file ACL with user group names
HEAD:backend/ee/onyx/access/access.py:154:) -> dict[str, DocumentAccess]:
HEAD:backend/ee/onyx/access/access.py:160:    result: dict[str, DocumentAccess] = {}
HEAD:backend/ee/onyx/access/access.py:163:            result[str(user_file.id)] = DocumentAccess.build(
HEAD:backend/ee/onyx/access/access.py:174:        result[str(user_file.id)] = DocumentAccess.build(
HEAD:backend/ee/onyx/access/access.py:184:def _get_acl_for_user(user: User, db_session: Session) -> set[str]:
HEAD:backend/ee/onyx/access/access.py:185:    """Returns a list of ACL entries that the user has access to. This is meant to be
HEAD:backend/ee/onyx/access/access.py:186:    used downstream to filter out documents that the user does not have access to. The
HEAD:backend/ee/onyx/access/access.py:187:    user should have access to a document if at least one entry in the document's ACL
HEAD:backend/ee/onyx/access/access.py:208:    user_acl = set(prefixed_user_groups + prefixed_external_groups)
HEAD:backend/ee/onyx/access/access.py:209:    user_acl.update(get_acl_for_user_without_groups(user, db_session))
HEAD:backend/ee/onyx/access/access.py:211:    return user_acl
HEAD:backend/ee/onyx/db/document.py:19:    This sets the permissions for a document in postgres.
HEAD:backend/ee/onyx/db/document.py:31:        for group_id in external_access.external_user_group_ids
HEAD:backend/ee/onyx/db/document.py:35:        # If the document does not exist, still store the external access
HEAD:backend/ee/onyx/db/document.py:36:        # So that if the document is added later, the external access is already stored
HEAD:backend/ee/onyx/db/document.py:47:    document.external_user_emails = list(external_access.external_user_emails)
HEAD:backend/ee/onyx/db/document.py:49:    document.is_public = external_access.is_public
HEAD:backend/ee/onyx/db/document.py:59:    This sets the permissions for a document in postgres. Returns True if the
HEAD:backend/ee/onyx/db/document.py:72:        for group_id in external_access.external_user_group_ids
HEAD:backend/ee/onyx/db/document.py:76:        # If the document does not exist, still store the external access
HEAD:backend/ee/onyx/db/document.py:77:        # So that if the document is added later, the external access is already stored
HEAD:backend/ee/onyx/db/document.py:90:    # If the document exists, we need to check if the external access has changed
HEAD:backend/ee/onyx/db/document.py:92:        external_access.external_user_emails != set(document.external_user_emails or [])
HEAD:backend/ee/onyx/db/document.py:94:        or external_access.is_public != document.is_public
HEAD:backend/ee/onyx/db/document.py:96:        document.external_user_emails = list(external_access.external_user_emails)
HEAD:backend/ee/onyx/db/document.py:98:        document.is_public = external_access.is_public
HEAD:backend/ee/onyx/db/external_perm.py:145:        if external_group.gives_anyone_access:
HEAD:backend/ee/onyx/db/hierarchy.py:25:    """Grant the connector-level access applied to indexed documents."""
HEAD:backend/ee/onyx/db/hierarchy.py:53:    """Grant access through the node ACL or an associated connector."""
HEAD:backend/ee/onyx/db/hierarchy.py:71:def _get_accessible_hierarchy_nodes_for_source(
HEAD:backend/ee/onyx/db/hierarchy.py:99:    """EE version: ACL-filtered case-insensitive display_name search."""
HEAD:backend/ee/onyx/db/persona.py:103:    # No group either side: a personal agent, nothing to authorize. Keeps groups=[]
HEAD:backend/ee/onyx/db/persona.py:200:    # When sharing changes, user file ACLs need to be updated in the vector DB
HEAD:backend/ee/onyx/db/scim.py:271:        replaced address keeps reaching documents whose indexed ACLs still name
HEAD:backend/ee/onyx/db/user_group.py:423:    Fetches all user groups that have access to the given documents.
HEAD:backend/ee/onyx/db/user_group.py:425:    NOTE: this doesn't include groups if the cc_pair is access type SYNC
HEAD:backend/ee/onyx/db/user_group.py:661:    group_permissions.discard(Permission.BASIC_ACCESS)
HEAD:backend/ee/onyx/db/user_group.py:720:    out-of-scope connector to the group, granting its members access. Admins /
HEAD:backend/ee/onyx/db/user_tenant_mapping.py:665:    # exact match would leave a stale entry behind to authorize a later move.
HEAD:backend/onyx/access/access.py:9:from onyx.access.models import DocumentAccess
HEAD:backend/onyx/access/access.py:12:from onyx.db.document import get_access_info_for_document, get_access_info_for_documents
HEAD:backend/onyx/access/access.py:34:def _get_access_for_document(
HEAD:backend/onyx/access/access.py:37:) -> DocumentAccess:
HEAD:backend/onyx/access/access.py:38:    info = get_access_info_for_document(
HEAD:backend/onyx/access/access.py:43:    doc_access = DocumentAccess.build(
HEAD:backend/onyx/access/access.py:54:def get_access_for_document(
HEAD:backend/onyx/access/access.py:57:) -> DocumentAccess:
HEAD:backend/onyx/access/access.py:58:    versioned_get_access_for_document_fn = fetch_versioned_implementation(
HEAD:backend/onyx/access/access.py:59:        "onyx.access.access", "_get_access_for_document"
HEAD:backend/onyx/access/access.py:61:    return versioned_get_access_for_document_fn(document_id, db_session)
HEAD:backend/onyx/access/access.py:64:def get_null_document_access() -> DocumentAccess:
HEAD:backend/onyx/access/access.py:65:    return DocumentAccess.build(
HEAD:backend/onyx/access/access.py:74:def _get_access_for_documents(
HEAD:backend/onyx/access/access.py:77:) -> dict[str, DocumentAccess]:
HEAD:backend/onyx/access/access.py:78:    document_access_info = get_access_info_for_documents(
HEAD:backend/onyx/access/access.py:83:    for document_id, user_emails, is_public in document_access_info:
HEAD:backend/onyx/access/access.py:84:        doc_access[document_id] = DocumentAccess.build(
HEAD:backend/onyx/access/access.py:99:            doc_access[doc_id] = get_null_document_access()
HEAD:backend/onyx/access/access.py:103:def get_access_for_documents(
HEAD:backend/onyx/access/access.py:106:) -> dict[str, DocumentAccess]:
HEAD:backend/onyx/access/access.py:107:    """Fetches all access information for the given documents."""
HEAD:backend/onyx/access/access.py:108:    versioned_get_access_for_documents_fn = fetch_versioned_implementation(
HEAD:backend/onyx/access/access.py:109:        "onyx.access.access", "_get_access_for_documents"
HEAD:backend/onyx/access/access.py:111:    return versioned_get_access_for_documents_fn(document_ids, db_session)
HEAD:backend/onyx/access/access.py:114:def _get_acl_for_user(
HEAD:backend/onyx/access/access.py:118:    """Returns a list of ACL entries that the user has access to. This is meant to be
HEAD:backend/onyx/access/access.py:119:    used downstream to filter out documents that the user does not have access to. The
HEAD:backend/onyx/access/access.py:120:    user should have access to a document if at least one entry in the document's ACL
HEAD:backend/onyx/access/access.py:123:    Anonymous users only have access to public documents.
HEAD:backend/onyx/access/access.py:125:    Addresses the user was renamed away from match too. Indexed ACLs keep
HEAD:backend/onyx/access/access.py:138:def get_acl_for_user(user: User, db_session: Session | None = None) -> set[str]:
HEAD:backend/onyx/access/access.py:139:    versioned_acl_for_user_fn = fetch_versioned_implementation(
HEAD:backend/onyx/access/access.py:140:        "onyx.access.access", "_get_acl_for_user"
HEAD:backend/onyx/access/access.py:142:    return versioned_acl_for_user_fn(user, db_session)
HEAD:backend/onyx/access/access.py:145:def source_should_fetch_permissions_during_indexing(source: DocumentSource) -> bool:
HEAD:backend/onyx/access/access.py:157:def get_access_for_user_files(
HEAD:backend/onyx/access/access.py:160:) -> dict[str, DocumentAccess]:
HEAD:backend/onyx/access/access.py:162:        "onyx.access.access", "get_access_for_user_files_impl"
HEAD:backend/onyx/access/access.py:167:def get_access_for_user_files_impl(
HEAD:backend/onyx/access/access.py:170:) -> dict[str, DocumentAccess]:
HEAD:backend/onyx/access/access.py:177:) -> dict[str, DocumentAccess]:
HEAD:backend/onyx/access/access.py:189:) -> dict[str, DocumentAccess]:
HEAD:backend/onyx/access/access.py:190:    result: dict[str, DocumentAccess] = {}
HEAD:backend/onyx/access/access.py:193:        result[str(user_file.id)] = DocumentAccess.build(
HEAD:backend/onyx/access/access.py:234:    - `Document` whose ACL grants access (covers connector-ingested files).
HEAD:backend/onyx/access/access.py:317:    """Mirror retrieval-time ACL: grant access if any `Document` referencing
HEAD:backend/onyx/access/access.py:318:    `file_id` has an ACL the user satisfies.
HEAD:backend/onyx/access/access.py:326:       ACL, so any one representative document answers the question.
HEAD:backend/onyx/access/access.py:342:    user_acl = get_acl_for_user(user, db_session)
HEAD:backend/onyx/access/access.py:343:    doc_access = get_access_for_documents(document_ids, db_session)
HEAD:backend/onyx/access/access.py:345:        not user_acl.isdisjoint(access.to_acl()) for access in doc_access.values()
HEAD:backend/onyx/access/access.py:355:    because ACLs are scoped to the cc_pair: the same connector paired with
HEAD:backend/onyx/access/access.py:356:    different credentials can have different ACLs, and a user with access
HEAD:backend/onyx/access/models.py:1:from dataclasses import dataclass
HEAD:backend/onyx/access/models.py:11:@dataclass(frozen=True)
HEAD:backend/onyx/access/models.py:19:    # Names or external IDs of groups with access to the doc
HEAD:backend/onyx/access/models.py:56:        This effectively makes the document in question "private" or inaccessible to anyone else.
HEAD:backend/onyx/access/models.py:58:        This is especially helpful to use when you are performing permission-syncing, and some document's permissions aren't able
HEAD:backend/onyx/access/models.py:69:@dataclass(frozen=True)
HEAD:backend/onyx/access/models.py:72:    This is just a class to wrap the external access and the document ID
HEAD:backend/onyx/access/models.py:109:@dataclass(frozen=True)
HEAD:backend/onyx/access/models.py:159:@dataclass(frozen=True, init=False)
HEAD:backend/onyx/access/models.py:160:class DocumentAccess(ExternalAccess):
HEAD:backend/onyx/access/models.py:173:            "Use `DocumentAccess.build(...)` instead of creating an instance directly."
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
HEAD:backend/onyx/access/models.py:209:    ) -> "DocumentAccess":
HEAD:backend/onyx/access/models.py:210:        """Don't prefix incoming data wth acl type, prefix on read from to_acl!"""
HEAD:backend/onyx/access/models.py:232:default_public_access = DocumentAccess.build(
HEAD:backend/onyx/db/auth.py:112:async def get_access_token_db(
HEAD:backend/onyx/db/connector_credential_pair.py:54:    """Grant public, credential-owner, or current user-group connector access."""
HEAD:backend/onyx/db/connector_credential_pair.py:485:    # guard: issubset is vacuously true for an empty set, which would authorize anything
HEAD:backend/onyx/db/document.py:32:from onyx.db.document_access import apply_document_access_filter
HEAD:backend/onyx/db/document.py:563:def get_accessible_documents_for_hierarchy_node_paginated(
HEAD:backend/onyx/db/document.py:584:    stmt = apply_document_access_filter(
HEAD:backend/onyx/db/document.py:761:def get_access_info_for_document(
HEAD:backend/onyx/db/document.py:765:    """Gets access info for a single document by calling the get_access_info_for_documents function
HEAD:backend/onyx/db/document.py:769:        document_id (str): The document ID to fetch access info for.
HEAD:backend/onyx/db/document.py:774:    results = get_access_info_for_documents(db_session, [document_id])
HEAD:backend/onyx/db/document.py:781:def get_access_info_for_documents(
HEAD:backend/onyx/db/document.py:785:    """Gets back all relevant access info for the given documents. This includes
HEAD:backend/onyx/db/document.py:850:    includes_permissions = any(doc.external_access for doc in seen_documents.values())
HEAD:backend/onyx/db/document_access.py:19:def apply_document_access_filter(
HEAD:backend/onyx/db/document_access.py:25:    """Filter documents by source ACL or associated connector access."""
HEAD:backend/onyx/db/document_access.py:48:        access_filters.append(any_(Document.external_user_emails) == user_email)
HEAD:backend/onyx/db/document_access.py:61:def get_accessible_documents_by_ids(
HEAD:backend/onyx/db/document_access.py:68:    """Return requested documents allowed by the retrieval-time access policy."""
HEAD:backend/onyx/db/document_access.py:73:    stmt = apply_document_access_filter(
HEAD:backend/onyx/db/document_set.py:44:    if has_global_permission(user, Permission.MANAGE_DOCUMENT_SETS):
HEAD:backend/onyx/db/document_set.py:74:    if has_global_permission(user, Permission.READ_DOCUMENT_SETS):
HEAD:backend/onyx/db/document_set.py:83:    accessible_via_group = select(DocumentSet__UserGroup.document_set_id).where(
HEAD:backend/onyx/db/document_set.py:89:            DocumentSetDBModel.id.in_(accessible_via_group),
HEAD:backend/onyx/db/document_set.py:223:def filter_document_set_names_by_user_access(
HEAD:backend/onyx/db/document_set.py:228:    """Return the subset of ``document_set_names`` the user has view access to.
HEAD:backend/onyx/db/document_set.py:241:def filter_document_set_ids_by_user_access(
HEAD:backend/onyx/db/document_set.py:246:    """Return the subset of ``document_set_ids`` the user has view access to."""
HEAD:backend/onyx/db/engine/shard_registry.py:24:from dataclasses import dataclass
HEAD:backend/onyx/db/engine/shard_registry.py:59:@dataclass(frozen=True, repr=False)
HEAD:backend/onyx/db/engine/shard_registry.py:64:    dataclass-generated repr would have included it.
HEAD:backend/onyx/db/engine/sql_engine.py:7:from dataclasses import dataclass
HEAD:backend/onyx/db/engine/sql_engine.py:201:@dataclass(frozen=True)
HEAD:backend/onyx/db/enums.py:495:    authorize URL, token URL, scope, and response parser in
HEAD:backend/onyx/db/enums.py:642:    Permission tokens for group-based authorization and PAT scoping.
HEAD:backend/onyx/db/enums.py:649:    granted directly to a group) and exist primarily to scope Personal Access
HEAD:backend/onyx/db/enums.py:703:        Permission.READ_DOCUMENT_SETS,
HEAD:backend/onyx/db/enums.py:721:    manager — only within managed groups. NONE: not authorized. A scoped grant
HEAD:backend/onyx/db/external_app.py:3:from dataclasses import dataclass
HEAD:backend/onyx/db/external_app.py:42:@dataclass(frozen=True)
HEAD:backend/onyx/db/external_app.py:718:    a fresh authorize couldn't determine it — both overwrite the stored value
HEAD:backend/onyx/db/hierarchy.py:540:def _get_accessible_hierarchy_nodes_for_source(
HEAD:backend/onyx/db/hierarchy.py:556:def get_accessible_hierarchy_nodes_for_source(
HEAD:backend/onyx/db/hierarchy.py:565:    EE combines node ACLs with associated connector permissions; MIT returns all.
HEAD:backend/onyx/db/hierarchy.py:568:        "onyx.db.hierarchy", "_get_accessible_hierarchy_nodes_for_source"
HEAD:backend/onyx/db/hierarchy.py:592:    """MIT version: case-insensitive display_name search without ACL filtering."""
HEAD:backend/onyx/db/hierarchy.py:619:    """Search hierarchy nodes by display_name substring, ACL-gated.
HEAD:backend/onyx/db/hierarchy.py:763:        external_user_group_ids: List of group IDs with access
HEAD:backend/onyx/db/input_prompt.py:74:    if not validate_user_prompt_authorization(user, input_prompt):
HEAD:backend/onyx/db/input_prompt.py:93:def validate_user_prompt_authorization(user: User, input_prompt: InputPrompt) -> bool:
HEAD:backend/onyx/db/input_prompt.py:138:    if not validate_user_prompt_authorization(user, input_prompt):
HEAD:backend/onyx/db/kg_temp_view.py:87:#     user_group_accessible_docs AS (
HEAD:backend/onyx/db/kg_temp_view.py:125:#         SELECT allowed_doc_id FROM user_group_accessible_docs
HEAD:backend/onyx/db/llm.py:133:    - is_public controls USER access (group bypass): when True, all users can access
HEAD:backend/onyx/db/mcp.py:85:    """Servers already on a persona's tools. No attach ACL — chat users of the
HEAD:backend/onyx/db/mcp.py:162:    session: public / group / direct / owner, plus admins (who bypass the access
HEAD:backend/onyx/db/mcp.py:183:    # Admins see every craft-enabled server (ACL bypass), so any change to a
HEAD:backend/onyx/db/mcp.py:203:    """MIT no-op stub. The EE override reconciles the user/group access rows.
HEAD:backend/onyx/db/mcp.py:222:    oauth_authorization_endpoint: str | None = None,
HEAD:backend/onyx/db/mcp.py:239:        oauth_authorization_endpoint=oauth_authorization_endpoint,
HEAD:backend/onyx/db/mcp.py:261:    oauth_authorization_endpoint: str | None | UnsetType = UNSET,
HEAD:backend/onyx/db/mcp.py:290:    if not isinstance(oauth_authorization_endpoint, UnsetType):
HEAD:backend/onyx/db/mcp.py:291:        server.oauth_authorization_endpoint = oauth_authorization_endpoint
HEAD:backend/onyx/db/models.py:355:    # Addresses this user was renamed away from. They still match indexed ACLs
HEAD:backend/onyx/db/models.py:929:    # (e.g. via owning the credential or being a part of a group that is given access)
HEAD:backend/onyx/db/models.py:1018:    permission model as Documents (external_user_emails, external_user_group_ids,
HEAD:backend/onyx/db/models.py:1052:    # ============= PERMISSION FIELDS (same pattern as Document) =============
HEAD:backend/onyx/db/models.py:1057:    # External group IDs with access (prefixed by source type)
HEAD:backend/onyx/db/models.py:1626:    acl: Mapped[list[str]] = mapped_column(
HEAD:backend/onyx/db/models.py:1698:    acl: Mapped[list[str]] = mapped_column(
HEAD:backend/onyx/db/models.py:4042:    # whether to pass through the user's OAuth token as Authorization header
HEAD:backend/onyx/db/models.py:4079:    authorization_url: Mapped[str] = mapped_column(Text, nullable=False)
HEAD:backend/onyx/db/models.py:5383:    attached to the ACL list matching during query time. User level permissions can be handled by
HEAD:backend/onyx/db/models.py:5384:    directly adding the Onyx user to the doc ACL list"""
HEAD:backend/onyx/db/models.py:5600:    # and/or ACL). The reconciler drains it; the swap waits on it. (Document has an ACL-only
HEAD:backend/onyx/db/models.py:5841:    oauth_authorization_endpoint: Mapped[str | None] = mapped_column(
HEAD:backend/onyx/db/models.py:5950:    #   "header_template": {"Authorization": "Bearer {api_key}"}, # shared API-token config
HEAD:backend/onyx/db/models.py:6461:    # time a new provisioning attempt is authorized. Every status write names
HEAD:backend/onyx/db/models.py:6470:    # When the current attempt was authorized; a committed PROVISIONING row
HEAD:backend/onyx/db/models.py:6574:    # The approval that authorized this action, when it went through one.
HEAD:backend/onyx/db/notification.py:156:            f"User {user_id} is not authorized to access notification {notification_id}"
HEAD:backend/onyx/db/oauth_config.py:18:    authorization_url: str,
HEAD:backend/onyx/db/oauth_config.py:29:        authorization_url=authorization_url,
HEAD:backend/onyx/db/oauth_config.py:57:    authorization_url: str | None = None,
HEAD:backend/onyx/db/oauth_config.py:82:    if authorization_url is not None:
HEAD:backend/onyx/db/oauth_config.py:83:        oauth_config.authorization_url = authorization_url
HEAD:backend/onyx/db/permission_sync_attempt.py:215:        docs_with_permission_errors: Number of documents that had permission errors
HEAD:backend/onyx/db/permission_sync_attempt.py:366:    Callers are expected to have already authorized the cc-pair and
HEAD:backend/onyx/db/persona.py:16:from onyx.db.document_access import get_accessible_documents_by_ids
HEAD:backend/onyx/db/persona.py:17:from onyx.db.document_set import filter_document_set_ids_by_user_access
HEAD:backend/onyx/db/persona.py:191:            detail=f"Persona with ID {persona_id} does not exist or user is not authorized to access it",
HEAD:backend/onyx/db/persona.py:372:    # When sharing changes, user file ACLs need to be updated in the vector DB
HEAD:backend/onyx/db/persona.py:392:    # Lock before reading — a content-only edit carries no groups, so update_persona_access
HEAD:backend/onyx/db/persona.py:412:    # Personal (no-group) agent: not a group-scoped resource, so nothing to authorize.
HEAD:backend/onyx/db/persona.py:1527:    so that their ACLs get updated in the vector DB."""
HEAD:backend/onyx/db/persona.py:1679:            accessible_set_ids = filter_document_set_ids_by_user_access(
HEAD:backend/onyx/db/persona.py:1683:                raise ValueError("Cannot attach document sets you don't have access to")
HEAD:backend/onyx/db/persona.py:1747:    # Fetch and attach documents by IDs, filtering for access permissions
HEAD:backend/onyx/db/persona.py:1754:        attached_documents = get_accessible_documents_by_ids(
HEAD:backend/onyx/db/persona.py:1762:            raise ValueError("documents not found or not accessible")
HEAD:backend/onyx/db/pinned_personas.py:44:    authorization, and the two failures are not worth distinguishing to a
HEAD:backend/onyx/db/scoped_permissions.py:4:scope clause. The authorization policy that consumes these (bundle guard + the
HEAD:backend/onyx/db/skill.py:3:Management authorization:
HEAD:backend/onyx/db/skill.py:10:Runtime selection is deliberately separate from authorization. It applies
HEAD:backend/onyx/db/skill.py:25:from dataclasses import dataclass
HEAD:backend/onyx/db/skill.py:83:@dataclass(frozen=True)
HEAD:backend/onyx/db/skill.py:90:@dataclass(frozen=True)
HEAD:backend/onyx/db/sso_provider.py:165:_AUTHORIZE_ROUTER_BY_TYPE: dict[SSOProviderType, str] = {
HEAD:backend/onyx/db/sso_provider.py:172:def sso_authorize_path(provider: SSOProvider) -> str:
HEAD:backend/onyx/db/sso_provider.py:174:    router = _AUTHORIZE_ROUTER_BY_TYPE[provider.provider_type]
HEAD:backend/onyx/db/sso_provider.py:175:    return f"/api/auth/{router}/{provider.name}/authorize"
HEAD:backend/onyx/db/sso_provider.py:221:    never resolve into an authorization flow. The admin API leaves it False to
HEAD:backend/onyx/db/user_file.py:247:    """Flag FUTURE as stale/missing for this file (deferred ACL or missing content).
HEAD:backend/onyx/db/users.py:82:    group membership — Admin-group members carry FULL_ADMIN_PANEL_ACCESS.
HEAD:backend/onyx/db/users.py:562:    documents whose indexed ACLs still name it.
```
Object-level access code is an important separate layer from route-level
permission checks.
A user may be authenticated and authorized for a feature while still being
unauthorized for a specific document, session, connector, agent or resource.
## Search and Document Access Context
Evidence lines: 202
```text
HEAD:backend/ee/onyx/access/access.py:16:from onyx.access.access import collect_user_file_access
HEAD:backend/ee/onyx/access/access.py:21:from onyx.db.user_file import fetch_user_files_with_access_relationships
HEAD:backend/ee/onyx/access/access.py:113:            user_emails=list(non_ee_access.user_emails),
HEAD:backend/ee/onyx/access/access.py:141:    Uses a single DB query (via fetch_user_files_with_access_relationships)
HEAD:backend/ee/onyx/access/access.py:146:    user_files = fetch_user_files_with_access_relationships(
HEAD:backend/ee/onyx/access/access.py:163:            result[str(user_file.id)] = DocumentAccess.build(
HEAD:backend/ee/onyx/access/access.py:172:        emails, is_public = collect_user_file_access(user_file)
HEAD:backend/ee/onyx/access/access.py:174:        result[str(user_file.id)] = DocumentAccess.build(
HEAD:backend/ee/onyx/access/access.py:185:    """Returns a list of ACL entries that the user has access to. This is meant to be
HEAD:backend/ee/onyx/access/access.py:186:    used downstream to filter out documents that the user does not have access to. The
HEAD:backend/ee/onyx/access/access.py:187:    user should have access to a document if at least one entry in the document's ACL
HEAD:backend/ee/onyx/access/access.py:208:    user_acl = set(prefixed_user_groups + prefixed_external_groups)
HEAD:backend/ee/onyx/access/access.py:209:    user_acl.update(get_acl_for_user_without_groups(user, db_session))
HEAD:backend/ee/onyx/access/access.py:211:    return user_acl
HEAD:backend/ee/onyx/server/query_and_chat/query_backend.py:26:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:46:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:76:        tenant_id=get_current_tenant_id(),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:208:        user_id=user.id,
HEAD:backend/ee/onyx/server/query_and_chat/token_limit.py:59:def _user_is_rate_limited(user_id: UUID) -> None:
HEAD:backend/ee/onyx/server/query_and_chat/token_limit.py:75:            user_usage = _fetch_user_usage(user_id, user_cutoff_time, db_session)
HEAD:backend/ee/onyx/server/query_and_chat/token_limit.py:85:                db_session, str(user_id), cost_cutoff
HEAD:backend/ee/onyx/server/query_and_chat/token_limit.py:93:    user_id: UUID, cutoff_time: datetime, db_session: Session
HEAD:backend/ee/onyx/server/query_and_chat/token_limit.py:95:    return get_user_token_buckets_since(db_session, str(user_id), cutoff_time)
HEAD:backend/ee/onyx/server/query_and_chat/token_limit.py:103:def _user_is_rate_limited_by_group(user_id: UUID) -> None:
HEAD:backend/ee/onyx/server/query_and_chat/token_limit.py:105:        group_rate_limits = fetch_user_group_token_rate_limits(db_session, user_id)
HEAD:backend/onyx/document_index/FILTER_SEMANTICS.md:12:| **Tenant** | `tenant_id` | AND (multi-tenant only) |
HEAD:backend/onyx/document_index/FILTER_SEMANTICS.md:164:| `tenant_id` | `tenant_id` | `string` | Tenant isolation (multi-tenant) |
HEAD:backend/onyx/document_index/document_index_utils.py:82:    tenant_id: str,
HEAD:backend/onyx/document_index/document_index_utils.py:97:                        tenant_id=tenant_id,
HEAD:backend/onyx/document_index/document_index_utils.py:128:                            tenant_id=tenant_id,
HEAD:backend/onyx/document_index/document_index_utils.py:140:    tenant_id: str,
HEAD:backend/onyx/document_index/document_index_utils.py:156:        unique_identifier_string += "_" + tenant_id
HEAD:backend/onyx/document_index/document_index_utils.py:190:        tenant_id=chunk.tenant_id,
HEAD:backend/onyx/document_index/factory.py:23:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/onyx/document_index/factory.py:27:    return TenantState(tenant_id=get_current_tenant_id(), multitenant=MULTI_TENANT)
HEAD:backend/onyx/document_index/interfaces_new.py:52:    tenant_id: str
HEAD:backend/onyx/document_index/interfaces_new.py:57:            f"TenantState(tenant_id={self.tenant_id}, multitenant={self.multitenant})"
HEAD:backend/onyx/document_index/interfaces_new.py:61:    def check_tenant_id_is_set_in_multitenant_mode(self) -> Self:
HEAD:backend/onyx/document_index/interfaces_new.py:62:        if self.multitenant and not self.tenant_id:
HEAD:backend/onyx/document_index/interfaces_new.py:185:    # callers want no access filtering they must explicitly supply an empty set.
HEAD:backend/onyx/document_index/opensearch/client.py:929:            tenant_state.tenant_id,
HEAD:backend/onyx/document_index/opensearch/client.py:1029:            tenant_state.tenant_id,
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:11:from onyx.document_index.opensearch.schema import TENANT_ID_FIELD_NAME
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:49:            "query": {"term": {TENANT_ID_FIELD_NAME: {"value": tenant_state.tenant_id}}}
HEAD:backend/onyx/document_index/opensearch/index_reclaim.py:60:            tenant_state.tenant_id,
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:236:        access_control_list=generate_opensearch_filtered_access_control_list(
HEAD:backend/onyx/document_index/opensearch/opensearch_document_index.py:268:        tenant_id=TenantState(tenant_id=chunk.tenant_id, multitenant=MULTI_TENANT),
HEAD:backend/onyx/document_index/opensearch/schema.py:35:from onyx.utils.tenant import get_tenant_id_short_string
HEAD:backend/onyx/document_index/opensearch/schema.py:37:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/onyx/document_index/opensearch/schema.py:61:TENANT_ID_FIELD_NAME = "tenant_id"
HEAD:backend/onyx/document_index/opensearch/schema.py:98:        short_tenant_id: str = get_tenant_id_short_string(tenant_state.tenant_id)
HEAD:backend/onyx/document_index/opensearch/schema.py:102:        opensearch_doc_chunk_id_tenant_prefix = f"{short_tenant_id}__"
HEAD:backend/onyx/document_index/opensearch/schema.py:145:    get_current_tenant_id. Generally relying on global state is bad, in this
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
HEAD:backend/onyx/document_index/opensearch/schema.py:485:                # If a user's access set contains at least one entry from this
HEAD:backend/onyx/document_index/opensearch/schema.py:492:                # Should clobber all other access search filters, namely
HEAD:backend/onyx/document_index/opensearch/schema.py:582:            schema["properties"][TENANT_ID_FIELD_NAME] = {"type": "keyword"}
HEAD:backend/onyx/document_index/opensearch/search.py:39:    TENANT_ID_FIELD_NAME,
HEAD:backend/onyx/document_index/opensearch/search.py:221:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:323:        # Single-tenant indices have no tenant_id field (added only in multitenant mode);
HEAD:backend/onyx/document_index/opensearch/search.py:327:                {"term": {TENANT_ID_FIELD_NAME: {"value": tenant_state.tenant_id}}}
HEAD:backend/onyx/document_index/opensearch/search.py:389:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:486:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:570:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:633:            access_control_list=index_filters.access_control_list,
HEAD:backend/onyx/document_index/opensearch/search.py:1366:                {"term": {TENANT_ID_FIELD_NAME: {"value": tenant_state.tenant_id}}}
HEAD:backend/onyx/document_index/vespa/app_config/schemas/danswer_chunk.sd.jinja:11:        field tenant_id type string {
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:56:    TENANT_ID,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:192:        tenant_id_fieldset_entry = f"{TENANT_ID}"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:193:        if field_set_list and tenant_id_fieldset_entry not in field_set_list:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:194:            field_set_list.append(tenant_id_fieldset_entry)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:210:    # enforcing tenant_id through a == condition
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:212:        if filters.tenant_id:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:213:            selection += f" and {index_name}.tenant_id=='{filters.tenant_id}'"
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:262:                        user_acl_entry in document_acl
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:263:                        for user_acl_entry in filters.access_control_list
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:268:                    if not filters.tenant_id:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:270:                    document_tenant_id = document["fields"].get(TENANT_ID)
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:271:                    if document_tenant_id != filters.tenant_id:
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:277:                            filters.tenant_id,
HEAD:backend/onyx/document_index/vespa/chunk_retrieval.py:336:            selection += f" and {index_name}.tenant_id=='{tenant_state.tenant_id}'"
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:57:    TENANT_ID,
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:229:        if chunk.tenant_id:
HEAD:backend/onyx/document_index/vespa/indexing_utils.py:230:            vespa_document_fields[TENANT_ID] = chunk.tenant_id
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:20:    tenant_id: str,
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:25:        tenant_state=TenantState(tenant_id=tenant_id, multitenant=MULTI_TENANT),
HEAD:backend/onyx/document_index/vespa/kg_interactions.py:31:        kg_update_requests=kg_update_requests, tenant_id=tenant_id
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:16:    TENANT_ID,
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:26:def build_tenant_id_filter(tenant_id: str) -> str:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:27:    return f'({TENANT_ID} contains "{tenant_id}")'
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:187:    # TODO: add error condition if MULTI_TENANT and no tenant_id filter is set
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:188:    if filters.tenant_id and MULTI_TENANT:
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:189:        filter_parts.append(build_tenant_id_filter(filters.tenant_id))
HEAD:backend/onyx/document_index/vespa/shared_utils/vespa_request_builders.py:199:                ACCESS_CONTROL_LIST, filters.access_control_list
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:613:        self._tenant_id = tenant_state.tenant_id
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:743:                tenant_id=self._tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:800:                tenant_id=self._tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:846:                        tenant_id=self._tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1040:            filters=IndexFilters(access_control_list=None, tenant_id=self._tenant_id),
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1070:                tenant_id=self._tenant_id, multitenant=MULTI_TENANT
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1091:                        tenant_id=self._tenant_id,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1112:            f'tenant_id contains "{self._tenant_id}"' if self._multitenant else "true"
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1114:        yql = f"select documentid from {self._index_name} where {where_clause} limit 0"  # noqa: S608 - Vespa YQL with internal index_name/tenant_id
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1184:        tenant_id: str,
HEAD:backend/onyx/document_index/vespa/vespa_document_index.py:1203:                tenant_id=tenant_id,
HEAD:backend/onyx/document_index/vespa_constants.py:46:TENANT_ID = "tenant_id"
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:21:from onyx.access.access import user_can_access_chat_file
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:25:from onyx.auth.users import current_chat_accessible_user
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:155:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:212:    user_id = user.id
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:224:            user_id=user_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:264:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:269:        user_id=user.id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:304:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:309:        user_id=user.id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:339:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:344:        user_id=user.id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:363:    user_id = user.id
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:367:            user_id=user_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:379:                user_id=None,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:395:        elif user_id is not None and existing_chat_session.user_id not in (
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:396:            user_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:406:    if chat_session.user_id is None and user_id is not None:
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:407:        chat_session.user_id = user_id
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:412:        user_id=user_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:504:    user_id = user.id
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:521:                tenant_id=get_current_tenant_id(),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:537:                user_id=str(user_id) if user_id else None,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:553:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:557:    user_id = user.id
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:563:                user_id=user_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:575:            user_id=user_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:612:            user_id=user_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:624:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:627:    user_id = user.id
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:630:        user_id=user_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:638:    chat_session_id: UUID, user_id: UUID, db_session: Session
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:646:        mark_incognito_user_files_deleting(db_session, chat_session_id, user_id)
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:658:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:684:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:687:    user_id = user.id
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:690:            chat_session_id=session_id, user_id=user_id, db_session=db_session
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:705:            user_id, session_id, db_session, hard_delete=actual_hard_delete
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:719:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:733:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:755:        deletable_ids, tenant_id=get_current_tenant_id(), bg_tasks=bg_tasks
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:829:    tenant_id = get_current_tenant_id()
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:831:        tenant_id=tenant_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:832:        distinct_id=tenant_id if user.is_anonymous else str(user.id),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:886:                    tenant_id=tenant_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:954:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:957:    user_id = user.id
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:961:        user_id=user_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:967:        user_id=user_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:975:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:984:            user_id=user.id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1002:    user: User = Depends(current_chat_accessible_user),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1005:    user_id = user.id
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1012:        user_id=user_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1023:    user: User = Depends(current_chat_accessible_user),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1026:    user_id = user.id
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1030:        user_id=user_id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1042:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1072:    user: User = Depends(current_chat_accessible_user),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1085:            user_id=user.id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1125:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1151:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1159:    if not user_can_access_chat_file(file_id, user, db_session):
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1221:        user_id=user.id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1309:                user_id=user.id,
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:1384:            user_id=user.id,
HEAD:backend/onyx/server/query_and_chat/query_backend.py:8:from onyx.context.search.preprocessing.access_filters import (
HEAD:backend/onyx/server/query_and_chat/query_backend.py:9:    build_access_filters_for_user,
HEAD:backend/onyx/server/query_and_chat/query_backend.py:25:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/onyx/server/query_and_chat/query_backend.py:36:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/query_and_chat/query_backend.py:39:    tenant_id = get_current_tenant_id()
HEAD:backend/onyx/server/query_and_chat/query_backend.py:43:    user_acl_filters = build_access_filters_for_user(user, db_session)
HEAD:backend/onyx/server/query_and_chat/query_backend.py:51:        access_control_list=user_acl_filters,
HEAD:backend/onyx/server/query_and_chat/query_backend.py:52:        tenant_id=tenant_id,
HEAD:backend/onyx/server/query_and_chat/token_limit.py:11:from onyx.auth.users import current_chat_accessible_user
HEAD:backend/onyx/server/query_and_chat/token_limit.py:32:from shared_configs.contextvars import get_current_tenant_id
HEAD:backend/onyx/server/query_and_chat/token_limit.py:42:    user: User = Depends(current_chat_accessible_user),
HEAD:backend/onyx/server/query_and_chat/token_limit.py:233:# tenant_id -> whether that tenant has any enabled token rate limit. Keyed by tenant so
HEAD:backend/onyx/server/query_and_chat/token_limit.py:245:    tenant_id = get_current_tenant_id()
HEAD:backend/onyx/server/query_and_chat/token_limit.py:247:        cached = _any_rate_limit_exists_cache.get(tenant_id)
HEAD:backend/onyx/server/query_and_chat/token_limit.py:263:        _any_rate_limit_exists_cache[tenant_id] = exists
HEAD:backend/onyx/server/query_and_chat/token_limit.py:271:        _any_rate_limit_exists_cache.pop(get_current_tenant_id(), None)
```
This surface is especially important for later RAG and tenant-isolation
testing.
## Authentication Router Wiring
Evidence lines: 400
```text
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:5:record we look for, so finding it is that proof. Verifying flips the catalog row
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:18:    list_login_domains,
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:33:_VALUE_PREFIX = "onyx-verify="
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:40:    tenant's published record cannot verify another's claim, and unguessable
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:77:def verify_domain_via_dns(tenant_id: str, domain: str) -> bool:
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:78:    """Resolve the TXT record and verify the domain on a match. Returns whether
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:89:            "Save the provider with this domain before verifying it.",
HEAD:backend/ee/onyx/auth/sso_domain_verification.py:119:    for record in list_login_domains(tenant_id):
HEAD:backend/ee/onyx/main.py:5:from httpx_oauth.clients.google import GoogleOAuth2
HEAD:backend/ee/onyx/main.py:30:from ee.onyx.server.oauth.api import router as ee_oauth_router
HEAD:backend/ee/onyx/main.py:35:from ee.onyx.server.scim.api import register_scim_exception_handlers, scim_router
HEAD:backend/ee/onyx/main.py:43:from onyx.auth.users import auth_backend, create_onyx_oauth_router
HEAD:backend/ee/onyx/main.py:45:    GOOGLE_LOGIN_BASE_SCOPES,
HEAD:backend/ee/onyx/main.py:46:    GOOGLE_OAUTH_SCOPE_OVERRIDE,
HEAD:backend/ee/onyx/main.py:47:    OAUTH_CLIENT_ID,
HEAD:backend/ee/onyx/main.py:48:    OAUTH_CLIENT_SECRET,
HEAD:backend/ee/onyx/main.py:54:    include_auth_router_with_prefix,
HEAD:backend/ee/onyx/main.py:55:    include_router_with_global_prefix_prepended,
HEAD:backend/ee/onyx/main.py:90:    # Register tier_gate FIRST so it becomes the innermost middleware: Starlette
HEAD:backend/ee/onyx/main.py:106:        # For Google OAuth, refresh tokens are requested by:
HEAD:backend/ee/onyx/main.py:108:        # 2. Properly configuring OAuth in Google Cloud Console to allow offline access
HEAD:backend/ee/onyx/main.py:109:        google_login_scopes = list(
HEAD:backend/ee/onyx/main.py:110:            GOOGLE_OAUTH_SCOPE_OVERRIDE or GOOGLE_LOGIN_BASE_SCOPES
HEAD:backend/ee/onyx/main.py:113:        oauth_client = GoogleOAuth2(
HEAD:backend/ee/onyx/main.py:114:            OAUTH_CLIENT_ID,
HEAD:backend/ee/onyx/main.py:115:            OAUTH_CLIENT_SECRET,
HEAD:backend/ee/onyx/main.py:116:            scopes=google_login_scopes,
HEAD:backend/ee/onyx/main.py:118:        include_auth_router_with_prefix(
HEAD:backend/ee/onyx/main.py:120:            create_onyx_oauth_router(
HEAD:backend/ee/onyx/main.py:121:                oauth_client,
HEAD:backend/ee/onyx/main.py:126:                # Points the user back to the login page
HEAD:backend/ee/onyx/main.py:127:                redirect_url=f"{WEB_DOMAIN}/auth/oauth/callback",
HEAD:backend/ee/onyx/main.py:129:            prefix="/auth/oauth",
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
HEAD:backend/ee/onyx/main.py:163:    # Unified billing API - always registered in EE.
HEAD:backend/ee/onyx/main.py:165:    include_router_with_global_prefix_prepended(application, billing_router)
HEAD:backend/ee/onyx/main.py:169:        include_router_with_global_prefix_prepended(application, tenants_router)
HEAD:backend/ee/onyx/main.py:174:    application.include_router(scim_router)
HEAD:backend/ee/onyx/main.py:175:    register_scim_exception_handlers(application)
HEAD:backend/onyx/auth/captcha.py:7:2. Google OAuth signup — the frontend pre-verifies a token, the backend
HEAD:backend/onyx/auth/captcha.py:9:   cookie on the ``/auth/oauth/callback`` redirect.
HEAD:backend/onyx/auth/captcha.py:14:the OAuth cookie.
HEAD:backend/onyx/auth/captcha.py:70:    LOGIN = "login"
HEAD:backend/onyx/auth/captcha.py:71:    OAUTH = "oauth"
HEAD:backend/onyx/auth/captcha.py:221:async def verify_captcha_token(token: str, action: CaptchaAction) -> None:
HEAD:backend/onyx/auth/email_utils.py:318:            s.login(SMTP_USER, SMTP_PASS)
HEAD:backend/onyx/auth/email_utils.py:373:    # Cloud offers Google login alongside password signup.
HEAD:backend/onyx/auth/email_utils.py:377:            "or login with Google and complete your registration.</p>"
HEAD:backend/onyx/auth/email_utils.py:400:        text_content += "You'll be asked to set a password or login with Google to complete your registration."
HEAD:backend/onyx/auth/email_utils.py:496:    link = f"{WEB_DOMAIN}/auth/verify-email?token={token}"
HEAD:backend/onyx/auth/email_utils.py:500:        f"<p>Click the following link to verify your email address:</p><p>{link}</p>"
HEAD:backend/onyx/auth/email_utils.py:504:        "Verify Your Email",
HEAD:backend/onyx/auth/email_utils.py:507:    text_content = f"Click the following link to verify your email address: {link}"
HEAD:backend/onyx/auth/jwt.py:104:    """Return the concrete public key used to verify the provided JWT token."""
HEAD:backend/onyx/auth/jwt.py:170:async def verify_jwt_token(token: str) -> dict[str, Any] | None:
HEAD:backend/onyx/auth/jwt.py:201:            # Enforced only when configured: verify_aud=True with audience=None
HEAD:backend/onyx/auth/jwt.py:209:                options={"verify_aud": settings.jwt_expected_audience is not None},
HEAD:backend/onyx/auth/login_claims_capture.py:1:"""Capture the identity attributes an IdP sends at login and derive a
HEAD:backend/onyx/auth/login_claims_capture.py:2:directory profile from them, independent of login protocol.
HEAD:backend/onyx/auth/login_claims_capture.py:4:Both protocols feed this module: OAuth/OIDC logins contribute id_token and
HEAD:backend/onyx/auth/login_claims_capture.py:6:logins contribute assertion attributes. The login flow itself only consumes
HEAD:backend/onyx/auth/login_claims_capture.py:9:attribute set into Redis at login time and derives a "directory profile"
HEAD:backend/onyx/auth/login_claims_capture.py:23:login flow can never break because of it. Oversized snapshots are dropped, and
HEAD:backend/onyx/auth/login_claims_capture.py:51:# Keeping one field per provider means a login through a second IdP never
HEAD:backend/onyx/auth/login_claims_capture.py:53:_IDP_CLAIMS_KEY_PREFIX = "idp_login_claims"
HEAD:backend/onyx/auth/login_claims_capture.py:58:# Hard ceiling on the whole best-effort capture. It runs inline in the login
HEAD:backend/onyx/auth/login_claims_capture.py:60:# hold the login open indefinitely. Capture is refreshed on every login, so
HEAD:backend/onyx/auth/login_claims_capture.py:82:    """Tenant to key the snapshot under. The login callbacks that run capture are
HEAD:backend/onyx/auth/login_claims_capture.py:87:    and the next login picks it up. The mapping is a sync DB call, so it runs in
HEAD:backend/onyx/auth/login_claims_capture.py:122:    outage at re-login cannot degrade a profile that was already captured.
HEAD:backend/onyx/auth/login_claims_capture.py:153:    provider = str(snapshot.get("oauth_name") or "unknown")
HEAD:backend/onyx/auth/login_claims_capture.py:183:    # TTL is per key, so any login through any provider keeps the whole hash
HEAD:backend/onyx/auth/login_claims_capture.py:205:    """Parse hash values into snapshots, most recent login first. Corrupt or
HEAD:backend/onyx/auth/login_claims_capture.py:226:        options={"verify_signature": False, "verify_aud": False, "verify_exp": False},
HEAD:backend/onyx/auth/login_claims_capture.py:240:                "OAuth claims capture: userinfo endpoint returned %s",
HEAD:backend/onyx/auth/login_claims_capture.py:261:                "OAuth claims capture: Graph /me returned %s", response.status_code
HEAD:backend/onyx/auth/login_claims_capture.py:277:async def capture_oauth_login_claims(
HEAD:backend/onyx/auth/login_claims_capture.py:278:    oauth_client: Any,
HEAD:backend/onyx/auth/login_claims_capture.py:284:    """Snapshot the claims the IdP sent for this login into Redis.
HEAD:backend/onyx/auth/login_claims_capture.py:286:    ``oauth_client`` is the httpx_oauth client used for the login (its
HEAD:backend/onyx/auth/login_claims_capture.py:289:    Never raises, and never holds the login open past
HEAD:backend/onyx/auth/login_claims_capture.py:296:            _capture_oauth_login_claims(
HEAD:backend/onyx/auth/login_claims_capture.py:297:                oauth_client, email, token, tenant_id=tenant_id
HEAD:backend/onyx/auth/login_claims_capture.py:303:            "OAuth claims capture timed out for %s (login unaffected)", email
HEAD:backend/onyx/auth/login_claims_capture.py:307:async def _capture_oauth_login_claims(
HEAD:backend/onyx/auth/login_claims_capture.py:308:    oauth_client: Any,
HEAD:backend/onyx/auth/login_claims_capture.py:321:                logger.warning("OAuth claims capture: id_token decode failed: %s", e)
HEAD:backend/onyx/auth/login_claims_capture.py:325:            oauth_client, "openid_configuration", None
HEAD:backend/onyx/auth/login_claims_capture.py:337:                logger.warning("OAuth claims capture: userinfo fetch failed: %s", e)
HEAD:backend/onyx/auth/login_claims_capture.py:350:                logger.warning("OAuth claims capture: Graph fetch failed: %s", e)
HEAD:backend/onyx/auth/login_claims_capture.py:354:            "oauth_name": getattr(  # ods: ignore[getattr]
HEAD:backend/onyx/auth/login_claims_capture.py:355:                oauth_client, "name", "unknown"
HEAD:backend/onyx/auth/login_claims_capture.py:376:            "OAuth claims capture failed for %s (login unaffected)",
HEAD:backend/onyx/auth/login_claims_capture.py:382:async def capture_saml_login_claims(
HEAD:backend/onyx/auth/login_claims_capture.py:387:    """Snapshot the directory attributes a SAML IdP asserted at login.
HEAD:backend/onyx/auth/login_claims_capture.py:393:    login open past _IDP_CLAIMS_CAPTURE_TIMEOUT_SECONDS.
HEAD:backend/onyx/auth/login_claims_capture.py:399:            _capture_saml_login_claims(email, saml_attributes, provider_name),
HEAD:backend/onyx/auth/login_claims_capture.py:403:        logger.warning("SAML claims capture timed out for %s (login unaffected)", email)
HEAD:backend/onyx/auth/login_claims_capture.py:406:async def _capture_saml_login_claims(
HEAD:backend/onyx/auth/login_claims_capture.py:412:        # OneLogin returns each attribute as a list. Keep the first string value
HEAD:backend/onyx/auth/login_claims_capture.py:421:            "oauth_name": provider_name,
HEAD:backend/onyx/auth/login_claims_capture.py:433:            "SAML claims capture failed for %s (login unaffected)",
HEAD:backend/onyx/auth/login_claims_capture.py:479:    is lowest by convention. A snapshot is written whole per login, so today a
HEAD:backend/onyx/auth/login_claims_capture.py:489:    most recent login first, then older providers' sources as gap fillers.
HEAD:backend/onyx/auth/login_claims_capture.py:585:    captured IdP login snapshots, as ordered ``{label: value}`` pairs for the auto
HEAD:backend/onyx/auth/login_claims_capture.py:598:async def get_captured_oauth_claims(email: str) -> dict[str, Any] | None:
HEAD:backend/onyx/auth/mobile_sso/__init__.py:3:Backend support for native-mobile (Expo / React Native) OAuth/SSO login. The
HEAD:backend/onyx/auth/mobile_sso/__init__.py:4:app runs the OAuth dance in the system browser (reusing the existing, already
HEAD:backend/onyx/auth/mobile_sso/__init__.py:5:registered IdP callback) and the backend returns a single-use, PKCE-bound
HEAD:backend/onyx/auth/mobile_sso/sso_completion.py:3:Every OAuth/SSO provider callback (Google today; OIDC / SAML / Apple later)
HEAD:backend/onyx/auth/mobile_sso/sso_completion.py:9:The mobile params travel inside the signed OAuth state token (see
HEAD:backend/onyx/auth/mobile_sso/sso_completion.py:31:# Keys carried (tamper-proof) inside the signed OAuth state token. Private to
HEAD:backend/onyx/auth/mobile_sso/sso_completion.py:46:    """Fold guarded mobile-SSO params into the (about-to-be-signed) OAuth state.
HEAD:backend/onyx/auth/mobile_sso/sso_completion.py:100:    """Finish an SSO login for a mobile client: mint -> store-under-code -> 302.
HEAD:backend/onyx/auth/mobile_sso/sso_completion.py:105:    does NOT call ``backend.login``, so no web auth cookie is ever set.
HEAD:backend/onyx/auth/oauth_refresher.py:16:    OAUTH_CLIENT_ID,
HEAD:backend/onyx/auth/oauth_refresher.py:17:    OAUTH_CLIENT_SECRET,
HEAD:backend/onyx/auth/oauth_refresher.py:22:from onyx.db.models import OAuthAccount, User
HEAD:backend/onyx/auth/oauth_refresher.py:29:GOOGLE_TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
HEAD:backend/onyx/auth/oauth_refresher.py:31:# Legacy env-credential refresh endpoints, keyed by oauth_account.oauth_name.
HEAD:backend/onyx/auth/oauth_refresher.py:78:# `check_and_refresh_oauth_tokens` so the second coroutine skips the redundant
HEAD:backend/onyx/auth/oauth_refresher.py:138:    login path applies.
HEAD:backend/onyx/auth/oauth_refresher.py:198:    db_session: AsyncSession, oauth_name: str
HEAD:backend/onyx/auth/oauth_refresher.py:201:    oauth_name wins, rowless accounts fall back to the legacy env config."""
HEAD:backend/onyx/auth/oauth_refresher.py:203:        provider = await fetch_sso_provider_by_name_async(db_session, oauth_name)
HEAD:backend/onyx/auth/oauth_refresher.py:209:            "SSO provider lookup failed for %s; skipping token refresh", oauth_name
HEAD:backend/onyx/auth/oauth_refresher.py:228:                oauth_name,
HEAD:backend/onyx/auth/oauth_refresher.py:235:            if provider.provider_type is SSOProviderType.GOOGLE_OAUTH
HEAD:backend/onyx/auth/oauth_refresher.py:243:            oauth_name,
HEAD:backend/onyx/auth/oauth_refresher.py:250:    endpoint = await _resolve_token_endpoint(oauth_name)
HEAD:backend/onyx/auth/oauth_refresher.py:252:        logger.warning("Refresh endpoint not configured for provider: %s", oauth_name)
HEAD:backend/onyx/auth/oauth_refresher.py:254:    if not OAUTH_CLIENT_ID or not OAUTH_CLIENT_SECRET:
HEAD:backend/onyx/auth/oauth_refresher.py:256:            "No OAuth credentials configured to refresh provider: %s", oauth_name
HEAD:backend/onyx/auth/oauth_refresher.py:259:    return _RefreshContext(endpoint, OAUTH_CLIENT_ID, OAUTH_CLIENT_SECRET)
HEAD:backend/onyx/auth/oauth_refresher.py:264:async def _test_expire_oauth_token(
HEAD:backend/onyx/auth/oauth_refresher.py:266:    oauth_account: OAuthAccount,
HEAD:backend/onyx/auth/oauth_refresher.py:272:    Utility function for testing - Sets an OAuth token to expire in a short time
HEAD:backend/onyx/auth/oauth_refresher.py:283:        await user_manager.user_db.update_oauth_account(  # ty: ignore[invalid-argument-type]
HEAD:backend/onyx/auth/oauth_refresher.py:285:            cast(Any, oauth_account),
HEAD:backend/onyx/auth/oauth_refresher.py:295:async def refresh_oauth_token(
HEAD:backend/onyx/auth/oauth_refresher.py:297:    oauth_account: OAuthAccount,
HEAD:backend/onyx/auth/oauth_refresher.py:302:    Attempt to refresh an OAuth token that's about to expire or has expired.
HEAD:backend/onyx/auth/oauth_refresher.py:305:    if not oauth_account.refresh_token:
HEAD:backend/onyx/auth/oauth_refresher.py:309:            oauth_account.oauth_name,
HEAD:backend/onyx/auth/oauth_refresher.py:313:    provider = oauth_account.oauth_name
HEAD:backend/onyx/auth/oauth_refresher.py:319:        logger.info("Refreshing OAuth token for %s's %s account", user.email, provider)
HEAD:backend/onyx/auth/oauth_refresher.py:327:                    "refresh_token": oauth_account.refresh_token,
HEAD:backend/onyx/auth/oauth_refresher.py:335:                    "Failed to refresh OAuth token: Status %s", response.status_code
HEAD:backend/onyx/auth/oauth_refresher.py:343:                "refresh_token", oauth_account.refresh_token
HEAD:backend/onyx/auth/oauth_refresher.py:354:            # Update the OAuth account
HEAD:backend/onyx/auth/oauth_refresher.py:372:            # Update the OAuth account
HEAD:backend/onyx/auth/oauth_refresher.py:373:            await user_manager.user_db.update_oauth_account(  # ty: ignore[invalid-argument-type]
HEAD:backend/onyx/auth/oauth_refresher.py:375:                cast(Any, oauth_account),
HEAD:backend/onyx/auth/oauth_refresher.py:379:            logger.info("Successfully refreshed OAuth token for %s", user.email)
HEAD:backend/onyx/auth/oauth_refresher.py:383:        logger.exception("Error refreshing OAuth token: %s", str(e))
HEAD:backend/onyx/auth/oauth_refresher.py:387:async def check_and_refresh_oauth_tokens(
HEAD:backend/onyx/auth/oauth_refresher.py:393:    Check if any OAuth tokens are expired or about to expire and refresh them.
HEAD:backend/onyx/auth/oauth_refresher.py:395:    if not hasattr(user, "oauth_accounts") or not user.oauth_accounts:
HEAD:backend/onyx/auth/oauth_refresher.py:403:    for oauth_account in user.oauth_accounts:
HEAD:backend/onyx/auth/oauth_refresher.py:405:        if not oauth_account.refresh_token:
HEAD:backend/onyx/auth/oauth_refresher.py:410:            oauth_account.expires_at
HEAD:backend/onyx/auth/oauth_refresher.py:411:            and oauth_account.expires_at - now_timestamp < buffer_seconds
HEAD:backend/onyx/auth/oauth_refresher.py:420:                    await db_session.refresh(oauth_account)
HEAD:backend/onyx/auth/oauth_refresher.py:422:                    # `db_session.refresh` can fail when oauth_account is
HEAD:backend/onyx/auth/oauth_refresher.py:441:                    oauth_account.expires_at
HEAD:backend/onyx/auth/oauth_refresher.py:442:                    and oauth_account.expires_at - now_timestamp >= buffer_seconds
HEAD:backend/onyx/auth/oauth_refresher.py:448:                    "OAuth token for %s is about to expire - refreshing", user.email
HEAD:backend/onyx/auth/oauth_refresher.py:450:                success = await refresh_oauth_token(
HEAD:backend/onyx/auth/oauth_refresher.py:451:                    user, oauth_account, db_session, user_manager
HEAD:backend/onyx/auth/oauth_refresher.py:456:                        "Failed to refresh OAuth token. User may need to re-authenticate."
HEAD:backend/onyx/auth/oauth_refresher.py:460:async def check_oauth_account_has_refresh_token(
HEAD:backend/onyx/auth/oauth_refresher.py:462:    oauth_account: OAuthAccount,
HEAD:backend/onyx/auth/oauth_refresher.py:465:    Check if an OAuth account has a refresh token.
HEAD:backend/onyx/auth/oauth_refresher.py:468:    return bool(oauth_account.refresh_token)
HEAD:backend/onyx/auth/oauth_refresher.py:471:async def get_oauth_accounts_requiring_refresh_token(user: User) -> List[OAuthAccount]:
HEAD:backend/onyx/auth/oauth_refresher.py:473:    Returns a list of OAuth accounts for a user that are missing refresh tokens.
HEAD:backend/onyx/auth/oauth_refresher.py:476:    if not hasattr(user, "oauth_accounts") or not user.oauth_accounts:
HEAD:backend/onyx/auth/oauth_refresher.py:480:    for oauth_account in user.oauth_accounts:
HEAD:backend/onyx/auth/oauth_refresher.py:481:        has_refresh_token = await check_oauth_account_has_refresh_token(
HEAD:backend/onyx/auth/oauth_refresher.py:482:            user, oauth_account
HEAD:backend/onyx/auth/oauth_refresher.py:485:            accounts_needing_refresh.append(oauth_account)
HEAD:backend/onyx/auth/oauth_token_manager.py:10:from onyx.db.models import OAuthConfig, OAuthUserToken
HEAD:backend/onyx/auth/oauth_token_manager.py:11:from onyx.db.oauth_config import get_user_oauth_token, upsert_user_oauth_token
HEAD:backend/onyx/auth/oauth_token_manager.py:19:def validate_oauth_endpoint_url(url: str, *, resolve_dns: bool = True) -> None:
HEAD:backend/onyx/auth/oauth_token_manager.py:20:    """SSRF guard for admin-configured OAuth endpoints, shared by store-time
HEAD:backend/onyx/auth/oauth_token_manager.py:25:    ``https_only`` since OAuth endpoints must be TLS. ``resolve_dns=False`` skips
HEAD:backend/onyx/auth/oauth_token_manager.py:40:OAUTH_RESPONSE_TYPE_CODE = "code"
HEAD:backend/onyx/auth/oauth_token_manager.py:41:OAUTH_GRANT_TYPE_AUTHORIZATION_CODE = "authorization_code"
HEAD:backend/onyx/auth/oauth_token_manager.py:42:OAUTH_PKCE_CHALLENGE_METHOD_S256 = "S256"
HEAD:backend/onyx/auth/oauth_token_manager.py:51:    # config without one. Matches Onyx's own Google login flow.
HEAD:backend/onyx/auth/oauth_token_manager.py:71:class OAuthFlowParams(BaseModel):
HEAD:backend/onyx/auth/oauth_token_manager.py:72:    """Stateless inputs for the OAuth 2.0 authorization-code grant, decoupled
HEAD:backend/onyx/auth/oauth_token_manager.py:73:    from any storage model so both `OAuthConfig`-backed tool OAuth and MCP
HEAD:backend/onyx/auth/oauth_token_manager.py:74:    known-provider OAuth can share the wire primitives below."""
HEAD:backend/onyx/auth/oauth_token_manager.py:84:def build_oauth_authorization_url(
HEAD:backend/onyx/auth/oauth_token_manager.py:85:    params: OAuthFlowParams,
HEAD:backend/onyx/auth/oauth_token_manager.py:98:        "response_type": OAUTH_RESPONSE_TYPE_CODE,
HEAD:backend/onyx/auth/oauth_token_manager.py:105:        query["code_challenge_method"] = OAUTH_PKCE_CHALLENGE_METHOD_S256
HEAD:backend/onyx/auth/oauth_token_manager.py:117:def exchange_oauth_code_for_token(
HEAD:backend/onyx/auth/oauth_token_manager.py:118:    params: OAuthFlowParams,
HEAD:backend/onyx/auth/oauth_token_manager.py:128:        "grant_type": OAUTH_GRANT_TYPE_AUTHORIZATION_CODE,
HEAD:backend/onyx/auth/oauth_token_manager.py:138:    validate_oauth_endpoint_url(params.token_url)
HEAD:backend/onyx/auth/oauth_token_manager.py:150:class OAuthTokenManager:
HEAD:backend/onyx/auth/oauth_token_manager.py:151:    """Manages OAuth token retrieval, refresh, and validation"""
HEAD:backend/onyx/auth/oauth_token_manager.py:153:    def __init__(self, oauth_config: OAuthConfig, user_id: UUID, db_session: Session):
HEAD:backend/onyx/auth/oauth_token_manager.py:154:        self.oauth_config = oauth_config
HEAD:backend/onyx/auth/oauth_token_manager.py:160:        user_token = get_user_oauth_token(
HEAD:backend/onyx/auth/oauth_token_manager.py:161:            self.oauth_config.id, self.user_id, self.db_session
HEAD:backend/onyx/auth/oauth_token_manager.py:173:        if OAuthTokenManager.is_token_expired(token_data):
HEAD:backend/onyx/auth/oauth_token_manager.py:186:    def refresh_token(self, user_token: OAuthUserToken) -> str:
HEAD:backend/onyx/auth/oauth_token_manager.py:192:            self.oauth_config.client_id is None
HEAD:backend/onyx/auth/oauth_token_manager.py:193:            or self.oauth_config.client_secret is None
HEAD:backend/onyx/auth/oauth_token_manager.py:196:                "OAuth client_id and client_secret are required for token refresh"
HEAD:backend/onyx/auth/oauth_token_manager.py:204:            "client_id": self._unwrap_sensitive_str(self.oauth_config.client_id),
HEAD:backend/onyx/auth/oauth_token_manager.py:206:                self.oauth_config.client_secret
HEAD:backend/onyx/auth/oauth_token_manager.py:209:        validate_oauth_endpoint_url(self.oauth_config.token_url)
HEAD:backend/onyx/auth/oauth_token_manager.py:211:            self.oauth_config.token_url,
HEAD:backend/onyx/auth/oauth_token_manager.py:230:        upsert_user_oauth_token(
HEAD:backend/onyx/auth/oauth_token_manager.py:231:            self.oauth_config.id,
HEAD:backend/onyx/auth/oauth_token_manager.py:261:            self.oauth_config.client_id is None
HEAD:backend/onyx/auth/oauth_token_manager.py:262:            or self.oauth_config.client_secret is None
HEAD:backend/onyx/auth/oauth_token_manager.py:265:                "OAuth client_id and client_secret are required for code exchange"
HEAD:backend/onyx/auth/oauth_token_manager.py:268:        return exchange_oauth_code_for_token(
HEAD:backend/onyx/auth/oauth_token_manager.py:269:            self._flow_params(self.oauth_config), code, redirect_uri
HEAD:backend/onyx/auth/oauth_token_manager.py:274:        oauth_config: OAuthConfig, redirect_uri: str, state: str
HEAD:backend/onyx/auth/oauth_token_manager.py:276:        """Build OAuth authorization URL"""
HEAD:backend/onyx/auth/oauth_token_manager.py:277:        if oauth_config.client_id is None:
HEAD:backend/onyx/auth/oauth_token_manager.py:278:            raise ValueError("OAuth client_id is required to build authorization URL")
HEAD:backend/onyx/auth/oauth_token_manager.py:279:        return build_oauth_authorization_url(
HEAD:backend/onyx/auth/oauth_token_manager.py:280:            OAuthTokenManager._flow_params(oauth_config), redirect_uri, state
HEAD:backend/onyx/auth/oauth_token_manager.py:284:    def _flow_params(oauth_config: OAuthConfig) -> OAuthFlowParams:
HEAD:backend/onyx/auth/oauth_token_manager.py:285:        if oauth_config.client_id is None:
HEAD:backend/onyx/auth/oauth_token_manager.py:286:            raise ValueError("OAuth client_id is required")
HEAD:backend/onyx/auth/oauth_token_manager.py:288:            OAuthTokenManager._unwrap_sensitive_str(oauth_config.client_secret)
HEAD:backend/onyx/auth/oauth_token_manager.py:289:            if oauth_config.client_secret is not None
HEAD:backend/onyx/auth/oauth_token_manager.py:292:        return OAuthFlowParams(
HEAD:backend/onyx/auth/oauth_token_manager.py:293:            authorization_url=oauth_config.authorization_url,
HEAD:backend/onyx/auth/oauth_token_manager.py:294:            token_url=oauth_config.token_url,
HEAD:backend/onyx/auth/oauth_token_manager.py:295:            client_id=OAuthTokenManager._unwrap_sensitive_str(oauth_config.client_id),
HEAD:backend/onyx/auth/oauth_token_manager.py:297:            scopes=oauth_config.scopes,
HEAD:backend/onyx/auth/oauth_token_manager.py:298:            additional_params=oauth_config.additional_params,
HEAD:backend/onyx/auth/oidc_client.py:10:from httpx_oauth.clients.openid import BASE_SCOPES, OpenID
HEAD:backend/onyx/auth/oidc_client.py:11:from httpx_oauth.exceptions import GetIdEmailError
HEAD:backend/onyx/auth/oidc_client.py:12:from httpx_oauth.oauth2 import GetAccessTokenError
HEAD:backend/onyx/auth/oidc_client.py:21:_OAUTH_ERROR_FIELDS = ("error", "error_description", "error_uri")
HEAD:backend/onyx/auth/oidc_client.py:31:    fields = {k: payload[k] for k in _OAUTH_ERROR_FIELDS if k in payload}
HEAD:backend/onyx/auth/oidc_client.py:110:    claim is exactly the nOAuth account-takeover vector. An absent claim
HEAD:backend/onyx/auth/oidc_client.py:114:    unchanged and rejected by the login flow's existing no-email handling."""
HEAD:backend/onyx/auth/oidc_client.py:153:            # A malformed userinfo body must surface as a controlled login
HEAD:backend/onyx/auth/permission_projection.py:130:    authenticate (its OAuth config) — is owner-or-admin (``can_manage``): the creator fully
HEAD:backend/onyx/auth/pkce.py:1:"""PKCE (RFC 7636) S256 helpers for OAuth flows."""
HEAD:backend/onyx/auth/session_tokens.py:4:and logout writes a tombstone instead of deleting, so a rejected token can be
HEAD:backend/onyx/auth/session_tokens.py:103:    Builds the logout tombstone, preserving the original fields when the
HEAD:backend/onyx/auth/sso_tenant_token.py:1:"""Signed workspace pin for an in-flight cloud SSO login.
HEAD:backend/onyx/auth/sso_tenant_token.py:3:Cloud serves every workspace from one domain, so the SSO login routes have no
HEAD:backend/onyx/auth/sso_tenant_token.py:21:SSO_TENANT_TOKEN_AUDIENCE = "onyx:sso-login-tenant"
HEAD:backend/onyx/auth/sso_tenant_token.py:37:    """The tenant this login step is pinned to. Raises when the token is
HEAD:backend/onyx/auth/sso_tenant_token.py:44:            "Sign-in link has expired. Return to the login page and try again.",
HEAD:backend/onyx/auth/users.py:29:from fastapi.security import OAuth2PasswordRequestForm
HEAD:backend/onyx/auth/users.py:56:from httpx_oauth.exceptions import GetIdEmailError
HEAD:backend/onyx/auth/users.py:57:from httpx_oauth.integrations.fastapi import OAuth2AuthorizeCallback
HEAD:backend/onyx/auth/users.py:58:from httpx_oauth.oauth2 import BaseOAuth2, GetAccessTokenError, OAuth2Token
HEAD:backend/onyx/auth/users.py:72:from onyx.auth.jwt import verify_jwt_token
HEAD:backend/onyx/auth/users.py:73:from onyx.auth.login_claims_capture import capture_oauth_login_claims
HEAD:backend/onyx/auth/users.py:137:from onyx.db.models import AccessToken, OAuthAccount, User
HEAD:backend/onyx/auth/users.py:144:    get_user_by_oauth_account,
HEAD:backend/onyx/auth/users.py:146:    promote_placeholder_to_web_login__no_commit,
HEAD:backend/onyx/auth/users.py:187:REGISTER_INVITE_ONLY_CODE = "REGISTER_INVITE_ONLY"
HEAD:backend/onyx/auth/users.py:194:def verify_auth_setting() -> None:
HEAD:backend/onyx/auth/users.py:204:    if raw_auth_type in ("google_oauth", "oidc", "saml"):
HEAD:backend/onyx/auth/users.py:207:            "as 'basic'. SSO login is now served by SSO provider rows (Admin "
HEAD:backend/onyx/auth/users.py:216:def verify_user_auth_secret() -> None:
HEAD:backend/onyx/auth/users.py:219:    The secret signs password-reset and email-verification tokens, OAuth login
HEAD:backend/onyx/auth/users.py:231:        "verification tokens, OAuth login state, and captcha cookies, so an "
HEAD:backend/onyx/auth/users.py:311:def verify_email_is_invited(email: str) -> None:
HEAD:backend/onyx/auth/users.py:346:def remove_user_from_invited_users_after_login(
HEAD:backend/onyx/auth/users.py:350:    member, so a failure must not fail the login."""
HEAD:backend/onyx/auth/users.py:355:            "Invite cleanup failed after login: user_id=%s tenant=%s",
HEAD:backend/onyx/auth/users.py:362:def rekey_tenant_mapping_after_login(
HEAD:backend/onyx/auth/users.py:365:    oauth_identities: list[tuple[str, str]],
HEAD:backend/onyx/auth/users.py:368:    """Best-effort catalog rekey for a login that has already succeeded.
HEAD:backend/onyx/auth/users.py:371:    the old address still reaches the right workspace and the next login retries.
HEAD:backend/onyx/auth/users.py:376:        )(email, tenant_id, oauth_identities, previous_email)
HEAD:backend/onyx/auth/users.py:379:            "Tenant mapping rekey failed after login: tenant=%s",
HEAD:backend/onyx/auth/users.py:385:def verify_email_in_whitelist(
HEAD:backend/onyx/auth/users.py:388:    oauth_name: str | None = None,
HEAD:backend/onyx/auth/users.py:393:        if user is None and oauth_name and account_id:
HEAD:backend/onyx/auth/users.py:395:            # provider has renamed their address since the previous login.
HEAD:backend/onyx/auth/users.py:396:            user = get_user_by_oauth_account(oauth_name, account_id, db_session)
HEAD:backend/onyx/auth/users.py:400:        if user is None or not user.account_type.is_web_login():
HEAD:backend/onyx/auth/users.py:401:            verify_email_is_invited(email)
HEAD:backend/onyx/auth/users.py:404:def verify_email_domain(
HEAD:backend/onyx/auth/users.py:427:        # able to sign in with the address they originally registered with.
HEAD:backend/onyx/auth/users.py:531:def _upgrade_placeholder_to_web_login__no_commit(
HEAD:backend/onyx/auth/users.py:534:    """Promote a placeholder row (EXT_PERM_USER, BOT) to a real web login.
HEAD:backend/onyx/auth/users.py:543:    first logins when it is not.
HEAD:backend/onyx/auth/users.py:552:    # the row is still a placeholder now that it is held: a concurrent login may
HEAD:backend/onyx/auth/users.py:556:    if user.account_type.is_web_login():
HEAD:backend/onyx/auth/users.py:566:    promote_placeholder_to_web_login__no_commit(
HEAD:backend/onyx/auth/users.py:573:    """Workspace to bind a user to. An explicit override wins, since an SSO login
HEAD:backend/onyx/auth/users.py:587:    reset_password_token_secret = USER_AUTH_SECRET
HEAD:backend/onyx/auth/users.py:602:                    db_session, User, OAuthAccount
HEAD:backend/onyx/auth/users.py:616:                    db_session, User, OAuthAccount
HEAD:backend/onyx/auth/users.py:627:    async def verify(self, token: str, request: Optional[Request] = None) -> User:
HEAD:backend/onyx/auth/users.py:631:            return await super().verify(token, request)
HEAD:backend/onyx/auth/users.py:633:        # Multi-tenant: the verify request has no auth cookie yet, so the
HEAD:backend/onyx/auth/users.py:636:        # session, mirroring oauth_callback / get_by_email.
HEAD:backend/onyx/auth/users.py:644:            raise exceptions.InvalidVerifyToken()
HEAD:backend/onyx/auth/users.py:650:            raise exceptions.InvalidVerifyToken()
HEAD:backend/onyx/auth/users.py:659:            raise exceptions.InvalidVerifyToken()
HEAD:backend/onyx/auth/users.py:665:                    db_session, User, OAuthAccount
HEAD:backend/onyx/auth/users.py:670:                    raise exceptions.InvalidVerifyToken()
HEAD:backend/onyx/auth/users.py:675:                    raise exceptions.InvalidVerifyToken()
HEAD:backend/onyx/auth/users.py:678:                    raise exceptions.InvalidVerifyToken()
HEAD:backend/onyx/auth/users.py:685:                await self.on_after_verify(verified_user, request)
HEAD:backend/onyx/auth/users.py:697:        # rejected before hitting Google's siteverify API. Cheap local check.
HEAD:backend/onyx/auth/users.py:707:            verify_email_domain(
HEAD:backend/onyx/auth/users.py:730:        # Verify captcha if enabled (for cloud signup protection)
HEAD:backend/onyx/auth/users.py:735:            verify_captcha_token,
HEAD:backend/onyx/auth/users.py:751:                await verify_captcha_token(captcha_token or "", CaptchaAction.SIGNUP)
HEAD:backend/onyx/auth/users.py:755:        # We verify the password here to make sure it's valid before we proceed
HEAD:backend/onyx/auth/users.py:788:                        verify_email_is_invited(user_create.email)
HEAD:backend/onyx/auth/users.py:791:                    verify_email_is_invited(user_create.email)
HEAD:backend/onyx/auth/users.py:794:                        db_session, User, OAuthAccount
HEAD:backend/onyx/auth/users.py:838:                        user.account_type.is_web_login()
HEAD:backend/onyx/auth/users.py:840:                        or not user_create.account_type.is_web_login()
HEAD:backend/onyx/auth/users.py:870:                        user.account_type.is_web_login()
HEAD:backend/onyx/auth/users.py:872:                        or not user_create.account_type.is_web_login()
HEAD:backend/onyx/auth/users.py:911:        ``safe`` marks the public register path, where the request body is
HEAD:backend/onyx/auth/users.py:930:                # A registrant must not self-verify an address they do not own.
HEAD:backend/onyx/auth/users.py:987:    async def _rewrite_oauth_link(
HEAD:backend/onyx/auth/users.py:988:        self, user: User, link: OAuthAccount, oauth_account_dict: dict[str, Any]
HEAD:backend/onyx/auth/users.py:990:        return await self.user_db.update_oauth_account(
HEAD:backend/onyx/auth/users.py:992:            # OAuthAccount implements OAuthAccountProtocol, but the type
HEAD:backend/onyx/auth/users.py:995:            oauth_account_dict,
HEAD:backend/onyx/auth/users.py:999:    async def oauth_callback(  # ty: ignore[invalid-method-override]
HEAD:backend/onyx/auth/users.py:1001:        oauth_name: str,
HEAD:backend/onyx/auth/users.py:1021:        # where they belong, so a pinned login (override set) skips provisioning
HEAD:backend/onyx/auth/users.py:1032:            oauth_name=oauth_name,
HEAD:backend/onyx/auth/users.py:1040:            verify_email_in_whitelist(account_email, tenant_id, oauth_name, account_id)
HEAD:backend/onyx/auth/users.py:1041:            oauth_security_settings = get_security_settings()
HEAD:backend/onyx/auth/users.py:1045:                else oauth_security_settings.valid_email_domains
HEAD:backend/onyx/auth/users.py:1047:            verify_email_domain(
HEAD:backend/onyx/auth/users.py:1056:                )(tenant_id, account_email, oauth_name, account_id)
HEAD:backend/onyx/auth/users.py:1066:            oauth_account_dict = {
HEAD:backend/onyx/auth/users.py:1067:                "oauth_name": oauth_name,
HEAD:backend/onyx/auth/users.py:1078:                # Attempt to get user by OAuth account
HEAD:backend/onyx/auth/users.py:1079:                user = await self.get_by_oauth_account(oauth_name, account_id)
HEAD:backend/onyx/auth/users.py:1091:                    stale_link: OAuthAccount | None = next(
HEAD:backend/onyx/auth/users.py:1094:                            for link in user.oauth_accounts
HEAD:backend/onyx/auth/users.py:1095:                            if link.oauth_name == oauth_name
HEAD:backend/onyx/auth/users.py:1102:                    if user.account_type.is_web_login():
HEAD:backend/onyx/auth/users.py:1115:                            and oauth_security_settings.allow_same_provider_subject_relink
HEAD:backend/onyx/auth/users.py:1119:                            or (user.oauth_accounts and not relink_allowed)
HEAD:backend/onyx/auth/users.py:1124:                    # oauth_accounts[0], and a second link for this provider could
HEAD:backend/onyx/auth/users.py:1127:                        user = await self.user_db.add_oauth_account(
HEAD:backend/onyx/auth/users.py:1128:                            user, oauth_account_dict
HEAD:backend/onyx/auth/users.py:1132:                            "Relinked %s login for user %s from subject %s to %s",
HEAD:backend/onyx/auth/users.py:1133:                            oauth_name,
HEAD:backend/onyx/auth/users.py:1138:                        user = await self._rewrite_oauth_link(
HEAD:backend/onyx/auth/users.py:1139:                            user, stale_link, oauth_account_dict
HEAD:backend/onyx/auth/users.py:1143:                    # OAuth-created accounts are not subject to the dotted-Gmail
HEAD:backend/onyx/auth/users.py:1146:                    verify_email_domain(
HEAD:backend/onyx/auth/users.py:1165:                    await self.user_db.add_oauth_account(user, oauth_account_dict)
HEAD:backend/onyx/auth/users.py:1169:                    await self.on_after_register(user, request)
HEAD:backend/onyx/auth/users.py:1172:                # User exists, update OAuth account if needed
HEAD:backend/onyx/auth/users.py:1174:                    for existing_oauth_account in user.oauth_accounts:
HEAD:backend/onyx/auth/users.py:1176:                            existing_oauth_account.account_id == account_id
HEAD:backend/onyx/auth/users.py:1177:                            and existing_oauth_account.oauth_name == oauth_name
HEAD:backend/onyx/auth/users.py:1179:                            user = await self._rewrite_oauth_link(
HEAD:backend/onyx/auth/users.py:1180:                                user, existing_oauth_account, oauth_account_dict
HEAD:backend/onyx/auth/users.py:1186:                # A pinned login skipped the provisioning that records
HEAD:backend/onyx/auth/users.py:1190:                )(user.email, tenant_id, oauth_name, account_id)
HEAD:backend/onyx/auth/users.py:1195:                "onyx.db.user_tenant_mapping", "record_oauth_identity", None
HEAD:backend/onyx/auth/users.py:1196:            )(user.email, tenant_id, oauth_name, account_id)
HEAD:backend/onyx/auth/users.py:1209:                # and no later login reports that address again.
HEAD:backend/onyx/auth/users.py:1215:            oauth_identities = [
HEAD:backend/onyx/auth/users.py:1216:                (oauth_account.oauth_name, oauth_account.account_id)
HEAD:backend/onyx/auth/users.py:1217:                for oauth_account in user.oauth_accounts
HEAD:backend/onyx/auth/users.py:1220:            rekey_tenant_mapping_after_login(
HEAD:backend/onyx/auth/users.py:1221:                user.email, tenant_id, oauth_identities, replaced_email
HEAD:backend/onyx/auth/users.py:1227:                oauth_security_settings.track_external_idp_expiry
HEAD:backend/onyx/auth/users.py:1236:            if not user.account_type.is_web_login():
```
## Token and Session State
Evidence lines: 450
```text
HEAD:backend/ee/onyx/auth/users.py:7:from ee.onyx.configs.app_configs import SUPER_CLOUD_API_KEY, SUPER_USERS
HEAD:backend/ee/onyx/auth/users.py:29:    if not SUPER_CLOUD_API_KEY:
HEAD:backend/ee/onyx/auth/users.py:30:        logger.warning("SUPER_CLOUD_API_KEY is not configured; rejecting request")
HEAD:backend/ee/onyx/auth/users.py:31:        raise HTTPException(status_code=401, detail="Invalid API key")
HEAD:backend/ee/onyx/auth/users.py:33:    api_key = request.headers.get("Authorization", "").replace("Bearer ", "")
HEAD:backend/ee/onyx/auth/users.py:34:    if not secrets.compare_digest(api_key, SUPER_CLOUD_API_KEY):
HEAD:backend/ee/onyx/auth/users.py:35:        raise HTTPException(status_code=401, detail="Invalid API key")
HEAD:backend/onyx/auth/api_key.py:11:    API_KEY_LENGTH,
HEAD:backend/onyx/auth/api_key.py:12:    API_KEY_PREFIX,
HEAD:backend/onyx/auth/api_key.py:13:    DEPRECATED_API_KEY_PREFIX,
HEAD:backend/onyx/auth/api_key.py:15:from onyx.auth.utils import get_hashed_bearer_token_from_request
HEAD:backend/onyx/auth/api_key.py:16:from onyx.configs.app_configs import API_KEY_HASH_ROUNDS
HEAD:backend/onyx/auth/api_key.py:21:class ApiKeyDescriptor(BaseModel):
HEAD:backend/onyx/auth/api_key.py:22:    api_key_id: int
HEAD:backend/onyx/auth/api_key.py:23:    api_key_display: str
HEAD:backend/onyx/auth/api_key.py:24:    api_key: str | None = None  # only present on initial creation
HEAD:backend/onyx/auth/api_key.py:25:    api_key_name: str | None = None
HEAD:backend/onyx/auth/api_key.py:31:def generate_api_key(tenant_id: str | None = None) -> str:
HEAD:backend/onyx/auth/api_key.py:33:        return API_KEY_PREFIX + secrets.token_urlsafe(API_KEY_LENGTH)
HEAD:backend/onyx/auth/api_key.py:36:    return f"{API_KEY_PREFIX}{encoded_tenant}.{secrets.token_urlsafe(API_KEY_LENGTH)}"
HEAD:backend/onyx/auth/api_key.py:39:def _deprecated_hash_api_key(api_key: str) -> str:
HEAD:backend/onyx/auth/api_key.py:40:    return sha256_crypt.hash(api_key, salt="", rounds=API_KEY_HASH_ROUNDS)
HEAD:backend/onyx/auth/api_key.py:43:def hash_api_key(api_key: str) -> str:
HEAD:backend/onyx/auth/api_key.py:44:    # NOTE: no salt is needed, as the API key is randomly generated
HEAD:backend/onyx/auth/api_key.py:46:    if api_key.startswith(API_KEY_PREFIX):
HEAD:backend/onyx/auth/api_key.py:47:        return hashlib.sha256(api_key.encode("utf-8")).hexdigest()
HEAD:backend/onyx/auth/api_key.py:49:    if api_key.startswith(DEPRECATED_API_KEY_PREFIX):
HEAD:backend/onyx/auth/api_key.py:50:        return _deprecated_hash_api_key(api_key)
HEAD:backend/onyx/auth/api_key.py:52:    raise ValueError(f"Invalid API key prefix: {api_key[:3]}")
HEAD:backend/onyx/auth/api_key.py:55:def build_displayable_api_key(api_key: str) -> str:
HEAD:backend/onyx/auth/api_key.py:56:    if api_key.startswith(API_KEY_PREFIX):
HEAD:backend/onyx/auth/api_key.py:57:        api_key = api_key[len(API_KEY_PREFIX) :]
HEAD:backend/onyx/auth/api_key.py:59:    return API_KEY_PREFIX + api_key[:4] + "********" + api_key[-4:]
HEAD:backend/onyx/auth/api_key.py:62:def get_hashed_api_key_from_request(request: Request) -> str | None:
HEAD:backend/onyx/auth/api_key.py:63:    """Extract and hash API key from Authorization header.
HEAD:backend/onyx/auth/api_key.py:65:    Accepts both "Bearer <key>" and raw key formats.
HEAD:backend/onyx/auth/api_key.py:67:    return get_hashed_bearer_token_from_request(
HEAD:backend/onyx/auth/api_key.py:69:        valid_prefixes=[API_KEY_PREFIX, DEPRECATED_API_KEY_PREFIX],
HEAD:backend/onyx/auth/api_key.py:70:        hash_fn=hash_api_key,
HEAD:backend/onyx/auth/api_key.py:71:        allow_non_bearer=True,  # API keys historically support both formats
HEAD:backend/onyx/auth/captcha.py:8:   sets a signed cookie, and ``CaptchaCookieMiddleware`` checks the
HEAD:backend/onyx/auth/captcha.py:9:   cookie on the ``/auth/oauth/callback`` redirect.
HEAD:backend/onyx/auth/captcha.py:13:``issue_captcha_cookie_value`` / ``validate_captcha_cookie_value`` sign
HEAD:backend/onyx/auth/captcha.py:14:the OAuth cookie.
HEAD:backend/onyx/auth/captcha.py:27:    CAPTCHA_COOKIE_TTL_SECONDS,
HEAD:backend/onyx/auth/captcha.py:29:    RECAPTCHA_ENTERPRISE_API_KEY,
HEAD:backend/onyx/auth/captcha.py:41:CAPTCHA_COOKIE_NAME = "onyx_captcha_verified"
HEAD:backend/onyx/auth/captcha.py:105:        and bool(RECAPTCHA_ENTERPRISE_API_KEY)
HEAD:backend/onyx/auth/captcha.py:241:                params={"key": RECAPTCHA_ENTERPRISE_API_KEY},
HEAD:backend/onyx/auth/captcha.py:263:def _cookie_signing_key() -> bytes:
HEAD:backend/onyx/auth/captcha.py:265:        f"onyx-captcha-cookie-v1::{USER_AUTH_SECRET}".encode("utf-8")
HEAD:backend/onyx/auth/captcha.py:269:def issue_captcha_cookie_value(now: int | None = None) -> str:
HEAD:backend/onyx/auth/captcha.py:272:    expiry = issued_at + CAPTCHA_COOKIE_TTL_SECONDS
HEAD:backend/onyx/auth/captcha.py:274:        _cookie_signing_key(), str(expiry).encode("utf-8"), hashlib.sha256
HEAD:backend/onyx/auth/captcha.py:279:def validate_captcha_cookie_value(value: str | None) -> bool:
HEAD:backend/onyx/auth/captcha.py:293:        _cookie_signing_key(), str(expiry).encode("utf-8"), hashlib.sha256
HEAD:backend/onyx/auth/constants.py:3:# API Key constants
HEAD:backend/onyx/auth/constants.py:4:API_KEY_PREFIX = "on_"
HEAD:backend/onyx/auth/constants.py:5:DEPRECATED_API_KEY_PREFIX = "dn_"
HEAD:backend/onyx/auth/constants.py:6:API_KEY_LENGTH = 192
HEAD:backend/onyx/auth/constants.py:18:API_KEY_HEADER_NAME = "Authorization"
HEAD:backend/onyx/auth/constants.py:19:API_KEY_HEADER_ALTERNATIVE_NAME = "X-Onyx-Authorization"
HEAD:backend/onyx/auth/constants.py:20:BEARER_PREFIX = "Bearer "
HEAD:backend/onyx/auth/email_utils.py:27:    SENDGRID_API_KEY,
HEAD:backend/onyx/auth/email_utils.py:197:    if SENDGRID_API_KEY:
HEAD:backend/onyx/auth/email_utils.py:264:    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
HEAD:backend/onyx/auth/login_claims_capture.py:231:    userinfo_endpoint: str, access_token: str
HEAD:backend/onyx/auth/login_claims_capture.py:236:            headers={"Authorization": f"Bearer {access_token}"},
HEAD:backend/onyx/auth/login_claims_capture.py:248:async def _fetch_ms_graph_profile(access_token: str) -> dict[str, Any]:
HEAD:backend/onyx/auth/login_claims_capture.py:257:            headers={"Authorization": f"Bearer {access_token}"},
HEAD:backend/onyx/auth/login_claims_capture.py:332:        access_token = token.get("access_token")
HEAD:backend/onyx/auth/login_claims_capture.py:333:        if userinfo_endpoint and access_token:
HEAD:backend/onyx/auth/login_claims_capture.py:335:                userinfo = await _fetch_userinfo(userinfo_endpoint, access_token)
HEAD:backend/onyx/auth/login_claims_capture.py:345:        if access_token and userinfo_endpoint and _MS_GRAPH_HOST in userinfo_endpoint:
HEAD:backend/onyx/auth/login_claims_capture.py:347:                directory_profile = await _fetch_ms_graph_profile(access_token)
HEAD:backend/onyx/auth/login_claims_capture.py:368:                "has_refresh_token": bool(token.get("refresh_token")),
HEAD:backend/onyx/auth/mobile_sso/__init__.py:7:that code for the existing revocable session token (as a Bearer) at
HEAD:backend/onyx/auth/mobile_sso/code_store.py:3:The mobile SSO bridge never puts a session token on the (interceptable)
HEAD:backend/onyx/auth/mobile_sso/sso_completion.py:5:marker. It mints the session token, stashes it behind a single-use PKCE-bound
HEAD:backend/onyx/auth/mobile_sso/sso_completion.py:11:need no separate cookie. ``is_mobile_sso`` / ``apply_mobile_state`` keep the
HEAD:backend/onyx/auth/mobile_sso/sso_completion.py:105:    does NOT call ``backend.login``, so no web auth cookie is ever set.
HEAD:backend/onyx/auth/mobile_sso/tokens.py:4:Today it mints the SAME session token the web cookie flow uses (via the active
HEAD:backend/onyx/auth/mobile_sso/tokens.py:7:only in transport (Authorization header vs HttpOnly cookie).
HEAD:backend/onyx/auth/oauth_refresher.py:305:    if not oauth_account.refresh_token:
HEAD:backend/onyx/auth/oauth_refresher.py:327:                    "refresh_token": oauth_account.refresh_token,
HEAD:backend/onyx/auth/oauth_refresher.py:328:                    "grant_type": "refresh_token",
HEAD:backend/onyx/auth/oauth_refresher.py:341:            new_access_token = token_data.get("access_token")
HEAD:backend/onyx/auth/oauth_refresher.py:342:            new_refresh_token = token_data.get(
HEAD:backend/onyx/auth/oauth_refresher.py:343:                "refresh_token", oauth_account.refresh_token
HEAD:backend/onyx/auth/oauth_refresher.py:356:                "access_token": new_access_token,
HEAD:backend/onyx/auth/oauth_refresher.py:357:                "refresh_token": new_refresh_token,
HEAD:backend/onyx/auth/oauth_refresher.py:405:        if not oauth_account.refresh_token:
HEAD:backend/onyx/auth/oauth_refresher.py:415:            # refreshed `expires_at` (and `refresh_token` for IdPs that
HEAD:backend/onyx/auth/oauth_refresher.py:460:async def check_oauth_account_has_refresh_token(
HEAD:backend/onyx/auth/oauth_refresher.py:468:    return bool(oauth_account.refresh_token)
HEAD:backend/onyx/auth/oauth_refresher.py:471:async def get_oauth_accounts_requiring_refresh_token(user: User) -> List[OAuthAccount]:
HEAD:backend/onyx/auth/oauth_refresher.py:481:        has_refresh_token = await check_oauth_account_has_refresh_token(
HEAD:backend/onyx/auth/oauth_refresher.py:484:        if not has_refresh_token:
HEAD:backend/onyx/auth/oauth_token_manager.py:158:    def get_valid_access_token(self) -> str | None:
HEAD:backend/onyx/auth/oauth_token_manager.py:175:            if "refresh_token" in token_data:
HEAD:backend/onyx/auth/oauth_token_manager.py:177:                    return self.refresh_token(user_token)
HEAD:backend/onyx/auth/oauth_token_manager.py:184:        return token_data.get("access_token")
HEAD:backend/onyx/auth/oauth_token_manager.py:186:    def refresh_token(self, user_token: OAuthUserToken) -> str:
HEAD:backend/onyx/auth/oauth_token_manager.py:202:            "grant_type": "refresh_token",
HEAD:backend/onyx/auth/oauth_token_manager.py:203:            "refresh_token": token_data["refresh_token"],
HEAD:backend/onyx/auth/oauth_token_manager.py:225:        # Preserve refresh_token if not returned (some providers don't return it)
HEAD:backend/onyx/auth/oauth_token_manager.py:226:        if "refresh_token" not in new_token_data and "refresh_token" in token_data:
HEAD:backend/onyx/auth/oauth_token_manager.py:227:            new_token_data["refresh_token"] = token_data["refresh_token"]
HEAD:backend/onyx/auth/oauth_token_manager.py:237:        return new_token_data["access_token"]
HEAD:backend/onyx/auth/oidc_client.py:147:                headers={**self.request_headers, "Authorization": f"Bearer {token}"},
HEAD:backend/onyx/auth/pat.py:1:"""Personal Access Token generation and validation."""
HEAD:backend/onyx/auth/pat.py:11:from onyx.auth.utils import get_hashed_bearer_token_from_request
HEAD:backend/onyx/auth/pat.py:40:    Only accepts "Bearer <token>" format (unlike API keys which support raw format).
HEAD:backend/onyx/auth/pat.py:42:    return get_hashed_bearer_token_from_request(
HEAD:backend/onyx/auth/pat.py:46:        allow_non_bearer=False,  # PATs require Bearer prefix
HEAD:backend/onyx/auth/permissions.py:61:    Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS.value: {
HEAD:backend/onyx/auth/permissions.py:195:        description="Add and update service accounts and their API keys.",
HEAD:backend/onyx/auth/permissions.py:196:        permissions=[Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS],
HEAD:backend/onyx/auth/permissions.py:237:        id="create_user_access_token",
HEAD:backend/onyx/auth/permissions.py:239:        description="Add and update the user's personal access tokens.",
HEAD:backend/onyx/auth/permissions.py:240:        permissions=[Permission.CREATE_USER_API_KEYS],
HEAD:backend/onyx/auth/permissions.py:327:    authenticating token's scopes (unrestricted PAT / session / API key = no cap).
HEAD:backend/onyx/auth/schemas.py:41:        # (SCIM, API key creation) supply a different account_type directly.
HEAD:backend/onyx/auth/session_tokens.py:6:(no entry: cookie outlived the grace window, or Redis dropped the key),
HEAD:backend/onyx/auth/session_tokens.py:11:``read_token`` must return None rather than raise (API keys/PATs/JWTs share the
HEAD:backend/onyx/auth/session_tokens.py:12:bearer transport and legitimately miss in Redis), so the classification is
HEAD:backend/onyx/auth/session_tokens.py:24:from onyx.auth.constants import API_KEY_PREFIX, DEPRECATED_API_KEY_PREFIX, PAT_PREFIX
HEAD:backend/onyx/auth/session_tokens.py:33:SESSION_TOKEN_GRACE_PERIOD_SECONDS = 60 * 60
HEAD:backend/onyx/auth/session_tokens.py:84:def build_session_token_value(
HEAD:backend/onyx/auth/session_tokens.py:130:    return lifetime_seconds + SESSION_TOKEN_GRACE_PERIOD_SECONDS
HEAD:backend/onyx/auth/session_tokens.py:133:def may_be_session_token(token: str) -> bool:
HEAD:backend/onyx/auth/session_tokens.py:135:    Session tokens are bare ``token_urlsafe()`` strings: no prefix, no dots.
HEAD:backend/onyx/auth/session_tokens.py:136:    Excludes API keys / PATs / JWTs so their expected misses never classify.
HEAD:backend/onyx/auth/session_tokens.py:138:    if token.startswith((API_KEY_PREFIX, DEPRECATED_API_KEY_PREFIX, PAT_PREFIX)):
HEAD:backend/onyx/auth/session_tokens.py:143:def classify_session_token_value(
HEAD:backend/onyx/auth/session_tokens.py:208:        "Rejected session token: reason=%s user_id=%s token_age=%s issued_at=%s "
HEAD:backend/onyx/auth/session_tokens.py:219:            "Presented session token has no Redis entry: the cookie outlived "
HEAD:backend/onyx/auth/sso_web_error.py:1:"""Render SSO callback failures for browsers and drop the flow's PKCE cookie.
HEAD:backend/onyx/auth/sso_web_error.py:8:single-use PKCE cookie is deleted with the error response.
HEAD:backend/onyx/auth/sso_web_error.py:21:from onyx.auth.users import get_pkce_cookie_name
HEAD:backend/onyx/auth/sso_web_error.py:29:_COOKIE_SECURE = WEB_DOMAIN.startswith("https")
HEAD:backend/onyx/auth/sso_web_error.py:32:def delete_pkce_cookie(response: Response, state: str) -> None:
HEAD:backend/onyx/auth/sso_web_error.py:33:    """Path must match the set-cookie or browsers treat the delete as a
HEAD:backend/onyx/auth/sso_web_error.py:34:    different cookie and keep the original."""
HEAD:backend/onyx/auth/sso_web_error.py:35:    response.delete_cookie(
HEAD:backend/onyx/auth/sso_web_error.py:36:        key=get_pkce_cookie_name(state),
HEAD:backend/onyx/auth/sso_web_error.py:38:        secure=_COOKIE_SECURE,
HEAD:backend/onyx/auth/sso_web_error.py:44:def _delete_flow_pkce_cookie(request: Request, response: Response) -> None:
HEAD:backend/onyx/auth/sso_web_error.py:46:    if state and request.cookies.get(get_pkce_cookie_name(state)) is not None:
HEAD:backend/onyx/auth/sso_web_error.py:47:        delete_pkce_cookie(response, state)
HEAD:backend/onyx/auth/sso_web_error.py:79:            _delete_flow_pkce_cookie(request, response)
HEAD:backend/onyx/auth/users.py:40:    BearerTransport,
HEAD:backend/onyx/auth/users.py:41:    CookieTransport,
HEAD:backend/onyx/auth/users.py:65:from onyx.auth.api_key import get_hashed_api_key_from_request
HEAD:backend/onyx/auth/users.py:84:from onyx.auth.session_tokens import (
HEAD:backend/onyx/auth/users.py:85:    SESSION_TOKEN_GRACE_PERIOD_SECONDS,
HEAD:backend/onyx/auth/users.py:88:    build_session_token_value,
HEAD:backend/onyx/auth/users.py:90:    classify_session_token_value,
HEAD:backend/onyx/auth/users.py:92:    may_be_session_token,
HEAD:backend/onyx/auth/users.py:99:    AUTH_COOKIE_EXPIRE_TIME_SECONDS,
HEAD:backend/onyx/auth/users.py:103:    REDIS_AUTH_KEY_PREFIX,
HEAD:backend/onyx/auth/users.py:110:    ANONYMOUS_USER_COOKIE_NAME,
HEAD:backend/onyx/auth/users.py:113:    DANSWER_API_KEY_DUMMY_EMAIL_DOMAIN,
HEAD:backend/onyx/auth/users.py:114:    DANSWER_API_KEY_PREFIX,
HEAD:backend/onyx/auth/users.py:115:    FASTAPI_USERS_AUTH_COOKIE_NAME,
HEAD:backend/onyx/auth/users.py:121:from onyx.db.api_key import fetch_api_key_auth_result
HEAD:backend/onyx/auth/users.py:123:    get_access_token_db,
HEAD:backend/onyx/auth/users.py:220:    state, and captcha cookies. An empty value makes all of them forgeable, so a
HEAD:backend/onyx/auth/users.py:231:        "verification tokens, OAuth login state, and captcha cookies, so an "
HEAD:backend/onyx/auth/users.py:245:    if email and email.endswith(DANSWER_API_KEY_DUMMY_EMAIL_DOMAIN):
HEAD:backend/onyx/auth/users.py:247:        if name == DANSWER_API_KEY_PREFIX + UNNAMED_KEY_PLACEHOLDER:
HEAD:backend/onyx/auth/users.py:248:            return "Unnamed API Key"
HEAD:backend/onyx/auth/users.py:253:        return name.replace("API_KEY__", "API Key: ")
HEAD:backend/onyx/auth/users.py:589:    verification_token_lifetime_seconds = AUTH_COOKIE_EXPIRE_TIME_SECONDS
HEAD:backend/onyx/auth/users.py:633:        # Multi-tenant: the verify request has no auth cookie yet, so the
HEAD:backend/onyx/auth/users.py:762:            request.cookies.get("referral_source", None)
HEAD:backend/onyx/auth/users.py:1002:        access_token: str,
HEAD:backend/onyx/auth/users.py:1006:        refresh_token: Optional[str] = None,
HEAD:backend/onyx/auth/users.py:1068:                "access_token": access_token,
HEAD:backend/onyx/auth/users.py:1072:                "refresh_token": refresh_token,
HEAD:backend/onyx/auth/users.py:1123:                    # Rewrite rather than append: bearer pass-through reads
HEAD:backend/onyx/auth/users.py:1279:            if response and request and ANONYMOUS_USER_COOKIE_NAME in request.cookies:
HEAD:backend/onyx/auth/users.py:1280:                response.delete_cookie(
HEAD:backend/onyx/auth/users.py:1281:                    ANONYMOUS_USER_COOKIE_NAME,
HEAD:backend/onyx/auth/users.py:1282:                    # Ensure cookie deletion doesn't override other cookies by setting the same path/domain
HEAD:backend/onyx/auth/users.py:1287:                logger.debug("Deleted anonymous user cookie for user %s", user.email)
HEAD:backend/onyx/auth/users.py:1289:            logger.exception("Error deleting anonymous user cookie")
HEAD:backend/onyx/auth/users.py:1349:        get_marketing_posthog_cookie_name = fetch_ee_implementation_or_noop(
HEAD:backend/onyx/auth/users.py:1351:            attribute="get_marketing_posthog_cookie_name",
HEAD:backend/onyx/auth/users.py:1354:        parse_posthog_cookie = fetch_ee_implementation_or_noop(
HEAD:backend/onyx/auth/users.py:1356:            attribute="parse_posthog_cookie",
HEAD:backend/onyx/auth/users.py:1368:            and (marketing_cookie_name := get_marketing_posthog_cookie_name())
HEAD:backend/onyx/auth/users.py:1369:            and (marketing_cookie_value := request.cookies.get(marketing_cookie_name))
HEAD:backend/onyx/auth/users.py:1370:            and (parsed_cookie := parse_posthog_cookie(marketing_cookie_value))
HEAD:backend/onyx/auth/users.py:1372:            marketing_anonymous_id = parsed_cookie["distinct_id"]
HEAD:backend/onyx/auth/users.py:1388:            # Add all other values from the marketing cookie (featureFlags, etc.)
HEAD:backend/onyx/auth/users.py:1392:            ) in parsed_cookie.items():
HEAD:backend/onyx/auth/users.py:1642:# The cookie outlives the logical expiry by the grace window so a dead token is
HEAD:backend/onyx/auth/users.py:1645:cookie_transport = CookieTransport(
HEAD:backend/onyx/auth/users.py:1646:    cookie_max_age=SESSION_EXPIRE_TIME_SECONDS + SESSION_TOKEN_GRACE_PERIOD_SECONDS,
HEAD:backend/onyx/auth/users.py:1647:    cookie_secure=WEB_DOMAIN.startswith("https"),
HEAD:backend/onyx/auth/users.py:1648:    cookie_name=FASTAPI_USERS_AUTH_COOKIE_NAME,
HEAD:backend/onyx/auth/users.py:1651:# Native mobile clients can't use the HttpOnly auth cookie above, so they
HEAD:backend/onyx/auth/users.py:1652:# authenticate with the SAME stateful session token returned/refreshed as a
HEAD:backend/onyx/auth/users.py:1653:# Bearer value (Authorization header) via this transport. `tokenUrl` is only
HEAD:backend/onyx/auth/users.py:1654:# used for OpenAPI docs. The token itself is identical to the web cookie value
HEAD:backend/onyx/auth/users.py:1657:# API keys / PATs also ride in the Authorization header; for those the session
HEAD:backend/onyx/auth/users.py:1659:# Onyx's own API-key/PAT handlers (see `optional_user`).
HEAD:backend/onyx/auth/users.py:1660:bearer_transport = BearerTransport(tokenUrl="auth/mobile/login")
HEAD:backend/onyx/auth/users.py:1671:    async def refresh_token(self, token: Optional[str], user: Any) -> str:
HEAD:backend/onyx/auth/users.py:1685:    see ``onyx/auth/session_tokens.py``.
HEAD:backend/onyx/auth/users.py:1691:        key_prefix: str = REDIS_AUTH_KEY_PREFIX,
HEAD:backend/onyx/auth/users.py:1707:            build_session_token_value(
HEAD:backend/onyx/auth/users.py:1725:        if raw_value is None and not may_be_session_token(token):
HEAD:backend/onyx/auth/users.py:1726:            # Expected miss for API keys / PATs / JWTs on the bearer transport.
HEAD:backend/onyx/auth/users.py:1729:        result = classify_session_token_value(raw_value)
HEAD:backend/onyx/auth/users.py:1755:            ex=SESSION_TOKEN_GRACE_PERIOD_SECONDS,
HEAD:backend/onyx/auth/users.py:1758:    async def refresh_token(self, token: Optional[str], user: User) -> str:
HEAD:backend/onyx/auth/users.py:1768:        result = classify_session_token_value(raw_value)
HEAD:backend/onyx/auth/users.py:1777:            build_session_token_value(
HEAD:backend/onyx/auth/users.py:1794:        access_token_db: AccessTokenDatabase[AccessToken],
HEAD:backend/onyx/auth/users.py:1797:        super().__init__(access_token_db, lifetime_seconds)
HEAD:backend/onyx/auth/users.py:1798:        self._access_token_db = access_token_db
HEAD:backend/onyx/auth/users.py:1800:    async def refresh_token(self, token: Optional[str], user: User) -> str:
HEAD:backend/onyx/auth/users.py:1806:        access_token = await self._access_token_db.get_by_token(token)
HEAD:backend/onyx/auth/users.py:1808:        if access_token is None:
HEAD:backend/onyx/auth/users.py:1816:        await self._access_token_db.update(access_token, {"expires": new_expires})
HEAD:backend/onyx/auth/users.py:1869:    async def refresh_token(
HEAD:backend/onyx/auth/users.py:1883:    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
HEAD:backend/onyx/auth/users.py:1886:        access_token_db, lifetime_seconds=SESSION_EXPIRE_TIME_SECONDS
HEAD:backend/onyx/auth/users.py:1907:        name="redis", transport=cookie_transport, get_strategy=get_redis_strategy
HEAD:backend/onyx/auth/users.py:1911:        name="postgres", transport=cookie_transport, get_strategy=get_database_strategy
HEAD:backend/onyx/auth/users.py:1915:        name="jwt", transport=cookie_transport, get_strategy=get_jwt_strategy
HEAD:backend/onyx/auth/users.py:1921:# the exact same stateful session token as the cookie backend), but delivered
HEAD:backend/onyx/auth/users.py:1922:# as a Bearer token. fastapi-users namespaces router names by backend name
HEAD:backend/onyx/auth/users.py:1923:# (`auth:mobile-bearer.*`), so the mobile login/refresh/logout routers never
HEAD:backend/onyx/auth/users.py:1924:# collide with the cookie backend's routes.
HEAD:backend/onyx/auth/users.py:1926:    name="mobile-bearer",
HEAD:backend/onyx/auth/users.py:1927:    transport=bearer_transport,
HEAD:backend/onyx/auth/users.py:1939:        Provide a router for session token refreshing.
HEAD:backend/onyx/auth/users.py:1980:                supports_refresh = hasattr(strategy, "refresh_token") and callable(
HEAD:backend/onyx/auth/users.py:1981:                    getattr(strategy, "refresh_token")  # noqa: B009  # ods: ignore[getattr]
HEAD:backend/onyx/auth/users.py:1986:                        refresh_method = getattr(strategy, "refresh_token")  # noqa: B009  # ods: ignore[getattr]
HEAD:backend/onyx/auth/users.py:1989:                            "Successfully refreshed session token for user %s",
HEAD:backend/onyx/auth/users.py:1994:                        logger.error("Error refreshing session token: %s", str(e))
HEAD:backend/onyx/auth/users.py:2139:        if auth_header and auth_header.startswith("Bearer "):
HEAD:backend/onyx/auth/users.py:2140:            token = auth_header[len("Bearer ") :].strip()
HEAD:backend/onyx/auth/users.py:2161:    PT_OAUTH MCP tools and any custom HTTP tool with bearer pass-through forward
HEAD:backend/onyx/auth/users.py:2162:    `user.oauth_accounts[0].access_token` directly to the upstream service. The
HEAD:backend/onyx/auth/users.py:2165:    hook the stored access_token could rot at the IdP's lifetime (~1 h on
HEAD:backend/onyx/auth/users.py:2249:        elif hashed_api_key := get_hashed_api_key_from_request(request):
HEAD:backend/onyx/auth/users.py:2250:            api_key = await fetch_api_key_auth_result(hashed_api_key, async_db_session)
HEAD:backend/onyx/auth/users.py:2251:            if api_key is not None:
HEAD:backend/onyx/auth/users.py:2252:                user = api_key.user
HEAD:backend/onyx/auth/users.py:2254:                    UsageCredentialType.API_KEY,
HEAD:backend/onyx/auth/users.py:2255:                    str(api_key.api_key_id),
HEAD:backend/onyx/auth/users.py:2256:                    api_key.api_key_name,
HEAD:backend/onyx/auth/users.py:2257:                    api_key.api_key_display,
HEAD:backend/onyx/auth/users.py:2538:CSRF_TOKEN_COOKIE_NAME = "fastapiusersoauthcsrf"
HEAD:backend/onyx/auth/users.py:2539:PKCE_COOKIE_NAME_PREFIX = "fastapiusersoauthpkce"
HEAD:backend/onyx/auth/users.py:2560:def get_pkce_cookie_name(state: str) -> str:
HEAD:backend/onyx/auth/users.py:2562:    return f"{PKCE_COOKIE_NAME_PREFIX}_{state_hash}"
HEAD:backend/onyx/auth/users.py:2570:    csrf_token_cookie_name: str = CSRF_TOKEN_COOKIE_NAME,
HEAD:backend/onyx/auth/users.py:2580:            OnyxErrorCode.VALIDATION_ERROR, ErrorCode.ACCESS_TOKEN_DECODE_ERROR
HEAD:backend/onyx/auth/users.py:2584:            OnyxErrorCode.VALIDATION_ERROR, ErrorCode.ACCESS_TOKEN_ALREADY_EXPIRED
HEAD:backend/onyx/auth/users.py:2588:            OnyxErrorCode.VALIDATION_ERROR, ErrorCode.ACCESS_TOKEN_DECODE_ERROR
HEAD:backend/onyx/auth/users.py:2591:    cookie_csrf_token = request.cookies.get(csrf_token_cookie_name)
HEAD:backend/onyx/auth/users.py:2594:        not cookie_csrf_token
HEAD:backend/onyx/auth/users.py:2596:        or not secrets.compare_digest(cookie_csrf_token, state_csrf_token)
HEAD:backend/onyx/auth/users.py:2636:            token["access_token"]
HEAD:backend/onyx/auth/users.py:2673:            token["access_token"],
HEAD:backend/onyx/auth/users.py:2677:            token.get("refresh_token"),
HEAD:backend/onyx/auth/users.py:2697:    # session cookie. Gated on the signed-state marker so only mobile clients
HEAD:backend/onyx/auth/users.py:2702:        # audit still fire. No web response, so its anon-cookie cleanup no-ops.
HEAD:backend/onyx/auth/users.py:2715:    # Carry auth headers onto the redirect. Set-Cookie may repeat, so append each
HEAD:backend/onyx/auth/users.py:2719:        if header_name_lower == "set-cookie":
HEAD:backend/onyx/auth/users.py:2760:    csrf_token_cookie_name: str = CSRF_TOKEN_COOKIE_NAME,
HEAD:backend/onyx/auth/users.py:2761:    csrf_token_cookie_path: str = "/",
HEAD:backend/onyx/auth/users.py:2762:    csrf_token_cookie_domain: Optional[str] = None,
HEAD:backend/onyx/auth/users.py:2763:    csrf_token_cookie_secure: Optional[bool] = None,
HEAD:backend/onyx/auth/users.py:2764:    csrf_token_cookie_httponly: bool = True,
HEAD:backend/onyx/auth/users.py:2765:    csrf_token_cookie_samesite: Optional[Literal["lax", "strict", "none"]] = "lax",
HEAD:backend/onyx/auth/users.py:2783:    async def null_access_token_state() -> tuple[OAuth2Token, Optional[str]] | None:
HEAD:backend/onyx/auth/users.py:2786:    access_token_state_dependency = (
HEAD:backend/onyx/auth/users.py:2787:        oauth2_authorize_callback if not enable_pkce else null_access_token_state
HEAD:backend/onyx/auth/users.py:2790:    if csrf_token_cookie_secure is None:
HEAD:backend/onyx/auth/users.py:2791:        csrf_token_cookie_secure = WEB_DOMAIN.startswith("https")
HEAD:backend/onyx/auth/users.py:2804:        # signed state so the callback returns a PKCE one-time code, not a cookie.
HEAD:backend/onyx/auth/users.py:2809:        referral_source = request.cookies.get("referral_source", None)
HEAD:backend/onyx/auth/users.py:2832:        pkce_cookie: tuple[str, str] | None = None
HEAD:backend/onyx/auth/users.py:2836:            pkce_cookie_name = get_pkce_cookie_name(state)
HEAD:backend/onyx/auth/users.py:2837:            pkce_cookie = (pkce_cookie_name, code_verifier)
HEAD:backend/onyx/auth/users.py:2859:        def set_oauth_cookie(
HEAD:backend/onyx/auth/users.py:2865:            target_response.set_cookie(
HEAD:backend/onyx/auth/users.py:2869:                path=csrf_token_cookie_path,
HEAD:backend/onyx/auth/users.py:2870:                domain=csrf_token_cookie_domain,
HEAD:backend/onyx/auth/users.py:2871:                secure=csrf_token_cookie_secure,
HEAD:backend/onyx/auth/users.py:2872:                httponly=csrf_token_cookie_httponly,
HEAD:backend/onyx/auth/users.py:2873:                samesite=csrf_token_cookie_samesite,
HEAD:backend/onyx/auth/users.py:2876:        response_with_cookies: Response
HEAD:backend/onyx/auth/users.py:2878:            response_with_cookies = RedirectResponse(authorization_url, status_code=302)
HEAD:backend/onyx/auth/users.py:2880:            response_with_cookies = response
HEAD:backend/onyx/auth/users.py:2882:        set_oauth_cookie(
HEAD:backend/onyx/auth/users.py:2883:            response_with_cookies,
HEAD:backend/onyx/auth/users.py:2884:            key=csrf_token_cookie_name,
HEAD:backend/onyx/auth/users.py:2887:        if pkce_cookie is not None:
HEAD:backend/onyx/auth/users.py:2888:            pkce_cookie_name, code_verifier = pkce_cookie
HEAD:backend/onyx/auth/users.py:2889:            set_oauth_cookie(
HEAD:backend/onyx/auth/users.py:2890:                response_with_cookies,
HEAD:backend/onyx/auth/users.py:2891:                key=pkce_cookie_name,
HEAD:backend/onyx/auth/users.py:2896:            return response_with_cookies
HEAD:backend/onyx/auth/users.py:2927:        access_token_state: Tuple[OAuth2Token, Optional[str]] | None = Depends(
HEAD:backend/onyx/auth/users.py:2928:            access_token_state_dependency
HEAD:backend/onyx/auth/users.py:2936:        pkce_cookie_name: str | None = None
HEAD:backend/onyx/auth/users.py:2938:        def delete_pkce_cookie(response: Response) -> None:
HEAD:backend/onyx/auth/users.py:2939:            if enable_pkce and pkce_cookie_name:
HEAD:backend/onyx/auth/users.py:2940:                response.delete_cookie(
HEAD:backend/onyx/auth/users.py:2941:                    key=pkce_cookie_name,
HEAD:backend/onyx/auth/users.py:2942:                    path=csrf_token_cookie_path,
HEAD:backend/onyx/auth/users.py:2943:                    domain=csrf_token_cookie_domain,
HEAD:backend/onyx/auth/users.py:2944:                    secure=csrf_token_cookie_secure,
HEAD:backend/onyx/auth/users.py:2945:                    httponly=csrf_token_cookie_httponly,
HEAD:backend/onyx/auth/users.py:2946:                    samesite=csrf_token_cookie_samesite,
HEAD:backend/onyx/auth/users.py:2952:            delete_pkce_cookie(error_response)
HEAD:backend/onyx/auth/users.py:2960:                csrf_token_cookie_name=csrf_token_cookie_name,
HEAD:backend/onyx/auth/users.py:2970:                pkce_cookie_name = get_pkce_cookie_name(state)
HEAD:backend/onyx/auth/users.py:3002:            code_verifier = request.cookies.get(cast(str, pkce_cookie_name))
HEAD:backend/onyx/auth/users.py:3007:                        "Missing PKCE verifier cookie in OAuth callback",
HEAD:backend/onyx/auth/users.py:3017:                token = await oauth_client.get_access_token(
HEAD:backend/onyx/auth/users.py:3029:            if access_token_state is None:
HEAD:backend/onyx/auth/users.py:3033:            token, callback_state = access_token_state
HEAD:backend/onyx/auth/users.py:3058:            delete_pkce_cookie(redirect_response)
HEAD:backend/onyx/auth/utils.py:1:"""Shared authentication utilities for bearer token extraction and validation."""
HEAD:backend/onyx/auth/utils.py:9:    API_KEY_HEADER_ALTERNATIVE_NAME,
HEAD:backend/onyx/auth/utils.py:10:    API_KEY_HEADER_NAME,
HEAD:backend/onyx/auth/utils.py:11:    API_KEY_PREFIX,
HEAD:backend/onyx/auth/utils.py:12:    BEARER_PREFIX,
HEAD:backend/onyx/auth/utils.py:13:    DEPRECATED_API_KEY_PREFIX,
HEAD:backend/onyx/auth/utils.py:19:def get_hashed_bearer_token_from_request(
HEAD:backend/onyx/auth/utils.py:23:    allow_non_bearer: bool = False,
HEAD:backend/onyx/auth/utils.py:25:    """Generic extraction and hashing of bearer tokens from request headers.
HEAD:backend/onyx/auth/utils.py:30:        hash_fn: Function to hash the token (e.g., hash_api_key or hash_pat)
HEAD:backend/onyx/auth/utils.py:31:        allow_non_bearer: If True, accept raw tokens without "Bearer " prefix
HEAD:backend/onyx/auth/utils.py:37:        API_KEY_HEADER_ALTERNATIVE_NAME
HEAD:backend/onyx/auth/utils.py:38:    ) or request.headers.get(API_KEY_HEADER_NAME)
HEAD:backend/onyx/auth/utils.py:43:    # Handle bearer format
HEAD:backend/onyx/auth/utils.py:44:    if auth_header.startswith(BEARER_PREFIX):
HEAD:backend/onyx/auth/utils.py:45:        token = auth_header[len(BEARER_PREFIX) :].strip()
HEAD:backend/onyx/auth/utils.py:46:    elif allow_non_bearer:
HEAD:backend/onyx/auth/utils.py:60:def _extract_tenant_from_bearer_token(
HEAD:backend/onyx/auth/utils.py:63:    """Generic tenant extraction from bearer token. Returns None if invalid format.
HEAD:backend/onyx/auth/utils.py:73:        API_KEY_HEADER_ALTERNATIVE_NAME
HEAD:backend/onyx/auth/utils.py:74:    ) or request.headers.get(API_KEY_HEADER_NAME)
HEAD:backend/onyx/auth/utils.py:76:    if not auth_header or not auth_header.startswith(BEARER_PREFIX):
HEAD:backend/onyx/auth/utils.py:79:    token = auth_header[len(BEARER_PREFIX) :].strip()
HEAD:backend/onyx/auth/utils.py:101:    """Extract tenant ID from an API key, PAT, or SCIM token header.
HEAD:backend/onyx/auth/utils.py:103:    Unified function for extracting tenant from any bearer token.
HEAD:backend/onyx/auth/utils.py:109:    return _extract_tenant_from_bearer_token(
HEAD:backend/onyx/auth/utils.py:111:        [API_KEY_PREFIX, DEPRECATED_API_KEY_PREFIX, PAT_PREFIX, SCIM_TOKEN_PREFIX],
HEAD:backend/onyx/db/api_key.py:9:from onyx.auth.api_key import (
HEAD:backend/onyx/db/api_key.py:10:    ApiKeyDescriptor,
HEAD:backend/onyx/db/api_key.py:11:    build_displayable_api_key,
HEAD:backend/onyx/db/api_key.py:12:    generate_api_key,
HEAD:backend/onyx/db/api_key.py:13:    hash_api_key,
HEAD:backend/onyx/db/api_key.py:16:    DANSWER_API_KEY_DUMMY_EMAIL_DOMAIN,
HEAD:backend/onyx/db/api_key.py:17:    DANSWER_API_KEY_PREFIX,
HEAD:backend/onyx/db/api_key.py:21:from onyx.db.models import ApiKey, User
HEAD:backend/onyx/db/api_key.py:31:from onyx.server.api_key.models import APIKeyArgs
HEAD:backend/onyx/db/api_key.py:39:class ApiKeyAuthResult(NamedTuple):
HEAD:backend/onyx/db/api_key.py:41:    api_key_id: int
HEAD:backend/onyx/db/api_key.py:42:    api_key_name: str | None
HEAD:backend/onyx/db/api_key.py:43:    api_key_display: str
HEAD:backend/onyx/db/api_key.py:46:def get_api_key_email_pattern() -> str:
HEAD:backend/onyx/db/api_key.py:47:    return DANSWER_API_KEY_DUMMY_EMAIL_DOMAIN
HEAD:backend/onyx/db/api_key.py:50:def is_api_key_email_address(email: str) -> bool:
HEAD:backend/onyx/db/api_key.py:51:    return email.endswith(get_api_key_email_pattern())
HEAD:backend/onyx/db/api_key.py:54:def fetch_api_keys(db_session: Session) -> list[ApiKeyDescriptor]:
HEAD:backend/onyx/db/api_key.py:55:    api_keys = (
HEAD:backend/onyx/db/api_key.py:56:        db_session.scalars(select(ApiKey).options(joinedload(ApiKey.user)))
HEAD:backend/onyx/db/api_key.py:62:        [api_key.user_id for api_key in api_keys],
HEAD:backend/onyx/db/api_key.py:66:        ApiKeyDescriptor(
HEAD:backend/onyx/db/api_key.py:67:            api_key_id=api_key.id,
HEAD:backend/onyx/db/api_key.py:68:            api_key_display=api_key.api_key_display,
HEAD:backend/onyx/db/api_key.py:69:            api_key_name=api_key.name,
HEAD:backend/onyx/db/api_key.py:70:            user_id=api_key.user_id,
HEAD:backend/onyx/db/api_key.py:73:                for gid, gname in groups_by_user.get(api_key.user_id, [])
HEAD:backend/onyx/db/api_key.py:76:        for api_key in api_keys
HEAD:backend/onyx/db/api_key.py:80:def fetch_api_key(db_session: Session, api_key_id: int) -> ApiKeyDescriptor | None:
HEAD:backend/onyx/db/api_key.py:81:    api_key = db_session.scalar(
HEAD:backend/onyx/db/api_key.py:82:        select(ApiKey).options(joinedload(ApiKey.user)).where(ApiKey.id == api_key_id)
HEAD:backend/onyx/db/api_key.py:84:    if api_key is None:
HEAD:backend/onyx/db/api_key.py:88:        db_session, [api_key.user_id], include_default=True
HEAD:backend/onyx/db/api_key.py:90:    return ApiKeyDescriptor(
HEAD:backend/onyx/db/api_key.py:91:        api_key_id=api_key.id,
HEAD:backend/onyx/db/api_key.py:92:        api_key_display=api_key.api_key_display,
HEAD:backend/onyx/db/api_key.py:93:        api_key_name=api_key.name,
HEAD:backend/onyx/db/api_key.py:94:        user_id=api_key.user_id,
HEAD:backend/onyx/db/api_key.py:97:            for gid, gname in groups_by_user.get(api_key.user_id, [])
HEAD:backend/onyx/db/api_key.py:102:async def fetch_user_for_api_key(
HEAD:backend/onyx/db/api_key.py:103:    hashed_api_key: str, async_db_session: AsyncSession
HEAD:backend/onyx/db/api_key.py:109:        .join(ApiKey, ApiKey.user_id == User.id)
HEAD:backend/onyx/db/api_key.py:110:        .where(ApiKey.hashed_api_key == hashed_api_key)
HEAD:backend/onyx/db/api_key.py:114:async def fetch_api_key_auth_result(
HEAD:backend/onyx/db/api_key.py:115:    hashed_api_key: str, async_db_session: AsyncSession
HEAD:backend/onyx/db/api_key.py:116:) -> ApiKeyAuthResult | None:
HEAD:backend/onyx/db/api_key.py:120:                select(ApiKey)
HEAD:backend/onyx/db/api_key.py:121:                .join(ApiKey.user)
HEAD:backend/onyx/db/api_key.py:123:                .options(contains_eager(ApiKey.user))
HEAD:backend/onyx/db/api_key.py:124:                .where(ApiKey.hashed_api_key == hashed_api_key)
HEAD:backend/onyx/db/api_key.py:133:    return ApiKeyAuthResult(
HEAD:backend/onyx/db/api_key.py:135:        api_key_id=row.id,
HEAD:backend/onyx/db/api_key.py:136:        api_key_name=row.name,
HEAD:backend/onyx/db/api_key.py:137:        api_key_display=row.api_key_display,
HEAD:backend/onyx/db/api_key.py:141:def get_api_key_fake_email(
HEAD:backend/onyx/db/api_key.py:145:    return f"{DANSWER_API_KEY_PREFIX}{name}@{unique_id}{DANSWER_API_KEY_DUMMY_EMAIL_DOMAIN}"
HEAD:backend/onyx/db/api_key.py:148:def insert_api_key(
HEAD:backend/onyx/db/api_key.py:149:    db_session: Session, api_key_args: APIKeyArgs, user_id: uuid.UUID | None
HEAD:backend/onyx/db/api_key.py:150:) -> ApiKeyDescriptor:
HEAD:backend/onyx/db/api_key.py:156:    api_key = generate_api_key(tenant_id)
HEAD:backend/onyx/db/api_key.py:157:    api_key_user_id = uuid.uuid4()
HEAD:backend/onyx/db/api_key.py:159:    display_name = api_key_args.name or UNNAMED_KEY_PLACEHOLDER
HEAD:backend/onyx/db/api_key.py:160:    api_key_user_row = User(
HEAD:backend/onyx/db/api_key.py:161:        id=api_key_user_id,
HEAD:backend/onyx/db/api_key.py:162:        email=get_api_key_fake_email(display_name, str(api_key_user_id)),
HEAD:backend/onyx/db/api_key.py:170:    db_session.add(api_key_user_row)
HEAD:backend/onyx/db/api_key.py:172:    api_key_row = ApiKey(
HEAD:backend/onyx/db/api_key.py:173:        name=api_key_args.name,
HEAD:backend/onyx/db/api_key.py:174:        hashed_api_key=hash_api_key(api_key),
HEAD:backend/onyx/db/api_key.py:175:        api_key_display=build_displayable_api_key(api_key),
HEAD:backend/onyx/db/api_key.py:176:        user_id=api_key_user_id,
HEAD:backend/onyx/db/api_key.py:179:    db_session.add(api_key_row)
HEAD:backend/onyx/db/api_key.py:182:    set_user_groups__no_commit(db_session, api_key_user_id, api_key_args.group_ids)
HEAD:backend/onyx/db/api_key.py:186:    return ApiKeyDescriptor(
HEAD:backend/onyx/db/api_key.py:187:        api_key_id=api_key_row.id,
HEAD:backend/onyx/db/api_key.py:188:        api_key_display=api_key_row.api_key_display,
HEAD:backend/onyx/db/api_key.py:189:        api_key=api_key,
HEAD:backend/onyx/db/api_key.py:190:        api_key_name=api_key_args.name,
HEAD:backend/onyx/db/api_key.py:191:        user_id=api_key_user_id,
HEAD:backend/onyx/db/api_key.py:192:        groups=get_user_groups(db_session, api_key_user_id, include_default=True),
HEAD:backend/onyx/db/api_key.py:196:def update_api_key(
HEAD:backend/onyx/db/api_key.py:197:    db_session: Session, api_key_id: int, api_key_args: APIKeyArgs
HEAD:backend/onyx/db/api_key.py:198:) -> ApiKeyDescriptor:
HEAD:backend/onyx/db/api_key.py:199:    existing_api_key = db_session.scalar(select(ApiKey).where(ApiKey.id == api_key_id))
HEAD:backend/onyx/db/api_key.py:200:    if existing_api_key is None:
HEAD:backend/onyx/db/api_key.py:202:            OnyxErrorCode.NOT_FOUND, f"API key with id {api_key_id} does not exist"
HEAD:backend/onyx/db/api_key.py:205:    existing_api_key.name = api_key_args.name
HEAD:backend/onyx/db/api_key.py:206:    api_key_user = db_session.scalar(
HEAD:backend/onyx/db/api_key.py:208:            User.id == existing_api_key.user_id  # ty: ignore[invalid-argument-type]
HEAD:backend/onyx/db/api_key.py:211:    if api_key_user is None:
HEAD:backend/onyx/db/api_key.py:212:        raise RuntimeError("API Key does not have associated user.")
```
Static source contains multiple token/session-related mechanisms.
Their active use depends on deployment and configuration.
## Request / Route Context Examples
Evidence lines: 500
```text
HEAD:backend/ee/onyx/server/analytics/api.py:5:from fastapi import APIRouter, Depends
HEAD:backend/ee/onyx/server/analytics/api.py:28:router = APIRouter(prefix="/analytics", tags=PUBLIC_API_TAGS)
HEAD:backend/ee/onyx/server/analytics/api.py:53:@router.get("/admin/query")
HEAD:backend/ee/onyx/server/analytics/api.py:57:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:85:@router.get("/admin/user")
HEAD:backend/ee/onyx/server/analytics/api.py:89:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:120:@router.get("/admin/onyxbot")
HEAD:backend/ee/onyx/server/analytics/api.py:124:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/analytics/api.py:156:@router.get("/admin/persona/messages")
HEAD:backend/ee/onyx/server/analytics/api.py:161:    user: User = Depends(require_permission(Permission.READ_AGENT_ANALYTICS)),
HEAD:backend/ee/onyx/server/analytics/api.py:196:@router.get("/admin/persona/unique-users")
HEAD:backend/ee/onyx/server/analytics/api.py:201:    user: User = Depends(require_permission(Permission.READ_AGENT_ANALYTICS)),
HEAD:backend/ee/onyx/server/analytics/api.py:236:@router.get("/assistant/{assistant_id}/stats")
HEAD:backend/ee/onyx/server/analytics/api.py:241:    user: User = Depends(require_permission(Permission.READ_AGENT_ANALYTICS)),
HEAD:backend/ee/onyx/server/billing/api.py:27:from fastapi import APIRouter, Depends
HEAD:backend/ee/onyx/server/billing/api.py:79:router = APIRouter(prefix="/admin/billing")
HEAD:backend/ee/onyx/server/billing/api.py:168:@router.post("/create-checkout-session")
HEAD:backend/ee/onyx/server/billing/api.py:171:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:218:@router.post("/create-customer-portal-session")
HEAD:backend/ee/onyx/server/billing/api.py:221:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:282:@router.get("/billing-information")
HEAD:backend/ee/onyx/server/billing/api.py:284:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:357:@router.post("/seats/update")
HEAD:backend/ee/onyx/server/billing/api.py:360:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:404:@router.post("/end-trial")
HEAD:backend/ee/onyx/server/billing/api.py:406:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/billing/api.py:433:@router.get("/stripe-publishable-key")
HEAD:backend/ee/onyx/server/billing/api.py:502:@router.post("/reset-connection")
HEAD:backend/ee/onyx/server/billing/api.py:504:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/documents/cc_pair.py:3:from fastapi import APIRouter, Depends
HEAD:backend/ee/onyx/server/documents/cc_pair.py:29:router = APIRouter(prefix="/manage")
HEAD:backend/ee/onyx/server/documents/cc_pair.py:32:@router.get("/admin/cc-pair/{cc_pair_id}/sync-permissions")
HEAD:backend/ee/onyx/server/documents/cc_pair.py:35:    user: User = Depends(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:55:@router.post("/admin/cc-pair/{cc_pair_id}/sync-permissions")
HEAD:backend/ee/onyx/server/documents/cc_pair.py:58:    user: User = Depends(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:111:@router.get("/admin/cc-pair/{cc_pair_id}/sync-groups")
HEAD:backend/ee/onyx/server/documents/cc_pair.py:114:    user: User = Depends(
HEAD:backend/ee/onyx/server/documents/cc_pair.py:134:@router.post("/admin/cc-pair/{cc_pair_id}/sync-groups")
HEAD:backend/ee/onyx/server/documents/cc_pair.py:137:    user: User = Depends(
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:5:from fastapi import APIRouter, Depends, HTTPException, Response, UploadFile, status
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:35:    current_user_with_expired_token,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:54:admin_router = APIRouter(prefix="/admin/enterprise-settings")
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:55:basic_router = APIRouter(prefix="/enterprise-settings")
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:125:    user: User = Depends(current_user_with_expired_token),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:201:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:240:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:316:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:350:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:380:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/evals/api.py:1:from fastapi import APIRouter, Depends
HEAD:backend/ee/onyx/server/evals/api.py:13:router = APIRouter(prefix="/evals")
HEAD:backend/ee/onyx/server/evals/api.py:16:@router.post("/eval_run", response_model=EvalRunAck)
HEAD:backend/ee/onyx/server/evals/api.py:19:    user: User = Depends(current_cloud_superuser),  # noqa: ARG001
HEAD:backend/ee/onyx/server/features/hooks/api.py:2:from fastapi import APIRouter, Depends, Query
HEAD:backend/ee/onyx/server/features/hooks/api.py:190:router = APIRouter(prefix="/admin/hooks")
HEAD:backend/ee/onyx/server/features/hooks/api.py:198:@router.get("/specs")
HEAD:backend/ee/onyx/server/features/hooks/api.py:200:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:219:@router.get("")
HEAD:backend/ee/onyx/server/features/hooks/api.py:221:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:229:@router.post("")
HEAD:backend/ee/onyx/server/features/hooks/api.py:232:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:265:@router.get("/{hook_id}")
HEAD:backend/ee/onyx/server/features/hooks/api.py:268:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:276:@router.patch("/{hook_id}")
HEAD:backend/ee/onyx/server/features/hooks/api.py:280:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:351:@router.delete("/{hook_id}")
HEAD:backend/ee/onyx/server/features/hooks/api.py:354:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:362:@router.post("/{hook_id}/activate")
HEAD:backend/ee/onyx/server/features/hooks/api.py:365:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:404:@router.post("/{hook_id}/validate")
HEAD:backend/ee/onyx/server/features/hooks/api.py:407:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:432:@router.post("/{hook_id}/deactivate")
HEAD:backend/ee/onyx/server/features/hooks/api.py:435:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/features/hooks/api.py:454:@router.get("/{hook_id}/execution-logs")
HEAD:backend/ee/onyx/server/features/hooks/api.py:458:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/gateway/api.py:11:from fastapi import APIRouter, Depends, Request, Response
HEAD:backend/ee/onyx/server/gateway/api.py:133:router = APIRouter(prefix=GATEWAY_PATH_PREFIX)
HEAD:backend/ee/onyx/server/gateway/api.py:1392:@router.get("/v1/models")
HEAD:backend/ee/onyx/server/gateway/api.py:1395:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1404:@router.post("/v1/chat/completions")
HEAD:backend/ee/onyx/server/gateway/api.py:1408:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1428:@router.post("/v1/responses")
HEAD:backend/ee/onyx/server/gateway/api.py:1432:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1458:@router.post("/v1/messages")
HEAD:backend/ee/onyx/server/gateway/api.py:1462:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/gateway/api.py:1491:@router.post("/v1/messages/count_tokens")
HEAD:backend/ee/onyx/server/gateway/api.py:1495:    user: User = Depends(require_permission(Permission.USE_LLM_GATEWAY)),
HEAD:backend/ee/onyx/server/license/api.py:14:from fastapi import APIRouter, Depends, File, UploadFile
HEAD:backend/ee/onyx/server/license/api.py:50:router = APIRouter(prefix="/license")
HEAD:backend/ee/onyx/server/license/api.py:53:@router.get("")
HEAD:backend/ee/onyx/server/license/api.py:55:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:79:@router.get("/seats")
HEAD:backend/ee/onyx/server/license/api.py:81:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:101:@router.post("/claim")
HEAD:backend/ee/onyx/server/license/api.py:104:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:181:@router.post("/upload")
HEAD:backend/ee/onyx/server/license/api.py:184:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:218:@router.post("/refresh")
HEAD:backend/ee/onyx/server/license/api.py:220:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/license/api.py:249:@router.delete("")
HEAD:backend/ee/onyx/server/license/api.py:251:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/log_export/api.py:7:from fastapi import APIRouter, Depends
HEAD:backend/ee/onyx/server/log_export/api.py:46:router = APIRouter()
HEAD:backend/ee/onyx/server/log_export/api.py:134:@router.post("/admin/log-export")
HEAD:backend/ee/onyx/server/log_export/api.py:136:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/log_export/api.py:236:@router.get("/admin/log-export/{export_id}")
HEAD:backend/ee/onyx/server/log_export/api.py:239:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/log_export/api.py:265:@router.get("/admin/log-export/{export_id}/download")
HEAD:backend/ee/onyx/server/log_export/api.py:268:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:1:from fastapi import APIRouter, Depends, HTTPException
HEAD:backend/ee/onyx/server/manage/standard_answer.py:27:router = APIRouter(prefix="/manage")
HEAD:backend/ee/onyx/server/manage/standard_answer.py:30:@router.post("/admin/standard-answer")
HEAD:backend/ee/onyx/server/manage/standard_answer.py:34:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:47:@router.get("/admin/standard-answer")
HEAD:backend/ee/onyx/server/manage/standard_answer.py:50:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:59:@router.patch("/admin/standard-answer/{standard_answer_id}")
HEAD:backend/ee/onyx/server/manage/standard_answer.py:64:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:86:@router.delete("/admin/standard-answer/{standard_answer_id}")
HEAD:backend/ee/onyx/server/manage/standard_answer.py:90:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:98:@router.post("/admin/standard-answer/category")
HEAD:backend/ee/onyx/server/manage/standard_answer.py:102:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:111:@router.get("/admin/standard-answer/category")
HEAD:backend/ee/onyx/server/manage/standard_answer.py:114:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:125:@router.patch("/admin/standard-answer/category/{standard_answer_category_id}")
HEAD:backend/ee/onyx/server/manage/standard_answer.py:130:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/manage/standard_answer.py:150:@router.delete("/admin/standard-answer/category/{standard_answer_category_id}")
HEAD:backend/ee/onyx/server/manage/standard_answer.py:154:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/oauth/api.py:23:@router.post("/prepare-authorization-request")
HEAD:backend/ee/onyx/server/oauth/api.py:27:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/api_router.py:1:from fastapi import APIRouter
HEAD:backend/ee/onyx/server/oauth/api_router.py:3:router: APIRouter = APIRouter(prefix="/oauth")
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:145:@router.post("/connector/confluence/callback")
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:149:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:258:@router.get("/connector/confluence/accessible-resources")
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:261:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:322:@router.post("/connector/confluence/finalize")
HEAD:backend/ee/onyx/server/oauth/confluence_cloud.py:328:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/google_drive.py:110:@router.post("/connector/google-drive/callback")
HEAD:backend/ee/onyx/server/oauth/google_drive.py:114:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/oauth/slack.py:99:@router.post("/connector/slack/callback")
HEAD:backend/ee/onyx/server/oauth/slack.py:103:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/ee/onyx/server/query_and_chat/query_backend.py:1:from fastapi import APIRouter, Depends, HTTPException
HEAD:backend/ee/onyx/server/query_and_chat/query_backend.py:19:basic_router = APIRouter(prefix="/query")
HEAD:backend/ee/onyx/server/query_and_chat/query_backend.py:26:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:14:from fastapi import APIRouter, Depends, HTTPException
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:50:router = APIRouter(prefix="/search")
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:53:@router.post("/search-flow-classification", tags=PUBLIC_API_TAGS)
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:56:    _: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:96:@router.post(
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:124:    user: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:170:@router.get("/search-history", tags=PUBLIC_API_TAGS)
HEAD:backend/ee/onyx/server/query_and_chat/search_backend.py:174:    user: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/ee/onyx/server/query_history/api.py:7:from fastapi import APIRouter, Depends, HTTPException, Query
HEAD:backend/ee/onyx/server/query_history/api.py:56:router = APIRouter()
HEAD:backend/ee/onyx/server/query_history/api.py:158:@router.get("/admin/chat-sessions")
HEAD:backend/ee/onyx/server/query_history/api.py:161:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:203:@router.get("/admin/chat-session-history")
HEAD:backend/ee/onyx/server/query_history/api.py:210:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:247:@router.get("/admin/chat-session-history/{chat_session_id}")
HEAD:backend/ee/onyx/server/query_history/api.py:250:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:283:@router.get("/admin/query-history/list")
HEAD:backend/ee/onyx/server/query_history/api.py:285:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:311:@router.post("/admin/query-history/start-export", tags=PUBLIC_API_TAGS)
HEAD:backend/ee/onyx/server/query_history/api.py:313:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:357:@router.get("/admin/query-history/export-status", tags=PUBLIC_API_TAGS)
HEAD:backend/ee/onyx/server/query_history/api.py:360:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/query_history/api.py:391:@router.get("/admin/query-history/download", tags=PUBLIC_API_TAGS)
HEAD:backend/ee/onyx/server/query_history/api.py:394:    _: User = Depends(require_permission(Permission.READ_QUERY_HISTORY)),
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:5:from fastapi import APIRouter, Depends, HTTPException, Response
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:27:router = APIRouter()
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:36:@router.post("/admin/usage-report", status_code=204)
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:39:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:71:@router.get("/admin/usage-report/{report_name}")
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:74:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:96:@router.get("/admin/usage-report")
HEAD:backend/ee/onyx/server/reporting/usage_export_api.py:98:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/scim/api.py:18:from fastapi import APIRouter, Depends, FastAPI, Query, Request, Response
HEAD:backend/ee/onyx/server/scim/api.py:153:scim_router = APIRouter(prefix="/scim/v2", tags=["SCIM"])
HEAD:backend/ee/onyx/server/tenants/admin_api.py:1:from fastapi import APIRouter, Depends, HTTPException, Response
HEAD:backend/ee/onyx/server/tenants/admin_api.py:23:router = APIRouter(prefix="/tenants")
HEAD:backend/ee/onyx/server/tenants/admin_api.py:26:@router.post("/impersonate")
HEAD:backend/ee/onyx/server/tenants/admin_api.py:29:    superuser: User = Depends(current_cloud_superuser),
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:1:from fastapi import APIRouter, Depends, HTTPException, Response
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:25:router = APIRouter(prefix="/tenants")
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:28:@router.get("/anonymous-user-path")
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:30:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:43:@router.post("/anonymous-user-path")
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:46:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:70:@router.post("/anonymous-user")
HEAD:backend/ee/onyx/server/tenants/api.py:1:from fastapi import APIRouter
HEAD:backend/ee/onyx/server/tenants/api.py:19:) -> APIRouter:
HEAD:backend/ee/onyx/server/tenants/api.py:29:    router = APIRouter()
HEAD:backend/ee/onyx/server/tenants/billing_api.py:22:from fastapi import APIRouter, Depends
HEAD:backend/ee/onyx/server/tenants/billing_api.py:71:router = APIRouter(prefix="/tenants")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:78:@router.post("/product-gating")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:98:@router.post("/product-gating/full-sync")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:118:@router.post("/tier-update")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:146:@router.get("/billing-information")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:148:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:155:@router.post("/seats/update")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:158:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:165:@router.post("/create-customer-portal-session")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:167:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:186:@router.post("/create-checkout-session")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:189:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:209:@router.post("/create-subscription-session")
HEAD:backend/ee/onyx/server/tenants/billing_api.py:212:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/billing_api.py:237:@router.get("/stripe-publishable-key")
HEAD:backend/ee/onyx/server/tenants/proxy.py:25:from fastapi import APIRouter, Depends, Header, HTTPException
HEAD:backend/ee/onyx/server/tenants/proxy.py:44:router = APIRouter(prefix="/proxy")
HEAD:backend/ee/onyx/server/tenants/proxy.py:242:@router.post("/create-checkout-session")
HEAD:backend/ee/onyx/server/tenants/proxy.py:287:@router.post("/claim-license")
HEAD:backend/ee/onyx/server/tenants/proxy.py:332:@router.post("/create-customer-portal-session")
HEAD:backend/ee/onyx/server/tenants/proxy.py:374:@router.get("/billing-information")
HEAD:backend/ee/onyx/server/tenants/proxy.py:445:@router.get("/license/{tenant_id}")
HEAD:backend/ee/onyx/server/tenants/proxy.py:480:@router.post("/seats/update")
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:1:from fastapi import APIRouter, Depends, HTTPException
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:21:router = APIRouter(prefix="/tenants")
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:24:@router.post("/leave-team")
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:27:    current_user: User = Depends(
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:34:    if current_user.email != user_email.user_email:
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:1:from fastapi import APIRouter, Depends
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:13:router = APIRouter(prefix="/tenants")
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:27:@router.get("/existing-team-by-domain")
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:29:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:1:from fastapi import APIRouter, Depends, HTTPException
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:35:router = APIRouter(prefix="/tenants")
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:64:@router.post("/users/invite/request")
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:67:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:81:@router.get("/users/pending")
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:83:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:89:@router.post("/users/invite/approve")
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:92:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:106:@router.post("/users/invite/accept")
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:109:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:128:@router.post("/users/invite/deny")
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:131:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:3:from fastapi import APIRouter, Depends
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:43:router = APIRouter(prefix="/admin/token-rate-limits", tags=PUBLIC_API_TAGS)
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:51:@router.get("/global")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:53:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:62:@router.post("/global")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:65:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:81:@router.put("/rate-limit/{token_rate_limit_id}")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:85:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:100:@router.delete("/rate-limit/{token_rate_limit_id}")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:103:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:119:@router.get("/user-groups")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:121:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:137:@router.get("/user-group/{group_id}")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:140:    user: User = Depends(
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:157:@router.post("/user-group/{group_id}")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:161:    user: User = Depends(
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:236:@router.put("/user-group/{group_id}/rate-limit/{rate_limit_id}")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:241:    user: User = Depends(
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:260:@router.delete("/user-group/{group_id}/rate-limit/{rate_limit_id}")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:264:    user: User = Depends(
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:281:@router.get("/users")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:283:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:292:@router.post("/users")
HEAD:backend/ee/onyx/server/token_rate_limits/api.py:295:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:1:from fastapi import APIRouter, Depends
HEAD:backend/ee/onyx/server/user_group/api.py:80:router = APIRouter(prefix="/manage", tags=PUBLIC_API_TAGS)
HEAD:backend/ee/onyx/server/user_group/api.py:83:@router.get("/admin/user-group")
HEAD:backend/ee/onyx/server/user_group/api.py:86:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:136:@router.get("/admin/user-group/{user_group_id}")
HEAD:backend/ee/onyx/server/user_group/api.py:139:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:171:@router.get("/user-groups/minimal")
HEAD:backend/ee/onyx/server/user_group/api.py:174:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:194:@router.get("/admin/permissions/registry")
HEAD:backend/ee/onyx/server/user_group/api.py:196:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:201:@router.get("/admin/user-group/{user_group_id}/permissions")
HEAD:backend/ee/onyx/server/user_group/api.py:205:    _: User = Depends(require_permission(Permission.MANAGE_USER_GROUPS)),
HEAD:backend/ee/onyx/server/user_group/api.py:221:@router.put("/admin/user-group/{user_group_id}/permissions")
HEAD:backend/ee/onyx/server/user_group/api.py:225:    user: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:268:@router.post("/admin/user-group")
HEAD:backend/ee/onyx/server/user_group/api.py:271:    user: User = Depends(require_permission(Permission.MANAGE_USER_GROUPS)),
HEAD:backend/ee/onyx/server/user_group/api.py:302:@router.patch("/admin/user-group/rename")
HEAD:backend/ee/onyx/server/user_group/api.py:305:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:347:@router.patch("/admin/user-group/{user_group_id}/incognito")
HEAD:backend/ee/onyx/server/user_group/api.py:351:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/ee/onyx/server/user_group/api.py:372:@router.patch("/admin/user-group/{user_group_id}")
HEAD:backend/ee/onyx/server/user_group/api.py:376:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:395:@router.post("/admin/user-group/{user_group_id}/add-users")
HEAD:backend/ee/onyx/server/user_group/api.py:399:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:418:@router.delete("/admin/user-group/{user_group_id}")
HEAD:backend/ee/onyx/server/user_group/api.py:421:    user: User = Depends(require_permission(Permission.MANAGE_USER_GROUPS)),
HEAD:backend/ee/onyx/server/user_group/api.py:456:@router.patch("/admin/user-group/{user_group_id}/agents")
HEAD:backend/ee/onyx/server/user_group/api.py:460:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:526:@router.patch("/admin/user-group/{user_group_id}/document-sets")
HEAD:backend/ee/onyx/server/user_group/api.py:530:    user: User = Depends(
HEAD:backend/ee/onyx/server/user_group/api.py:613:@router.put("/admin/user-group/{user_group_id}/manager")
HEAD:backend/ee/onyx/server/user_group/api.py:617:    user: User = Depends(
HEAD:backend/onyx/server/api_key/api.py:1:from fastapi import APIRouter, Depends
HEAD:backend/onyx/server/api_key/api.py:27:router = APIRouter(prefix="/admin/api-key")
HEAD:backend/onyx/server/api_key/api.py:30:@router.get("")
HEAD:backend/onyx/server/api_key/api.py:32:    _: User = Depends(require_permission(Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS)),
HEAD:backend/onyx/server/api_key/api.py:38:@router.get("/{api_key_id}")
HEAD:backend/onyx/server/api_key/api.py:41:    _: User = Depends(require_permission(Permission.MANAGE_SERVICE_ACCOUNT_API_KEYS)),
HEAD:backend/onyx/server/api_key/api.py:52:@router.post("")
HEAD:backend/onyx/server/api_key/api.py:55:    user: User = Depends(
HEAD:backend/onyx/server/api_key/api.py:74:@router.post("/{api_key_id}/regenerate")
HEAD:backend/onyx/server/api_key/api.py:77:    user: User = Depends(
HEAD:backend/onyx/server/api_key/api.py:93:@router.patch("/{api_key_id}")
HEAD:backend/onyx/server/api_key/api.py:97:    user: User = Depends(
HEAD:backend/onyx/server/api_key/api.py:116:@router.delete("/{api_key_id}")
HEAD:backend/onyx/server/api_key/api.py:119:    user: User = Depends(
HEAD:backend/onyx/server/auth/captcha_api.py:17:from fastapi import APIRouter, Request, Response
HEAD:backend/onyx/server/auth/captcha_api.py:42:router = APIRouter(prefix="/auth/captcha", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/auth/captcha_api.py:60:@router.post("/oauth-verify")
HEAD:backend/onyx/server/auth/mobile.py:16:from fastapi import APIRouter
HEAD:backend/onyx/server/auth/mobile.py:30:router = APIRouter()
HEAD:backend/onyx/server/auth/mobile.py:48:@router.post("/sso/exchange")
HEAD:backend/onyx/server/auth_check.py:10:    current_user,
HEAD:backend/onyx/server/auth_check.py:11:    current_user_from_websocket,
HEAD:backend/onyx/server/auth_check.py:12:    current_user_with_expired_token,
HEAD:backend/onyx/server/auth_check.py:172:                    or depends_fn == current_user
HEAD:backend/onyx/server/auth_check.py:173:                    or depends_fn == current_user_with_expired_token
HEAD:backend/onyx/server/auth_check.py:175:                    or depends_fn == current_user_from_websocket
HEAD:backend/onyx/server/documents/cc_pair.py:4:from fastapi import APIRouter, Depends, Query
HEAD:backend/onyx/server/documents/cc_pair.py:98:router = APIRouter(prefix="/manage")
HEAD:backend/onyx/server/documents/cc_pair.py:117:@router.get("/admin/cc-pair/{cc_pair_id}/index-attempts", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/cc_pair.py:122:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:159:@router.get("/admin/index-attempt/{index_attempt_id}/stage-metrics")
HEAD:backend/onyx/server/documents/cc_pair.py:162:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:234:@router.get("/admin/cc-pair/{cc_pair_id}/permission-sync-attempts")
HEAD:backend/onyx/server/documents/cc_pair.py:239:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:284:@router.get("/admin/cc-pair/{cc_pair_id}/external-group-sync-attempts")
HEAD:backend/onyx/server/documents/cc_pair.py:289:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:337:@router.get("/admin/cc-pair/{cc_pair_id}", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/cc_pair.py:340:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:362:    is_editable_for_current_user = editable_cc_pair is not None
HEAD:backend/onyx/server/documents/cc_pair.py:430:        is_editable_for_current_user=is_editable_for_current_user,
HEAD:backend/onyx/server/documents/cc_pair.py:469:@router.put("/admin/cc-pair/{cc_pair_id}/status", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/cc_pair.py:473:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:576:@router.put("/admin/cc-pair/{cc_pair_id}/name")
HEAD:backend/onyx/server/documents/cc_pair.py:580:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:610:@router.put("/admin/cc-pair/{cc_pair_id}/property")
HEAD:backend/onyx/server/documents/cc_pair.py:614:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:666:@router.get("/admin/cc-pair/{cc_pair_id}/last_pruned")
HEAD:backend/onyx/server/documents/cc_pair.py:669:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:684:@router.post("/admin/cc-pair/{cc_pair_id}/prune", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/cc_pair.py:687:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:740:@router.get("/admin/cc-pair/{cc_pair_id}/get-docs-sync-status")
HEAD:backend/onyx/server/documents/cc_pair.py:743:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/documents/cc_pair.py:753:@router.get("/admin/cc-pair/{cc_pair_id}/errors", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/cc_pair.py:759:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/documents/cc_pair.py:794:@router.put(
HEAD:backend/onyx/server/documents/cc_pair.py:801:    user: User = Depends(
HEAD:backend/onyx/server/documents/cc_pair.py:922:@router.delete(
HEAD:backend/onyx/server/documents/cc_pair.py:928:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:11:    APIRouter,
HEAD:backend/onyx/server/documents/connector.py:176:router = APIRouter(prefix="/manage", dependencies=[Depends(require_vector_db)])
HEAD:backend/onyx/server/documents/connector.py:182:@router.put("/admin/connector/google-drive/service-account-credential")
HEAD:backend/onyx/server/documents/connector.py:185:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:202:@router.put("/admin/connector/gmail/service-account-credential")
HEAD:backend/onyx/server/documents/connector.py:205:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:221:@router.get("/admin/connector/google-drive/check-auth/{credential_id}")
HEAD:backend/onyx/server/documents/connector.py:224:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:432:@router.post("/admin/connector/file/upload", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:436:    _: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:441:@router.get("/admin/connector/{connector_id}/files", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:444:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:558:@router.post("/admin/connector/{connector_id}/files/update", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:563:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:782:@router.get("/admin/connector", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:784:    _: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:815:@router.get("/admin/connector/failed-indexing-status", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:818:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:903:@router.get("/admin/connector/status", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:905:    user: User = Depends(
HEAD:backend/onyx/server/documents/connector.py:965:@router.post("/admin/connector/indexing-status", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:968:    user: User = Depends(
HEAD:backend/onyx/server/documents/connector.py:1457:@router.post("/admin/connector", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:1460:    user: User = Depends(
HEAD:backend/onyx/server/documents/connector.py:1498:@router.post("/admin/connector-with-mock-credential")
HEAD:backend/onyx/server/documents/connector.py:1501:    user: User = Depends(
HEAD:backend/onyx/server/documents/connector.py:1587:@router.patch("/admin/connector/{connector_id}", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:1591:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:1634:@router.delete(
HEAD:backend/onyx/server/documents/connector.py:1641:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:1663:@router.post("/admin/connector/run-once", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:1666:    user: User = Depends(
HEAD:backend/onyx/server/documents/connector.py:1745:@router.get("/connector/gmail/authorize/{credential_id}")
HEAD:backend/onyx/server/documents/connector.py:1749:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1766:@router.get("/connector/google-drive/authorize/{credential_id}")
HEAD:backend/onyx/server/documents/connector.py:1770:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1787:@router.get("/connector/gmail/callback")
HEAD:backend/onyx/server/documents/connector.py:1791:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1817:@router.get("/connector/google-drive/callback")
HEAD:backend/onyx/server/documents/connector.py:1821:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1847:@router.get("/connector", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:1849:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:1862:@router.get("/indexed-sources", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:1866:    _: User = Depends(require_permission(Permission.READ_SEARCH)),
HEAD:backend/onyx/server/documents/connector.py:1875:@router.get("/connector/{connector_id}", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:1878:    _: User = Depends(require_permission(Permission.READ_CONNECTORS)),
HEAD:backend/onyx/server/documents/connector.py:1904:@router.post("/connector-request")
HEAD:backend/onyx/server/documents/connector.py:1907:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/connector.py:1991:@router.get("/connector-status", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/connector.py:1993:    user: User = Depends(current_chat_accessible_user),
HEAD:backend/onyx/server/documents/credential.py:3:from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
HEAD:backend/onyx/server/documents/credential.py:52:router = APIRouter(prefix="/manage", tags=PUBLIC_API_TAGS)
HEAD:backend/onyx/server/documents/credential.py:58:@router.get("/admin/credential")
HEAD:backend/onyx/server/documents/credential.py:60:    user: User = Depends(
HEAD:backend/onyx/server/documents/credential.py:79:@router.get("/admin/similar-credentials/{source_type}")
HEAD:backend/onyx/server/documents/credential.py:82:    user: User = Depends(
HEAD:backend/onyx/server/documents/credential.py:102:@router.delete("/admin/credential/{credential_id}")
HEAD:backend/onyx/server/documents/credential.py:105:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/credential.py:122:@router.put("/admin/credential/swap")
HEAD:backend/onyx/server/documents/credential.py:125:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/credential.py:168:@router.post("/credential")
HEAD:backend/onyx/server/documents/credential.py:171:    user: User = Depends(
HEAD:backend/onyx/server/documents/credential.py:196:@router.post("/credential/private-key")
HEAD:backend/onyx/server/documents/credential.py:204:    user: User = Depends(
HEAD:backend/onyx/server/documents/credential.py:263:@router.get("/credential")
HEAD:backend/onyx/server/documents/credential.py:265:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:278:@router.get("/credential/{credential_id}")
HEAD:backend/onyx/server/documents/credential.py:281:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:301:@router.put("/admin/credential/{credential_id}")
HEAD:backend/onyx/server/documents/credential.py:305:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/credential.py:328:@router.put("/admin/credential/private-key/{credential_id}")
HEAD:backend/onyx/server/documents/credential.py:336:    user: User = Depends(require_permission(Permission.MANAGE_CONNECTORS)),
HEAD:backend/onyx/server/documents/credential.py:378:@router.patch("/credential/{credential_id}")
HEAD:backend/onyx/server/documents/credential.py:382:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:422:@router.delete("/credential/{credential_id}")
HEAD:backend/onyx/server/documents/credential.py:425:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential.py:447:@router.delete("/credential/force/{credential_id}")
HEAD:backend/onyx/server/documents/credential.py:450:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/credential_capabilities.py:12:from fastapi import APIRouter, Depends
HEAD:backend/onyx/server/documents/credential_capabilities.py:58:router = APIRouter(prefix="/manage", dependencies=[Depends(require_vector_db)])
HEAD:backend/onyx/server/documents/credential_capabilities.py:133:@router.post("/admin/credential/{credential_id}/capability-check")
HEAD:backend/onyx/server/documents/credential_capabilities.py:137:    user: User = Depends(
HEAD:backend/onyx/server/documents/credential_capabilities.py:262:@router.get("/admin/credential/{credential_id}/capability-report")
HEAD:backend/onyx/server/documents/credential_capabilities.py:266:    user: User = Depends(
HEAD:backend/onyx/server/documents/credential_capabilities.py:307:@router.get("/admin/credential/capability-reports")
HEAD:backend/onyx/server/documents/credential_capabilities.py:310:    user: User = Depends(
HEAD:backend/onyx/server/documents/document.py:1:from fastapi import APIRouter, Depends, HTTPException, Query
HEAD:backend/onyx/server/documents/document.py:20:router = APIRouter(prefix="/document")
HEAD:backend/onyx/server/documents/document.py:25:@router.get("/document-size-info", dependencies=[Depends(require_vector_db)])
HEAD:backend/onyx/server/documents/document.py:28:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/document.py:69:@router.get("/chunk-info", dependencies=[Depends(require_vector_db)])
HEAD:backend/onyx/server/documents/document.py:73:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/models.py:452:    is_editable_for_current_user: bool
HEAD:backend/onyx/server/documents/models.py:531:        is_editable_for_current_user: bool,
HEAD:backend/onyx/server/documents/models.py:586:            is_editable_for_current_user=is_editable_for_current_user,
HEAD:backend/onyx/server/documents/models.py:588:                is_editable=is_editable_for_current_user,
HEAD:backend/onyx/server/documents/standard_oauth.py:4:from fastapi import APIRouter, Depends, Query, Request
HEAD:backend/onyx/server/documents/standard_oauth.py:31:router = APIRouter(prefix="/connector/oauth")
HEAD:backend/onyx/server/documents/standard_oauth.py:196:@router.get("/authorize/{source}")
HEAD:backend/onyx/server/documents/standard_oauth.py:201:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/standard_oauth.py:241:@router.get("/callback/{source}")
HEAD:backend/onyx/server/documents/standard_oauth.py:247:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/standard_oauth.py:294:@router.get("/details/{source}")
HEAD:backend/onyx/server/documents/standard_oauth.py:297:    _: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/documents/targeted_reindex.py:17:from fastapi import APIRouter, Depends
HEAD:backend/onyx/server/documents/targeted_reindex.py:43:router = APIRouter(prefix="/manage")
HEAD:backend/onyx/server/documents/targeted_reindex.py:77:@router.post("/admin/indexing/targeted-reindex")
HEAD:backend/onyx/server/documents/targeted_reindex.py:80:    user: User = Depends(
HEAD:backend/onyx/server/documents/targeted_reindex.py:171:@router.get("/admin/indexing/targeted-reindex/{job_id}")
HEAD:backend/onyx/server/documents/targeted_reindex.py:174:    user: User = Depends(
HEAD:backend/onyx/server/features/admin_banner/api.py:1:from fastapi import APIRouter, Depends
HEAD:backend/onyx/server/features/admin_banner/api.py:33:admin_router = APIRouter(prefix="/admin/banner")
HEAD:backend/onyx/server/features/admin_banner/api.py:38:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/admin_banner/api.py:46:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/admin_banner/api.py:66:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/api.py:1:from fastapi import APIRouter, Depends
HEAD:backend/onyx/server/features/build/api.py:35:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/api.py:45:router = APIRouter(prefix="/build", dependencies=[Depends(require_onyx_craft_enabled)])
HEAD:backend/onyx/server/features/build/api.py:49:admin_router = APIRouter(
HEAD:backend/onyx/server/features/build/api.py:51:    dependencies=[Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS))],
HEAD:backend/onyx/server/features/build/api.py:58:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/approvals/api.py:13:from fastapi import APIRouter, Depends
HEAD:backend/onyx/server/features/build/approvals/api.py:37:router = APIRouter(prefix="/approvals")
HEAD:backend/onyx/server/features/build/approvals/api.py:120:@router.get("/sessions/{session_id}/live")
HEAD:backend/onyx/server/features/build/approvals/api.py:123:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/approvals/api.py:144:@router.post("/{approval_id}/decision")
HEAD:backend/onyx/server/features/build/approvals/api.py:148:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/approvals/api.py:201:@router.post("/{approval_id}/session-grant")
HEAD:backend/onyx/server/features/build/approvals/api.py:204:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/debug.py:14:from fastapi import APIRouter, Depends, HTTPException
HEAD:backend/onyx/server/features/build/debug.py:29:router = APIRouter()
HEAD:backend/onyx/server/features/build/debug.py:40:@router.get("/debug/opencode-logs/stream")
HEAD:backend/onyx/server/features/build/debug.py:42:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:3:from fastapi import APIRouter, Depends
HEAD:backend/onyx/server/features/build/external_apps/api.py:67:router = APIRouter()
HEAD:backend/onyx/server/features/build/external_apps/api.py:69:admin_router = APIRouter()
HEAD:backend/onyx/server/features/build/external_apps/api.py:161:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:207:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:280:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:316:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:333:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:342:    _: User = Depends(require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:371:@router.post("/apps/{external_app_id}/credentials")
HEAD:backend/onyx/server/features/build/external_apps/api.py:375:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:402:@router.delete("/apps/{external_app_id}/credentials")
HEAD:backend/onyx/server/features/build/external_apps/api.py:405:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:419:@router.get("/apps")
HEAD:backend/onyx/server/features/build/external_apps/api.py:421:    user: User = Depends(require_permission(Permission.BASIC_ACCESS)),
HEAD:backend/onyx/server/features/build/external_apps/api.py:436:@router.post("/apps/connect/{request_id}/decision")
```
## Failure Semantics
Evidence lines: 143
```text
HEAD:backend/ee/onyx/auth/users.py:31:        raise HTTPException(status_code=401, detail="Invalid API key")
HEAD:backend/ee/onyx/auth/users.py:35:        raise HTTPException(status_code=401, detail="Invalid API key")
HEAD:backend/ee/onyx/auth/users.py:39:            status_code=status.HTTP_403_FORBIDDEN,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:48:from onyx.server.utils import BasicAuthenticationError
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:174:                status_code=status.HTTP_401_UNAUTHORIZED,
HEAD:backend/ee/onyx/server/enterprise_settings/api.py:231:            raise BasicAuthenticationError(detail="User must authenticate")
HEAD:backend/ee/onyx/server/log_export/collection.py:28:# unknown system logs fail open: they are collected as noise rather than risking
HEAD:backend/ee/onyx/server/middleware/license_enforcement.py:212:            # Fail open - don't block users due to cache connectivity issues
HEAD:backend/ee/onyx/server/middleware/tenant_tracking.py:80:                    # Fail open on Redis errors — don't lock paying tenants out
HEAD:backend/ee/onyx/server/middleware/tier_gate.py:92:            # Fail closed: on any tier resolution error, treat as COMMUNITY (most restrictive)
HEAD:backend/ee/onyx/server/settings/api.py:61:        # Fail closed - if Redis is down, other things will break anyway
HEAD:backend/ee/onyx/server/settings/api.py:137:        # Fail closed - disable EE features if we can't verify license
HEAD:backend/ee/onyx/server/tenants/access.py:31:        raise HTTPException(status_code=401, detail="Invalid API key")
HEAD:backend/ee/onyx/server/tenants/access.py:36:        raise HTTPException(status_code=401, detail="Invalid authorization header")
HEAD:backend/ee/onyx/server/tenants/access.py:43:            raise HTTPException(status_code=403, detail="Insufficient permissions")
HEAD:backend/ee/onyx/server/tenants/access.py:46:        raise HTTPException(status_code=401, detail="Token has expired")
HEAD:backend/ee/onyx/server/tenants/access.py:49:        raise HTTPException(status_code=401, detail="Invalid token")
HEAD:backend/ee/onyx/server/tenants/anonymous_users_api.py:82:        raise HTTPException(status_code=403, detail="Anonymous user is not enabled")
HEAD:backend/ee/onyx/server/tenants/billing.py:203:    Stripe errors propagate (fail closed). No-op when current quantity
HEAD:backend/ee/onyx/server/tenants/provisioning.py:202:        raise HTTPException(status_code=403, detail="Multi-tenancy is not enabled")
HEAD:backend/ee/onyx/server/tenants/proxy.py:102:                status_code=401, detail="Missing or invalid authorization header"
HEAD:backend/ee/onyx/server/tenants/proxy.py:128:        raise HTTPException(status_code=401, detail=f"Invalid license: {e}")
HEAD:backend/ee/onyx/server/tenants/proxy.py:131:        raise HTTPException(status_code=401, detail="License has expired")
HEAD:backend/ee/onyx/server/tenants/proxy.py:344:        raise HTTPException(status_code=401, detail="License missing tenant_id")
HEAD:backend/ee/onyx/server/tenants/proxy.py:391:        raise HTTPException(status_code=401, detail="License missing tenant_id")
HEAD:backend/ee/onyx/server/tenants/proxy.py:454:        raise HTTPException(status_code=401, detail="License missing tenant_id")
HEAD:backend/ee/onyx/server/tenants/proxy.py:458:            status_code=403,
HEAD:backend/ee/onyx/server/tenants/proxy.py:492:        raise HTTPException(status_code=401, detail="License missing tenant_id")
HEAD:backend/ee/onyx/server/tenants/team_membership_api.py:36:            status_code=403, detail="You can only leave the organization as yourself"
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:15:FORBIDDEN_COMMON_EMAIL_SUBSTRINGS = [
HEAD:backend/ee/onyx/server/tenants/tenant_management_api.py:32:    if any(substring in domain for substring in FORBIDDEN_COMMON_EMAIL_SUBSTRINGS):
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:16:    FORBIDDEN_COMMON_EMAIL_SUBSTRINGS,
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:53:    # Case-folded: the forbidden list is lower case, so GMAIL.com would pass it.
HEAD:backend/ee/onyx/server/tenants/user_invitations_api.py:56:    if not any(substring in domain for substring in FORBIDDEN_COMMON_EMAIL_SUBSTRINGS):
HEAD:backend/onyx/auth/captcha.py:117:    the TTL returns False → raise. Redis errors fail open so a blip does
HEAD:backend/onyx/auth/mobile_sso/code_store.py:71:        # fail-closed contract.
HEAD:backend/onyx/auth/mobile_sso/code_store.py:74:        # A malformed verifier (e.g. non-ascii) must fail closed as the same
HEAD:backend/onyx/auth/permission_projection.py:7:its own guard as the security boundary. Fail-closed — a key absent from the map reads
HEAD:backend/onyx/auth/scoped_permissions.py:79:    requested) is one they manage, landing in >=1 group. Fail-closed: NONE,
HEAD:backend/onyx/auth/scoped_permissions.py:151:    for a group they manage. Fail-closed: empty managed scope is ``False``.
HEAD:backend/onyx/auth/sso_tenant_token.py:43:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/auth/sso_tenant_token.py:50:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/auth/users.py:158:from onyx.server.utils import BasicAuthenticationError
HEAD:backend/onyx/auth/users.py:304:        # Fail closed: if the setting can't be read, treat the workspace as
HEAD:backend/onyx/auth/users.py:341:        OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/auth/users.py:1037:            raise HTTPException(status_code=401, detail="User not found")
HEAD:backend/onyx/auth/users.py:1061:                        OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/auth/users.py:1540:            raise BasicAuthenticationError(detail="PASSWORD_LOGIN_DISABLED")
HEAD:backend/onyx/auth/users.py:1584:                raise BasicAuthenticationError(
HEAD:backend/onyx/auth/users.py:1951:            status.HTTP_401_UNAUTHORIZED: {
HEAD:backend/onyx/auth/users.py:2201:    """Whether a scoped PAT may proceed on this route (fail-closed)."""
HEAD:backend/onyx/auth/users.py:2263:    # Fail-closed: a scoped PAT may only reach routes guarded by a
HEAD:backend/onyx/auth/users.py:2328:            raise BasicAuthenticationError(
HEAD:backend/onyx/auth/users.py:2337:            raise BasicAuthenticationError(
HEAD:backend/onyx/auth/users.py:2350:    raise BasicAuthenticationError(
HEAD:backend/onyx/auth/users.py:2387:        raise BasicAuthenticationError(
HEAD:backend/onyx/auth/users.py:2453:    Raises BasicAuthenticationError if authentication fails.
HEAD:backend/onyx/auth/users.py:2469:        raise BasicAuthenticationError(detail="Access denied. Missing origin.")
HEAD:backend/onyx/auth/users.py:2475:        raise BasicAuthenticationError(detail="Access denied. Invalid origin.")
HEAD:backend/onyx/auth/users.py:2481:            raise BasicAuthenticationError(
HEAD:backend/onyx/auth/users.py:2484:    except BasicAuthenticationError:
HEAD:backend/onyx/auth/users.py:2488:        raise BasicAuthenticationError(
HEAD:backend/onyx/auth/users.py:2496:            raise BasicAuthenticationError(
HEAD:backend/onyx/auth/users.py:2508:            raise BasicAuthenticationError(
HEAD:backend/onyx/auth/users.py:2516:            raise BasicAuthenticationError(
HEAD:backend/onyx/server/auth/captcha_api.py:76:        raise OnyxError(OnyxErrorCode.UNAUTHORIZED, str(exc))
HEAD:backend/onyx/server/auth/captcha_api.py:111:                        OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/auth/captcha_api.py:133:    server-side shared secret. Empty env var = bypass disabled (fail-closed)
HEAD:backend/onyx/server/auth/captcha_api.py:186:                        OnyxError(OnyxErrorCode.UNAUTHORIZED, str(exc))
HEAD:backend/onyx/server/documents/connector.py:427:        status_code=403,
HEAD:backend/onyx/server/documents/connector.py:992:                status.setdefault("permissions", {})  # fail-closed for mock rows
HEAD:backend/onyx/server/documents/connector.py:1797:            status_code=401, detail="Request did not pass CSRF verification."
HEAD:backend/onyx/server/documents/connector.py:1827:            status_code=401, detail="Request did not pass CSRF verification."
HEAD:backend/onyx/server/features/build/db/build_session.py:274:    Returns the updated session, or None if not found/unauthorized.
HEAD:backend/onyx/server/features/build/sandbox/image/firewall-init.sh:100:    # distinguish "lockdown working" from "no internet" — fail-open.
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py:88:        raise HTTPException(status_code=401, detail="Invalid timestamp")
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py:90:        raise HTTPException(status_code=401, detail="Timestamp out of range")
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py:95:        raise HTTPException(status_code=401, detail="Invalid signature encoding")
HEAD:backend/onyx/server/features/build/sandbox/image/sandbox_daemon/server.py:101:        raise HTTPException(status_code=401, detail="Invalid signature")
HEAD:backend/onyx/server/features/build/sandbox/serve_transport.py:224:        fail_open: bool = True,
HEAD:backend/onyx/server/features/build/sandbox/serve_transport.py:247:                "open" if fail_open else "closed",
HEAD:backend/onyx/server/features/build/sandbox/serve_transport.py:251:            yield PromptSlot(acquired=fail_open)
HEAD:backend/onyx/server/features/build/sandbox/util/api_url_check.py:63:    (confirmed, or fail-open) latch ``_validated`` so we never re-probe on
HEAD:backend/onyx/server/features/build/sandbox/util/api_url_check.py:64:    later provisions — validation is of static config, and fail-open already
HEAD:backend/onyx/server/features/build/session/api.py:545:            raise HTTPException(status_code=403, detail="Access denied")
HEAD:backend/onyx/server/features/build/session/api.py:577:            raise HTTPException(status_code=403, detail="Access denied")
HEAD:backend/onyx/server/features/build/session/api.py:627:            raise HTTPException(status_code=403, detail="Access denied")
HEAD:backend/onyx/server/features/build/session/api.py:669:            raise HTTPException(status_code=403, detail="Access denied")
HEAD:backend/onyx/server/features/build/session/api.py:750:            raise HTTPException(status_code=403, detail="Access denied")
HEAD:backend/onyx/server/features/build/session/api.py:839:            raise HTTPException(status_code=403, detail="Access denied")
HEAD:backend/onyx/server/features/build/session/manager.py:386:                fail_open=False,
HEAD:backend/onyx/server/features/build/session/sandbox_lifecycle.py:820:    Invariant: snapshot before terminate, fail-closed — a snapshot failure on
HEAD:backend/onyx/server/features/build/session/sandbox_lifecycle.py:896:    # Fail-closed: terminating with an unsnapshotted workspace loses it
HEAD:backend/onyx/server/features/build/timeouts.py:172:# "snapshotting can take minutes"; the reaper is fail-closed on snapshot
HEAD:backend/onyx/server/features/build/webapp_proxy.py:369:        raise HTTPException(status_code=401, detail="Authentication required")
HEAD:backend/onyx/server/features/document_set/models.py:157:    # Defaults empty (fail-closed); the list endpoint stamps the real map.
HEAD:backend/onyx/server/features/document_set/models.py:171:        an empty (fail-closed) map — the document-set list endpoint stamps the real one;
HEAD:backend/onyx/server/features/hierarchy/api.py:54:            status_code=403,
HEAD:backend/onyx/server/features/hierarchy/api.py:59:            status_code=403,
HEAD:backend/onyx/server/features/mcp/api.py:661:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/features/mcp/api.py:934:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/features/mcp/api.py:1585:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/features/mcp/api.py:2191:    #     raise HTTPException(status_code=403, detail="Forbidden")
HEAD:backend/onyx/server/features/mcp/models.py:730:    # Server-stamped affordance map; fail-closed empty (only the admin server list stamps it).
HEAD:backend/onyx/server/features/mcp/ssrf.py:62:                    status_code=401,
HEAD:backend/onyx/server/features/notifications/api.py:230:    except PermissionError as e:
HEAD:backend/onyx/server/features/notifications/api.py:232:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/features/oauth_config/api.py:255:                status_code=403, detail="User mismatch in OAuth callback"
HEAD:backend/onyx/server/features/persona/api.py:200:        raise HTTPException(status_code=403, detail=str(e))
HEAD:backend/onyx/server/features/persona/api.py:219:        raise HTTPException(status_code=403, detail=str(e))
HEAD:backend/onyx/server/features/persona/api.py:237:        raise HTTPException(status_code=403, detail=str(e))
HEAD:backend/onyx/server/features/persona/api.py:520:    except PermissionError as e:
HEAD:backend/onyx/server/features/persona/api.py:522:        raise HTTPException(status_code=403, detail=str(e))
HEAD:backend/onyx/server/features/persona/api.py:554:    except PermissionError as e:
HEAD:backend/onyx/server/features/persona/api.py:556:        raise HTTPException(status_code=403, detail=str(e))
HEAD:backend/onyx/server/features/persona/api.py:596:        # not forbidden. Only checked once the delete has already failed, so the
HEAD:backend/onyx/server/features/persona/api.py:625:# so without this a scoped PAT is rejected fail-closed. MCP clients need this
HEAD:backend/onyx/server/features/persona/models.py:239:    # stamp it (fail-closed on the client). List endpoints stamp it so each card
HEAD:backend/onyx/server/features/persona/models.py:248:        # Fail closed: the owner email is PII and is only included when a caller
HEAD:backend/onyx/server/features/projects/api.py:189:                OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/features/search/api.py:113:            raise OnyxError(OnyxErrorCode.UNAUTHORIZED)
HEAD:backend/onyx/server/features/tool/models.py:42:    # Server-stamped affordance map; fail-closed empty (only the admin actions list stamps it).
HEAD:backend/onyx/server/manage/image_generation/api.py:283:            status_code=401,
HEAD:backend/onyx/server/manage/invite_rate_limit.py:35:# counter. Self-hosted / Lite deployments fail open when Redis is unavailable.
HEAD:backend/onyx/server/manage/users.py:134:from onyx.server.utils import BasicAuthenticationError
HEAD:backend/onyx/server/manage/users.py:1068:        raise BasicAuthenticationError(detail="Unauthorized")
HEAD:backend/onyx/server/manage/users.py:1071:        raise BasicAuthenticationError(
HEAD:backend/onyx/server/oidc_multi.py:117:        raise OnyxError(OnyxErrorCode.UNAUTHORIZED, _NO_WORKSPACE_DETAIL)
HEAD:backend/onyx/server/oidc_multi.py:135:        raise OnyxError(OnyxErrorCode.UNAUTHORIZED, _NO_WORKSPACE_DETAIL)
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:393:                    status_code=403, detail="Chat session is not shared"
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:399:            raise HTTPException(status_code=403, detail="Access denied")
HEAD:backend/onyx/server/query_and_chat/chat_backend.py:485:        raise HTTPException(status_code=403, detail=str(e))
HEAD:backend/onyx/server/saml_multi.py:156:    raise OnyxError(OnyxErrorCode.UNAUTHORIZED, "unrecognized SAML issuer")
HEAD:backend/onyx/server/saml_multi.py:167:        raise OnyxError(OnyxErrorCode.UNAUTHORIZED, "malformed SAML response")
HEAD:backend/onyx/server/saml_multi.py:179:    raise OnyxError(OnyxErrorCode.UNAUTHORIZED, "SAML response missing issuer")
HEAD:backend/onyx/server/saml_multi.py:196:    raise OnyxError(OnyxErrorCode.UNAUTHORIZED, detail)
HEAD:backend/onyx/server/saml_multi.py:250:        OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/saml_multi.py:325:        raise OnyxError(OnyxErrorCode.UNAUTHORIZED, "missing SAML response")
HEAD:backend/onyx/server/saml_multi.py:350:            OnyxErrorCode.UNAUTHORIZED,
HEAD:backend/onyx/server/settings/api.py:85:        # Fail closed: a settings-read error must not fall back to defaults and
HEAD:backend/onyx/server/settings/store.py:65:        # re-raise so they can fail closed instead of trusting the default.
HEAD:backend/onyx/server/utils.py:11:class BasicAuthenticationError(HTTPException):
HEAD:backend/onyx/server/utils.py:13:        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)
```
These findings identify candidate fail-open/fail-closed and 401/403 behavior
for later verification.
## Current Request-Context Model
```text
Stage | Static evidence status
------|-----------------------
HTTP/FastAPI application entry | OBSERVED
Router registration | OBSERVED
Authentication backend selection | OBSERVED
User identity dependency mechanisms | OBSERVED
Permission model / require_permission | OBSERVED
Routes using permission dependencies | OBSERVED
Tenant-related context mechanisms | OBSERVED
Tenant-aware DB/session mechanisms | OBSERVED
Object/document access-control code | OBSERVED
Exact runtime middleware order | NOT RUNTIME VERIFIED
Every route correctly authenticated | NOT PROVEN
Every object access correctly authorized | NOT PROVEN
Cross-tenant isolation correctness | NOT PROVEN
```
## Evidence-Backed Security Flow
Static evidence now supports the following provisional flow:
1. A request reaches the FastAPI application/router layer.
2. Authentication mechanisms can resolve credentials/session state into a
   user identity.
3. Request handlers can require authenticated/current-user dependencies.
4. Onyx defines explicit permissions and permission-check dependencies.
5. Some routes explicitly depend on permission requirements.
6. Tenant-related context exists and is propagated into application/data
   handling.
7. Tenant-aware database/session mechanisms exist.
8. Separate object/document access-control mechanisms exist.
9. Search/document paths contain user/ACL/permission-related context.
## Security Layers That Must Not Be Confused
### Authentication
Who is the caller?
### Tenant resolution
Which tenant/security namespace is the request operating inside?
### Feature/route authorization
May this identity perform this type of operation?
### Object-level authorization
May this identity access this specific document, connector, chat session,
agent, credential or other object?
A PASS at one layer does not imply a PASS at the next layer.
## High-Value Future Verification Questions
Later security phases must test questions such as:
- Can unauthenticated requests reach protected handlers?
- Can a low-privilege user reach admin functionality?
- Can tenant context be manipulated or confused?
- Can object identifiers cross ownership boundaries?
- Can one tenant access another tenant's documents?
- Are search/RAG results filtered using the caller's effective access?
- Do background tasks preserve tenant context correctly?
- Do API keys, PATs and browser sessions receive equivalent authorization?
- Do MCP requests preserve the same effective identity and access controls?
- Are revocations immediately reflected in retrieval and object access?
No vulnerability claim is made by Action 6.5.
## Interpretation Boundary
Static source evidence establishes control mechanisms and candidate flow.
It does not prove:
- actual runtime middleware ordering;
- control completeness;
- correct behavior under malformed credentials;
- authorization correctness;
- absence of IDOR/BOLA;
- tenant isolation;
- absence of privilege escalation;
- correct revocation;
- runtime session behavior.
Those require bounded runtime tests in later phases.
## Safety Record
During Action 6.5:
- Onyx execution: NO
- Docker execution: NO
- Authentication attempts: NO
- Tokens created: NO
- Credentials used: NO
- Database startup: NO
- Network probing: NO
- Vulnerability exploitation: NO
- External AI calls: NO
- Production data: NO
- Onyx source modification: NO
## Result
Action 6.5 identity and request-context flow trace: **PASS**.
