character_super_powers = {'reading':81, 'running':55, 'dancing':60,'jumping':70,'invisibility':45, 'blink':80}
character_wallet = {'dollars':170.0,'pounds':50.0,'euros':38.0}

def super_powers_at_or_above_given_number(dict,num):
    filtered_list_of_powers = []
    for key in dict:
        if dict[key] >= num:
            filtered_list_of_powers.append(key)
    return filtered_list_of_powers


def spend_money(wallet, currency, amount):
    remaining_amount = int(wallet.get(currency)) - amount
    if (remaining_amount > 0) :
            wallet[currency] =  remaining_amount
            return f"you have spent  {currency} {amount}"
    return 0

def main():
    print(super_powers_at_or_above_given_number(character_super_powers, 70))
    print(spend_money(character_wallet, 'dollars', 38))


if __name__ == "__main__":
   main()




