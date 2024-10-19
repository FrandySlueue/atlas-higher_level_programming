#!/usr/bin/python3

# Write a program that prints the ASCII alphabet, in reverse order,
# alternating lowercase and uppercase (z in lowercase and Y in uppercase) , 
# not followed by a new line.

# You can only use one print function with string format
# You can only use one loop in your code
# You are not allowed to store characters in a variable
# You are not allowed to import any module

def main():
   for i in range(ord('z'), ord('a') - 1, -1):
      print(chr(i - 32) if i % 2 != 0 else chr(i), end=' ')


if __name__ == '__main__':
   main()
