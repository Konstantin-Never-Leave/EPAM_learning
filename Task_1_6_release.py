"""
Task 1.6
Write a Python program to convert a given tuple of positive integers into an integer.
Examples:

Input: (1, 2, 3, 4)
1, 2,6   ,4 , 5, 9 ,8
Output: 1234
"""

external_input = (1, 2,6   ,4 , 5, 9 ,8)


def concatenate(x):

    if x:

        x = int("".join(map(str, x)))
        return x

    else:
        x = "input is empty"
        return x


def main(x):

    return concatenate(x)
