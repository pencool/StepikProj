random_numbers = lambda x, y: iter(range(x, y+1), '')

iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))