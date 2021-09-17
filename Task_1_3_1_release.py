"""
Task 1.3
Create a program that asks the user for a number and then prints out a list of all the [divisors] of that number.
Examples:
```
Input: 60
Output: [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
```

"""

external_input = 60  # divider


def dividend_find(dividend, divisor=1, divisor_list=None):
    """
    :param dividend: Need to input only this parameter
    :param divisor:
    :param divisor_list:
    :return: sorted list of all divisors
    """

    if divisor_list is None:
        divisor_list = []
    n = divisor + 1

    while n > divisor:
        n = dividend / divisor

        if dividend % divisor == 0:
            divisor_list.append(divisor)
            divisor_list.append(dividend // divisor)

        divisor = divisor + 1

    return sorted(divisor_list)


def main(x):

    return dividend_find(x)



