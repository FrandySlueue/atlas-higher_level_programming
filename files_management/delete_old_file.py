#!/usr/bin/env python3

import os
from typing import List

def delete_files(file_paths: str) -> None:
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
   files_to_delete: List[str] = [""]

   delete_files(files_to_delete)
