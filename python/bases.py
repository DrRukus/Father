#!/usr/bin/env python

import argparse

def GetCliArgs(number, base):
    parser = argparse.ArgumentParser()
    parser.add_argument(number, type=int)
    parser.add_argument(base, type=int)
    return parser.parse_args()

def IntegerBaseConverter(decimalNumber, newBase=2):

    digits = '0123456789ABCDEF'
    numberOfDigits = 0

    while newBase ** numberOfDigits <= decimalNumber:
        numberOfDigits += 1

    newNumber = ''

    # Set most-significant digit 
    msb = numberOfDigits - 1

    # Every iteration, we subtract from place
    place = decimalNumber

    # Set each digit in converted-number string
    for currentPower in range(msb, -1, -1):

        # Weight of current digit
        weight = newBase ** currentPower

        #print "Place: {0}; Weight: {1}".format(place, weight)
        index = place / weight
        #if currentPower != msb:
        #    index = place / weight
        #else:
        #    index = (place - 1) / weight
        if index < newBase:
            newNumber += digits[index]
        else:
            newNumber += digits[index - 1]
        if place >= weight:
            place = place - (weight * index)

    return newNumber

# Get CLI arguments and pass to BaseConverter() function
#args = GetCliArgs('-n', '-b')

#newNumber = IntegerBaseConverter(args.n, args.b)

#print newNumber
