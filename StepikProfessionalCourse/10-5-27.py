def flatten(nested_list):
    for i in nested_list:
        if isinstance(i, int):
            yield i
        else:
            yield flatten(i)


generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)
