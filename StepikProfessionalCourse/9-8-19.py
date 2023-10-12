import functools


def repeat(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                val = func(*args, **kwargs)
            return val
        return wrapper
    return decorator


@repeat(10)
def add(a, b):
    '''sum of two numbers'''
    return a + b


print(add.__name__)
print(add.__doc__)
print(add(10, b=20))