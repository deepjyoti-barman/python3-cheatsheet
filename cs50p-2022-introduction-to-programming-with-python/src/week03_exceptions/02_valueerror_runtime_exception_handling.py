# Revised Code with exception handling
try:
    x = int(input("What is x? "))  # input: cat
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
