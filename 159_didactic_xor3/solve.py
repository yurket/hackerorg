#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

ct = '31cf55aa0c91fb6fcb33f34793fe00c72ebc4c88fd57dc6ba71e71b759d83588'

nums = [ int(ct[i:i+2], 16) for i in xrange(0, len(ct), 2) ]

x, b = 0, 0
b_start = 0

count = 0 
while x < 256:
    while b_start < 256:
        b = b_start
        for i in xrange(256):
            pt_nums = []
            for num in nums:
                # count += 1
                # if count % 1000000 == 0:
                #     print('b_start= %d, b= %d, x= %d, len(pt_nums)= %d' % (b_start, b, x, len(pt_nums)))

                pt_num = num ^ b
                if pt_num > 127:
                    break
                pt_nums.append(chr(pt_num))
                b = (b + x) % 256
            if len(pt_nums) == 32:
                print( ''.join(pt_nums))
            # else:
            #     print(len(pt_nums))

        b_start += 1
    x += 1
    b_start = 0
