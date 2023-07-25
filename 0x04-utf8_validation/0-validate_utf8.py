#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """method that determines if a given
    data set represents a valid UTF-8 encoding"""
    def is_continuation(byte):
        return byte & 0b11000000 == 0b10000000

    def num_following_bytes(byte):
        if byte & 0b11100000 == 0b11000000:
            return 1
        elif byte & 0b11110000 == 0b11100000:
            return 2
        elif byte & 0b11111000 == 0b11110000:
            return 3
        else:
            return 0

    num_bytes_to_follow = 0

    for byte in data:
        if num_bytes_to_follow == 0:
            if byte & 0b10000000 == 0:  # 1-byte character
                continue
            num_bytes_to_follow = num_following_bytes(byte)
            if num_bytes_to_follow == 0:  # Invalid start byte
                return False
        else:
            if not is_continuation(byte):  # Invalid continuation byte
                return False
            num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0  # All bytes have been validated
