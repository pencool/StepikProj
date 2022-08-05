def get_biggest(numbers):
    numbers = [*map(str, numbers)]
    for i in numbers:
        if len(i) == 1 and numbers.count(i) >= 2 and i != '0':
            x = i * numbers.count(i)
            for j in range(numbers.count(i)):
                numbers.remove(i)
            numbers.append(x)
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if int(numbers[j][0]) < int(numbers[j+1][0]):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            elif int(numbers[j][0]) == int(numbers[j+1][0]):
                for c in range(min([len(numbers[j]), len(numbers[j+1])])):
                    if int(numbers[j][c]) < int(numbers[j + 1][c]):
                        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                    elif numbers[j][:min([len(numbers[j]), len(numbers[j+1])])] == numbers[j+1][:min([len(numbers[j]), len(numbers[j+1])])]:
                        if len(numbers[j]) > len(numbers[j+1]) and int(numbers[j][0]) > int(numbers[j][len(numbers[j+1])]):
                            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                        elif len(numbers[j]) < len(numbers[j+1]) and int(numbers[j+1][0]) < int(numbers[j+1][len(numbers[j])]):
                            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                        elif len(numbers[j]) < len(numbers[j + 1]) and int(numbers[j + 1][len(numbers[j])-1]) == int(numbers[j][len(numbers[j])-1]):
                            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                        elif len(numbers[j]) > len(numbers[j + 1]) and int(numbers[j + 1][len(numbers[j])-1]) == int(numbers[j][len(numbers[j])-1]):
                            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(numbers)
    if len(numbers) != 0 and all(map(lambda p: p == '0', numbers)):
        return 0

    return ''.join(numbers) if numbers else -1


#print(get_biggest([7, 71, 72]))
#print(get_biggest([62, 626]))
#print(get_biggest([0, 0, 0, 0, 0, 0]))
#print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))