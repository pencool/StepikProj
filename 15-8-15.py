from functools import reduce


def evaluate(coefficients=[*map(int, input().split())], num=input()):
    stepen = [*sorted(range(len(coefficients)), reverse=True)]
    nums = [int(num)]*len(coefficients)
    coefstep = tuple(zip(coefficients, stepen, nums))
    print(reduce(lambda y, x: x[2]**x[1]*x[0] + y, coefstep, 0))
    #print(coefstep)


evaluate()