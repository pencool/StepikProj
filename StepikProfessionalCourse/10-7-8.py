import csv


def invest():
    with open('data.csv', 'r', encoding='utf-8') as f:
        x = csv.DictReader(f)
        return sum((int(i['raisedAmt']) for i in x if i['round'] == 'a'))


print(invest())
