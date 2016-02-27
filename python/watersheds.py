#!/usr/bin/env python

import map
"""
matrix = 1
                  
mapVals = [[[9, 6, 3],
            [5, 9, 6],
            [3, 5, 9]],
           [[1, 2, 3, 4, 5],
            [2, 9, 3, 9, 6],
            [3, 3, 0, 8, 7],
            [4, 9, 8, 9, 8],
            [5, 6, 7, 8, 9]],
           [[7, 6, 7],
            [7, 6, 7]],
           [[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
            [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]]]
"""

with open("inputFiles/B-large-practice.in") as inputFile:
#with open("inputFiles/map_test") as inputFile:
    inputLines = inputFile.readlines()

    numOfMaps = int(inputLines[0])

    print numOfMaps

    lineNum = 1

    # Read in all map values
    for index in range(0, numOfMaps):
        dims = inputLines[lineNum].split(" ")
        numRows = int(dims[0])
        numCols = int(dims[1])
            
        print "Rows: {0}; Cols: {1}".format(numRows, numCols)

        mapVals = []
        for rowNum in range(lineNum + 1, lineNum + numRows + 1):
            mapVals.append(inputLines[rowNum].rstrip().split(" "))

        map0 = map.Map(mapVals)
        map0.DisplayMap()
        map0.FindWatersheds()
        map0.DisplayWatersheds()

        lineNum += numRows + 1

"""
map0 = map.Map(mapVals[matrix])

map0.DisplayMap()
#map0.DisplayWatersheds()

map0.FindWatersheds()

map0.DisplayWatersheds()
"""
