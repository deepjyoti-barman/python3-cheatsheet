# Demonstration of 'NameError' runtime exception
try:
    # When the user enters an integer value, the value is successfully converted to an integer and then assigned to x
    # Later the value of x can be printed in console as well

    # But when the user enters a non-integer value, a runtime exception ValueError would occur on the RHS of the expression
    # and assignment of the value to x is skipped, hence printing the value of x would raise NameError runtime exception
    x = int(input("What is x? "))  # input: 20 | # input: cat
except ValueError:
    print("x is not an integer")

print(f"x is {x}")  # NameError: name 'x' is not defined
