def print_digits(n):
    if n // 10 != 0 or n % 10 != 0:
        print_digits(n // 10)
        print(n % 10)


print_digits(20000000077)
