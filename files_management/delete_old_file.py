#!/usr/bin/env python3

import os
from typing import List

def delete_files(file_paths: List[str]) -> None:
   """
   Deletes the specified files from the filesystem.

   Args:
       file_paths (str): A list of file paths to delete.
   Returns:
        None: This function prints the result of the deletion attempts.
   """
   for file_path in file_paths:
      try:
         if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File: '{file_path}' deleted successfully.")
         else:
            print(f"File: '{file_path}' does not exist.")
      
      except Exception as e:
         print(f"An error occurred while deleting '{file_path}'\n{e}")

if __name__ == ("__main__"):
   # File(s) to delete
   files_to_delete: List[str] = []
   
   delete_files(files_to_delete)
