import pygame as pg

def grid(newSize, newXPos, newYPos, newCellSize, newDisplay):
    for i in range(int(newSize[0] / newCellSize)):
        newXPos = i*newCellSize
        newPos = newXPos, newYPos
        pg.draw.line(newDisplay, pg.Color(255, 255, 255), pg.math.Vector2(newXPos, newYPos), pg.math.Vector2(newXPos, newSize[1]))
    newXPos = 0
    for j in range(int(newSize[1] / newCellSize)):
        newYPos = j*newCellSize
        newPos = newXPos, newYPos
        pg.draw.line(newDisplay, pg.Color(255, 255, 255), pg.math.Vector2(newXPos, newYPos), pg.math.Vector2(newSize[0], newYPos))

def printCell(newGrid, newGridSize, newDisplay, newCellSize):
    for y in range(newGridSize[0]):
        for x in range(newGridSize[1]):
            if newGrid[y][x] == 1:
                pg.draw.rect(newDisplay, pg.Color(255, 255, 255), pg.Rect(x*newCellSize, y*newCellSize, newCellSize, newCellSize))
            else:
                pg.draw.rect(newDisplay, pg.Color(0, 0, 0), pg.Rect(x*newCellSize, y*newCellSize, newCellSize, newCellSize))

def cell(newGrid):
    numOfAdjacentCell = 0
    saveGrid = newGrid.copy()
    h,w = newGrid.shape
    for y in range(1, h-1):
        for x in range(1, w - 1):
            numOfAdjacentCell = saveGrid[y-1][x-1:x+2].sum() + saveGrid[y+1][x-1:x+2].sum() + saveGrid[y][x-1] + saveGrid[y][x+1]
            if numOfAdjacentCell == 3 and saveGrid[y][x] == 0:
                newGrid[y][x] = 1
            elif (numOfAdjacentCell > 3 or numOfAdjacentCell < 2) and saveGrid[y][x] == 1:
                newGrid[y][x] = 0
            numOfAdjacentCell = 0
