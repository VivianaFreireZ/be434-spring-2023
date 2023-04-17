#!/usr/bin/env python3
"""
Author : vfreirezapata <vfreirezapata@localhost>
Date   : 2023-04-16
Purpose: Run-length enconding DNA
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type=str,
                        help='DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, encoding='utf-8') as fh:
            args.text = fh.read()

    return args


# --------------------------------------------------
def rle(seq):
    """Make a jazz noise here"""

    output = ''
    i = 0

    while i <= len(seq) - 1:
        rep = 1
        new_letter = seq[i]
        output = output + new_letter
        j = i
        while j < len(seq) - 1:
            if re.match(new_letter, seq[j+1]):
                rep += 1
                j += 1
            else:
                break
        output = output + str(rep)
        i = j + 1

    output = re.sub('1', '', output)

    return output


# --------------------------------------------------
def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for seq in args.text.splitlines():
        print(rle(seq))


# --------------------------------------------------
if __name__ == '__main__':
    main()
