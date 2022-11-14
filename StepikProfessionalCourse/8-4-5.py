def linear(nested_list):
    out = []

    def new_list(nested_list):
        for i in nested_list:
            if type(i) is not list:
                out.append(i)
            if type(i) is list:
                new_list(i)
        return out
    return new_list(nested_list)


my_list = [10, 20, 30, 40, 50]

print(linear(my_list))
