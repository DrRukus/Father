#!/usr/bin/env python

grid = [['.', '.', '.'],
        ['+', '+', '+'],
        ['x', '.', '.']]

#grid = [['+', '.', 'x'],
#        ['+', 'x', '+'],
#        ['o', '.', '.']]

#grid = [['.', '.', '.'],
#        ['x', '+', 'o'],
#        ['.', '+', '.']]

class FashionShow:
    def __init__(self, grid):
        for row in grid:
            if len(row) != len(grid):
                raise Exception("Grid must be a square!!")
        else:
            self.grid = grid
            self.dims = len(grid)
            self.maxInd = self.dims - 1
            self.currentRow = 0
            self.currentCol = 0
            self.score = 0
            self.diagNum = self.dims * 2 - 1
            self.scores = {'.': 0,
                           '+': 1,
                           'x': 1,
                           'o': 2}

    def getRow(self, rowNum):
        return self.grid[rowNum]

    def getCol(self, colNum):
        return [row[colNum] for row in self.grid]

    def getCell(self, i, j):
        return self.grid[i][j]

    def printGrid(self):
        for row in self.grid:
            print(' '.join(row))

    def getScore(self):
        score = 0
        for row in self.grid:
            for cell in row:
                score += self.scores[cell]
        print(score)
        self.score = score

    def checkUpDown(self, array):
        nonPlusCount = 0
        for cell in array:
            if cell == 'x' or cell == 'o':
                nonPlusCount += 1
        return False if nonPlusCount > 1 else True

    def checkRowsAndCols(self):
        violation = False
        for i in range(self.dims):
            if not (self.checkUpDown(self.getRow(i)) and 
                    self.checkUpDown(self.getCol(i))):
                violation = True
        return violation

    def getNextDiagCoord(self, ptr, direction):
        newPtr = ptr
        if direction == 'left':
            if ptr[0] < self.maxInd and ptr[1] > 0:
                newPtr = newPtr[0] + 1, newPtr[1] - 1
            else:
                newPtr = -1, -1
        elif direction == 'right':
            if ptr[0] < self.maxInd and ptr[1] < self.maxInd:
                newPtr = newPtr[0] + 1, newPtr[1] + 1
            else:
                newPtr = -1, -1
        return newPtr

    def getDiagonal(self, index, direction):
        """
        Diagonals are indexed as follows:
        * if direction is right, index 0 is lower left corner, 
            highest index is upper right corner
        * if direction is left, lowest index is upper left corner,
            highest index is lower right corner
        """
        diagArr = []
        if direction == 'right':
            if index <= self.maxInd:
                coord = [self.maxInd - index, 0]
            else:
                coord = [0, index - self.maxInd]
            for i in range(self.diagNum):
                diagArr.append(self.grid[coord[0]][coord[1]])
                coord = self.getNextDiagCoord(coord, direction)
                if coord[0] == -1 or coord[1] == -1:
                    break
        elif direction == 'left':
            if index <= self.maxInd:
                coord = [self.maxInd - index, self.maxInd]
            else:
                coord = [0, 2 * self.maxInd - index]
            for i in range(self.diagNum):
                diagArr.append(self.grid[coord[0]][coord[1]])
                coord = self.getNextDiagCoord(coord, direction)
                if coord[0] == -1 or coord[1] == -1:
                    break
        print(diagArr)

    def checkDiagonals(self):
        violation = False
        for i in range(self.diagNum):
            self.getDiagonal(i, 'left')
        return violation

    def checkRules(self):
        violation = False
        if self.checkRowsAndCols() or self.checkDiagonals():
            violation = True
            print("Violation detected!")
        return violation

fs = FashionShow(grid)

fs.printGrid()
print(fs.getRow(1))
print(fs.getCol(1))
fs.getScore()

print(fs.getNextDiagCoord([1, 2], 'right'))

print('Rule violation? {}'.format(fs.checkRules()))
