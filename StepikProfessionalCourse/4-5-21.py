from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zf:
        if len(args) > 0:
            for i in args:
                zf.extract(i)
        else:
            zf.extractall()
