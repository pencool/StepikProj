def primes(left, right):
    for i in range(left, right + 1):
        x = 0
        for j in range(2, i):
            x += i % j
        if x == 0 and i != 1:
            yield i


generator = primes(1, 15)

print(*generator)
