from collections import defaultdict


def flip_dict(dict_of_lists: dict):
    flp_dict = defaultdict(list)
    for k, v in dict_of_lists.items():
        for j in v:
            flp_dict[j].append(k)
    return flp_dict


print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))