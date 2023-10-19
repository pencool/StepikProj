def get_min_max(iterable):
    min = None
    max = None
    for i in iterable:
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i
    if min is None and max is None:
        return None
    return (min, max)

iterable = iter([])

print(get_min_max(iterable))
