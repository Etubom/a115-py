from functools import reduce

data = [
    {'name': 'John', 'gender': 'male', 'spending':
        900,'months': ['January', 'November', 'December']},
    {'name': 'Alice', 'gender': 'female',
     'spending': 1200,'months': ['January', 'November', 'December']},
    {'name': 'Bob', 'gender': 'male', 'spending':
        500,'months': ['January', 'November', 'December']},
    {'name': 'Eve', 'gender': 'female',
     'spending': 1800,'months': ['January', 'November', 'December']},
    {'name': 'X', 'gender': 'male',
     'spending': 9000,'months': ['January', 'November', 'December']},
]

# Challenge 1
total_spending = sum(client_details.get('spending', 0) for client_details in data if client_details['name'] != 'X')

print(total_spending)

# Challenge 2
gender_totals = {'male': {'sum': 0, 'count': 0}, 'female': {'sum': 0, 'count': 0}}

for client_details in data:
    if client_details['name'] != 'X':  # exclude customers with name 'X'
        gender = client_details['gender']
        spending = client_details['spending']
        gender_totals[gender]['sum'] += spending
        gender_totals[gender]['count'] += 1

gender_averages = {gender: gender_totals[gender]['sum'] / gender_totals[gender]['count'] for gender in gender_totals}

print(gender_averages)

# Challenge 3
list_of_numbers = [1,2,3,4,5,6,7,8,9]
positive_numbers = [number for number in list_of_numbers if number % 2 == 0]
print(positive_numbers)

squared_positive_numbers = [(number ** 2) for number in list_of_numbers if number % 2 == 0]
print(squared_positive_numbers)

# Challenge 4
product_of_all_numbers = reduce(lambda total,item: total * item,list_of_numbers)
print(product_of_all_numbers)

product_of_even_numbers = reduce(lambda total, item: total * item, [number for number in list_of_numbers if number % 2 == 0], 1)

print(product_of_even_numbers)

