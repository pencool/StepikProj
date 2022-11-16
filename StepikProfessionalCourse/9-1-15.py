def zip_longest(*args, fill=None):
    max_len = len(max(args, key=len))
    for i in args:
        if len(i) < max_len:
            i.extend([fill] * (max_len - len(i)))
    return [*zip(*args)]


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))