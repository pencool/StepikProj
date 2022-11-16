def custom_isinstance(objects, typeinfo):
    return sum([1 if isinstance(i, typeinfo) else 0 for i in objects])

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, int))