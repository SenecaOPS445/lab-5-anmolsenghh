#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    """Add two numbers together, return the result, if error return string 'error: could not add numbers'"""
    try:
        return int(number1) + int(number2)
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    """Read a file, return a list of all lines, if error return string 'error: could not read file'"""
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except (FileNotFoundError, IOError):
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                      # Works
    print(add('10', 5))                    # Works
    print(add('abc', 5))                   # Exception
    print(read_file('seneca2.txt'))        # Works
    print(read_file('file10000.txt'))      # Exception
