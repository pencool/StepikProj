from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')

birthday = date(1992, 10, 6)

print('Название месяца:', birthday.strftime('%B'))
print('Название дня недели:', birthday.strftime('%W'))
print('Год:', birthday.strftime('%Y'))
print('Месяц:', birthday.strftime('%m'))
print('День:', birthday.strftime('%d'))