from functools import wraps


# Decorator without @wraps
def add_logs(func):
    def wrapper():
        """Wrapper __doc__"""
        print(f"Function {func.__name__} is called.")
        return func()

    return wrapper


@add_logs
def print_hello():
    """print_hello __doc__"""
    return "Hello!"


print(print_hello.__name__)
print(print_hello.__doc__)
print(print_hello())
print()


# Decorator with @wraps
def debug(func):
    @wraps(func)
    def wrapper():
        """Wrapper __doc__"""
        print(f"Function {func.__name__} is called.")
        return func()

    return wrapper


@debug
def print_hi():
    """print_hi __doc__"""
    return "Hi!"


print(print_hi.__name__)
print(print_hi.__doc__)
print(print_hi())
