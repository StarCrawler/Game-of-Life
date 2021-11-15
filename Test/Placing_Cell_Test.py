import sys
import pygame as pg
import numpy as np

pg.init()

displaySize = width, height = 720, 576
maxPrintGrid = [width, height - 100]
xPosGridLine = 0
yPosGridLine = 0
cellSize = 10
gridSize = [int(maxPrintGrid[1]/cellSize), int(width/cellSize)]
grid = np.zeros(gridSize)

screen = pg.display.set_mode(displaySize)


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

def addCell(newGrid, newMaxPrintGrid, newCellSize, newPos):
    if pg.mouse.get_pressed()[0]:
        posGrid = (int(newPos[0]/newCellSize), int(newPos[1]/newCellSize))
        if newGrid[posGrid[1]][posGrid[0]] == 0:
            newGrid[posGrid[1]][posGrid[0]] == 1
        else:
            newGrid[posGrid[1]][posGrid[0]] == 0



while True:
    printCell(grid, gridSize, screen, cellSize)
    grid(maxPrintGrid,xPosGridLine, yPosGridLine ,cellSize,screen)
    addCell(grid, maxPrintGrid, cellSize, pg.mouse.get_pos())
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
             sys.exit(0)
