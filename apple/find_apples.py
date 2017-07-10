#!/usr/bin/env python

"""
Procedure:
    1. Read all lines of inptu file into list
    2. Iterate through list
    3. Check each line for the substring "Apple"
    4. If "Apple" is found, print out line
"""

with open('file.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "Apple" in line:
            print line
