#!/usr/bin/env python3

# Write a function that adds all unique integers in a list (only once for each integer).

# Prototype: def uniq_add(my_list=[]):
# You are not allowed to import any module

from typing import List


def uniq_add(my_list: List[int]=[]) -> int:
   """
   Adds all unique integers in a list and return the sum.

   Args:
       my_list (List[int], optional): The list whose unique integer elements
         will be summed. Defaults to [].

   Returns:
       int: The sum of unique interger found in `my_list`.
   """
   return sum(set(my_list))


if __name__ == '__main__':
   my_list: List[int] = [1, 2, 3, 1, 4, 2, 5]
   result: int = uniq_add(my_list)
   print("Result: {:d}".format(result))
