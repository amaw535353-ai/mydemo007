import unittest
from unittest.mock import MagicMock

from onyx.configs.chat_configs import (
    MAX_LLM_CYCLES,
    MAX_TOOL_CALLS_PER_CYCLE,
)
from onyx.server.query_and_chat.placement import (
    Placement,
)
from onyx.tools.interface import Tool
from onyx.tools.models import (
    ToolCallKickoff,
    ToolResponse,
)
from onyx.tools.tool_runner import (
    TOOL_EXECUTION_TIMEOUT_SECONDS,
    run_tool_calls,
)


class DummyTool(Tool[None]):
    def __init__(
        self,
        tool_id: int,
        name: str,
    ):
        super().__init__(
            emitter=MagicMock()
        )
        self._tool_id = tool_id
        self._name = name
        self.run_count = 0

    @property
    def id(self) -> int:
        return self._tool_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return "synthetic resource test"

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

    def emit_start(
        self,
        placement: Placement,
    ) -> None:
        return None

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


def make_call(
    name: str,
    index: int,
) -> ToolCallKickoff:
    return ToolCallKickoff(
        tool_call_id=f"call-{index}",
        tool_name=name,
        tool_args={},
        placement=Placement(
            turn_index=0,
            tab_index=index,
        ),
    )


class TestPhase11AgentResourceBounds(
    unittest.TestCase
):
    def test_agent_cycle_and_tool_bounds_are_finite(
        self,
    ) -> None:
        self.assertGreater(
            MAX_LLM_CYCLES,
            0,
        )

        self.assertGreaterEqual(
            MAX_TOOL_CALLS_PER_CYCLE,
            0,
        )

        self.assertLessEqual(
            MAX_TOOL_CALLS_PER_CYCLE,
            10,
        )

        self.assertGreater(
            TOOL_EXECUTION_TIMEOUT_SECONDS,
            0,
        )

    def test_tool_runner_enforces_cycle_fanout_cap(
        self,
    ) -> None:
        tools = [
            DummyTool(
                i,
                f"synthetic_tool_{i}",
            )
            for i in range(12)
        ]

        calls = [
            make_call(
                tool.name,
                i,
            )
            for i, tool in enumerate(tools)
        ]

        result = run_tool_calls(
            tool_calls=calls,
            tools=tools,
            message_history=[],
            user_memory_context=None,
            user_info=None,
            citation_mapping={},
            next_citation_num=1,
            max_concurrent_tools=(
                MAX_TOOL_CALLS_PER_CYCLE
            ),
        )

        self.assertEqual(
            len(result.tool_responses),
            MAX_TOOL_CALLS_PER_CYCLE,
        )

        self.assertEqual(
            sum(
                tool.run_count
                for tool in tools
            ),
            MAX_TOOL_CALLS_PER_CYCLE,
        )

    def test_llm_loop_uses_application_cap(
        self,
    ) -> None:
        from pathlib import Path

        source = Path(
            "onyx/chat/llm_loop.py"
        ).read_text()

        self.assertIn(
            "for llm_cycle_count "
            "in range(MAX_LLM_CYCLES):",
            source,
        )

        self.assertIn(
            "max_concurrent_tools="
            "MAX_TOOL_CALLS_PER_CYCLE",
            source,
        )

        self.assertNotIn(
            "max_concurrent_tools=None",
            source,
        )


if __name__ == "__main__":
    unittest.main()
