def non_negative_even(numbers: list):
    return all([*map(lambda x: (x % 2) == 0 and x >= 0, numbers)])


print(non_negative_even([0, 0, 0, 0, 0]))
