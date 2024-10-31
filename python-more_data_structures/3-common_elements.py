#!/usr/bin/env python3

# Write a function that returns a set of common elements in two sets.

# Prototype: def common_elements(set_1, set_2):
# You are not allowed to import any module

from typing import Set


def common_elements(set_1: Set[str], set_2: Set[str]) -> Set[str]:
   """
   Returns a set of common elements between two sets.

   Args:
       set_1 (Set[str]): The first set
       set_2 (Set[str]): The second set

   Returns:
       Set[str]: A set containing the common elements between `set_1` and `set_2`.
                 If no common elements, exist, returns and empty set.
   """
   return set_1 & set_2


if __name__ == '__main__':
   set_1: Set[str] = { "Python", "C", "Javascript" }
   set_2: Set[str] = { "Bash", "C", "Ruby", "Perl" }
   c_set: Set[str] = common_elements(set_1, set_2)
   print(sorted(list(c_set)))
