from datetime import datetime

lstdays = ['день', 'дня', 'дней']
lsthrs = ['час', 'часа', 'часов']
lstmins = ['минута', 'минуты', 'минут']


def choose_plural(num, words):
    num1 = num
    num = int(str(num)[-2:])
    if int(list(str(num))[-1]) == 1 and num != 11:
        return f'{num1} {words[0]}'
    elif int(list(str(num))[-1]) in (2, 3, 4) and num not in (12, 13, 14):
        return f'{num1} {words[1]}'
    else:
        return f'{num1} {words[-1]}'


curclock = datetime.strptime(input(), '%d.%m.%Y %H:%M')
startcourse = datetime(day=8, month=11, year=2022, hour=12, minute=0)
remainder = startcourse - curclock
if curclock >= startcourse:
    print(f'Курс уже вышел!')
elif remainder.seconds < 3600 and remainder.days > 0:
    print(f'До выхода курса осталось: {choose_plural(remainder.days, lstdays)}')
elif remainder.days == 0:
    if remainder.days == 0 and remainder.seconds % 3600 < 60:
        print(f'До выхода курса осталось: {choose_plural(remainder.seconds // 3600, lsthrs)}')
    elif remainder.days == 0 and remainder.seconds < 3600:
        print(f'До выхода курса осталось: {choose_plural(remainder.seconds // 60, lstmins)}')
    else:
        print(
            f'До выхода курса осталось: {choose_plural(remainder.seconds // 3600, lsthrs)} и {choose_plural(remainder.seconds % 3600 // 60, lstmins)}')
else:
    print(
        f'До выхода курса осталось: {choose_plural(remainder.days, lstdays)} и {choose_plural(remainder.seconds // 3600, lsthrs)}')
