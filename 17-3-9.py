with open('lines.txt') as f:
    z = max(f.read().split('\n'), key=len)
    f.seek(0)
    print(*filter(lambda x: len(x) == len(z), f.read().split('\n')), sep='\n')


