def takes_positive(func):
    def wrapper(*args, **kwargs):
        for i in args:
            if type(i) is not int:
                raise TypeError
            elif i <= 0:
                raise ValueError

    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
