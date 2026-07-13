# Version 4: Further simplified function to check even or odd
def main():
    x = int(input("What's x? "))  # 4

    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()
