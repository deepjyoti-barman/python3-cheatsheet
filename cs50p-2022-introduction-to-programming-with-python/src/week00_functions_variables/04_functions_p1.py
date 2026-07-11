# Functions are useful to avoid repeating the same code again and again, no need to reinvent the wheel
def hello(to="world"):
    print("hello,", to)


hello()
name = input("What's your name? ")
hello(name)
