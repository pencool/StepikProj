from collections import ChainMap


def deep_update(chainmap: ChainMap, key, value):
    if key not in chainmap.keys():
        chainmap[key] = value
    else:
        for i in chainmap.maps:
            if key in i.keys():
                i[key] = value
    return None


chainmap = ChainMap({'name': 'Tanya'}, {'name': 'Arthur'}, {'name': 'Timur'})

deep_update(chainmap, 'name', 'Dima')

print(chainmap)
