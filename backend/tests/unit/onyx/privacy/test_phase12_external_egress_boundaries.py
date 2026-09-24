import unittest
from pathlib import Path


CUSTOM = Path(
    "onyx/tools/tool_implementations/custom/custom_tool.py"
).read_text()

MCP_TOOL = Path(
    "onyx/tools/tool_implementations/mcp/mcp_tool.py"
).read_text()

MCP_CLIENT = Path(
    "onyx/server/features/mcp/client.py"
).read_text()

MCP_CREDS = Path(
    "onyx/server/features/mcp/credentials.py"
).read_text()

LLM_FACTORY = Path(
    "onyx/llm/factory.py"
).read_text()


class TestPhase12ExternalEgressBoundaries(unittest.TestCase):
    def test_custom_tool_validates_outbound_target(self) -> None:
        self.assertIn(
            "validate_outbound_http_url",
            CUSTOM,
        )
        self.assertIn(
            "_validate_custom_tool_outbound_url(",
            CUSTOM,
        )

    def test_custom_tool_does_not_follow_redirects(self) -> None:
        self.assertIn(
            "requests.request(",
            CUSTOM,
        )
        self.assertIn(
            "allow_redirects=False",
            CUSTOM,
        )

    def test_mcp_filters_request_headers_before_merge(self) -> None:
        self.assertIn(
            "filter_request_mcp_headers(",
            MCP_TOOL,
        )
        self.assertIn(
            "merge_mcp_headers(request_headers, managed_headers)",
            MCP_TOOL,
        )

    def test_mcp_transport_uses_ssrf_factory_and_timeout(self) -> None:
        self.assertIn(
            "mcp_ssrf_httpx_client_factory",
            MCP_CLIENT,
        )
        self.assertIn(
            "MCP_TOOL_CALL_TIMEOUT_SECONDS",
            MCP_CLIENT,
        )
        self.assertIn(
            "header values are credentials",
            MCP_CREDS,
        )

    def test_model_provider_boundary_is_explicit(self) -> None:
        self.assertIn(
            "api_key=llm_provider.api_key",
            LLM_FACTORY,
        )
        self.assertIn(
            "api_base=llm_provider.api_base",
            LLM_FACTORY,
        )


if __name__ == "__main__":
    unittest.main()
