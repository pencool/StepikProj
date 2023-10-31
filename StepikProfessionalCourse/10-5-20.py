card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама",
               "король", "туз"]

card_mast = ["пик", "треф", "бубен", "червей"]


def card_deck(suit):
    del card_mast[card_mast.index(suit)]
    i = 0
    j = 0
    while True:
        if j >= len(card_values):
            j = 0
            i += 1
        if i >= len(card_mast):
            i = 0
        yield ' '.join([card_values[j], card_mast[i]])
        j += 1


generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)