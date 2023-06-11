import unittest
from wallet import Wallet
from character import Character


class CharacterTest(unittest.TestCase):
    def test_give_money_with_sufficient_balance(self):
        wallet1 = Wallet("wallet 1")
        wallet2 = Wallet("wallet 2")
        John = Character("John", wallet1)
        Alice = Character("Alice", wallet2)

        # given
        wallet1.deposit_money("USD", 100)

        # when
        success = John.give_money(Alice, "USD", 50)

        # then
        self.assertTrue(success)
        self.assertEqual(wallet1.get_balance_for("USD"), 50)
        self.assertEqual(wallet2.get_balance_for("USD"), 50)

    def test_give_money_with_insufficient_balance(self):
        wallet1 = Wallet("wallet 1")
        wallet2 = Wallet("wallet 2")
        John = Character("John", wallet1)
        Alice = Character("Alice", wallet2)

        # given
        wallet1.deposit_money("USD", 10)

        # when
        success = John.give_money(Alice, "USD", 50)

        # then
        self.assertFalse(success)
        self.assertEqual(wallet1.get_balance_for("USD"), 10)
        self.assertEqual(wallet2.get_balance_for("USD"), 0)


if __name__ == "__main__":
    unittest.main()
