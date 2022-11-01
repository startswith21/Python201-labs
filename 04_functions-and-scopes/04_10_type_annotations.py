# Add type annotations to the three functions shown below.

def multiply(num1, num2) -> int:
    return num1 * num2

def greet(greeting, name) -> str:
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def shopping_list(*args) -> str:
    [print(f"* {item}") for item in args]
    return args
