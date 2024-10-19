#!/usr/bin/env python3

# Write a program that prints #pythoniscool, followed by a new line,\
   # in the standard output.

# Your program should be maximum 2 lines long
# You are not allowed to use print or eval or open or import \
   # sys in your file 101-easy_print.py

import os

def main():
   os.write(1, b"#pythonischool\n")
   """Print to standard output with os module.
   """


if __name__ == '__main__':
   main()
