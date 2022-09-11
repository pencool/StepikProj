from zipfile import ZipFile


def converter(x):
    space = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}
    for i in space.keys():
        if 1 < x < 1024:
            return f'{int(round(x))} {i}'
        else:
            x = x / 1024


with ZipFile('desktop.zip') as zf:
    for i in zf.infolist():
        spaces = i.filename.strip('/').count('/')
        if i.is_dir():
            print(f"{'  ' * spaces}{i.filename.strip('/').split('/')[-1]}")
        else:
            print(f"{'  ' * spaces}{i.filename.strip('/').split('/')[-1]} "
                  f"{converter(i.file_size)}")
