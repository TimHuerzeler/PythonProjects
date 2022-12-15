# to be able to specify type annotations and static type checker mypy
from typing import List


def int_to_bin_mod8(num: int) -> List[bool]:
    """
    Converts an integer into binary over 3 bits (modulo 8).
    Each bit is represented by a boolean. It is more logical to represent
    the bits with true/false values rather than with 0/1 integer value.
    For the sake of simplicity every constant is converted explicitly
    :param num: the integer to convert into binary
    :return: the list of booleans, each boolean represents a bit (Most Significant Bit on the left)
    """

    # dictionary used for switch-case
    int_bin_converter = {
        0: [False, False, False],    # 000
        1: [False, False, True],     # 001
        2: [False, True, False],     # 010
        3: [False, True, True],
        4: [True, False, False],
        5: [True, False, True],
        6: [True, True, False],      # 110
        7: [True, True, True]        # 111
    }
    dic_length = len(int_bin_converter)
    num = num % dic_length
    return int_bin_converter[num]


def int_to_bin_mod8_match(num: int) -> List[bool]:
    """
    Same behavior as int_to_bin_mod8 but make use of match case statement instead of a dictionary
    :param num: the integer to convert into binary
    :return: the list of booleans, each boolean represents a bit (Most Significant Bit on the left)
    """
    num = num % 8
    res = []
    match num:
        case 0:
            res = [False, False, False]     # 000
        case 1:
            res = [False, False, True]      # 001
        case 2:
            res = [False, True, False]      # 010
        case 3:
            res = [False, True, True]
        case 4:
            res = [True, False, False]
        case 5:
            res = [True, False, True]
        case 6:
            res = [True, True, False]      # 110
        case 7:
            res = [True, True, True]       # 111
    return res


def main():
    """ Launcher """
    print(int_to_bin_mod8(6))
    print(int_to_bin_mod8(9))

    print(int_to_bin_mod8_match(6))
    print(int_to_bin_mod8_match(9))


if __name__ == "__main__":
    main()
