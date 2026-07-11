def add_logs(func):
    def wrapper():
        print("---- Function execution started ----")
        func()
        print("---- Function execution completed ----")

    return wrapper


def print_hello():
    print("Hello!")


@add_logs
def print_hi():
    print("Hi!")


# 1st way of invocation
hello = add_logs(print_hello)
hello()
print()

# 2nd way of invocation
add_logs(print_hello)()
print()

# 3rd way of invocation
print_hi()
