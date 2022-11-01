# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list1 = [1, 2, 5, 3, 4, 3, 4, 5]        #1. set conversion
listtoset = set(list1)
print(listtoset)
print(type(listtoset))
settolist = list(listtoset)
print(settolist)
print(type(settolist))

list2 = [1, 2, 5, 3, 4, 3, 4, 5]         #2. loop & second list
listnodup = []
for element in list2:
    if element not in listnodup:
        listnodup.append(element)
print(listnodup)
