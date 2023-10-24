class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.n = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        if self.n >= len(self.iterable):
            self.n = 0
        return self.iterable[self.n]


cycle = Cycle(range(100_000_000))

print(next(cycle))
print(next(cycle))