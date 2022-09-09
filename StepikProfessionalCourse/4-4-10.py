import csv
import json

with open('playgrounds.csv', encoding='utf-8') as f, open(
    'addresses.json', 'w', encoding='utf-8') as n:
    reader, parks = csv.DictReader(f, delimiter=';'), {}
    for i in reader:
        parks.setdefault(i['AdmArea'], {}).setdefault(i['District'], []).append(i['Address'])
    json.dump(parks, n, indent=3, ensure_ascii=False)