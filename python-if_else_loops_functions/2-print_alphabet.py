#!/usr/bin/python3

# Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

# Use only one print function with string format
# Use only one loop in your code
# You are not allowed to store characters in a variable
# You are not allowed to import any module

for i in range(ord('a'), ord('z') + 1):
   print(chr(i), end='')
