def number_of_frogs(f):
    if f == 1:
        return 77
    else:
        return 3*(number_of_frogs(f-1) - 30)

print(number_of_frogs(10))