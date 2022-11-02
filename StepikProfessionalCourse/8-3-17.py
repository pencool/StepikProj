def no_for(n=int(input()), m=5):
    if n <= 0:
        print(n)
    else:
        print(n)
        no_for(n - m, m)
        print(n)
no_for()