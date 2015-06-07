#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


# decompile maeda.swf (for example here: http://www.showmycode.com) and find answer generation code:
def answer_generator():
    xx = 18
    aa = 17
    xx = xx * (29 * aa)
    xx = xx + (5423 + aa)
    xx = xx * 11
    xx = xx - (77 * aa)
    return xx

def main():
    print(answer_generator())



if __name__ == '__main__':
    main()

