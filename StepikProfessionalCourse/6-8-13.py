from collections import Counter
berrys = Counter(input().lower().split())
min_berry = min(berrys.values())
print(*[k for k, v in sorted(berrys.items()) if v == min_berry], sep=', ')