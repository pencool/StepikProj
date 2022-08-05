n = int(input())
lst = [[*map(int, input().split())] for i in range(n)]
counter = 0
for i in range(n):
    for j in range(n):
        if i >= n - 1 -j and lst[i][j] > counter:
            counter = lst[i][j]
print(counter)
