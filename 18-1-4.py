with open('words.txt') as f:
    words = f.read().split(' ')
    print(*filter(lambda x: len(x) == len(max(words, key=len)), words), sep='\n')