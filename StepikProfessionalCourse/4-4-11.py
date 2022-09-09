import csv
import json

with open('students.json', encoding='utf-8') as f, open(
    'data3.csv', 'w', encoding='utf-8') as out:
    studs = [[i['name'], i['phone']] for i in json.load(f)
             if i['age'] >= 18 and i['progress'] >= 75]
    csv.writer(out).writerow(['name', 'phone'])
    csv.writer(out).writerows(sorted(studs))
