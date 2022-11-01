# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

str_text = "codingnomads"
print(str_text)
print(str_text[2:4])     
tup_text = tuple(str_text)
print(type(tup_text))
print(tup_text)
print(tup_text[2:4])
