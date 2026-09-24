import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import onyx.tools.tool_implementations.custom.custom_tool as custom_tool
from onyx.server.security.models import (
    SSRFProtectionLevel,
)
from onyx.utils.url import SSRFException


class TestPhase11CustomToolSSRF(unittest.TestCase):
    def test_default_policy_blocks_loopback(
        self,
    ) -> None:
        settings = SimpleNamespace(
            ssrf_protection_level=(
                SSRFProtectionLevel.VALIDATE_ALL
            )
        )

        with patch.object(
            custom_tool,
            "get_security_settings",
            return_value=settings,
        ):
            with self.assertRaises(
                SSRFException
            ):
                custom_tool._validate_custom_tool_outbound_url(
                    "http://127.0.0.1:8080/admin"
                )

    def test_cloud_metadata_block_remains_even_when_disabled(
        self,
    ) -> None:
        settings = SimpleNamespace(
            ssrf_protection_level=(
                SSRFProtectionLevel.DISABLED
            )
        )

        with patch.object(
            custom_tool,
            "get_security_settings",
            return_value=settings,
        ):
            with self.assertRaises(
                SSRFException
            ):
                custom_tool._validate_custom_tool_outbound_url(
                    "http://169.254.169.254/"
                    "latest/meta-data/"
                )

    def test_disabled_policy_can_allow_loopback_for_trusted_lab(
        self,
    ) -> None:
        settings = SimpleNamespace(
            ssrf_protection_level=(
                SSRFProtectionLevel.DISABLED
            )
        )

        with patch.object(
            custom_tool,
            "get_security_settings",
            return_value=settings,
        ):
            result = (
                custom_tool
                ._validate_custom_tool_outbound_url(
                    "http://127.0.0.1:8765/mcp"
                )
            )

        self.assertEqual(
            result,
            "http://127.0.0.1:8765/mcp",
        )

    def test_custom_actions_disable_automatic_redirects(
        self,
    ) -> None:
        source = Path(
            "onyx/tools/tool_implementations/"
            "custom/custom_tool.py"
        ).read_text()

        self.assertIn(
            "allow_redirects=False",
            source,
        )

        self.assertIn(
            "_validate_custom_tool_outbound_url",
            source,
        )


if __name__ == "__main__":
    unittest.main()
