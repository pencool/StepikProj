import functools


def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        return val*val
    return wrapper

@square
def add(a, b):
    return a + b

print(add(3, 7))