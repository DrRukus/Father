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
    for i in range(0, precision + 1):
        subs.append('00')

    firstGroup = None
    for i in range(0, 10):
        if i**2 > int(subs[0]):
            firstGroup = i - 1
            break

    solution = [str(firstGroup)]
    stepSum = 0
    minuend = int(subs[0])
    subtrahend = firstGroup**2
    for i in range(1, numOfSubs + precision + 1):
        solInt = int(''.join(solution))
        stepDiff = minuend - subtrahend
        minuend = stepDiff * 100 + int(subs[i])
        for j in range(0, 10):
            if (solInt * 20 + j) * j > minuend:
                subtrahend = (solInt * 20 + (j - 1)) * (j - 1)
                solution.append(str(j - 1))
                break
            if j == 9:
                subtrahend = (solInt * 20 + j) * j
                solution.append(str(j))
    rounder = 1 if int(solution[-1]) > 4 else 0
    finalSolutionInt = int((int(''.join(solution)) / 10.0) + rounder)
    return str(finalSolutionInt / 10.0**(precision))

print "\nGive me a number and I'll tell you the square root"
print "========================================================="
inputNum = input("Enter number: ")
prec = input("To how many decimal places: ")
root = sqrt(inputNum, precision=prec)
print "The square root of {0}, to {1} decimal places, is {2}".format(inputNum, prec, root)
percentError = ((float(root) * float(root) - inputNum) / inputNum) * 100
print "Percent Error: {0} %".format(percentError)
