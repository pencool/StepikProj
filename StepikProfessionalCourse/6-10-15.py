from collections import ChainMap


def get_value(chainmap: ChainMap, key, from_left: bool = True):
    if key not in chainmap.keys():
        return None
    if not from_left:
        chainmap.maps.reverse()
    return chainmap[key]


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))
