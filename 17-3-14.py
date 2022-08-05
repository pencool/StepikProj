with open('population.txt') as p:
    lst = [i.split('\t') for i in p]
    print(*map(lambda x: f'{x[0]}', filter(lambda x: x[0][0] == 'G' and int(x[1].strip()) > 500000, lst)), sep='\n')
