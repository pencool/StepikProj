from zipfile import ZipFile

with ZipFile('workbook.zip') as zp:
    cnt = len(zp.namelist())
    for i in zp.infolist():
        if i.is_dir():
            cnt -= 1
    print(cnt)