from random import choice


class RandomNumbers:
    def __init__(self, l, r, n):
        self.i = -1
        self.l = l
        self.r = r
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        itr = lambda: choice(list(range(self.l, self.r + 1)))
        return iter(itr, self.r + 2)


iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))
