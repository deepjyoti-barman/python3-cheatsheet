# Modularized version of code with functions
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What is x? "))  # input: cat | input: dog | input: 20
        except ValueError:
            print("x is not an integer")


main()
