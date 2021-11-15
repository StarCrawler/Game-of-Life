import pygame as pg

def grid(newSize, newXPos, newYPos, newCellSize, newDisplay):
    for i in range(int(newSize[0] / newCellSize) + 1):
        newXPos = i*newCellSize
        newPos = newXPos, newYPos
        pg.draw.line(newDisplay, pg.Color(255, 255, 255), pg.math.Vector2(newXPos, newYPos), pg.math.Vector2(newXPos, newSize[1]))
    newXPos = 0
    for j in range(int(newSize[1] / newCellSize) + 1):
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

def addCell(newGrid, newMaxPrintGrid, newCellSize, newPos, newChoice):
    if pg.mouse.get_pressed()[0] and newPos[1] <= newMaxPrintGrid[1]:
        posGrid = (int(newPos[0]/newCellSize), int(newPos[1]/newCellSize))
        if newGrid[posGrid[1]][posGrid[0]] == 0 and newChoice == "Add":
            newGrid[posGrid[1]][posGrid[0]] = 1
        elif newChoice == "Remove":
            newGrid[posGrid[1]][posGrid[0]] = 0
