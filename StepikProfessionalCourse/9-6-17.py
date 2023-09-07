def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    dct = {}
    x = 1
    for i in matrix:
        dct[x] = i
        x += 1
    return dct

matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict(matrix))