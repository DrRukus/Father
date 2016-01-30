#!/usr/bin/env python

with open("inputFiles/revWordsInput.txt") as inputfile:
    inputLines = inputfile.readlines()

    caseCount = int(inputLines[0])

    for count in range(1, caseCount + 1):
        wordList = inputLines[count].rstrip().split(" ")
        #print wordList        
        newWordList = []
        lengthOfList = len(wordList)
        #print "Length of list: {0}".format(str(lengthOfList))
        for i in range(0, lengthOfList):
            #print "Index: {0}; Length of List - Index: {1}".format(i, lengthOfList - i - 1)
            newWordList.append(wordList[lengthOfList - i - 1])

        print "Case #{0}: {1}".format(count, " ".join(newWordList))
