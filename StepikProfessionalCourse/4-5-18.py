from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zp:
    for i in sorted(zp.namelist(), key=lambda x: x.split('/')[-1].lower()):
        if not zp.getinfo(i).is_dir():
            print(f'{zp.getinfo(i).filename.split("/")[-1]}\n  '
                  f'Дата модификации файла: {datetime(*zp.getinfo(i).date_time)}\n  '
                  f'Объем исходного файла: {zp.getinfo(i).file_size} байт(а)\n  '
                  f'Объем сжатого файла: {zp.getinfo(i).compress_size} байт(а)\n')
