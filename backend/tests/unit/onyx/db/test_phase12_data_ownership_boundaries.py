import unittest
from pathlib import Path


CHAT = Path(
    "onyx/db/chat.py"
).read_text()

MEMORY = Path(
    "onyx/db/memory.py"
).read_text()

CREDENTIALS = Path(
    "onyx/db/credentials.py"
).read_text()

USER_FILES = Path(
    "onyx/db/user_file.py"
).read_text()


class TestPhase12DataOwnershipBoundaries(
    unittest.TestCase
):
    def test_chat_session_and_message_owner_checks_exist(
        self,
    ) -> None:
        self.assertIn(
            "ChatSession.user_id == user_id",
            CHAT,
        )

        self.assertIn(
            "expected_user_id != user_id",
            CHAT,
        )

        self.assertIn(
            "Chat message does not belong to user",
            CHAT,
        )

    def test_memory_reads_and_updates_are_user_scoped(
        self,
    ) -> None:
        self.assertIn(
            "Memory.user_id == user.id",
            MEMORY,
        )

        self.assertGreaterEqual(
            MEMORY.count(
                "Memory.user_id == user_id"
            ),
            2,
        )

        self.assertIn(
            "user_id=user.id",
            MEMORY,
        )

    def test_credential_reads_apply_user_filter(
        self,
    ) -> None:
        self.assertIn(
            "Credential.user_id == user.id",
            CREDENTIALS,
        )

        self.assertIn(
            "Anonymous users are not allowed "
            "to access credentials",
            CREDENTIALS,
        )

        self.assertIn(
            "fetch_credential_by_id_for_user",
            CREDENTIALS,
        )

    def test_user_file_module_contains_owner_scoped_paths(
        self,
    ) -> None:
        self.assertGreaterEqual(
            USER_FILES.count(
                "UserFile.user_id == user_id"
            ),
            2,
        )

        # This low-level helper is deliberately ID-only.
        # It must not be treated as a complete authorization API.
        self.assertIn(
            "def get_user_file_by_id(",
            USER_FILES,
        )

        self.assertIn(
            "fetch_user_files_with_access_relationships",
            USER_FILES,
        )


if __name__ == "__main__":
    unittest.main()
