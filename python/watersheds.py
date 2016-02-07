#!/usr/bin/env python

DIRECTIONS = ['north', 'west', 'east', 'south']

class Coordinate(object):

    def __init__(self, i, j, value):
        self.iCrd = i
        self.jCrd = j
        self.value = value
        self.edges = {'north': None,
                      'south': None,
                      'east':  None,
                      'west':  None}
        self.drain = None
        self.isSink = True
        #self.IsSink()
        #print "Is a sink: {0}".format(self.isSink)
        self.watershed = None

    def GetCoordinates(self):
        return self.iCrd, self.jCrd

    def IsSink(self):
        for edge, elevation in self.edges.iteritems():
            if elevation < self.value:
                #print "Edge: {0}; Elevation: {1}; Value: {2}".format(edge, elevation, self.value)
                self.isSink = False
        #print "{0}, {1} is a sink: {2}".format(self.iCrd, self.jCrd, self.isSink)
        return self.isSink

    def DisplayEdges(self):
        print self.edges

    def SetEdge(self, edge, value):
        self.edges[edge] = value

    def GetDrain(self):
        return self.drain

    def GetWatershed(self):
        return self.watershed

    def SetWatershed(self, watershed):
        self.watershed = watershed

    def FindDrain(self):
        lowestDir = None
        for index in range(0, len(DIRECTIONS)):
            if not self.edges[DIRECTIONS[index]]:
                continue
            else:
                if self.isSink:
                    self.drain = 'DNE'
                    break
                lowestNum = self.edges[DIRECTIONS[index]]
                #print "Lowest Num Init: {0}".format(lowestNum)
                lowestDir = DIRECTIONS[index]
                for subIndex in range(index, len(DIRECTIONS)):
                    #print "Index: {0}; SubIndex: {1}".format(index, subIndex)
                    if self.edges[DIRECTIONS[subIndex]]:
                        if self.edges[DIRECTIONS[subIndex]] < lowestNum:
                            lowestNum = self.edges[DIRECTIONS[subIndex]]
                            lowestDir = DIRECTIONS[subIndex]
            break
        self.drain = lowestDir
        

class Map(object):

    def __init__(self, mapVals):
        self.mapVals = mapVals
        self.dims = {'height': len(self.mapVals),
                     'width':  len(self.mapVals[0])}

        self.coordinates = []

        for i in range(0, self.dims['height']):
            tempRow = []
            for j in range(0, self.dims['width']):
                crd = Coordinate(i, j, mapVals[i][j])
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
            printRow = []
            for index in range(0, len(row)):
                  #if row[index]:
                  print row[index].GetWatershed(),
                  print " ",
            print

    #def GetLowestPoints(self):
    #    lowestPoints = []
    #    for i in range(0, dims['height']):
    #        for j in range(1, dims['width']):

    def SetEdges(self, i, j):
        if j == 0:
            self.coordinates[i][j].SetEdge('east', self.mapVals[i][j + 1])
        elif j == self.dims['width'] - 1:
            self.coordinates[i][j].SetEdge('west', self.mapVals[i][j - 1])
        else:
            self.coordinates[i][j].SetEdge('east', self.mapVals[i][j + 1])
            self.coordinates[i][j].SetEdge('west', self.mapVals[i][j - 1])

        # Get values of north and south
        if i == 0:
            self.coordinates[i][j].SetEdge('south', self.mapVals[i + 1][j])
        elif i == self.dims['height'] - 1:
            self.coordinates[i][j].SetEdge('north', self.mapVals[i - 1][j])
        else:
            self.coordinates[i][j].SetEdge('south', self.mapVals[i + 1][j])
            self.coordinates[i][j].SetEdge('north', self.mapVals[i - 1][j])

        self.coordinates[i][j].IsSink()

    def FindWatersheds(self):

        directionWeight = ['north', 'west', 'east', 'south']

        #coordinates = []

        for i in range(0, self.dims['height']):
            for j in range(0, self.dims['width']):

                linearIndex = j + len(self.mapVals[0]) * i

                # Get values of east and west
                self.SetEdges(i, j)
                

                #print "i: {0}; j: {1}".format(i, j)
                #self.coordinates[i][j].DisplayEdges()

                #drain = None
                self.coordinates[i][j].FindDrain() 
                #for direction in directionWeight:
                print self.coordinates[i][j].GetDrain()    
                #coordinates
                                
                    
mapVals = [[9, 6, 3],
           [5, 9, 6],
           [3, 5, 9]]

#mapVals = [[1, 2, 3, 4, 5],
#           [2, 9, 3, 9, 6],
#           [3, 3, 0, 8, 7],
#           [4, 9, 8, 9, 8],
#           [5, 6, 7, 8, 9]]

watersheds = Map(mapVals)

watersheds.DisplayMap()
watersheds.DisplayWatersheds()

watersheds.FindWatersheds()

watersheds.DisplayWatersheds()
