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
        subs.append("00")

    firstGroup = None
    for i in range(0, 10):
        if i**2 > int(subs[0]):
            firstGroup = i - 1
            break

    print firstGroup
    solution = str(firstGroup)
    stepSum = 0
    minuend = int(subs[0])
    subtrahend = firstGroup**2
    for i in range(1, numOfSubs + precision + 1):
        print "Solution so far: {0}".format(solution)
        stepDiff = minuend - subtrahend
        print "Step Diff for i={0}: {1}".format(i, stepDiff)
        minuend = stepDiff * 100 + int(subs[i])
        for j in range(0, 10):
            if (int(solution) * 20 + j) * j > minuend:
                print j
                subtrahend = (int(solution) * 20 + (j - 1)) * ( j - 1)
                solution = str(int(solution) * 10 + (j - 1))
                break
        print "\n\nMinuend for i={0}: {1}".format(i, minuend)
        print "Subtrahend for i={0}: {1}\n".format(i, subtrahend)

    return str(int(solution) / 10.0**(precision + 1))


inputNum = 70284
prec = 5
print "The square root of {0} is {1}".format(inputNum, sqrt(inputNum, precision=prec))
