#!/usr/bin/env python

UPPER = 1000
nums = range(1, UPPER)

mults = []
for num in nums:
    if num % 3 == 0 or num % 5 == 0:
        mults.append(num)

print(sum(mults))
