import unittest
from pathlib import Path

from onyx.utils.redaction import REDACTED_VALUE
from onyx.utils.redaction import scrub_sensitive_values


LOG_EXPORT = Path(
    "ee/onyx/server/log_export/api.py"
).read_text()

USAGE_EXPORT = Path(
    "ee/onyx/server/reporting/usage_export_api.py"
).read_text()


class TestPhase12DlpRedactionExport(unittest.TestCase):
    def test_synthetic_sensitive_values_are_redacted(self) -> None:
        email = "alice@tenant-alpha.test"
        token = "fake-api-token-phase12"

        message = (
            f"user={email} authorization={token} "
            "safe=synthetic"
        )

        result = scrub_sensitive_values(
            message,
            [email, token],
        )

        self.assertNotIn(
            email,
            result,
        )
        self.assertNotIn(
            token,
            result,
        )
        self.assertGreaterEqual(
            result.count(REDACTED_VALUE),
            2,
        )

    def test_overlapping_values_are_redacted_safely(self) -> None:
        result = scrub_sensitive_values(
            "synthetic-secret-long synthetic-secret",
            [
                "synthetic-secret",
                "synthetic-secret-long",
            ],
        )

        self.assertNotIn(
            "synthetic-secret",
            result,
        )

    def test_short_value_false_positive_guard(self) -> None:
        self.assertEqual(
            scrub_sensitive_values(
                "id=ab",
                ["ab"],
            ),
            "id=ab",
        )

    def test_log_export_download_requires_admin_permission(self) -> None:
        self.assertIn(
            "download_log_export",
            LOG_EXPORT,
        )
        self.assertIn(
            "require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)",
            LOG_EXPORT,
        )

    def test_usage_export_requires_admin_permission(self) -> None:
        self.assertIn(
            "require_permission(Permission.FULL_ADMIN_PANEL_ACCESS)",
            USAGE_EXPORT,
        )
        self.assertIn(
            "StreamingResponse",
            USAGE_EXPORT,
        )


if __name__ == "__main__":
    unittest.main()
