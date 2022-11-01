# Write a function that prints out nicely formatted information about a
# real estate listing. The information can vary for every listing, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def realestate(**House1):
    estate = f'--- Special house offer --- \n{House1}'
    print(estate)

realestate(price = "150 Euro", size = "900 qm", location = "central", extra = "balcony")

