#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function



def main():
    data = ''
    with open("original", 'rb') as f:
        data = f.read().split('.')
    
    with open("newlined", 'wb') as f:
        for l in data:
            f.write(l+'.\n')
            

if __name__ == '__main__':
    main()

