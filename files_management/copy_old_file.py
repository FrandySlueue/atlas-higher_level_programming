#!/usr/bin/env python3

from typing import List

def copy_content_to_file(source_file: str, target_files: List[str]) -> None:
   """
   Append content of the source file to the target file(s).

   Args:
       source_file (str): The file to copy from.
       target_files (List[str]): The file or files to append to.
   
   Returns:
      None
   """
   try:
      # Read and store content from source file
      with open(source_file, 'r') as src:
         content: str = src.read()
      
      # Copy stored content to target file 
      for target_file in target_files:
         with open(target_file, 'a') as tgt:
            tgt.write(f"\n{content}")
         print(f"Content copied to: {target_file} successfully.")
         
   except FileNotFoundError:
      print(f"The file: {source_file} does not exist.")
   
   except Exception as e:
      print(f"An error occurred: {e}")


if __name__ == ("__main__"):
   # File to copy from
   source_file: str = ''
   
   # File(s) to copy to
   target_files: List[str] = ['']

   copy_content_to_file(source_file, target_files)
