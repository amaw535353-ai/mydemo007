import ast
from pathlib import Path
import unittest


SOURCE = (
    Path(__file__).resolve().parents[5]
    / "onyx"
    / "db"
    / "engine"
    / "async_sql_engine.py"
)


def _top_level_functions() -> dict[str, ast.FunctionDef | ast.AsyncFunctionDef]:
    tree = ast.parse(SOURCE.read_text())
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def _arguments(
    function: ast.FunctionDef | ast.AsyncFunctionDef,
) -> tuple[str, ...]:
    arguments = (
        function.args.posonlyargs
        + function.args.args
        + function.args.kwonlyargs
    )
    return tuple(argument.arg for argument in arguments)


class TestAsyncSessionTenantBoundary(unittest.TestCase):
    def test_fastapi_dependency_exposes_no_tenant_parameter(self) -> None:
        functions = _top_level_functions()

        self.assertIn("get_async_session", functions)
        self.assertEqual(
            _arguments(functions["get_async_session"]),
            (),
        )

    def test_internal_context_manager_preserves_explicit_tenant_api(
        self,
    ) -> None:
        functions = _top_level_functions()

        self.assertIn("get_async_session_context_manager", functions)
        self.assertEqual(
            _arguments(functions["get_async_session_context_manager"]),
            ("tenant_id",),
        )

    def test_internal_generator_owns_explicit_tenant_selection(self) -> None:
        functions = _top_level_functions()

        self.assertIn("_get_async_session_for_tenant", functions)
        self.assertEqual(
            _arguments(functions["_get_async_session_for_tenant"]),
            ("tenant_id",),
        )


if __name__ == "__main__":
    unittest.main()
