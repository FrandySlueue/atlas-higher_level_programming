#!/usr/bin/env python3

# Complete the source code in order to switch value of a and b

# You can find the source code here:  a = 89; b = 10
# Your program should be exactly 5 lines long

"""
Swaps the values of two integer variables, `a` and `b`.

Initially, `a` is set to 89 and `b` to 10. The values are then swapped,
so that `a` holds the value of `b` and vice versa.

Example:
   Before swapping: a = 89, b = 10
   After swapping: a = 10, b = 89
"""
a: int = 89
b: int = 10

a, b = b, a

if __name__ == '__main__':
   print("a: {:d} - b: {:d}".format(a, b))
