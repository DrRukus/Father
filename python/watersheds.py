#!/usr/bin/env python

VALUE = 0
COORDINATES = 1
DIRECTIONS = ['north', 'west', 'east', 'south']

class Coordinate(object):

    def __init__(self, i, j, value):
        self.iCrd = i
        self.jCrd = j
        self.value = value
        self.edges = {'north': [None, None],
                      'south': [None, None],
                      'east':  [None, None],
                      'west':  [None, None]}
        self.drain = None
        self.isSink = True
        #self.IsSink()
        #print "Is a sink: {0}".format(self.isSink)
        self.watershed = None

    def GetCoordinates(self):
        return self.iCrd, self.jCrd

    def IsSink(self):
        for edge, data in self.edges.iteritems():
            if data[VALUE] < self.value:
                #print "Edge: {0}; Elevation: {1}; Value: {2}".format(edge, elevation, self.value)
                self.isSink = False
        #print "{0}, {1} is a sink: {2}".format(self.iCrd, self.jCrd, self.isSink)
        return self.isSink

    def GetEdges(self):
        return self.edges

    def SetEdgeValue(self, edge, value):
        self.edges[edge][VALUE] = value
        #print "Edge: {0}; Value: {1}".format(edge, self.edges[edge][0])

    def SetEdgeCoordinates(self, edge, coordinates):
        self.edges[edge][COORDINATES] = coordinates

    def GetDrain(self):
        return self.drain

    def GetWatershed(self):
        return self.watershed

    def SetWatershed(self, watershed):
        self.watershed = watershed

    def FindDrain(self):
        lowestDir = None
        for index in range(0, len(DIRECTIONS)):
            #print "Starting drain search"
            #print self.edges[DIRECTIONS[index]][VALUE]
            if self.edges[DIRECTIONS[index]][VALUE] == None:
                #print "{0} does not exist".format(DIRECTIONS[index])
                continue
            else:
                #print "{0} exists".format(DIRECTIONS[index])
                if self.isSink:
                    self.drain = 'DNE'
                    break
                lowestNum = self.edges[DIRECTIONS[index]][VALUE]
                #print "Lowest Num Init: {0}".format(lowestNum)
                lowestDir = DIRECTIONS[index]
                for subIndex in range(index, len(DIRECTIONS)):
                    #print "Index: {0}; SubIndex: {1}".format(index, subIndex)
                    #print self.edges[DIRECTIONS[subIndex]][VALUE]
                    #print lowestNum
                    if self.edges[DIRECTIONS[subIndex]][VALUE]:
                        if self.edges[DIRECTIONS[subIndex]][VALUE] < lowestNum:
                            #print self.edges[DIRECTIONS[subIndex]][VALUE]
                            #print lowestNum
                            lowestNum = self.edges[DIRECTIONS[subIndex]][VALUE]
                            lowestDir = DIRECTIONS[subIndex]
            break
        #print "In function: {0}".format(lowestDir)
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
            for index in range(0, len(row)):
                  print row[index],
                  print " ",
            print

    def DisplayWatersheds(self):
        for row in self.coordinates:
            for index in range(0, len(row)):
                  print row[index].GetWatershed(),
                  print " ",
            print

    #def GetLowestPoints(self):
    #    lowestPoints = []
    #    for i in range(0, dims['height']):
    #        for j in range(1, dims['width']):

    def SetEdges(self, i, j, verbose = False):
        # Get values of east and west
        if j == 0:
            self.coordinates[i][j].SetEdgeValue('east', self.mapVals[i][j + 1])
            self.coordinates[i][j].SetEdgeCoordinates('east', str(i) + str(j + 1))
        elif j == self.dims['width'] - 1:
            self.coordinates[i][j].SetEdgeValue('west', self.mapVals[i][j - 1])
            self.coordinates[i][j].SetEdgeCoordinates('west', str(i) + str(j - 1))
        else:
            self.coordinates[i][j].SetEdgeValue('east', self.mapVals[i][j + 1])
            self.coordinates[i][j].SetEdgeValue('west', self.mapVals[i][j - 1])
            self.coordinates[i][j].SetEdgeCoordinates('east', str(i) + str(j + 1))
            self.coordinates[i][j].SetEdgeCoordinates('west', str(i) + str(j - 1))

        # Get values of north and south
        if i == 0:
            self.coordinates[i][j].SetEdgeValue('south', self.mapVals[i + 1][j])
            self.coordinates[i][j].SetEdgeCoordinates('south', str(i + 1) + str(j))
        elif i == self.dims['height'] - 1:
            self.coordinates[i][j].SetEdgeValue('north', self.mapVals[i - 1][j])
            self.coordinates[i][j].SetEdgeCoordinates('north', str(i - 1) + str(j))
        else:
            self.coordinates[i][j].SetEdgeValue('south', self.mapVals[i + 1][j])
            self.coordinates[i][j].SetEdgeValue('north', self.mapVals[i - 1][j])
            self.coordinates[i][j].SetEdgeCoordinates('south', str(i + 1) + str(j))
            self.coordinates[i][j].SetEdgeCoordinates('north', str(i - 1) + str(j))

        edges = self.coordinates[i][j].GetEdges()
        if verbose:
            for edge, data in edges.iteritems():
                print "Edge: {0}".format(edge)
                print "Value: {0}; Coordinates: {1}".format(data[VALUE], data[COORDINATES])

        self.coordinates[i][j].IsSink()

    def SetDrains(self, verbose = False):
        for i in range(0, self.dims['height']):
            for j in range(0, self.dims['width']):
                self.SetEdges(i, j)
                self.coordinates[i][j].FindDrain()
                if verbose:
                    print self.coordinates[i][j].GetDrain()

    def FindWatersheds(self):
        self.SetDrains(verbose = True)

#        for i in range(0, self.dims['height']):
#            for j in range(0, self.dims['width']):
                

        
        
                                
                    
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
