import functools


class Fibonacci:
    def __init__(self):
        self.n = 0

    def __iter__(self):
        return self

    @functools.lru_cache()
    def fib(self, n):
        if n <= 2:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def __next__(self):
        self.n += 1
        return self.fib(self.n)


fibonacci = Fibonacci()

for _ in range(50):
    print(next(fibonacci))
