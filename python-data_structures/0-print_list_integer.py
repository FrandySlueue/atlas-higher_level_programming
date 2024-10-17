#!/usr/bin/env python3

# Write a function that prints all integers of a list.

# Prototype: def print_list_integer(my_list=[]):
# Format: one integer per line. See example
# You are not allowed to import any module
# You can assume that the list only contains integers
# You are not allowed to cast integers into strings
# You have to use str.format() to print integers

from typing import List


def print_list_integer(my_list: List[int]=[]) -> None:
   """
   Prints the integer elements of a list one element per line.

   Args:
       my_list (List[int], optional): The list whose integer elements \
          will be printed. Defaults to an empty list.
   
   Returns:
      None: This function prints directly to the console.
   """
   for num in my_list:
      print("{}".format(num))


def main():
   my_list: List[int] = [3, 5, 6, 7, 8]
   print_list_integer(my_list)


if __name__ == '__main__':
   main()
