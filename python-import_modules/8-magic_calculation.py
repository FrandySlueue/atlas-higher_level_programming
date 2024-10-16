#!/usr/bin/env python3

from dis import dis
from typing import Callable

def magic_calculation(a: int, b: int) -> int:
    """
    This function performs a magic calculation using the 'add' and 'sub' 
    functions from the 'calculation_1' module.

    - If `a` is less than `b`, it calculates `c = add(a, b)`, and then adds 
      values from 4 to 5 to `c` using the `add` function.
    - If `a` is greater than or equal to `b`, it returns `sub(a, b)`.

    Args:
        a (int): The first integer for comparison and calculation.
        b (int): The second integer for comparison and calculation.

    Returns:
        int: The result of the calculation, either from the `add` function or 
             the `sub` function depending on the comparison of `a` and `b`.
    """
    from calculator_1 import add, sub

    if a < b:
        c: int = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)  # If a >= b, return sub(a, b)


dis(magic_calculation)
