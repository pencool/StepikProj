def sum_nums(num):
    return sum((num := map(int, list(num))))


print(*sorted(input().split(), key=sum_nums))
