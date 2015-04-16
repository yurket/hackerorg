#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import itertools
import string


ct = [1, 'b', 4, 'a', 6, 1, 7, 8, 'a', 4, 'a', 5, 9, 7, 10, 11, 12, 'a', 1, 7, 3, 4, 2, 13, 9, 'b', 4, 1, 11, 3, 4, 14]
C = [1,2,3,4,5,6,7,8,9,10,11,12,13,14, 'a', 'b']


def hex_to_string(hex_seq):
    out_str = ''
    for i in range(0, len(hex_seq), 2):
        code = int(hex_seq[i:i+2], 16)
        # dont'include not-ascii charachters
        if code > 128:
            return None
        out_str += chr(code)
    return out_str


def main():
    hexes = '0123456789abcdef'
    counter = 0
    for key in itertools.permutations(hexes):
        dictionary = dict(zip(C, list(key)))
        msg = ''.join([dictionary[c] for c in ct])
        answer = hex_to_string(msg)
        if answer:
            print("key: %s, message: %s" % (key, msg))
            print(answer)
        if counter % 1000000:
            print('.')
            counter += 1


if __name__ == '__main__':
    main()

