from collections import OrderedDict

data = OrderedDict(
    {'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
     'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
     'District': 'район Арбат',
     'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
     'SeatsCount': '10'})
data2 = OrderedDict()
for k, v in reversed(data.items()):
    data2[k] = v
print(data2)