import sys
import pygame as pg
import Placing_Cell_Test_Fonction as fct
import numpy as np

pg.init()

displaySize = width, height = 720, 580
maxPrintGrid = [width, height - 100]
xPosGridLine = 0
yPosGridLine = 0
cellSize = 10
gridSize = [int(maxPrintGrid[1]/cellSize), int(width/cellSize)]
grid = np.zeros(gridSize)

screen = pg.display.set_mode(displaySize)

while True:
    fct.printCell(grid, gridSize, screen, cellSize)
    fct.grid(maxPrintGrid, xPosGridLine, yPosGridLine , cellSize, screen)
    pg.display.flip()
    for event in pg.event.get():
        fct.addCell(grid, maxPrintGrid, cellSize, pg.mouse.get_pos(), "Add")
        if event.type == pg.QUIT:
             sys.exit(0)
