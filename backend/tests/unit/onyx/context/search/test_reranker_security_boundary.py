import ast
import asyncio
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from onyx.context.search import pipeline
from onyx.context.search.models import (
    ChunkSearchRequest,
    IndexFilters,
)
import onyx.natural_language_processing.search_nlp_models as nlp
from shared_configs.enums import RerankerProvider


QUERY = "synthetic authorized search"
AUTHORIZED = object()
UNAUTHORIZED = object()

SENTINEL = (
    "TENANT-ALPHA-CONFIDENTIAL-RERANK-SENTINEL"
)

ACTIVE_SEARCH_FILES = [
    Path("onyx/context/search/pipeline.py"),
    Path(
        "onyx/context/search/retrieval/"
        "search_runner.py"
    ),
    Path(
        "onyx/tools/tool_implementations/"
        "search/search_tool.py"
    ),
]

FORBIDDEN_ACTIVE_SYMBOLS = [
    "RerankingModel",
    "cohere_rerank_api",
    "cohere_rerank_aws",
    "litellm_rerank",
    "cross-encoder-scores",
]


class TestRerankerSecurityBoundary(
    unittest.TestCase
):
    def test_old_reranker_not_reachable_from_active_search(
        self,
    ) -> None:
        for path in ACTIVE_SEARCH_FILES:
            source = path.read_text()

            for symbol in FORBIDDEN_ACTIVE_SYMBOLS:
                self.assertNotIn(
                    symbol,
                    source,
                    msg=(
                        f"{symbol!r} became reachable "
                        f"from {path}"
                    ),
                )

    def test_active_pipeline_censors_retrieved_candidates(
        self,
    ) -> None:
        request = ChunkSearchRequest(
            query=QUERY,
            bypass_acl=False,
            limit=10,
        )

        user = SimpleNamespace(
            id="synthetic-user-alice",
            is_anonymous=False,
        )

        filters = IndexFilters(
            access_control_list=[
                "user:alice@tenant-alpha.test"
            ]
        )

        def censor(*, chunks, user):
            self.assertEqual(
                chunks,
                [AUTHORIZED, UNAUTHORIZED],
            )
            self.assertEqual(
                user.id,
                "synthetic-user-alice",
            )
            return [AUTHORIZED]

        with (
            patch.object(
                pipeline,
                "_build_index_filters",
                return_value=filters,
            ),
            patch.object(
                pipeline,
                "strip_stopwords",
                return_value=[],
            ),
            patch.object(
                pipeline,
                "search_chunks",
                return_value=[
                    AUTHORIZED,
                    UNAUTHORIZED,
                ],
            ),
            patch.object(
                pipeline,
                "fetch_ee_implementation_or_noop",
                return_value=censor,
            ),
        ):
            result = pipeline.search_pipeline(
                chunk_search_request=request,
                document_index=object(),
                user=user,
                persona_search_info=None,
                db_session=None,
                acl_filters=[
                    "user:alice@tenant-alpha.test"
                ],
            )

        self.assertEqual(
            result,
            [AUTHORIZED],
        )

        self.assertNotIn(
            UNAUTHORIZED,
            result,
        )

    def test_reranking_settings_removed_from_schema_migration(
        self,
    ) -> None:
        source = Path(
            "alembic/versions/"
            "78ebc66946a0_"
            "remove_reranking_from_search_settings.py"
        ).read_text()

        removed_fields = [
            "disable_rerank_for_streaming",
            "rerank_model_name",
            "rerank_provider_type",
            "rerank_api_key",
            "rerank_api_url",
            "num_rerank",
        ]

        for field in removed_fields:
            self.assertIn(
                f'op.drop_column("search_settings", "{field}")',
                source,
            )

    def test_legacy_local_reranker_is_not_executable(
        self,
    ) -> None:
        source = Path(
            "model_server/legacy/reranker.py"
        ).read_text()

        tree = ast.parse(source)

        self.assertEqual(
            tree.body,
            [],
        )

    def test_dormant_cloud_reranker_is_explicit_egress_boundary(
        self,
    ) -> None:
        model = nlp.RerankingModel(
            model_name="synthetic-reranker",
            provider_type=(
                RerankerProvider.COHERE
            ),
            api_key="synthetic-key",
            api_url=None,
        )

        async_mock = AsyncMock(
            return_value=[0.91]
        )

        with patch.object(
            nlp,
            "cohere_rerank_api",
            new=async_mock,
        ):
            result = asyncio.run(
                model._make_direct_rerank_call(
                    QUERY,
                    [SENTINEL],
                )
            )

        self.assertEqual(
            result,
            [0.91],
        )

        async_mock.assert_awaited_once()

        args = async_mock.await_args.args

        self.assertEqual(
            args[0],
            QUERY,
        )

        self.assertEqual(
            args[1],
            [SENTINEL],
        )

        self.assertEqual(
            args[2],
            "synthetic-reranker",
        )

        self.assertEqual(
            args[3],
            "synthetic-key",
        )


if __name__ == "__main__":
    unittest.main()
