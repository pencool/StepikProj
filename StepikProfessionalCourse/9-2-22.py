func, line = input(), list(map(int, input().split()))
results = []
for x in range(line[0], line[-1]+1):
    results.append(eval(func))
print(f'Минимальное значение функции {func} на отрезке [{line[0]}; {line[-1]}] равно {min(results)}')
print(f'Максимальное значение функции {func} на отрезке [{line[0]}; {line[-1]}] равно {max(results)}')