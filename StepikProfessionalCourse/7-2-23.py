from sys import stdin

total = 0
not_digit = 0

for i in stdin:
    try:
        total += int(i)
    except ValueError:
        try:
            total += float(i)
        except ValueError:
            not_digit += 1
print(total, not_digit, sep='\n')
