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

    map_table = {
        '1': getattr(drawer, 'right_')
        , '2': getattr(drawer, 'left_')
        , '3': getattr(drawer, 'down_')
        , '4': getattr(drawer, 'up_')
    }

    with open('inputg', 'r') as f:
        for line in f.readlines():
            l = line.strip()
            map_table[l]()

    end_fill()
    done()



if __name__ == '__main__':
    main()

