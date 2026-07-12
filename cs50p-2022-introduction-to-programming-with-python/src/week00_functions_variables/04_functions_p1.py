# Defining and calling a function with a default parameter for personalized greeting
def hello(to="world"):
    print("hello,", to)


hello()
name = input("What's your name? ")
hello(name)
