def comparator(x, y):
    if x + y > y + x:
        return True
    return False


def get_biggest(massive):
    if not massive:
        return -1
    massive = list(map(str, massive))
    n = len(massive)
    for i in range(n - 1):
        count_changes = False
        for j in range(n - 1 - i):
            if comparator(massive[j], massive[j + 1]):
                count_changes += True
                massive[j], massive[j + 1] = massive[j + 1], massive[j]
        if not count_changes and i == 0:
            x = ''.join(massive[::-1])
            if int(x) == 0:
                return 0
            return x
        elif not count_changes:
            x = ''.join(massive[::-1])
            if int(x) == 0:
                return 0
            return x
    x = ''.join(massive[::-1])
    if int(x) == 0:
        return 0
    return x

print(get_biggest([1, 2, 3]))