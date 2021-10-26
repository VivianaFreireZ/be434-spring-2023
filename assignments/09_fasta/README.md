# FASTA Interleaved Paired Read Splitter

Some sequencing platforms such as Illumina may generate forward/reverse read pairs that sequence the target region from either end. 
Sometimes these reads overlap and can be joined into a single read, but sometimes they have a gap and cannot be joined.
The resulting read pairs are often placed into two files with an extension like `_1` or `_R1` for the forward reads and `_2` or `_R2` for the reverse, but sometimes the reads are interleaved in one file with the forward read immediately followed by the reverse read.

In this exercise, you will write a Python program called `au_pair.py` that accepts a list of positional arguments that are FASTA sequence files in _interleaved format_ and splits them into `_1`/`_2` files in a `-o|--outdir` argument (default `split`).
You should use the original extension of the file, e.g., `inputs/reads1.fa` should be split into `outdir/reads1_1.fa` and `outdir/reads1_2.fa` while `inputs/reads2.fasta` should be split into `outdir/reads2_1.fasta` and `outdir/reads2_2.fasta`.

The [https://en.wikipedia.org/wiki/FASTA_format](FASTA format) spans multiple lines per sequence record.
A record starts with the `>` as the first character on a line, and this is followed by a record identifier up to the first space character.
Any other information on the header line is consider the description.
Following this is one or more lines of sequences, e.g.:

```
$ head inputs/reads1.fa
>M10991:61:000000000-A7EML:1:1101:14011:1001 1:N:0:28
NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA
>M10991:61:000000000-A7EML:1:1101:14011:1001 2:N:0:28
NGCTCCTAGGTCGGCATGACGCTAGCTACGATCGACTACGCTAGCATCGAGAGTAGCAA
>M10991:61:000000000-A7EML:1:1201:15411:3101 1:N:0:28
NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA
>M10991:61:000000000-A7EML:1:1201:15411:3101 2:N:0:28
CGCTAGCTACGACTCGACGACAGCGAACACGCGATCGATCGGAAATGAGAGAGTAGCAA
```

You will use [https://biopython.org/](Biopython) to parse the FASTA files into records containing fields like `rec.id` and `rec.seq`.
Be sure to run `python3 -m pip install biopython`, then you can type the following code into a REPL to view the contents of the preceding file.
Note that the `rec.seq` is itself a `Bio.Seq` objects, so I call `str(rec.seq)` to coerce this to a `str`:

```
>>> from Bio import SeqIO
>>> reader = SeqIO.parse('inputs/reads1.fa', 'fasta')
>>> for rec in reader:
...     print('ID :', rec.id)
...     print('Seq:', str(rec.seq))
...
ID : M10991:61:000000000-A7EML:1:1101:14011:1001
Seq: NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA
ID : M10991:61:000000000-A7EML:1:1101:14011:1001
Seq: NGCTCCTAGGTCGGCATGACGCTAGCTACGATCGACTACGCTAGCATCGAGAGTAGCAA
ID : M10991:61:000000000-A7EML:1:1201:15411:3101
Seq: NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA
ID : M10991:61:000000000-A7EML:1:1201:15411:3101
Seq: CGCTAGCTACGACTCGACGACAGCGAACACGCGATCGATCGGAAATGAGAGAGTAGCAA
```

The program should accept one or more required positional arguments that are readable files and an optional `-o|--outdir` output directory name that defaults to `out`.
When run with no arguments, the program should print a brief usage:

```
$ ./au_pair.py
usage: au_pair.py [-h] [-o DIR] FILE [FILE ...]
au_pair.py: error: the following arguments are required: FILE
```

It should print a longer usage statements on `-h|--help`:

```
$ ./au_pair.py -h
usage: au_pair.py [-h] [-o DIR] FILE [FILE ...]

Split interleaved/paired reads

positional arguments:
  FILE                  Input file(s)

optional arguments:
  -h, --help            show this help message and exit
  -o DIR, --outdir DIR  Output directory (default: split)
```

If one of the positional arguments is not a valid file, the program should print a usage and an appropriate error message:

```
$ ./au_pair.py blargh
usage: au_pair.py [-h] [-o DIR] FILE [FILE ...]
au_pair.py: error: argument FILE: can't open 'blargh': 
[Errno 2] No such file or directory: 'blargh'
```

If the `--outdir` does not exist, create it.
When run with valid input files, the program should write the odd-numbered (1st, 3rd, 5th, ...) sequences of each file into `<outdir>/<basename>_1.<extension>` and the even-numbered into the `_2` file.
While processing, the program should print the number and basename of each input file, which you can get using `os.path.basename`:

```
$ ./au_pair.py inputs/reads1.fa
  1: reads1.fa
Done, see output in "split"
```

The output directory should contain two files for each input file:

```
$ ls split/
reads1_1.fa  reads1_2.fa
```

Since there were a total of 4 input sequences (each taking 2 lines), each output file should contain 4 lines:

```
$ wc -l split/*
  4 split/reads1_1.fa
  4 split/reads1_2.fa
  8 total
```

The `_1` file should contain the odd-numbered sequences:

```
$ head split/reads1_1.fa
>M10991:61:000000000-A7EML:1:1101:14011:1001 1:N:0:28
NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA
>M10991:61:000000000-A7EML:1:1201:15411:3101 1:N:0:28
NGCTCCTAGGTCGGCATGATGGGGGAAGGAGAGCATGGGAAGAAATGAGAGAGTAGCAA
```

And the `_2` file should contain the complementary sequences:

```
$ head split/reads1_2.fa
>M10991:61:000000000-A7EML:1:1101:14011:1001 2:N:0:28
NGCTCCTAGGTCGGCATGACGCTAGCTACGATCGACTACGCTAGCATCGAGAGTAGCAA
>M10991:61:000000000-A7EML:1:1201:15411:3101 2:N:0:28
CGCTAGCTACGACTCGACGACAGCGAACACGCGATCGATCGGAAATGAGAGAGTAGCAA
```

For the purposes of this exercise, assume the reads are properly interleaved such that the first read is forward and the second read is its reverse mate. Do not worry about testing the read IDs for forward/reverse or mate pair information. Also assume all input files are in FASTA format and should be written in FASTA format.

```
$ ./au_pair.py
usage: au_pair.py [-h] [-o DIR] FILE [FILE ...]
au_pair.py: error: the following arguments are required: FILE
$ ./au_pair.py -h
usage: au_pair.py [-h] [-o DIR] FILE [FILE ...]

Split interleaved/paired reads

positional arguments:
  FILE                  Input file(s)

optional arguments:
  -h, --help            show this help message and exit
  -o DIR, --outdir DIR  Output directory (default: split)
$ ./au_pair.py foo
"foo" is not a file
$ ./au_pair.py inputs/reads1.fa
  1: reads1.fa
	Split 4 sequences to dir "split"
$ ./au_pair.py inputs/reads2.fasta -o out
  1: reads2.fasta
	Split 500 sequences to dir "out"
$ ./au_pair.py inputs/* -o all
  1: reads1.fa
	Split 4 sequences to dir "all"
  2: reads2.fasta
	Split 500 sequences to dir "all"
```