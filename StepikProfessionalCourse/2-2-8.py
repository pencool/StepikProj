import re

resnames = [re.sub(r'@.+', '', input()) for i in range(int(input()))]
for i in range(int(input())):
    x = input()
    counter = 0
    flag = True
    while flag:
        if x not in resnames and counter == 0:
            print(f'{x}@beegeek.bzz')
            resnames.append(x)
            flag = False
        elif x+str(counter) not in resnames and counter != 0:
            print(f'{x}{str(counter)}@beegeek.bzz')
            resnames.append(x+str(counter))
            flag = False
        counter += 1