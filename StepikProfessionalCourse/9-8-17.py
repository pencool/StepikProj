import functools


def prefix(string: str, to_the_end: bool = False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                return func(*args, **kwargs) + string
            else:
                return string + func(*args, **kwargs)

        return wrapper

    return decorator


@prefix(' online-school', to_the_end=True)
def beegeek():
    '''beegeek docs'''
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)
print(beegeek())
