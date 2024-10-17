#!/usr/bin/env python3

# Write a function that replaces an element of a list at a specific position.

# Prototype: def replace_in_list(my_list, idx, element):
# If idx is negative, the function should not modify anything, and returns the original list
# If idx is out of range (> of number of element in my_list), the function \
#    should not modify anything, and returns the original list
# You are not allowed to import any module
# You are not allowed to use try/except

from typing import List, Any


def replace_in_list(my_list: List[Any], idx: int, element: Any) -> List[Any]:
   """
   This program updates an element at a given index and return the modified list
   if the provided index is not out of bounds ( idx < 0 or idx >= lengh of list), 
   otherwise it will return the original list. 
   
   Args:
       my_list (List[Any]): The list to be updated.
       idx (int): The index of the element to update.
       element (Any): The new updated element.

   Returns:
       List[Any]: The updated list or the original list if the index is out of bounds.
   """
   if idx < 0 or idx >= len(my_list):
      return my_list
   
   my_list[idx] = element
   
   return my_list


def main():
   my_list: List[Any] = ['qoder', 'code', 'pythonist', 'Javascript']
   idx: int = 6
   element: Any = 'Python'
   
   print(replace_in_list(my_list, idx, element))


if __name__ == '__main__':
   main()
