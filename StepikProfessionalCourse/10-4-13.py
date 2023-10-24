class CardDeck:
    def __init__(self):
        self.m = 0
        self.n = -1
        self.mas = ("пик", "треф", "бубен", "червей")
        self.nom = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет",
                    "дама", "король", "туз")

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= len(self.nom) - 1:
            self.m += 1
            self.n = - 1
        if self.m >= len(self.mas):
            raise StopIteration
        else:
            self.n += 1
        return f'{self.nom[self.n]} {self.mas[self.m]}'


cards = list(CardDeck())

print(cards)
print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])
