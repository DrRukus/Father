#!/usr/bin/env python

with open('file.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "Apple" in line:
            print line
