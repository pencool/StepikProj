import json


with open('people.json', 'r', encoding='utf-8') as f, open(
    'updated_people.json', 'w', encoding='utf-8') as n:
    data = json.load(f)
    bufer_dict = {j: None for i in data for j in i.keys()}
    json.dump([bufer_dict|i for i in data], n, indent=3)
