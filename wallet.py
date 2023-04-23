from typing import Dict


# In the code for your super-power character, replace your character’s wallet with an instance
#    of the class Wallet, instead of a simple dictionary. Feel free to change or enhance that class
#    to better suit your needs. It’s probably a good idea to keep that class in a separate module
#     (like wallet.py maybe)
class Wallet:
    def __init__(self, name: str, initial_balances: Dict[str, int] = {}):
        self.name = name
        self.balances = initial_balances

    def spend_money(self, currency: str, amount: int) -> int:
        if self.get_balance_for(currency) >= amount:
            self.balances[currency] -= amount
            return self.balances[currency]
        else:
            return f"Insufficient funds  {self.balances[currency]}"

    def deposit_money(self, currency: str, amount: int) -> int:
        if currency in self.balances:
            self.balances[currency] += amount
        else:
            self.balances[currency] = amount
            return self.balances[currency]

    def get_balance_for(self, currency: str) -> int:
        return self.balances.get(currency, 0)
