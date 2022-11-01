# Write code that creates a list of all unique values in a list.
# For example:
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

list_all = [32, -5, 12, "hi", 32, 0, 6, 9, 6.0]

list_uniq = []
for x in list_all:
    y = list_all.count(x)
    print(y)
    if y < 2:
        list_uniq.append(x)
print(list_uniq)               



