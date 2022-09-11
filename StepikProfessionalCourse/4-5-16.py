from zipfile import ZipFile

best_compression = [100, 100]
with ZipFile('workbook.zip') as zp:
    for i in zp.infolist():
        if i.is_dir() == False and i.compress_size / i.file_size * 100 < \
                best_compression[1]:
            best_compression = [str(i.filename).split('/')[-1],
                                i.compress_size / i.file_size * 100]
    print(best_compression[0])
