# Refactored version using functions to prompt user and print "meow" n times
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))  # 3

        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
