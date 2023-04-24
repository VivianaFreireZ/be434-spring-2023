#!/usr/bin/env python3
"""
Author : vfreirezapata <vfreirezapata@localhost>
Date   : 2023-04-23
Purpose: Python grep
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Pythin grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        help='Search pattern',
                        metavar='PATTERN',
                        type=str,
                        default=None)

    parser.add_argument('files',
                        help='Input file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    flag_case = re.I if args.insensitive else 0

    for file in args.files:
        for line in file:
            match = re.search(args.pattern, line, flags=flag_case)
            if match:
                if len(args.files) > 1:
                    args.outfile.write(f'{file.name}:{line}')
                else:
                    args.outfile.write(line)


# --------------------------------------------------
if __name__ == '__main__':
    main()
