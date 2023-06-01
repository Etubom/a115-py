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

    def export_to_csv(self, data: List[Dict[str, Any]], file_path: str) -> None:
        header: List[str] = ["currency", "balance"]

        with open(file_path, "w", newline="") as csv_file:
            writer: csv.writer = csv.writer(csv_file)

            writer.writerow(header)
            for row in data:
                writer.writerow(row.items())

    def load_from_csv(self, file_path: str) -> None:
        with open(file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print("print from load from csv", row)

    def export_to_json(data: List[Dict[str, Any]], file_path: str) -> None:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def load_from_json(file_path: str) -> List[List[str]]:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data
