from datetime import datetime
import csv

with open('name_log.csv') as f, open('new_name_log.csv', 'w', newline='') as n:
    last_names = {}
    for i in [*csv.DictReader(f)]:
        if datetime.strptime(
                i['dtime'], '%d/%m/%Y %H:%M') > datetime.strptime(
            last_names.setdefault(
                i['email'], [i['username'], i['dtime']])[1], '%d/%m/%Y %H:%M'):
            last_names[i['email']] = [i['username'], i['dtime']]
    writer = csv.writer(n)
    writer.writerow(['username', 'email', 'dtime'])
    for i in sorted(last_names.items()):
        writer.writerow([i[1][0], i[0], i[1][1]])
