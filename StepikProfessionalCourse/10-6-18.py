all_together = lambda *args: (j for i in args for j in i)



objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))
