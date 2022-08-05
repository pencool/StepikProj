from math import *


def quad(element):
    return element ** 2


def kub(element):
    return element ** 3


operations = {'квадрат': quad, 'куб': kub, 'корень': sqrt, 'модуль': abs, 'синус': sin}
num, fn = int(input()), input()
x = operations[fn]
print(x(num))
