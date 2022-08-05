with open('code.txt') as f:
    x = f.read().split('\n')
    func = []
    if x[0].split()[0] == 'def':
        for j in range(len(x[0].split()[1])):
            if x[0].split()[1][j] == '(':
                func.append(x[0].split()[1][0:j])
    for i in range(len(x)):
        if x[i] != '' and x[i].split()[0] == 'def' and x[i-1] == '':
            buf = x[i].split(' ')[1]
            for j in range(len(buf)):
                if buf[j] == '(':
                    func.append(buf[0:j])
    if len(func) == 0:
        print('Best Programming Team')
    else:
        print(*func, sep='\n')