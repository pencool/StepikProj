from random import randint as r
with open('random.txt', 'w') as f:
    print(*[f'{r(111, 778)}\n' for i in range(25)], file=f)