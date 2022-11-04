# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.
# -> write function, that iterates over items and assigns an index to each item resulting returning a tuple
cars = ['kia', 'audi', 'bmw']
listOfCars = []

def indlist(list2):
    for car in cars:
        n = 0
        listOfCars.append((n, car))
        n += 1
    print(listOfCars)
indlist(cars)

languages = ['Python', 'Java', 'JavaScript']
enumerate_prime = enumerate(languages)
# convert enumerate object to list
print(list(enumerate_prime))
# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]


destinations = ["east coast", "sea", "west coast", "surf"]
def indexedlist(list1):
    for n in range(len(list1)):
        print(n, list1[n])
indexedlist(destinations)


