import csv
import json
from typing import Dict, List, Any


class InsufficientFundsException(Exception):
    pass


class Wallet:
    def __init__(self, name: str, initial_balances: Dict[str, int] = {}):
        self.name = name
        self.balances = initial_balances

    def spend_money(self, currency: str, amount: int) -> int:
        if currency in self.balances:
            if self.balances[currency] >= amount:
                self.balances[currency] = self.balances[currency] - amount
            else:
                raise ValueError("Insufficient balance")
        else:
            raise ValueError("Currency not found")
        return self.balances[currency]
        # if self.get_balance_for(currency) >= amount:
        #     self.balances[currency] -= amount
        #     return self.balances[currency]
        #
        # raise InsufficientFundsException(
        #     f"Insufficient funds  {self.balances[currency]}"
        # )

    def deposit_money(self, currency: str, amount: int) -> int:
        # if currency not in self.balances:
        #     self.balances[currency] = 0
        # self.balances[currency] += amount
        self.balances[currency] = self.balances.get(currency, 0) + amount
        return self.balances[currency]

    def get_balance_for(self, currency: str) -> int:
        return self.balances.get(currency, 0)

    def export_to_csv(self, file_path: str) -> None:
        header: List[str] = ["currency", "balance"]
        data: List[Dict[str, Any]] = [
            {"currency": currency, "balance": balance}
            for currency, balance in self.balances.items()
        ]

        with open(file_path, "w", newline="") as csv_file:
            writer: csv.writer = csv.writer(csv_file)
            writer.writerow(header)
            for row in data:
                writer.writerow(row.values())

    def load_from_csv(self, file_path: str) -> None:
        with open(file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)  # Read the header row
            if header == ["currency", "balance"]:
                self.balances = {row[0]: int(row[1]) for row in reader}
            else:
                raise ValueError("Invalid CSV file format")

    def export_to_json(self, file_name: str) -> None:
        data = {"balances": self.balances}

        with open(file_name, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def load_from_json(self, file_name: str) -> None:
        with open(file_name, "r") as json_file:
            data = json.load(json_file)
            self.balances = data.get("balances", {})
