def get_biggest(numbers):
    numbers = [*map(str, numbers)]
    flag = True
    while flag:
        flag = False
        for i in range(len(numbers)-1):
            maxnum = max([numbers[i], numbers[i + 1]], key=len)
            minnum = min([numbers[i], numbers[i + 1]], key=len)
            if len(numbers[i]) != len(numbers[i+1]) and maxnum[:len(minnum)] == minnum:
                if maxnum[len(minnum)] < minnum[0]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    flag = True
                elif len(minnum) == 1:
                    for c in maxnum:
                        if c != minnum and c < minnum:
                            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                            flag = True
            elif numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                flag = True
    return numbers[::-1]

print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))
#print(get_biggest([7, 771, 72]))
#print(get_biggest([62, 626]))
#print(get_biggest([0, 0, 0, 0, 0, 0]))