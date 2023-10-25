class Alphabet:
    def __init__(self, language):
        self.n = -1
        self.language = language
        self.local = {'en': 'abcdefghijklmnopqrstuvwxyz',
                      'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        try:
            return next(iter(self.local[self.language][self.n]))
        except (StopIteration, IndexError):
            self.n = 0
        return next(iter(self.local[self.language][self.n]))


en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)
