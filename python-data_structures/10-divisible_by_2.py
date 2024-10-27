#!/usr/bin/env python3

# Write a function that finds all multiples of 2 in a list.

# Prototype: def divisible_by_2(my_list=[]):
# Return a new list with True or False, depending on whether the 
# integer at the same position in the original list is a multiple of 2
# The new list should have the same size as the original list
# You are not allowed to import any module


from typing import List, Any


def divisible_by_2(my_list: List[Any] = []) -> List[bool]:
   """
   Returns a copy of `my_list` where the list elements are converted to
   boolean values, True if an element is multiple of 2, otherwise False.

   Args:
       my_list (List[Any]): The list of integer to evaluate for multiples of 2.

   Returns:
       List[bool]: A new list containing boolean values indicating whether each
       element in `my_list` is a multiple of 2.
   """
   result: List[bool] = [num % 2 == 0 for num in my_list]
   
   return result


if __name__ == '__main__':
   my_list: List[int] = [0, 1, 2, 3, 4, 5, 6]
   list_result: List[bool] = divisible_by_2(my_list)

   i = 0
   while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1