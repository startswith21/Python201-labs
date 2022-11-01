# Write a script that takes a string from the user   USE LIST APPEND? or tuple + tuple ?
# and creates a list that contains a tuple for each word.
# For example:input = "hello world"result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

user_string = input("Enter words: ").split()
print(list(map(tuple, user_string)))

