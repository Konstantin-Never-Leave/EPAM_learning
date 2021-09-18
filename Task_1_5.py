"""
Task 1.5
Write a Python program to print all unique values of all dictionaries in a list.
Examples:

Input:[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},{"V": "S009"}, {"VIII": "S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

external_input = []
internal_input = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
                  {"V": "S009"}, {"VIII": "S007"}]


def take_unique_value(x):
    """
    sorting received list of dictionaries from users input
    :param x: users input
    :return: list of unique values
    """
    values_list = []

    for i in x:
        values_list.extend(i.values())

    return set(values_list)


def main(x):

    return take_unique_value(x)


if __name__ == "__main__":
    print(main(internal_input))
