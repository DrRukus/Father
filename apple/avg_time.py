#!/usr/bin/env python

"""
Procedure:
    1. read all lines of inmput file into list
    2. Store number of lines
    3. iterate through list, parse out time values and sum
    4. Divide sum by number of data entries (lines in file)
    5. Print out result
"""

total = 0.0
with open('results.txt', 'r') as f:
    lines = f.readlines()
    numberOfLines = float(len(lines))
    for i, line in enumerate(lines):
        try:
            total += float(line.rstrip().split('\t')[-1].split(' ')[0])
        except IndexError:
            print "Line {} is improperly formatted...skipping...".format(i)
            numberOfLines -= 1.0
    avg = total / numberOfLines

print avg
