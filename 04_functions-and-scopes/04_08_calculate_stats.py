# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console when you call the function.
import statistics
example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(listnumbers):
    maximum = max(listnumbers)
    minimum = min(listnumbers)
    average = statistics.mean(listnumbers)
    total   = sum(listnumbers)
    return maximum, minimum, average, total
  
print(stats(example_list))

