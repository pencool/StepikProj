from random import choice as ch

with open('first_names.txt') as n, open('last_names.txt') as f:
    n, f = n.readlines(), f.readlines()
    print(*[f'{ch(n).strip()} {ch(f).strip()}' for i in range(3)], sep='\n')
