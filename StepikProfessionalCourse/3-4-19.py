from datetime import datetime, timedelta

dates = []
data = datetime.strptime(input(), '%d.%m.%Y').date()
while len(dates) < 10:
    dates.append(data.strftime('%d.%m.%Y'))
    data += timedelta(days=len(dates)+1)
print(*dates, sep='\n')