def natural_digits():
    def func(n):
        if n >= 1:
            func(n - 1)
            print(n)
    func(100)

natural_digits()