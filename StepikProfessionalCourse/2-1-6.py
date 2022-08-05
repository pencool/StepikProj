def is_valid(string):
    return True if 4 <= len(string) <= 6 and all(map(lambda x: x.isdigit(), string)) and ' ' not in string else False


print(is_valid('49 83'))
