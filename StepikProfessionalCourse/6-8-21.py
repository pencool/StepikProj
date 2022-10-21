import csv
import json

with (open('quarter1.csv', encoding='utf-8') as q1,
      open('quarter2.csv', encoding='utf-8') as q2,
      open('quarter3.csv', encoding='utf-8') as q3,
      open('quarter4.csv', encoding='utf-8') as q4,
      open('prices.json', encoding='utf-8') as pr):
    total = 0
    price = json.load(pr)
    for i in [q1, q2, q3, q4]:
        for j in [*csv.reader(i)][1:]:
            total += price[j[0]] * sum(map(int, j[1:]))
    print(total)