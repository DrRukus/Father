#!/usr/bin/env python

LIMIT = 100
nums = range(1, LIMIT + 1)

def sumOfSquares():
    return sum([n*n for n in nums])

def squareOfSums():
    initSum = sum([n for n in nums])
    return initSum * initSum

diff = squareOfSums() - sumOfSquares()
print('Diff: {}'.format(diff))