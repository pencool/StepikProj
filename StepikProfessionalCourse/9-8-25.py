import functools


class MaxRetriesException(Exception):
    pass


def retry(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times+1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass
            raise MaxRetriesException
        return wrapper
    return decorator


@retry(10)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 10:
        raise ValueError
    return a + b


try:
    print(add(10, 30))
except Exception as e:
    print(type(e))