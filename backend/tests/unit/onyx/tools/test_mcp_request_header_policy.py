"""Focused H9-16 MCP request-header policy regression tests."""

from types import SimpleNamespace
from typing import Any, cast
from unittest.mock import MagicMock, patch

from onyx.db.enums import (
    MCPAuthenticationPerformer,
    MCPAuthenticationType,
    MCPTransport,
)
from onyx.db.models import MCPConnectionConfig
from onyx.server.features.mcp.credentials import ResolvedMCPCredentials
from onyx.server.features.mcp.models import (
    MCPAuthTemplate,
    filter_request_mcp_headers,
    merge_mcp_headers,
    request_mcp_headers_can_authenticate,
)
from onyx.server.query_and_chat.placement import Placement
from onyx.tools.tool_implementations.mcp.mcp_tool import MCPTool


def _make_tool(
    *,
    auth_type: MCPAuthenticationType,
    auth_performer: MCPAuthenticationPerformer,
    credentials: ResolvedMCPCredentials,
    additional_headers: dict[str, str],
) -> MCPTool:
    server = SimpleNamespace(
        name="h916_synthetic",
        server_url="http://127.0.0.1:8765/mcp",
        auth_type=auth_type,
        auth_performer=auth_performer,
        transport=MCPTransport.STREAMABLE_HTTP,
    )
    return MCPTool(
        tool_id=916,
        emitter=MagicMock(),
        mcp_server=cast(Any, server),
        tool_name="h916_probe",
        tool_description="Synthetic H9-16 policy probe",
        tool_definition={},
        additional_headers=additional_headers,
        resolved_credentials=credentials,
    )


def _run_with_mocked_call(tool: MCPTool) -> tuple[Any, MagicMock]:
    with (
        patch(
            "onyx.tools.tool_implementations.mcp.mcp_tool.call_mcp_tool",
            return_value={"ok": True},
        ) as call,
        patch(
            "onyx.tools.tool_implementations.mcp.mcp_tool."
            "record_mcp_client_tool_outcome"
        ),
    ):
        response = tool.run(Placement(turn_index=0))
    return response, call


def test_request_headers_denied_without_admin_template() -> None:
    assert filter_request_mcp_headers(
        {
            "Authorization": "Bearer synthetic-caller",
            "X-Synthetic-Privilege": "admin",
        },
        None,
    ) == {}


def test_request_header_allowlist_is_case_insensitive() -> None:
    template = MCPAuthTemplate(
        headers={
            "Authorization": "Bearer {api_key}",
            "X-User": "{user_email}",
        }
    )
    assert filter_request_mcp_headers(
        {
            "authorization": "Bearer synthetic-caller",
            "x-USER": "alice@tenant-alpha.test",
            "X-Synthetic-Privilege": "admin",
        },
        template,
    ) == {
        "authorization": "Bearer synthetic-caller",
        "x-USER": "alice@tenant-alpha.test",
    }


def test_protocol_headers_denied_even_for_malformed_legacy_template() -> None:
    template = MCPAuthTemplate.model_construct(
        headers={
            "Host": "{host}",
            "Connection": "{connection}",
            "Transfer-Encoding": "{encoding}",
        },
        required_fields=["connection", "encoding", "host"],
    )
    assert filter_request_mcp_headers(
        {
            "HOST": "127.0.0.1",
            "connection": "keep-alive",
            "transfer-encoding": "chunked",
        },
        template,
    ) == {}


def test_fallback_is_limited_to_per_user_api_token() -> None:
    template = MCPAuthTemplate(headers={"Authorization": "Bearer {api_key}"})
    request_headers = {"authorization": "Bearer synthetic-caller"}

    assert request_mcp_headers_can_authenticate(
        request_headers,
        {},
        auth_type=MCPAuthenticationType.API_TOKEN,
        auth_performer=MCPAuthenticationPerformer.PER_USER,
        auth_template=template,
    )

    denied_shapes = (
        (MCPAuthenticationType.API_TOKEN, MCPAuthenticationPerformer.ADMIN),
        (MCPAuthenticationType.OAUTH, MCPAuthenticationPerformer.PER_USER),
        (MCPAuthenticationType.PT_OAUTH, MCPAuthenticationPerformer.PER_USER),
        (MCPAuthenticationType.NONE, MCPAuthenticationPerformer.PER_USER),
    )
    for auth_type, auth_performer in denied_shapes:
        assert not request_mcp_headers_can_authenticate(
            request_headers,
            {},
            auth_type=auth_type,
            auth_performer=auth_performer,
            auth_template=template,
        )


