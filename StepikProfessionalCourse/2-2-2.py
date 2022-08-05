import re
liter = [input() for i in range(3)]
if all(map(lambda x: x in "AaBCcEeHKMOoPpTXxy", liter)):
    print('en')
elif all(map(lambda x: x in "АаВСсЕеНКМОоРрТХху", liter)):
    print('ru')
else:
    print('mix')
