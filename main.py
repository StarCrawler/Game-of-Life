import sys
import pygame as pg
import Game_of_Life_Fonction as fct
import Game_of_Life_Class as cs
import numpy as np
#import time

pg.init()

displaySize = width, height = 720, 580
maxPrintGrid = [width, height - 100]
xPosGridLine = 0
yPosGridLine = 0
cellSize = 10
gridSize = [int(maxPrintGrid[1]/cellSize), int(width/cellSize)]
grid = np.zeros(gridSize)
simulating = False
modificationType = ""
icon = pg.image.load("logo.png")


screen = pg.display.set_mode(displaySize)
pg.display.set_icon(icon)
pg.display.set_caption("Game of Life")

grid[5][1] = 1
grid[6][1] = 1
grid[5][2] = 1
grid[6][2] = 1
grid[5][11] = 1
grid[6][11] = 1
grid[7][11] = 1
grid[4][12] = 1
grid[3][13] = 1
grid[3][14] = 1
grid[8][12] = 1
grid[9][13] = 1
grid[9][14] = 1
grid[6][15] = 1
grid[4][16] = 1
grid[8][16] = 1
grid[5][17] = 1
grid[6][17] = 1
grid[7][17] = 1
grid[6][18] = 1
grid[5][21] = 1
grid[4][21] = 1
grid[3][21] = 1
grid[3][22] = 1
grid[4][22] = 1
grid[5][22] = 1
grid[2][23] = 1
grid[6][23] = 1
grid[1][25] = 1
grid[2][25] = 1
grid[6][25] = 1
grid[7][25] = 1
grid[3][35] = 1
grid[4][35] = 1
grid[3][36] = 1
grid[4][36] = 1

#print(grid)

AddButton = cs.Button("Add", pg.Color(100,100,100), 50, height-75, screen)
RemoveButton = cs.Button("Remove", pg.Color(100,100,100), 320, height-75, screen)
SimulateButton = cs.Button("Simulate", pg.Color(100,100,100), 600, height-75, screen)
StopSimulateButton = cs.Button("Stop Simulation", pg.Color(100,100,100), 550, height-75, screen)
ClearButton = cs.Button("Clear Grid", pg.Color(100,100,100), 150, height-75, screen)

while True:
    screen.fill(pg.Color(225,225,225))

    AddButton.printButton()
    AddButton.isHoover()

    RemoveButton.printButton()
    RemoveButton.isHoover()

    if simulating == False:
        SimulateButton.printButton()
        SimulateButton.isHoover()

        ClearButton.printButton()
        ClearButton.isHoover()
    if simulating == True:
        StopSimulateButton.printButton()
        StopSimulateButton.isHoover()
        fct.cell(grid)

    fct.printCell(grid, gridSize, screen, cellSize)
    fct.grid(maxPrintGrid,xPosGridLine, yPosGridLine ,cellSize,screen)

    pg.display.flip()

    for event in pg.event.get():
        if simulating == False and SimulateButton.isClicked() == True:
            simulating = True
        if simulating == True and StopSimulateButton.isClicked() == True:
            simulating = False

        if simulating == False and ClearButton.isClicked() == True:
            grid = np.zeros(gridSize)

        if AddButton.isClicked():
            modificationType = "Add"
        elif RemoveButton.isClicked():
            modificationType = "Remove"

        if simulating == False:
            fct.addCell(grid, maxPrintGrid, cellSize, pg.mouse.get_pos(), modificationType)

        if event.type == pg.QUIT:
             sys.exit(0)
