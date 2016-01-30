#!/usr/bin/env python

from math import ceil

def sqrt(number, precision=2):
    numStub = number
    numString = str(number)

    numOfSubs = int(ceil(len(numString) / 2.0))

    subs = []

    start = 2 if len(numString) % 2 == 0 else 1
    subs.append(numString[0:start])

    for i in range(start, len(numString), 2):
        subs.append(numString[i:i + 2])
    print subs
    
    firstGroup = None
    for i in range(0, 10):
        if i**2 > int(subs[0]):
            firstGroup = i - 1
            break

    print firstGroup 


sqrt(39535947)
