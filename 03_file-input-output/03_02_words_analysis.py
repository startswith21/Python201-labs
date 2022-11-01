# Read in all the words from the `words.txt` file.
# Then find and print:
# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

wordlist = []
with open ("words.txt", "r") as wordfile:
    for line in wordfile.readlines():
        line = line.rstrip()
        wordlist.append(line)
#print(wordlist)

longestwords = max([len(word) for word in wordlist])  # returns number of char but not string itself
print(longestwords)

sortedwords = sorted(wordlist, key = len)
print(sortedwords)
print(len(sortedwords))     # total number of words
print(sortedwords[0])       # one of or the shortest word
print(len(sortedwords[-1])) # one of or the longest word; but how to print al shortest words if there is a tie?