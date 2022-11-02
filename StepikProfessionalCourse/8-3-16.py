def to_binary(number):
    if number // 2 == 0:
        return number % 2
    return f'{to_binary(number // 2)}{number % 2}'


print(to_binary(123123))
