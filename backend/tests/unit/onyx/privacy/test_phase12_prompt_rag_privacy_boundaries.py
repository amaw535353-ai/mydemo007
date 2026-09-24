import unittest
from pathlib import Path


ACCESS = Path(
    "onyx/context/search/preprocessing/access_filters.py"
).read_text()

PIPELINE = Path(
    "onyx/context/search/pipeline.py"
).read_text()

PROMPT = Path(
    "onyx/chat/prompt_utils.py"
).read_text()


class TestPhase12PromptRagPrivacyBoundaries(unittest.TestCase):
    def test_retrieval_acl_is_derived_from_user(self) -> None:
        self.assertIn(
            "get_acl_for_user",
            ACCESS,
        )
        self.assertIn(
            "access_control_list=user_acl_filters",
            ACCESS,
        )

    def test_document_set_override_is_permission_checked(self) -> None:
        self.assertIn(
            "filter_document_set_names_by_user_access",
            PIPELINE,
        )
        self.assertIn(
            "OnyxErrorCode.INSUFFICIENT_PERMISSIONS",
            PIPELINE,
        )

    def test_search_filters_carry_acl_and_tenant_boundary(self) -> None:
        self.assertIn(
            "access_control_list=user_acl_filters",
            PIPELINE,
        )
        self.assertIn(
            "tenant_id=get_current_tenant_id() if MULTI_TENANT else None",
            PIPELINE,
        )

    def test_post_query_censoring_boundary_exists(self) -> None:
        self.assertIn(
            "_post_query_chunk_censoring",
            PIPELINE,
        )

    def test_personalization_data_is_explicit_prompt_surface(self) -> None:
        self.assertIn(
            "USER_MEMORIES_PROMPT",
            PROMPT,
        )
        self.assertIn(
            "USER_PREFERENCES_PROMPT",
            PROMPT,
        )
        self.assertIn(
            "user_email=ctx.user_info.email",
            PROMPT,
        )


if __name__ == "__main__":
    unittest.main()
