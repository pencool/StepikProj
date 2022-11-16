def my_pow(number: int):
    return sum(map(lambda x: int(x[1]) ** int(x[0]+1), enumerate(list(str(
        number)))))


print(my_pow(139))
