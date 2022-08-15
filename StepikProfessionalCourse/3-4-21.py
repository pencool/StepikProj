from datetime import datetime
def fill_up_missing_dates(dates):
    rdates = sorted([datetime.strptime(i, '%d.%m.%Y') for i in dates])
    return [datetime.fromordinal(i).date().strftime('%d.%m.%Y') for i in range(rdates[0].toordinal(), rdates[-1].toordinal()+1)]






dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))