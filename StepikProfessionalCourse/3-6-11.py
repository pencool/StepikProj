import time


def get_the_fastest_func(funcs):
    min_time = 0
    answer = 0
    for i in funcs:
        start = time.monotonic()
        x = i(range(100000000))
        end = time.monotonic()
        print(end - start)
        if min_time > end - start or min_time == 0:
            min_time = end - start
            answer = i
    return answer


# def for_and_append():  # с использованием цикла for и метода append()
#     iterations = 10_000_000
#     result = []
#     for i in range(iterations):
#         result.append(i + 1)
#     return result
#
#
# def list_comprehension():  # с использованием списочного выражения
#     iterations = 10_000_000
#     return [i + 1 for i in range(iterations)]
def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)

funcs = [for_and_append, list_comprehension, list_function]

print(get_the_fastest_func(funcs))
