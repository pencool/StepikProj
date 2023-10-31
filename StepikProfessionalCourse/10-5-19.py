from datetime import date, timedelta


def dates(start, count=None):
    i = 0
    while True:
        yield start
        if start >= date(year=9999, month=12, day=31):
            return StopIteration
        if count is not None and i >= count-1:
            return StopIteration
        start += timedelta(days=1)
        i += 1



generator = dates(date(2022, 3, 8), 5)

print(*generator)
