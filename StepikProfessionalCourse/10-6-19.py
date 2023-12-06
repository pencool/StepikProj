interleave = lambda *args: (j[i] for i in range(len(args[0])) for j in args)

numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]

print(*interleave(numbers, squares, qubes))