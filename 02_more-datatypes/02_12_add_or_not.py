# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# input hasn't been added and deduce a point.
# If the user gets loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items. nested loops!?
num_set = set()
num_points = 5
num_itemsinset = 0

while num_points >= 0 and num_itemsinset < 3:
    user_guess = input("Enter a number: ")
    if user_guess.isnumeric() == False:
        print("Next time please enter a number.")
        break
    elif user_guess not in num_set:
        num_set.update(user_guess)
        num_itemsinset += 1
        print(num_itemsinset)
        print(num_set)  
        if num_itemsinset == 3:
            print("You won")
            break    
    else:
        num_points -= 1
        print("Already present!")
        if num_points == 0:
            print("You lost")
            break
