# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.

generator = (x+3 for x in range(10))
print(generator)
for item in generator:
    print(item)

word = "hello world"
generator1 = ("hello" for char in word)
for char in generator1:
    print(char)
