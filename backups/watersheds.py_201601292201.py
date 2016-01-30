#!/usr/bin/env python

drainCode = {0: 'a',
             1: 'b',
             2: 'c'}

mapVals = [[9, 6, 3],
           [5, 9, 6],
           [3, 5, 9]]

#mapVals = [[1, 2, 3, 4, 5],
#           [2, 9, 3, 9, 6],
#           [3, 3, 0, 8, 7],
#           [4, 9, 8, 9, 8],
#           [5, 6, 7, 8, 9]]

#dims = {'height': len(mapVals),
#        'width':  len(mapVals[0])}

#watersheds = []

class WaterSheds(object):

    def __init__(self, dims):
        self.watersheds = []
        self.dims = dims
        for i in range(0, self.dims['height']):
            tempRow = []
            for j in range(0, self.dims['width']):
                tempRow.append(None)
            self.watersheds.append(tempRow)
    
        self.watersheds[0][0] = 'a'

    def DisplayWatersheds(self):
        print self.watersheds

    def GetValue(self, i, j):
        return self.watersheds[i][j]
   
dims = {'height': len(mapVals),
        'width':  len(mapVals[0])}

watersheds = WaterSheds(dims)

watersheds.DisplayWatersheds()

sinks = []
edges = {'top': None,
         'bottom': None,
         'right': None,
         'left': None}

for i in range(0, dims['height']):
    for j in range(1, dims['width']):
        if watersheds.GetValue(i, j):
            continue
        #if (i == 0) or (i == dims['height'] - 1):
            
