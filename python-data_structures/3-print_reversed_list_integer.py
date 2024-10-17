#!/usr/bin/env python3

# Write a function that prints all integers of a list, in reverse order.

# Prototype: def print_reversed_list_integer(my_list=[]):
# Format: one integer per line. See example
# You are not allowed to import any module
# You can assume that the list only contains integers
# You are not allowed to cast integers into strings
# You have to use str.format() to print integers

from typing import List, Any


def print_reversed_list_integer(my_list: List[Any]=[]) -> None:
   """
   Prints the integer elements of a list in reverse order one element per line.

   Args:
       my_list (List[Any], optional): 
         - The list whose integer elements will be printed.
         - Defaults to an empty list.
   
   Returns:
      None: This function prints directly to the console.    
   """
   print(*("{}".format(i) for i in reversed(my_list) if isinstance(i, int)), sep='\n')


def main():
   my_list: List[Any] = [1, 'qoder', 2, 3, 4, 5, 'pythonist', 6, 7, 'Python', 8, 9]
   print_reversed_list_integer(my_list)


if __name__ == '__main__':
   main()
