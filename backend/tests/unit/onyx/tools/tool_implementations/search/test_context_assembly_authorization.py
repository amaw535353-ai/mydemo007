import unittest
from types import SimpleNamespace
from unittest.mock import patch

from onyx.configs.constants import DocumentSource
from onyx.context.search.models import InferenceChunk
from onyx.context.search.utils import (
    inference_section_from_chunks,
)
from onyx.tools.tool_implementations.search.search_tool import (
    _recensor_expanded_sections,
)
import onyx.tools.tool_implementations.search.search_tool as search_tool
from onyx.tools.tool_implementations.utils import (
    convert_inference_sections_to_llm_string,
)


SECRET = (
    "SYNTHETIC-UNAUTHORIZED-ADJACENT-CONTENT"
)

SAFE = "AUTHORIZED-CENTER-CONTENT"


def make_chunk(
    *,
    chunk_id: int,
    content: str,
) -> InferenceChunk:
    return InferenceChunk.model_construct(
        chunk_id=chunk_id,
        blurb=content,
        content=content,
        source_links=None,
        image_file_id=None,
        section_continuation=False,
        document_id="synthetic-salesforce-document",
        source_type=DocumentSource.SALESFORCE,
        semantic_identifier="Synthetic Salesforce Record",
        title="Synthetic Salesforce Record",
        boost=0,
        score=1.0,
        hidden=False,
        is_relevant=None,
        relevance_explanation=None,
        metadata={},
        match_highlights=[],
        doc_summary="",
        chunk_context="",
        updated_at=None,
        primary_owners=None,
        secondary_owners=None,
        large_chunk_reference_ids=[],
        is_federated=False,
        file_id=None,
    )


class TestContextAssemblyAuthorization(
    unittest.TestCase
):
    def setUp(self) -> None:
        self.user = SimpleNamespace(
            id="synthetic-user-alice",
            email="alice@tenant-alpha.test",
            is_anonymous=False,
        )

        self.center = make_chunk(
            chunk_id=0,
            content=SAFE,
        )

        self.secret = make_chunk(
            chunk_id=1,
            content=SECRET,
        )

        self.section = (
            inference_section_from_chunks(
                center_chunk=self.center,
                chunks=[
                    self.center,
                    self.secret,
                ],
            )
        )

        assert self.section is not None

    def test_expanded_unauthorized_chunk_removed(
        self,
    ) -> None:
        def censor(*, chunks, user):
            self.assertEqual(
                user.email,
                "alice@tenant-alpha.test",
            )

            return [
                chunk
                for chunk in chunks
                if chunk.content != SECRET
            ]

        with patch.object(
            search_tool,
            "fetch_ee_implementation_or_noop",
            return_value=censor,
        ):
            result = _recensor_expanded_sections(
                [self.section],
                self.user,
            )

        self.assertEqual(
            len(result),
            1,
        )

        self.assertIn(
            SAFE,
            result[0].combined_content,
        )

        self.assertNotIn(
            SECRET,
            result[0].combined_content,
        )

    def test_removed_center_drops_entire_section(
        self,
    ) -> None:
        def censor(*, chunks, user):
            return [
                chunk
                for chunk in chunks
                if chunk.unique_id
                != self.center.unique_id
            ]

        with patch.object(
            search_tool,
            "fetch_ee_implementation_or_noop",
            return_value=censor,
        ):
            result = _recensor_expanded_sections(
                [self.section],
                self.user,
            )

        self.assertEqual(
            result,
            [],
        )

    def test_llm_context_uses_only_recensored_content(
        self,
    ) -> None:
        def censor(*, chunks, user):
            return [self.center]

        with patch.object(
            search_tool,
            "fetch_ee_implementation_or_noop",
            return_value=censor,
        ):
            safe_sections = (
                _recensor_expanded_sections(
                    [self.section],
                    self.user,
                )
            )

        docs_str, citation_mapping = (
            convert_inference_sections_to_llm_string(
                top_sections=safe_sections,
            )
        )

        self.assertIn(
            SAFE,
            docs_str,
        )

        self.assertNotIn(
            SECRET,
            docs_str,
        )

        self.assertEqual(
            citation_mapping,
            {
                1: "synthetic-salesforce-document",
            },
        )

    def test_no_safe_section_produces_no_citation(
        self,
    ) -> None:
        def censor(*, chunks, user):
            return []

        with patch.object(
            search_tool,
            "fetch_ee_implementation_or_noop",
            return_value=censor,
        ):
            safe_sections = (
                _recensor_expanded_sections(
                    [self.section],
                    self.user,
                )
            )

        docs_str, citation_mapping = (
            convert_inference_sections_to_llm_string(
                top_sections=safe_sections,
            )
        )

        self.assertEqual(
            citation_mapping,
            {},
        )

        self.assertNotIn(
            SECRET,
            docs_str,
        )


if __name__ == "__main__":
    unittest.main()
