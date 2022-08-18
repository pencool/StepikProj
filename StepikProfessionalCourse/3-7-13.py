from datetime import datetime
import calendar

year = int(input())
tus = []
counter = 0
for month in range(1, 13):
    for week in calendar.monthcalendar(year=year, month=month):
        for day in week:
            if int(day) != 0 and calendar.weekday(year=year, month=month, day=int(day)) == 3:
                counter += 1
            if int(day) != 0 and calendar.weekday(year=year, month=month, day=int(day)) == 3 and counter == 3:
                tus.append(datetime(year=year, month=month, day=int(day)).strftime('%d.%m.%Y'))
    counter = 0
print(*tus, sep='\n')