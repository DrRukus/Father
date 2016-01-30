#!/usr/bin/env python

import argparse

def BaseConverter(decimalNumber, newBase=2):

    digits = '0123456789ABCDEF'
    numberOfDigits = 0

    while newBase ** numberOfDigits < decimalNumber:
        numberOfDigits += 1

    newNumber = ''
 
    msb = numberOfDigits - 1
    place = decimalNumber
    for currentPower in range(msb, -1, -1):
        weight = newBase ** currentPower
        index = place / weight
        newNumber += digits[index]
        if place >= weight:
            place = place - (weight * index)

    return newNumber

# Get CLI arguments and pass to BaseConverter() function
parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int)
parser.add_argument('-b', type=int)
args = parser.parse_args()

newNumber = BaseConverter(args.n, args.b)

print newNumber
