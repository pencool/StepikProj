class DictItemsIterator:
    def __init__(self, data: dict):
        self.data = data
        self.n = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        if self.n >= len(self.data):
            raise StopIteration
        ans = list(enumerate(self.data))[self.n][1]
        return ans, self.data[ans]


pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)