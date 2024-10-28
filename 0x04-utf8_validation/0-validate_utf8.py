#!/usr/bin/python3
"""
Module for validating UTF-8 character encoding.

Provides a function to check if a given list of integers represents
a valid UTF-8 encoding.
"""

# UTF-8 byte patterns
# b is short for bytes
# c is short for continue
patterns = {
    '1byte': 0x7F,
    '2b_starter': 0xC2,
    '2b_c': 0x80,
    '3b_starter': 0xE0,
    '3b_c': 0x80,
    '4b_starter': 0xF0,
    '4b_c': 0x80
}


def validUTF8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding.

    Args:
        data (list[int]): List of integers, each representing a byte.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    i = 0
    while i < len(data):
        # Check for 2-byte sequence
        if (data[i] & patterns['2b_starter']) == patterns['2b_starter']:
            # If we are not still inside the array or the pattern doesn't match
            # return false
            if (i + 1 >= len(data) or
                    (data[i + 1] & patterns['2b_c']) != patterns['2b_c']):
                return False
            i += 2

        # Check for 3-byte sequence
        elif (data[i] & patterns['3b_starter']) == patterns['3b_starter']:
            if (i + 2 >= len(data) or
                (data[i + 1] & patterns['3b_c']) != patterns['3b_c'] or
                    (data[i + 2] & patterns['3b_c']) != patterns['3b_c']):
                return False
            i += 3

        # Check for 4-byte sequence
        elif (data[i] & patterns['4b_starter']) == patterns['4b_starter']:
            if (i + 3 >= len(data) or
                (data[i + 1] & patterns['4b_c']) != patterns['4b_c'] or
                (data[i + 2] & patterns['4b_c']) != patterns['4b_c'] or
                    (data[i + 3] & patterns['4b_c']) != patterns['4b_c']):
                return False
            i += 4

        # Check for 1-byte sequence
        elif (data[i] & patterns['1byte']) == data[i]:
            i += 1

        # If none of the above, it's an invalid UTF-8 encoding
        else:
            return False

    return True
