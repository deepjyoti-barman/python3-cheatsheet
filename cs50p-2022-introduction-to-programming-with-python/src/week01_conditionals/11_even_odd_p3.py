# Version 3: Simplified function to check even or odd
def main():
    x = int(input("What's x? "))  # 3

    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return True if n % 2 == 0 else False


main()
