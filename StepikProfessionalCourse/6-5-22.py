from collections import defaultdict


def wins(pairs):
    winner_list = defaultdict(set)
    for k, v in pairs:
        winner_list[k].add(v)
    return winner_list


result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))
