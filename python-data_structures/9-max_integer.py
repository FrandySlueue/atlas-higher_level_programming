#!/usr/bin/env python3

# Write a function that finds the biggest integer of a list.

# Prototype: def max_integer(my_list=[]):
# If the list is empty, return None
# You can assume that the list only contains integers
# You are not allowed to import any module
# You are not allowed to use the builtin max()

from typing import List, Optional


def max_integer(my_list: List[int] = []) -> Optional[int]:
   """
   Returns the largest integer in `my_list`, or None if `my_list` is empty.

   Args:
       my_list (List[int], optional): A list of integers from which the largest number
       will be returned. Returns None if the list is empty. Defaults to [].

   Returns:
       int: The largest integer in `my_list` or `None` if the list is empty.
   """
   if not my_list:
      return None
   
   max_num: int = my_list[0]
   for num in my_list:
      if num > max_num:
         max_num = num
      
   return max_num


if __name__ == '__main__':
   my_list: List[int] = []
   max_value: Optional[int] = max_integer(my_list)
   print("Max: {}".format(max_value))
