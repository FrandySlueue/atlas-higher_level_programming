#!/usr/bin/python3

# Write a function that adds two integers and returns the result.

# Prototype: def add(a, b):
# Returns the value of a + b
# You are not allowed to import any module
# You don’t need to understand __import__

def add(a: int, b: int) -> int:
   """
   Computes the addition of two integers, `a` and `b`.

   Args:
       a (int): The first number.
       b (int): The second number.

   Returns:
       int: The sum of `a` and `b`.
   """
   return a + b


def main():
   a: int = 10
   b: int = 5
   
   print(add(a, b))


if __name__ == '__main__':
   main()
