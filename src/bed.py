"""Module for working with lines of BED data."""

from typing import (
    NamedTuple, TextIO
)

# You haven't seen this yet, but I am creating a type,
# BedLine, that we can create as
# >>> line = BedLine('chr21', 20_100, 20_101, 'foobar')
# and access both as a tuple, line[0], or by name, line.chrom.
BedLine = NamedTuple("BedLine", [
    ('chrom', str),
    ('chrom_start', int),
    ('chrom_end', int),
    ('name', str)
])


def parse_line(line: str) -> BedLine:
    """Parse a single line from a BED file (with four columns).

    >>> parse_line('chr1   20_100  20_101  foo')
    BedLine(chrom='chr1', chrom_start=20100, chrom_end=20101, name='foo')

    We assert that the interval the line specifies is a singleton nucleotide.
    We need this for some of the exercises, but you can remove the assert
    if you ever want to allow more general features.
    """
    chrom, start, end, name = line.split()  # split on any white-space
    bed_line = BedLine(chrom, int(start), int(end), name)
    assert bed_line.chrom_start + 1 == bed_line.chrom_end
    return bed_line


def print_line(line: BedLine, f: TextIO) -> None:
    """Prints line to the stream f as a BED line."""
    print(line.chrom, line.chrom_start,
          line.chrom_end, line.name, file=f, sep='\t')
