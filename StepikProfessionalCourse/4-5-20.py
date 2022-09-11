from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']

with ZipFile('files_size.zip', mode='a') as zp:
    for i in file_names:
        zp.write(i)

with ZipFile('files.zip', mode='a') as zf, ZipFile('files_size.zip') as zf2:
    for i in file_names:
        if zf2.getinfo(i).file_size <= 100:
            zf.write(i)
