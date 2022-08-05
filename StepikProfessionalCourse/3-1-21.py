from datetime import date


def get_date_range(start, end):
    return [date.fromordinal(i) for i in range(date.toordinal(start), date.toordinal(end)+1)] if start <= end else []


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')
