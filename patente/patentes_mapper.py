#!/usr/bin/env python3

import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin)
    next(reader)
    for citing, cited in reader:
        print(f"{cited}\t{citing}")


if __name__ == "__main__":
    mapper()
