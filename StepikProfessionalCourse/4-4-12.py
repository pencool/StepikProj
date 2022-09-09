import json
from datetime import datetime

with open('pools.json', encoding='utf-8') as f:
    pools = filter(lambda x: datetime.strptime(
        x['WorkingHoursSummer']['Понедельник'].split('-')[0], '%H:%M').hour
                             <= 10 and datetime.strptime(
        x['WorkingHoursSummer']['Понедельник'].split('-')[1], '%H:%M').hour
                             >= 12, json.load(f))
    best_pool = sorted(sorted(pools,
                              key=lambda x: x['DimensionsSummer']['Width'],
                              reverse=True),
                       key=lambda x: x['DimensionsSummer']['Length'],
                       reverse=True)[0]
    print(f"{best_pool['DimensionsSummer']['Length']}x"
          f"{best_pool['DimensionsSummer']['Width']}\n"
          f"{best_pool['Address']}")
