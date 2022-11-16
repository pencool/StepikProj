def is_greater(lists: list, number: int):
    return any(map(lambda x: sum(x) > number, lists))

data = [[0, 1, 2], [0, 3], [1, 1, 1], [3]]

print(is_greater(data, 3))