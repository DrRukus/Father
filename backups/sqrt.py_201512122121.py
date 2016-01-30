#!/usr/bin/env python

from math import ceil

def isEven(number):
    return True if number % 2 == 0 else False

def firstDigits(number, two=True):
    places = len(str(number))
    powerTen = 1
    diff = 2 if two else 1
    for i in range(0, places - diff):
        powerTen *= 10
    print "Power of ten: {0}".format(powerTen)
    return (number - (number % powerTen)) / powerTen

def sqrt(number, precision=2):
    numStub = number
    numString = str(number)

    numOfSubs = int(ceil(len(numString) / 2.0))

    print numOfSubs
    subs = []

    #subs.append(firstDigits(number, two=isEven(len(numString)))
    start = 0
    if isEven(len(numString)):
        start = 1
    else:
        start = 0
    subs.append(numString[0:start + 1])
    print subs[0]

    for i in range(start, len(numString) + 1, 2):
        #print "Number Stub: {0}".format(numStub)
        #numStub = numStub - subs[i - 1]
        subs.append(numString[i:i + 1])

    print subs

sqrt(36535947)
