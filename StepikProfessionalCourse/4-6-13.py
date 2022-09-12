import pickle
import sys

with open(input(), 'rb') as bf:
    func = pickle.load(bf)
    print(func(*[i.strip('\n') for i in sys.stdin]))
