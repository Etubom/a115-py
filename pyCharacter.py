from datetime import date


character_name="Sammy"
print("Name is",character_name)
character_age=25
print("Age is",character_age)
character_dob=date(1960, 11, 11).strftime('%d/%b/%Y')
print("Character dob is",character_dob)
character_net_worth = '{0:.2f}'.format(50000)
print("Their net worth is ", '$'+ character_net_worth)
character_super_powers=['reading', 'running', 'dancing']
print("Current set of super powers",character_super_powers)
user_super_power_input=list(input("What is your favourite super power? : ").split())
updated_super_powers = set(character_super_powers + user_super_power_input)
print(updated_super_powers)

