"""
Task 1.1
Write a Python program to calculate the length of a string without using the `len` function.
"""

external_input = ""


def length_count(x):
    """
    length calculation without len method
    :param x:   investigated string
    :return:    length of investigated string
    """
    length = 0
    for _ in x:
        length += 1

    return length


def main(x):

    return length_count(x)


