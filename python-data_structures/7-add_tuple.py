#!/usr/bin/env python3


# Write a function that adds 2 tuples.

# Prototype: def add_tuple(tuple_a=(), tuple_b=()):
# Returns a tuple with 2 integers:
# The first element should be the addition of the first element of each argument
# The second element should be the addition of the second element of each argument
# You are not allowed to import any module
# You can assume that the two tuples will only contain integers
# If a tuple is smaller than 2, use the value 0 for each missing integer
# If a tuple is bigger than 2, use only the first 2 integers


from typing import Tuple

def add_tuple(tuple_a: Tuple[int, int] = (0, 0),
              tuple_b: Tuple[int, int] = (0, 0)) -> Tuple[int, int]:
   """
   Returns new tuple containing the sum of two tuples' elements at index
   0 and index 1 where the matching indices are added.
   If and element is missing for either index, it is replace by 0.
   Args:
       tuple_a (Tuple[int, int], optional): The first tuple. Defaults to (0, 0).
       tuple_b (Tuple[int, int], optional): The second tuple. Defaults to (0, 0).

   Returns:
       Tuple[int, int]: The sum of tuples' elements at index 0 and index 1.
   """
   # Get the element or 0 if not available
   a_first = tuple_a[0] if len(tuple_a) > 0 else 0
   a_second = tuple_a[1] if len(tuple_a) > 1 else 0
   b_first = tuple_b[0] if len(tuple_b) > 0 else 0
   b_second = tuple_b[1] if len(tuple_b) > 1 else 0

   # Return the sum of the first and second elements
   return (a_first + b_first, a_second + b_second)

if __name__ == '__main__':
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))
    print(add_tuple((1, 89), (88, 11)))
    print(add_tuple((1,), (3, 4)))
    print(add_tuple((), (3,)))
    print(add_tuple((1, 2, 5), (3, 4)))
