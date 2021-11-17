import sys
import pygame as pg
import Placing_Cell_Test_Fonction as fct
import numpy as np
import csv

pg.init()

displaySize = width, height = 720, 580
maxPrintGrid = [width, height - 100]
xPosGridLine = 0
yPosGridLine = 0
cellSize = 10
gridSize = [int(maxPrintGrid[1]/cellSize), int(width/cellSize)]
grid = np.zeros(gridSize)

screen = pg.display.set_mode(displaySize)

SaveButton = fct.Button("Save" , pg.Color(100,100,100), 80, height-75, screen)
LoadButton = fct.Button("Load" , pg.Color(100,100,100), 350, height-75, screen)

while True:
    """
    SaveButton.printButton()
    SaveButton.isHoover()

    LoadButton.printButton()
    LoadButton.isHoover()

    fct.printCell(grid, gridSize, screen, cellSize)
    fct.grid(maxPrintGrid, xPosGridLine, yPosGridLine , cellSize, screen)
    """
    fct.csvLoad()
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
             sys.exit(0)
