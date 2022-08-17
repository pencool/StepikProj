#from datetime import datetime
info = {}
answer = []
for i in range(int(input())):
    *name, data = input().split()
    info.setdefault(data, []).append(name)
for k, v in info.items():
    if len(v) == len(sorted(info.values(), key=len, reverse=True)[0]):
        answer.append(k)
print(*sorted(answer, key=lambda x: x.split('.')[::-1]),sep='\n')
#print(*sorted(answer, key=lambda x: datetime.strptime(x, '%d.%m.%Y')),sep='\n')

