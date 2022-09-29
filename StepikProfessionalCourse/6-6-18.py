from collections import OrderedDict

data = OrderedDict(
    {'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
     'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
     'District': 'район Арбат',
     'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
     'SeatsCount': '10'})

data2 = OrderedDict()
for i in range(len(data)):
    if i % 2 == 0:
        data2 |= OrderedDict([data.popitem(last=False)])
    else:
        data2 |= OrderedDict([data.popitem()])
print(data2)
