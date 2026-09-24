import unittest
from pathlib import Path


CHAT = Path("onyx/db/chat.py").read_text()
FILE_STORE = Path("onyx/file_store/file_store.py").read_text()
MODELS = Path("onyx/db/models.py").read_text()
MIGRATION = Path(
    "alembic/versions/"
    "0d9c7b6a5e4f_retain_user_usage_after_user_deletion.py"
).read_text()


def class_block(name: str) -> str:
    marker = f"class {name}(Base):"
    start = MODELS.index(marker)

    next_class = MODELS.find(
        "\nclass ",
        start + len(marker),
    )

    if next_class == -1:
        return MODELS[start:]

    return MODELS[start:next_class]


MEMORY = class_block("Memory")
CHAT_SESSION = class_block("ChatSession")
USER_USAGE = class_block("UserUsage")


class TestPhase12RetentionDeletion(unittest.TestCase):
    def test_chat_hard_delete_path_removes_messages(self) -> None:
        self.assertIn(
            "delete_messages_and_files_from_chat_session",
            CHAT,
        )
        self.assertIn(
            "delete_all_chat_sessions_for_user",
            CHAT,
        )
        self.assertIn(
            "delete(ChatSession)",
            CHAT,
        )

    def test_file_store_has_physical_delete_path(self) -> None:
        self.assertIn(
            "def delete_file(",
            FILE_STORE,
        )
        self.assertIn(
            "delete_object(",
            FILE_STORE,
        )
        self.assertIn(
            "delete_filerecord_by_file_id",
            FILE_STORE,
        )

    def test_memory_and_chat_are_user_cascade_scoped(self) -> None:
        self.assertIn(
            'ForeignKey("user.id", ondelete="CASCADE")',
            MEMORY,
        )
        self.assertIn(
            'ForeignKey("user.id", ondelete="CASCADE")',
            CHAT_SESSION,
        )

    def test_user_usage_retains_row_without_direct_user_fk(self) -> None:
        self.assertIn(
            'ForeignKey("user.id", ondelete="SET NULL")',
            USER_USAGE,
        )
        self.assertIn(
            'ondelete="SET NULL"',
            MIGRATION,
        )

    def test_retained_usage_schema_is_accounting_metadata(self) -> None:
        expected_accounting_fields = (
            "input_tokens",
            "output_tokens",
            "cache_read_tokens",
            "cache_creation_tokens",
            "cost_cents",
            "model",
            "flow",
            "provider",
            "window_start",
        )

        for field in expected_accounting_fields:
            self.assertIn(
                field,
                USER_USAGE,
            )

        direct_content_fields = (
            "memory_text",
            "chat_message",
            "file_content",
            "prompt_text",
            "message_text",
        )

        for field in direct_content_fields:
            self.assertNotIn(
                field,
                USER_USAGE,
            )


if __name__ == "__main__":
    unittest.main()
