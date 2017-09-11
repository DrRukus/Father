#!/usr/bin/env python

from math import sqrt
from itertools import count, islice

def isPrime(num):
    return num > 1 and all(num%i for i in islice(count(2), int(sqrt(num)-1)))

def getNthPrime(n):
    num = 2
    primeIndex = 1
    while primeIndex != n:
        num += 1
        if isPrime(num):
            primeIndex += 1
    return num

print(getNthPrime(10001))