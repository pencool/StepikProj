def get_value(nested_dicts: dict, key):
    if key in nested_dicts.keys():
        return nested_dicts[key]
    for k, v in nested_dicts.items():
        if isinstance(v, dict):
            value = get_value(v, key)
            if value is not None:
                return value


data = {'firstName': 'Тимур', 'lastName': 'Гуев',
        'birthDate': {'day': 10, 'month': 'October', 'year': 1993},
        'address': {'streetAddress': 'Часовая 25, кв. 127',
                    'city': {'region': 'Московская область', 'type': 'город',
                             'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'cityName'))
