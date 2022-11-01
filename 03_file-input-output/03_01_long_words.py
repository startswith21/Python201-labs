# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).
import pathlib 

#readlines(): reads all lines, returns list containing the lines

with open ("words.txt", "r") as txtfile1:
    for line in txtfile1:
        if (len(line)) >= 20:        # for loop and if statement to print lines with at least 20 char 
            print(line.rstrip())     #removes whitespace char/new line char
            # print(type(line))      #each line is a string 


with open ("words.txt", "r") as txtfile:  # generate object of the file to analyze in py
    file1 = txtfile.readline(1)           # reads only first line (of given len),line is a list item (string)
    print(file1)

with open ("words.txt", "r") as txtfile3:
    file2 = txtfile3.readline()
    while file2:                          #prints all lines using while loop
        #print(file2.rstrip())
        file2 = txtfile3.readline()

#parameter for readlines to get lines with certain length (py readline method guru99)



