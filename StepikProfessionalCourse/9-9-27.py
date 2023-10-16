from functools import lru_cache


@lru_cache()
def ways(n: int) -> int:
    if n == 1:
        return 1
    elif n < 1:
        return 0
    return ways(n - 1) + ways(n - 3) + ways(n - 4)


print(ways(5))
