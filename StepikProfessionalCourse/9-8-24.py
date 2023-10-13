import functools


def ignore_exception(*argsd: Exception):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                val = func(*args, **kwargs)
            except Exception as e:
                if type(e) not in argsd:
                    raise e
                else:
                    return print(f'Исключение {type(e).__name__} обработано')
            return val
        return wrapper

    return decorator


@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def beegeek():
    return 'beegeek'


print(beegeek())
