from datetime import datetime
import sys

dates = [datetime.strptime(i.strip('\n'), '%Y-%m-%d') for i in sys.stdin.readlines()]
print((max(dates) - min(dates)).days)