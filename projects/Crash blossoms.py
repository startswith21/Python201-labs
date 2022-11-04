#write function that a user input as string and convert it into all words capitalized

userinput = str(input("Enter your text: "))

def titlecap(userinput):
    titlecap = []
    for word in userinput.split():      #splits string into list of strings
        cappedtitle = word.capitalize()
        titlecap.append(cappedtitle)
    return " ".join(titlecap)

print(titlecap(userinput))

blossom = titlecap(userinput)
print(blossom)




