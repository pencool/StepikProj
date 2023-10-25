from random import choices


class RandomNumbers:
    def __init__(self, l, r, n):
        self.i = -1
        self.l = l
        self.r = r
        self.n = n
        self.itr = iter(choices(list(range(self.l, self.r + 1)), k=self.n))

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i >= self.n:
            raise StopIteration
        return next(self.itr)


iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))
