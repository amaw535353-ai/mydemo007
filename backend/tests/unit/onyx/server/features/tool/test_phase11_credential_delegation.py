import unittest
from pathlib import Path

from onyx.external_apps.credentials import (
    build_auth_headers,
)


class TestPhase11CredentialDelegation(unittest.TestCase):
    def test_missing_secret_omits_auth_header(
        self,
    ) -> None:
        rendered = build_auth_headers(
            {
                "Authorization":
                "Bearer {api_token}",
                "X-Synthetic": "fixed",
            },
            {},
        )

        self.assertNotIn(
            "Authorization",
            rendered,
        )

        self.assertEqual(
            rendered["X-Synthetic"],
            "fixed",
        )

    def test_secret_substitution_is_single_pass(
        self,
    ) -> None:
        rendered = build_auth_headers(
            {
                "Authorization":
                "Bearer {api_token}",
            },
            {
                "api_token":
                "{other_user_secret}",
            },
        )

        self.assertEqual(
            rendered["Authorization"],
            "Bearer {other_user_secret}",
        )

    def test_custom_action_management_has_delegation_gates(
        self,
    ) -> None:
        source = Path(
            "onyx/server/features/tool/api.py"
        ).read_text()

        self.assertIn(
            "tool_data.passthrough_auth "
            "and tool_data.custom_headers",
            source,
        )

        self.assertIn(
            'header.key.lower() == "authorization"',
            source,
        )

        self.assertIn(
            "_assert_can_link_oauth_config",
            source,
        )

        self.assertIn(
            "can_link_oauth_config",
            source,
        )

    def test_tool_construction_uses_current_user_identity(
        self,
    ) -> None:
        source = Path(
            "onyx/tools/tool_constructor.py"
        ).read_text()

        self.assertIn(
            "OAuthTokenManager("
            "oauth_config, user.id, db_session",
            source,
        )

        self.assertIn(
            "user_id=user.id",
            source,
        )

        self.assertIn(
            "user_email="
            '"anonymous" if user.is_anonymous else user.email',
            source,
        )

    def test_external_app_resolver_uses_sandbox_identity(
        self,
    ) -> None:
        source = Path(
            "onyx/sandbox_proxy/resolvers/"
            "external_app.py"
        ).read_text()

        self.assertIn(
            "ctx.sandbox.tenant_id",
            source,
        )

        self.assertIn(
            "ctx.sandbox.user_id",
            source,
        )

        self.assertIn(
            "resolve_injection_headers",
            source,
        )


if __name__ == "__main__":
    unittest.main()
