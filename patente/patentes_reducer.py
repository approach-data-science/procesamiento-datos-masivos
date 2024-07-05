#!/usr/bin/env python3

import sys
from collections import defaultdict

def reducer():
    cited_dict = defaultdict(list)

    for line in sys.stdin:
        cited, citing = line.strip().split('\t')
        cited_dict[cited].append(citing)

    for cited in sorted(cited_dict.keys(), key=int):
        citing_list = ','.join(sorted(cited_dict[cited], key=int))
        print(f"{cited}\t{citing_list}")

if __name__ == "__main__":
    reducer()
