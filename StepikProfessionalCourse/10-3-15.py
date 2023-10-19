is_iterator = lambda x: '__next__' in dir(x)

print(is_iterator([1, 2, 3, 4, 5]))

