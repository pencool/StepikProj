from datetime import datetime

start, end = datetime.strptime(input(), '%d.%m.%Y').toordinal(), datetime.strptime(input(), '%d.%m.%Y').toordinal()
while (datetime.fromordinal(start).day + datetime.fromordinal(start).month) % 2 == 0:
    start += 1
for i in range(start, end + 1, 3):
    if datetime.fromordinal(i).weekday() != 0 and datetime.fromordinal(i).weekday() != 3:
        print(datetime.fromordinal(i).strftime('%d.%m.%Y'))