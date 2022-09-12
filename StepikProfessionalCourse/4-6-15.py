import pickle

with open(input(), 'rb') as bf:
    massive = pickle.load(bf)
    md = int(input())
    if type(massive) is list:
        lst = [i for i in massive if type(i) is int]
        if len(lst) == 0:
            lst = [0]
        print('Контрольные суммы совпадают' if min(lst) * max(lst) == md else
              'Контрольные суммы не совпадают')
    elif type(massive) is dict:
        lst = [i for i in massive.keys() if type(i) is int]
        if len(lst) == 0:
            lst = [0]
        print('Контрольные суммы совпадают' if sum(lst) == md else
              'Контрольные суммы не совпадают')
