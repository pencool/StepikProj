from collections import deque


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    deq = deque(numbers)
    shift = step % len(numbers)
    if shift != 0:
        deq.rotate(shift)
    numbers[:] = list(deq)


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)

print(numbers)
