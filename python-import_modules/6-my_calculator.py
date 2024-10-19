#!/usr/bin/env python3

# Write a program that imports all functions from the file calculator_1.py \
   # and handles basic operations.

# Usage: ./100-my_calculator.py a operator b
# If the number of arguments is not 3, your program has to:
# print Usage: ./100-my_calculator.py <a> <operator> <b> followed with a new line
# exit with the value 1
# operator can be:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# If the operator is not one of the above:
# print Unknown operator. Available operators: +, -, * and / followed with a new line
# exit with the value 1
# You can cast a and b into integers by using int() \
   # (you can assume that all arguments will be castable into integers)
# The result should be printed like this: <a> <operator> <b> = <result>, followed by a new line
# You are not allowed to use * for importing or __import__
# Your code should not be executed when imported

import sys
from typing import Callable, Dict, List
from calculator_1 import add, sub, mul, div


def my_calculator(a: int, operator: str, b: int) -> None:
   """
   This program performs basic arithmatic between two integers depending
   on the operator introduced and prints the result.

   Args:
       a (int): The first integer
       operator (str): The operator
       b (int): The second integer
   Exceptions:
      Handles ZeroDivisionError
  
   """
   operations: Dict[str, Callable[[int, int], float]] = \
      { "+": add, "-": sub, "*": mul, "/": div }
   
   if operator in operations:
      try:
         result: float = operations[operator](a, b)
         print(f"{a} {operator} {b} = {result}")
      except ZeroDivisionError as e:
         print(e)
         sys.exit(1)

   else:
      print("Unknown operator. Available operators: +, -, * and /")
      sys.exit(1)


def main():
   args: List[str] = sys.argv[1:]
   
   if len(args) != 3:
      print("Usage: ./6-my_calculator.py <a> <operator> <b>")
      sys.exit(1)
   
   a, operator, b = args
   my_calculator(int(a), operator, int(b))


if __name__ == '__main__':
   main()
