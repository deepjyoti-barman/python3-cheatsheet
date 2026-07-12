# Calculate and return the square of a user input number using functions
def main():
    x = int(input("What's the value of x? "))
    print(f"{x} square is: {square(x)}")


def square(n):
    # return n ** 2
    # return pow(n, 2)
    return n * n


main()
