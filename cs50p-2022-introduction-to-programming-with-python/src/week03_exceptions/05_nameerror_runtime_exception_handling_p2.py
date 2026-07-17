# Revised code with retry-except inside a loop for robustness
# Since we want to keep the user prompting for the valid input again and again
while True:
    try:
        x = int(input("What is x? "))  # input: cat | input: dog | input: 20
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")  # Safe to use x here
