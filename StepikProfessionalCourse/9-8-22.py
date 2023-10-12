import functools


def takes(*argsa):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in args:
                if type(i) not in argsa:
                    raise TypeError
            for i in kwargs.values():
                if type(i) not in argsa:
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper

    return decorator


@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times

try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))
