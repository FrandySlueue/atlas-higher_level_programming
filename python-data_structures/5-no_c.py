#!/usr/bin/env python3

# Write a function that removes all characters c and C from a string.

# Prototype: def no_c(my_string):
# The function should return the new string
# You are not allowed to import any module
# You are not allowed to use str.replace()

def no_c(my_string: str) -> str:
   """
   Removes the characters `c` and `C` from a given string.

   Args:
       my_string (str): The string that will be modified.
   
   Returns:
      str: A new string with all occurences of `c` and `C` removed.
   """
   return ''.join(char for char in my_string if char not in ['c', 'C'])


def main():
   my_string: str = 'Coming compare codes with my Cocomelone class.'
   print(no_c(my_string))


if __name__ == '__main__':
   main()
