#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse
import os
import string


from collections import Counter

def print_stats(data):
    if not data:
        print('Empty data')
        return None

    data_len = len(data)
    ctr = Counter(data)

    SEP = '-'*100

    print('\n\t\t\tSTATISTICS:')
    print(SEP)
    print()
    keys = sorted(ctr.keys())
    printable_keys = (' '.join(keys)).replace('\n', '\\n')
    print('Whole alphabet is: %s' % printable_keys)
    print('Lengh: %d' % len(keys))
    print(SEP)

    without_whitespaces = [k for k in keys if k not in string.whitespace]
    print('Without whitespaces: %s' % ' '.join(without_whitespaces))
    print('Lengh: %d' % len(without_whitespaces))
    print(SEP)

    without_punct = [k for k in without_whitespaces if k not in string.punctuation]
    print('Without punctuation: %s' % ' '.join(without_punct))
    print('Lengh: %d' % len(without_punct))
    print(SEP)

    # print percents
    print('\t\tLETTERS DISTRIBUTION: \n')
    for char, count in ctr.most_common():
        percent = (float(count)/data_len)*100
        percent = str(round(percent, 3)) + '%'

        if char == '\n':
            char = '\\n'
        print("%s: %s (%d times)" %(char, percent, count))
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    filename = args.filename
    if not os.path.exists(filename):
        print('[-] Error: File %s does not exists!' % filename)
        return

    data = None
    try:
        with open(filename, 'rb') as f:
            data = f.read()
    except IOError as e:
        print(e.message)
        return

    print_stats(data)


if __name__ == '__main__':
    main()

