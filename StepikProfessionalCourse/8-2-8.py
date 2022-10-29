def reversed_list():
    n = int(input())
    if n != 0:
        reversed_list()
        print(n)
    else:
        print(n)


reversed_list()
