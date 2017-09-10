#!/usr/bin/env python

from math import pow

MAX_DIGITS = 4
START = int(pow(10, MAX_DIGITS)) - 1
STOP = int(pow(10, MAX_DIGITS - 1))

def isPalindrome(testNum):
   return testNum == int(str(testNum)[::-1])

ans = 0
factors = list()
for i in range(START, STOP, -1):
    for j in range(i, STOP, -1):
        num = i * j
        if isPalindrome(num) and num > ans:
            ans = num
            factors = i, j

print('Solution with two {}-digit numbers is {} from {} and {}.'.format(MAX_DIGITS, ans, *factors))