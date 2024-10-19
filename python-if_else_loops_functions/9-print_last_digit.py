#!/usr/bin/python3

# Write a function that prints the last digit of a number.

# Prototype: def print_last_digit(number):
# Returns the value of the last digit
# You are not allowed to import any module
# You don’t need to understand __import__

import random


def print_last_digit(number: int) -> int:
   """
   Returns the last digit of an integer `number`.

   Args:
       number (int): The integer.

   Returns:
       int: The last digit of `number`.
   """
   last_digit: int = abs(number) % 10
   
   return last_digit


def main():
   number: int = random.randint(-100, 100)
   
   print(f'The last digit of {number} is {print_last_digit(number)}')


if __name__ == '__main__':
   main()
