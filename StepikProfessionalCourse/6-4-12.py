import csv
from collections import namedtuple
from datetime import datetime

with open('meetings.csv', encoding='utf-8') as f:
    fields, *rows = csv.reader(f)
    Meet = namedtuple('Meet', [*fields])
    meets = [Meet(*i) for i in rows]
    for i in sorted(meets, key=lambda x: (
            datetime.strptime(x.meeting_date, '%d.%m.%Y'),
            datetime.strptime(x.meeting_time, '%H:%M'))):
        print(f'{i.surname} {i.name}')


