#!/usr/bin/env python3

# Write a program that prints the alphabet in uppercase, followed by a new line.

# Your program should be maximum 3 lines long
# You are not allowed to use:
# any loops
# any conditional statements
# str.join()
# any string literal
# any system calls

import string

print(*map(chr, range(65, 91)),sep='', end='\n')
"""
Print the ascii alphabet in uppercase follow by a new line.
"""
