import json

with open('data.json', 'r', encoding='utf-8') as f, open(
        'updated_data.json', 'w', encoding='utf-8') as n:
    new_list = []
    for i in json.load(f):
        print(type(i))
        if type(i) is str:
            new_list.append(i + '!')
        elif type(i) is int:
            new_list.append(i + 1)
        elif type(i) is bool:
            new_list.append(not i)
        elif type(i) is list:
            new_list.append(i * 2)
        elif type(i) is dict:
            i.update({'newkey': None})
            new_list.append(i)
    json.dump(new_list, n, indent=3)

print(new_list)
