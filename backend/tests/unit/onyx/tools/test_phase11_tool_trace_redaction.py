import unittest
from pathlib import Path

from onyx.tools.tool_runner import (
    _tool_args_trace_summary,
    _tool_output_trace_summary,
)


class TestPhase11ToolTraceRedaction(unittest.TestCase):
    def test_argument_values_are_not_traced(self) -> None:
        secret = "sk-SYNTHETIC-SECRET-DO-NOT-RECORD"

        summary = _tool_args_trace_summary(
            {
                "api_key": secret,
                "requestBody": {
                    "password": secret,
                },
                "cmd": (
                    "curl -H Authorization:"
                    + secret
                ),
            }
        )

        rendered = str(summary)

        self.assertNotIn(
            secret,
            rendered,
        )

        self.assertEqual(
            summary["arg_count"],
            3,
        )

        self.assertEqual(
            summary["arg_names"],
            [
                "api_key",
                "cmd",
                "requestBody",
            ],
        )

    def test_nested_values_are_not_traced(self) -> None:
        secret = "SYNTHETIC-NESTED-PASSWORD"

        rendered = str(
            _tool_args_trace_summary(
                {
                    "requestBody": {
                        "credentials": {
                            "password": secret,
                        }
                    }
                }
            )
        )

        self.assertNotIn(
            secret,
            rendered,
        )

        self.assertNotIn(
            "password",
            rendered,
        )

    def test_output_content_is_not_traced(self) -> None:
        secret = "Bearer SYNTHETIC-RESPONSE-SECRET"

        summary = _tool_output_trace_summary(
            secret
        )

        self.assertNotIn(
            secret,
            summary,
        )

        self.assertEqual(
            summary,
            f"<tool output: {len(secret)} chars>",
        )

    def test_raw_trace_paths_are_removed(self) -> None:
        source = Path(
            "onyx/tools/tool_runner.py"
        ).read_text()

        self.assertNotIn(
            "span_fn.span_data.input = "
            "str(tool_call.tool_args)",
            source,
        )

        self.assertNotIn(
            "span_fn.span_data.output = "
            "tool_response.llm_facing_response",
            source,
        )

        self.assertNotIn(
            '"tool_args": tool_call.tool_args,',
            source,
        )


if __name__ == "__main__":
    unittest.main()
