def n_print(func):
    def wrapper(*args, sep=' ', end='\n'):
        return func(*[str.upper(i) if type(i) is str else i for i in args],
                    sep=sep.upper(), end=end.upper())

    return wrapper


print = n_print(print)

print('hi', 'there', end='!')
