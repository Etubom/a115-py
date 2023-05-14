from typing import List, Dict, Tuple

# import wallet
from wallet import Wallet


class Character:
    def __init__(self, name: str, wallet: Wallet):
        self.name = name
        self.wallet = wallet

    def super_powers_at_or_above_given_number(
        self, my_dict: Dict, num: int
    ) -> List[str]:
        filtered_list_of_powers = []
        for key in my_dict:
            if my_dict[key] >= num:
                filtered_list_of_powers.append(key)
        return filtered_list_of_powers

    def give_money(self, other: "Character", currency: str, amount: int) -> bool:
        if self.wallet.get_balance_for(currency) >= amount:
            self.wallet.spend_money(currency, amount)
            other.wallet.deposit_money(currency, amount)

            print(f"{self.name} gave {other.name} {amount} {currency}.")
            return True

        print(f"{self.name} doesn't have enough {currency}.")
        return False
