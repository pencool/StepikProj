from datetime import datetime


def is_available_date(dates, some_date):
    answer = []
    for i in range(len(dates)):
        if len(dates[i]) == 10:
            dates[i] = {int(datetime.strptime(dates[i], '%d.%m.%Y').toordinal())}
        else:
            dates[i] = {j for j in range(int(datetime.strptime(dates[i].split('-')[0], '%d.%m.%Y').toordinal()),
                       int(datetime.strptime(dates[i].split('-')[1], '%d.%m.%Y').toordinal())+1)}
    if len(some_date) == 10:
        some_date = {int(datetime.strptime(some_date, '%d.%m.%Y').toordinal())}
    else:
        some_date = {i for i in range(int(datetime.strptime(some_date.split('-')[0], '%d.%m.%Y').toordinal()),
                   int(datetime.strptime(some_date.split('-')[1], '%d.%m.%Y').toordinal())+1)}
    for i in dates:
        if len(some_date & i) == 0:
            answer.append(True)
        else:
            answer.append(False)
    return all(answer)


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))