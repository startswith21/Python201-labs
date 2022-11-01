# Using f-strings, print out the name, last name,and quote of each person in the given dictionary,
# formatted like so:                           # by leaving it as a list?, name plus comm reordered?
# "The inspiring quote" - Lastname, Firstname   #new dict/list append? list comprehensions?
famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]
for element in famous_quotes:                        #list of dictionaries
    splitname = element["full_name"].split()  #turns string into  list of strings
    #print(splitname)
    #print(type(splitname))
    lastname = splitname[1]    
    #print(lastname)                  #now lastname is a string!!
    #print(type(lastname))
    firstname = splitname[0]
    #print(firstname)
    quote = element["quote"]          
    print(f'"{quote}" - {lastname}, {firstname}')
















