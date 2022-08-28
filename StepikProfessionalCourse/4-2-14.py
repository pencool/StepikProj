import csv

with open('salary_data.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    rows = [i for i in reader]
    zp = {}
    ct = {}
    for i in rows[1:]:
        zp[i[0]] = zp.get(i[0], 0) + int(i[1])
        ct[i[0]] = ct.get(i[0], 0) + 1
    zp = {i: zp[i] / ct[i] for i in zp}
    print(*map(lambda x: x[0],
               sorted(zp.items(), key=lambda x: x[1])), sep='\n')
