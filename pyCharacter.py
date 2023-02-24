character_super_powers = {'reading':81, 'running':55, 'dancing':60,'jumping':70,'invisibility':45, 'blink':80}
character_wallet = {'dollars':'{:,.2f}'.format(170),'pounds':'{:,.2f}'.format(50),'euros':'{:,.2f}'.format(38)}

def super_powers_at_or_above_given_number(dict,num):
    filtered_list_of_powers = []
    for key in dict:
        if dict[key] >= num:
            filtered_list_of_powers += {key}
    return filtered_list_of_powers


def spend_money(wallet, currency, amount):

    if (int(float(wallet.get(currency))) - amount) > 0:
            new_currency_value = float(wallet.get(currency)) - amount
            wallet[currency] = new_currency_value
            return 'you have spent '+ currency + f" {amount}"
    return 0

def main():
    print(super_powers_at_or_above_given_number(character_super_powers, 70))
    print(spend_money(character_wallet, 'dollars', 38))


if __name__ == "__main__":
   main()




