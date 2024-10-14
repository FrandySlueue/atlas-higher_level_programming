#!/usr/bin/env python3

# Write a program that prints the result of the addition of all arguments

# The output should be the result of the addition of all arguments, followed by a new line
# You can cast arguments into integers by using int() \
   # (you can assume that all arguments can be casted into integers)
# Your code should not be executed when imported

import sys
from typing import List
from functools import reduce

def get_sum_of_args(*args) -> int:
   """
   This program prints the result of the addition of all arguments

   Arguments:
      args (List[int]): A list of 0 or more integers.
   Returns:
       int: The sum of all argument passed.
   """
   return 0 if len(args) == 0 else reduce(lambda a, b: a + b, args)


if __name__ == '__main__':
   args: List[int] = list(map(int, sys.argv[1:]))
   print(get_sum_of_args(*args))
