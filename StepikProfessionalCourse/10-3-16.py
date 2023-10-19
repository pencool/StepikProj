from random import choice


def random_numbers(left, right):
    itr = lambda: choice(list(range(left,right + 1)))
    return iter(itr, right + 2)


iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
