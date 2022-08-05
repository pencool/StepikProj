with open('file.txt') as f:
    rows, words, letters = 0, 0, 0
    for i in f:
        rows += 1
        words += len(i.strip().split())
        letters += len([*filter(str.isalpha, i)])
    print(f'Input file contains:\n{letters} letters\n{words} words\n{rows} lines')