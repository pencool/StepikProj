def tribonacci(n):
    cach = {1: 1, 2: 1, 3: 1}
    def func(n):
        res = cach.get(n)
        if res is None:
            res = func(n - 1) + func(n - 2) + func(n - 3)
            cach[n] = res
        return res
    return func(n)


print(tribonacci(300))
