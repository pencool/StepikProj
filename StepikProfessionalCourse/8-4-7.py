def get_all_values(nested_dicts: dict, key):
    res = set()

    def support(nested_dicts: dict):
        for k, v in nested_dicts.items():
            if k == key:
                res.add(str(v))
            if isinstance(v, dict):
                support(v)
        return res
    return support(nested_dicts)


my_dict = {
           'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
           'Timur': {'hobby': 'math'},
           'Dima': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))
