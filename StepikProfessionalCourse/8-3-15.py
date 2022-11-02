def is_palindrome(string):
    if string:
        if string[0] == string[-1]:
            is_palindrome(string[1:-2])
            return True
        else:
            return False
    else:
        return True

print(is_palindrome(''))