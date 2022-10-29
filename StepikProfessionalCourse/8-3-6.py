def count_nums(n=input()):
    def func(n, nums=0):
        if n:
            return func(n[1:], nums + 1)
        return nums

    return func(n)


print(count_nums())
