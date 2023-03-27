#!/usr/bin/env python3
"""
Author : vfreirezapata <vfreirezapata@localhost>
Date   : 2023-03-26
Purpose: Finding common K-mers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Finding common K-mers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    parser.add_argument('file1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        default=None)

    args = parser.parse_args()

    if args.kmer <= 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def find_kmers(seq, k):
    """ Find k-mers in string """
    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    words1 = {}
    for line in args.file1:
        for word in line.split():
            for kmer in find_kmers(word, args.kmer):
                if kmer in words1:
                    words1[kmer] += 1
                else:
                    words1[kmer] = 1

    words2 = {}
    for line in args.file2:
        for word in line.split():
            for kmer in find_kmers(word, args.kmer):
                if kmer in words2:
                    words2[kmer] += 1
                else:
                    words2[kmer] = 1

    for kmer in set(words1).intersection(set(words2)):
        print(f'{kmer:<10}{words1.get(kmer):>6}{words2.get(kmer):>6}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
