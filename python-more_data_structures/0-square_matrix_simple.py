#!/usr/bin/env python3

# Write a function that computes the square value of all integers of a matrix.

# Prototype: def square_matrix_simple(matrix=[]):
# matrix is a 2 dimensional array
# Returns a new matrix:
# Same size as matrix
# Each value should be the square of the value of the input
# Initial matrix should not be modified
# You are not allowed to import any module
# You are allowed to use regular loops, map, etc.

from typing import List


def square_matrix_simple(matrix: List[List[int]] = []) -> List[List[int]]:
   """
   Returns a matrix where each element is squared.

   Args:
       matrix (List[List[int]], optional): The input matrix of integers. Defaults to [].

   Returns:
       List[List[int]]: A new matrix where each element is the squared of the corresponding
            element in the input matrix.
   """
   return [[elm * elm for elm in row] for row in matrix]


if __name__ == '__main__':
   matrix: List[List[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
   ]

   new_matrix: List[List[int]] = square_matrix_simple(matrix)
   print(new_matrix)
   print(matrix)
