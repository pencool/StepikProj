with open('numbers.txt') as f:
    for i in f.read().split('\n'):
        print(sum(map(int, i.split())))


