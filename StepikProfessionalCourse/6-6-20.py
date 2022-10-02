from collections import OrderedDict


def custom_sort(order_dict: OrderedDict, by_values: bool = False):
    for k, v in sorted(order_dict.items(), key=lambda x: x[int(by_values)]):
        order_dict.move_to_end(k)


data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)