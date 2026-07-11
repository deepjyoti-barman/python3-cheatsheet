import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__}() took '{end - start:.4f}' seconds to execute.")
        return result
    return wrapper


@timer
def add(a, b):
    """Add two numbers together"""
    time.sleep(2)
    return a + b


print(add.__name__)
print(add.__doc__)
print(add(1, 2))