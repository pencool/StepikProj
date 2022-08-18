from datetime import datetime, timedelta
import calendar


def get_all_mondays(year):
    if calendar.isleap(year):
        return [(datetime(year=year, month=1, day=1) + timedelta(i)).date() for i in range(timedelta(days=366).days) if
                (datetime(year=year, month=1, day=1) + timedelta(i)).date().weekday() == 0]
    elif not calendar.isleap(year):
        return [(datetime(year=year, month=1, day=1) + timedelta(i)).date() for i in range(timedelta(days=365).days) if
                (datetime(year=year, month=1, day=1) + timedelta(i)).date().weekday() == 0]


print(get_all_mondays(1864))
