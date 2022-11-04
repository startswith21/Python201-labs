#Write a script that takes a sentence from the user and returns:
#the number of lower case letters
#the number of uppercase letters
#the number of punctuations characters
#the total number of characters
#Use a dictionary to store the count of each of the above.
#Note: ignore all spaces.
#Example input:
#I love to work with dictionaries!
#Example output: Upper case: 1 Lower case: 26 Punctuation: 1 Total chars: 28

UserSentence = str(input("Enter your sentence: "))
UserSentence.split()
#print(UserSentence)
totalChar = len(UserSentence)
print(totalChar)
UpperCase = 0
LowerCase = 0
Punctuation = 0
SentenceDict = {}
for item in range(len(UserSentence)):
    if UserSentence[item] >= 'a' and UserSentence[item] <= 'z':
        LowerCase += 1
    elif (UserSentence[item] >= 'A' and UserSentence[item] <= 'Z'):
        UpperCase += 1
print(UpperCase)
print(LowerCase)

import string
#print(string.punctuation)

for item in UserSentence:
    if item in string.punctuation:
        Punctuation += 1
print(Punctuation)

for variable in ["totalChar", "UpperCase", "LowerCase", "Punctuation"]: #alternative dict.update function!!
    SentenceDict[variable] = eval(variable)
print(SentenceDict)


