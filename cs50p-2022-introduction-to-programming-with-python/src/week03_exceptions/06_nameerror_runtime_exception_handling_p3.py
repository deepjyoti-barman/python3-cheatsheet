# Shorter version of retry-except loop
while True:
    try:
        x = int(input("What is x? "))  # input: cat | input: dog | input: 20
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")  # Safe to use x here
