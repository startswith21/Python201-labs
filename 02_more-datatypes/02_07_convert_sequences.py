# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.
string = "codingnomads"
tuple1 = tuple(string)             #converts each char into tuple separated by commas
print(tuple1)
print(type(tuple1))
tuple1tolist = list(tuple1)
print(tuple1tolist)
print(type(tuple1tolist))
klist = [sub.replace("c", "k") for sub in tuple1tolist] #replace first item in list with k;list comprehension
print(klist)
tupleklist = tuple(klist)
print(tupleklist)
print(type(tupleklist))
