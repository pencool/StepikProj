from random import choices


class Xrange:
    def __init__(self, s, e, step):
        self.i = -1
        self.s = s
        self.e = e
        self.step = step

    def __iter__(self):
        return self

    def rng(self):
        mas = [self.s]
        x = self.s
        for i in range(int((self.e - self.s) / self.step)):
            x += self.step
            mas.append(x)
        return iter(mas)

    def __next__(self):
        self.i += 1
        if self.i >= self.e:
            raise StopIteration
        return next(self.rng())


xrange = Xrange(0, 3, 0.5)

print(*xrange, sep='; ')
