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


def csvLoad():
    documentName = int(input("Enter CSV File name : "))
    return documentName



class Button(object):
    """docstring for Button."""


    def __init__(self, Name, Color, XPos, YPos, Display):
        self.hisName = Name
        self.startColor = Color
        self.hisColor = 0
        self.hisWidth = 0
        self.hisHeight = 0
        self.hisX = XPos
        self.hisY = YPos
        self.hisDisplay = Display
        self.buttonFont = pg.font.SysFont('Comic sans MS', 20)


    def printButton(self):
        text = self.buttonFont.render(self.hisName, True, pg.Color(0, 0, 0))
        self.hisWidth = text.get_rect()[2] + 20
        self.hisHeight = text.get_rect()[3] + 20
        pg.draw.rect(self.hisDisplay, self.hisColor, pg.Rect(self.hisX, self.hisY, self.hisWidth, self.hisHeight))
        self.hisDisplay.blit(text,(self.hisX + self.hisWidth/2 - text.get_rect()[2]/2,self.hisY + self.hisHeight/2 - text.get_rect()[3]/2))

    def isCollided(self,Pos):
        if Pos[0] >= self.hisX and Pos[0] <= self.hisX + self.hisWidth and Pos[1] >= self.hisY and Pos[1] <= self.hisY + self.hisHeight:
            return True

    def isClicked(self):
        if pg.mouse.get_pressed()[0] and self.isCollided(pg.mouse.get_pos()):
            screen.fill(pg.Color(0,0,0))

    def isHoover(self):
        if self.isCollided(pg.mouse.get_pos()):
            self.hisColor = pg.Color(200,200,200)
        else:
            self.hisColor = self.startColor
