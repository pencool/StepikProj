import numbers


def alternating_sequence(count=None):
    num = 1
    while abs(num) - 1 != count:
        yield num
        num = int((abs(num) + 1) * -(num / abs(num)))


generator = alternating_sequence(10)

print(*generator)