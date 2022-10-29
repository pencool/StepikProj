def is_power(number):
    if number == 1 or number == 2:
        return True
    else:
        if number > 2:
            return is_power(number/2)
        return False

print(is_power(1))