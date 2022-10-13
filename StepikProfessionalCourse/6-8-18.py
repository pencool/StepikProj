import csv
from collections import Counter

with open('name_log.csv') as f:
    print(*[f'{k}: {v}' for k, v in sorted(
        Counter([i['email'] for i in csv.DictReader(f)]).items())], sep='\n')