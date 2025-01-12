#!/usr/bin/env python3

def add(a: int, b: int) -> int:
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a: int, b: int) -> int:
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a: int, b: int) -> int:
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a: int, b: int) -> float:
   """My division function

   Args:
      a: first integer
      b: second integer
   Exceptions:
      ZeroDivisionError if the value of b is 0
   Returns:
      The return value. a / b
   """
   try:
      return a / b
   except ZeroDivisionError:
      print(f"Cannot divide by 0")
      return 0.0


def main():
    a: int = 10
    b: int = 0
    
    print(add(a, b))
    print(sub(a, b))
    print(mul(a, b))
    print(div(a, b))


if __name__ == ('__main__'):
   main()
