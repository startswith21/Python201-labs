# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread, *topping):   #*turns args into list or tuple
    components = f'My favorite sandwich:\n {bread}\n {topping}\n {bread}\n'   
    return components
    
print(make_sandwich("wheat", "cheese", "sugar", "salt"))      #how to print with new line character?
