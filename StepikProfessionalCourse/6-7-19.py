from collections import Counter

with open('pythonzen.txt') as f:
    chars = Counter([i for i in f.read().lower() if i.isalpha() ])
    for k, v in sorted(chars.items()):
        print(f'{k}: {v}')