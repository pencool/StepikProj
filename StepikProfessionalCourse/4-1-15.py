import sys
print(*[i for i in sys.stdin if not i.strip(' ').startswith('#')], sep='')