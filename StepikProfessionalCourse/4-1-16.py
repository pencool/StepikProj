import sys

news = [i.strip('\n').split(' / ') for i in sys.stdin]
therm_news = [(i[0], i[2]) for i in news[:-1] if [i[1]] == news[-1]]
print(*[i[0] for i in sorted(sorted(therm_news), key=lambda x: float(x[-1]))], sep='\n')