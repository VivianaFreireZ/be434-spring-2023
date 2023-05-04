#!/usr/bin/env python3
"""
Author : vfreirezapata <vfreirezapata@localhost>
Date   : 2023-05-03
Purpose: Vigenere
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='vigenere cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-k',
                        '--keyword',
                        help='A key word',
                        metavar='KEYWORD',
                        type=str,
                        default='CIPHER')

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true',
                        default=False)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    args = get_args()
    for line in args.file:
        line = line.upper()
        key_len = len(args.keyword)
        ciph_idx = 0
        encoded = []

        for i, _ in enumerate(line):
            letter = line[i]
            if letter in alpha:
                cipher_letter = args.keyword[ciph_idx]
                ciph_idx = 0 if ciph_idx + 1 == key_len else ciph_idx + 1
                index1 = alpha.index(letter)
                index2 = alpha.index(cipher_letter)
                if args.decode:
                    new_index = index1 - index2
                else:
                    new_index = (index1 + index2) % 26
                new_letter = alpha[new_index]
            else:
                new_letter = letter

            encoded.append(new_letter)
        trans = ''.join(encoded)
        args.outfile.write(trans)


# --------------------------------------------------
if __name__ == '__main__':
    main()
