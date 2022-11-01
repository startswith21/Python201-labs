# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

from collections import Counter
user_strings = input("Enter words: ").split()
print(user_strings)
print(type(user_strings))
user_wordlist = user_strings
print(user_wordlist)
user_wordlist.sort()
print(user_wordlist)

user_wordlist = Counter(user_wordlist)
mostfrequent_word = user_wordlist.most_common()
print(mostfrequent_word)





