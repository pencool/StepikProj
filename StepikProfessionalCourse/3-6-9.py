import time


def calculate_it(func, *args):
    start = time.perf_counter()
    return (func(args), time.perf_counter() - start)
