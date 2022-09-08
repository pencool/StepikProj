import csv

with open('titanic.csv') as f:
    for i in [*sorted(filter(
            lambda x: float(x['age']) < 18 and float(x['survived']) == 1,
            csv.DictReader(f, delimiter=';')),
            key=lambda x: x['sex'], reverse=True)]:
        print(i['name'], sep='\n')
