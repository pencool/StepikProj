import calendar, locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def get_weekday(number):
    try:
        if type(number) is not int:
            raise TypeError('Аргумент не является целым числом')
        if number < 1 or number > 7:
            raise ValueError('Аргумент не принадлежит требуемому диапазону')
        return calendar.day_name[number-1].title()
    except TypeError as err:
        print(err)
        return type(err)
    except ValueError as e:
        print(e)
        return type(e)

print(get_weekday(1))