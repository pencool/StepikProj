n = int(input())
snow = [['.' for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if (i==j) or (j == n - 1 - i) or (i == n//2) or (j == n // 2):
            snow[i][j] = '*'
for i in snow:
    print(*i)