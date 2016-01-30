#!/usr/bin/env python

#minDotProd = 0

def dotProduct(v1, v2):
    assert len(v1) == len(v2)
        
    dotProd = 0
    for j in range(len(v1)):
        dotProd += v1[j] * v2[j]
    #print dotProd
    return dotProd

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def rotateList(inputList):
    v1Temp = list(inputList)
    for k in range(0, len(inputList)):
        if k == len(inputList) - 1:
            v1Temp[-1] = inputList[0]
        else:
            v1Temp[k] = inputList[k + 1]
    return v1Temp

def permutations(inputList):
    if len(inputList) == 2:
        #print "Gotcha!!!"
        return [inputList, rotateList(inputList)]
    else:
        listLength = len(inputList)
        numOfPerms = factorial(listLength)
        perms = [inputList]
        tempList = [] # Each perm in here will have the same first number
        # Each number will be in 1st position
        for i in range(0, listLength):
            tempList.append([inputList[i]])
            print "Temp List"
            print tempList
            setChar = inputList[i] # put the ith number in 1st position
            # With the same number in 1st position, loop through (listLength - 1)! times
            smallList = []
            for j in range(0, listLength):
                if j != i:
                    smallList.append(inputList[j])
            #print "Small List"
            #print smallList
            smallPerms = permutations(smallList)
            print "Small Perms"
            print smallPerms
            #print "Temp List [0]"
            #print tempList[0]
            k = 0

            for j in range(factorial(len(inputList) - 1)):
                tempList.append([inputList[i]])
                print "Initial Temp Temp List"
                print tempList
                print "J = {0}; K = {1}".format(j, k)
                if k == factorial(len(inputList) - 2):
                    k = 0
                else:
                    k += 1
                tempList[j] = tempList[j] + smallPerms[k]
                print "Final Temp Temp List"
                print tempList
            print "Final Temp List"
            print tempList
        return perms
    
"""
with open("inputFiles/minScalarInput.txt") as inputFile:
    inputLines = inputFile.readlines()

    #cases = int(inputLines[0])
    lineCount = 1
    for j in range(1, int(inputLines[0])):
        for i in range(1, len(inputLines), 3):
            #print lineCount
            
            vectorSize = int(inputLines[lineCount])
    
            v1 = inputLines[lineCount + 1].rstrip().split(" ")
            v2 = inputLines[lineCount + 2].rstrip().split(" ")
    
            v1 = [ int(comp) for comp in v1 ]
            v2 = [ int(comp) for comp in v2 ]

            permutations(v1)  
            lineCount += 3
"""

testList = [1, 2, 3, 4]

permutations(testList)

    
