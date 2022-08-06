from datetime import date
counter = 0
while True:
    date_for_test = input()
    if date_for_test == 'end':
        print(counter)
        break
    day, month, year = map(int, date_for_test.split('.'))
    try:
        date(year, month, day)
        print('Корректная')
        counter += 1
    except ValueError:
        print('Некорректная')