import unittest
from pathlib import Path
from unittest.mock import MagicMock

from onyx.server.query_and_chat.placement import Placement
from onyx.tools.interface import Tool
from onyx.tools.models import (
    ToolCallKickoff,
    ToolResponse,
)
from onyx.tools.tool_runner import run_tool_calls


class DummyTool(Tool[None]):
    def __init__(self, name: str):
        super().__init__(emitter=MagicMock())
        self._name = name
        self.run_count = 0
        self.start_count = 0

    @property
    def id(self) -> int:
        return 1

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return "Synthetic Phase 11 tool"

    @property
    def display_name(self) -> str:
        return self._name

    def tool_definition(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self._name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {},
                },
            },
        }

    def emit_start(self, placement: Placement) -> None:
        self.start_count += 1

    def run(
        self,
        placement: Placement,
        override_kwargs: None,
        **llm_kwargs,
    ) -> ToolResponse:
        self.run_count += 1
        return ToolResponse(
            rich_response=None,
            llm_facing_response="synthetic-ok",
        )


def call(name: str, call_id: str) -> ToolCallKickoff:
    return ToolCallKickoff(
        tool_call_id=call_id,
        tool_name=name,
        tool_args={},
        placement=Placement(
            turn_index=0,
            tab_index=0,
        ),
    )


def execute(calls, tools, cap=None):
    return run_tool_calls(
        tool_calls=calls,
        tools=tools,
        message_history=[],
        user_memory_context=None,
        user_info=None,
        citation_mapping={},
        next_citation_num=1,
        max_concurrent_tools=cap,
    )


class TestPhase11ToolAuthorityBoundaries(unittest.TestCase):
    def test_model_cannot_invent_unavailable_tool(self) -> None:
        available = DummyTool("authorized_tool")

        result = execute(
            [call("invented_admin_tool", "a")],
            [available],
            1,
        )

        self.assertEqual(
            result.tool_responses,
            [],
        )

        self.assertEqual(
            available.run_count,
            0,
        )

    def test_zero_execution_cap_prevents_tool_execution(self) -> None:
        tool = DummyTool("synthetic_tool")

        result = execute(
            [call("synthetic_tool", "a")],
            [tool],
            0,
        )

        self.assertEqual(
            result.tool_responses,
            [],
        )

        self.assertEqual(
            tool.run_count,
            0,
        )

    def test_execution_cap_limits_tool_batch(self) -> None:
        one = DummyTool("tool_one")
        two = DummyTool("tool_two")

        result = execute(
            [
                call("tool_one", "a"),
                call("tool_two", "b"),
            ],
            [one, two],
            1,
        )

        self.assertEqual(
            len(result.tool_responses),
            1,
        )

        self.assertEqual(
            one.run_count + two.run_count,
            1,
        )

    def test_constructor_uses_application_authority(self) -> None:
        source = Path(
            "onyx/tools/tool_constructor.py"
        ).read_text()

        self.assertIn(
            "if not db_tool_model.enabled:",
            source,
        )

        self.assertIn(
            "allowed_tool_ids is not None "
            "and db_tool_model.id not in allowed_tool_ids",
            source,
        )

        self.assertIn(
            "user_id=user.id",
            source,
        )

        self.assertIn(
            "resolve_mcp_credentials("
            "mcp_server, user, db_session",
            source,
        )


if __name__ == "__main__":
    unittest.main()
