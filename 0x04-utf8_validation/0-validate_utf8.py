#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else
return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you
only need to handle the 8 least significant bits of each
integer
"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # For each integer in the data array
    for num in data:
        # Get the binary representation. We only need the least significant 8 bits
        # for any given number, so we discard the rest.
        bin_rep = format(num, '#010b')[-8:]

        # If this is the case then we are to start to parse a new UTF-8 character.
        if n_bytes == 0:
            # Get the number of 1s in the beginning of the string.
            for bit in bin_rep:
                if bit == '0': break
                n_bytes += 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios according to the rules of the problem.
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Else, we are to account for the number of bytes that indicate the
            # current UTF-8 character.
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        # We reduce the number of bytes to process by 1 after each integer.
        n_bytes -= 1

    # This is for the case where we might not have the complete data for
    # a particular UTF-8 character.
    return n_bytes == 0

