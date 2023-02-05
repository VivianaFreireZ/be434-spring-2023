#!/usr/bin/env python3
"""
Author : vfreirezapata <vfreirezapata@localhost>
Date   : 2023-02-05
Purpose: Add numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('number',
                        metavar='INT',
                        type=int,
                        nargs='+',
                        help='Numbers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if len(args.number) == 1:
        print(f"{args.number[0]} = {args.number[0]}")
    else:
        str_numbers = [str(i) for i in args.number]
        num_joined = ' + '.join(str_numbers)
        sum_numbers = sum(args.number)
        print(f'{num_joined} = {sum_numbers}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
