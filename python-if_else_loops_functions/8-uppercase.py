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
   """
   Prints each character of `string` while converting them to 
   uppercase when possible.

   Args:
       string (str): The string whose characters will be printed.
   Returns:
        None: This function prints directly to the console.
   """
   for char in string:
      if 'a' <= char <= 'z':
         print(chr(ord(char) - 32), end='')
      else:
         print(char, end='')
   print()


def main():
   name: str = 'Frandy Slueuez'
   school: str = 'atlaS sChool 918'
   
   uppercase(name)
   uppercase(school)


if __name__ == '__main__':
   main()
