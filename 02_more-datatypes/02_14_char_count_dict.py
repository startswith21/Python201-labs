# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}
user_word = str(input("Enter a word: "))
print(type(user_word))
dictlettfreq = {}
for char in user_word:
    dictkey = dictlettfreq.keys()
    if char in dictkey:
        dictlettfreq[char] += 1
    else:
        dictlettfreq[char] = 1
print(dictlettfreq)





