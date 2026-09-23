import asyncio
import unittest
from unittest.mock import AsyncMock, MagicMock, Mock, patch

from tenacity import wait_none

import onyx.natural_language_processing.search_nlp_models as nlp
from onyx.configs.constants import DocumentSource
from onyx.connectors.models import Document, TextSection
from onyx.indexing.embedder import DefaultIndexingEmbedder
from onyx.indexing.models import DocAwareChunk
from shared_configs.enums import EmbeddingProvider, EmbedTextType
from shared_configs.model_server_models import EmbedRequest


SENTINEL = (
    "TENANT-ALPHA-CONFIDENTIAL-EMBEDDING-SENTINEL"
)

API_KEY = "sk-synthetic-1234567890"


class FakeCloudEmbedding:
    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ):
        return None

    async def embed(self, **kwargs):
        return [None]


class TestEmbeddingSecurityBoundaries(
    unittest.TestCase
):
    def test_empty_embedding_error_does_not_echo_input(
        self,
    ) -> None:
        model = nlp.EmbeddingModel.__new__(
            nlp.EmbeddingModel
        )

        with self.assertRaises(
            ValueError
        ) as exc:
            model.encode(
                [SENTINEL, ""],
                EmbedTextType.PASSAGE,
            )

        self.assertNotIn(
            SENTINEL,
            str(exc.exception),
        )

    def test_provider_failure_does_not_log_raw_text(
        self,
    ) -> None:
        async def run() -> None:
            async with nlp.CloudEmbedding(
                API_KEY,
                EmbeddingProvider.OPENAI,
            ) as cloud:
                with (
                    patch.object(
                        cloud,
                        "_embed_openai",
                        new=AsyncMock(
                            side_effect=ValueError(
                                "synthetic-provider-failure"
                            )
                        ),
                    ),
                    patch.object(
                        nlp.CloudEmbedding.embed.retry,
                        "wait",
                        wait_none(),
                    ),
                    patch.object(
                        nlp.logger,
                        "debug",
                    ) as debug_log,
                    patch.object(
                        nlp.logger,
                        "warning",
                    ) as warning_log,
                ):
                    with self.assertRaises(
                        RuntimeError
                    ):
                        await cloud.embed(
                            texts=[SENTINEL],
                            text_type=(
                                EmbedTextType.PASSAGE
                            ),
                        )

                    calls = (
                        list(debug_log.call_args_list)
                        + list(
                            warning_log.call_args_list
                        )
                    )

                    for call in calls:
                        for arg in call.args:
                            self.assertNotIn(
                                SENTINEL,
                                str(arg),
                            )

                            self.assertNotIn(
                                API_KEY,
                                str(arg),
                            )

        asyncio.run(run())

    def test_none_embedding_error_does_not_echo_input(
        self,
    ) -> None:
        model = nlp.EmbeddingModel.__new__(
            nlp.EmbeddingModel
        )

        model.provider_type = (
            EmbeddingProvider.OPENAI
        )
        model.api_key = API_KEY
        model.api_url = None
        model.api_version = None

        request = EmbedRequest(
            texts=[SENTINEL],
            model_name="synthetic-model",
            max_context_length=32,
            normalize_embeddings=True,
            provider_type=(
                EmbeddingProvider.OPENAI
            ),
            text_type=(
                EmbedTextType.PASSAGE
            ),
        )

        with patch.object(
            nlp,
            "CloudEmbedding",
            return_value=FakeCloudEmbedding(),
        ):
            with self.assertRaises(
                ValueError
            ) as exc:
                asyncio.run(
                    model._make_direct_api_call(
                        request
                    )
                )

        self.assertNotIn(
            SENTINEL,
            str(exc.exception),
        )

    def test_local_model_server_gets_tenant_context(
        self,
    ) -> None:
        model = nlp.EmbeddingModel.__new__(
            nlp.EmbeddingModel
        )

        model.embed_server_endpoint = (
            "http://127.0.0.1:9999/"
            "encoder/bi-encoder-embed"
        )

        request = EmbedRequest(
            texts=["synthetic"],
            model_name="synthetic-model",
            max_context_length=32,
            normalize_embeddings=True,
            provider_type=None,
            text_type=EmbedTextType.PASSAGE,
        )

        response = Mock()
        response.status_code = 200
        response.raise_for_status = Mock()
        response.json.return_value = {
            "embeddings": [[0.1, 0.2]]
        }

        with patch.object(
            nlp.requests,
            "post",
            return_value=response,
        ) as post:
            result = (
                model._make_model_server_request(
                    request,
                    tenant_id=(
                        "tenant-alpha-synthetic"
                    ),
                    request_id=(
                        "request-synthetic-001"
                    ),
                )
            )

        self.assertEqual(
            result.embeddings,
            [[0.1, 0.2]],
        )

        kwargs = post.call_args.kwargs

        self.assertEqual(
            kwargs["headers"][
                "X-Onyx-Tenant-ID"
            ],
            "tenant-alpha-synthetic",
        )

        self.assertEqual(
            kwargs["headers"][
                "X-Onyx-Request-ID"
            ],
            "request-synthetic-001",
        )

    def test_indexing_embedder_propagates_context(
        self,
    ) -> None:
        embedder = (
            DefaultIndexingEmbedder.__new__(
                DefaultIndexingEmbedder
            )
        )

        embedding_model = MagicMock()

        embedding_model.encode.side_effect = [
            [[0.1, 0.2]],
            [[0.3, 0.4]],
        ]

        embedder.embedding_model = (
            embedding_model
        )

        document = Document(
            id="synthetic-document",
            source=DocumentSource.FILE,
            semantic_identifier=(
                "Synthetic Document"
            ),
            metadata={},
            sections=[
                TextSection(
                    text="synthetic content",
                    link=None,
                )
            ],
        )

        chunk = DocAwareChunk(
            chunk_id=0,
            blurb="synthetic",
            content="synthetic content",
            source_links=None,
            image_file_id=None,
            section_continuation=False,
            source_document=document,
            title_prefix="",
            metadata_suffix_semantic="",
            metadata_suffix_keyword="",
            contextual_rag_reserved_tokens=0,
            doc_summary="",
            chunk_context="",
            mini_chunk_texts=None,
            large_chunk_id=None,
            large_chunk_reference_ids=[],
        )

        result = embedder.embed_chunks(
            [chunk],
            tenant_id=(
                "tenant-alpha-synthetic"
            ),
            request_id=(
                "request-synthetic-001"
            ),
        )

        self.assertEqual(
            len(result),
            1,
        )

        self.assertEqual(
            embedding_model.encode.call_count,
            2,
        )

        for call in (
            embedding_model.encode.call_args_list
        ):
            self.assertEqual(
                call.kwargs["tenant_id"],
                "tenant-alpha-synthetic",
            )

            self.assertEqual(
                call.kwargs["request_id"],
                "request-synthetic-001",
            )


if __name__ == "__main__":
    unittest.main()
