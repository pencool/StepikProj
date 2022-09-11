import json

with open('food_services.json', encoding='utf-8') as f:
    dist, netname = {}, {}
    for i in json.load(f):
        dist[i['District']] = dist.setdefault(i['District'], 0) + 1
        if i['IsNetObject'] == 'да':
            netname[i['OperatingCompany']] = netname.setdefault(
                i['OperatingCompany'], 0) + 1
    print('{}: {}'.format(*max(dist.items(), key=lambda x: x[1])))
    print('{}: {}'.format(*max(netname.items(), key=lambda x: x[1])))
