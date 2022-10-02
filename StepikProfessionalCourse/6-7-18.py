from collections import Counter
fruits = Counter(input().split(','))
for k, v in sorted(fruits.items()):
    one = sum(map(ord, k.replace(' ', '')))
    print(f'{k.ljust(max(map(len, fruits)))}: {one} UC x {v} = {one * v} UC')
