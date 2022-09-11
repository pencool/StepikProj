from zipfile import ZipFile

with ZipFile('workbook.zip') as zp:
    v = [0, 0]
    for i in zp.infolist():
        v[0] += i.file_size
        v[1] += i.compress_size
    print(f'Объем исходных файлов: {v[0]} байт(а)\n'
          f'Объем сжатых файлов: {v[1]} байт(а)')