#!/usr/bin/python3

# Write a function that creates a copy of the string, 
# removing the character at the position n 
# (not the Python way, the “C array index”).

# Prototype: def remove_char_at(str, n):
# You are not allowed to import any module
# You don’t need to understand __import__

def remove_char_at(string: str, n: int) -> str:
   """
   Creates a copy of 'string' and remove character at 'n' position
   then returns the new modified copy.

   Args:
       string (str): The string that will be copied.
       n (int): The index of the character that will be removed.

   Returns:
       str: The new modified copy of 'string' with the character at index 'n' removed.
   """
   if n < 0 or n >= len(string):
      return string

   return string[:n] + string[n+1:]


def main():
   string: str = 'Welcome to qcoding with us..!'
   n: int = 11
   
   print(remove_char_at(string, n))


if __name__ == '__main__':
   main()
