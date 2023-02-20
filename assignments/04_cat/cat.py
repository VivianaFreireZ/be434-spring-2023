#!/usr/bin/env python3
"""
Author : vfreirezapata <vfreirezapata@localhost>
Date   : 2023-02-19
Purpose: Python CAT
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('f',
                        help='A readable file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for file in args.f:
        count_lines = 1
        for line in file:
            if args.number:
                format_line = f'     {count_lines}\t{line.rstrip()}'
                print(format_line)
                count_lines += 1

            else:
                print(line.rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
