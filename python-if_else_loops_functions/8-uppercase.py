#!/usr/bin/python3

# Write a function that prints a string in uppercase followed by a new line.

# Prototype: def uppercase(str):
# You can only use no more than 2 print functions with string format
# You can only use one loop in your code
# You are not allowed to import any module
# You are not allowed to use str.upper() and str.isupper()
# Tips: ord()
# You don’t need to understand __import__

def uppercase(string: str) -> None:
   uppercase_str: str = ''
   for char in str:
      if ord(char) in range(ord('a'), ord('z') + 1):
         uppercase_str += chr(ord(char) - 32)
      else:
         uppercase_str += char
   print(f"{uppercase_str}")
