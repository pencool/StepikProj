# def cubes_of_odds(lst):
#     return (i**3 for i in lst if i % 2 == 1)

cubes_of_odds = lambda x: (i ** 3 for i in x if i % 2 == 1)

print(*cubes_of_odds([1, 2, 3, 4, 5]))
