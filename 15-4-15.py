def sum_nums(num):
    return sum((num := map(int, list(str(num)))))


print(*sorted(sorted(map(int, input().split())), key=sum_nums))
