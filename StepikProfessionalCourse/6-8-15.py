from collections import Counter

for k, v in sorted(Counter([len(i) for i in input().split()]).most_common(),
                   key=lambda x: (x[1])):
    print(f'Слов длины {k}: {v}')