import csv

with open('wifi.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    points = {}
    for i in reader:
        points[i['district']] = points.get(i['district'], 0) + int(
            i['number_of_access_points'])
    for i in sorted(sorted(points.items()), key=lambda x: -x[-1]):
        print(f'{i[0]}: {i[1]}')
