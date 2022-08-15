from datetime import time, timedelta, datetime
start, end = input().split(':'), input().split(':')
start = timedelta(hours=int(start[0]), minutes=int(start[1]))
end = timedelta(hours=int(end[0]), minutes=int(end[1]))
for i in range(start.seconds, end.seconds+1, 55*60):
    if i + 45*60 < end.seconds+1:
        print(f"{datetime.strptime(str(timedelta(seconds=i)), '%H:%M:%S').strftime('%H:%M')} - {datetime.strptime(str(timedelta(seconds=i + 45*60)), '%H:%M:%S').strftime('%H:%M')}")
