import re


def convert(text):
    low = re.findall(r'[a-zа-я]', text)
    up = re.findall(r'[A-ZА-Я]', text)
    if len(low) > len(up):
        return text.lower()
    elif len(low) == len(up):
        return text.lower()
    elif len(low) < len(up):
        return text.upper()


print(convert('BEEgeek'))
