#!/usr/bin/python3

# Write a function that checks for lowercase character.

# Prototype: def islower(c):
# Returns True if c is lowercase
# Returns False otherwise
# You are not allowed to import any module
# You are not allowed to use str.upper() and str.isupper()
# Tips: ord()
# You don’t need to understand __import__

def islower(c: str) -> bool:
   """
   Returns True if `c` is a lowercase character otherwise
   False is returned.

   Args:
       c (str): The character that will be evaluated.
               This function expects a single character.

   Returns:
       bool: True if `c` is lowercase,
       False if it is not lowercase of if `c` is not a single character.
   """
   return 'a' <= c <= 'z' if len(c) == 1 else False
   

def main():
   print(islower('a'))
   print(islower('A'))
   print(islower('1'))
   print(islower('ab'))
   print(islower(' '))
   print(islower('r '))
   print(islower('z'))
   

if __name__ == '__main__':
   main()
