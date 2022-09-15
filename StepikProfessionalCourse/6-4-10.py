import pickle
from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
with open('data.pkl', 'rb') as bf:
    for i in pickle.load(bf):
        pet = Animal(*i)
        for k, v in zip(Animal._fields, pet):
            print(f'{k}: {v}')
        print()