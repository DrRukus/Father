#!/usr/bin/env python

grid = [['.', '.', '.'],
        ['+', '+', '+'],
        ['x', '.', '.']]

#grid = [['+', '.', 'x'],
#        ['+', 'x', '+'],
#        ['o', '.', '.']]

# grid = [['.', '.', '.'],
#        ['.', '+', 'o'],
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
            self.score = 0
            self.diagNum = self.dims * 2 - 1
            self.numberOfCells = self.dims ** 2
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

    def setCell(self, i, j, value):
        self.grid[i][j] = value

    def getNumberOfCells(self):
        return self.numberOfCells

    def printGrid(self):
        for row in self.grid:
            print(' '.join(row))

    def getGridCopy(self):
        return self.grid[:]

    def getScore(self):
        score = 0
        for row in self.grid:
            for cell in row:
                score += self.scores[cell]
        print(score)
        self.score = score
        return self.score

    def check(self, cells, rule='updwn'):
        assert rule == 'updwn' or rule == 'diag'
        count = 0
        for cell in cells:
            if rule == 'updwn':
                if cell == 'x' or cell == 'o':
                    count += 1
            else:
                if cell == '+' or cell == 'o':
                   count += 1
        return False if count > 1 else True

    def checkRowsAndCols(self):
        violation = False
        for i in range(self.dims):
            if not (self.check(self.getRow(i)) and 
                    self.check(self.getCol(i))):
                print("\nUp/Down rule broken!")
                violation = True
                break
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

    def getDiagonal(self, ind, direction):
        """
        Diagonals are indexed as follows:
        * if direction is right, index 0 is lower left corner, 
            highest index is upper right corner
        * if direction is left, lowest index is upper left corner,
            highest index is lower right corner
        """
        diagArr = []
        if direction == 'right':
            if ind <= self.maxInd:
                coord = [self.maxInd - ind, 0]
            else:
                coord = [0, ind - self.maxInd]
            for i in range(self.diagNum):
                diagArr.append(self.grid[coord[0]][coord[1]])
                coord = self.getNextDiagCoord(coord, direction)
                if coord[0] == -1 or coord[1] == -1:
                    break
        elif direction == 'left':
            if ind <= self.maxInd:
                coord = [self.maxInd - ind, self.maxInd]
            else:
                coord = [0, 2 * self.maxInd - ind]
            for i in range(self.diagNum):
                diagArr.append(self.grid[coord[0]][coord[1]])
                coord = self.getNextDiagCoord(coord, direction)
                if coord[0] == -1 or coord[1] == -1:
                    break
        return diagArr

    def checkDiagonals(self):
        violation = False
        for i in range(self.diagNum):
            leftDiag = self.getDiagonal(i, 'left')
            rightDiag = self.getDiagonal(i, 'right')
            if not (self.check(leftDiag, rule='diag') and
                    self.check(rightDiag, rule='diag')):
                print("Diagonal rule broken!")
                violation = True
                break
        return violation

    def checkRules(self):
        violation = False
        if self.checkRowsAndCols() or self.checkDiagonals():
            violation = True
            print("Violation detected!\n")
        return violation

    def mapIndexToCoords(self, index):
        assert index <= self.numberOfCells - 1
        return index // self.dims, index % self.dims

    def mapCoordsToIndex(self, coords):
        pass

def main():
    fs = FashionShow(grid)

    fs.printGrid()
    fs.getScore()

    # print(fs.getNextDiagCoord([1, 2], 'right'))

    print('Rule violation? {}\n\n'.format(fs.checkRules()))
    print(fs.mapIndexToCoords(8))
    for cellNum in range(fs.getNumberOfCells()):
        i, j = fs.mapIndexToCoords(cellNum)
        cell = fs.getCell(i, j)
        print(cell)
        if cell == 'o':
            continue
        else:
            order = iter(['o', '+', 'x'])
            score = fs.getScore()
            initVal = fs.getCell(i, j)
            while True:
                try:
                    fs.setCell(i, j, next(order))
                except StopIteration:
                    fs.setCell(i, j, initVal)
                    break
                if not fs.checkRules():
                    break
            if fs.getScore() <= score:
                fs.setCell(i, j, initVal)
    fs.printGrid()

main()