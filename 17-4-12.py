with open('goats.txt') as g, open('answer.txt', 'w') as ans:
    x = g.read().replace('GOATS', 'justnums.txt').replace('COLOURS', '').lstrip().split('justnums.txt')
    count_goats = dict(zip(x[0].strip().split('\n'), [0]*len(x[0].strip().split('\n'))))
    goats = x[1].strip().split('\n')
    for i in goats:
        count_goats[i] += 1
    for k,v in count_goats.items():
        if v > len(goats) * 0.07:
            print(k, end='\n', file=ans)