from datetime import timedelta, datetime
refday = datetime.strptime(input()[:5], '%d.%m')
info = {}
for i in range(int(input())):
    *name, data = input().split()
    if (refday < datetime.strptime(data[:5], '%d.%m') <= (refday + timedelta(days=7))) or (refday < (datetime.strptime(data[:5], '%d.%m')+timedelta(days=360)) <= (refday + timedelta(days=7))):
        info.setdefault(data, []).append(name)
print(' '.join(*info[sorted(info, key=lambda x: datetime.strptime(x, '%d.%m.%Y'))[-1]]) if len(info) != 0 else 'Дни рождения не планируются')