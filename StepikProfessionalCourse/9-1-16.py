word = input()


def even_sort(x):
    if x.isdigit():
        return 1 if int(x) % 2 == 0 else 0
    return x


print(''.join(sorted(sorted(word),
             key=lambda x: (x == x.upper(), x == x.lower(), even_sort(x)))))
