massive = eval(input())
if isinstance(massive, list):
    print(massive[-1])
elif isinstance(massive, tuple):
    print(massive[0])
elif isinstance(massive, set):
    print(len(massive))

