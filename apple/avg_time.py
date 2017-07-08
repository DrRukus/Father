#!/usr/bin/env python

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