def test_fallback_requires_complete_nonempty_template_headers() -> None:
    template = MCPAuthTemplate(
        headers={
            "Authorization": "Bearer {api_key}",
            "X-Tenant": "{tenant}",
        }
    )
    request_headers = {"authorization": "Bearer synthetic-caller"}

    assert not request_mcp_headers_can_authenticate(
        request_headers,
        {},
        auth_type=MCPAuthenticationType.API_TOKEN,
        auth_performer=MCPAuthenticationPerformer.PER_USER,
        auth_template=template,
    )
    assert request_mcp_headers_can_authenticate(
        request_headers,
        {"X-Tenant": "tenant-alpha"},
        auth_type=MCPAuthenticationType.API_TOKEN,
        auth_performer=MCPAuthenticationPerformer.PER_USER,
        auth_template=template,
    )
    assert not request_mcp_headers_can_authenticate(
        {"Authorization": ""},
        {"X-Tenant": "tenant-alpha"},
        auth_type=MCPAuthenticationType.API_TOKEN,
        auth_performer=MCPAuthenticationPerformer.PER_USER,
        auth_template=template,
    )


def test_managed_header_wins_case_insensitive_collision() -> None:
    assert merge_mcp_headers(
        {"authorization": "Bearer synthetic-caller"},
        {"Authorization": "Bearer synthetic-managed"},
    ) == {"Authorization": "Bearer synthetic-managed"}


def test_runtime_filters_unlisted_header_and_preserves_managed_precedence() -> None:
    template = MCPAuthTemplate(headers={"Authorization": "Bearer {api_key}"})
    credentials = ResolvedMCPCredentials(
        connection_config=MCPConnectionConfig(
            config={
                "headers": {},
                "header_substitutions": {"api_key": "synthetic-managed"},
            }
        ),
        user_oauth_token=None,
        auth_type=MCPAuthenticationType.API_TOKEN,
        auth_template=template,
    )
    tool = _make_tool(
        auth_type=MCPAuthenticationType.API_TOKEN,
        auth_performer=MCPAuthenticationPerformer.ADMIN,
        credentials=credentials,
        additional_headers={
            "authorization": "Bearer synthetic-caller",
            "X-Synthetic-Privilege": "admin",
        },
    )

    _, call = _run_with_mocked_call(tool)

    assert call.call_count == 1
    assert call.call_args.kwargs["connection_headers"] == {
        "Authorization": "Bearer synthetic-managed"
    }


def test_runtime_allows_explicit_per_user_api_token_delegation() -> None:
    template = MCPAuthTemplate(headers={"Authorization": "Bearer {api_key}"})
    credentials = ResolvedMCPCredentials(
        connection_config=None,
        user_oauth_token=None,
        auth_type=MCPAuthenticationType.API_TOKEN,
        auth_template=template,
    )
    tool = _make_tool(
        auth_type=MCPAuthenticationType.API_TOKEN,
        auth_performer=MCPAuthenticationPerformer.PER_USER,
        credentials=credentials,
        additional_headers={
            "authorization": "Bearer synthetic-delegated",
            "X-Synthetic-Privilege": "admin",
        },
    )

    _, call = _run_with_mocked_call(tool)

    assert call.call_count == 1
    assert call.call_args.kwargs["connection_headers"] == {
        "authorization": "Bearer synthetic-delegated"
    }


def test_runtime_rejects_caller_auth_without_admin_template() -> None:
    credentials = ResolvedMCPCredentials(
        connection_config=None,
        user_oauth_token=None,
        auth_type=MCPAuthenticationType.API_TOKEN,
        auth_template=None,
    )
    tool = _make_tool(
        auth_type=MCPAuthenticationType.API_TOKEN,
        auth_performer=MCPAuthenticationPerformer.PER_USER,
        credentials=credentials,
        additional_headers={"Authorization": "Bearer synthetic-caller"},
    )

    response, call = _run_with_mocked_call(tool)

    call.assert_not_called()
    assert "requires connection values" in response.llm_facing_response


TESTS = (
    test_request_headers_denied_without_admin_template,
    test_request_header_allowlist_is_case_insensitive,
    test_protocol_headers_denied_even_for_malformed_legacy_template,
    test_fallback_is_limited_to_per_user_api_token,
    test_fallback_requires_complete_nonempty_template_headers,
    test_managed_header_wins_case_insensitive_collision,
    test_runtime_filters_unlisted_header_and_preserves_managed_precedence,
    test_runtime_allows_explicit_per_user_api_token_delegation,
    test_runtime_rejects_caller_auth_without_admin_template,
)


if __name__ == "__main__":
    for test in TESTS:
        test()
    print(f"H9_16_POLICY_TEST_COUNT={len(TESTS)}")
    print("H9_16_POLICY_UNIT_TESTS=PASS")
    print("EXTERNAL_REQUESTS=0")
