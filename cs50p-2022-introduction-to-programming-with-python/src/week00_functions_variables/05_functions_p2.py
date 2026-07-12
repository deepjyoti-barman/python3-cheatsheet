# Even though the following piece of code might work in jupyter notebooks or interactive Python shells
# But, it will raise an error because the function is called before its definition

hello()  # NameError: name 'hello' is not defined. Did you mean: 'help'?
name = input("What's your name? ")
hello(name)  # NameError: name 'hello' is not defined. Did you mean: 'help'?


def hello(to="world"):
    print("hello,", to)
