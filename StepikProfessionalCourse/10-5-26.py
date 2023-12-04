def palindromes():
    i = 1
    while True:
        if str(i) == str(i)[::-1]:
            yield i
        i += 1


generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)
