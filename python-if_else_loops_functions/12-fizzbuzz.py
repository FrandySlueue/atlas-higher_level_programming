#!/usr/bin/python3

# Write a function that prints the numbers from 1 to 100 separated by a space.

# For multiples of three print Fizz instead of the number and for multiples of five print Buzz.
# For numbers which are multiples of both three and five print FizzBuzz.
# Prototype: def fizzbuzz():
# Each element should be followed by a space
# You are not allowed to import any module
# You don’t need to understand __import__

import random


def fizzbuzz(number: int) -> None:
   """
   Circles through a range of numbers from 1 to the specified 'number'.
   It prints 'Fizz' if a number is divisible by 3, 'Buzz' if it is divisible
   by 5 and 'FizzBuzz' if divisible by both 3 and 5 otherwise, it prints the number.

   Args:
       number (int): The number that defines the end range (inclusive).
   Returns:
        None: This function prints directly to the console.
   """
   value: str = ''
   
   for i in range(1, number):
      if i % 3 == 0 and i % 5 == 0:
         value += 'FizzBuzz'
      elif i % 3 == 0:
         value += 'Fizz'
      elif i % 5 == 0:
         value += 'Buzz'
      else:
         value += str(i)
      value += ' '
      
   print(f"{value}")


def main():
   number: int = random.randint(50, 100)
   
   fizzbuzz(number)


if __name__ == '__main__':
   main()
