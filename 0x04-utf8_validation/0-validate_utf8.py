#!/usr/bin/python3
"""
Module for validating UTF-8 character encoding.

Provides a function to check if a given list of integers represents
a valid UTF-8 encoding.
"""


def validUTF8(data):
    expect_continuation = 0
    for byte in data:
        if expect_continuation == 0:
            if byte < 0x80:  # 1-byte sequence (ASCII)
                continue
            elif byte & 0xE0 == 0xC0:  # 2-byte sequence starter
                expect_continuation = 1
            elif byte & 0xF0 == 0xE0:  # 3-byte sequence starter
                expect_continuation = 2
            elif byte & 0xF8 == 0xF0:  # 4-byte sequence starter
                expect_continuation = 3
            else:  # Invalid byte
                # (most significant bit set but doesn't match any pattern)
                return False
        else:
            if byte & 0xC0 != 0x80:  # Invalid continuation byte
                return False
            expect_continuation -= 1
    return expect_continuation == 0
