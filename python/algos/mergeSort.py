#!/usr/bin/env python

unsortedList = [9, 4, 2, 6, 3, 5, 1, 7, 8]

def splitList(inputList):
    halfList = len(inputList) / 2
    return inputList[0:halfList], inputList[halfList:len(inputList)]

def merge(leftList, rightList):
    merger = []
    leftPtr = 0
    rightPtr = 0
    loopCount = len(leftList) + len(rightList)
    while loopCount > 0:
        if leftList[leftPtr] > rightList[rightPtr]:
            merger.append(leftList[leftPtr])
            if leftPtr >= len(leftList) - 1:
                break
            leftPtr += 1
        else:
            merger.append(rightList[rightPtr])
            if rightPtr >= len(rightList) - 1:
                break
            rightPtr += 1
        loopCount -= 1
    if leftPtr < len(leftList) - 1:
        merger.extend(leftList[leftPtr:len(leftList)])
    elif rightPtr < len(rightList) - 1:
        merger.extend(rightList[rightPtr:len(rightList)])
    return merger

print merge([6, 4, 3], [5, 2, 1])
