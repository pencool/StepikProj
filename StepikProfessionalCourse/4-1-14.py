import sys
print(len([1 for i in sys.stdin if i.strip(' ').startswith('#')]))