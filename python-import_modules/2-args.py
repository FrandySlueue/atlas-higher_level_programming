#!/usr/bin/env python3

# Write a program that prints the number of and the list of its arguments.

# The output should be:
# Number of argument(s) followed by argument (if number is one) or \
   # arguments (otherwise), followed by
# : (or . if no arguments were passed) followed by
# a new line, followed by (if at least one argument),
# one line per argument:
# the position of the argument (starting at 1) followed by :, \
   # followed by the argument value and a new line
# Your code should not be executed when imported
# The number of elements of argv can be retrieved by using: len(argv)
# You do not have to fully understand lists yet, but imagine that \
   # argv can be used just like a C array: you can use an index to \
      # walk through it. There are other ways (which will be preferred \
         # for future project tasks), if you know them you can use them.

import sys
from typing import List

def print_args(args: List[str]=[]) -> None:
   """
   This program prints the number of and the list of its command line argments.

   Args:
       args (List[str], optional): The command line arguments to print. Defaults to [].
   """
   args_size: int = len(args)
   
   # Handle both singular and plural using a conditional expression in the print statement.
   print(f"{args_size} argument{'s' if args_size != 1 else ''}{'.' if args_size == 0 else ':'}")
   
   for idx, arg in enumerate(args, 1):
      print(f"{idx}: {arg}")

if __name__ == '__main__':
   args: List[str] = sys.argv[1:]
   print_args(args)
