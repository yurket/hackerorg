#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from text_stat import print_stats

ct_list = [1, 'b', 4, 'a', 6, 1, 7, 8, 'a', 4, 'a', 5, 9, 7, 'c', 'd', 'e', 'a', 1, 7, 3, 4, 2, 'f', 9, 'b', 4, 1, 'c', 3, 4, 'g']
C = [1,2,3,4,5,6,7,8,9,10,11,12,13,14, 'a', 'b']


def main():
    ct = ''.join([str(x) for x in ct_list])
    print("ciphertext: %s" % ct)
    print_stats(ct)


if __name__ == '__main__':
    main()

