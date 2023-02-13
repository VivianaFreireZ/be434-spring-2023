#!/usr/bin/env python3
"""
Author : vfreirezapata <vfreirezapata@localhost>
Date   : 2023-02-12
Purpose: Dictionary
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Do Re Mi',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        nargs='+',
                        help='Solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    song = {'Do': 'A deer, a female deer',
            'Re': 'A drop of golden sun',
            'Mi': 'A name I call myself',
            'Fa': 'A long long way to run',
            'Sol': 'A needle pulling thread',
            'La': 'A note to follow sol',
            'Ti': 'A drink with jam and bread'}

    for text in args.str:
        if text in song:
            lyrics = ', '.join([text, song.get(text)])
        else:
            lyrics = f'I don\'t know "{text}"'

        print(lyrics)


# --------------------------------------------------
if __name__ == '__main__':
    main()
