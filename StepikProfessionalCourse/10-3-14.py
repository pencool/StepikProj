is_iterable = lambda x: '__iter__' in dir(x)

objects = [(1, 13), 7.0004, [1, 2, 3]]

for obj in objects:
    print(is_iterable(obj))
