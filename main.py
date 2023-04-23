# import py_character
from character import Character
from wallet import Wallet
from typing import Dict

py_character_wallet = Wallet("py_character's multi-currency wallet")
py_character = Character("Neo", py_character_wallet)

character_super_powers: Dict[str, int] = {
    "reading": 81,
    "running": 55,
    "dancing": 60,
    "jumping": 70,
    "invisibility": 45,
    "blink": 80,
}
py_character_initial_balances = {"dollars": 170.0, "pounds": 50.0, "euros": 38.0}
py_character_wallet.balances = py_character_initial_balances


def main():
    print(py_character.super_powers_at_or_above_given_number(character_super_powers, 70))
    print(py_character_wallet.spend_money("dollars", 38))


if __name__ == "__main__":
    main()
