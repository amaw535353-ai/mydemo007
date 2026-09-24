import unittest
from pathlib import Path

from onyx.db.enums import (
    EndpointPolicy,
    GatedAppKind,
)
from onyx.external_apps.matching.engine import (
    AllMatchedActions,
    GatedTarget,
    MatchedAction,
    actions_requiring_approval,
)


def make_action(
    name: str,
    policy: EndpointPolicy,
) -> MatchedAction:
    return MatchedAction(
        action_type=name,
        display_name=name,
        description=name,
        policy=policy,
    )


class TestPhase11ActionApprovalBoundaries(unittest.TestCase):
    def test_strictest_policy_governs_batch(
        self,
    ) -> None:
        matched = AllMatchedActions(
            actions=(
                make_action(
                    "read",
                    EndpointPolicy.ALWAYS,
                ),
                make_action(
                    "write",
                    EndpointPolicy.ASK,
                ),
                make_action(
                    "delete",
                    EndpointPolicy.DENY,
                ),
            ),
            target=GatedTarget(
                kind=GatedAppKind.EXTERNAL_APP,
                id=42,
                app_name="Synthetic",
            ),
        )

        self.assertEqual(
            matched.governing_action.policy,
            EndpointPolicy.DENY,
        )

    def test_only_ask_actions_enter_approval_scope(
        self,
    ) -> None:
        self.assertEqual(
            actions_requiring_approval(
                (
                    make_action(
                        "read",
                        EndpointPolicy.ALWAYS,
                    ),
                    make_action(
                        "write",
                        EndpointPolicy.ASK,
                    ),
                    make_action(
                        "delete",
                        EndpointPolicy.DENY,
                    ),
                )
            ),
            ["write"],
        )

    def test_mcp_defaults_to_ask_and_unclassified_denies(
        self,
    ) -> None:
        source = Path(
            "onyx/sandbox_proxy/"
            "request_evaluator.py"
        ).read_text()

        self.assertIn(
            "MCP_TOOL_DEFAULT_POLICY = "
            "EndpointPolicy.ASK",
            source,
        )

        self.assertIn(
            "MCP_UNCLASSIFIABLE_ACTION_TYPE",
            source,
        )

        self.assertIn(
            "policy=EndpointPolicy.DENY",
            source,
        )

    def test_session_authority_headers_removed_before_forward(
        self,
    ) -> None:
        source = Path(
            "onyx/sandbox_proxy/addons/gate.py"
        ).read_text()

        self.assertIn(
            'flow.request.headers.pop('
            '"Proxy-Authorization", None)',
            source,
        )

        self.assertIn(
            'flow.request.headers.pop('
            'MCP_SESSION_TAG_HEADER, None)',
            source,
        )

    def test_gate_contains_fail_closed_error_paths(
        self,
    ) -> None:
        source = Path(
            "onyx/sandbox_proxy/addons/gate.py"
        ).read_text()

        self.assertIn(
            "SandboxProxyError.POLICY_DENIED",
            source,
        )

        self.assertIn(
            "SandboxProxyError.INTERNAL_ERROR",
            source,
        )

        self.assertIn(
            "_dispatch_approved_request",
            source,
        )


if __name__ == "__main__":
    unittest.main()
