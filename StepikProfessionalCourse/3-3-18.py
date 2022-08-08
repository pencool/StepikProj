from datetime import datetime

with open('diary.txt') as f:
    print(*('\n'.join(j) + '\n' for j in sorted([i.split('\n') for i in f.read().split('\n\n')], key=lambda x: datetime.strptime(x[0], '%d.%m.%Y; %H:%M'))), sep='\n', end='\n')