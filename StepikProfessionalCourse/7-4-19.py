import re


def get_id(names: list, name):
    try:
        if type(name) is not str:
            raise TypeError('Имя не является строкой')
        if not re.fullmatch(r'^[A-Z]{1}[a-z]+', name):
            raise ValueError('Имя не является корректным')
        return len(names) + 1
    except TypeError as err:
        return err
    except ValueError as e:
        return e


names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'ruslan'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)
