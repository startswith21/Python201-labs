# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}         # counter method alternative to loop
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
dict_3 = {}
dict_3 = dict_1 | dict_2
print(dict_3)
for key in dict_1.keys():
    if key in dict_2:
        add_values = dict_1[key] + dict_2[key]
        print(add_values)
        dict_3[key] = add_values
print(dict_3)





