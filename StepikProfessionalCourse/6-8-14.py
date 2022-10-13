from collections import Counter

print(
    Counter(sorted(input().lower().split(), reverse=True)).most_common()[0][0])
