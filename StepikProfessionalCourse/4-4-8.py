import json

with open('data1.json', encoding='utf-8') as f, open(
        'data2.json', encoding='utf-8') as n, open(
    'data_merge.json', 'w', encoding='utf-8') as out:
    data1, data2 = json.load(f), json.load(n)
    json.dump(data1 | data2, out, indent=3)
