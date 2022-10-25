from datetime import datetime

x = 0


def month():
    try:
        x: int = int(input())
    except (TypeError, ValueError):
        print('Введено некорректное значение')
    else:
        if not 1 <= x <= 12:
            return print('Введено число из недопустимого диапазона')
        print(datetime(month=x, day=x, year=x).strftime('%B'))

month()