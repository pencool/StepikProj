n, m = map(int, input().split())
lst = [[0] * m for i in range(n)]
direction = ['right', 'down', 'left', 'top']
cur_dir = 'right'
i, j = 0, 0
for c in range(1, (n * m) + 1):
    if cur_dir == 'right':
        try:
            if cur_dir == 'right' and lst[i][j + 1] == 0:
                lst[i][j] = c
                j += 1
                continue
            else:
                lst[i][j] = c
                i += 1
                cur_dir = 'down'
                continue
        except IndexError:
            lst[i][j] = c
            i += 1
            cur_dir = 'down'
            continue
    if cur_dir == 'down':
        try:
            if cur_dir == 'down' and lst[i + 1][j] == 0:
                lst[i][j] = c
                i += 1
                continue
            else:
                lst[i][j] = c
                j -= 1
                cur_dir = 'left'
                continue
        except IndexError:
            lst[i][j] = c
            j -= 1
            cur_dir = 'left'
            continue
    if cur_dir == 'left':
        try:
            if cur_dir == 'left' and lst[i][j - 1] == 0:
                lst[i][j] = c
                j -= 1
                continue
            else:
                lst[i][j] = c
                i -= 1
                cur_dir = 'top'
                continue
        except IndexError:
            lst[i][j] = c
            i -= 1
            cur_dir = 'top'
            continue
    if cur_dir == 'top':
        try:
            if cur_dir == 'top' and lst[i - 1][j] == 0:
                lst[i][j] = c
                i -= 1
                continue
            else:
                lst[i][j] = c
                j += 1
                cur_dir = 'right'
                continue
        except IndexError:
            lst[i][j] = c
            j += 1
            cur_dir = 'right'
            continue
for i in range(n):
    print(*lst[i])







