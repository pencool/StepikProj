def sand_clock(l, n, x=5):
    if n < l:
        print((str(n) * x*l).center(l*l))
        sand_clock(l, n + 1, x-1)
    print((str(n) * x*l).center(l*l))


sand_clock(5, 1)
