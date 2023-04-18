# import py_character
import py_character
from typing import Dict

character_super_powers: Dict[str, int] = {
    "reading": 81,
    "running": 55,
    "dancing": 60,
    "jumping": 70,
    "invisibility": 45,
    "blink": 80,
}
character_wallet: Dict[str, float] = {"dollars": 170.0, "pounds": 50.0, "euros": 38.0}



def main():
    print(py_character.super_powers_at_or_above_given_number(character_super_powers, 70))
    print(py_character.spend_money(character_wallet, "dollars", 38))


if __name__ == "__main__":
    main()
