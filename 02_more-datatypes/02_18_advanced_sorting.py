# CHALLENGE: Write a script that sorts a dictionary into a    #dict cannot be sorted, are unordered
# list of tuples based on the dictionary's values. For example:
# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]
# https://docs.python.org/3/howto/sorting.html#key-functions

input_dict = {"item4": 5, "item2": 6, "item3": 1}
print(input_dict["item2"])     #prints value of key item2
for key, value in input_dict.items():  #converts dict into list of tuple objects
    print(key, value)
    tupldict = input_dict.items()
    print(tupldict)          
for key in input_dict:
    print(key)
for value in input_dict.values():
    print(value)
for key, value in input_dict.items():
    items10 = value + 10
    print(items10)

dicttuple = input_dict.items()      #list of tuples
print(dicttuple)
dicttuplesorted = sorted(dicttuple) 
print(dicttuplesorted)              #list of tuples sorted by key

dictsorted = sorted(input_dict.items())  #2 steps above in one step, returns tuple list
print(dictsorted)

dictsorted = sorted(input_dict.items(), key = lambda x:x[1], reverse = False)
print(dictsorted)




