import unittest
from pathlib import Path

from onyx.db.enums import (
    MCPAuthenticationPerformer,
    MCPAuthenticationType,
)
from onyx.server.features.mcp.models import (
    MCPAuthTemplate,
    filter_request_mcp_headers,
    merge_mcp_headers,
    request_mcp_headers_can_authenticate,
)


class TestPhase11MCPSecurityBoundaries(unittest.TestCase):
    def test_protocol_host_header_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MCPAuthTemplate(
                headers={
                    "Host": "{target}",
                }
            )

    def test_request_headers_are_admin_allowlisted(
        self,
    ) -> None:
        template = MCPAuthTemplate(
            headers={
                "Authorization":
                "Bearer {api_key}",
            }
        )

        self.assertEqual(
            filter_request_mcp_headers(
                {
                    "Authorization":
                    "Bearer synthetic-user",
                    "X-Synthetic-Privilege":
                    "admin",
                },
                template,
            ),
            {
                "Authorization":
                "Bearer synthetic-user",
            },
        )

    def test_managed_credentials_override_request_collision(
        self,
    ) -> None:
        self.assertEqual(
            merge_mcp_headers(
                {
                    "authorization":
                    "Bearer synthetic-caller",
                },
                {
                    "Authorization":
                    "Bearer synthetic-managed",
                },
            ),
            {
                "Authorization":
                "Bearer synthetic-managed",
            },
        )

    def test_request_auth_fallback_is_per_user_only(
        self,
    ) -> None:
        template = MCPAuthTemplate(
            headers={
                "Authorization":
                "Bearer {api_key}",
            }
        )

        request_headers = {
            "Authorization":
            "Bearer synthetic-user"
        }

        self.assertTrue(
            request_mcp_headers_can_authenticate(
                request_headers,
                {},
                auth_type=(
                    MCPAuthenticationType.API_TOKEN
                ),
                auth_performer=(
                    MCPAuthenticationPerformer.PER_USER
                ),
                auth_template=template,
            )
        )

        self.assertFalse(
            request_mcp_headers_can_authenticate(
                request_headers,
                {},
                auth_type=(
                    MCPAuthenticationType.API_TOKEN
                ),
                auth_performer=(
                    MCPAuthenticationPerformer.ADMIN
                ),
                auth_template=template,
            )
        )

    def test_client_uses_ssrf_guarded_transport(
        self,
    ) -> None:
        client = Path(
            "onyx/server/features/mcp/client.py"
        ).read_text()

        ssrf = Path(
            "onyx/server/features/mcp/ssrf.py"
        ).read_text()

        self.assertIn(
            "httpx_client_factory="
            "mcp_ssrf_httpx_client_factory",
            client,
        )

        self.assertIn(
            "validate_mcp_outbound_url("
            "str(request.url)",
            ssrf,
        )

        self.assertIn(
            "follow_redirects=True",
            ssrf,
        )

    def test_sandbox_mcp_resolver_checks_user_and_gate(
        self,
    ) -> None:
        resolver = Path(
            "onyx/sandbox_proxy/resolvers/"
            "mcp_server.py"
        ).read_text()

        self.assertIn(
            "user_can_access_mcp_server",
            resolver,
        )

        self.assertIn(
            "non-plumbing MCP request",
            resolver,
        )

        self.assertIn(
            "CredentialUnavailableError",
            resolver,
        )


if __name__ == "__main__":
    unittest.main()
