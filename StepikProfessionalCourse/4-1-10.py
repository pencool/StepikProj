import sys

for i in sys.stdin:
    print(i.strip('\n')[::-1])