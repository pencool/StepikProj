def print_digits(n):
    if n % 10 > 0:
        print(n % 10)
        print_digits(n // 10)

print_digits(6)