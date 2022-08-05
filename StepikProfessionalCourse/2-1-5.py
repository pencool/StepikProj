def same_parity(numbers):
    return [*filter(lambda x: abs(x % 2) == (abs(numbers[0]) % 2), numbers)]


print(same_parity([-7, 0, 67, -9, 70, -29, 90]))
