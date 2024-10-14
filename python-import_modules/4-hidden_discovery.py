#!/usr/bin/env python3

import importlib.util

def main():
    # Load the compiled 'hidden_4.pyc' module
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get all names defined by the module
    names = dir(hidden_4)

    # Filter out names that start with '__'
    visible_names = [name for name in names if not name.startswith('__')]

    # Sort names in alphabetical order
    visible_names.sort()

    # Print each name on a new line
    for name in visible_names:
        print(name)

if __name__ == "__main__":
    main()


# import hidden_4

# def main():
#     # Get all names defined by the module
#     names = dir(hidden_4)
    
#     # Filter out names that start with '__'
#     visible_names = [name for name in names if not name.startswith('__')]
    
#     # Sort names in alphabetical order
#     visible_names.sort()
    
#     # Print each name on a new line
#     for name in visible_names:
#         print(name)

# if __name__ == "__main__":
#     main()