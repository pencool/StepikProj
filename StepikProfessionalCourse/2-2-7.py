word = [*enumerate(input())]
words = [input() for i in range(int(input()))]
indexes = [[] for i in range(len(words))]
chars = 'ауоыиэяюёе'
wordindex = [i[0] for i in word if i[1] in chars]
for i in range(len(words)):
    for j in range(len(words[i])):
        if words[i][j] in chars:
            indexes[i].append(j)
for i in range(len(indexes)):
    if indexes[i] == wordindex:
        print(words[i])