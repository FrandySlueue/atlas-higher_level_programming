#!/usr/bin/python3

# Complete this source code

# You can find the source code here (word = "Holberton")
# You are not allowed to use any loops or conditional statements
# Your program should be exactly 8 lines long
# word_first_3 should contain the first 3 letters of the variable word
# word_last_2 should contain the last 2 letters of the variable word
# middle_word should contain the value of the variable word 
# without the first and last letters

word: str = "Holberton"

def main():
   word_first_3: str = word[:3]
   word_last_2: str = word[-2:]
   middle_word: str = word[1:-1]
   
   print(f"First 3 letters: {word_first_3}")
   print(f"Last two letters: {word_last_2}")
   print(f"Middle word: {middle_word}")


if __name__ == '__main__':
   main()
