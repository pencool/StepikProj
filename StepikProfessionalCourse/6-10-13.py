from collections import ChainMap


def get_all_values(chainmap: ChainMap, key):
    res_massive = [*map(lambda x: x.get(key, None), chainmap.maps)]
    if not any(res_massive):
        return set()
    else:
        return set(filter(lambda x: x is not None, res_massive))


chainmap = ChainMap({'name': 'Anri', 'city': 'Moscow'}, {'name': 'Arthur', 'city': 'Moscow'}, {'name': 'Timur', 'age': 29, 'city': 'Moscow'})

result = get_all_values(chainmap, 'city')

print(*sorted(result))
