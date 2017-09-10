#!/usr/bin/env python

UPPER = 4000000

def isEven(num):
    return num % 2 == 0

def fib(limit):
    fibSum = 0
    x, y = 1, 1
    while True:
        x, y = x + y, x
        if x >= limit:
            break
        else:
            if isEven(x):
                fibSum += x
    return fibSum


print(fib(UPPER))
