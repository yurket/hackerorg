#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import math


# def mul(A, B):
#     a, b, c = A
#     d, e, f = B
#     return a*d + b*e, a*e + b*f, b*e + c*f

# def pow(A, n):
#     if n == 1:     return A
#     if n & 1 == 0: return pow(mul(A, A), n//2)
#     else:          return mul(A, pow(mul(A, A), (n-1)//2))

# def fib(n):
#     if n < 2: return n
#     return pow((1,1,0), n-1)[0]

# algorithm is taken from here: http://en.literateprograms.org/Fibonacci_numbers_%28Python%29
def powLF(n):
    if n == 1:     return (1, 1)
    L, F = powLF(n//2)
    L, F = (L**2 + 5*F**2) >> 1, L*F
    if n & 1:
        return ((L + 5*F)>>1, (L + F) >>1)
    else:
        return (L, F)

def fib(n):
    return powLF(n)[1]



def main():
    print(math.log(fib(150*10**6)))


if __name__ == '__main__':
    main()

