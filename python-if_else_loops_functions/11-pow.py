#!/usr/bin/python3

# Write a function that computes a to the power of b and return the value.

# Prototype: def pow(a, b):
# Returns the value of a ^ b
# You are not allowed to import any module
# You don’t need to understand __import__

def pow(a: int, b: int) -> int:
   """
   Computes `a` raised to the power of `b`.

   Args:
       a (int): The base number.
       b (int): The exponent, which c an be negative, zero or positive.

   Returns:
       int: The result of `a` raised to the power of `b`
   """
   return a ** b


def main():
   a: int = 4
   b: int = 3
   
   print(pow(a, b))


if __name__ == '__main__':
   main()
