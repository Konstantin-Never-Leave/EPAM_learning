"""
Task 1.2
Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
"""

external_input = ""
internal_input = "python is choking me"


def char_freq_count(x):
    """
    length calculation without len method
    :param x:   investigated string
    :return:    length of investigated string
    """
    length = {}
    for i in x:
        if i in length:
            length[i.lower()] += 1
        else:
            length[i.lower()] = 1

    return length


def main(x):

    return char_freq_count(x)


if __name__ == "__main__":
    print(main(internal_input))
