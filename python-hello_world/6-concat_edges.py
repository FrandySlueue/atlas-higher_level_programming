#!/usr/bin/python3

from typing import Any

# Complete this source code (str = "Python is an interpreted, interactive, object-oriented programming\ language that combines remarkable power with very clear syntax") to print `object-oriented programming with Python`, followed by a new line.

# You can find the source code here
# You are not allowed to use any loops or conditional statements
# Your program should be exactly 5 lines long
# You are not allowed to create new variables
# You are not allowed to use string literals

str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
py: Any = str[:6]
obj: Any = str[39:66]
wit: Any = str[-22:-18]
print(f"{obj} {wit} {py}")
