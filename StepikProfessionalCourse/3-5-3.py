from datetime import datetime, timedelta, time
shop = {
    0: [timedelta(hours=9), timedelta(hours=21)],
    1: [timedelta(hours=9), timedelta(hours=21)],
    2: [timedelta(hours=9), timedelta(hours=21)],
    3: [timedelta(hours=9), timedelta(hours=21)],
    4: [timedelta(hours=9), timedelta(hours=21)],
    5: [timedelta(hours=10), timedelta(hours=18)],
    6: [timedelta(hours=10), timedelta(hours=18)]
}
x = input().split()
data, clock = datetime.strptime(x[0], '%d.%m.%Y').weekday(), timedelta(hours=int(x[1].split(':')[0]), minutes=int(x[1].split(':')[1]))
if shop[data][0] <= clock < shop[data][1]:
    print(int((shop[data][1] - clock).seconds / 60))
else:
    print('Магазин не работает')