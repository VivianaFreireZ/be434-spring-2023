#!/usr/bin/env python3
"""
Author : vfreirezapata <vfreirezapata@localhost>
Date   : 2023-04-02
Purpose: CSV filter
"""

import argparse
import csv
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='CSV file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True,
                        default=None)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        required=True,
                        default=None)

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    args = parser.parse_args()

    if args.delimiter == '$\t':
        reader = csv.DictReader(args.file, delimiter='\t')
    else:
        reader = csv.DictReader(args.file, delimiter=args.delimiter)

    if args.col != '':
        if args.col not in reader.fieldnames:
            parser.error(f'--col "{args.col}" not a valid column!')

    return args, reader


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args, reader = get_args()

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    n_row = 0

    for row in reader:
        if args.col != '':
            search_text = row[args.col]
        else:
            search_text = ' '.join(list(row.values()))
        if re.search(args.val, search_text, re.IGNORECASE):
            writer.writerow(row)
            n_row += 1

    print(f'Done, wrote {n_row} to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
