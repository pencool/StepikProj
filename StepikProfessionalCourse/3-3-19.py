from datetime import datetime


def is_available_date(dates, some_date):
    answer = []
    for i in range(len(dates)):
        if len(dates[i]) == 10:
            dates[i] = {int(datetime.strptime(dates[i], '%d.%m.%Y').timestamp())}
        else:
            dates[i] = {j for j in range(int(datetime.strptime(dates[i].split('-')[0], '%d.%m.%Y').timestamp()),
                       int(datetime.strptime(dates[i].split('-')[1], '%d.%m.%Y').timestamp()))}
    if len(some_date) == 10:
        some_date = {int(datetime.strptime(some_date, '%d.%m.%Y').timestamp())}
    else:
        some_date = {i for i in range(int(datetime.strptime(some_date.split('-')[0], '%d.%m.%Y').timestamp()),
                   int(datetime.strptime(some_date.split('-')[1], '%d.%m.%Y').timestamp()))}
    for i in dates:
        if len(some_date & i) == 0:
            answer.append(True)
        else:
            answer.append(False)
    print(answer)
    return True if True in answer else False


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))
