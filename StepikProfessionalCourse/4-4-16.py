import json

with open('food_services.json', encoding='utf-8') as f:
    type_objects = {}
    for i in json.load(f):
        if type_objects.setdefault(
        i['TypeObject'], (i['Name'], i['SeatsCount']))[1] < i['SeatsCount']:
            type_objects[i['TypeObject']] = i['Name'], i['SeatsCount']
    for k, v in sorted(type_objects.items()):
        print(f'{k}: {v[0]}, {v[1]}')