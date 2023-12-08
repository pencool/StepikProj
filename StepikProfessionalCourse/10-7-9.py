import calendar
from datetime import datetime

def years_days(year):
    for i in calendar(year):
        for j in i.days():
            print(j)

years_days(2022)