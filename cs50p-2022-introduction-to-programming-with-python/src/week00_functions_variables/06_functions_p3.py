# Solving the problem that arises due to calling function before defining it
# and also demonstrating how to access a variable of global scope
count = 1


def main():
    hello()
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    global count
    print(f"PS-{count}: hello, {to}")
    count += 1


# Always call main() function at the end of the program
main()
