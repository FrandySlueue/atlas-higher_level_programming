#!/usr/bin/env python3

# Write a function that replaces all occurrences of an element by another in a new list.

# Prototype: def search_replace(my_list, search, replace):
# my_list is the initial list
# search is the element to replace in the list
# replace is the new element
# You are not allowed to import any module

from typing import List, Any


def search_replace(my_list: List[Any], search: Any, replace: Any) -> List[Any]:
   """
   Replaces all occurrences of an element by another in a list and return a new list
   without modifying the original list.

   Args:
       my_list (List[Any]): The original list whose elements are to be untouched.
       search (Any): The occurrences of the element(s) to replace.
       replace (Any): The new element that will replace the searched element(s).

   Returns:
       List[Any]: A new list where the search elements are swapped with the replacing elements.
       
   Example:
        >>> search_replace([1, 2, 3, 2], 2, 5)
        [1, 5, 3, 5]
   """
   return [replace if elm == search else elm for elm in my_list]

if __name__ == '__main__':
   my_list: List[int] = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
   new_list: List[Any] = search_replace(my_list, 2, 89)

   print(new_list)
   print(my_list)
