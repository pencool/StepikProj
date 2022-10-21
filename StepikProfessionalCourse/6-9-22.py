import json
from collections import ChainMap

with open('zoo.json', encoding='utf-8') as f:
    print(sum(ChainMap(*json.load(f)).values()))