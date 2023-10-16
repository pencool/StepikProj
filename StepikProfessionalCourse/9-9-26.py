from functools import lru_cache
import sys


@lru_cache()
def word_sort():
    words = []
    for i in sys.stdin:
        words.append(''.join(sorted(i.strip())))
    return words


print(*word_sort(), sep='\n')
