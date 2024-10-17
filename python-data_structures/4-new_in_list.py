#!/usr/bin/env python3

# Write a function that replaces an element in a list at a specific \
    #position without modifying the original list.

# Prototype: def new_in_list(my_list, idx, element):
# If idx is negative, the function should return a copy of the original list
# If idx is out of range (> of number of element in my_list), \
    #the function should return a copy of the original list
# You are not allowed to import any module
# You are not allowed to use try/except

from typing import List, Any


def new_in_list(my_list: List[Any], idx: int, element: Any) -> List[Any]:
   """
   Replaces an element in a list at a specific position
   without modifying the original list.

   Args:
       my_list (List[Any]): The original list
       idx (int): The index of the element to be replaced.
       element (Any): The new element to insert at the given index.

   Returns:
       List[Any]:
         - A copy of the original list if index is out of range.
         - A modified copy of the list with the new element at the
            given index, if the index is valid.
   
   Note:
      This function does not support Python's native negative indexing.
      If a negative index is provided, the original list will be returned.
   """
   return (
      [*my_list] if idx >= len(my_list) or idx < 0
      else [*my_list[:idx], element, *my_list[idx + 1:]]
   )


def main():
   my_list: List[Any] = ['qoder', 45, 'pythonist', 'JavaScript', True]
   idx: int = -32
   element: Any = 'Python'
   print(new_in_list(my_list, idx, element))


if __name__ == '__main__':
   main()
