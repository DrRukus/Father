#!/usr/bin/env python

class Coordinate(object):

    def __init__(self, i, j):
        self.iCrd = i
        self.jCrd = j
        self.edges = {'north': None,
                      'south': None,
                      'east': None,
                      'west': None}
        self.drain = None
        self.watershed = None

    def GetCoordinates(self):
        return self.iCrd, self.jCrd

    def DisplayEdges(self):
        print self.edges

    def SetEdge(self, edge, value):
        self.edges[edge] = value

    def GetWatershed(self):
        return self.watershed

    def SetWatershed(self, watershed):
        self.watershed = watershed

class WaterSheds(object):

    def __init__(self, mapVals):
        #self.watersheds = []
        self.mapVals = mapVals
        self.dims = {'height': len(self.mapVals),
                     'width':  len(self.mapVals[0])}

        self.coordinates = []

        for i in range(0, self.dims['height']):
            tempRow = []
            for j in range(0, self.dims['width']):
                crd = Coordinate(i, j)
                if i == 0 and j == 0:
                    crd.SetWatershed('a')
                else:
                    crd.SetWatershed(None)
                tempRow.append(crd)
            self.coordinates.append(tempRow)

    def DisplayMap(self):
        for row in self.mapVals:
            print row

    def DisplayWatersheds(self):
        for row in self.coordinates:
            print str(row[0].GetWatershed()) + \
                  " " + str(row[1].GetWatershed()) + \
                  " " + str(row[2].GetWatershed())

    def GetValue(self, i, j):
        return self.watersheds[i][j]

    #def GetLowestPoints(self):
    #    lowestPoints = []
    #    for i in range(0, dims['height']):
    #        for j in range(1, dims['width']):
                

    def FindWatersheds(self):

        directionWeight = ['north', 'west', 'east', 'south']

        coordinates = []

        for i in range(0, self.dims['height']):
            for j in range(0, self.dims['width']):
                edges = {'north': None,
                         'south': None,
                         'east': None,
                         'west': None}

                crd = Coordinate(i, j)    

                # Get values of sides
                if j == 0:
                    crd.SetEdge('east', self.mapVals[i][j + 1])
                elif j == self.dims['width'] - 1:
                    crd.SetEdge('west', self.mapVals[i][j - 1])
                else:
                    crd.SetEdge('east', self.mapVals[i][j + 1])
                    crd.SetEdge('west', self.mapVals[i][j - 1])

                # Get values of top and bottom
                if i == 0:
                    crd.SetEdge('south', self.mapVals[i + 1][j])
                elif i == self.dims['height'] - 1:
                    crd.SetEdge('north', self.mapVals[i - 1][j])
                else:
                    crd.SetEdge('north', self.mapVals[i - 1][j])
                    crd.SetEdge('south', self.mapVals[i + 1][j])

                #print "i: {0}; j: {1}".format(i, j)
                crd.DisplayEdges()

                drain = None
                #for direction in directionWeight:
                    
                #coordinates
                                
                    
mapVals = [[9, 6, 3],
           [5, 9, 6],
           [3, 5, 9]]

#mapVals = [[1, 2, 3, 4, 5],
#           [2, 9, 3, 9, 6],
#           [3, 3, 0, 8, 7],
#           [4, 9, 8, 9, 8],
#           [5, 6, 7, 8, 9]]

watersheds = WaterSheds(mapVals)

watersheds.DisplayMap()
watersheds.DisplayWatersheds()

watersheds.FindWatersheds()

watersheds.DisplayWatersheds()
