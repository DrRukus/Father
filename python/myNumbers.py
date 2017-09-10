#!/usr/bin/env python

from math import sqrt

n = 5

innerSum = 3 + sqrt(5)

result = 1
for i in range(0, n):
    result *= innerSum

print("%03d" % (int(result) % 1000))
