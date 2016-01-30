#!/usr/bin/env python

#minDotProd = 0

def dotProduct(v1, v2):
    assert len(v1) == len(v2)
        
    dotProd = 0
    for j in range(len(v1)):
        dotProd += v1[j] * v2[j]
    #print dotProd
    return dotProd

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

            #print v1
            #print v2
       
            minDotProd = dotProduct(v1, v2)
            #v1Temp = list(v1)
            #v1Temp[-1] = v1[0]
            #print v1
            #print v1Temp
            
            loop = 0
            while loop < len(v1):
                v1Temp = list(v1)
                for k in range(0, len(v1)):
                    if k == len(v1) - 1:
                        v1Temp[-1] = v1[0]
                    else:
                        v1Temp[k] = v1[k + 1]
                #print v1Temp
                v1 = v1Temp
                dotProd = dotProduct(v1, v2)
                if dotProd < minDotProd:
                    minDotProd = dotProd
                loop += 1
            print minDotProd
            lineCount += 3
        

    
