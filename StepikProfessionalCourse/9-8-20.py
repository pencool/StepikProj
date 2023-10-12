import functools


def strip_range(start: int, end: int, char: str = '.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            val = list(val)
            for i in range(start, end):
                if i < len(val):
                    val[i] = char
            return ''.join(val)

        return wrapper

    return decorator


@strip_range(20, 30)
def beegeek():
    return 'beegeek'


print(beegeek())
