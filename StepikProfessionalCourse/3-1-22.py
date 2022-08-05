from datetime import date


def saturdays_between_two_dates(start, end):
    return sum([1 for i in range(min(date.toordinal(start), date.toordinal(end)), max(date.toordinal(start), date.toordinal(end))+1) if date.fromordinal(i).weekday() == 5])


date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))