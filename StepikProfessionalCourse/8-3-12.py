def recursive_sum(a, b):
    if a != 0:
        return recursive_sum(a - 1, b + 1)
    return b

print(recursive_sum(11, 0))