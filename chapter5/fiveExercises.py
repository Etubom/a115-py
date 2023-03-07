# Write a function which takes a list of numbers and returns the
# sum of their squares. Does your function still work if the input list is empty? Why (or why not?)
numbers = [1,2,3]
def sum_of_squares(numbers):
    return sum([x * x for x in numbers])
print(sum_of_squares(numbers))
# ' The function still works if the list is empty because it's sum will be zero'

# Write a function called `apply()` which takes two arguments:
#     a. A list of `items`;
#     b. Another function `f`, which takes a single value and returns a single value;
#     Your function should return a list in which each value is the result of applying
#     the function `f` on the corresponding value in `items`.
def apply(items, f):
    return [f(x) for x in items]

def plus_one(x):
    return x + 1

my_list = [1, 2, 3, 4, 5]
result = apply(my_list, plus_one)
print(result)