with open('grades.txt') as f:
    x = [[*map(int, i.split()[1:])] for i in f.readlines()]
    count = 0
    for i in x:
        if all(map(lambda x: x >= 65, i)):
            count += 1
    print(count)