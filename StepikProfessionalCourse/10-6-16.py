# def is_prime(num):
#     return sum((1 for i in range(1, num + 1) if num % i == 0)) == 2
is_prime = lambda x: sum((1 for i in range(1, x + 1) if x % i == 0)) == 2

print(is_prime(3))