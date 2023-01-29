#!/usr/bin/env python3
"""
Author : vfreirezapata <vfreirezapata@localhost>
Date   : 2023-01-28
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        metavar='str',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet',
                        metavar='str',
                        type=str,
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sign = '!' if args.excited else '.'
    print(f'{args.greeting}, {args.name}{sign}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
