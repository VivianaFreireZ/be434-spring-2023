#!/usr/bin/env python3
"""
Author : vfreirezapata <vfreirezapata@localhost>
Date   : 2023-02-26
Purpose: Translate DNA/RNA sequences
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        required=True)

    parser.add_argument('-o',
                        '--output',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    codon_table = {}
    for line in args.codons:
        splitted = line.rstrip().split()
        codon_table[splitted[0]] = splitted[1]
    k = 3
    seq = args.sequence
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        codon = codon.upper()
        if codon not in codon_table:
            args.output.write('-')
        else:
            args.output.write(f'{codon_table[codon]}')
    print(f'Output written to "{args.output.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
