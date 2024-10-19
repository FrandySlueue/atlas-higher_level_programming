#!/usr/bin/env python3

def add(a: int, b: int) -> int:
   """
   Add two integers and return their sum.

   Args:
       a (int): The first integer.
       b (int): The second integer.

   Returns:
       int: The sum of a + b
   """
   return a + b


def main():
    a = 10
    b = 5
    
    print(add(a, b))
    

if __name__ == ('__main__'):
   main()
