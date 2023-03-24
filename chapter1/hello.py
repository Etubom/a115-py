from functools import reduce
from collections import Counter


# print("Hello to the terminal")
# a = 6
# if a > 5:
#      a += 1
# a = a *2
#
# # if a > 5:
# #     a += 1
# # else:
# #     a = a * 2
#
# print(a)
# def reverse(text):
#      return text[::-1]
# print(type(reverse('123')))
# print(type(reverse))
#
# user_input = input('Enter your text to be reversed here: ')
# print(reverse(user_input))
# def count_words_with(words,letter):
#      occurence = 0
#      for word in words:
#          if not word.startswith(letter):
#              pass
#          else:
#              occurence += 1
#      return occurence
# print(count_words_with(['sly','buy','cry','soy','eye'],'s'))

# first_var = 'Outside the fucntion'
# print('First var here is :',first_var)
# def fn_scope_sample():
#     first_var = 'changed from inside function'
#     return first_var
#
# print(fn_scope_sample())
# print(first_var)

# print(locals())
# for n in range(99, 0, -1):
#     print(n, "bottles of rum on the wall")
# numbers = [1,2,3]
# def sum_of_squares(numbers):
#     return sum([x**2 for x in numbers])
# print(sum_of_squares(numbers))

#
# Write a programme, which ranks the months during which people most often spend money.
# (Hint: use a nested `for` loop to add 1 for each occurrence of a month to a dictionary, whose keys are the months and values are their corresponding frequencies.
# Then, use the `sorted` function with a custom key to sort by frequency.)
# BONUS: Write another version of your programme, which uses the
# `collections.Counter` class from Python's standard library. Hint: Use `reduce` with an initial value of an empty list, and a list comprehension, to create a single list with all occurrences of the months during which any customer has made a purchase. Then create a `Counter` object by passing in this list. Finally, use the `most_common` method on that object to find the ranking of months by frequency. Compare the code for this solution to your original solution.


data = [
    {
        "name": "John",
        "gender": "male",
        "spending": 900,
        "months": ["January", "November", "December"],
    },
    {
        "name": "Alice",
        "gender": "female",
        "spending": 1200,
        "months": ["January", "November", "December"],
    },
    {
        "name": "Bob",
        "gender": "male",
        "spending": 500,
        "months": ["January", "November", "December"],
    },
    {
        "name": "Eve",
        "gender": "female",
        "spending": 1800,
        "months": ["January", "November", "December"],
    },
    {
        "name": "X",
        "gender": "male",
        "spending": 9000,
        "months": ["January", "November", "December"],
    },
]

# Solution one
month_count = {}

for customer in data:
    for month in customer["months"]:
        if month in month_count:
            month_count[month] += 1
        else:
            month_count[month] = 1

sorted_months = sorted(month_count.items(), key=lambda x: x[1], reverse=True)

for month, count in sorted_months:
    print(month, count)
# Explanation:
#
# We initialize an empty dictionary month_count to keep track of the count for each month.
# We use a nested for loop to iterate over each customer and each month in their list of months.
# If the month already exists in the month_count dictionary, we add 1 to its count. Otherwise, we create a new key with a count of 1.
# We sort the month_count dictionary by the count of each month using the sorted() function with a custom key parameter. This sorts the dictionary by the values instead of the keys, in descending order.
# Finally, we iterate over the sorted dictionary and print out the month and its count.


# Solution 2
all_months = reduce(lambda x, y: x + y["months"], data, [])
month_count = Counter(all_months)

for month, count in month_count.most_common():
    print(month, count)
#
# Explanation:
#
# We import the Counter class from the collections module, and the reduce function from the functools module.
# We use reduce() to create a list of all the months across all customers. The lambda function takes two arguments, x and y, and concatenates x with the list of months for the current customer y. The initial value of x is an empty list.
# We create a Counter object by passing in the list of all months to the Counter() constructor.
# We use the most_common() method on the Counter object to get a list of tuples representing the months and their corresponding counts, sorted in descending order by count.
# Finally, we iterate over the list of tuples and print out the month and its count.
