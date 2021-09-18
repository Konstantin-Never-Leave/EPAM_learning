import Task_1_1
import Task_1_2
import Task_1_3
import Task_1_3_1
import Task_1_4
import Task_1_5
import Task_1_6
import Task_1_6_1

# Task 1.1
# Write a Python program to calculate the length of a string without using the `len` function.
checking_value_1_1 = "Oh, it is python"
expected_output_1_1 = len("Oh, it is python")

# Task 1.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
checking_value_1_2 = "Oh, it is python"
expected_output_1_2 = {'o': 2, 'h': 2, ',': 1, ' ': 3, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}

# Task 1.3
# Write a Python program that accepts a comma separated sequence of words as input
# and prints the unique words in sorted form.
checking_value_1_3 = "red, pink, blue, green, red, red, blue, red, pink, red, blue, red, pink, blue, green"
expected_output_1_3 = ["blue", "green", "pink", "red"]

# Task 1.3.1
# Create a program that asks the user for a number and then prints out a list of all the [divisors] of that number.
checking_value_1_3_1 = 120
expected_output_1_3_1 = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]

# Task 1.4
# Write a Python program to sort a dictionary by key.
checking_value_1_4 = {1: "qwe", 2: "asd", 4: "zxc", 7: "rty", 3: "fgh", 9: "vbn"}
expected_output_1_4 = {1: 'qwe', 2: 'asd', 3: 'fgh', 4: 'zxc', 7: 'rty', 9: 'vbn'}

# Task 1.5
# Write a Python program to print all unique values of all dictionaries in a list.
checking_value_1_5 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                      {"VIII": "S007"}]
expected_output_1_5 = {'S001', 'S007', 'S002', 'S005', 'S009'}

# Task 1.6
# Write a Python program to convert a given tuple of positive integers into an integer.
checking_value_1_6 = (1, 2, 3, 4)
expected_output_1_6 = 1234

# Task 1.6.1 Write a program which makes a pretty print of a part of the multiplication table.
checking_value_1_6_1 = "Oh, it is python"
expected_output_1_6_1 = {}

# Messages:
msg_passed = "test passed "
msg_failed = "test failed "

if __name__ == "__main__":
    def check_1st_task(check_value, expect_output):
        """
        :param check_value: Our input
        :param expect_output: Output which we are expecting
        :return: passed or not passed msg
        """

        if (Task_1_1.main(check_value)) == expect_output:
            return "\033[42m {}\033[0m".format(msg_passed)

        else:
            return "\033[41m {}\033[0m".format(msg_failed)


    print("{:<12}".format("Task_1_1 "), check_1st_task(checking_value_1_1, expected_output_1_1))


    def check_2nd_task(check_value, expect_output):
        """
        :param check_value: Our input
        :param expect_output: Output which we are expecting
        :return: passed or not passed msg
        """

        if (Task_1_2.main(check_value)) == expect_output:
            return "\033[42m {}\033[0m".format(msg_passed)

        else:
            return "\033[41m {}\033[0m".format(msg_failed)

    print("{:<12}".format("Task_1_2 "), check_2nd_task(checking_value_1_2, expected_output_1_2))


    def check_3d_task(check_value, expect_output):
        """
        :param check_value: Our input
        :param expect_output: Output which we are expecting
        :return: passed or not passed msg
        """
        if (Task_1_3.main(check_value)) == expect_output:
            return "\033[42m {}\033[0m".format(msg_passed)

        else:
            return "\033[41m {}\033[0m".format(msg_failed)


    print("{:<12}".format("Task_1_3 "), check_3d_task(checking_value_1_3, expected_output_1_3))


    def check_3_1th_task(check_value, expect_output):
        """
        :param check_value: Our input
        :param expect_output: Output which we are expecting
        :return: passed or not passed msg
        """

        if (Task_1_3_1.main(check_value)) == expect_output:
            return "\033[42m {}\033[0m".format(msg_passed)

        else:
            return "\033[41m {}\033[0m".format(msg_failed)


    print("{:<12}".format("Task_1_3_1 "), check_3_1th_task(checking_value_1_3_1, expected_output_1_3_1))


    def check_4th_task(check_value, expect_output):
        """
        :param check_value: Our input
        :param expect_output: Output which we are expecting
        :return: passed or not passed msg
        """

        if (Task_1_4.main(check_value)) == expect_output:
            return "\033[42m {}\033[0m".format(msg_passed)

        else:
            return "\033[41m {}\033[0m".format(msg_failed)


    print("{:<12}".format("Task_1_4 "), check_4th_task(checking_value_1_4, expected_output_1_4))


    def check_5th_task(check_value, expect_output):
        """
        :param check_value: Our input
        :param expect_output: Output which we are expecting
        :return: passed or not passed msg
        """

        if (Task_1_5.main(check_value)) == expect_output:
            return "\033[42m {}\033[0m".format(msg_passed)

        else:
            return "\033[41m {}\033[0m".format(msg_failed)


    print("{:<12}".format("Task_1_5 "), check_5th_task(checking_value_1_5, expected_output_1_5))


    def check_6th_task(check_value, expect_output):
        """
        :param check_value: Our input
        :param expect_output: Output which we are expecting
        :return: passed or not passed msg
        """

        if (Task_1_6.main(check_value)) == expect_output:
            return "\033[42m {}\033[0m".format(msg_passed)

        else:
            return "\033[41m {}\033[0m".format(msg_failed)


    print("{:<12}".format("Task_1_6 "), check_6th_task(checking_value_1_6, expected_output_1_6))


    def check_6_1th_task(a, b, c, d):
        """
        :param a: first row
        :param b: last row
        :param c: first column
        :param d: last column
        :return: Prints a peace of a multiplication table
        """

        return Task_1_6_1.main(a, b, c, d)

    print("\nTask_1_6_1 result: ")
    print(check_6_1th_task(2, 4, 3, 7))
