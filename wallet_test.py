import unittest
from wallet import Wallet


class WalletTest(unittest.TestCase):
    def test_deposit_money(self):
        # given
        self.wallet = Wallet("test wallet")
        self.wallet.deposit_money("GBP", 100)
        # when
        self.wallet.deposit_money("GBP", 35)
        # then
        self.assertEqual(self.wallet.get_balance_for("GBP"), 135)

    def test_spend_money(self):
        # given
        self.wallet = Wallet("test wallet")
        self.wallet.deposit_money("USD", 100)
        # when
        self.wallet.spend_money("USD", 50)
        # then
        self.assertEqual(self.wallet.get_balance_for("USD"), 50)


if __name__ == "__main__":
    unittest.main()
