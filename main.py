import os

from character import Character
from wallet import Wallet
from typing import Dict

character_super_powers: Dict[str, int] = {
    "reading": 81,
    "running": 55,
    "dancing": 60,
    "jumping": 70,
    "invisibility": 45,
    "blink": 80,
}

# create initial wallet balances for characters
jake_balances: Dict[str, int] = {"USD": 50, "EUR": 70, "GBP": 65}
mina_balances: Dict[str, int] = {"USD": 80, "EUR": 85, "GBP": 45}


# create wallet for characters
jake_wallet = Wallet("Jake", jake_balances)
mina_wallet = Wallet("Mina", mina_balances)

# create characters with wallet
jake = Character("Jake", jake_wallet)
mina = Character("Mina", mina_wallet)

# print initial balances
print(f"{jake.name}'s balances: {jake.wallet.balances}")
print(f"{mina.name}'s balances: {mina.wallet.balances}")

# transfer money from Mina to Jake
mina.give_money(jake, "USD", 10)

# print updated balances
print(f"{jake.name}'s balances: {jake.wallet.balances}")
print(f"{mina.name}'s balances: {mina.wallet.balances}")

# transfer money from Jake to Mina
jake.give_money(mina, "GBP", 65)

# print updated balances
print(f"{jake.name}'s balances: {jake.wallet.balances}")
print(f"{mina.name}'s balances: {mina.wallet.balances}")

# transfer money from Jake to Mina to test insufficient funds
jake.give_money(mina, "GBP", 10)

# print give_money()  not enough currency
print(f"{jake.name}'s balances: {jake.wallet.balances}")

# spend money response when insufficient funds
# print(jake.wallet.spend_money("GBP", 70))

# write balance to csv file
jake_wallet.export_to_csv("jake_balances.csv")
mina_wallet.export_to_csv("mina_balances.csv")

jake_wallet.export_to_json("jake_balances.json")
mina_wallet.export_to_json("mina_balances.json")

jake_csv_path = "jake_balances.csv"
mina_csv_path = "mina_balances.csv"

if os.path.exists(jake_csv_path):
    print("Jakes wallet csv", jake_wallet.load_from_csv(jake_csv_path))
else:
    print(f"CSV file '{jake_csv_path}' does not exist.")

if os.path.exists(mina_csv_path):
    print("Minas wallet csv", mina_wallet.load_from_csv(mina_csv_path))
else:
    print(f"CSV file '{mina_csv_path}' does not exist.")

print("Jake wallet json>>", jake_wallet.load_from_json("jake_balances.json"))
print("Mina wallet json>>", mina_wallet.load_from_json("mina_balances.json"))


# def main():
#
#
#
# if __name__ == "__main__":
#     main()
