# Revised Code with exception handling
try:
    x = int(input("What is x? "))  # input: 20 | input: cat
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")  # This will only run if no exception occurred
