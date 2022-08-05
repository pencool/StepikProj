def print_products(*args):
    c = {}
    counter = 0
    for i in range(len(args)):
        if type(args[i]) is str and len(args[i]) > 0:
            counter += 1
            c.setdefault(str(counter) + ')', args[i])
    return print(*[f'{k} {v}' for k, v in c.items()] if len(c) > 0 else ['Нет продуктов'], sep='\n')

print_products([1, 2], ('Stepik',), 5, True)