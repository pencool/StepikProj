def dict_travel(nested_dicts: dict):
    res = []

    def dot_notion(nested_dicts: dict, notion=''):
        for k, v in nested_dicts.items():
            if not isinstance(v, dict):
                res.append(f'{notion}{k}: {v}')
            if isinstance(v, dict):
                dot_notion(v, notion=notion + f'{k}.')
        return sorted(res)
    return print(*dot_notion(nested_dicts), sep='\n')


data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)
