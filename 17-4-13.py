files = [input() for i in range(int(input()))]
for i in files:
    with open('output.txt', 'a') as out, open(i) as f:
        print(f.read(), file=out)