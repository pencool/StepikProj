class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string: str):
    try:
        if len(string) < 9:
            raise LengthError()
        if string == string.upper() or string == string.lower():
            raise LetterError()
        if all(map(lambda x: not x.isdigit(), string)):
            raise DigitError()
        return True
    except (LengthError, LetterError, DigitError) as e:
        raise


try:
    print(is_good_password('Short7'))
except Exception as err:
    print(type(err))
