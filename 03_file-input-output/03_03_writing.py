# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.
wordlist = []

with open ("words.txt", "r") as wordsfile:
   for line in wordsfile.readlines():
       wordlist.append(line)
       
wordlist.reverse()        # does not create new list, changes original list!
#print(wordlist)           # other option: use slicing [::-1] to reverse a list

with open("words_reverse.txt", "w") as reversewordsfile:
    reversewordsfile.write(str(wordlist))         #must be str format

  