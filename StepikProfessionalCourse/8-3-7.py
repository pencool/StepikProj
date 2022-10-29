def sum_nums(n = int(input())):
    x = 0
    if n // 10 != 0:
        x = sum_nums(n//10)
    return n % 10 + x
print(sum_nums())