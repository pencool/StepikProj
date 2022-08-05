import re

with open('nums.txt') as f:
    q = []
    for i in f.read().split():
        q.append([*map(lambda x: int(x) if x.isdigit() else 0, re.findall('\d+', i))])
    print(sum(map(sum, q)))
