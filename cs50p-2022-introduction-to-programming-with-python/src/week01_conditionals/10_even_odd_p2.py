# Version 2: Using a function to check even or odd
def main():
    x = int(input("What's x? "))  # 2

    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
