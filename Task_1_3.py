"""
 Task 1.3
 Write a Python program that accepts a comma separated sequence of words as input
 and prints the unique words in sorted form.
 "red, pink, blue, green, red, red, blue, red, pink, blue, red, blue, red, pink, blue, green, red, red, blue"
"""

external_input = ""
internal_input = "lion, bear, tyrannosaur, dolphin, chicken, tyrannosaur, lion, chicken, bear, lion"


def unique_selecting(x):
    """
    length calculation without len method
    :param x:   investigated tuple
    :return:    list of unique values from input
    """
    if x[-1].isalpha() or x[-1].isdigit():
        x += ","

    x = x.replace(",", "")
    # converting string to set for take only unique values from sequence:
    unique = (set(x.split()))

    # sorting converted set to list:
    unique = sorted(list(unique))
    (" ".join(unique))

    return unique


def main(x):

    return unique_selecting(x)


if __name__ == "__main__":
    print(main(internal_input))
