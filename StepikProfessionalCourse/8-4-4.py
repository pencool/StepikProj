def recursive_sum(nested_lists: list, x=0):
    for i in nested_lists:
        if type(i) is int:
            x += i
        if type(i) is list:
            x += recursive_sum(i)
    return x

my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))