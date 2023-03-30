from typing import List, Dict

def super_powers_at_or_above_given_number(my_dict: Dict, num: int) -> List[str]:
    filtered_list_of_powers = []
    for key in my_dict:
        if my_dict[key] >= num:
            filtered_list_of_powers.append(key)
    return filtered_list_of_powers


def spend_money(wallet:Dict, currency:str, amount:float) -> str:
    remaining_amount = wallet.get(currency)
    if remaining_amount is not None:
        remaining_amount = int(remaining_amount) - amount
        if remaining_amount >= 0:
            wallet[currency] = remaining_amount
        return f"you have spent  {currency} {amount}"
    return str(0)






