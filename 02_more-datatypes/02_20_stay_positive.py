# Use a list comprehension to create a list called `positive` from the list
# `numbers` that contains only the positive numbers from the provided list.

numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]
positive = []
for element in numbers:
    if element > 0:
        positive.append(element)
print(positive)
print(numbers)

numbers1 = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]
print([item for item in numbers1 if item > 0])

