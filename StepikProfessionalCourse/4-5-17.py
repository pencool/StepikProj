from zipfile import ZipFile
from datetime import datetime

names = []
with ZipFile('workbook.zip') as zp:
    for i in zp.infolist():
        if not i.is_dir() and datetime(*i.date_time) > datetime(year=2021,
                                                                month=11,
                                                                day=30,
                                                                hour=14,
                                                                minute=22,
                                                                second=00):
            names.append(i.filename.split('/')[-1])
    print(*sorted(names), sep='\n')
