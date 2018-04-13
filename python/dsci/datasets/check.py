#!/usr/bin/env python

with open('FAO.csv') as f:
	lines = f.readlines()
	print(type(lines[0][0]))
