import sys

socks = sys.stdin.readlines()
if len(socks) % 2 == 0 and int(socks[-1].strip('\n')) % 2 == 0 or len(socks) % 2 == 1 and int(socks[-1].strip('\n')) % 2 == 1:
    print('Дима')
else:
    print('Анри')
