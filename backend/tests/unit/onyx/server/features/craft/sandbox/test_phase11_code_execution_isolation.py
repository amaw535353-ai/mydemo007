import unittest
from pathlib import Path
from uuid import UUID

from onyx.server.features.build.sandbox.docker.docker_sandbox_manager import (
    build_container_create_kwargs,
)
from onyx.tools.tool_implementations.python.python_tool import (
    _safe_code_interpreter_filename,
)


class TestPhase11CodeExecutionIsolation(unittest.TestCase):
    def test_python_staged_filename_has_no_path_separator(
        self,
    ) -> None:
        safe = _safe_code_interpreter_filename(
            "../../etc/passwd"
        )

        self.assertNotIn("/", safe)
        self.assertNotIn("\\", safe)

    def test_container_security_posture(
        self,
    ) -> None:
        kwargs = build_container_create_kwargs(
            sandbox_id=UUID(
                "11111111-1111-1111-1111-111111111111"
            ),
            user_id=UUID(
                "22222222-2222-2222-2222-222222222222"
            ),
            tenant_id="tenant-alpha",
            image="onyx-sandbox:test",
            onyx_pat="synthetic-placeholder",
            api_server_url=(
                "https://onyx.example.test/api"
            ),
            network="onyx_craft_sandbox",
            volume_name="synthetic-volume",
            memory_limit="1g",
            cpu_limit=1.0,
            opencode_password="synthetic-password",
            opencode_config_json="{}",
            provisioning_attempt_number=1,
            sandbox_proxy_host="sandbox-proxy",
            proxy_ca_volume_name="sandbox-proxy-ca",
        )

        self.assertEqual(
            kwargs["cap_drop"],
            ["ALL"],
        )

        self.assertIn(
            "no-new-privileges:true",
            kwargs["security_opt"],
        )

        self.assertFalse(
            kwargs["privileged"]
        )

        self.assertEqual(
            kwargs["mem_limit"],
            "1g",
        )

        self.assertGreater(
            kwargs["nano_cpus"],
            0,
        )

        volume_binds = {
            v["bind"]
            for v in kwargs["volumes"].values()
        }

        self.assertNotIn(
            "/var/run/docker.sock",
            volume_binds,
        )

    def test_filesystem_listing_rejects_traversal_and_symlink_escape(
        self,
    ) -> None:
        source = Path(
            "onyx/server/features/build/sandbox/"
            "image/sandbox_daemon/filesystem.py"
        ).read_text()

        self.assertIn(
            'if any(part == ".." '
            "for part in path_obj.parts)",
            source,
        )

        self.assertIn(
            "is_relative_to("
            "session_root_resolved",
            source,
        )

        self.assertIn(
            "session_root.is_symlink()",
            source,
        )

    def test_python_staging_and_timeout_are_bounded(
        self,
    ) -> None:
        source = Path(
            "onyx/tools/tool_implementations/"
            "python/python_tool.py"
        ).read_text()

        self.assertIn(
            "CODE_INTERPRETER_MAX_STAGED_BYTES",
            source,
        )

        self.assertIn(
            "CODE_INTERPRETER_MAX_STAGED_FILES",
            source,
        )

        self.assertIn(
            "CODE_INTERPRETER_STAGING_CONCURRENCY",
            source,
        )

        self.assertIn(
            "CODE_INTERPRETER_DEFAULT_TIMEOUT_MS",
            source,
        )


if __name__ == "__main__":
    unittest.main()
