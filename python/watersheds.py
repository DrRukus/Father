#!/usr/bin/env python

VALUE = 0
COORDINATES = 1
DIRECTIONS = ['north', 'west', 'east', 'south']
WATERSHEDS = 'abcdefghijklmnopqrstuvwxyz'

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
        self.isSink = None
        self.watershed = None

    def GetCoordinates(self):
        return self.iCrd, self.jCrd

    def IsSink(self):
        self.isSink = True
        for edge, data in self.edges.iteritems():
            if data[VALUE] < self.value and data[VALUE] != None:
                #print "{0}{1} is not a sink because {2} < {3}".format(self.iCrd, self.jCrd, data[VALUE], self.value)
                self.isSink = False
        #if self.isSink:
        #    print "{0}{1} is a sink".format(self.iCrd, self.jCrd)
        return self.isSink

    def GetEdges(self):
        return self.edges

    def SetEdgeValue(self, edge, value):
        self.edges[edge][VALUE] = value

    def SetEdgeCoordinates(self, edge, coordinates):
        self.edges[edge][COORDINATES] = coordinates

    def GetDrainDirection(self):
        return self.drain

    def DrainI(self):
        return None if self.drain == 'DNE' else int(self.edges[self.drain][1][0])

    def DrainJ(self):
        return None if self.drain == 'DNE' else int(self.edges[self.drain][1][1])

    def GetWatershed(self):
        return self.watershed

    def SetWatershed(self, watershed):
        self.watershed = watershed

    def _SetLowestDirection(self, index):
        return self.edges[DIRECTIONS[index]][VALUE], DIRECTIONS[index]

    def FindDrain(self):
        lowestDir = None
        for index in range(0, len(DIRECTIONS)):
            if self.edges[DIRECTIONS[index]][VALUE] == None:
                continue
            else:
                if self.isSink:
                    self.drain = 'DNE'
                    break
                lowestNum, lowestDir = self._SetLowestDirection(index)
                for subIndex in range(index, len(DIRECTIONS)):
                    if self.edges[DIRECTIONS[subIndex]][VALUE] != None:
                        if self.edges[DIRECTIONS[subIndex]][VALUE] < lowestNum:
                            lowestNum, lowestDir = self._SetLowestDirection(subIndex)
                self.drain = lowestDir
            break


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
                #if i == 0 and j == 0:
                #    crd.SetWatershed('a')
                #else:
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

    def FindSink(self, i, j):
        if self.coordinates[i][j].IsSink():
            #print "This is a sink!"
            return None
        doneFlag = False
        maxLoops = self.dims['height'] * self.dims['width']
        currentCell = self.coordinates[i][j]
        for _ in range(0, maxLoops):
            newCell = self.coordinates[currentCell.DrainI()][currentCell.DrainJ()]
            currentCell = newCell
            if newCell.IsSink():
                break
        return newCell.GetCoordinates()
            

    def SetWatershedDrainCodes(self, cornerDrain, verbose = False):
        codeIndex = 0
        self.coordinates[0][0].SetWatershed(WATERSHEDS[codeIndex])
        if not cornerDrain:
            sinkI, sinkJ = self.FindSink(0, 0)
            self.coordinates[sinkI][sinkJ].SetWatershed(WATERSHEDS[codeIndex])
            if verbose:
                print "Watershed code for {0}, {1}: {2}".format(sinkI, sinkJ, WATERSHEDS[codeIndex])
        codeIndex += 1
        for i in range(0, self.dims['height']):
            for j in range(0, self.dims['width']):
                if i == 0 and j == 0:
                    continue
                else:
                    if self.coordinates[i][j].IsSink() and not self.coordinates[i][j].GetWatershed():
                        if verbose:
                            print "i = {0}; j = {1}".format(i, j)
                            print "    Code Index = {0}; Code = {1}".format(codeIndex, WATERSHEDS[codeIndex])
                        self.coordinates[i][j].SetWatershed(WATERSHEDS[codeIndex])
                        codeIndex += 1
                    

    def FindWatersheds(self):
        self.SetDrains(verbose = False)

        self.SetWatershedDrainCodes(self.coordinates[0][0].IsSink())

        for i in range(0, self.dims['height']):
            for j in range(0, self.dims['width']):
                drainI = self.coordinates[i][j].DrainI()
                drainJ = self.coordinates[i][j].DrainJ()
                if self.coordinates[i][j].GetDrainDirection() == 'DNE':
                    continue
                watershed = self.coordinates[drainI][drainJ].GetWatershed()
                if watershed:
                    self.coordinates[i][j].SetWatershed(watershed)
                                
matrix = 9
                  
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

watersheds = Map(mapVals[3])

watersheds.DisplayMap()
watersheds.DisplayWatersheds()

watersheds.FindWatersheds()

#sinkI, sinkJ = watersheds.FindSink(0, 0)

#print "i = {0}; j = {1}".format(sinkI, sinkJ)

watersheds.DisplayWatersheds()
