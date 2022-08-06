import datetime
from datetime import date
def is_correct(day, month, year):
    try:
        correct_date = date(year, month, day)
        return type(correct_date) is datetime.date
    except ValueError:
        return False

print(is_correct(31, 12, 2021))
#print(is_correct(31, 13, 2021))