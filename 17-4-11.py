with open('class_scores.txt') as f, open('new_scores.txt', 'w') as sc:
    print(*[f'{i.split()[0]} {min(100,(int(i.split()[1])+5))}' for i in f.read().split('\n')], sep='\n', file=sc)