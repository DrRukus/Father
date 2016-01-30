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
    numString = str(number)
    places = len(numString)
    even = isEven(places)

    numOfSubs = ceil(len(numString) / 2.0)

    print even
    print numOfSubs
    print places
    subs = []

    #powerTen = 1
    #diff = 2 if even else 1
    #for i in range(0, places - diff):
    #    powerTen *= 10
    #print "Power of ten: {0}".format(powerTen)
    #subs.append((number - (number % powerTen)) / powerTen)
    subs.append(firstDigits(number, two=even))
    print subs[0]

sqrt(58947)
