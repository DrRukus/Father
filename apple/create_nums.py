#!/usr/bin/env python

"""
Procedure:
    1. Create and open file Numbers.txt.
    2. Iterate through list of integers from 1 to 100.
    3. Check each for divisibility by 5 (number ends in 0 or 5).
    4. If divides into 5, print out tab + asterisk, 
       otherwise print tab + number.
    5. Check if number is mulptiple of 10
    6. If multiple of 10, add new line character after number
"""

with open('Numbers.txt', 'w+') as f:
    for num in range(101):
        f.write('{}\t'.format(num) if num % 5 != 0 else '*\t')
        if num % 10 == 0:
            f.write('\n')
