with open('deniro.csv', encoding='utf-8') as f:
    string = int(input())-1
    data = f.read()
    table = [line for line in data.splitlines()]
    print(*sorted(table, key=lambda x: x.split(',')[string]) if
          string == 0 else sorted(
        table, key=lambda x: int(x.split(',')[string])), sep='\n')
