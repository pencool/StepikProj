def takes_positive(func):
    def wrapper(*args, **kwargs):
        for i in args:
            if type(i) is not int:
                raise TypeError
            elif i <= 0:
                raise ValueError
        for k, v in kwargs.items():
            if type(v) is not int:
                raise TypeError
            elif v <= 0:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
except Exception as err:
    print(type(err))
