#!/usr/bin/python3

# Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).

# Prototype: def remove_char_at(str, n):
# You are not allowed to import any module
# You don’t need to understand __import__

def remove_char_at(string: str, n: int) -> None:
   new_str = ''
   
   for i in range(len(string)):
      if i != n:
         new_str += string[i]

   return new_str
