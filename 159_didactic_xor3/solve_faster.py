#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

CT = '31cf55aa0c91fb6fcb33f34793fe00c72ebc4c88fd57dc6ba71e71b759d83588'

nums = [ int(CT[i:i+2], 16) for i in xrange(0, len(CT), 2) ]

x, b = 0, 0
b_start = 0

count = 0 
while x < 256:
    while b_start < 256:
        b = b_start
        pt_nums = []
        for num in nums:
            pt_num = num ^ b
            if pt_num > 127 or pt_num < 32:
                break
            pt_nums.append(chr(pt_num))
            b = (b + x) % 256
        if len(pt_nums) == 32:
            print( ''.join(pt_nums))

        b_start += 1
    x += 1
    b_start = 0
