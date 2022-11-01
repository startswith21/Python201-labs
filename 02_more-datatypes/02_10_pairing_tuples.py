# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#If the list has an odd number of items,add the last item to a tuple together with the number `0`.
# Note: This lab might be challenging! 
from resources import randlist
print(randlist)
randlist.sort()
if len(randlist) % 2 != 0:
    randlist.append(0)
tuppairlist = list(zip(randlist[0::2], randlist[1::2]))
print(tuppairlist)

    
