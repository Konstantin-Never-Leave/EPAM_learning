"""
Write a program which makes a pretty print of a part of the multiplication table.
"""

a = 2
b = 4
c = 3
d = 7
indent = "\t"
new_line = "\n"


def print_pretty_table(x, y, z, t):
    """
    :param x: 1st row value
    :param y: last row value
    :param z: 1st column value
    :param t: last column value
    :return:  a pretty print of a part of the multiplication table
    """

    print(end=indent)
    for i in range(z, t + 1):
        print(i, end=indent)
    print(end=new_line)
    for j in range(x, y + 1):
        print(j, end=indent)
        for k in range(z, t + 1):
            print(j * k, end=indent)

        print(end=new_line)

    return new_line


def main(*args):

    return print_pretty_table(*args)


if __name__ == "__main__":
    print(main(2, 4, 3, 7))
