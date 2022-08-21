import sys
from datetime import datetime

dates = [datetime.strptime(i.strip(), '%d.%m.%Y') for i in sys.stdin]
trfl = []
if sorted(dates) == dates:
    print('ASC')
elif sorted(dates, reverse=True) == dates:
    print('DESC')
else:
    print('MIX')
