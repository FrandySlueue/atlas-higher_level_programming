#!/usr/bin/env python3

# Write a function that retrieves an element from a list.

# Prototype: def element_at(my_list, idx):
# If idx is negative, the function should return None
# If idx is out of range (> of number of element in my_list), the function should return None
# You are not allowed to import any module
# You are not allowed to use try/except

from typing import List, Any

def element_at(my_list: List[Any], idx: int) -> Any:
   """
   This program return an element at a given index of a list.
   It will return `None` if the index is out of bound:
   (greater than the list length or less than zero)

   Args:
       my_list (List[Any]): The list who element is to be returned
       idx (int): The index of the element to be returned

   Returns:
       Any: The element returned from the given index or `None`
   """
   return None if idx > len(my_list) or idx < 0 else my_list[idx]

if __name__ == '__main__':
   idx: int = 9
   
   my_list: List[Any] = ['qoder', 'python', 'Rue 66', 'pythonist']

   print(element_at(my_list, idx))
