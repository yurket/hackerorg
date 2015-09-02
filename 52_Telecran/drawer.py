#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from turtle import *


class D(object):
    def __init__(self, scale=5, speed_=6):
        self.scale_ = scale
        speed(speed_)

    def move_(self, direction_angle):
        start_angle = heading()
        left(-start_angle + direction_angle)
        fd(self.scale_)

    def up_(self):
        self.move_(90)

    def down_(self):
        self.move_(270)

    def left_(self):
        self.move_(180)

    def right_(self):
        self.move_(0)


def main():
    drawer = D(8, 8)
    color('red', 'yellow')
    
    with open('inputg', 'r') as f:
        for line in f.readlines():
            l = line.strip()
            if l == '2':
                drawer.left_()
            elif l == '3':
                drawer.down_()
            elif l == '1':
                drawer.right_()
            elif l == '4':
                drawer.up_()

    end_fill()
    done()



if __name__ == '__main__':
    main()

