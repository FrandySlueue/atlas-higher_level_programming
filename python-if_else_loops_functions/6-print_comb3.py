#!/usr/bin/python3

# Write a program that prints all possible different combinations of two digits.

# Numbers must be separated by ,, followed by a space
# The two digits must be different
# 01 and 10 are considered the same combination of the two digits 0 and 1
# Print only the smallest combination of two digits
# Numbers should be printed in ascending order, with two digits
# The last number should be followed by a new line
# You can only use no more than 3 print functions with string format
# You can only use no more than 2 loops in your code
# You are not allowed to store numbers or strings in a variable
# You are not allowed to import any module

def main():
   for i in range(10):
      for j in range(i + 1, 10):
         if i == 8 and j == 9:   
            print(f"{i}{j}")
         else:
            print(f"{i}{j}", end=", ")


if __name__ == '__main__':
   main()
