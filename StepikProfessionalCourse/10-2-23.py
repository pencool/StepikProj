def starmap(func, iterable):
    return map(lambda x: func(*x), iterable)

pairs = [(1, 3), (2, 5), (6, 4)]

print(*starmap(lambda a, b: a + b, pairs))