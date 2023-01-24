#print_operation_table = lambda x, y, z: [[x(j, i) for i in range(1, z+1)] for j in range(1, y+1)]

def print_operation_table(x, y, z):
    table = [[x(j, i) for i in range(1, z+1)] for j in range(1, y+1)]
    for i in table:
        print(*i)


print_operation_table(pow, 5, 4)
