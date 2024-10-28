#!/usr/bin/env python3

# Write a function that deletes the item at a specific position in a list.

# Prototype: def delete_at(my_list=[], idx=0):
# If idx is negative or out of range, nothing change (returns the same list)
# You are not allowed to use pop()
# You are not allowed to import any module

from typing import List, Any


def delete_at(my_list: List[Any] = [], idx: int=0) -> List[Any]:
   """
   Deletes a list element from a given index.

   Args:
       my_list (List[Any], optional): The list that will be modified. Defaults to [].
       idx (int, optional): The index of the list element that will be deleted. 
       Defaults to 0.

   Returns:
       List[Any]: The modified list. If the index is out of range or the orinal
       list is empty, the original list is returned.
   """
   if not my_list:
      return []
   if idx >= len(my_list) or idx < 0:
      return my_list
   del my_list[idx]
   
   return my_list


if __name__ == '__main__':
   my_list: List[Any] = [1, 2, 3, 4, 5]
   idx: int = 5
   new_list: List[Any] = delete_at(my_list, idx)
   print(new_list)
   print(my_list)
