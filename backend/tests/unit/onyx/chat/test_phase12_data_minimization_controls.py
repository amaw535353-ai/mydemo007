import unittest
from pathlib import Path


INCOGNITO = Path(
    "onyx/chat/incognito.py"
).read_text()

CONTEXT = Path(
    "onyx/chat/incognito_context.py"
).read_text()

CHAT = Path(
    "onyx/db/chat.py"
).read_text()


class TestPhase12DataMinimizationControls(
    unittest.TestCase
):
    def test_content_free_context_has_ttl_and_size_bounds(
        self,
    ) -> None:
        self.assertIn(
            "INCOGNITO_CONTEXT_TTL_SECONDS = 3600",
            CONTEXT,
        )

        self.assertIn(
            "_MAX_CONTEXT_MESSAGES = 200",
            CONTEXT,
        )

        self.assertIn(
            "_MAX_CONTEXT_BYTES = 1_000_000",
            CONTEXT,
        )

    def test_content_free_context_strips_images(
        self,
    ) -> None:
        self.assertIn(
            'model_copy(update={"image_files": None, '
            '"image_token_count": 0})',
            CONTEXT,
        )

    def test_provider_retention_suppression_exists(
        self,
    ) -> None:
        self.assertIn(
            'return {"store": False}',
            INCOGNITO,
        )

        self.assertIn(
            '"data_collection": "deny"',
            INCOGNITO,
        )

        self.assertIn(
            "LITELLM_PROXY_REDACTION_HEADER",
            INCOGNITO,
        )

    def test_content_free_chat_title_is_not_persisted(
        self,
    ) -> None:
        self.assertIn(
            "record_mode_persists_content(",
            CHAT,
        )

        self.assertIn(
            "chat_session.description = description",
            CHAT,
        )

        self.assertIn(
            "content-free session never stores",
            CHAT,
        )

    def test_content_free_file_descriptor_omits_filename(
        self,
    ) -> None:
        start = INCOGNITO.index(
            "def content_free_file_descriptors("
        )

        end = INCOGNITO.index(
            "\ndef ",
            start + 10,
        )

        block = INCOGNITO[start:end]

        self.assertIn(
            'id=fd["id"]',
            block,
        )

        self.assertIn(
            'type=fd["type"]',
            block,
        )

        self.assertNotIn(
            "display_name",
            block,
        )


if __name__ == "__main__":
    unittest.main()
