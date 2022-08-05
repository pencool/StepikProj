with open('forbidden_words.txt') as f, open('beegeek.txt') as b:
    x = b.read()
    b_low = x.lower()
    out = ''
    for j in f.read().split():
        rep = '*' * len(j)
        b_low = b_low.replace(j, rep)
    for i in range(len(b_low)):
        if list(b_low)[i] != '*':
            out += list(x)[i]
        else:
            out += '*'
    print(out)