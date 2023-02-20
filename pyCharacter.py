from datetime import date


# character_name="Sammy"
# print("Name is",character_name)
# character_age=25
# print("Age is",character_age)
# character_dob=date(1960, 11, 11).strftime('%d/%b/%Y')
# print("Character dob is",character_dob)
# character_net_worth = '{0:.2f}'.format(50000)
# print("Their net worth is ", '$'+ character_net_worth)
character_super_powers = {'reading':81, 'running':55, 'dancing':60,'jumping':70,'invisibility':45, 'blink':80}
print("Current set of super powers",character_super_powers)
user_super_power_input= input("What is your favourite super power? : ").lower()
user_input_value = character_super_powers[user_super_power_input]
print(user_input_value)
if user_input_value == 80:
    print("TRY AGAIN")
if user_input_value < 80 and user_input_value > 50:
    print("COOL")
if user_input_value > 80:
    print("SUPER COOL")


character_wallet = {'dollars':'{:,.2f}'.format(170),'pounds':'{:,.2f}'.format(50),'euros':'{:,.2f}'.format(38)}
print(character_wallet.get('euros'))

def super_powers_at_or_above_given_number(dict,num):
    filtered_list_of_powers = []
    for key in dict:
        if dict[key] >= num:
            filtered_list_of_powers += {key}
    return filtered_list_of_powers

print(super_powers_at_or_above_given_number(character_super_powers,70))

def spend_money(wallet, currency, amount):
    for key in wallet:
        if (float(wallet[currency]) - amount) > 0:
         return 'you have spent '+ currency +f" {amount}"

    return  0
print(spend_money(character_wallet,'euros',38))


