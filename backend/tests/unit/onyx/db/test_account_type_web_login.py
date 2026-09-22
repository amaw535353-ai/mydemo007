import unittest

from onyx.db.enums import AccountType


class TestAccountTypeWebLogin(unittest.TestCase):
    def test_service_account_cannot_web_login(self) -> None:
        self.assertFalse(AccountType.SERVICE_ACCOUNT.is_web_login())

    def test_standard_account_can_still_web_login(self) -> None:
        self.assertTrue(AccountType.STANDARD.is_web_login())

    def test_existing_placeholder_types_remain_non_web_login(self) -> None:
        self.assertFalse(AccountType.BOT.is_web_login())
        self.assertFalse(AccountType.EXT_PERM_USER.is_web_login())


if __name__ == "__main__":
    unittest.main()
