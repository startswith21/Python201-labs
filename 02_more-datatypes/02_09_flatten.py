# Write a script that "flattens" a shallow list. For example:
## starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
## Note that your input list only contains one level of nested lists.
# This is called a "shallow list".#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?
startlist1 = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
list1flat = [element for sublist in startlist1 for element in sublist] #list comprehension 
print(list1flat)
list2flat = []      #for loop
for sublist in startlist1:
    for element in sublist:
        list2flat.append(element)
print(list2flat)

import itertools      #flatten using itertool and unpacking 
list3flati = itertools.chain(*startlist1) #converts list into function arguments, can be parsed by chain()method
list3flat = list(list3flati)           #convert chain object back into list
print(list3flat)

