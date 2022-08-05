with open('prices.txt') as f:
    print(sum(map(lambda x: int(x[1].strip()) * int(x[2].strip()), map(str.split, f.readlines()))))
