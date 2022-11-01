# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """Calculates the conversion from km into miles.

    Args: takes one integer or float value as input for km 
    Returns: a value of float type indicating the miles after conversion
    
    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
print(km_to_miles(3.77))
