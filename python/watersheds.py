#!/usr/bin/env python

drainCode = {0: 'a',
             1: 'b',
             2: 'c'}

#mapVals = [[9, 6, 3],
#           [5, 9, 6],
#           [3, 5, 9]]

mapVals = [[1, 2, 3, 4, 5],
           [2, 9, 3, 9, 6],
           [3, 3, 0, 8, 7],
           [4, 9, 8, 9, 8],
           [5, 6, 7, 8, 9]]

#dims = {'height': len(mapVals),
#        'width':  len(mapVals[0])}

#watersheds = []

class WaterSheds(object):

    def __init__(self, mapVals):
        self.watersheds = []
        self.mapVals = mapVals
        self.dims = {'height': len(self.mapVals),
                     'width':  len(self.mapVals[0])}
        for i in range(0, self.dims['height']):
            tempRow = []
            for j in range(0, self.dims['width']):
                tempRow.append(None)
            self.watersheds.append(tempRow)
    
        self.watersheds[0][0] = 'a'

    def DisplayMap(self):
        for row in self.mapVals:
            print row

    def DisplayWatersheds(self):
        for row in self.watersheds:
            print row

    def GetValue(self, i, j):
        return self.watersheds[i][j]

    #def GetLowestPoints(self):
    #    for i in range(

    def FindWatersheds(self):
        #edges = {'top': None,
        #         'bottom': None,
        #         'right': None,
        #         'left': None}

        for i in range(0, self.dims['height']):
            for j in range(1, self.dims['width']):
                edges = {'top': None,
                         'bottom': None,
                         'right': None,
                         'left': None}

                # Get values of sides
                if self.watersheds[i][j]:
                    continue
                if j == 0:
                    edges['right'] = self.mapVals[i][j + 1]
                elif j == self.dims['width'] - 1:
                    edges['left'] = self.mapVals[i][j - 1]
                else:
                    edges['right'] = self.mapVals[i][j + 1]
                    edges['left'] = self.mapVals[i][j - 1]

                # Get values of top and bottom
                if i == 0:
                    edges['right'] = self.mapVals[i + 1][j]
                elif i == self.dims['height'] - 1:
                    edges['left'] = self.mapVals[i - 1][j]
                else:
                    edges['right'] = self.mapVals[i + 1][j]
                    edges['left'] = self.mapVals[i + 1][j]

                drain = None
                #for side, value in edges:
                    
   
watersheds = WaterSheds(mapVals)

watersheds.DisplayMap()
watersheds.DisplayWatersheds()

watersheds.FindWatersheds()

watersheds.DisplayWatersheds()
