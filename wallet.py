from typing import Dict


class InsufficientFundsException(Exception):
    pass


class Wallet:
    def __init__(self, name: str, initial_balances: Dict[str, int] = {}):
        self.name = name
        self.balances = initial_balances

    def spend_money(self, currency: str, amount: int) -> int:
        if self.get_balance_for(currency) >= amount:
            self.balances[currency] -= amount
            return self.balances[currency]

        raise InsufficientFundsException(
            f"Insufficient funds  {self.balances[currency]}"
        )

    def deposit_money(self, currency: str, amount: int) -> int:
        self.balances[currency] = self.balances.get(currency, 0) + amount
        return self.balances[currency]

    def get_balance_for(self, currency: str) -> int:
        return self.balances.get(currency, 0)
