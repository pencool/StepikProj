from datetime import datetime, date
birthdays = [*map(lambda x: [x[0], x[1], datetime.strptime(x[2], '%d.%m.%Y')], [input().split() for i in range(int(input()))])]
oldest = min(birthdays, key=lambda x: x[2])
count = 0
for i in birthdays:
    if i[2] == oldest[2]:
        count += 1
if count > 1:
    print(f"{oldest[2].strftime('%d.%m.%Y')} {count}")
else:
    print(f"{oldest[2].strftime('%d.%m.%Y')} {oldest[0]} {oldest[1]}")