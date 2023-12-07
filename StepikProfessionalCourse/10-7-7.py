def filter_names(names, ignore_char, max_names):
    len_contr = 0
    for i in names:
        if i[0].lower() not in ignore_char.lower() and not any(map(str.isdigit, i)):
            len_contr += 1
            if len_contr <= max_names:
                yield i

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))