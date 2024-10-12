#!/usr/bin/python3

# Write a function that prints the numbers from 1 to 100 separated by a space.

# For multiples of three print Fizz instead of the number and for multiples of five print Buzz.
# For numbers which are multiples of both three and five print FizzBuzz.
# Prototype: def fizzbuzz():
# Each element should be followed by a space
# You are not allowed to import any module
# You don’t need to understand __import__

def fizzbuzz() -> None:
   value: str = ''
   for i in range(1, 101):
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
