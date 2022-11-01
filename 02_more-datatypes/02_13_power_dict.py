# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}   #tuple pairs list? adding to empty dict,  dict.items not work
#adding with .update?, calling dict method

list_num = list(range(1, 11))
print(list_num)
dict_num = dict.fromkeys(list_num, 1)
print(dict_num)
for key, value in dict_num.items():
    new_value = key * key
    print(key, new_value)
    tup_num = (key, new_value)
    print(tup_num)
    dict_num.update([tup_num])
print(dict_num)

   



   

#replace all val with another value d = {x: 1 for x in d}