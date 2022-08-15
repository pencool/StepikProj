from datetime import datetime, timedelta
def num_of_sundays(yy):
    counter = 0
    data = datetime(year=yy, month=1, day=1)
    while data.year == yy:
        if data.weekday() == 6:
            counter += 1
        data = data + timedelta(days=1)
    return counter

print(num_of_sundays(2022))