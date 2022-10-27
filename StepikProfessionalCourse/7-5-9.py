import sys


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


for i in sys.stdin:
    try:
        i = i.strip()
        if len(i) <= 9:
            raise LengthError('LengthError')
        if i == i.upper() or i == i.lower():
            raise LetterError('LetterError')
        if all(map(lambda x: not x.isdigit(), i)):
            raise DigitError('DigitError')
        print('Success!')
        break
    except (LengthError, LetterError, DigitError) as e:
        print(e)
