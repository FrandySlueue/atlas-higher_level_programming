#!/usr/bin/python3

# This program will assign a random signed number to the variable number 
# each time it is executed. Complete the source code in order to 
# print whether the number stored in the variable number is positive or negative.

# You can find the source code here (import random; number = random.randint(-10, 10))
# The variable number will store a different value every time you will run this program
# You don’t have to understand what import, random. randint do. 
# Please do not touch this code
# The output of the program should be:
# The number, followed by
# if the number is greater than 0: is positive
# if the number is 0: is zero
# if the number is less than 0: is negative
# followed by a new line

import random

number: int = random.randint(-10, 10)

def main():
   print(
      f"{number} is positive"
      if number > 0
      else f"{number} is negative" 
      if number < 0
      else f"{number} is zero"
   )


if __name__ == '__main__':
   main()
