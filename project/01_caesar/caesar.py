#!/usr/bin/env python3
"""
Author : vfreirezapata <vfreirezapata@localhost>
Date   : 2023-05-03
Purpose: Caesar
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Caesar',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-n',
                        '--number',
                        help='A number to shift',
                        metavar='NUMBER',
                        type=int,
                        default=3)

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true',
                        default=False)

    parser.add_argument('-o',
                        '--outfile',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # creating a dictionary according to n
    text_dict = {}
    for i, _ in enumerate(alpha):
        if i+args.number < len(alpha):
            new_letter = alpha[i+args.number]
        else:
            new_letter = alpha[i+args.number-len(alpha)]
        text_dict[alpha[i]] = new_letter

    if args.decode:
        for line in args.file:
            key_list = list(text_dict.keys())
            val_list = list(text_dict.values())
            decoded = []
            for char in line:
                if char in alpha:
                    position = val_list.index(char)
                    new_letter = key_list[position]
                else:
                    new_letter = char
                decoded.append(new_letter)

            trans = ''.join(decoded)
            args.outfile.write(trans)
    else:
        for line in args.file:
            line = line.upper()
            trans = ''.join([text_dict.get(char, char) for char in line])
            args.outfile.write(trans)


# --------------------------------------------------
if __name__ == '__main__':
    main()
