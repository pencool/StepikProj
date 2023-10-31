def primes(left, right):
    pr = []
    for i in range(left, right + 1):
        x = 0
        for j in range(2, i):
            if i % j == 0:
                x += 1
        if x == 0 and i != 1:
            yield i


generator = primes(1, 15)

print(*generator)
