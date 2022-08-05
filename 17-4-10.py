with open('input.txt') as inp, open('output.txt', 'w') as out:
    print(*[f'{i[0]}) {i[1]}' for i in enumerate(inp.read().split(), 1)], sep='\n', file=out)