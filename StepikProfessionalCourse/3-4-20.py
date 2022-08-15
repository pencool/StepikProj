from datetime import datetime
dates = [datetime.strptime(i, '%d.%m.%Y') for i in input().split()]
print([abs(dates[i] - dates[i + 1]).days for i in range(len(dates)-1)])
