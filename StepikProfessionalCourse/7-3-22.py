try:
    f = open(input(), encoding='utf-8')
    try:
        print(f.read())
    finally:
        f.close()
except FileNotFoundError:
    print('Файл не найден')
