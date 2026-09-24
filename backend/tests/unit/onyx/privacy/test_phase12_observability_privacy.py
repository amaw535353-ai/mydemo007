import unittest
from pathlib import Path


INCOGNITO = Path("onyx/tracing/incognito.py").read_text()
MASKING = Path("onyx/tracing/masking.py").read_text()
TELEMETRY = Path("onyx/utils/telemetry.py").read_text()
BACKGROUND = Path("onyx/background/error_logging.py").read_text()
BRAINTRUST = Path(
    "onyx/tracing/braintrust_tracing_processor.py"
).read_text()
LANGFUSE = Path(
    "onyx/tracing/langfuse_tracing_processor.py"
).read_text()


class TestPhase12ObservabilityPrivacy(unittest.TestCase):
    def test_incognito_can_suppress_external_tracing(self) -> None:
        self.assertIn(
            "not mode.emits_external_traces",
            INCOGNITO,
        )
        self.assertIn(
            "suppresses_external_traces()",
            BRAINTRUST,
        )
        self.assertIn(
            "suppresses_external_traces()",
            LANGFUSE,
        )

    def test_trace_masking_handles_auth_and_private_keys(self) -> None:
        self.assertIn(
            '"private_key" in key.lower()',
            MASKING,
        )
        self.assertIn(
            '"authorization" in key.lower()',
            MASKING,
        )
        self.assertIn(
            "***REDACTED***",
            MASKING,
        )

    def test_langfuse_applies_shared_masking(self) -> None:
        self.assertIn(
            "mask_sensitive_data",
            LANGFUSE,
        )

    def test_telemetry_has_disable_gate_and_explicit_payload(self) -> None:
        self.assertIn(
            "if DISABLE_TELEMETRY:",
            TELEMETRY,
        )
        self.assertIn(
            '"data": data',
            TELEMETRY,
        )
        self.assertIn(
            '"user_id": user_id',
            TELEMETRY,
        )
        self.assertIn(
            '"customer_uuid": customer_uuid',
            TELEMETRY,
        )

    def test_background_error_can_persist_original_message(self) -> None:
        self.assertIn(
            "create_background_error",
            BACKGROUND,
        )
        self.assertIn(
            "Original message: {message}",
            BACKGROUND,
        )


if __name__ == "__main__":
    unittest.main()
