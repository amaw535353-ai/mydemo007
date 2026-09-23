import json
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from onyx.access.models import DocumentAccess
from onyx.document_index.interfaces_new import (
    MetadataUpdateRequest,
    SecondaryIndexDocumentMissingError,
    TenantState,
)
from onyx.document_index.opensearch.client import (
    OpenSearchDocumentMissingError,
)
from onyx.document_index.opensearch.opensearch_document_index import (
    OpenSearchDocumentIndex,
    OpenSearchIndexPair,
)
from onyx.document_index.opensearch.schema import (
    ACCESS_CONTROL_LIST_FIELD_NAME,
    PUBLIC_FIELD_NAME,
    get_opensearch_doc_chunk_id,
)


def make_index(
    tenant_id: str = "synthetic",
    multitenant: bool = False,
):
    index = OpenSearchDocumentIndex.__new__(
        OpenSearchDocumentIndex
    )

    client = MagicMock()

    index._client = client
    index._tenant_state = TenantState(
        tenant_id=tenant_id,
        multitenant=multitenant,
    )
    index._index_name = "synthetic-index"

    return index, client


def request_for(
    is_public: bool,
):
    access = DocumentAccess.build(
        user_emails=(
            []
            if is_public
            else ["alice@tenant-alpha.test"]
        ),
        user_groups=[],
        external_user_emails=[],
        external_user_group_ids=[],
        is_public=is_public,
    )

    return MetadataUpdateRequest(
        document_ids=["synthetic-doc"],
        doc_id_to_chunk_cnt={
            "synthetic-doc": 1
        },
        access=access,
    )


class TestRevocationIndexConsistency(
    unittest.TestCase
):
    def test_public_to_private_updates_public_and_acl(
        self,
    ) -> None:
        index, client = make_index()

        index.update([
            request_for(False)
        ])

        props = (
            client.bulk_update_documents
            .call_args.kwargs[
                "properties_to_update"
            ]
        )

        self.assertIn(
            ACCESS_CONTROL_LIST_FIELD_NAME,
            props,
        )

        self.assertIn(
            PUBLIC_FIELD_NAME,
            props,
        )

        self.assertFalse(
            props[PUBLIC_FIELD_NAME]
        )

        self.assertTrue(
            props[
                ACCESS_CONTROL_LIST_FIELD_NAME
            ]
        )

    def test_private_to_public_updates_public_true(
        self,
    ) -> None:
        index, client = make_index()

        index.update([
            request_for(True)
        ])

        props = (
            client.bulk_update_documents
            .call_args.kwargs[
                "properties_to_update"
            ]
        )

        self.assertTrue(
            props[PUBLIC_FIELD_NAME]
        )

        # Public marker is represented by
        # the dedicated public field, not ACL.
        self.assertEqual(
            props[
                ACCESS_CONTROL_LIST_FIELD_NAME
            ],
            [],
        )

    def test_multitenant_chunk_ids_are_distinct(
        self,
    ) -> None:
        alpha = get_opensearch_doc_chunk_id(
            tenant_state=TenantState(
                tenant_id="tenant-alpha",
                multitenant=True,
            ),
            document_id="same-doc",
            chunk_index=0,
        )

        beta = get_opensearch_doc_chunk_id(
            tenant_state=TenantState(
                tenant_id="tenant-beta",
                multitenant=True,
            ),
            document_id="same-doc",
            chunk_index=0,
        )

        self.assertNotEqual(
            alpha,
            beta,
        )

    def test_delete_query_is_tenant_scoped(
        self,
    ) -> None:
        index, client = make_index(
            tenant_id="tenant-alpha",
            multitenant=True,
        )

        index.delete(
            "synthetic-doc"
        )

        query = (
            client.delete_by_query
            .call_args.args[0]
        )

        serialized = json.dumps(query)

        self.assertIn(
            "tenant-alpha",
            serialized,
        )

        self.assertIn(
            "synthetic-doc",
            serialized,
        )

    def test_index_pair_delete_fans_out(
        self,
    ) -> None:
        pair = OpenSearchIndexPair.__new__(
            OpenSearchIndexPair
        )

        primary = MagicMock()
        secondary = MagicMock()

        primary.delete.return_value = 2
        secondary.delete.return_value = 3

        pair._primary = primary
        pair._secondary = secondary
        pair._primary_backfill_in_progress = False

        deleted = pair.delete(
            "synthetic-doc",
            5,
        )

        self.assertEqual(
            deleted,
            5,
        )

        primary.delete.assert_called_once_with(
            "synthetic-doc",
            5,
        )

        secondary.delete.assert_called_once_with(
            "synthetic-doc",
            5,
        )

    def test_backfill_missing_document_fails_deferred(
        self,
    ) -> None:
        pair = OpenSearchIndexPair.__new__(
            OpenSearchIndexPair
        )

        primary = MagicMock()

        primary.update.side_effect = (
            OpenSearchDocumentMissingError(
                ["chunk-1"],
                ["synthetic-doc"],
            )
        )

        pair._primary = primary
        pair._secondary = None
        pair._primary_backfill_in_progress = True

        with self.assertRaises(
            SecondaryIndexDocumentMissingError
        ) as ctx:
            pair.update([
                request_for(False)
            ])

        self.assertEqual(
            ctx.exception.document_ids,
            ["synthetic-doc"],
        )

    def test_sync_uses_last_modified_watermark(
        self,
    ) -> None:
        source = Path(
            "onyx/background/celery/"
            "tasks/vespa/tasks.py"
        ).read_text()

        self.assertIn(
            "doc_last_modified = "
            "doc.last_modified",
            source,
        )

        self.assertGreaterEqual(
            source.count(
                "synced_as_of="
                "doc_last_modified"
            ),
            2,
        )

        self.assertIn(
            "mark_document_"
            "synced_secondary_pending",
            source,
        )


if __name__ == "__main__":
    unittest.main()
