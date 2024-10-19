#!/usr/bin/env python3

import os
from typing import List

def create_python_files(filename: str, interpreter: str='/usr/bin/env python3') -> None:
   """
   Creates a new file(s) and adds execution permissions and a shebang line.

   Args:
       filename (str): The new file(s) that will be created.
       interpreter (str, optional): _The shebang line to be added. Defaults to '/usr/bin/env python3'.
   
   Returns:
      None: This function prints the result of created files attemps.
   """
   # The shebang which will be the first line of code in the file
   shebang_line: str = f"#!{interpreter}\n"
   
   try:
      # Add the shebang line to the file with execution permissions
      with open(filename, 'w') as f:
         f.write(shebang_line)
         os.chmod(filename, 0o755)
         print(f"File: {filename} was successfully created.")
   
   except Exception as e:
      print(f"An error occurred:\n{e}")


if __name__ == ("__main__"):
   # File(s) to create
   file_list: List[str] = ["../python-data_structures/12-switch.py"]
   for filename in file_list:
      create_python_files(filename)
