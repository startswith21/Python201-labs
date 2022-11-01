# Using f-strings, print out the name, last name, and favorite
# office supply item of each person in the given dictionary,formatted like so:
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item
office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

for element in office:                        #list of dictionaries
    splitname = element["full_name"].split()  #turns string into  list of strings!!
    #print(splitname)
    #print(type(splitname))
    lastname = splitname[1].upper()    #last name should be all  caps
    #print(lastname)                  #now lastname is a string!!
    #print(type(lastname))
    firstname = splitname[0]
    #print(firstname)
    OSitem = element["item"]          #OSitem contains a string 
    #print(OSitem)
    #print(type(OSitem))
    print(f'{lastname}, {firstname:<20} \t{OSitem:<15}')




