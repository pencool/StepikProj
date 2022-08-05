with open('ledger.txt') as f:
    print("$" + str(sum(map(lambda x: int(x.replace("$", "")), f.readlines()))))