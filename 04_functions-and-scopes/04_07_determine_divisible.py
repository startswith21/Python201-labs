# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages
# both functions cannot take the same user input?? 
#userinput = int(input("Enter number:")) #must be integer! control
def inputnumber():
    number = int(input("Enter a number:"))
    return number

userinput = inputnumber()  #!def function for userinput, then it can be used as argument in both funct

def fourORseven(userinput):
    if userinput % 4 == 0 or userinput % 7 == 0:
        return True
    else:
        return False
outputOR = fourORseven(userinput)    # f string for description 
print(f"The number is divisible by 4 or 7: {outputOR}")

def fourANDseven(userinput):
    if userinput % 4 == 0 and userinput % 7 == 0:
        return True
    else:
        return False

outputAND = fourANDseven(userinput)    # f string for description 
print(f"The number is divisible by 4 and 7: {outputAND}")




