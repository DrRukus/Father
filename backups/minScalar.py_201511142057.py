#!/usr/bin/env python

#minDotProd = 0

def dotProduct(v1, v2):
    assert len(v1) == len(v2)
        
    dotProd = 0
    for i in range(len(v1)):
        dotProd += v1[i] * v2[i]
    #print dotProd
    return dotProd


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def rotateList(inputList):
    listRot = list(inputList)
    listRot[-1] = inputList[0]
    for i in range(0, len(inputList) - 1):
        listRot[i] = inputList[i + 1]
    return listRot


#def elementsAreUnique(inputList):



def permutations(inputList):
    if len(inputList) == 2:
        return [inputList, rotateList(inputList)]
    else:
        listLength = len(inputList)
        perms = []    # List of all permutations of inputList
        # Each number will be in 1st position
        for i in range(0, listLength):
            # With the same number in 1st position, loop through (listLength - 1)! times
            smallList = [] # inputList without the ith element
            for j in range(0, listLength):
                if j != i: # do not copy the ith element to smallList
                    smallList.append(inputList[j])
            smallPerms = permutations(smallList) # all permutations of smallList
            k = 0
            for j in range(factorial(listLength - 1)):
                #print [inputList[i]] + smallPerms[k]
                #print "K = {0}".format(k)
                newList = [inputList[i]] + smallPerms[k]
                #if newList not in perms:
                perms.append(newList)
                #perms.append([inputList[i]] + smallPerms[k])
                k = 0 if k == len(perms) else k + 1
        return perms
    

with open("inputFiles/minScalarInput.txt") as inputFile:
    inputLines = inputFile.readlines()

    #cases = int(inputLines[0])
    lineCount = 1
    caseCount = 1
    for i in range(1, len(inputLines), 3):
        #print lineCount

        vectorSize = int(inputLines[lineCount])
    
        v1 = inputLines[lineCount + 1].rstrip().split(" ")
        v2 = inputLines[lineCount + 2].rstrip().split(" ")
    
        v1 = [ int(comp) for comp in v1 ]
        v2 = [ int(comp) for comp in v2 ]

        v1Perms = permutations(v1)
        v2Perms = permutations(v2)

        #for j in range(len(v1Perms)):
        #    print v1Perms[j]
        #for j in range(len(v2Perms)):
        #    print v2Perms[j]

        minDotProd = dotProduct(v1Perms[0], v2Perms[0])
        for j in range(1, len(v1Perms)):
            for k in range(1, len(v1Perms)):
                dotProd = dotProduct(v1Perms[j], v2Perms[k])
                if dotProd < minDotProd:
                    #print "j = {0}; k = {1}".format(j, k)
                    minDotProd = dotProd
        print "Case #{0}: {1}".format(caseCount, minDotProd)
        lineCount += 3
        caseCount += 1


#testList = [1, 2, 3, 4, 5]

#print rotateList(testList)

#ps = permutations(testList)

#for i in range(len(ps)):
#    print ps[i]

    
