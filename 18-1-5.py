with open('strings.txt') as f:
    answer = []
    for i in f:
        answer.append(i.strip())
        if len(answer) > 10:
            del answer[0]
    print(*answer, sep='\n')