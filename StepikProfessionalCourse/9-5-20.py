def sort_priority(nmbrs, group):
    global numbers
    global data
    group = set(group).intersection(nmbrs)
    nmbrs = set(nmbrs)
    group = set(group)
    nmbrs.difference_update(group)
    ans = sorted(list(group)) + sorted(list(nmbrs))
    nmbrs = numbers = data = ans
    return nmbrs


data = list(range(0, 100, 5))
sort_priority(data, {1, 90, 95, 25, 55, 64})

print(data)
