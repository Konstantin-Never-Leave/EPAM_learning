"""
Task 1.4
Write a Python program to sort a dictionary by key.

myDict = {1: "qwe", 2: "asd", 4: "zxc", 7: "rty", 3: "fgh", 9: "vbn"}
"""

external_input = {}


def dict_sort(x):
    """
    sorting received dict from users input
    :param x: dict from external input
    :return: sorted list
    """
    keys_list = list(x.keys())
    sorted_list = []
    keys_list.sort()

    for i in keys_list:
        sorted_list.append(i)
        sorted_list.append(x[i])

    keys = []
    values = []
    for i, j in enumerate(sorted_list):
        if i % 2 == 0:
            keys.append(j)
        else:
            values.append(j)

    sorted_dict = (dict(zip(keys, values)))

    return sorted_dict


def main(x):

    return dict_sort(x)

