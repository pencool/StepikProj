responders = [set(input().split(', ')) for i in range(int(input()))]
result = responders.pop()
for i in range(len(responders)):
    result = result.intersection(responders[i])
print(*sorted(result) if result else ['Сериал снять не удастся'], sep=', ')