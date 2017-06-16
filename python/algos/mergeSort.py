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
    if loopCount > 2:
        while loopCount > 0:
            #print "Left Ptr: {}; Right Ptr: {}".format(leftPtr, rightPtr)
            if leftList[leftPtr] > rightList[rightPtr]:
                #print "\t{} > {}".format(leftList[leftPtr], rightList[rightPtr])
                merger.append(leftList[leftPtr])
                if leftPtr >= len(leftList) - 1:
                    if rightPtr == len(rightList) - 1:
                        merger.append(rightList[-1])
                    break
                leftPtr += 1
            else:
                #print "\t{} <= {}".format(leftList[leftPtr], rightList[rightPtr])
                merger.append(rightList[rightPtr])
                if rightPtr >= len(rightList) - 1:
                    if leftPtr == len(leftList) - 1:
                        merger.append(leftList[-1])
                    break
                rightPtr += 1
            loopCount -= 1
        if leftPtr < len(leftList) - 1:
            merger.extend(leftList[leftPtr:len(leftList)])
        elif rightPtr < len(rightList) - 1:
            merger.extend(rightList[rightPtr:len(rightList)])
        return merger
    else:
        return sorted([leftList[0], rightList[0]], reverse=True)

def mergeSort(unsortedList):
    leftList = unsortedList([0:len(unsortedList) / 2])
    rightList = unsortedList([len(unsortedList) / 2:len(unsortedList)])
    if len(rightList) > 1:
        merge(mergeSort(leftList), mergeSort(

#print merge([6, 3, 2], [5, 4, 1])

#print merge([6, 4, 3], [5, 2, 1])

#print merge([6], [4])

#print merge([6, 4], [4, 3])
