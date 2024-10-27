#!/usr/bin/env python3

# Write a function that prints a matrix of integers.

# Prototype: def print_matrix_integer(matrix=[[]]):
# Format: see example
# You are not allowed to import any module
# You can assume that the list only contains integers
# You are not allowed to cast integers into strings
# You have to use str.format() to print integers

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Becomes:
# 1 2 3$
# 4 5 6$
# 7 8 9$
# --$


from typing import List


def print_matrix_integer(matrix: List[List[int]]=[[]]) -> None:
   """
   Prints a matrix of entegers

   Args:
       matrix (List[List[int]], optional): The matrix of integers whose elements will
            be printed to standard output. Defaults to [[]].
   
   Returns:
       None: This program prints directly to the console.
   """
   print('\n'.join(' '.join(str(num) for num in row) for row in matrix))


def main():
   matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
   ]
   print_matrix_integer(matrix)


if __name__ == '__main__':
   main()
