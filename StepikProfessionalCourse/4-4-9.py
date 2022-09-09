import json

with open('countries.json', encoding='utf-8') as f, open(
    'religion.json', 'w', encoding='utf-8') as n:
    data_country = {}
    for i in json.load(f):
        data_country.setdefault(i['religion'], []).append(i['country'])
    json.dump(data_country, n, indent=3)