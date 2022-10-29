def get_fast_pow(a, n):
    if n > 0:
        if n % 2 == 0:
            return get_fast_pow((a**2), n/2)
        if n % 2 == 1:
            return a * get_fast_pow(a, n-1)
    return 1

print(get_fast_pow(5, 2))