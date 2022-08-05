n = int(input())
lst = [[*map(int, input().split())] for i in range(n)]
for i in range(n):
    for j in range(i, n):
        lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
for i in lst:
    print(*i)