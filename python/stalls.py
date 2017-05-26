#!/usr/bin/env python

def initStalls(numStalls):
    stalls = [0] * numStalls
    stalls[0], stalls[-1] = 1, 1

    return stalls

def iterateUp(arr, start=0):
    if start >= 0 and start < (len(arr) - 1):
        for i in range(start + 1, len(arr)):
            yield arr[i]
    else:
        yield -1

def iterateDown(arr, start):
    if start >= 0 and start < (len(arr) - 1):
        for j in range(start - 1, 0, -1):
            yield arr[j]
    else:
        yield -1

def getLeftAndRightDistances(stallNum, stalls):
    if stallNum > len(stalls) - 2:
        return -1, -1
    left, right = 0, 0
    for stall in iterateDown(stalls, stallNum):
        if stall == 0:
            left += 1
        else:
            break
    for stall in iterateUp(stalls, stallNum):
        if stall == 0:
            right += 1
        else:
            break
    return left, right

numStalls = 10
peeps = 5

stalls = initStalls(numStalls)

for peep in range(peeps):
    print stalls
    availables = []
    for stallNum in range(1, numStalls - 1):
        left, right = getLeftAndRightDistances(stallNum, stalls)
        #print "Left: {}; Right: {}".format(left, right)
        availables.append([stallNum, min(left, right)])

    #print availables
    maxDist = 0
    spot = 0
    for available, distance in availables:
        #print available, distance
        if distance > maxDist and stalls[available] != 1 and distance > 0:
            maxDist = distance
            spot = available
        else:
            

    print maxDist, spot
    stalls[spot] = 1
