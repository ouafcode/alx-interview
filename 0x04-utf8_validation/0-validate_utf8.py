#!/usr/bin/python3
"""
utf8 module
"""


def validUTF8(data) -> bool:
    """valid UTF-8 encoding"""

    def byte_sequence_count(byte):
        """Return nbr byte in UTF-8 sequence"""
        leading_ones = 0
        while (byte >> 7 - leading_ones) & 1:
            leading_ones += 1
        return leading_ones

    i = 0

    while i < len(data):
        sequence_count = byte_sequence_count(data[i])

        if sequence_count == 0:
            i += 1
            continue

        if sequence_count == 1 or sequence_count > 4:
            return False

        if i + sequence_count > len(data):
            return False

        for j in range(1, sequence_count):
            if not (data[i + j] >> 6 == 0b10):
                return False

        i += sequence_count

    return True
