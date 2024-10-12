#!/usr/bin/python3

# This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

# You can find the source code here (import random; number = random.randint(-10000, 10000))
# The variable number will store a different value every time you will run this program
# You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)
# The output of the program should be:
# The string Last digit of, followed by
# the number, followed by
# the string is, followed by the last digit of number, followed by
# if the last digit is greater than 5: the string and is greater than 5
# if the last digit is 0: the string and is 0
# if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
# followed by a new line

import random

number: int = random.randint(-1000, 1000)
last_digit: int = abs(number) % 10
last_digit: int = -abs(last_digit) if number < 0 else last_digit

if last_digit == 0:
   comparison = 'is 0'
elif last_digit > 5:
   comparison = 'and is greater than 5'
elif last_digit < 6:
   comparison = 'and is less than 6 and not 0'
   
print(f"The last digit of {number} is {last_digit} {comparison}")
   