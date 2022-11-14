def convert(number):
    return tuple([format(number, 'b'),
                  format(number, 'o'),
                  format(number, 'X')])

print(convert(-24))