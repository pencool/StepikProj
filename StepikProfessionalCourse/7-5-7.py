import re


def is_good_password(string):
    pattern = r"(?=.*[0-9])(?=.*[A-ZА-Я])(?=.*[a-zа-я])[" \
              r"0-9a-zA-ZА-Яа-я!@#$%^&*]{9,}"
    if re.fullmatch(pattern, string):
        return True
    return False

print(is_good_password('МойПарольСамыйЛучший111'))