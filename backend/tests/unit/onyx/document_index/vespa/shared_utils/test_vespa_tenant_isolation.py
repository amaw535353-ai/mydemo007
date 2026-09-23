import unittest
from unittest.mock import patch

from onyx.context.search.models import IndexFilters
import onyx.document_index.vespa.shared_utils.vespa_request_builders as builders


class TestVespaTenantIsolation(unittest.TestCase):
    def test_multitenant_missing_tenant_fails_closed(
        self,
    ) -> None:
        filters = IndexFilters(
            access_control_list=[],
            tenant_id=None,
        )

        with patch.object(
            builders,
            "MULTI_TENANT",
            True,
        ):
            with self.assertRaisesRegex(
                ValueError,
                "Tenant ID must be set",
            ):
                builders.build_vespa_filters(
                    filters,
                    remove_trailing_and=True,
                )

    def test_multitenant_filter_contains_exact_tenant(
        self,
    ) -> None:
        filters = IndexFilters(
            access_control_list=[],
            tenant_id="tenant-alpha-synthetic",
        )

        with patch.object(
            builders,
            "MULTI_TENANT",
            True,
        ):
            result = builders.build_vespa_filters(
                filters,
                remove_trailing_and=True,
            )

        self.assertIn(
            'tenant_id contains "tenant-alpha-synthetic"',
            result,
        )

        self.assertNotIn(
            "tenant-beta-synthetic",
            result,
        )

    def test_single_tenant_missing_tenant_remains_valid(
        self,
    ) -> None:
        filters = IndexFilters(
            access_control_list=[],
            tenant_id=None,
        )

        with patch.object(
            builders,
            "MULTI_TENANT",
            False,
        ):
            result = builders.build_vespa_filters(
                filters,
                remove_trailing_and=True,
            )

        self.assertNotIn(
            "tenant_id",
            result.lower(),
        )


if __name__ == "__main__":
    unittest.main()
