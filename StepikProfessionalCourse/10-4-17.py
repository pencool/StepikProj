from random import choices


class Xrange:
    def __init__(self, s, e, step=1):
        self.i = s - step
        self.s = s
        self.e = e
        self.step = step
        self.itr = self.rng()

    def __iter__(self):
        return self

    def rng(self):
        mas = [self.s]
        x = self.s
        for i in range(int(self.s * 100), int((self.e - self.step) * 100),
                       int(self.step * 100)):
            x += self.step
            mas.append(x)
            print(mas)
        return iter(mas)

    def __next__(self):
        self.i += self.step
        if self.step < 0:
            if self.i < self.e:
                raise StopIteration
        else:
            if self.i >= self.e:
                raise StopIteration
        return next(self.itr)


xrange = Xrange(10, 1, -1)

print(*xrange)
