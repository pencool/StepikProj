import calendar
from datetime import datetime


def get_days_in_month(year, month):
    answer = []
    month = list(calendar.month_name).index(month)
    all_dates = calendar.monthcalendar(year, month)
    for i in range(len(all_dates)):
        for j in all_dates[i]:
            if int(j) != 0:
                answer.append(datetime(year=year, month=month, day=int(j)).date())
    return answer


print(get_days_in_month(2021, 'December'))
