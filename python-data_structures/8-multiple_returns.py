#!/usr/bin/env python3

# Write a function that returns a tuple with the length of a string and its first character.

# Prototype: def multiple_returns(sentence):
# If the sentence is empty, the first character should be equal to None
# You are not allowed to import any module

from typing import Tuple, Optional


def multiple_returns(sentence: str) -> Tuple[int, Optional[str]]:
   """
   Returns the length of the string `sentence` and its first character,
   or (0, None) if the string is empty.

   Args:
       sentence (str): The string whose length and first character are
       to be returned.

   Returns:
       Optional[Tuple[int, str]]: A tuple containing the length of `sentence` 
       and its first character. It returns (0, None) if the string is empty.
   """
   if len(sentence) == 0:
      return (0, None)
   
   return (len(sentence), sentence[0])


if __name__ == '__main__':
   sentence = ""
   length, first = multiple_returns(sentence)
   print("Length: {:d} - First character: {}".format(length, first))
   