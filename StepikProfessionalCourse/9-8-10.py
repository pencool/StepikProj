import functools
def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        if type(val) is not str:
            raise TypeError
        return val
    return wrapper


@returns_string
def add(a, b):
    return a + b

try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))